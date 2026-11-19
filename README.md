# Guest Lecture Visualizations

Interactive Streamlit visualizations exploring the pace of change in agentic coding and AI progress.

Prepared for NCSU CSC510. Data revised 19 November 2026.

## The story in one paragraph

Capability kept climbing through 2026, but the instruments used to show it broke. Every benchmark the earlier version of this deck charted has been retired, METR's time-horizon series ended above its own reliability limit, and vendor and independent scores have drifted apart. Meanwhile real-world evidence arrived: agents now start more than 40% of GitHub pull requests, delivered work has moved much less than activity, and entry-level hiring in AI-exposed jobs has narrowed.

## Tabs

| Tab | What it shows |
|---|---|
| 📅 Release Cadence | Swim-lane timeline of model releases, Feb 2024 to Nov 2026, across ten labs (US labs plus DeepSeek, Moonshot, Z.ai, Alibaba). Diamonds mark access-gated releases. A stacked bar counts releases per quarter. |
| ⏳ Benchmark Lifespans | One bar per benchmark from introduction to saturation, discrediting or replacement. Average life fell from about 46 months (2019 to 2021 cohort) to 22 (2023 to 2024) to 12 (2025). |
| 📊 Progress Measures | Epoch Capabilities Index (each new frontier model and the best open-weight models, with least-squares trend lines before and after reasoning models), the ARC-AGI-2 and ARC-AGI-3 climb, and the four retired series (GPQA Diamond, SWE-bench Verified, MATH/AIME, MMLU) with end markers. |
| 🔍 Who Measured It? | Paired dots for the same model on the same benchmark: vendor vs independent, one lab's table vs another's, and one model under different harnesses or scoring rules. |
| ⏱ Task Time Horizons | METR Time Horizon 1.1 at 50% or 80% success, with confidence intervals, the 16-hour reliability limit, the three readings of GPT-5.6 Sol, and the date the series was frozen. Below it, an "After METR" panel lists the instruments now used instead and charts METR's expenditure horizon. |
| 🏗 Benchmarks vs Reality | Share of code from AI (GitHub measurement and company statements), firm-level productivity studies split into activity, delivered work and friction, and METR's controlled trials. |
| 🎓 Jobs & Education | Indeed software postings index, Stanford's entry-level employment gap, CS salary, enrollment and BLS projection figures. |
| 🎯 Prediction Scorecard | Dated predictions from industry figures with a verdict and what happened. |

## Data

All chart data lives in `working-data-tables/`, one CSV per chart, each row with a source link or a source-quality label.

| File | Used by |
|---|---|
| `model-release-timeline.csv` | Release Cadence |
| `benchmark-lifespans.csv` | Benchmark Lifespans |
| `eci-scores.csv`, `arc-agi-scores.csv`, `model-benchmark-scores.csv` | Progress Measures |
| `vendor-vs-independent.csv` | Who Measured It? |
| `model-task-time-horizons.csv`, `after-metr-instruments.csv`, `expenditure-horizon.csv` | Task Time Horizons |
| `adoption-series.csv`, `productivity-studies.csv`, `metr-uplift-studies.csv` | Benchmarks vs Reality |
| `labor-series.csv` | Jobs & Education |
| `prediction-scorecard.csv` | Prediction Scorecard |
| `publications-agentic.csv` | Not charted; the earlier reading list |

The research behind the November 2026 revision, including a table of open conflicts and figures that still need checking against primary sources, is in `reports/LLM progress update late 2026.md`. Working notes are in `research_notes/`; `verification.md` there records the later check of flagged figures against primary sources and supersedes the report where they differ.

### Conventions and caveats

- **Release dates** are first public availability, from lab changelogs where one exists. The `Source_Quality` column says when a date rests on press coverage or when the lab publishes only a month.
- **METR values** are copied from METR's published Time Horizon 1.1 data file. Models measured only on the older TH 1.0 suite are kept in a separate series and hidden by default.
- **Vendor figures** are the lab's own numbers and were mostly read through secondary sources. `Confidence` in the score table is `confirmed`, `reported` or `unverified`; unverified points are drawn hollow.
- **Benchmark end dates** and the cohort averages are judgment calls computed from the lifespans table, not a published statistic.
- **Company code-share figures** are executive statements with differing definitions.

### Corrections made in the November 2026 revision

- Time horizons: 12 of 14 rows had a wrong value or date (for example o1-preview was listed at 90 minutes; METR's figure is about 20, and Claude Opus 4.6 was listed at about 7 hours; it is about 12).
- Scores: Claude Sonnet 4.6 GPQA corrected from 74.1 to 89.9 and GPT-5.3-Codex GPQA from 73.8 to 92.6, both against the labs' own tables; HumanEval and MATH cells from September 2025 onward, which had no traceable source, blanked.
- Timeline: GPT-5.3-Codex moved from 2026-01-14 to 2026-02-05; Claude 3.7 Sonnet moved to 2025-02-24.

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
