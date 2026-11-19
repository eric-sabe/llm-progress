"""Build a static copy of the Streamlit app for GitHub Pages.

    python build_site.py            # writes ./site
    python -m http.server -d site   # preview at http://localhost:8000

How it works: app.py is run with a stand-in for the `streamlit` module that records
every call (markdown, charts, metrics, columns, widgets) instead of drawing it. The
script is run once for every combination of widget values on each tab, and each
recording is written out as HTML. A few lines of JavaScript switch between the
pre-rendered combinations when a control changes.

app.py therefore stays the single source of truth: change a chart or a sentence there
and both the Streamlit app and the static site pick it up. If app.py starts using a
Streamlit call this file does not know, the build fails with the name of the call.
"""
from __future__ import annotations

import html
import itertools
import json
import re
import runpy
import shutil
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "site"
REPO_URL = "https://github.com/eric-sabe/llm-progress"


# ── Recording stand-in for streamlit ─────────────────────────────────────────
class Node:
    def __init__(self, kind, **props):
        self.kind = kind
        self.props = props
        self.children: list[Node] = []


class Container(Node):
    """A node that can hold others and be used as `with container:`."""

    def __init__(self, rec, kind, **props):
        super().__init__(kind, **props)
        self._rec = rec

    def __enter__(self):
        self._rec.stack.append(self)
        return self

    def __exit__(self, *exc):
        self._rec.stack.pop()
        return False

    # content
    def _add(self, node):
        self.children.append(node)
        return node

    def markdown(self, body, unsafe_allow_html=False, **_):
        self._add(Node("markdown", body=str(body), raw=unsafe_allow_html))

    def divider(self):
        self._add(Node("divider"))

    def info(self, body, **_):
        self._add(Node("info", body=str(body)))

    def caption(self, body, **_):
        self._add(Node("caption", body=str(body)))

    def metric(self, label, value, delta=None, **_):
        self._add(Node("metric", label=str(label), value=str(value), delta=delta))

    def plotly_chart(self, fig, **_):
        self._add(Node("plot", fig=fig.to_json()))

    # layout
    def tabs(self, labels):
        group = self._add(Node("tabs"))
        tabs = [Container(self._rec, "tab", label=lab) for lab in labels]
        group.children.extend(tabs)
        return tabs

    def columns(self, spec, **_):
        weights = [1] * spec if isinstance(spec, int) else list(spec)
        group = self._add(Node("columns"))
        cols = [Container(self._rec, "column", weight=w) for w in weights]
        group.children.extend(cols)
        return cols

    # widgets: return the value assigned for this run, and leave a marker in place
    def _widget(self, kind, label, options, default, key, show_label):
        wid = key or label
        tab = next((c for c in reversed(self._rec.stack) if c.kind == "tab"), None)
        value = self._rec.assign.get(wid, default)
        self._add(Node("widget", wid=wid, widget=kind, label=label, options=list(options),
                       value=value, show_label=show_label))
        self._rec.widgets.setdefault(wid, dict(options=list(options), default=default,
                                               tab=tab.props["label"] if tab else None))
        return value

    def radio(self, label, options, index=0, key=None, label_visibility="visible", **_):
        options = list(options)
        return self._widget("radio", label, options, options[index], key, label_visibility == "visible")

    def selectbox(self, label, options, index=0, key=None, label_visibility="visible", **_):
        options = list(options)
        return self._widget("select", label, options, options[index], key, label_visibility == "visible")

    def checkbox(self, label, value=False, key=None, **_):
        return self._widget("checkbox", label, [False, True], bool(value), key, True)


class Recorder:
    def __init__(self, assign):
        self.assign = assign
        self.widgets: dict[str, dict] = {}
        self.page_title = ""
        self.root = Container(self, "root")
        self.stack = [self.root]

    def module(self):
        rec = self
        mod = types.ModuleType("streamlit")

        def set_page_config(page_title="", **_):
            rec.page_title = page_title

        def cache_data(func=None, **_):
            return func if callable(func) else (lambda f: f)

        mod.set_page_config = set_page_config
        mod.cache_data = cache_data

        def __getattr__(name):
            top = rec.stack[-1]
            if hasattr(top, name):
                return getattr(top, name)
            raise AttributeError(
                f"build_site.py does not support st.{name}; add it to Container in build_site.py"
            )

        mod.__getattr__ = __getattr__
        return mod


