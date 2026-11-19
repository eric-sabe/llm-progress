# The Pace of Change in Agentic Coding

Interactive charts on how fast AI coding capability is moving, how it is measured, what it costs and what has changed in practice. Prepared as a guest lecture for NCSU CSC510. Data revised 19 November 2026.

**Live site:** https://eric-sabe.github.io/llm-progress/

The same content runs two ways from one source file: as a static site on GitHub Pages (ten pages, one per tab) and as a Streamlit app for local use.

## The story in one paragraph

Capability kept climbing through 2026, but the instruments used to show it broke. Every benchmark the earlier version of this deck charted has been retired, METR's time-horizon series ended above its own reliability limit, and vendor and independent scores have drifted apart. Meanwhile real-world evidence arrived: agents now start more than 40% of GitHub pull requests, delivered work has moved much less than activity, and entry-level hiring in AI-exposed jobs has narrowed.

## Pages

| Page | What it shows |
|---|---|
| 📅 Release Cadence | Swim-lane timeline of model releases, Feb 2024 to Nov 2026, across ten labs (US labs plus DeepSeek, Moonshot, Z.ai, Alibaba). Diamonds mark access-gated releases. A stacked bar counts releases per quarter. A cyber-capability panel (CyBench and ExploitBench) shows what lay behind the gating. |
| ⏳ Benchmark Lifespans | One bar per benchmark from introduction to saturation, discrediting or replacement. Average life fell from about 46 months (2019 to 2021 cohort) to 22 (2023 to 2024) to 12 (2025). Benchmarks still in use carry Epoch's review verdict. |
| 📊 Progress Measures | Epoch Capabilities Index (each lab's best model over time for ten labs, open-weight models marked, with least-squares trend lines before and after reasoning models), the ARC-AGI-2 and ARC-AGI-3 climb, the portfolio of benchmarks proposed in place of SWE-bench, and the four retired series (GPQA Diamond, SWE-bench Verified, MATH/AIME, MMLU) with end markers. |
| 🔍 Who Measured It? | Paired dots for the same model on the same benchmark: vendor vs independent, one lab's table vs another's, and one model under different harnesses or scoring rules. |
| ⏱ Task Time Horizons | METR Time Horizon 1.1 at 50% or 80% success, with confidence intervals, the 16-hour reliability limit, the three readings of GPT-5.6 Sol, and the date the series was frozen. Below it, an "After METR" panel lists the instruments now used instead and charts METR's expenditure horizon. |
| 💵 Cost & Value | List prices per million tokens for current models, price by version within each product line, the cheapest price for a fixed capability level over time, capability index against price, ARC Prize's measured cost per task, and the total cost to run one evaluation suite. |
| 🏗 Benchmarks vs Reality | Share of code from AI (GitHub measurement and company statements), firm-level productivity studies split into activity, delivered work and friction, and METR's controlled trials. |
| 🎓 Jobs & Education | Indeed software postings index, Stanford's entry-level employment gap, CS salary, enrollment and BLS projection figures. |
| 🎯 Prediction Scorecard | Dated predictions from industry figures with a verdict and what happened. |
| 📚 Benchmark Guide | A reference list of about 170 benchmarks in 14 categories: what each asks a model to do, who runs it, its status and Epoch's review verdict, with a category filter. |

## Data

All chart data lives in `working-data-tables/` as CSV files. Each row carries a source link, a source-quality label, or both. A file can feed more than one chart on its page.

| File | Used by |
|---|---|
| `model-release-timeline.csv`, `cyber-capability.csv` | Release Cadence |
| `benchmark-lifespans.csv` | Benchmark Lifespans |
| `eci-scores.csv`, `arc-agi-scores.csv`, `successor-benchmarks.csv`, `model-benchmark-scores.csv` | Progress Measures |
| `vendor-vs-independent.csv` | Who Measured It? |
| `model-task-time-horizons.csv`, `after-metr-instruments.csv`, `expenditure-horizon.csv` | Task Time Horizons |
| `model-prices.csv`, `arc-cost-per-task.csv`, `aa-cost-to-run.csv` | Cost & Value |
| `adoption-series.csv`, `productivity-studies.csv`, `metr-uplift-studies.csv` | Benchmarks vs Reality |
| `labor-series.csv` | Jobs & Education |
| `prediction-scorecard.csv` | Prediction Scorecard |
| `benchmark-catalog.csv` | Benchmark Guide |
| `publications-agentic.csv`, `publications-agentic.xlsx` | Not charted; the reading list from the first version |

The research behind the November 2026 revision is in `reports/LLM progress update late 2026.md`. It is the single authoritative write-up: every figure with its source and source quality, a table of claims that are still unverified, and a runbook for the next refresh that says where each data file comes from. Raw working notes are kept in `research_notes/` for provenance only; they contain superseded figures.

### Conventions and caveats

- **Release dates** are first public availability, from lab changelogs where one exists. The `Source_Quality` column is `primary` (lab's own page), `secondary` (press coverage) or `legacy` (carried over from the first version and not re-checked).
- **METR values** are copied from METR's published Time Horizon 1.1 data file. Models measured only on the older TH 1.0 suite are kept in a separate series and hidden by default.
- **Vendor figures** are the lab's own numbers. `Confidence` in the score table is `confirmed` (read on the lab's page or system card), `reported` (read through a secondary source) or `estimated`. On the retired-benchmark charts, hollow markers are MMMLU, a different test from MMLU.
- **Benchmark end dates** and the cohort averages are judgment calls computed from the lifespans table, not a published statistic.
- **Company code-share figures** are executive statements with differing definitions.
- **Prices** are each provider's standard list rate for the base context window, with no batch, cache or volume discount. "Blended" means three parts input to one part output.

### Corrections made in the November 2026 revision

- Time horizons: 12 of 14 rows had a wrong value or date (for example o1-preview was listed at 90 minutes; METR's figure is about 20, and Claude Opus 4.6 was listed at about 7 hours; it is about 12).
- Scores: Claude Sonnet 4.6 GPQA corrected from 74.1 to 89.9 and GPT-5.3-Codex GPQA from 73.8 to 92.6, both against the labs' own tables; HumanEval and MATH cells from September 2025 onward, which had no traceable source, blanked.
- Timeline: GPT-5.3-Codex moved from 2026-01-14 to 2026-02-05; Claude 3.7 Sonnet moved to 2025-02-24.

### Generated tables

Two tables and one column are built by scripts from files you download. Everything else is edited by hand.

```bash
python scripts/build_eci_scores.py path/to/eci_scores.csv 2026-11-19               # eci-scores.csv
python scripts/update_price_eci.py path/to/eci_scores.csv                           # index scores in model-prices.csv
python scripts/build_arc_cost.py evaluations.json models.json 2026-11-19            # arc-cost-per-task.csv
```

## Running Locally

Tested with Python 3.12, which is also what the GitHub Actions build uses.

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app caches the data files, so restart it after editing a CSV.

## Published site

The site on GitHub Pages is a static copy of the same app. `build_site.py` runs `app.py` with a stand-in for Streamlit that records what the app would draw, once for every combination of the controls on each tab, and writes one HTML page per tab. `app.py` stays the single source: edit a chart or a sentence there and both versions change.

```bash
python build_site.py            # writes ./site
python -m http.server -d site   # preview at http://localhost:8000
```

Every push and pull request builds the site in GitHub Actions (`.github/workflows/pages.yml`), so a broken data file or chart fails the check. Pushes to `main` publish it.

Each page has its own address, for linking from slides: `index.html` (Release Cadence), `benchmark-lifespans.html`, `progress-measures.html`, `who-measured-it.html`, `task-time-horizons.html`, `cost-value.html`, `benchmarks-vs-reality.html`, `jobs-education.html`, `prediction-scorecard.html`, `benchmark-guide.html`. The pages need no server once loaded, and the `site` folder works offline if you serve it locally.

If `app.py` starts using a Streamlit call the builder does not know, the build stops and names the call; add it to `Container` in `build_site.py`.

## Repository layout

| Path | What it is |
|---|---|
| `app.py` | Every chart and every sentence. The single source for both the Streamlit app and the site |
| `build_site.py` | Turns `app.py` into the static site in `site/` (not committed) |
| `working-data-tables/` | The data behind the charts |
| `scripts/` | Builders for the generated tables |
| `reports/` | The consolidated research report and refresh runbook |
| `research_notes/` | Raw working notes, kept for provenance |
| `initial-data-tables/` | The score table from the first version, kept for reference and not used |
| `.github/workflows/pages.yml` | Builds the site on every push and pull request; publishes from `main` |
