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

st.markdown("""
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
""", unsafe_allow_html=True)

# ── Color palette ─────────────────────────────────────────────────────────────
ORG_COLORS = {
    "OpenAI":    "#10a37f",
    "Anthropic": "#e07b4a",
    "Google":    "#4c8ef5",
    "xAI":       "#e04a7b",
    "Meta":      "#5c8fff",
    "DeepSeek":  "#a855f7",
    "Microsoft": "#888888",
}

PLOT_BG   = "#0e1117"
PAPER_BG  = "#0e1117"
GRID_COL  = "#23262f"
FONT_COL  = "#d0d0d0"

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


# ── Data loading ──────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    base = Path(__file__).parent / "working-data-tables"

    th = pd.read_csv(base / "model-task-time-horizons.csv")
    bm = pd.read_csv(base / "model-benchmark-scores.csv")
    tl = pd.read_csv(base / "model-release-timeline.csv")

    th["Release_Date"] = pd.to_datetime(th["Release_Date"])
    bm["Date"]         = pd.to_datetime(bm["Date"])
    tl["Release Date"] = pd.to_datetime(tl["Release Date"])

    for col in ["METR_50pct_TH_min", "CI_95_lower_min", "CI_95_upper_min"]:
        th[col] = pd.to_numeric(th[col], errors="coerce")

    for col in ["MMLU", "GPQA", "SWE_bench_Verified", "HumanEval", "MATH"]:
        bm[col] = pd.to_numeric(bm[col], errors="coerce")

    return th, bm, tl


th_df, bm_df, tl_df = load_data()

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("# The Pace of Change in Agentic Coding")
st.markdown('<p class="subtitle">A graduate lecture on exponential AI progress &nbsp;·&nbsp; 2023 – 2026</p>', unsafe_allow_html=True)
st.divider()

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "📅  Release Cadence",
    "📊  Benchmark Progression",
    "⏱  Task Time Horizons",
])


