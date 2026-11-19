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
(tab_rel, tab_life, tab_bench, tab_who, tab_th, tab_real, tab_jobs, tab_pred) = st.tabs(
    [
        "📅  Release Cadence",
        "⏳  Benchmark Lifespans",
        "📊  Progress Measures",
        "🔍  Who Measured It?",
        "⏱  Task Time Horizons",
        "🏗  Benchmarks vs Reality",
        "🎓  Jobs & Education",
        "🎯  Prediction Scorecard",
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
        eci = D["eci"].sort_values("Date")
        fr = eci[eci["Series"] == "Frontier"]
        op = eci[eci["Series"] == "Open-weight"]
        split = pd.Timestamp("2024-09-12")  # first reasoning model on the frontier (o1-mini)

        def _fit(df):
            x = (df["Date"] - split).dt.days / 365.25
            n = len(x)
            slope = ((x * df["ECI"]).sum() - x.sum() * df["ECI"].sum() / n) / ((x**2).sum() - x.sum() ** 2 / n)
            return slope, df["ECI"].mean() - slope * x.mean()

        pre, post = fr[fr["Date"] < split], fr[fr["Date"] >= split]
        (s_pre, b_pre), (s_post, b_post) = _fit(pre), _fit(post)
        fig2 = go.Figure()
        for (sl, b, d0, d1, nm, colr) in [
            (s_pre, b_pre, pre["Date"].min(), split, f"Before reasoning models: about {s_pre:.0f} pts/yr", "#777"),
            (s_post, b_post, split, AS_OF, f"Since reasoning models: about {s_post:.0f} pts/yr", "#bbb"),
        ]:
            fig2.add_trace(go.Scatter(
                x=[d0, d1], y=[b + sl * (d - split).days / 365.25 for d in (d0, d1)], mode="lines",
                name=nm, line=dict(color=colr, width=2, dash="dash")))
        for _, r in fr.dropna(subset=["CI_lo"]).iterrows():
            fig2.add_trace(go.Scatter(
                x=[r["Date"]] * 2, y=[r["CI_lo"], r["CI_hi"]], mode="lines", showlegend=False,
                hoverinfo="skip", line=dict(color=hex_to_rgba(ORG_COLORS.get(r["Org"], "#888"), 0.35), width=3)))
        keep = {"GPT-4", "Claude 3.5 Sonnet", "o1-mini", "o3", "GPT-5", "Gemini 3 Pro", "GPT-5.2 Pro",
                "GPT-5.5 Pro", "Claude Fable 5", "GPT-6 Astra", "GPT-6.2 Astra"}
        fig2.add_trace(go.Scatter(
            x=fr["Date"], y=fr["ECI"], mode="markers+text", name="Frontier model at release",
            marker=dict(size=11, color=[ORG_COLORS.get(o, "#888") for o in fr["Org"]],
                        line=dict(width=1.5, color=PLOT_BG)),
            text=[m.replace("Claude ", "") if m in keep else "" for m in fr["Model"]],
            textposition="top left", textfont=dict(size=9.5, color="#aaa"),
            customdata=list(zip(fr["Model"], fr["Org"])),
            hovertemplate="<b>%{customdata[0]}</b> (%{customdata[1]})<br>%{x|%b %d, %Y}"
                          "<br>ECI %{y:.1f}<extra></extra>"))
        fig2.add_trace(go.Scatter(
            x=op["Date"], y=op["ECI"], mode="markers+text", name="Best open-weight models (May 2026 table)",
            marker=dict(size=11, symbol="circle-open", color=[ORG_COLORS.get(o, "#888") for o in op["Org"]],
                        line=dict(width=2)),
            text=op["Model"], textposition="bottom center", textfont=dict(size=9, color="#888"),
            customdata=list(zip(op["Model"], op["Org"])),
            hovertemplate="<b>%{customdata[0]}</b> (%{customdata[1]}, open weights)"
                          "<br>ECI %{y:.1f}<extra></extra>"))
        add_vline(fig2, split, "First reasoning model", color="#666", y_text=0.02)
        fig2.update_layout(
            **BASE_LAYOUT, height=580, margin=dict(l=70, r=60, t=55, b=60),
            title=dict(text="Epoch Capabilities Index: each new frontier model, 2023 to Nov 2026",
                       font=dict(size=15), x=0.0),
            xaxis=dict(gridcolor=GRID_COL, range=["2022-12-01", "2027-01-15"]),
            yaxis=dict(title="ECI score", gridcolor=GRID_COL, range=[116, 182]),
            legend=dict(**LEGEND_STYLE, x=0.01, y=0.99), hovermode="closest",
        )
        st.plotly_chart(fig2, width="stretch")
        st.info(
            "**One number that survives benchmark turnover.** Epoch's index statistically links "
            "scores across many benchmarks, so it keeps working as individual tests saturate. "
            f"The frontier climbed about **{s_pre:.0f} points a year before reasoning models and "
            f"about {s_post:.0f} a year since** (Epoch's own estimates: 8.0 and 16.6). 2026 models "
            "sit on or slightly above the faster line: no slowdown, and no confirmed second "
            "speed-up. GPT-6.2 Astra (174.2) and Claude Fable 5.2 (173.5) are level within their "
            "error bars. Open-weight models (hollow) trailed the closed frontier by about "
            "**4 months** in Epoch's May 2026 estimate."
        )
        st.caption(
            "Frontier points and intervals are from Epoch's data file as downloaded 19 November "
            "2026. The dashed lines are least-squares fits to those points, computed here. "
            "Open-weight points come from Epoch's May 2026 table, an earlier data vintage that "
            "can differ by 1 to 2 points, and none is available for later open-weight models."
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
