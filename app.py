"""
Pace of Change in Agentic Coding
Interactive visualizations for a graduate guest lecture.
"""

import math
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Pace of Change in Agentic Coding",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
    /* Full-bleed dark background */
    .stApp { background-color: #0e1117; }
    .block-container { padding: 2rem 3rem 1rem 3rem; max-width: 1400px; }

    /* Header */
    h1 { font-size: 2.0rem !important; font-weight: 700; letter-spacing: -0.5px; }
    .subtitle { color: #888; font-size: 1.0rem; margin-top: -0.6rem; margin-bottom: 1.2rem; }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 4px; border-bottom: 1px solid #2d2d2d; }
    .stTabs [data-baseweb="tab"] {
        font-size: 1.0rem;
        font-weight: 500;
        padding: 10px 24px;
        color: #888;
    }
    .stTabs [aria-selected="true"] { color: #e0e0e0 !important; }

    /* Metric cards */
    [data-testid="stMetricValue"] { font-size: 1.6rem !important; font-weight: 700; }
    [data-testid="stMetricLabel"] { font-size: 0.85rem !important; color: #888; }
    [data-testid="stMetricDelta"] { font-size: 0.85rem !important; }

    /* Info boxes */
    .stInfo { background-color: #1a1d27; border-left: 3px solid #10a37f; }

    hr { border-color: #2d2d2d; margin: 0.8rem 0 1.4rem 0; }
</style>
""",
    unsafe_allow_html=True,
)

# ── Color palette ─────────────────────────────────────────────────────────────
ORG_COLORS = {
    "OpenAI": "#10a37f",
    "Anthropic": "#e07b4a",
    "Google": "#4c8ef5",
    "xAI": "#e04a7b",
    "Meta": "#5c8fff",
    "DeepSeek": "#a855f7",
    "Microsoft": "#888888",
    "Moonshot": "#f5c542",
    "Z.ai": "#22d3ee",
    "Alibaba": "#84cc16",
}

PLOT_BG = "#0e1117"
PAPER_BG = "#0e1117"
GRID_COL = "#23262f"
FONT_COL = "#d0d0d0"

LEGEND_STYLE = dict(
    bgcolor="rgba(20,22,30,0.85)",
    bordercolor="#333",
    borderwidth=1,
    font=dict(size=12),
)

BASE_LAYOUT = dict(
    template="plotly_dark",
    plot_bgcolor=PLOT_BG,
    paper_bgcolor=PAPER_BG,
    font=dict(color=FONT_COL, family="Inter, sans-serif", size=13),
    hoverlabel=dict(
        bgcolor="#1a1d27",
        bordercolor="#444",
        font=dict(color="#e0e0e0", size=13),
    ),
)


def hex_to_rgba(hex_color: str, alpha: float = 0.18) -> str:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"



def add_vline(fig, x, text, color="#666", dash="dash", y_text=1.0, anchor="left"):
    """Vertical date marker with a label (avoids plotly's date-annotation quirks)."""
    fig.add_shape(
        type="line", x0=x, x1=x, xref="x", y0=0, y1=1, yref="paper",
        line=dict(color=color, width=1.2, dash=dash),
    )
    fig.add_annotation(
        x=x, y=y_text, xref="x", yref="paper", text=text, showarrow=False,
        font=dict(size=10.5, color=color), xanchor=anchor, yanchor="bottom",
        xshift=4 if anchor == "left" else -4,
    )


def fmt_minutes(m):
    if pd.isna(m):
        return "n/a"
    if m < 1:
        return f"{m * 60:.0f} sec"
    if m < 60:
        return f"{m:.0f} min"
    h = int(m // 60)
    return f"{h} h {int(round(m - h * 60)):02d} m"


# ── Data loading ──────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    base = Path(__file__).parent / "working-data-tables"

    def read(name, dates=()):
        df = pd.read_csv(base / name)
        for c in dates:
            df[c] = pd.to_datetime(df[c])
        return df

    d = dict(
        th=read("model-task-time-horizons.csv", ["Release_Date"]),
        bm=read("model-benchmark-scores.csv", ["Date"]),
        tl=read("model-release-timeline.csv", ["Release Date"]),
        life=read("benchmark-lifespans.csv", ["Introduced", "Ended"]),
        arc=read("arc-agi-scores.csv", ["Date"]),
        eci=read("eci-scores.csv", ["Date"]),
        vi=read("vendor-vs-independent.csv"),
        adopt=read("adoption-series.csv", ["Date"]),
        prod=read("productivity-studies.csv"),
        uplift=read("metr-uplift-studies.csv"),
        labor=read("labor-series.csv", ["Date"]),
        pred=read("prediction-scorecard.csv").fillna("n/a"),
        after=read("after-metr-instruments.csv"),
        exph=read("expenditure-horizon.csv"),
        succ=read("successor-benchmarks.csv", ["Launched"]),
        prices=read("model-prices.csv", ["Release_Date"]),
        arccost=read("arc-cost-per-task.csv", ["Date"]),
        aacost=read("aa-cost-to-run.csv"),
        cyber=read("cyber-capability.csv", ["Date"]),
        catalog=read("benchmark-catalog.csv").fillna(""),
    )
    for col in ["MMLU", "GPQA", "SWE_bench_Verified", "HumanEval", "MATH"]:
        d["bm"][col] = pd.to_numeric(d["bm"][col], errors="coerce")
    return d


D = load_data()
th_df, bm_df, tl_df = D["th"], D["bm"], D["tl"]
AS_OF = pd.Timestamp("2026-11-19")

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("# The Pace of Change in Agentic Coding")
st.markdown(
    '<p class="subtitle">Prepared for NCSU CSC510 &nbsp;·&nbsp; data as of 19 November 2026</p>',
    unsafe_allow_html=True,
)
st.divider()

# ── Tabs ──────────────────────────────────────────────────────────────────────
(tab_rel, tab_life, tab_bench, tab_who, tab_th, tab_cost, tab_real, tab_jobs, tab_pred, tab_guide) = st.tabs(
    [
        "📅  Release Cadence",
        "⏳  Benchmark Lifespans",
        "📊  Progress Measures",
        "🔍  Who Measured It?",
        "⏱  Task Time Horizons",
        "💵  Cost & Value",
        "🏗  Benchmarks vs Reality",
        "🎓  Jobs & Education",
        "🎯  Prediction Scorecard",
        "📚  Benchmark Guide",
    ]
)


# ═════════════════════════════════════════════════════════════════════════════
# TAB — Release Cadence
# ═════════════════════════════════════════════════════════════════════════════
with tab_rel:
    st.markdown("### Model Release Cadence by Organization")
    st.markdown(
        "Each marker is a model release. Large markers are flagships; **diamonds were "
        "access-gated** (approved organizations or government first). Hover for details."
    )

    ORG_ORDER = [
        "OpenAI", "Anthropic", "Google", "xAI", "Meta", "Microsoft",
        "DeepSeek", "Moonshot", "Z.ai", "Alibaba",
    ]
    org_y = {org: i for i, org in enumerate(ORG_ORDER)}

    win = st.radio(
        "Window", ["2024 to today", "2026 only"], horizontal=True,
        label_visibility="collapsed", key="rel_window",
    )
    x_range = (
        ["2024-01-01", "2026-12-15"] if win == "2024 to today" else ["2025-12-15", "2026-12-05"]
    )

    def _short(name: str) -> str:
        for a, b in [
            ("Claude Opus ", "Opus "), ("Claude Sonnet ", "Sonnet "), ("Claude Haiku ", "Haiku "),
            ("Claude Fable ", "Fable "), ("Claude Mythos ", "Mythos "),
            ("Claude 3.5 Sonnet", "3.5 Sonnet"), ("Claude 3.7 Sonnet", "3.7 Sonnet"),
            ("Claude 3 ", "3 "), ("Gemini ", ""), ("GPT-", ""), ("DeepSeek ", ""),
            (" Preview", ""), (" / Terra / Luna", ""), (" / Sol", ""), (" / Luna", ""),
            (" / Wonder Full", ""), (" / Code 2 Flash", ""), (" / V4-Flash", ""),
            (" / MAI-Code-1-Flash", ""), ("-35B-A3B", ""), (" Scout/Maverick", ""),
            (" / Sonnet 4", ""), (" / o4-mini", ""), (" 8B/70B", ""),
        ]:
            name = name.replace(a, b)
        return name

    SYMBOL = {
        "Gated": "diamond-open", "Gated first": "diamond",
        "Preview": "circle-open", "Weights promised": "circle-open",
    }

    fig3 = go.Figure()
    for year in [2025, 2026]:
        add_vline(fig3, f"{year}-01-01", str(year), color="#444")

    for org in ORG_ORDER:
        org_df = tl_df[tl_df["Organization"] == org].sort_values("Release Date")
        if org_df.empty:
            continue
        color = ORG_COLORS.get(org, "#888")
        flag = org_df["Tier"] == "Flagship"
        show_label = flag if win == "2024 to today" else pd.Series(True, index=org_df.index)
        labels = [(_short(m) if s else "") for m, s in zip(org_df["Model"], show_label)]
        # alternate label side to reduce collisions
        pos, k = [], 0
        for lab in labels:
            if lab:
                pos.append("top center" if k % 2 == 0 else "bottom center")
                k += 1
            else:
                pos.append("top center")

        fig3.add_trace(
            go.Scatter(
                x=org_df["Release Date"],
                y=[org_y[org]] * len(org_df),
                mode="markers+text",
                name=org,
                marker=dict(
                    size=[15 if f else 9 for f in flag],
                    color=color,
                    symbol=[SYMBOL.get(a, "circle") for a in org_df["Access"]],
                    line=dict(color=[color if a in SYMBOL else PLOT_BG for a in org_df["Access"]], width=2),
                ),
                text=labels,
                textposition=pos,
                textfont=dict(size=9, color=hex_to_rgba(color, 0.9)),
                customdata=list(
                    zip(
                        org_df["Model"], org_df["Type"],
                        org_df["Release Date"].dt.strftime("%B %d, %Y"),
                        org_df["Access"], org_df["Source_Quality"],
                    )
                ),
                hovertemplate=(
                    "<b>%{customdata[0]}</b><br>%{customdata[1]}<br>"
                    "Released: %{customdata[2]}<br>Access: %{customdata[3]}<br>"
                    "Date source: %{customdata[4]}<extra></extra>"
                ),
            )
        )

    fig3.update_layout(
        **BASE_LAYOUT,
        height=640,
        margin=dict(l=90, r=40, t=55, b=40),
        title=dict(text="Model Releases, Feb 2024 to Nov 2026", font=dict(size=15), x=0.0),
        xaxis=dict(title="", gridcolor=GRID_COL, showgrid=True, range=x_range),
        yaxis=dict(
            tickvals=list(org_y.values()), ticktext=list(org_y.keys()),
            gridcolor=GRID_COL, showgrid=True, tickfont=dict(size=13),
            range=[len(ORG_ORDER) - 0.4, -0.6],
        ),
        showlegend=False,
        hovermode="closest",
    )
    st.plotly_chart(fig3, width="stretch")

    # ── Releases per quarter ───────────────────────────────────────────────
    q = tl_df.copy()
    q["Quarter"] = q["Release Date"].dt.to_period("Q")
    counts = q.groupby(["Quarter", "Organization"]).size().unstack(fill_value=0)
    counts = counts.reindex(pd.period_range("2024Q1", "2026Q4", freq="Q"), fill_value=0)
    qlabels = [f"{p.year} Q{p.quarter}" for p in counts.index]
    figq = go.Figure()
    for org in ORG_ORDER:
        if org in counts.columns:
            figq.add_trace(
                go.Bar(x=qlabels, y=counts[org], name=org, marker_color=ORG_COLORS.get(org, "#888"),
                       hovertemplate=f"{org}: %{{y}}<extra></extra>")
            )
    totals = counts.sum(axis=1)
    figq.add_trace(
        go.Scatter(x=qlabels, y=totals, mode="text", text=[str(int(t)) for t in totals],
                   textposition="top center", textfont=dict(size=12, color="#bbb"),
                   showlegend=False, hoverinfo="skip")
    )
    figq.update_layout(
        **BASE_LAYOUT, barmode="stack", height=370,
        margin=dict(l=70, r=40, t=55, b=40),
        title=dict(text="Tracked releases per quarter (2026 Q4 is partial, through Nov 19)",
                   font=dict(size=15), x=0.0),
        xaxis=dict(gridcolor=GRID_COL), yaxis=dict(gridcolor=GRID_COL, title="Releases"),
        legend=dict(**LEGEND_STYLE, orientation="h", y=-0.28),
    )
    st.plotly_chart(figq, width="stretch")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Anthropic launch events", "13 in 2026", "6 in 2025", delta_color="off")
    c2.metric("OpenAI: GPT-6 → 6.1 → 6.2", "75 days", "GPT-4 → GPT-5 took 28 months", delta_color="off")
    c3.metric("Google: Gemini 4 models", "4 in 5 weeks", "Oct 13 to Nov 18", delta_color="off")
    c4.metric("Access-gated releases, 2026", f"{int(tl_df['Access'].str.startswith('Gated').sum())}", "0 before April 2026", delta_color="off")

    st.info(
        "**What changed in 2026:** the shape, not just the speed. Labs added **tiers above "
        "their old flagships** (Fable and Mythos over Opus in June; GPT-6 Astra in September), "
        "shipped **gated cyber and bio variants**, and split announcement dates from availability. "
        "Four Chinese labs now ship open-weight coding models within months of the closed frontier."
    )
    st.caption(
        "Dates are first public availability, from lab changelogs where one exists. Hover shows "
        "the date source: some Microsoft, Meta and Chinese-lab rows rest on press coverage. The quarterly count covers the models tracked here, "
        "which is more complete for 2026 than for 2024."
    )


    # ── Why labs started gating: cyber capability ──────────────────────────
    st.divider()
    st.markdown("### Why the Gates Went Up: Cyber Capability")
    st.markdown(
        "Most of the gated releases above were restricted on cybersecurity grounds. Two "
        "security benchmarks show what the labs were looking at."
    )
    cy = D["cyber"]
    gated = tl_df[tl_df["Access"].str.startswith("Gated")].sort_values("Release Date")
    first_gate = gated["Release Date"].min()
    left, right = st.columns([3, 2])
    with left:
        cb = cy[cy["Benchmark"] == "CyBench"].sort_values("Date")
        figcy = go.Figure()
        best = cb[cb["Score"] == cb["Score"].cummax()]
        figcy.add_trace(go.Scatter(
            x=list(best["Date"]) + [AS_OF], y=list(best["Score"]) + [best["Score"].iloc[-1]], mode="lines",
            line=dict(color="#ddd", width=1.5, dash="dot", shape="hv"), name="Best to date", hoverinfo="skip"))
        for org in cb["Org"].unique():
            g = cb[cb["Org"] == org]
            colr = ORG_COLORS.get(org, "#888")
            figcy.add_trace(go.Scatter(
                x=g["Date"], y=g["Score"], mode="markers", name=org,
                marker=dict(size=10, color=colr, line=dict(color=PLOT_BG, width=1.5)),
                customdata=list(zip(g["Model"], g["Reported_in"])),
                hovertemplate="<b>%{customdata[0]}</b><br>%{x|%b %Y}: %{y:.1f}% solved"
                              "<br>Reported in: %{customdata[1]}<extra></extra>"))
        for _, r in best.iloc[[0, -3, -2, -1]].iterrows():
            figcy.add_annotation(x=r["Date"], y=r["Score"], text=r["Model"].replace("Claude ", ""),
                                 showarrow=False, xanchor="right", xshift=-9, font=dict(size=10, color="#bbb"))
        for _, r in gated.iterrows():
            figcy.add_trace(go.Scatter(
                x=[r["Release Date"]], y=[3], mode="markers", showlegend=False,
                marker=dict(size=11, symbol="diamond", color=ORG_COLORS.get(r["Organization"], "#888"),
                            line=dict(color="#fff", width=1)),
                hovertemplate=f"<b>{r['Model']}</b><br>Gated release, {r['Release Date']:%b %d, %Y}<extra></extra>"))
        add_vline(figcy, first_gate, "First gated release<br>(Mythos Preview)", color="#e0524a", y_text=0.3, anchor="left")
        figcy.update_layout(
            **BASE_LAYOUT, height=470, margin=dict(l=60, r=20, t=70, b=40),
            title=dict(text="CyBench: professional capture-the-flag challenges solved unaided<br>"
                            "(diamonds along the bottom mark gated releases)", font=dict(size=14), x=0.0),
            xaxis=dict(gridcolor=GRID_COL, range=["2024-01-01", "2026-12-15"]),
            yaxis=dict(title="Solved (%)", gridcolor=GRID_COL, range=[0, 102]),
            legend=dict(**LEGEND_STYLE, x=0.01, y=0.99), hovermode="closest",
        )
        st.plotly_chart(figcy, width="stretch")
    with right:
        eb = cy[cy["Benchmark"] == "ExploitBench"].sort_values("Score", ascending=False)
        gated_names = set(gated["Model"])
        is_gated = eb["Model"].isin(gated_names)
        figeb = go.Figure(go.Bar(
            y=[m.replace("Claude ", "") + ("  ◆ gated" if g else "") for m, g in zip(eb["Model"], is_gated)],
            x=eb["Score"], orientation="h",
            marker_color=[ORG_COLORS.get(o, "#888") for o in eb["Org"]],
            marker_line=dict(color=["#fff" if g else PLOT_BG for g in is_gated], width=1.5),
            text=[f"{v:.0f}%" for v in eb["Score"]], textposition="outside",
            customdata=eb["Date"].dt.strftime("%b %d, %Y"),
            hovertemplate="%{y}<br>Released %{customdata}<br>Mean capability %{x:.1f}%<extra></extra>"))
        figeb.update_layout(
            **BASE_LAYOUT, height=470, margin=dict(l=20, r=40, t=70, b=40),
            title=dict(text="ExploitBench: building working exploits<br>for 41 known browser-engine bugs",
                       font=dict(size=14), x=0.0),
            xaxis=dict(title="Mean capability (%)", gridcolor=GRID_COL, range=[0, 88]),
            yaxis=dict(autorange="reversed", tickfont=dict(size=12)),
        )
        st.plotly_chart(figeb, width="stretch")

    myth = cy[(cy["Benchmark"] == "ExploitBench") & (cy["Model"] == "Claude Mythos Preview")]["Score"].iloc[0]
    nxt = cy[(cy["Benchmark"] == "ExploitBench") & (cy["Model"] != "Claude Mythos Preview")]["Score"].max()
    cb0, cb1 = cb["Score"].iloc[0], cb["Score"].max()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("CyBench, Feb 2024 to Feb 2026", f"{cb0:.0f}% → {cb1:.0f}%", "last entry in Epoch's file", delta_color="off")
    c2.metric("ExploitBench: first gated model", f"{myth:.0f}%", f"best ungated model: {nxt:.0f}%", delta_color="off")
    c3.metric("ExploitGym: exploits via the intended bug", "157 vs 120", "Mythos Preview vs GPT-5.5", delta_color="off")
    c4.metric("Gated releases since April 2026", str(len(gated)), "cyber, bio and top-tier models", delta_color="off")

    st.info(
        "**Security tests form a ladder, and models climbed it in order.** Solving "
        "capture-the-flag puzzles (CyBench) went from 8% to 93% in two years and stopped being "
        "informative. Reproducing known vulnerabilities (CyberGym) reached 82% for GPT-5.5 by "
        "OpenAI's own figure. "
        "The step that changed release policy is building working exploits: the first model "
        "Anthropic held back, Claude Mythos Preview, scored 74% on ExploitBench, against 27% "
        "for Claude Opus 4.7, which shipped openly nine days later. OpenAI, Google and Microsoft "
        "have each since sent at least one model to approved organizations first."
    )
    st.caption(
        "CyBench and ExploitBench figures are from Epoch's benchmark data file of 19 November "
        "2026, which records where each was reported: mostly the benchmark's leaderboard or "
        "the lab's own system card. The chart shows each model's best listed run. ExploitBench "
        "is one of five benchmarks Epoch's review programme rates Verified. ExploitGym counts "
        "are from its project page; it is a different benchmark from ExploitBench. The reasons "
        "labs gave for gating come from their own release notes and from press reports. Finding "
        "new vulnerabilities and breaking into live networks are measured separately, mostly "
        "by government institutes, and are not charted here."
    )


# ═════════════════════════════════════════════════════════════════════════════
# TAB — Benchmark Lifespans
# ═════════════════════════════════════════════════════════════════════════════
with tab_life:
    st.markdown("### How Long Does a Benchmark Last?")
    st.markdown(
        "Each bar runs from a benchmark's introduction to the point it stopped separating "
        "frontier models: saturated, discredited, or superseded."
    )
    life = D["life"].sort_values("Introduced").reset_index(drop=True)
    life["End_Plot"] = life["Ended"].fillna(AS_OF)
    life["Months"] = ((life["End_Plot"] - life["Introduced"]).dt.days / 30.44).round(0)

    STATUS_COL = {
        "Saturated": "#e0a23c", "Discredited": "#e0524a",
        "Superseded": "#9aa0aa", "Active": "#10a37f",
    }
    figl = go.Figure()
    for status, colr in STATUS_COL.items():
        figl.add_trace(go.Scatter(x=[life["Introduced"].iloc[0]], y=[None], mode="lines", name=status,
                                  line=dict(color=colr, width=10)))
    for i, r in life.iterrows():
        colr = STATUS_COL[r["Status"]]
        active = r["Status"] == "Active"
        figl.add_trace(
            go.Scatter(
                x=[r["Introduced"], r["End_Plot"]], y=[r["Benchmark"]] * 2, mode="lines",
                line=dict(color=hex_to_rgba(colr, 0.55 if active else 0.95), width=16),
                showlegend=False,
                hovertemplate=(
                    f"<b>{r['Benchmark']}</b><br>{r['Measures']}<br>"
                    f"Introduced {r['Introduced']:%b %Y}"
                    + ("" if active else f" · ended {r['Ended']:%b %Y}")
                    + f"<br>{r['How_Ended']}"
                    + (f"<br>Epoch review: {r['Epoch_Review']}" if isinstance(r["Epoch_Review"], str) else "")
                    + "<extra></extra>"
                ),
            )
        )
        figl.add_annotation(
            x=r["End_Plot"], y=r["Benchmark"], xanchor="left", xshift=8, showarrow=False,
            text=(f"{int(r['Months'])} mo so far" if active else f"<b>{int(r['Months'])} mo</b>")
            + (" · rated Flawed" if active and str(r["Epoch_Review"]).startswith("Flawed") else ""),
            font=dict(size=11.5, color=colr),
        )
    figl.update_layout(
        **BASE_LAYOUT, height=600, margin=dict(l=160, r=90, t=55, b=40),
        title=dict(text="Benchmark lifespans, by introduction date", font=dict(size=15), x=0.0),
        xaxis=dict(type="date", gridcolor=GRID_COL, range=["2019-06-01", "2027-11-01"]),
        yaxis=dict(type="category", categoryorder="array", categoryarray=list(life["Benchmark"]),
                   gridcolor=GRID_COL, autorange="reversed", tickfont=dict(size=12.5)),
        legend=dict(**LEGEND_STYLE, orientation="h", y=-0.08),
        hovermode="closest",
    )
    st.plotly_chart(figl, width="stretch")

    ended = life[life["Status"] != "Active"]

    def _avg(a, b):
        s = ended[(ended["Introduced"] >= a) & (ended["Introduced"] < b)]["Months"]
        return f"{s.mean():.0f} months", f"{len(s)} benchmarks"

    c1, c2, c3, c4 = st.columns(4)
    c4.metric("Epoch's reviews of 29 benchmarks", "15 Flawed", "5 Verified · 9 not enough info", delta_color="off")
    v, n = _avg("2019-01-01", "2022-01-01")
    c1.metric("Introduced 2019 to 2021", v, n, delta_color="off")
    v, n = _avg("2023-01-01", "2025-01-01")
    c2.metric("Introduced 2023 to 2024", v, n, delta_color="off")
    v, n = _avg("2025-01-01", "2026-01-01")
    c3.metric("Introduced 2025", v, n, delta_color="off")

    st.info(
        "**Every benchmark the previous version of this deck charted is now retired.** "
        "The average useful life fell by roughly half with each cohort. Two of the 2026 "
        "endings were not ceilings but **validity failures**: OpenAI stopped reporting "
        "SWE-bench Verified in February (flawed tests, memorised fixes), endorsed SWE-bench Pro, "
        "then withdrew that endorsement in July after finding about 30% of its tasks broken. "
        "Being current is not the same as being sound: Epoch's review programme rates three of "
        "the five benchmarks still in use here as **Flawed** (ARC-AGI-3, Humanity's Last Exam, "
        "Terminal-Bench 4.0)."
    )
    st.caption(
        "End dates are judgment calls: the month a benchmark stopped discriminating among "
        "frontier models or was disowned by a major evaluator. Cohort averages are computed "
        "from this table, not a published statistic. Pre-2023 dates are from background "
        "knowledge and the Stanford AI Index; 2025 to 2026 dates are from Epoch, ARC Prize, "
        "Artificial Analysis and tbench.ai. \"Flawed\" is Epoch's review verdict on a "
        "benchmark's scoring, setup or consistency, not a retirement; Epoch does not review "
        "its own benchmarks, FrontierMath among them."
    )


# ═════════════════════════════════════════════════════════════════════════════
# TAB — Progress Measures
# ═════════════════════════════════════════════════════════════════════════════
with tab_bench:
    st.markdown("### Measuring Progress When Benchmarks Keep Dying")

    SUCC_INFO = (
        "**No single benchmark replaced SWE-bench; a portfolio did.** Each successor tests a "
        "different part of the job, and the scores spread accordingly. Agents rebuild a whole "
        "program to an exact, checkable specification almost perfectly (98%), and score 65% to "
        "80% on fresh issues and maintenance tasks. They complete only **19%** of from-scratch "
        "builds and **25%** of tasks that require keeping earlier work intact while adding to "
        "it. On ARE-bench the same runs earn 93% of the checklist and 66% on delivering "
        "everything: mostly right is not the same as done."
    )
    SUCC_CAPTION = (
        "Each bar is the best score found on the benchmark owner's page or paper as of 19 "
        "November 2026, with its own harness and budget; bars are not comparable to one another "
        "as model rankings. Hover for who ran each result and its caveat. SWE-rebench's board "
        "has not added a model since July, LoopsBench has only its July paper result, and the "
        "SWE-bench-Live entry is self-submitted."
    )
    VIEWS = [
        "Composite index (Epoch ECI)",
        "ARC-AGI-2 and ARC-AGI-3",
        "After SWE-bench: the successor portfolio",
        "Retired: GPQA Diamond",
        "Retired: SWE-bench Verified",
        "Retired: MATH / AIME",
        "Retired: MMLU",
    ]
    top_col, _ = st.columns([2, 3])
    with top_col:
        view = st.selectbox("Select measure", VIEWS, label_visibility="collapsed")

    if view == VIEWS[0]:
        eci = D["eci"].sort_values(["Date", "ECI"])
        fr = eci[eci["Is_Frontier"] == "yes"]
        split = pd.Timestamp("2024-09-12")  # first reasoning model on the frontier

        def _fit(df):
            x = (df["Date"] - split).dt.days / 365.25
            n = len(x)
            slope = ((x * df["ECI"]).sum() - x.sum() * df["ECI"].sum() / n) / ((x**2).sum() - x.sum() ** 2 / n)
            return slope, df["ECI"].mean() - slope * x.mean()

        pre, post = fr[fr["Date"] < split], fr[fr["Date"] >= split]
        (s_pre, b_pre), (s_post, b_post) = _fit(pre), _fit(post)
        fig2 = go.Figure()
        for (sl, b, d0, d1, nm, colr) in [
            (s_pre, b_pre, pre["Date"].min(), split, f"Frontier trend before reasoning models: about {s_pre:.0f} pts/yr", "#777"),
            (s_post, b_post, split, AS_OF, f"Frontier trend since: about {s_post:.0f} pts/yr", "#bbb"),
        ]:
            fig2.add_trace(go.Scatter(
                x=[d0, d1], y=[b + sl * (d - split).days / 365.25 for d in (d0, d1)], mode="lines",
                name=nm, line=dict(color=colr, width=1.5, dash="dash"), hoverinfo="skip"))

        LAB_ORDER = ["OpenAI", "Anthropic", "Google", "Meta", "Moonshot", "DeepSeek", "xAI",
                     "Alibaba", "Z.ai", "Microsoft"]
        ends = []
        for org in LAB_ORDER:
            g = eci[eci["Org"] == org]
            if g.empty:
                continue
            colr = ORG_COLORS.get(org, "#888")
            last = g.iloc[-1]
            stale = (AS_OF - last["Date"]).days > 365
            xs = list(g["Date"]) + ([] if stale else [AS_OF])
            ys = list(g["ECI"]) + ([] if stale else [last["ECI"]])
            fig2.add_trace(go.Scatter(
                x=xs, y=ys, mode="lines",
                line=dict(color=hex_to_rgba(colr, 0.9 if org in LAB_ORDER[:3] else 0.5),
                          width=2.6 if org in LAB_ORDER[:3] else 1.4, shape="hv"),
                legendgroup=org, showlegend=False, hoverinfo="skip"))
            is_open = g["Weights"] == "Open"
            fig2.add_trace(go.Scatter(
                x=g["Date"], y=g["ECI"], mode="markers", name=org, legendgroup=org,
                marker=dict(size=[9 if f == "yes" else 6 for f in g["Is_Frontier"]],
                            color=[PLOT_BG if o else colr for o in is_open],
                            line=dict(color=colr, width=1.8)),
                customdata=list(zip(g["Model"], g["Access_Detail"], g["CI_lo"], g["CI_hi"])),
                hovertemplate="<b>%{customdata[0]}</b> (" + org + ")<br>%{x|%b %d, %Y}"
                              "<br>ECI %{y:.1f} (%{customdata[2]:.1f} to %{customdata[3]:.1f})"
                              "<br>%{customdata[1]}<extra></extra>"))
            ends.append(dict(org=org, y=last["ECI"], x=last["Date"] if stale else AS_OF,
                             stale=stale, model=last["Model"], colr=colr))

        # end-of-line labels, nudged apart so they do not overlap
        live = sorted([e for e in ends if not e["stale"]], key=lambda e: -e["y"])
        ylab = None
        for e in live:
            ylab = e["y"] if ylab is None else min(e["y"], ylab - 2.0)
            fig2.add_annotation(x=AS_OF, y=ylab, xanchor="left", xshift=10, showarrow=False,
                                text=f"<b>{e['org']}</b> {e['y']:.0f}", font=dict(size=11.5, color=e["colr"]))
        for e in [e for e in ends if e["stale"]]:
            fig2.add_annotation(
                x=e["x"], y=e["y"], xanchor="left", xshift=10, showarrow=False,
                text=f"<b>{e['org']}</b> {e['y']:.0f} ({e['model']}, {e['x']:%Y}); no MAI model evaluated",
                font=dict(size=10.5, color="#aaa"), align="left", yshift=-12)
        add_vline(fig2, split, "First reasoning model", color="#666", y_text=0.02)
        fig2.update_layout(
            **BASE_LAYOUT, height=700, margin=dict(l=70, r=110, t=55, b=110),
            title=dict(text="Epoch Capabilities Index: each lab's best model to date", font=dict(size=15), x=0.0),
            xaxis=dict(gridcolor=GRID_COL, range=["2022-12-01", "2026-12-01"]),
            yaxis=dict(title="ECI score", gridcolor=GRID_COL, range=[116, 180]),
            legend=dict(**LEGEND_STYLE, orientation="h", y=-0.13), hovermode="closest",
        )
        st.plotly_chart(fig2, width="stretch")

        lead = eci.loc[eci["ECI"].idxmax()]
        op = eci[eci["Weights"] == "Open"]
        best_open = op.loc[op["ECI"].idxmax()]
        passed = fr[fr["ECI"] >= best_open["ECI"]]["Date"].min()
        lag_mo = (best_open["Date"] - passed).days / 30.44
        chinese = eci[eci["Org"].isin(["Moonshot", "DeepSeek", "Alibaba", "Z.ai"])]
        best_cn_closed = chinese[chinese["Weights"] == "Closed"]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Leader", f"{lead['ECI']:.1f}", lead["Model"], delta_color="off")
        c2.metric("Best open-weight model", f"{best_open['ECI']:.1f}",
                  f"{best_open['Model']} · {lead['ECI'] - best_open['ECI']:.0f} pts behind", delta_color="off")
        c3.metric("Open-weight lag", f"about {lag_mo:.0f} months",
                  f"frontier passed that score in {passed:%b %Y}", delta_color="off")
        c4.metric("Labs within 5 points of the lead",
                  str(sum(1 for e in live if lead["ECI"] - e["y"] <= 5)),
                  "OpenAI, Anthropic, Google", delta_color="off")

        st.info(
            "**One number that survives benchmark turnover.** Epoch's index statistically links "
            "scores across many benchmarks, so it keeps working as individual tests saturate. "
            f"The frontier climbed about **{s_pre:.0f} points a year before reasoning models and "
            f"about {s_post:.0f} a year since** (Epoch's own estimates: 8.0 and 16.6), with no "
            "slowdown in 2026. Three labs trade the lead; everyone else sits 12 to 17 points back, "
            "which is roughly where the frontier was seven to eleven months earlier. The best "
            "open-weight models (hollow markers) now come from Moonshot and DeepSeek and match "
            "Meta's closed flagship. Alibaba's strongest Qwen models are closed and API-only; its "
            "best open-weight model scores about 153."
        )
        st.caption(
            "Each point is a model that raised its own lab's best score; larger points also set "
            "a new overall record. All values are from one copy of Epoch's data file, downloaded "
            "19 November 2026. The dashed lines are least-squares fits to the record-setting "
            "points, computed here. The open-weight lag is our reading of this file (Epoch's own "
            "estimate in May 2026 was about 4 months). A lab appears only if Epoch has evaluated "
            "its models: Microsoft's MAI models are absent because none is in the file, and "
            "models released in the last few days (Qwen4-Max, Gemini 4 Neon) are not yet scored."
        )

    elif view == VIEWS[1]:
        arc = D["arc"].sort_values("Date")
        fig2 = go.Figure()
        for col, name, colr, sym in [
            ("ARC_AGI_2", "ARC-AGI-2", "#e0a23c", "circle"),
            ("ARC_AGI_3_Standard", "ARC-AGI-3 (standard harness)", "#10a37f", "circle"),
            ("ARC_AGI_3_Adapter", "ARC-AGI-3 (provider-adapter harness)", "#10a37f", "circle-open"),
        ]:
            sub = arc.dropna(subset=[col])
            fig2.add_trace(go.Scatter(
                x=sub["Date"], y=sub[col], mode="markers", name=name,
                marker=dict(size=8, color=hex_to_rgba(colr, 0.55), symbol=sym,
                            line=dict(width=1.5, color=hex_to_rgba(colr, 0.7))),
                customdata=sub["Model"],
                hovertemplate="<b>%{customdata}</b><br>" + name + ": %{y:.1f}%<extra></extra>",
            ))
            if sym == "circle":
                best = sub[sub[col] == sub[col].cummax()].drop_duplicates(subset=[col])
                fig2.add_trace(go.Scatter(
                    x=list(best["Date"]) + [AS_OF], y=list(best[col]) + [best[col].iloc[-1]],
                    mode="lines", line=dict(color=colr, width=2.5, shape="hv"),
                    showlegend=False, hoverinfo="skip"))
                fig2.add_annotation(x=AS_OF, y=best[col].iloc[-1], xanchor="left", showarrow=False,
                                    text=f"  {best[col].iloc[-1]:.0f}%", font=dict(size=12, color=colr))
        add_vline(fig2, "2026-03-25", "ARC-AGI-3 launches", color="#10a37f", y_text=0.02)
        fig2.update_layout(
            **BASE_LAYOUT, height=560, margin=dict(l=70, r=80, t=55, b=60),
            title=dict(text="ARC-AGI-2 and ARC-AGI-3: best score to date (ARC Prize leaderboard)",
                       font=dict(size=15), x=0.0),
            xaxis=dict(gridcolor=GRID_COL, range=["2025-11-01", "2026-12-20"]),
            yaxis=dict(title="Score (%)", gridcolor=GRID_COL, range=[-3, 105]),
            legend=dict(**LEGEND_STYLE, x=0.01, y=0.99), hovermode="closest",
        )
        st.plotly_chart(fig2, width="stretch")
        st.info(
            "**The fastest saturation on record.** ARC-AGI-2 went from **54% to 96% in eleven "
            "months**. ARC-AGI-3, built to resist exactly that, launched in March 2026 with every "
            "frontier model **under 1%** and stands at **81%** eight months later. The hollow "
            "points show the same models on a harness the provider supplies: at the same effort "
            "setting, GPT-6 Astra scores 63% on the standard harness and 98.6% on its own."
        )
        st.caption(
            "Scores are from ARC Prize's Verified Leaderboard, which ARC Prize runs itself on a "
            "semi-private task set. Entry dates can trail model launch by a few days. The separate "
            "ARC Prize 2026 competition reports results on 4 December 2026. Epoch rated ARC-AGI-3 "
            "Flawed on 30 October 2026: the headline number is action efficiency against a human "
            "baseline, not a percentage solved, and the standard harness discards the model's "
            "reasoning after every action."
        )

    elif view == VIEWS[2]:
        sc = D["succ"].sort_values("Top_score").reset_index(drop=True)
        CAT_COL = {
            "Build from scratch": "#e0524a", "Sustained work": "#e0a23c",
            "Project continuation": "#a855f7", "Fresh issues": "#4c8ef5", "Maintenance": "#10a37f",
            "Rebuild to exact spec": "#9aa0aa",
        }
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            y=sc["Benchmark"], x=[100] * len(sc), orientation="h", showlegend=False,
            marker_color="rgba(255,255,255,0.05)", hoverinfo="skip"))
        for cat, colr in CAT_COL.items():
            g = sc[sc["Category"] == cat]
            if g.empty:
                continue
            fig2.add_trace(go.Bar(
                y=g["Benchmark"], x=g["Top_score"], orientation="h", name=cat, marker_color=colr,
                customdata=list(zip(g["Measures"], g["Holder"], g["Executed_by"], g["Run_by"],
                                    g["Launched"].dt.strftime("%b %Y"), g["Caveat"])),
                hovertemplate="<b>%{y}</b> (%{customdata[3]}, %{customdata[4]})<br>%{customdata[0]}"
                              "<br>Top score %{x:.1f}%: %{customdata[1]}"
                              "<br>Run by: %{customdata[2]}<br>%{customdata[5]}<extra></extra>"))
        for _, r in sc.iterrows():
            fig2.add_annotation(
                x=r["Top_score"] if r["Top_score"] < 75 else 2, y=r["Benchmark"], xanchor="left",
                xshift=8, showarrow=False,
                text=f"<b>{r['Top_score']:.0f}%</b>  {r['Holder']}",
                font=dict(size=11.5, color="#ddd" if r["Top_score"] < 75 else "#0e1117"))
        fig2.update_layout(
            **BASE_LAYOUT, barmode="overlay", height=520, margin=dict(l=20, r=40, t=55, b=50),
            title=dict(text="Benchmarks proposed in place of SWE-bench: best score to date",
                       font=dict(size=15), x=0.0),
            xaxis=dict(title="Top score (%)  ·  the dim bar is the room left", gridcolor=GRID_COL, range=[0, 100]),
            yaxis=dict(categoryorder="array", categoryarray=list(sc["Benchmark"]), tickfont=dict(size=13)),
            legend=dict(**LEGEND_STYLE, orientation="h", y=-0.2, title="What it tests"),
            hovermode="closest",
        )
        st.plotly_chart(fig2, width="stretch")
        st.info(SUCC_INFO)
        st.caption(SUCC_CAPTION)

    else:
        LEGACY = {
            VIEWS[3]: ("GPQA", "GPQA Diamond score (%)"),
            VIEWS[4]: ("SWE_bench_Verified", "SWE-bench Verified score (%)"),
            VIEWS[5]: ("MATH", "MATH / AIME score (%)"),
            VIEWS[6]: ("MMLU", "MMLU score (%)"),
        }
        col_key, y_label = LEGACY[view]
        plot_df = bm_df.dropna(subset=[col_key]).copy()
        fig2 = go.Figure()
        for org in ["OpenAI", "Anthropic", "Google", "xAI", "DeepSeek"]:
            org_df = plot_df[plot_df["Org"] == org].sort_values("Date")
            if org_df.empty:
                continue
            color = ORG_COLORS.get(org, "#888")
            soft = (org_df["Confidence"] == "unverified") | (
                (col_key == "MMLU") & (org_df["MMLU_Instrument"] == "MMMLU")
            )
            fig2.add_trace(go.Scatter(
                x=org_df["Date"], y=org_df[col_key], mode="lines+markers", name=org,
                line=dict(color=color, width=2.5),
                marker=dict(size=10, color=[PLOT_BG if s else color for s in soft],
                            line=dict(color=color, width=2)),
                customdata=list(zip(org_df["Model"], org_df["Date"].dt.strftime("%b %Y"),
                                    org_df["Confidence"])),
                hovertemplate="<b>%{customdata[0]}</b><br>%{customdata[1]}<br>%{y:.1f}%"
                              "<br>Source status: %{customdata[2]}<extra></extra>",
            ))
            last = org_df.iloc[-1]
            fig2.add_annotation(x=last["Date"], y=last[col_key], text=f"  {last[col_key]:.0f}%",
                                showarrow=False, font=dict(size=11, color=color), xanchor="left")

        if col_key == "GPQA":
            fig2.add_hline(y=69.7, line_dash="dot", line_color="#555", line_width=1.5,
                           annotation_text="PhD expert level: 69.7%", annotation_position="bottom right",
                           annotation_font=dict(size=11, color="#666"))
            add_vline(fig2, "2026-09-04", "Dropped by Artificial Analysis as saturated", color="#e0a23c", anchor="right")
        if col_key == "SWE_bench_Verified":
            add_vline(fig2, "2026-02-23", "OpenAI stops reporting it", color="#e0524a", anchor="right")
        last_seen = plot_df["Date"].max()
        y_min = max(0, plot_df[col_key].min() - 8)
        y_max = min(105, plot_df[col_key].max() + 6)
        fig2.update_layout(
            **BASE_LAYOUT, margin=dict(l=70, r=120, t=55, b=60), height=540,
            title=dict(text=f"{view.replace('Retired: ', '')} (last frontier report found: {last_seen:%b %Y})",
                       font=dict(size=15), x=0.0),
            xaxis=dict(title="", gridcolor=GRID_COL, range=["2023-01-01", "2026-12-15"]),
            yaxis=dict(title=y_label, gridcolor=GRID_COL, range=[y_min, y_max]),
            hovermode="closest", legend=dict(**LEGEND_STYLE, title="Organization"),
        )
        st.plotly_chart(fig2, width="stretch")
        callouts = {
            "GPQA": (
                "**GPQA Diamond** topped out in a 93.6% to 94.6% band across four labs between "
                "February and June 2026, about 25 points above expert level. The last report "
                "found is Claude Mythos 5 (94.1%, June 2026), whose system card calls the test "
                "saturated. Artificial Analysis removed it from its index in September 2026."
            ),
            "SWE_bench_Verified": (
                "**SWE-bench Verified** ended as a validity failure, not a ceiling. OpenAI's audit "
                "of 138 hard tasks reportedly found flawed tests in at least 59%, and frontier "
                "models could reproduce reference fixes from a task ID. Points after February 2026 "
                "are vendor figures on a benchmark its creator had disowned; the last found is "
                "Claude Opus 5 at 96.0% in July 2026."
            ),
            "MATH": (
                "**MATH / AIME** hit its ceiling in 2024 to 2025. No launch from December 2025 "
                "onward was found reporting it; mathematics reporting moved to FrontierMath and "
                "research-level problem sets."
            ),
            "MMLU": (
                "**MMLU** saturated near 90% by 2024. Hollow markers are **MMMLU**, a multilingual "
                "variant labs switched to; it is a different test and should not be read as the "
                "same line."
            ),
        }
        st.info(callouts[col_key])
        st.caption(
            "Hollow markers are a different instrument (MMMLU). Cells with no traceable source "
            "were removed in the November 2026 revision, and two GPQA values that were wrong in "
            "the previous version were corrected against the labs' own tables."
        )


# ═════════════════════════════════════════════════════════════════════════════
# TAB — Who Measured It?
# ═════════════════════════════════════════════════════════════════════════════
with tab_who:
    st.markdown("### Same Model, Same Benchmark, Different Number")
    vi = D["vi"]
    GROUP_BLURB = {
        "Vendor vs independent": "The lab's own figure against a third party running the same benchmark.",
        "Lab vs lab": "The same model's score as printed in two different labs' launch tables.",
        "Same model different setup": "One model, one benchmark, with only the harness, effort level or scoring rule changed.",
    }
    grp = st.radio("Comparison", list(GROUP_BLURB), horizontal=True, label_visibility="collapsed")
    st.markdown(GROUP_BLURB[grp])
    sub = vi[vi["Group"] == grp].copy()
    sub["Row"] = sub["Benchmark"] + " · " + sub["Model"]
    sub["Gap"] = (sub["Value_A"] - sub["Value_B"]).abs()
    COL_A, COL_B = "#e07b4a", "#4c8ef5"
    figv = go.Figure()
    for _, r in sub.iterrows():
        figv.add_trace(go.Scatter(
            x=[r["Value_A"], r["Value_B"]], y=[r["Row"]] * 2, mode="lines",
            line=dict(color="#555", width=3), showlegend=False, hoverinfo="skip"))
        figv.add_annotation(
            x=max(r["Value_A"], r["Value_B"]), y=r["Row"], xanchor="left", xshift=12, showarrow=False,
            text=f"<b>{r['Gap']:.1f} pts</b>", font=dict(size=12, color="#ddd"))
    for which, colr, first in [("A", COL_A, True), ("B", COL_B, False)]:
        figv.add_trace(go.Scatter(
            x=sub[f"Value_{which}"], y=sub["Row"], mode="markers",
            name="First-listed source" if first else "Second-listed source",
            marker=dict(size=15, color=colr, line=dict(color=PLOT_BG, width=1.5)),
            customdata=list(zip(sub[f"Label_{which}"], sub["Note"].fillna(""))),
            hovertemplate="<b>%{customdata[0]}</b>: %{x:.1f}%<br>%{customdata[1]}<extra></extra>",
            showlegend=False))
    figv.update_layout(
        **BASE_LAYOUT, height=120 + 62 * len(sub), margin=dict(l=20, r=90, t=30, b=50),
        xaxis=dict(title="Score (%)", gridcolor=GRID_COL, range=[15, 108]),
        yaxis=dict(gridcolor=GRID_COL, autorange="reversed", tickfont=dict(size=12.5)),
        hovermode="closest",
    )
    st.plotly_chart(figv, width="stretch")
    a_lab = ", ".join(sorted({l.split(" (")[0] for l in sub["Label_A"]}))
    b_lab = ", ".join(sorted({l.split(" (")[0] for l in sub["Label_B"]}))
    st.markdown(
        f'<span style="color:{COL_A}">●</span> {a_lab} &nbsp;&nbsp; '
        f'<span style="color:{COL_B}">●</span> {b_lab}',
        unsafe_allow_html=True,
    )
    st.info(
        "**The setup now moves the score more than the model does.** Through April 2026, vendor "
        "and independent SWE-bench Pro figures ranged from agreement within a point or two to "
        "gaps of 8 and 15 points. Since then the two series have separated entirely: vendor "
        "claims reach 93% while the independent board's best is 61.5%, on different models, "
        "because no independent run exists for any Anthropic or OpenAI model released after April. The definition of success matters as much: on the ExploitGym security "
        "benchmark, GPT-5.5 captured 210 flags but only 120 by exploiting the intended bug. "
        "\"Independent\" now needs qualifying too: in November OpenAI announced assessments by "
        "four outside groups working inside the company, two of them paid by OpenAI, with "
        "OpenAI keeping redaction rights. Questions to ask of any score: who ran it, who paid, "
        "on which version, with what harness, and what counted as success?"
    )
    st.caption(
        "Vendor figures for the SWE-bench Pro pairs are from the labs' system cards and launch "
        "posts; the November 2026 lab-versus-lab figures were read through secondary summaries "
        "of those tables. Independent figures are from Scale Labs, ARC Prize and Vals."
    )


# ═════════════════════════════════════════════════════════════════════════════
# TAB — Task Time Horizons
# ═════════════════════════════════════════════════════════════════════════════
with tab_th:
    st.markdown("### AI Task Time Horizon (METR)")
    st.markdown(
        "The length of software task, measured in human working time, that a model completes "
        "at a given success rate. METR Time Horizon 1.1 suite, 228 tasks."
    )
    cA, cB, cC = st.columns([1.3, 1.2, 2.5])
    with cA:
        pct = st.radio("Success rate", ["50% success", "80% success"], horizontal=True, key="th_pct")
    with cB:
        start = st.radio("Start", ["From 2023", "From 2019"], horizontal=True, key="th_start")
    with cC:
        show_old = st.checkbox("Also show models measured only on the older suite (TH 1.0)", value=False)
    ycol = "p50_min" if pct.startswith("50") else "p80_min"
    is50 = ycol == "p50_min"

    main = th_df[th_df["Suite"] == "TH 1.1"].sort_values("Release_Date")
    old = th_df[th_df["Suite"] == "TH 1.0"].sort_values("Release_Date")
    fig = go.Figure()

    # unreliable zone (METR: above 16 h)
    y_top = 30000
    fig.add_shape(type="rect", xref="paper", x0=0, x1=1, yref="y", y0=960, y1=y_top,
                  fillcolor="rgba(224,82,74,0.07)", line_width=0, layer="below")
    fig.add_annotation(xref="paper", x=0.01, y=math.log10(1300), yref="y", xanchor="left",
                       text="Above 16 hours: METR says its suite cannot measure reliably",
                       showarrow=False, font=dict(size=11, color="#c9695f"))

    if is50:
        for _, r in main.iterrows():
            color = ORG_COLORS.get(r["Org"], "#888")
            fig.add_trace(go.Scatter(
                x=[r["Release_Date"]] * 2, y=[r["p50_ci_lo"], r["p50_ci_hi"]], mode="lines",
                line=dict(color=hex_to_rgba(color, 0.4), width=4), showlegend=False, hoverinfo="skip"))

    sota = main[main["SOTA"] == "yes"]
    if is50:
        fig.add_trace(go.Scatter(
            x=sota["Release_Date"], y=sota[ycol], mode="lines", name="Record at release",
            line=dict(color="#ddd", width=1.5, dash="dot"), hoverinfo="skip"))

    for org in main["Org"].unique():
        o = main[main["Org"] == org]
        color = ORG_COLORS.get(org, "#888")
        fig.add_trace(go.Scatter(
            x=o["Release_Date"], y=o[ycol], mode="markers", name=org,
            marker=dict(size=11, color=color, line=dict(color=PLOT_BG, width=1.5)),
            customdata=[
                f"<b>{r['Model']}</b><br>{r['Release_Date']:%b %d, %Y}"
                f"<br>50% horizon: {fmt_minutes(r['p50_min'])}"
                f"<br>95% CI: {fmt_minutes(r['p50_ci_lo'])} to {fmt_minutes(r['p50_ci_hi'])}"
                f"<br>80% horizon: {fmt_minutes(r['p80_min'])}"
                for _, r in o.iterrows()
            ],
            hovertemplate="%{customdata}<extra></extra>"))
    if show_old:
        fig.add_trace(go.Scatter(
            x=old["Release_Date"], y=old[ycol], mode="markers", name="Older suite only (TH 1.0)",
            marker=dict(size=10, symbol="circle-open", color=[ORG_COLORS.get(o, "#888") for o in old["Org"]],
                        line=dict(width=2)),
            customdata=[f"<b>{r['Model']}</b> ({r['Org']})<br>TH 1.0, not comparable point for point"
                        f"<br>50%: {fmt_minutes(r['p50_min'])} · 80%: {fmt_minutes(r['p80_min'])}"
                        for _, r in old.iterrows()],
            hovertemplate="%{customdata}<extra></extra>"))

    # labels for record-setting models
    lab_df = sota if start == "From 2019" else sota[sota["Release_Date"] >= "2023-01-01"]
    for i, (_, r) in enumerate(lab_df.iterrows()):
        short = (r["Model"].replace("Claude ", "").replace("GPT-", "").replace("Gemini ", "")
                 .replace(" (0314)", "").replace(" (davinci-002)", "").replace(" Turbo Instruct", ""))
        fig.add_annotation(
            x=r["Release_Date"], y=math.log10(r[ycol]), text=short, showarrow=False,
            font=dict(size=9.5, color=hex_to_rgba(ORG_COLORS.get(r["Org"], "#888"), 0.95)),
            xanchor="right", xshift=-8, yshift=7)

    if is50:
        # GPT-5.6 Sol: three readings of one evaluation
        sx = pd.Timestamp("2026-07-09")
        fig.add_trace(go.Scatter(
            x=[sx, sx, sx], y=[11.3 * 60, 71 * 60, 270 * 60], mode="lines+markers",
            name="GPT-5.6 Sol: depends how cheating is scored",
            line=dict(color="#10a37f", width=2, dash="dot"),
            marker=dict(size=11, symbol="x", color="#10a37f"),
            customdata=["Cheating runs counted as failures: about 11.3 h (CI 5 to 40 h)",
                        "Cheating runs discarded: 71 h (CI 13 to 11,400 h)",
                        "Cheating runs counted as successes: beyond 270 h"],
            hovertemplate="<b>GPT-5.6 Sol</b> (METR, 26 Jun 2026)<br>%{customdata}"
                          "<br>METR: none of these is a robust measurement<extra></extra>"))
        for yv, t in [(11.3 * 60, "11 h"), (71 * 60, "71 h"), (270 * 60, "270 h+")]:
            fig.add_annotation(x=sx, y=math.log10(yv), text=t, showarrow=False, xanchor="left",
                               xshift=9, font=dict(size=10, color="#10a37f"))
    add_vline(fig, "2026-09-08", "Series frozen<br>8 Sep 2026", color="#888", y_text=0.02)

    y_lo = 0.008 if start == "From 2019" else (1.5 if is50 else 0.4)
    ticks = [0.0167, 0.1, 1, 5, 15, 60, 240, 960, 2880, 10080]
    tlabels = ["1 sec", "6 sec", "1 min", "5 min", "15 min", "1 hr", "4 hr", "16 hr", "2 days", "1 week"]
    fig.update_layout(
        **BASE_LAYOUT, margin=dict(l=70, r=40, t=55, b=50), height=660,
        title=dict(text=f"METR task time horizon at {pct}", font=dict(size=15), x=0.0),
        xaxis=dict(title="Model release date", gridcolor=GRID_COL,
                   range=["2018-10-01" if start == "From 2019" else "2022-11-01", "2026-12-15"]),
        yaxis=dict(title=f"Task length at {pct}", type="log",
                   range=[math.log10(y_lo), math.log10(y_top)], gridcolor=GRID_COL,
                   tickvals=ticks, ticktext=tlabels),
        hovermode="closest", legend=dict(**LEGEND_STYLE, x=0.99, xanchor="right", y=0.02, yanchor="bottom"),
    )
    st.plotly_chart(fig, width="stretch")

    def _row(name):
        return main[main["Model"] == name].iloc[0]

    g4, o45, o46, myth = _row("GPT-4 (0314)"), _row("Claude Opus 4.5"), _row("Claude Opus 4.6"), _row("Claude Mythos Preview")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("GPT-4 · Mar 2023", fmt_minutes(g4[ycol]), "baseline", delta_color="off")
    for c, r, lab in [(c2, o45, "Opus 4.5 · Nov 2025"), (c3, o46, "Opus 4.6 · Feb 2026"),
                      (c4, myth, "Mythos Preview · Apr 2026")]:
        c.metric(lab, fmt_minutes(r[ycol]), f"↑ {r[ycol] / g4[ycol]:.0f}× GPT-4")

    st.info(
        "**The curve kept climbing until the ruler ran out.** METR's last entry is Claude Mythos "
        "Preview at about 17.4 hours, above the 16-hour limit METR itself sets for its suite; "
        "the page was frozen on 8 September 2026 with no successor named. The one later "
        "evaluation, GPT-5.6 Sol, gave **11 hours, 71 hours or more than 270 hours** depending on "
        "how runs where the model cheated are scored. METR's current doubling-time estimate is "
        "**about 129 days** for 2023 onward (CI 104 to 158) and about 6 to 7 months over the "
        "whole series. Switch to 80% success for a much less dramatic picture."
    )
    st.caption(
        "Values copied from METR's published data file for Time Horizon 1.1 (bars are 95% "
        "confidence intervals). The previous version of this chart mixed older data vintages: "
        "12 of its 14 rows had a wrong value or date. Tasks are clean, well-specified software "
        "problems; in METR's own maintainer review, Claude Sonnet 4.5's horizon was about 50 "
        "minutes by automated grading and about 8 minutes by what maintainers would merge."
    )

    # ── After METR: what fills the gap ─────────────────────────────────────
    st.divider()
    st.markdown("### After METR: What Fills the Gap?")
    st.markdown(
        "METR has named **no replacement** for this series. Its page says only that it is no "
        "longer actively updated. These are the instruments people now point to instead; "
        "none of them continues the curve above."
    )
    left, right = st.columns([3, 2])
    with left:
        rows = []
        for _, r in D["after"].iterrows():
            cont = r["Continues_the_curve"]
            colr = "#e0a23c" if cont.startswith("Partly") else "#e0524a"
            head, _, tail = cont.partition(": ")
            rows.append(
                f"<tr><td class='who'><b>{r['Instrument']}</b><br><span>{r['Run_by']}</span></td>"
                f"<td>{r['Measures']}<br><span>Latest: {r['Latest_reading']}</span> "
                f"<a href='{r['Source']}' target='_blank'>source</a></td>"
                f"<td><span class='chip' style='background:{hex_to_rgba(colr, 0.2)};color:{colr};"
                f"border:1px solid {colr}'>{head}</span><br><span>{tail}</span></td></tr>"
            )
        st.markdown(
            """
<style>
table.after { width:100%; border-collapse:collapse; font-size:0.9rem; }
table.after th { text-align:left; color:#888; font-weight:500; padding:8px 10px; border-bottom:1px solid #333; }
table.after td { padding:10px; border-bottom:1px solid #23262f; vertical-align:top; color:#d0d0d0; }
table.after td span { color:#888; font-size:0.82rem; }
table.after td.who { white-space:nowrap; }
table.after .chip { padding:2px 9px; border-radius:12px; font-size:0.78rem !important; font-weight:600; white-space:nowrap; }
table.after a { color:#4c8ef5; font-size:0.8rem; text-decoration:none; }
</style>
<table class="after"><tr><th>Instrument</th><th>What it measures</th><th>Continues the curve?</th></tr>
"""
            + "".join(rows)
            + "</table>",
            unsafe_allow_html=True,
        )
    with right:
        ex = D["exph"]
        fige = go.Figure()
        for model in ex["Model"].unique():
            g = ex[ex["Model"] == model]
            colr = ORG_COLORS.get(g["Org"].iloc[0], "#888")
            fige.add_trace(go.Bar(
                x=g["Assumption"].str.replace(": ", ":<br>"), y=g["Expenditure_horizon_usd"],
                name=model, marker_color=colr,
                text=[f"${v:,.0f}" for v in g["Expenditure_horizon_usd"]], textposition="outside",
                hovertemplate=model + ": $%{y:,.0f}<extra></extra>"))
        fige.update_layout(
            **BASE_LAYOUT, barmode="group", height=470, margin=dict(l=60, r=20, t=70, b=40),
            title=dict(text="METR's expenditure horizon (NanoGPT speedrun),<br>by assumed cost of human work",
                       font=dict(size=14), x=0.0),
            xaxis=dict(gridcolor=GRID_COL, tickfont=dict(size=11)),
            yaxis=dict(title="Expenditure horizon (USD, log scale)", type="log", gridcolor=GRID_COL,
                       range=[math.log10(60), math.log10(60000)],
                       tickvals=[100, 1000, 10000], ticktext=["$100", "$1K", "$10K"]),
            legend=dict(**LEGEND_STYLE, x=0.01, y=0.99),
        )
        st.plotly_chart(fige, width="stretch")
    st.info(
        "**Why there is no successor yet.** METR's July methods note gives the reason: without a "
        "token cap, success rates on its tasks are so high that time horizons become impossible "
        "to calculate, and benchmarks grounded in human performance stop being useful once "
        "models pass it. Its proposed alternative, the **expenditure horizon**, asks at what "
        "budget an agent stops beating a human with the same money. On its one test so far the "
        "answer moves about **100-fold** with the assumed price of human work, and METR concluded "
        "autonomous agents have had minimal effect on that task's progress. Forecasters have "
        "moved to composite indices and lab-internal evidence instead."
    )
    st.caption(
        "Expenditure-horizon figures are from METR's 21 July 2026 post; METR does not describe "
        "the metric as a replacement for time horizons. The Remote Labor Index and FrontierSWE "
        "readings are vendor-reported and reached us through secondary sources."
    )


# ═════════════════════════════════════════════════════════════════════════════
# TAB — Cost & Value
# ═════════════════════════════════════════════════════════════════════════════
with tab_cost:
    st.markdown("### What Does Capability Cost?")
    st.markdown(
        "List prices per million tokens, how they moved from one version to the next, and "
        "what each dollar buys on Epoch's capability index and on a measured task."
    )
    pr = D["prices"].copy()
    pr["Blended"] = (3 * pr["Input"] + pr["Output"]) / 4
    LAB_SEQ = ["OpenAI", "Anthropic", "Google", "xAI", "Meta", "DeepSeek", "Moonshot", "Z.ai", "Alibaba"]

    def _frontier(df, xcol, ycol):
        """Rows where nothing cheaper scores as high (the efficient frontier)."""
        best, keep = float("-inf"), []
        for idx, r in df.sort_values([xcol, ycol], ascending=[True, False]).iterrows():
            if r[ycol] > best:
                keep.append(idx)
                best = r[ycol]
        return df.loc[keep]

    # ── 1. Current list prices ─────────────────────────────────────────────
    cur = pr[pr["Current"] == "yes"].copy()
    cur["rank"] = cur["Org"].map({o: i for i, o in enumerate(LAB_SEQ)})
    cur = cur.sort_values(["rank", "Output"], ascending=[True, False])
    cur["Label"] = cur["Model"] + "  ·  " + cur["Org"]
    figc = go.Figure()
    for col, name, alpha in [("Input", "Input, per million tokens", 0.45), ("Output", "Output, per million tokens", 1.0)]:
        figc.add_trace(go.Bar(
            y=cur["Label"], x=cur[col], orientation="h", name=name,
            marker_color=[hex_to_rgba(ORG_COLORS.get(o, "#888"), alpha) for o in cur["Org"]],
            text=[f"${v:,.2f}" for v in cur[col]], textposition="outside", textfont=dict(size=10.5),
            customdata=list(zip(cur["Verdict"], cur["Note"].fillna(""))),
            hovertemplate="%{y}<br>" + name + ": $%{x:,.2f}<br>Source: %{customdata[0]}"
                          "<br>%{customdata[1]}<extra></extra>"))
    figc.update_layout(
        **BASE_LAYOUT, barmode="group", height=130 + 44 * len(cur), margin=dict(l=20, r=60, t=55, b=50),
        title=dict(text="List prices today: input (pale) and output (solid), US dollars per million tokens",
                   font=dict(size=15), x=0.0),
        xaxis=dict(type="log", gridcolor=GRID_COL, title="US dollars per million tokens (log scale)",
                   tickvals=[0.1, 0.3, 1, 3, 10, 30, 100], ticktext=["$0.10", "$0.30", "$1", "$3", "$10", "$30", "$100"]),
        yaxis=dict(autorange="reversed", categoryorder="array", categoryarray=list(cur["Label"]),
                   tickfont=dict(size=12)),
        showlegend=False,
    )
    st.plotly_chart(figc, width="stretch")

    # ── 2. Price by generation, like for like ──────────────────────────────
    left, right = st.columns(2)
    with left:
        lines = pr.dropna(subset=["Line"]).sort_values("Release_Date")
        figg = go.Figure()
        for line in lines["Line"].unique():
            g = lines[lines["Line"] == line]
            if len(g) < 2:
                continue
            colr = ORG_COLORS.get(g["Org"].iloc[0], "#888")
            dash = "solid" if g["Line_Rank"].iloc[0] == 1 else "dot"
            figg.add_trace(go.Scatter(
                x=g["Release_Date"], y=g["Output"], mode="lines+markers", name=line,
                line=dict(color=colr, width=2, dash=dash, shape="hv"),
                marker=dict(size=7, color=colr),
                customdata=list(zip(g["Model"], g["Input"])),
                hovertemplate="<b>%{customdata[0]}</b><br>%{x|%b %Y}<br>Output $%{y:,.2f} · "
                              "input $%{customdata[1]:,.2f} per million tokens<extra></extra>"))
        figg.update_layout(
            **BASE_LAYOUT, height=560, margin=dict(l=60, r=20, t=70, b=170),
            title=dict(text="Same product line, version to version:<br>output price at launch",
                       font=dict(size=14), x=0.0),
            xaxis=dict(gridcolor=GRID_COL, range=["2023-01-01", "2026-12-20"]),
            yaxis=dict(type="log", gridcolor=GRID_COL, title="Output, US dollars per million tokens",
                       tickvals=[0.3, 1, 3, 10, 30, 100], ticktext=["$0.30", "$1", "$3", "$10", "$30", "$100"]),
            legend=dict(**LEGEND_STYLE, orientation="h", y=-0.2, font_size=11), hovermode="closest",
        )
        st.plotly_chart(figg, width="stretch")
    with right:
        # cheapest way to buy a fixed level of capability, over time
        ev = pr.dropna(subset=["ECI"]).sort_values("Release_Date")
        figf = go.Figure()
        levels = [(130, "GPT-4o level (ECI 128+)", 128, "#9aa0aa"), (150, "GPT-5 level (ECI 150+)", 150, "#e0a23c"),
                  (160, "GPT-5.4 Pro level (ECI 160+)", 160, "#10a37f")]
        fall = {}
        for _, name, thr, colr in levels:
            g = ev[ev["ECI"] >= thr]
            if g.empty:
                continue
            g = g.assign(Cheapest=g["Blended"].cummin())
            steps = g[g["Blended"] == g["Cheapest"]].drop_duplicates("Cheapest")
            figf.add_trace(go.Scatter(
                x=list(steps["Release_Date"]) + [AS_OF], y=list(steps["Cheapest"]) + [steps["Cheapest"].iloc[-1]],
                mode="lines+markers", name=name, line=dict(color=colr, width=2.5, shape="hv"),
                marker=dict(size=7), customdata=list(steps["Model"]) + [steps["Model"].iloc[-1]],
                hovertemplate="<b>%{customdata}</b><br>%{x|%b %Y}<br>$%{y:,.2f} per million tokens (blended)<extra></extra>"))
            fall[thr] = (steps["Cheapest"].iloc[0] / steps["Cheapest"].iloc[-1],
                         (AS_OF - steps["Release_Date"].iloc[0]).days / 30.44, steps["Model"].iloc[-1])
        figf.update_layout(
            **BASE_LAYOUT, height=560, margin=dict(l=60, r=20, t=70, b=170),
            title=dict(text="Cheapest way to buy a fixed capability level:<br>lowest blended price at or above each index score",
                       font=dict(size=14), x=0.0),
            xaxis=dict(gridcolor=GRID_COL, range=["2024-03-01", "2026-12-20"]),
            yaxis=dict(type="log", gridcolor=GRID_COL, title="Blended US dollars per million tokens",
                       tickvals=[0.1, 0.3, 1, 3, 10, 30], ticktext=["$0.10", "$0.30", "$1", "$3", "$10", "$30"]),
            legend=dict(**LEGEND_STYLE, orientation="h", y=-0.2, font_size=11), hovermode="closest",
        )
        st.plotly_chart(figf, width="stretch")

    # ── 3. Value: capability per dollar ────────────────────────────────────
    basis = st.radio(
        "Price basis for the value chart",
        ["Blended (3 parts input to 1 part output)", "Output price only"],
        horizontal=True, key="cost_basis",
    )
    xcol = "Blended" if basis.startswith("Blended") else "Output"
    val = pr.dropna(subset=["ECI"]).copy()
    val = val[val["Release_Date"] >= "2025-11-01"]
    figv = go.Figure()
    fr = _frontier(val, xcol, "ECI").sort_values(xcol)
    figv.add_trace(go.Scatter(
        x=fr[xcol], y=fr["ECI"], mode="lines", name="Best capability at each price",
        line=dict(color="#ddd", width=1.5, dash="dot", shape="hv"), hoverinfo="skip"))
    for org in LAB_SEQ:
        g = val[val["Org"] == org]
        if g.empty:
            continue
        colr = ORG_COLORS.get(org, "#888")
        on = g.index.isin(fr.index)
        figv.add_trace(go.Scatter(
            x=g[xcol], y=g["ECI"], mode="markers+text", name=org,
            marker=dict(size=[13 if o else 9 for o in on], color=colr,
                        line=dict(color=["#fff" if o else PLOT_BG for o in on], width=1.5)),
            text=[m.replace("Claude ", "").replace("DeepSeek ", "") if o else "" for m, o in zip(g["Model"], on)],
            textposition="top center", textfont=dict(size=10, color="#bbb"),
            customdata=list(zip(g["Model"], g["Input"], g["Output"], g["Release_Date"].dt.strftime("%b %Y"))),
            hovertemplate="<b>%{customdata[0]}</b> (" + org + ", %{customdata[3]})<br>ECI %{y:.1f}"
                          "<br>Input $%{customdata[1]:,.2f} · output $%{customdata[2]:,.2f}<extra></extra>"))
    figv.update_layout(
        **BASE_LAYOUT, height=560, margin=dict(l=70, r=40, t=55, b=60),
        title=dict(text="Value: capability index against price, models released since November 2025",
                   font=dict(size=15), x=0.0),
        xaxis=dict(type="log", gridcolor=GRID_COL,
                   title=("Blended" if xcol == "Blended" else "Output") + " US dollars per million tokens (log scale)",
                   tickvals=[0.1, 0.3, 1, 3, 10, 30, 100], ticktext=["$0.10", "$0.30", "$1", "$3", "$10", "$30", "$100"]),
        yaxis=dict(title="Epoch Capabilities Index", gridcolor=GRID_COL),
        legend=dict(**LEGEND_STYLE, x=0.99, xanchor="right", y=0.02, yanchor="bottom"), hovermode="closest",
    )
    st.plotly_chart(figv, width="stretch")

    # ── 4. Measured cost of a task ─────────────────────────────────────────
    ac = D["arccost"]
    ac = ac[ac["Date"] >= "2026-06-01"]
    figa2 = go.Figure()
    fa = _frontier(ac, "Cost_per_task_usd", "ARC_AGI_2").sort_values("Cost_per_task_usd")
    figa2.add_trace(go.Scatter(
        x=fa["Cost_per_task_usd"], y=fa["ARC_AGI_2"], mode="lines", name="Best score at each cost",
        line=dict(color="#ddd", width=1.5, dash="dot", shape="hv"), hoverinfo="skip"))
    for org in LAB_SEQ:
        g = ac[ac["Org"] == org]
        if g.empty:
            continue
        colr = ORG_COLORS.get(org, "#888")
        on = g.index.isin(fa.index)
        figa2.add_trace(go.Scatter(
            x=g["Cost_per_task_usd"], y=g["ARC_AGI_2"], mode="markers+text", name=org,
            marker=dict(size=[12 if o else 7 for o in on], color=hex_to_rgba(colr, 0.85),
                        line=dict(color=["#fff" if o else PLOT_BG for o in on], width=1.2)),
            text=[c.replace("Claude ", "").replace("DeepSeek ", "") if o else "" for c, o in zip(g["Config"], on)],
            textposition="top left", textfont=dict(size=9.5, color="#bbb"),
            customdata=g["Config"],
            hovertemplate="<b>%{customdata}</b><br>ARC-AGI-2 %{y:.1f}%<br>$%{x:,.3f} per task<extra></extra>"))
    figa2.update_layout(
        **BASE_LAYOUT, height=540, margin=dict(l=70, r=40, t=55, b=60),
        title=dict(text="Measured, not listed: what one ARC-AGI-2 task cost to run (models since June 2026, every effort setting)",
                   font=dict(size=15), x=0.0),
        xaxis=dict(type="log", gridcolor=GRID_COL, title="US dollars per task, as run by ARC Prize (log scale)",
                   tickvals=[0.01, 0.03, 0.1, 0.3, 1, 3, 10], ticktext=["$0.01", "$0.03", "$0.10", "$0.30", "$1", "$3", "$10"]),
        yaxis=dict(title="ARC-AGI-2 score (%)", gridcolor=GRID_COL, range=[0, 102]),
        legend=dict(**LEGEND_STYLE, x=0.99, xanchor="right", y=0.02, yanchor="bottom"), hovermode="closest",
    )
    st.plotly_chart(figa2, width="stretch")

    # ── 5. Same list price, different bill ─────────────────────────────────
    aa = D["aacost"].sort_values("AA_Index", ascending=False)
    aa["Label"] = aa["Model"] + "  ·  list $" + aa["Input"].map("{:g}".format) + " / $" + aa["Output"].map("{:g}".format)
    figb = go.Figure(go.Bar(
        y=aa["Label"], x=aa["Cost_to_run_usd"], orientation="h",
        marker_color=[ORG_COLORS.get(o, "#888") for o in aa["Org"]],
        text=[f"${v:,.0f}" for v in aa["Cost_to_run_usd"]], textposition="outside",
        customdata=list(zip(aa["AA_Index"], aa["Effort"], aa["Cost_per_task_usd"])),
        hovertemplate="%{y}<br>Total to run the index: $%{x:,.0f}<br>Index score %{customdata[0]} at "
                      "%{customdata[1]} effort · $%{customdata[2]:.2f} per task<extra></extra>"))
    figb.update_layout(
        **BASE_LAYOUT, height=470, margin=dict(l=20, r=70, t=55, b=50),
        title=dict(text="Same list price, different bill: total cost to run one evaluation suite (Artificial Analysis index, top ten models)",
                   font=dict(size=15), x=0.0),
        xaxis=dict(gridcolor=GRID_COL, title="US dollars to run the full index once", range=[0, 25500]),
        yaxis=dict(autorange="reversed", categoryorder="array", categoryarray=list(aa["Label"]), tickfont=dict(size=12)),
    )
    st.plotly_chart(figb, width="stretch")

    # ── Cards and reading notes ────────────────────────────────────────────
    lead = val.loc[val["ECI"].idxmax()]
    near = val[(val["ECI"] >= lead["ECI"] - 10) & (val["Blended"] < lead["Blended"])]
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Top of the index", f"${lead['Blended']:,.2f}", f"{lead['Model']}, blended per million tokens", delta_color="off")
    if not near.empty:
        cheap = near.loc[near["Blended"].idxmin()]
        c2.metric("Cheapest within 10 index points", f"${cheap['Blended']:,.2f}",
                  f"{cheap['Model']} · {lead['Blended'] / cheap['Blended']:.0f}× cheaper", delta_color="off")
    if 150 in fall:
        ratio, months, model = fall[150]
        c3.metric("GPT-5-level capability", f"{ratio:.0f}× cheaper", f"in {months:.0f} months (now {model})", delta_color="off")
    top_run = ac.loc[ac["ARC_AGI_2"].idxmax()]
    eff = fa[fa["ARC_AGI_2"] >= 90]
    if not eff.empty:
        e = eff.iloc[0]
        c4.metric("Cheapest run above 90% on ARC-AGI-2", f"${e['Cost_per_task_usd']:.2f} a task",
                  f"{e['Config']} · top score costs ${top_run['Cost_per_task_usd']:.2f}", delta_color="off")

    st.info(
        "**The price of a fixed level of capability is collapsing; the price of the frontier is "
        "not.** The top tier at OpenAI and Anthropic lists at $8 per million input tokens, a "
        "little below the $10 to $15 that flagships cost in 2024. What changed is everything "
        "below it: a model within a point of the March 2026 frontier on Epoch's index now "
        "lists at 10 cents per million input tokens. Within a product line, prices mostly held "
        "or fell from version to version; Anthropic's Opus line went from $75 to $20 per "
        "million output tokens. **List price is a poor guide to the bill.** Two flagships at "
        "the same $8 / $40 cost $4,530 and $22,191 to run the same evaluation suite, about "
        "five times apart. For real work, compare cost per finished task."
    )
    st.caption(
        "List prices are each provider's published standard rate at launch for the base context "
        "window, with no batch, cache or volume discount; hover shows where each was read. "
        "\"Blended\" weights input three to one over output, a common convention; agentic "
        "coding often runs far more input-heavy, and cached input is much cheaper. A price per "
        "token is not a cost per task: reasoning models can spend many times more tokens on the "
        "same job, which is why the last chart uses ARC Prize's measured cost per task, taken "
        "from its data file of 19 November 2026. Index scores are from Epoch's file of the same "
        "date; models Epoch has not scored do not appear on the value chart. The cost-to-run "
        "figures are Artificial Analysis's own, for its index version 5.0.1 at each model's "
        "top effort setting; it prices Gemini 4 Carbon at the $4 / $20 rate that takes effect "
        "on 1 December 2026, where the first chart shows the $2 / $10 introductory price."
    )


# ═════════════════════════════════════════════════════════════════════════════
# TAB — Benchmarks vs Reality
# ═════════════════════════════════════════════════════════════════════════════
with tab_real:
    st.markdown("### What Happened Outside the Benchmarks")

    ad = D["adopt"].sort_values("Date")
    SERIES_COL = {
        "GitHub: pull requests started by agents": "#ffffff",
        "Google: share of new code AI-generated": ORG_COLORS["Google"],
        "Anthropic: share of merged production code": ORG_COLORS["Anthropic"],
        "Microsoft: share of repo code written by AI": ORG_COLORS["Microsoft"],
    }
    figa = go.Figure()
    for s, colr in SERIES_COL.items():
        g = ad[ad["Series"] == s]
        measured = (g["Kind"] == "Measured").all()
        figa.add_trace(go.Scatter(
            x=g["Date"], y=g["Value"], mode="lines+markers+text",
            name=s + (" (measured)" if measured else " (executive statement)"),
            line=dict(color=colr, width=3 if measured else 2, dash=None if measured else "dash"),
            marker=dict(size=11, color=colr, line=dict(color=PLOT_BG, width=1.5)),
            text=[f"{v:.0f}%" for v in g["Value"]], textposition="top center",
            textfont=dict(size=11, color=colr),
            customdata=g["Definition"],
            hovertemplate="%{x|%b %Y}: %{y:.0f}%<br>%{customdata}<extra></extra>"))
    figa.update_layout(
        **BASE_LAYOUT, height=440, margin=dict(l=70, r=40, t=55, b=40),
        title=dict(text="Adoption: how much code comes from AI", font=dict(size=15), x=0.0),
        xaxis=dict(gridcolor=GRID_COL, range=["2024-08-01", "2026-12-15"]),
        yaxis=dict(title="Share (%)", gridcolor=GRID_COL, range=[0, 100]),
        legend=dict(**LEGEND_STYLE, x=0.01, y=0.99), hovermode="closest",
    )
    st.plotly_chart(figa, width="stretch")

    left, right = st.columns([3, 2])
    with left:
        pr = D["prod"].copy()
        KIND_COL = {"Activity": "#4c8ef5", "Delivered work": "#10a37f", "Friction": "#e0524a"}
        pr["Label"] = pr["Metric"] + "  ·  " + pr["Study"].str.replace(r" \(.*\)", "", regex=True)
        figp = go.Figure()
        for kind, colr in KIND_COL.items():
            g = pr[pr["Kind"] == kind]
            figp.add_trace(go.Bar(
                y=g["Label"], x=g["Change_pct"], orientation="h", name=kind, marker_color=colr,
                text=[f"{v:+.0f}%" for v in g["Change_pct"]], textposition="outside",
                customdata=g["Note"].fillna(""),
                hovertemplate="%{y}: %{x:+.1f}%<br>%{customdata}<extra></extra>"))
        figp.update_layout(
            **BASE_LAYOUT, height=470, margin=dict(l=20, r=40, t=55, b=40),
            title=dict(text="After teams adopt coding agents", font=dict(size=15), x=0.0),
            xaxis=dict(title="Change (%)", gridcolor=GRID_COL, range=[-25, 72], zerolinecolor="#666"),
            yaxis=dict(autorange="reversed", categoryorder="array", categoryarray=list(pr["Label"]),
                       tickfont=dict(size=11.5)),
            legend=dict(**LEGEND_STYLE, orientation="h", y=-0.16),
        )
        st.plotly_chart(figp, width="stretch")
    with right:
        up = D["uplift"]
        figu = go.Figure()
        figu.add_trace(go.Scatter(
            x=up["Time_change_pct"], y=up["Study"].str.replace(": ", ":<br>"), mode="markers",
            marker=dict(size=14, color=["#e0524a", "#10a37f", "#10a37f"]),
            error_x=dict(type="data", symmetric=False,
                         array=up["CI_hi"] - up["Time_change_pct"],
                         arrayminus=up["Time_change_pct"] - up["CI_lo"],
                         color="#888", thickness=2, width=6),
            customdata=list(zip(up["Sample"], up["Period"], up["Note"])),
            hovertemplate="%{x:+.0f}% time<br>%{customdata[0]}, %{customdata[1]}"
                          "<br>%{customdata[2]}<extra></extra>", showlegend=False))
        figu.add_vline(x=0, line_color="#666", line_width=1)
        figu.update_layout(
            **BASE_LAYOUT, height=470, margin=dict(l=20, r=30, t=55, b=40),
            title=dict(text="Controlled trials: time to finish a task", font=dict(size=15), x=0.0),
            xaxis=dict(title="← faster with AI     slower with AI →", gridcolor=GRID_COL, range=[-45, 45]),
            yaxis=dict(autorange="reversed", tickfont=dict(size=11.5)),
        )
        st.plotly_chart(figu, width="stretch")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Automated grader says", "50 min", "Sonnet 4.5 horizon, SWE-bench", delta_color="off")
    c2.metric("Maintainers would merge", "8 min", "same model, same patches", delta_color="off")
    c3.metric("Review comments written by AI", "23%", "Harvard panel of 655 firms", delta_color="off")
    c4.metric("Incoming open-source PRs judged AI slop", "25%", "Linux Foundation, Oct 2026", delta_color="off")

    st.markdown("##### Inside a frontier lab: tasks agents finished with no human intervention (OpenAI, Aug to Oct 2026)")
    d1, d2, d3, d4 = st.columns(4)
    d1.metric("Monitoring training runs", "79%", "OpenAI's own telemetry", delta_color="off")
    d2.metric("Launching training runs", "35%", "OpenAI's own telemetry", delta_color="off")
    d3.metric("Inference and serving code", "25%", "OpenAI's own telemetry", delta_color="off")
    d4.metric("AI progress at Anthropic", "about 1.9×", "its earlier rate (METR, CI 1.5 to 2.8)", delta_color="off")

    st.info(
        "**Activity is up sharply; delivered work is up a little; review is the new bottleneck.** "
        "Agents went from starting 17% of GitHub pull requests in March 2026 to more than 40% in "
        "September. Across 655 firms, adopting agents raised pull requests about 36% and lines of "
        "code 44%, while issues resolved rose about 14% (borderline significant) and review "
        "time rose 56%. Benchmarks score self-contained task "
        "completion; teams are limited by review, integration and the defects that surface later."
    )
    st.caption(
        "Company code-share figures are executive statements with differing definitions, not "
        "audited measurements. GitHub publishes only the March and September figures, so the line "
        "between them is drawn, not measured; it counts pull requests with a detectable agent, so "
        "it is a floor. Faros is vendor telemetry. METR considers its 2026 follow-up unreliable "
        "because many developers declined to do tasks without AI, and has dropped the design; "
        "the 2025 result describes experienced maintainers on their own repositories in early 2025. "
        "The OpenAI figures are the company's own measurements of its internal agents, from a "
        "post of 18 November 2026, reported as midpoints of a range."
    )


# ═════════════════════════════════════════════════════════════════════════════
# TAB — Jobs & Education
# ═════════════════════════════════════════════════════════════════════════════
with tab_jobs:
    st.markdown("### The Entry Door Narrowed; the Building Did Not Empty")
    lab = D["labor"]
    left, right = st.columns([3, 2])
    with left:
        ix = lab[lab["Series"].str.startswith("Indeed")].sort_values("Date")
        figi = go.Figure()
        figi.add_trace(go.Scatter(
            x=ix["Date"], y=ix["Value"], mode="lines",
            line=dict(color="#4c8ef5", width=3),
            hovertemplate="%{x|%b %Y}: %{y:.1f}<extra></extra>", showlegend=False))
        peak, low, last = ix.loc[ix["Value"].idxmax()], ix.loc[ix["Value"].idxmin()], ix.iloc[-1]
        for r, txt, pos in [(peak, f"Peak {peak['Value']:.0f}", "middle right"),
                            (low, f"Low {low['Value']:.0f}", "bottom center"),
                            (last, f"{last['Value']:.0f}", "top center")]:
            figi.add_trace(go.Scatter(
                x=[r["Date"]], y=[r["Value"]], mode="markers+text", text=[txt], textposition=pos,
                textfont=dict(size=12, color="#9cc0ff"), showlegend=False, hoverinfo="skip",
                marker=dict(size=10, color="#4c8ef5", line=dict(color=PLOT_BG, width=1.5))))
        figi.add_hline(y=100, line_dash="dot", line_color="#555",
                       annotation_text="Pre-pandemic level (Feb 2020 = 100)",
                       annotation_font=dict(size=11, color="#777"))
        add_vline(figi, "2022-11-30", "ChatGPT", color="#666")
        figi.update_layout(
            **BASE_LAYOUT, height=430, margin=dict(l=70, r=30, t=55, b=40),
            title=dict(text="US software development job postings (Indeed index, monthly)", font=dict(size=15), x=0.0),
            xaxis=dict(gridcolor=GRID_COL, range=["2021-11-01", "2027-02-01"]),
            yaxis=dict(title="Index", gridcolor=GRID_COL, range=[40, 250]),
        )
        st.plotly_chart(figi, width="stretch")
    with right:
        stf = lab[lab["Series"].str.startswith("Stanford")].sort_values("Date")
        figs = go.Figure(go.Bar(
            x=[f"Data to {d:%b %Y}" for d in stf["Date"]], y=-stf["Value"],
            marker_color=["#b0553f", "#e0524a"], text=[f"−{v:.0f}%" for v in stf["Value"]],
            textposition="outside", textfont=dict(size=16),
            hovertemplate="%{x}: %{y:.0f}% vs less-exposed peers<extra></extra>"))
        figs.update_layout(
            **BASE_LAYOUT, height=430, margin=dict(l=60, r=30, t=55, b=40),
            title=dict(text="Ages 22 to 25 in AI-exposed jobs,<br>employment vs less-exposed peers",
                       font=dict(size=14), x=0.0),
            xaxis=dict(gridcolor=GRID_COL), yaxis=dict(title="Gap (%)", gridcolor=GRID_COL, range=[-26, 0]),
        )
        st.plotly_chart(figs, width="stretch")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("CS starting salary, class of 2026", "$81,535", "highest of any major (NACE projection)", delta_color="off")
    c2.metric("New CS bachelor's majors", "−13%", "while degrees awarded rose 13% (CRA)", delta_color="inverse")
    c3.metric("BLS 10-year developer job growth", "+10%", "−5.8 pts vs prior edition", delta_color="inverse")
    c4.metric("Senior roles' share of postings rebound", "71%", "Indeed, 2026", delta_color="off")

    st.info(
        "**No measured drop in total developer employment, and a measurable squeeze at entry "
        "level.** Stanford's payroll study finds 22-to-25-year-olds in AI-exposed occupations "
        "19% below where they would be had they tracked less-exposed peers, up from 15% a year "
        "earlier, working through reduced hiring. Postings fell from more than twice the "
        "pre-pandemic level in early 2022 to a low in May 2025, and have recovered about 30% "
        "since, mostly in senior roles. The work is shifting toward reviewing, verifying "
        "and directing agent output."
    )
    st.caption(
        "The Indeed line is the first-of-month reading from Indeed Hiring Lab's public data "
        "file; the 2022 peak reflects the pandemic hiring boom and its unwinding as much as AI. "
        "Stanford describes its estimate as "
        "descriptive, not causal, and changed its headline measure between editions, so only "
        "these two like-for-like figures are shown. Enrollment figures are from CRA's summary of "
        "the 2025 Taulbee survey, which ties graduate declines partly to visa barriers."
    )


# ═════════════════════════════════════════════════════════════════════════════
# TAB — Prediction Scorecard
# ═════════════════════════════════════════════════════════════════════════════
with tab_pred:
    st.markdown("### Predictions, Scored")
    st.markdown("What prominent voices said would happen, and what the evidence shows by November 2026.")
    CHIP = {
        "Missed": "#e0524a", "Split": "#e0a23c", "Holding": "#10a37f",
        "Reported": "#4c8ef5", "Open": "#777777",
    }
    rows = []
    for _, r in D["pred"].iterrows():
        colr = CHIP.get(r["Verdict"], "#777777")
        rows.append(
            f"<tr><td class='who'><b>{r['Who']}</b><br><span>{r['Made']}</span></td>"
            f"<td>{r['Prediction']}<br><span>Deadline: {r['Deadline']}</span></td>"
            f"<td><span class='chip' style='background:{hex_to_rgba(colr, 0.2)};color:{colr};"
            f"border:1px solid {colr}'>{r['Verdict']}</span></td>"
            f"<td>{r['What happened']} <a href='{r['Source']}' target='_blank'>source</a></td></tr>"
        )
    st.markdown(
        """
<style>
table.score { width:100%; border-collapse:collapse; font-size:0.93rem; }
table.score th { text-align:left; color:#888; font-weight:500; padding:8px 12px; border-bottom:1px solid #333; }
table.score td { padding:12px; border-bottom:1px solid #23262f; vertical-align:top; color:#d0d0d0; }
table.score td span { color:#777; font-size:0.82rem; }
table.score td.who { white-space:nowrap; }
table.score .chip { padding:3px 10px; border-radius:12px; font-size:0.8rem !important; font-weight:600; white-space:nowrap; }
table.score a { color:#4c8ef5; font-size:0.82rem; text-decoration:none; }
</style>
<table class="score"><tr><th>Who</th><th>Prediction</th><th>Verdict</th><th>What happened</th></tr>
"""
        + "".join(rows)
        + "</table>",
        unsafe_allow_html=True,
    )
    st.info(
        "**The pattern:** predictions about what happens *inside frontier labs* largely came "
        "true near schedule. Predictions about the *whole economy* missed their deadlines or "
        "remain open. Diffusion is slower than capability."
    )
    st.caption(
        "Original wording and dates for the Amodei and Zuckerberg predictions were taken from "
        "secondary scorecards and should be checked against the primary interviews before quoting."
    )

# ═════════════════════════════════════════════════════════════════════════════
# TAB — Benchmark Guide
# ═════════════════════════════════════════════════════════════════════════════
with tab_guide:
    st.markdown("### A Field Guide to AI Benchmarks")
    st.markdown(
        "Every benchmark this project has come across, with what it asks a model to do, who "
        "runs it and whether it still tells frontier models apart."
    )
    cat = D["catalog"]
    G_STATUS = {
        "Active": "#10a37f", "Saturated": "#e0a23c", "Discredited": "#e0524a",
        "Superseded": "#9aa0aa", "Historical": "#6b7280",
    }
    cats = sorted(cat["Category"].unique())

    counts = cat.groupby(["Category", "Status"]).size().unstack(fill_value=0).reindex(cats)
    order = counts.sum(axis=1).sort_values().index
    figk = go.Figure()
    for status, colr in G_STATUS.items():
        if status in counts.columns:
            figk.add_trace(go.Bar(
                y=list(order), x=counts.loc[order, status], orientation="h", name=status,
                marker_color=colr, hovertemplate="%{y}<br>" + status + ": %{x}<extra></extra>"))
    figk.update_layout(
        **BASE_LAYOUT, barmode="stack", height=90 + 30 * len(cats), margin=dict(l=20, r=30, t=55, b=40),
        title=dict(text=f"{len(cat)} benchmarks by what they test and where they stand", font=dict(size=15), x=0.0),
        xaxis=dict(gridcolor=GRID_COL, title="Benchmarks"), yaxis=dict(tickfont=dict(size=12.5)),
        legend=dict(**LEGEND_STYLE, orientation="h", y=-0.14),
    )
    st.plotly_chart(figk, width="stretch")

    c1, c2, c3, c4 = st.columns(4)
    n_active = int((cat["Status"] == "Active").sum())
    n_flawed = int(cat["Epoch_Review"].str.startswith("Flawed").sum())
    n_recent = int((cat["Launched"].str[:4] >= "2025").sum())
    n_vendor = int((cat["Scored_by"] == "Vendors self-report").sum())
    c1.metric("Listed as active", str(n_active), f"of {len(cat)} benchmarks", delta_color="off")
    c2.metric("Launched in 2025 or 2026", str(n_recent), "the field turns over fast", delta_color="off")
    c3.metric("Rated Flawed by Epoch", str(n_flawed), "of 29 it has reviewed", delta_color="off")
    c4.metric("Scores mostly self-reported", str(n_vendor), "by the labs being measured", delta_color="off")

    pick_col, _ = st.columns([2, 3])
    with pick_col:
        pick = st.selectbox("Category", ["All categories"] + cats, key="guide_cat")
    view = cat if pick == "All categories" else cat[cat["Category"] == pick]
    view = view.sort_values(["Category", "Launched", "Benchmark"])

    def _esc(t):
        return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    rows, last_cat = [], None
    for _, r in view.iterrows():
        if pick == "All categories" and r["Category"] != last_cat:
            rows.append(f"<tr class='grp'><td colspan='5'>{_esc(r['Category'])}</td></tr>")
            last_cat = r["Category"]
        colr = G_STATUS.get(r["Status"], "#777777")
        name = _esc(r["Benchmark"])
        if r["URL"]:
            name = f"<a href='{_esc(r['URL'])}' target='_blank'>{name}</a>"
        why = f"<br><span>{_esc(r['Why_it_matters'])}</span>" if r["Why_it_matters"] else ""
        review = f"<br><span>Epoch review: {_esc(r['Epoch_Review'])}</span>" if r["Epoch_Review"] else ""
        unchecked = "<br><span class='unc'>description not independently checked</span>" if r["Basis"] == "survey only" else ""
        rows.append(
            f"<tr><td class='who'><b>{name}</b><br><span>{_esc(r['Run_by'])}</span></td>"
            f"<td class='yr'>{_esc(r['Launched'][:7])}</td>"
            f"<td>{_esc(r['What_it_measures'])}{why}{unchecked}</td>"
            f"<td><span class='chip' style='background:{hex_to_rgba(colr, 0.2)};color:{colr};"
            f"border:1px solid {colr}'>{_esc(r['Status'])}</span>{review}</td>"
            f"<td class='by'>{_esc(r['Scored_by'])}</td></tr>"
        )
    st.markdown(
        """
<style>
table.guide { width:100%; border-collapse:collapse; font-size:0.9rem; }
table.guide th { text-align:left; color:#888; font-weight:500; padding:8px 10px; border-bottom:1px solid #333; }
table.guide td { padding:9px 10px; border-bottom:1px solid #23262f; vertical-align:top; color:#d0d0d0; }
table.guide td span { color:#888; font-size:0.82rem; }
table.guide td.who { min-width:190px; }
table.guide td.yr, table.guide td.by { white-space:nowrap; color:#aaa; font-size:0.85rem; }
table.guide tr.grp td { color:#e6e6e6; font-weight:600; font-size:0.95rem; padding-top:20px; border-bottom:1px solid #444; }
table.guide .chip { padding:2px 9px; border-radius:12px; font-size:0.78rem !important; font-weight:600; white-space:nowrap; }
table.guide a { color:#8fb8ff; text-decoration:none; }
table.guide td span.unc { color:#a07c3a; font-style:italic; }
</style>
<table class="guide"><tr><th>Benchmark</th><th>Since</th><th>What a model has to do</th><th>Status</th><th>Who runs the scores</th></tr>
"""
        + "".join(rows)
        + "</table>",
        unsafe_allow_html=True,
    )
    st.info(
        "**How to read a benchmark name in a headline.** Ask four things: what the model "
        "had to do, who ran it, whether the test still has room at the top, and whether anyone "
        "has checked the test itself. *Saturated* means frontier models score near the ceiling. "
        "*Discredited* means a major evaluator disowned it on validity grounds. *Superseded* "
        "means a newer version replaced it. *Historical* means frontier labs no longer report it."
    )
    st.caption(
        "Compiled on 19 November 2026 from Epoch's benchmark metadata, the benchmarks' own "
        "pages and papers, and this project's research notes. About a quarter of the rows "
        "rest on a single survey and are marked as not independently checked. Descriptions are one-line "
        "summaries, not specifications; status is a judgment call outside the benchmarks this "
        "project charts. The list is broad but not exhaustive, and scores are deliberately "
        "left out because they date within weeks. Follow each link for current results."
    )

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.markdown(
    '<p style="color:#555;font-size:0.8rem;text-align:center;">'
    "Data: METR · Epoch AI · ARC Prize · Scale Labs · Artificial Analysis · lab changelogs · "
    "GitHub Octoverse · Stanford Digital Economy Lab · Indeed Hiring Lab &nbsp;|&nbsp; "
    "Revised 19 November 2026 · source for every row is in working-data-tables/"
    "</p>",
    unsafe_allow_html=True,
)