with tab3:
    st.markdown("### AI Task Time Horizon (METR 50th-Percentile)")
    st.markdown(
        "The longest software-engineering task an AI agent completes with **50% success rate**, "
        "measured by METR across 228 real tasks (HCAST + RE-Bench + SWAA suite)."
    )

    fig = go.Figure()

    # ── Doubling-era shaded bands ──────────────────────────────────────────
    eras = [
        ("2023-01-01", "2024-09-01", "~7-month doubling"),
        ("2024-09-01", "2025-07-01", "~131-day doubling"),
        ("2025-07-01", "2026-04-01", "~89-day doubling"),
    ]
    for x0, x1, label in eras:
        fig.add_vrect(
            x0=x0, x1=x1,
            fillcolor="rgba(255,255,255,0.025)",
            layer="below", line_width=0,
            annotation_text=label,
            annotation_position="top left",
            annotation_font=dict(size=11, color="#666"),
        )

    # ── 95% CI vertical bars (where data exists) ───────────────────────────
    ci_df = th_df.dropna(subset=["CI_95_lower_min", "CI_95_upper_min"])
    for _, row in ci_df.iterrows():
        color = ORG_COLORS.get(row["Org"], "#888")
        fig.add_trace(go.Scatter(
            x=[row["Release_Date"], row["Release_Date"]],
            y=[row["CI_95_lower_min"], row["CI_95_upper_min"]],
            mode="lines",
            line=dict(color=hex_to_rgba(color, 0.55), width=4),
            showlegend=False,
            hoverinfo="skip",
        ))

    # ── Main trend lines per org ───────────────────────────────────────────
    _all_labels = []  # collect first, position smartly after
    for org in th_df["Org"].unique():
        org_df = th_df[th_df["Org"] == org].sort_values("Release_Date")
        color  = ORG_COLORS.get(org, "#888")

        def _fmt_minutes(m):
            if pd.isna(m):
                return "—"
            if m < 60:
                return f"{m:.0f} min"
            return f"{m/60:.1f} hr ({m:.0f} min)"

        hover = [
            f"<b>{row['Model']}</b><br>"
            f"{row['Release_Date'].strftime('%b %Y')}<br>"
            f"50th-pct TH: {_fmt_minutes(row['METR_50pct_TH_min'])}"
            + (f"<br>95% CI: {_fmt_minutes(row['CI_95_lower_min'])} – {_fmt_minutes(row['CI_95_upper_min'])}"
               if pd.notna(row.get("CI_95_lower_min")) else "")
            for _, row in org_df.iterrows()
        ]

        fig.add_trace(go.Scatter(
            x=org_df["Release_Date"],
            y=org_df["METR_50pct_TH_min"],
            mode="lines+markers",
            name=org,
            line=dict(color=color, width=2.5),
            marker=dict(size=10, color=color, line=dict(color=PLOT_BG, width=1.5)),
            hovertemplate="%{customdata}<extra></extra>",
            customdata=hover,
        ))

        # Collect labels — positioned after all traces are added
        for _, row in org_df.iterrows():
            mins = row["METR_50pct_TH_min"]
            if pd.isna(mins):
                continue
            short_name = (
                row["Model"]
                .replace("Claude ", "")
                .replace("GPT-", "")
                .replace("Gemini ", "")
                .replace("DeepSeek-", "")
                .replace(" (0314)", "")
                .replace(" (1106)", "")
            )
            _all_labels.append(dict(
                x=row["Release_Date"], y=mins,
                text=short_name, color=color,
            ))

    # ── Smart label placement (alternate above/below for log-close points) ──
    _all_labels.sort(key=lambda p: (p["x"], p["y"]))
    _placed = []  # (x_ts, log_y, side)  — track what's already placed

    for pt in _all_labels:
        log_y  = math.log10(pt["y"])
        x_ts   = pt["x"].timestamp()
        # Points below the human baseline: always label above with a leader line
        if pt["y"] < 25:
            fig.add_annotation(
                x=pt["x"], y=pt["y"],
                text=pt["text"],
                showarrow=True,
                arrowhead=0, arrowwidth=1,
                arrowcolor=hex_to_rgba(pt["color"], 0.45),
                ax=0, ay=-28,
                font=dict(size=9, color=hex_to_rgba(pt["color"], 0.9)),
            )
            _placed.append((x_ts, log_y, "above"))
            continue
        # Points above baseline: conflict-aware above/below alternation
        conflicts_above = any(
            abs(x_ts - px) < 120 * 86400 and abs(log_y - py) < 0.20 and side == "above"
            for px, py, side in _placed
        )
        side   = "below" if conflicts_above else "above"
        yshift = -14 if side == "below" else 13
        _placed.append((x_ts, log_y, side))

        fig.add_annotation(
            x=pt["x"], y=pt["y"],
            text=pt["text"],
            showarrow=False,
            font=dict(size=9.5, color=hex_to_rgba(pt["color"], 0.9)),
            yshift=yshift,
            xshift=2,
        )

    # ── Human-baseline reference (margin annotation, not an hline) ─────────
    fig.add_annotation(
        x=1.01, y=math.log10(30),
        xref="paper", yref="y",
        text="← human baseliners<br>   ~30 min",
        showarrow=False,
        font=dict(size=10, color="#555"),
        xanchor="left",
    )
    # Subtle dotted line
    fig.add_shape(
        type="line",
        x0=0, x1=1, xref="paper",
        y0=30, y1=30, yref="y",
        line=dict(color="#333", width=1, dash="dot"),
    )

    fig.update_layout(
        **BASE_LAYOUT,
        margin=dict(l=70, r=120, t=55, b=60),
        height=650,
        title=dict(text="METR Task Time Horizon by Model", font=dict(size=15), x=0.0),
        xaxis=dict(title="Model Release Date", gridcolor=GRID_COL, showgrid=True),
        yaxis=dict(
            title="50th-percentile Task Time Horizon",
            type="log",
            range=[math.log10(3), math.log10(700)],
            gridcolor=GRID_COL, showgrid=True,
            tickvals=[3, 5, 10, 30, 60, 120, 300, 480, 600],
            ticktext=["3 min", "5 min", "10 min", "30 min", "1 hr", "2 hr", "5 hr", "8 hr", "10 hr"],
        ),
        hovermode="closest",
        legend=dict(**LEGEND_STYLE, title="Organization"),
    )

    st.plotly_chart(fig, use_container_width=True)

    # ── Key metrics row ────────────────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("GPT-4 — Mar 2023",          "5 min",       "baseline")
    c2.metric("o1-preview — Sep 2024",     "90 min",      "↑ 18× from GPT-4")
    c3.metric("Claude Opus 4.5 — Nov 2025","4 hr 49 min", "↑ 55× from GPT-4")
    c4.metric("Claude Opus 4.6 — Feb 2026","7+ hr",       "↑ ~84× from GPT-4")

    st.info(
        "**Reading this chart:** Each point is the 50th-percentile task time horizon — the duration "
        "at which a model succeeds on half of low-context software engineering tasks. "
        "Vertical bars show 95% confidence intervals where reported. "
        "The shaded regions mark three distinct doubling-time regimes."
    )