def record(assign=None) -> Recorder:
    rec = Recorder(assign or {})
    real = sys.modules.get("streamlit")
    sys.modules["streamlit"] = rec.module()
    try:
        runpy.run_path(str(ROOT / "app.py"), run_name="__main__")
    finally:
        if real is not None:
            sys.modules["streamlit"] = real
        else:
            del sys.modules["streamlit"]
    return rec


# ── HTML rendering ───────────────────────────────────────────────────────────
def inline_md(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text, flags=re.S)
    return re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text, flags=re.S)


def block_md(text: str) -> str:
    out = []
    for para in re.split(r"\n\s*\n", text.strip()):
        m = re.match(r"(#{1,6})\s+(.*)", para, flags=re.S)
        if m:
            level = len(m.group(1))
            out.append(f"<h{level}>{inline_md(m.group(2))}</h{level}>")
        else:
            out.append(f"<p>{inline_md(para)}</p>")
    return "\n".join(out)


class Renderer:
    def __init__(self):
        self.n = 0

    def uid(self, prefix):
        self.n += 1
        return f"{prefix}{self.n}"

    def render(self, node: Node) -> str:
        return getattr(self, f"r_{node.kind}")(node)

    def children(self, node):
        return "\n".join(self.render(c) for c in node.children)

    def r_markdown(self, n):
        return n.props["body"] if n.props["raw"] else block_md(n.props["body"])

    def r_divider(self, n):
        return "<hr>"

    def r_info(self, n):
        return f'<div class="info">{block_md(n.props["body"])}</div>'

    def r_caption(self, n):
        return f'<div class="caption">{block_md(n.props["body"])}</div>'

    def r_metric(self, n):
        delta = n.props["delta"]
        delta_html = f'<div class="m-delta">{html.escape(str(delta))}</div>' if delta else ""
        return (f'<div class="metric"><div class="m-label">{html.escape(n.props["label"])}</div>'
                f'<div class="m-value">{html.escape(n.props["value"])}</div>{delta_html}</div>')

    def r_plot(self, n):
        fid = self.uid("fig")
        payload = n.props["fig"].replace("</", "<\\/")
        return (f'<div class="plot" data-fig="{fid}"></div>'
                f'<script type="application/json" id="{fid}">{payload}</script>')

    def r_columns(self, n):
        cols = "".join(
            f'<div class="col" style="flex:{c.props["weight"]} 1 0">{self.children(c)}</div>'
            for c in n.children
        )
        return f'<div class="cols">{cols}</div>'

    def r_widget(self, n):
        p = n.props
        wid = html.escape(p["wid"], quote=True)
        own = html.escape(json.dumps(p["value"]), quote=True)
        label = f'<div class="w-label">{html.escape(p["label"])}</div>' if p["show_label"] else ""
        if p["widget"] == "radio":
            name = self.uid("r")
            opts = "".join(
                f'<label><input type="radio" name="{name}" value="{html.escape(json.dumps(o), quote=True)}"'
                f'{" checked" if o == p["value"] else ""}><span>{html.escape(str(o))}</span></label>'
                for o in p["options"]
            )
            body = f'<div class="radio">{opts}</div>'
        elif p["widget"] == "select":
            opts = "".join(
                f'<option value="{html.escape(json.dumps(o), quote=True)}"'
                f'{" selected" if o == p["value"] else ""}>{html.escape(str(o))}</option>'
                for o in p["options"]
            )
            body = f"<select>{opts}</select>"
        else:
            body = (f'<label class="check"><input type="checkbox"{" checked" if p["value"] else ""}>'
                    f'<span>{html.escape(p["label"])}</span></label>')
            label = ""
        return f'<div class="widget" data-wid="{wid}" data-kind="{p["widget"]}" data-own="{own}">{label}{body}</div>'


