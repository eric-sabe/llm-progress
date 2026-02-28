# Guest Lecture Visualizations

Interactive Streamlit visualizations exploring the pace of change in agentic coding and AI progress.

Prepared for NCSU CSC510.

## Charts

### 📅 Release Cadence
A swim-lane timeline showing every major frontier model release from February 2024 through February 2026, organized by lab (OpenAI, Anthropic, Google, xAI, Meta, DeepSeek, Microsoft). The chart makes the post-2025 acceleration immediately visible — after GPT-5 shipped in August 2025, every major lab followed with a new flagship within 16 weeks.

### 📊 Benchmark Progression
Tracks how model scores have evolved over time across four standard benchmarks, selectable via dropdown:

- **GPQA Diamond** — PhD-level reasoning questions. Human experts score 69.7%; frontier models now exceed 94%.
- **SWE-bench Verified** — Real GitHub bug-fix pull requests. GPT-4 solved 4.4% at launch; current leaders solve over 80%.
- **MATH / AIME** — Competition mathematics. Scores have approached ceiling (~97%), pushing evals toward harder AIME problems.
- **MMLU** — Broad academic knowledge across 57 subjects. Progress has slowed (~87% → 93%), suggesting saturation.

### ⏱ Task Time Horizons
Plots the METR 50th-percentile task time horizon — the longest software-engineering task an AI agent completes with a 50% success rate — on a log scale over time. Based on 228 real tasks across the HCAST, RE-Bench, and SWAA suites. Key milestones:

| Model | Date | 50th-pct Horizon |
|---|---|---|
| GPT-4 | Mar 2023 | ~5 min |
| o1-preview | Sep 2024 | ~90 min (18× GPT-4) |
| Claude Opus 4.5 | Nov 2025 | ~4 hr 49 min (55× GPT-4) |
| Claude Opus 4.6 | Feb 2026 | 7+ hr (~84× GPT-4) |

Shaded bands on this chart highlight three distinct doubling-time regimes: ~7 months, ~131 days, and ~89 days.

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```