# ═════════════════════════════════════════════════════════════════════════════
# TAB 2 — Benchmark Progression
# ═════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("### Benchmark Progression Over Time")

    BENCHMARKS = {
        "GPQA Diamond  (PhD-level reasoning)":    ("GPQA",             "GPQA Diamond Score (%)"),
        "SWE-bench Verified  (real GitHub issues)": ("SWE_bench_Verified","SWE-bench Verified Score (%)"),
        "MATH / AIME  (competition mathematics)":  ("MATH",             "MATH / AIME Score (%)"),
        "MMLU  (broad knowledge)":                  ("MMLU",             "MMLU Score (%)"),
    }

    top_col, _ = st.columns([2, 3])
    with top_col:
        selected = st.selectbox("Select benchmark", list(BENCHMARKS.keys()), label_visibility="collapsed")

    col_key, y_label = BENCHMARKS[selected]
    plot_df = bm_df.dropna(subset=[col_key]).copy()

    fig2 = go.Figure()

    for org in ["OpenAI", "Anthropic", "Google", "xAI", "DeepSeek"]:
        org_df = plot_df[plot_df["Org"] == org].sort_values("Date")
        if org_df.empty:
            continue
        color = ORG_COLORS.get(org, "#888")

        hover = [
            f"<b>{row['Model']}</b><br>"
            f"{row['Date'].strftime('%b %Y')}<br>"
            f"{col_key.replace('_', ' ')}: {row[col_key]:.1f}%"
            for _, row in org_df.iterrows()
        ]

        fig2.add_trace(go.Scatter(
            x=org_df["Date"],
            y=org_df[col_key],
            mode="lines+markers",
            name=org,
            line=dict(color=color, width=2.5),
            marker=dict(size=10, color=color, line=dict(color=PLOT_BG, width=1.5)),
            hovertemplate="%{customdata}<extra></extra>",
            customdata=hover,
        ))

        # Label last point
        last = org_df.iloc[-1]
        fig2.add_annotation(
            x=last["Date"], y=last[col_key],
            text=f"  {last[col_key]:.0f}%",
            showarrow=False,
            font=dict(size=11, color=color),
            xanchor="left",
        )

    # Benchmark-specific reference lines
    references = {
        "GPQA":             (69.7,  "PhD expert human level: 69.7%"),
        "SWE_bench_Verified": (4.4, "GPT-4 baseline: 4.4% (Mar 2023)"),
    }
    if col_key in references:
        val, label = references[col_key]
        fig2.add_hline(
            y=val, line_dash="dot", line_color="#555", line_width=1.5,
            annotation_text=label,
            annotation_position="right",
            annotation_font=dict(size=11, color="#666"),
        )

    y_min = max(0, plot_df[col_key].min() - 8) if not plot_df.empty else 0
    y_max = min(105, plot_df[col_key].max() + 5) if not plot_df.empty else 105

    fig2.update_layout(
        **BASE_LAYOUT,
        margin=dict(l=70, r=120, t=55, b=60),
        height=540,
        title=dict(text=selected.split("  ")[0], font=dict(size=15), x=0.0),
        xaxis=dict(title="Date", gridcolor=GRID_COL, showgrid=True),
        yaxis=dict(title=y_label, gridcolor=GRID_COL, showgrid=True, range=[y_min, y_max]),
        hovermode="closest",
        legend=dict(**LEGEND_STYLE, title="Organization"),
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Contextual callouts per benchmark
    callouts = {
        "GPQA": (
            "**GPQA Diamond** poses questions written by domain experts that are designed to be "
            "difficult even for other PhD specialists. Human experts score **69.7%**. "
            "As of Feb 2026, Gemini 3.1 Pro reaches **94.3%** — nearly 25 points above expert human level."
        ),
        "SWE_bench_Verified": (
            "**SWE-bench Verified** tests real bug-fix pull requests from popular Python repos. "
            "GPT-4 solved just **4.4%** at launch (Mar 2023). "
            "Gemini 3.1 Pro now solves **80.6%** — an 18× improvement in under 3 years."
        ),
        "MATH": (
            "**MATH / AIME** measures competition-level math problem solving. "
            "Progress has been near-vertical: DeepSeek R1 and Claude Opus 4.5+ now exceed "
            "**97%**, approaching ceiling on standard MATH; frontier evals have shifted to AIME."
        ),
        "MMLU": (
            "**MMLU** covers 57 academic subjects. Progress has been steadier here (~87% → 93%), "
            "suggesting it's approaching saturation. "
            "Newer benchmarks like GPQA and SWE-bench better discriminate frontier models."
        ),
    }
    if col_key in callouts:
        st.info(callouts[col_key])


with tab1:
    st.markdown("### Model Release Cadence by Organization")
    st.markdown(
        "Each marker is a major frontier model release. "
        "Note the acceleration and crowding post-2025."
    )

    ORG_ORDER = ["OpenAI", "Anthropic", "Google", "xAI", "Meta", "DeepSeek", "Microsoft"]
    org_y = {org: i for i, org in enumerate(ORG_ORDER)}  # OpenAI at top

    fig3 = go.Figure()

    # ── Year separators ────────────────────────────────────────────────────
    for year in [2025, 2026]:
        fig3.add_vline(
            x=pd.Timestamp(f"{year}-01-01").value,
            line_dash="dash", line_color="#2a2a2a", line_width=1.5,
            annotation_text=str(year),
            annotation_position="top",
            annotation_font=dict(size=12, color="#555"),
        )

    # ── One trace per org ──────────────────────────────────────────────────
    for org in ORG_ORDER:
        org_df = tl_df[tl_df["Organization"] == org].sort_values("Release Date")
        if org_df.empty:
            continue
        color  = ORG_COLORS.get(org, "#888")
        y_val  = org_y[org]

        # Shorten model names for labels
        def _short(name: str) -> str:
            return (
                name
                .replace("Claude Opus ", "Opus ")
                .replace("Claude Sonnet ", "Sonnet ")
                .replace("Claude Haiku ", "Haiku ")
                .replace("Claude 3.5 Sonnet", "3.5 Sonnet")
                .replace("Claude 3.7 Sonnet", "3.7 Sonnet")
                .replace("Claude 3 ", "3 ")
                .replace("Gemini ", "")
                .replace("Llama ", "Llama ")
                .replace("GPT-", "")
                .replace("DeepSeek ", "")
            )

        labels = [_short(m) for m in org_df["Model"]]
        hover_data = list(zip(
            org_df["Model"],
            org_df["Type"],
            org_df["Release Date"].dt.strftime("%B %d, %Y"),
        ))

        fig3.add_trace(go.Scatter(
            x=org_df["Release Date"],
            y=[y_val] * len(org_df),
            mode="markers+text",
            name=org,
            marker=dict(
                size=16,
                color=color,
                symbol="circle",
                line=dict(color=PLOT_BG, width=2),
            ),
            text=labels,
            textposition="top center",
            textfont=dict(size=9, color=hex_to_rgba(color, 0.85)),
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "Type: %{customdata[1]}<br>"
                "Released: %{customdata[2]}<extra></extra>"
            ),
            customdata=hover_data,
        ))

    fig3.update_layout(
        **BASE_LAYOUT,
        height=480,
        margin=dict(l=90, r=40, t=55, b=60),
        # margin overrides BASE_LAYOUT default intentionally
        title=dict(text="Frontier Model Releases (Feb 2024 – Feb 2026)", font=dict(size=15), x=0.0),
        xaxis=dict(
            title="",
            gridcolor=GRID_COL, showgrid=True,
            range=["2024-01-01", "2026-04-01"],
        ),
        yaxis=dict(
            tickvals=list(org_y.values()),
            ticktext=list(org_y.keys()),
            gridcolor=GRID_COL, showgrid=True,
            tickfont=dict(size=13),
        ),
        showlegend=False,
        hovermode="closest",
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.info(
        "The visual density of Q3–Q4 2025 is not a coincidence: "
        "after GPT-5 (Aug 7) raised the bar, every major lab shipped a new flagship "
        "within 16 weeks. The cadence from GPT-4 → GPT-5 (28 months) compressed to "
        "GPT-5 → GPT-5.2 in just **4 months**."
    )

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.markdown(
    '<p style="color:#555;font-size:0.8rem;text-align:center;">'
    "Data: METR Time Horizon Reports · Official model release announcements · "
    "SWE-bench · GPQA Diamond · MATH/AIME benchmarks &nbsp;|&nbsp; "
    "All dates and scores validated Feb 2026"
    "</p>",
    unsafe_allow_html=True,
)