CSS = """
:root { --bg:#0e1117; --panel:#1a1d27; --line:#2d2d2d; --text:#d0d0d0; --muted:#888; --accent:#10a37f; }
* { box-sizing:border-box; }
html { background:var(--bg); }
body { margin:0; background:var(--bg); color:var(--text);
  font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:16px; line-height:1.55; }
main { max-width:1400px; margin:0 auto; padding:2rem 3rem 1rem; }
h1 { font-size:2rem; font-weight:700; letter-spacing:-0.5px; margin:0 0 .4rem; color:#fafafa; }
h3 { font-size:1.6rem; font-weight:600; margin:1.2rem 0 .6rem; color:#fafafa; }
h5 { font-size:1.05rem; font-weight:600; margin:1.6rem 0 .6rem; color:#e6e6e6; }
p { margin:.5rem 0 .9rem; }
a { color:#4c8ef5; }
.subtitle { color:var(--muted); font-size:1rem; margin:0 0 1.2rem; }
hr { border:0; border-top:1px solid var(--line); margin:.8rem 0 1.4rem; }
nav { display:flex; flex-wrap:wrap; gap:4px; border-bottom:1px solid var(--line); margin-bottom:1rem; }
nav a { padding:10px 9px; color:var(--muted); text-decoration:none; font-weight:500; font-size:.94rem;
  border-bottom:2px solid transparent; margin-bottom:-1px; white-space:nowrap; }
nav a:hover { color:#e0e0e0; }
nav a.active { color:#e0e0e0; border-bottom-color:var(--accent); }
.cols { display:flex; gap:1.5rem; align-items:flex-start; margin:.4rem 0; }
.col { min-width:0; }
.plot { width:100%; }
.metric { padding:.4rem 0 1rem; }
.m-label { font-size:.85rem; color:var(--muted); }
.m-value { font-size:1.6rem; font-weight:700; color:#fafafa; line-height:1.3; }
.m-delta { display:inline-block; margin-top:.25rem; font-size:.82rem; color:#b5b5b5;
  background:rgba(255,255,255,.07); border-radius:10px; padding:1px 9px; }
.info { background:var(--panel); border-left:3px solid var(--accent); border-radius:6px;
  padding:.9rem 1.1rem; margin:1rem 0; color:#c9d7ee; }
.info p { margin:0; }
.info strong { color:#e3ecfb; }
.caption { color:var(--muted); font-size:.87rem; margin:.6rem 0 1rem; }
.caption p { margin:0; }
.widget { margin:.3rem 0 .8rem; }
.w-label { font-size:.87rem; color:#bbb; margin-bottom:.3rem; }
.radio { display:flex; flex-wrap:wrap; gap:.4rem 1.2rem; }
.radio label, .check { display:inline-flex; align-items:center; gap:.45rem; cursor:pointer; font-size:.95rem; }
input[type=radio], input[type=checkbox] { accent-color:var(--accent); width:16px; height:16px; margin:0; }
select { background:var(--panel); color:#e6e6e6; border:1px solid #3a3d48; border-radius:8px;
  padding:.55rem .8rem; font-size:.95rem; width:100%; max-width:560px; }
.variant[hidden] { display:none; }
footer { color:#666; font-size:.8rem; text-align:center; padding:0 1rem 2rem; }
footer p { margin:.3rem 0; }
@media (max-width: 860px) {
  main { padding:1.2rem 1rem; }
  .cols { flex-direction:column; gap:.4rem; }
  .col { width:100%; flex:1 1 auto !important; }
  nav { flex-wrap:nowrap; overflow-x:auto; -webkit-overflow-scrolling:touch; }
  nav a { padding:8px 10px; font-size:.92rem; }
}
"""

JS = """
function drawPlots(root) {
  root.querySelectorAll('.plot:not([data-done])').forEach(function (el) {
    var fig = JSON.parse(document.getElementById(el.dataset.fig).textContent);
    Plotly.newPlot(el, fig.data, fig.layout, {responsive: true, displaylogo: false});
    el.dataset.done = '1';
  });
}
function widgetValue(w) {
  if (w.dataset.kind === 'radio') { var c = w.querySelector('input:checked'); return c ? c.value : w.dataset.own; }
  if (w.dataset.kind === 'select') { return w.querySelector('select').value; }
  return JSON.stringify(w.querySelector('input').checked);
}
function resetWidget(w) {
  var own = w.dataset.own;
  if (w.dataset.kind === 'radio') { w.querySelectorAll('input').forEach(function (i) { i.checked = (i.value === own); }); }
  else if (w.dataset.kind === 'select') { w.querySelector('select').value = own; }
  else { w.querySelector('input').checked = (own === 'true'); }
}
function comboOf(variant) {
  return Array.prototype.map.call(variant.querySelectorAll('.widget'), widgetValue).join('||');
}
document.addEventListener('DOMContentLoaded', function () {
  var variants = document.querySelectorAll('.variant');
  if (!variants.length) { drawPlots(document); return; }
  variants.forEach(function (v) {
    if (!v.hidden) { drawPlots(v); }
    v.addEventListener('change', function () {
      var key = comboOf(v), target = null;
      variants.forEach(function (o) { if (o.dataset.combo === key) { target = o; } });
      if (!target || target === v) { return; }
      v.hidden = true;
      v.querySelectorAll('.widget').forEach(resetWidget);
      target.hidden = false;
      drawPlots(target);
      window.dispatchEvent(new Event('resize'));
    });
  });
});
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Interactive charts on the pace of change in agentic coding and AI progress.">
<link rel="stylesheet" href="style.css">
<script src="plotly.min.js"></script>
</head>
<body>
<main>
{header}
<nav>{nav}</nav>
{content}
{footer}
</main>
<footer><p>Charts, data tables and the research report are on <a href="{repo}">GitHub</a>.</p></footer>
<script src="site.js"></script>
</body>
</html>
"""


def slugify(label: str, first: bool) -> str:
    if first:
        return "index"
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def find_tabs(root: Node) -> Node:
    return next(c for c in root.children if c.kind == "tabs")


def combo_key(values) -> str:
    return "||".join(json.dumps(v) for v in values)


def build() -> None:
    base = record()
    tabs_node = find_tabs(base.root)
    labels = [t.props["label"] for t in tabs_node.children]
    slugs = {lab: slugify(lab, i == 0) for i, lab in enumerate(labels)}
    assert len(set(slugs.values())) == len(slugs), "two tabs map to the same file name"

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    import plotly.offline

    (OUT / "plotly.min.js").write_text(plotly.offline.get_plotlyjs(), encoding="utf-8")
    (OUT / "style.css").write_text(CSS, encoding="utf-8")
    (OUT / "site.js").write_text(JS, encoding="utf-8")
    (OUT / ".nojekyll").write_text("")

    idx = base.root.children.index(tabs_node)
    shell = Renderer()
    header = "\n".join(
        shell.render(c) for c in base.root.children[:idx]
        if not (c.kind == "markdown" and c.props["raw"] and c.props["body"].lstrip().startswith("<style"))
    )
    footer = "\n".join(shell.render(c) for c in base.root.children[idx + 1:])
    title_base = base.page_title or "Pace of Change in Agentic Coding"

    runs = 1
    for pos, label in enumerate(labels):
        wids = [w for w, meta in base.widgets.items() if meta["tab"] == label]
        r = Renderer()
        if not wids:
            content = r.children(tabs_node.children[pos])
            variants = 1
        else:
            defaults = tuple(base.widgets[w]["default"] for w in wids)
            parts = []
            combos = list(itertools.product(*(base.widgets[w]["options"] for w in wids)))
            for combo in combos:
                if combo == defaults:
                    rec = base
                else:
                    rec = record(dict(zip(wids, combo)))
                    runs += 1
                tab = find_tabs(rec.root).children[pos]
                hidden = "" if combo == defaults else " hidden"
                key = html.escape(combo_key(combo), quote=True)
                parts.append(f'<div class="variant" data-combo="{key}"{hidden}>\n{r.children(tab)}\n</div>')
            content = "\n".join(parts)
            variants = len(combos)

        nav = "".join(
            '<a href="{}"{}>{}</a>'.format(
                "./" if slugs[lab] == "index" else slugs[lab] + ".html",
                ' class="active"' if lab == label else "",
                html.escape(lab),
            )
            for lab in labels
        )
        plain = re.sub(r"[^\w &?:,.'-]+", "", label).strip()
        page = PAGE.format(title=html.escape(f"{plain} · {title_base}"), header=header, nav=nav,
                           content=content, footer=footer, repo=REPO_URL)
        dest = OUT / f"{slugs[label]}.html"
        dest.write_text(page, encoding="utf-8")
        print(f"{dest.name:28s} {variants:2d} view(s)  {dest.stat().st_size / 1024:7.0f} KB")
    print(f"built {len(labels)} pages in {OUT} from {runs} runs of app.py")


if __name__ == "__main__":
    build()
