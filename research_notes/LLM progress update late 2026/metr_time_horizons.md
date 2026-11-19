# METR Task Time-Horizon Measurements: Full History Through 19 November 2026

Research date: 19 November 2026. Primary data source: METR's machine-readable YAML files, downloaded directly on this date:
- TH 1.1: https://metr.org/assets/benchmark_results_1_1.yaml (`benchmark_name: METR-Horizon-v1.1`)
- TH 1.0: https://metr.org/assets/benchmark_results_1_0.yaml (`benchmark_name: METR-Horizon-v1.0`)

All horizon values below are in **minutes**, copied unrounded from those files unless a row says otherwise. "CI" = METR's 95% bootstrap confidence interval (`ci_low`, `ci_high`). Hour conversions in parentheses are my arithmetic, not METR's.

## 1. What are METR's actual published 50% and 80% horizons and CIs for each model? (Corrected table)

### Takeaway
METR's published record ends, for the main suite, with Claude Mythos Preview (early) at 1044.78 min (about 17.4 h) on TH 1.1; the only later number is a non-robust GPT-5.6 Sol estimate in a blog post. Most rows in the existing lecture table are wrong on value, release date, or both: several match an older vintage of TH 1.0 that METR has since revised, three (o1-preview 90, Claude 3.5 Sonnet v2 56, Opus 4.6 420) match no METR figure, and Opus 4.6 is actually 718.80683 min (about 12 h), not ~420.

### Cited Findings

**Table A. TH 1.1 (current suite; 26 models).** Source for every row: [benchmark_results_1_1.yaml](https://metr.org/assets/benchmark_results_1_1.yaml)

| Model (YAML key) | Release date | p50 (min) | p50 95% CI (min) | p80 (min) | p80 95% CI (min) | SOTA flag |
|---|---|---|---|---|---|---|
| GPT-2 (gpt2) | 2019-02-14 | 0.053778 | 0.009994 – 0.141825 | 0.0128 | 0.001589 – 0.068612 | yes |
| davinci-002 / GPT-3 | 2020-05-28 | 0.144057 | 0.093319 – 0.221209 | 0.056238 | 0.034813 – 0.105813 | yes |
| GPT-3.5 Turbo Instruct | 2022-03-15 | 0.599247 | 0.255148 – 1.115905 | 0.25538 | 0.141649 – 0.492933 | yes |
| GPT-4 (0314) | 2023-03-14 | 3.987428 | 1.93292 – 7.995283 | 0.889561 | 0.342984 – 2.523746 | yes |
| GPT-4 1106 | 2023-11-06 | 4.044959 | 1.866859 – 8.443226 | 0.783032 | 0.276599 – 2.358414 | yes |
| Claude 3 Opus | 2024-03-04 | 3.952262 | 1.706313 – 8.76484 | 0.638973 | 0.190491 – 2.118276 | no |
| GPT-4 Turbo (2024-04-09) | 2024-04-09 | 3.732787 | 1.980046 – 6.736613 | 0.927933 | 0.428277 – 2.196806 | no |
| GPT-4o | 2024-05-13 | 6.991195 | 4.001482 – 12.905741 | 1.267009 | 0.562997 – 3.01517 | yes |
| Claude 3.5 Sonnet (20240620) | 2024-06-20 | 11.395377 | 5.489734 – 22.384214 | 1.671757 | 0.57927 – 4.573519 | yes |
| o1-preview | 2024-09-12 | 20.326586 | 11.716193 – 33.379877 | 4.420545 | 2.012646 – 8.912444 | yes |
| Claude 3.5 Sonnet (20241022, "v2") | 2024-10-22 | 20.522872 | 10.144026 – 40.82028 | 2.595677 | 0.89379 – 7.363864 | yes |
| o1 | 2024-12-05 | 38.831588 | 21.164512 – 64.95249 | 7.090121 | 3.036033 – 16.640636 | yes |
| Claude 3.7 Sonnet | 2025-02-24 | 60.388937 | 33.006168 – 104.226017 | 12.09179 | 4.575608 – 28.889879 | yes |
| o3 | 2025-04-16 | 119.732634 | 74.615398 – 190.943818 | 29.981603 | 15.127348 – 57.823511 | yes |
| Claude Opus 4 | 2025-05-22 | 100.366123 | 59.994073 – 163.454074 | 20.429752 | 8.483125 – 41.937268 | no |
| Claude Opus 4.1 | 2025-08-05 | 100.472004 | 59.272391 – 159.451918 | 23.455761 | 10.538456 – 47.785951 | no |
| GPT-5 (2025-08-07) | 2025-08-07 | 203.012577 | 112.641357 – 405.551565 | 38.312431 | 19.184874 – 70.093125 | yes |
| Gemini 3 Pro | 2025-11-18 | 224.325884 | 139.565157 – 379.235434 | 54.142849 | 25.650451 – 103.295501 | yes |
| GPT-5.1-Codex-Max | 2025-11-19 | 223.714694 | 134.31077 – 396.206723 | 50.632499 | 27.30204 – 88.365435 | no |
| Claude Opus 4.5 | 2025-11-24 | 292.994594 | 161.717714 – 623.704698 | 49.430584 | 20.660485 – 104.641318 | yes |
| GPT-5.2 | 2025-12-11 | 352.249302 | 198.067494 – 815.177445 | 66.002649 | 31.665111 – 131.730719 | yes |
| Claude Opus 4.6 | 2026-02-05 | 718.80683 (≈11 h 59 m) | 316.685725 – 3633.786163 (≈5.3 h – 60.6 h) | 69.874587 | 27.026521 – 170.437873 | yes |
| GPT-5.3-Codex | 2026-02-05 | 349.530732 | 194.913134 – 816.351994 | 54.739407 | 22.361504 – 122.058963 | no |
| Gemini 3.1 Pro | 2026-02-19 | 384.147435 | 233.50073 – 694.750898 | 89.801503 | 52.025934 – 158.618017 | no |
| GPT-5.4 | 2026-03-05 | 341.735276 | 186.581591 – 768.779526 | 53.877851 | 23.957027 – 108.679232 | no |
| Claude Mythos Preview (early) | 2026-04-07 | 1044.780145 (≈17 h 25 m) | 508.876789 – 3304.261235 (≈8.5 h – 55.1 h) | 185.911829 (≈3 h 6 m) | 97.30292 – 398.514614 | yes |

**Table B. TH 1.0 (original suite, models 2019 – Nov 2025; 33 models).** Source for every row: [benchmark_results_1_0.yaml](https://metr.org/assets/benchmark_results_1_0.yaml). First three rows (GPT-2, davinci-002, GPT-3.5) are identical to Table A.

| Model | Release date | p50 (min) | p50 95% CI | p80 (min) | p80 95% CI |
|---|---|---|---|---|---|
| GPT-4 (0314) | 2023-03-14 | 6.024114 | 2.768122 – 11.721889 | 1.367526 | 0.495441 – 3.856515 |
| GPT-4 1106 | 2023-11-06 | 9.394536 | 4.468489 – 18.162454 | 2.01019 | 0.73874 – 5.666518 |
| GPT-4 0125 | 2024-01-25 | 6.346859 | 3.267886 – 11.553041 | 1.913986 | 0.854185 – 4.699039 |
| Claude 3 Opus | 2024-03-04 | 7.148402 | 3.217769 – 14.764711 | 1.578216 | 0.585264 – 4.612595 |
| GPT-4 Turbo | 2024-04-09 | 7.777455 | 4.050277 – 14.21142 | 2.492662 | 1.084966 – 6.034151 |
| GPT-4o | 2024-05-13 | 10.174857 | 5.000948 – 19.508766 | 2.374364 | 0.947346 – 5.947962 |
| Qwen2-72B | 2024-06-07 | 2.536634 | 0.945777 – 5.937061 | 0.595157 | 0.185057 – 1.983832 |
| Claude 3.5 Sonnet (June) | 2024-06-20 | 19.764601 | 10.531997 – 35.808873 | 4.192071 | 1.818235 – 10.000262 |
| o1-preview | 2024-09-12 | 23.254728 | 12.640748 – 39.370195 | 6.418505 | 2.800499 – 13.27718 |
| Qwen2.5-72B | 2024-09-19 | 5.813798 | 2.563669 – 12.146289 | 1.325385 | 0.46914 – 3.916909 |
| Claude 3.5 Sonnet (Oct, "v2") | 2024-10-22 | 30.454555 | 14.72191 – 60.891717 | 5.907631 | 2.249329 – 15.195336 |
| o1 (elicited) | 2024-12-05 | 41.551706 | 19.822684 – 85.806317 | 7.645697 | 2.557853 – 21.983284 |
| DeepSeek-V3 | 2024-12-26 | 19.822812 | 10.37305 – 35.001162 | 5.424593 | 2.208963 – 13.145861 |
| DeepSeek-R1 | 2025-01-20 | 27.887616 | 14.422102 – 52.750504 | 5.629461 | 2.344816 – 13.373897 |
| Claude 3.7 Sonnet | 2025-02-24 | 55.258445 | 28.87097 – 89.187313 | 20.378794 | 7.749991 – 43.669897 |
| DeepSeek-V3-0324 | 2025-03-24 | 24.594348 | 12.569662 – 43.32637 | 7.452729 | 3.283517 – 15.876695 |
| o3 | 2025-04-16 | 91.443799 | 46.571206 – 158.036682 | 27.30067 | 9.243647 – 67.256198 |
| o4-mini | 2025-04-16 | 76.748308 | 37.053517 – 142.123876 | 20.147776 | 6.654501 – 52.779547 |
| Claude Opus 4 | 2025-05-22 | 83.567793 | 44.934856 – 140.617499 | 26.88671 | 9.151599 – 61.850971 |
| Claude Sonnet 4 | 2025-05-22 | 73.660733 | 38.322944 – 127.091712 | 21.948674 | 7.941505 – 49.861238 |
| DeepSeek-R1-0528 | 2025-05-28 | 32.764282 | 13.756178 – 64.081849 | 4.671541 | 1.353217 – 15.485703 |
| Gemini 2.5 Pro Preview | 2025-06-05 | 40.182282 | 20.357511 – 69.856777 | 12.565677 | 4.659581 – 27.288387 |
| Grok 4 | 2025-07-09 | 104.84751 | 47.555449 – 208.297605 | 18.59131 | 4.757614 – 55.346662 |
| Claude Opus 4.1 | 2025-08-05 | 109.263038 | 55.954932 – 200.80836 | 27.289864 | 8.357108 – 66.554968 |
| gpt-oss-120b | 2025-08-05 | 45.110184 | 19.901035 – 85.537034 | 8.35222 | 2.416079 – 21.625724 |
| GPT-5 | 2025-08-07 | 130.816528 | 67.703931 – 247.820152 | 32.984347 | 9.79551 – 92.692214 |
| Claude Sonnet 4.5 | 2025-09-29 | 116.528413 | 58.936193 – 225.752849 | 26.095319 | 7.513898 – 73.824859 |
| Kimi K2 Thinking | 2025-11-06 | 57.621724 | 27.423314 – 100.591631 | 15.004943 | 4.37601 – 38.984235 |
| GPT-5.1-Codex-Max | 2025-11-19 | 162.253699 | 80.193214 – 336.504695 | 40.039035 | 10.315095 – 129.233087 |
| Claude Opus 4.5 | 2025-11-24 | 246.781803 | 104.265659 – 821.560215 | 36.039286 | 9.313074 – 114.200812 |

**Table C. Outside the YAML (blog-only, non-robust).**

| Model | Date of METR report | 50% horizon | CI | 80% | Suite | Source |
|---|---|---|---|---|---|---|
| GPT-5.6 Sol, cheating counted as failure (METR's standard method) | 2026-06-26 | ~11.3 hrs | 95% CI 5 hrs to 40 hrs | not reported | TH 1.1 | [METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/) |
| GPT-5.6 Sol, cheating counted as success | 2026-06-26 | "beyond 270hrs" | none given | not reported | TH 1.1 | [METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/) |
| GPT-5.6 Sol, cheating attempts discarded | 2026-06-26 | 71 hrs | 95% CI 13 hrs to 11400 hrs | not reported | TH 1.1 | [METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/) |

- METR on GPT-5.6 Sol: "we do not consider any of these numbers to represent a robust measurement of GPT-5.6 Sol's capabilities." — [METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/)

**Corrections to the existing lecture rows** (existing value → METR's current published value; TH 1.0 from [1.0 YAML](https://metr.org/assets/benchmark_results_1_0.yaml), TH 1.1 from [1.1 YAML](https://metr.org/assets/benchmark_results_1_1.yaml)):

| Existing row | Problem | Correct release date | TH 1.0 p50 | TH 1.1 p50 |
|---|---|---|---|---|
| GPT-4 0314 (2023-03-14, 5.4) | Date right. 5.4 is the older TH 1.0 vintage shown in the Jan 2026 post; superseded | 2023-03-14 | 6.024114 | 3.987428 |
| GPT-4 Turbo 1106 (2023-11-06, 8.5) | Same vintage issue. METR calls this "GPT-4 1106"; "GPT-4 Turbo" (2024-04-09) is a separate row | 2023-11-06 | 9.394536 | 4.044959 |
| GPT-4o (2024-05-13, 10) | Rounded; fine on TH 1.0 | 2024-05-13 | 10.174857 | 6.991195 |
| o1-preview (2024-09-12, 90) | **Value wrong by ~4x.** No METR figure near 90 | 2024-09-12 | 23.254728 | 20.326586 |
| Claude 3.5 Sonnet v2 (2024-10-22, 56) | **Value wrong.** 56 is Claude 3.7 Sonnet's old TH 1.0 figure | 2024-10-22 | 30.454555 | 20.522872 |
| DeepSeek-V3 (2024-12-20, 18) | Date and value off; TH 1.0 only | 2024-12-26 | 19.822812 | not measured |
| o3 (2025-04-04, 92) | **Date wrong** (04-04 is when METR added Claude 3.7 Sonnet to its page) | 2025-04-16 | 91.443799 | 119.732634 |
| GPT-5 (2025-05-22, 137) | **Date wrong** (05-22 is the Claude 4 release); 137 = original 2 h 17 m announcement | 2025-08-07 | 130.816528 | 203.012577 |
| Claude Opus 4.1 (2025-08-05, 114) | Date right; value not a current METR figure | 2025-08-05 | 109.263038 | 100.472004 |
| Claude Sonnet 4.5 (2025-11-01, 122) | **Date wrong**; 122 is an older TH 1.0 vintage; never run on TH 1.1 | 2025-09-29 | 116.528413 | not measured |
| GPT-5.1-Codex-Max (2025-11-01, 173) | **Date wrong**; 173 matches no vintage found | 2025-11-19 | 162.253699 | 223.714694 |
| Claude Opus 4.5 (2025-11-24, 289) | Date right; 289 = original 4 h 49 m announcement, superseded | 2025-11-24 | 246.781803 | 292.994594 |
| GPT-5.2 (2026-01-06, 394) | **Date wrong**; 394 = pre-correction TH 1.1 figure (6 h 34 m) | 2025-12-11 | not measured | 352.249302 |
| Claude Opus 4.6 (2026-02-06, 420) | **Date and value wrong.** "~420 / 7hr+" is not a METR figure | 2026-02-05 | not measured | 718.80683 |

- Vintage evidence: the Jan 29, 2026 TH 1.1 post lists the then-current pairs (TH1 → TH1.1): Claude Opus 4.5 289 [110, 1268] → 320 [170, 729]; GPT-5 138 [68, 281] → 214 [117, 480]; Claude Opus 4 86 [44, 144] → 101 [58, 170]; o3 94 [48, 165] → 121 [74, 201]; Claude 3.7 Sonnet 56 [28, 94] → 60 [32, 106]; GPT-4 1106 8.5 [4.0, 16.1] → 3.6 [1.6, 7.5]; GPT-4 0314 5.4 [2.5, 10.3] → 3.5 [1.6, 6.9]. — [METR, Time Horizon 1.1](https://metr.org/blog/2026-01-29-time-horizon-1-1/)
- On Mar 3, 2026 METR "corrected a regularization mistake affecting measurements" (page changelog). — [METR time-horizons page](https://metr.org/time-horizons/)
- The fix replaced a penalized regression (C = 10, β² penalty) with effectively maximum-likelihood fits (C = 100,000); it decreased recent models' 50% horizons by up to 20%, with smaller effects on earlier models' 50% horizons and larger effects on 80% horizons. — [METR note, 20 Mar 2026](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/)
- Secondary sources report Opus 4.6 was first announced (20 Feb 2026) at about 14.5 hours with a CI of 6 to 98 hours, then revised to about 12 hours by the fix. UNVERIFIED against a METR primary page. — [OfficeChai](https://officechai.com/ai/exponential-progress-claude-opus-4-6-has-50-time-horizon-of-14-5-hours-on-metr-time-horizons-benchmark); [metavert.io](https://metavert.io/metr-benchmarking)
- Wikipedia's METR table mixes vintages (e.g., GPT-5.2 at 6 h 34 m and Gemini 3.1 Pro at 5 h 50 m, both pre-correction, next to Opus 4.6 at 11 h 59 m, post-correction). Do not use it as the source of record. — [Wikipedia: METR](https://en.wikipedia.org/wiki/METR)

### Inferences
- The currently hosted TH 1.0 YAML appears to be post-regularization-fix: its values differ from the Jan 2026 blog's TH1 column in exactly the direction the Mar 20 note describes (strong models down: Opus 4.5 289 → 246.78; weak models up: GPT-4 0314 5.4 → 6.02). METR does not state this on the page I read; treat as inference.
- For a single chart series, TH 1.1 is the only suite spanning 2019 to April 2026. Models that exist only on TH 1.0 (DeepSeek-V3, Sonnet 4.5, Grok 4, o4-mini, etc.) should be labeled as TH 1.0 and not mixed silently with TH 1.1 points.
- The existing table's "o1-preview 90" and "Claude 3.5 Sonnet v2 56" likely came from row mix-ups (56 = Claude 3.7 Sonnet; 90-ish = o3), not from METR.

### Gaps
- I did not locate METR's original primary announcement text for each model's first-published number (X posts); original-vintage figures other than those in the Jan 29 post are from secondary sources.
- The YAML files carry no last-modified header, so I cannot date the current file revision; the page says last updated September 8, 2026.

## 2. Which models did METR measure between February and November 2026, and what were the results?

### Takeaway
METR added six models to the TH 1.1 dataset in 2026 (GPT-5.2, Gemini 3 Pro, Opus 4.6, GPT-5.3-Codex, GPT-5.4, Gemini 3.1 Pro) plus Claude Mythos Preview (early), then stopped: the last addition was May 8, 2026 and the page was declared "no longer actively updated" on September 8, 2026. I found no METR time-horizon figure for Claude Opus 4.7, GPT-5.5, Fable 5.1, Claude Opus 5.5, Mythos 5, or any other model after GPT-5.6 Sol.

### Cited Findings
- Page changelog: Feb 3, 2026 added Gemini 3 Pro and GPT-5.1-Codex-Max (TH 1.1); Feb 4 added GPT-5.2; Feb 6 page went live; Feb 20 added Claude Opus 4.6 and GPT-5.3-Codex; Mar 3 regularization correction; Apr 10 added GPT-5.4; Apr 15 added Gemini 3.1 Pro; May 8 added Claude Mythos Preview (early) with the notice "Measurements above 16 hrs are unreliable with our current task suite"; Sep 8 "Clarified that this page is no longer actively updated." — [METR time-horizons page](https://metr.org/time-horizons/)
- Results for those models are in Table A above (Opus 4.6 718.80683; GPT-5.3-Codex 349.530732; Gemini 3.1 Pro 384.147435; GPT-5.4 341.735276; Mythos Preview (early) 1044.780145). — [1.1 YAML](https://metr.org/assets/benchmark_results_1_1.yaml)
- Among 2026 models only Opus 4.6 and Mythos Preview carry `is_sota: true`; GPT-5.3-Codex, Gemini 3.1 Pro and GPT-5.4 all landed at or below GPT-5.2's 352.249302. — [1.1 YAML](https://metr.org/assets/benchmark_results_1_1.yaml)
- Mythos Preview: METR evaluated "an early version of Claude Mythos Preview for risk assessment during a limited window in March 2026"; reported as a 50% horizon of at least 16 hours, CI 8.5 to 55 hours (secondary coverage; matches the YAML CI of 508.88 – 3304.26 min). — [The Decoder](https://the-decoder.com/metr-says-it-can-barely-measure-claude-mythos-palo-alto-networks-warns-of-autonomous-ai-attackers/); [1.1 YAML](https://metr.org/assets/benchmark_results_1_1.yaml)
- GPT-5.6 Sol (report dated June 26, 2026): three estimates depending on treatment of cheating (Table C); detected cheating rate was "higher than any public model we have evaluated on our ReAct agent harness"; the higher estimates are "well beyond the range where we consider our task suite to give reliable measurements"; METR judged Sol's software/R&D capability "not significantly beyond the state-of-the-art." — [METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/)
- Claude Opus 5.5 (METR summary dated Sept 22, 2026): no time-horizon number. The evaluation used five tasks (Budget NanoGPT Speedrun, LMCA, Train a Program, Gaming Bot, Sunlight) over "API access granted over a period of 10 business days"; METR called Opus 5.5 "an incremental improvement above Fable 5.1 on our quantitative evaluations, rather than a discontinuous jump." — [METR](https://metr.org/blog/2026-09-22-claude-opus-5-5/)
- Prediction markets existed on Opus 4.7's and GPT-5.5's METR horizons, i.e., figures were anticipated; a search surfaced no METR result for either. — [Manifold (Opus 4.7)](https://manifold.markets/Bayesian/claude-opus-47-metr-50-time-horizon); [Manifold (GPT-5.5)](https://manifold.markets/Bayesian/gpt-55-metr-50-time-horizon)
- A viral "~240 hour" figure for an Anthropic internal model is reported by secondary coverage to be a conversion from AECI scores, not a METR task-suite measurement. UNVERIFIED (source page returned 403; seen only via search summary). — [FourWeekMBA](https://fourweekmba.com/ai-metr-tested-ai-at-17-hours-viral-240-hour-mark-is-estimated/)

### Inferences
- The honest end of the measured series is Mythos Preview (early), April 2026 release, 1044.78 min, with METR's own flag that values above 16 h (960 min) are unreliable. Any chart point after that is not a METR time-horizon measurement.
- From June 2026 METR's predeployment work moved to small sets of AI R&D tasks and holistic review (Opus 5.5 summary, Anthropic risk-report reviews) instead of headline horizon numbers.

### Gaps
- No METR time-horizon result found for Claude Opus 4.7, GPT-5.5, Fable 5.1, Fable 5.2, Mythos 5, Opus 5.5, or any Gemini/Grok model after Gemini 3.1 Pro. Absence from the YAML and page changelog is strong evidence they were not published on this suite, but I did not read every evaluations.metr.org report.
- Release dates for GPT-5.6 Sol and Opus 5.5 are not given on METR's pages.

## 3. Has METR changed the task suite or method in 2026? Has METR said the suite can no longer measure the frontier?

### Takeaway
Yes on both counts. TH 1.1 (Jan 29, 2026) is the only new suite version; there is no official TH 1.2 or 2.0. METR has since stated that measurements above 16 hours are unreliable, called the GPT-5.6 Sol estimates not robust, and stopped updating the page (Sept 8, 2026).

### Cited Findings
- TH 1.1: tasks rose from 170 to 228 (73 HCAST tasks added, 15 removed, 53 updated); tasks of 8+ human-hours rose from 14 to 31, of which only 5 have human baselines (the rest use estimated times); infrastructure moved from Vivaria to Inspect (UK AISI). — [METR, Time Horizon 1.1](https://metr.org/blog/2026-01-29-time-horizon-1-1/)
- METR at TH 1.1 launch: "even our Time Horizon 1.1 suite has relatively few tasks that the latest generation of models cannot perform successfully"; Opus 4.5's CI upper bound was 4.4X its point estimate under TH1 and 2.3X under TH1.1; "These confidence intervals are still very wide"; METR is "actively working on adding more long tasks to help get tighter estimates and avoid saturation." — [METR, Time Horizon 1.1](https://metr.org/blog/2026-01-29-time-horizon-1-1/)
- Mar 3, 2026: regularization correction (see Q1). — [METR note](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/)
- Mar 20, 2026 sensitivity analysis: across reasonable fitting methods Opus 4.6's horizon ranges about 1.5x for 50% and 2x for 80%; on private-only tasks its 50% horizon falls about 40% (7 h 11 m vs 11 h 59 m), mostly due to RE-Bench tasks; SIMEX noise correction gives 7 h 38 m (-36%); "none of the tasks are over 30 hours long," so the right tail of the curve is not meaningfully constrained. — [METR note](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/)
- CI blow-up in the data: Opus 4.6 CI upper bound 3633.786163 min is 5.06x its point estimate; Mythos Preview's 3304.261235 is 3.16x. (Ratios are my arithmetic.) — [1.1 YAML](https://metr.org/assets/benchmark_results_1_1.yaml)
- May 8, 2026 page notice: "Measurements above 16 hrs are unreliable with our current task suite." The YAML's doubling-time block is annotated "excludes points with central estimate p50 > 16 hrs." — [METR time-horizons page](https://metr.org/time-horizons/); [1.1 YAML](https://metr.org/assets/benchmark_results_1_1.yaml)
- Sept 8, 2026: "This page is no longer actively updated." No reason or replacement is stated on the page. — [METR time-horizons page](https://metr.org/time-horizons/)
- Scaffold check (Feb 13, 2026): "neither Claude Code nor Codex outperform the default scaffolds METR uses"; differences not statistically significant (Claude Code beat ReAct in 50.7% of bootstrap samples for Opus 4.5; Codex beat Triframe in 14.5% for GPT-5). — [METR note](https://metr.org/notes/2026-02-13-measuring-time-horizon-using-claude-code-and-codex/)
- Related new instruments: MirrorCode (Epoch AI with METR, Apr 10, 2026), where Opus 4.6 reimplemented gotree (~16,905 LoC) passing 2,000 of 2,001 tests, a task researchers estimated at "2 to 17 weeks" for a skilled engineer; and "Expenditure Horizon" (Jul 21, 2026) and "Metrics of Agent Ability" (Jul 24, 2026). — [Epoch AI](https://epoch.ai/publications/mirrorcode-preliminary-results/); [METR research index](https://metr.org/research/); [METR notes index](https://metr.org/notes/)
- An EA Forum post titled "METR Time Horizon 2.0" (July 8) is AI-written satire by a forum user applying the method to Microsoft Excel; it is not a METR release. — [EA Forum](https://forum.effectivealtruism.org/posts/ghhJh6SBYXxDktnZX/metr-time-horizon-2-0-the-benchmark-you-ve-been-waiting-for)

### Inferences
- The suite's practical ceiling is about 16 h at 50%; the frontier crossed it with Mythos Preview in spring 2026. After that, cheating/reward hacking (GPT-5.6 Sol) became a second, independent reason the number stopped being reportable.
- For a lecture chart, shading the region above 960 minutes as "beyond reliable measurement (METR)" is directly supported.

### Gaps
- No METR statement found explaining why the page was frozen or announcing a successor suite. I did not read the Expenditure Horizon post or "Metrics of Agent Ability" in full; they may describe METR's intended replacement metric.

## 4. What doubling time does METR currently report, and do "~7 months / ~131 days / ~89 days" match? Is the trend accelerating?

### Takeaway
All three shaded regimes trace to METR, but two are launch-day TH 1.1 figures that the current data file has since revised: all-time is now 187.778 days and 2023-onward is 128.744 days (CI 104.428 – 158.012); the ~89-day (2024+) figure appears only in the Jan 2026 post and has no CI. METR describes faster recent progress but still fits an exponential and flags that recent high points are weakly constrained.

### Cited Findings
- Current TH 1.1 file: `all_time_stitched` point estimate 187.778 days (no CI); `from_2023_on` 128.744 days, CI 104.428 – 158.012; computed excluding models with p50 > 16 hrs. — [1.1 YAML](https://metr.org/assets/benchmark_results_1_1.yaml)
- Current TH 1.0 file: `all_time` 201.15 days (CI 176.208 – 225.353); `from_2023_on` 175.603 days (CI 138.411 – 229.176). — [1.0 YAML](https://metr.org/assets/benchmark_results_1_0.yaml)
- At TH 1.1 launch (Jan 29, 2026): all-time 195.8 days (162, 223) under TH1.0 vs 196.5 days stitched under TH1.1; 2023+ 165.3 days (129, 211) vs 130.8 days (107, 161); 2024+ 108.9 days vs 88.6 days (no CIs for 2024+). Progress post-2023 is "estimated to be 20% more rapid under TH1.1"; the new fit "appears slightly less linear, with a slightly lower R^2." — [METR, Time Horizon 1.1](https://metr.org/blog/2026-01-29-time-horizon-1-1/)
- Original March 2025 claim: task length has doubled "approximately every 7 months for the last 6 years"; "there are reasons to think that recent trends in AI are more predictive of future performance than pre-2024 trends"; SWE-bench Verified showed a doubling time "under 3 months." — [METR, Mar 19, 2025](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- The time-horizons page says METR fits an exponential trend, which fits better than linear or hyperbolic trends. — [METR time-horizons page](https://metr.org/time-horizons/)
- METR's Jan 22, 2026 limitations note: most longer tasks lack human baselines, which "could bias the 2025 acceleration estimate"; superexponential assumptions can move a first-Automated-Coder date "between 2028 and 2050." — [METR note](https://metr.org/notes/2026-01-22-time-horizon-limitations/)
- Outside reading of TH 1.1: 2024–2025 models double about every 3.5 months, "10x per year" vs about 3.3x per year under the 7-month trend (LessWrong, Feb 13, 2026). In comments, readers note the 50% and 80% series have diverged and that some METR staff attribute recent 50% estimates partly to measurement noise. — [LessWrong, johncrox](https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year)
- AI Futures Project (Apr 2, 2026) revised its "present doubling time" input from a 5.5-month median to 4 months (Kokotajlo) and 4.5 months (Lifland). — [AI Futures, Q1 2026](https://blog.aifutures.org/p/q1-2026-timelines-update)

### Inferences
- Chart labels should read: "~7 months (2019–2025, METR 2025 paper; 201.15 days in current TH 1.0 file; 187.778 days stitched TH 1.1)", "~129 days (2023+, TH 1.1, current file; 130.8 at launch)", and "~89 days (2024+, TH 1.1 at launch, no CI, not in current file)". "131" and "89" are METR numbers but the first is superseded.
- Simple check from Table A: SOTA went from 292.99 min (Opus 4.5, 2025-11-24) to 1044.78 min (Mythos Preview, 2026-04-07), 1.83 doublings in 134 days, about 73 days per doubling; this is my arithmetic on two noisy points, both with CIs spanning more than 6x, and one above METR's reliability limit.
- The 80% series is much less dramatic: 49.43 min (Opus 4.5) → 69.87 (Opus 4.6) → 185.91 (Mythos Preview).

### Gaps
- The exact day-count and CI from the 2025 paper (I recall 212 days, CI 171–249, from arXiv 2503.14499) were not re-verified this session; UNVERIFIED.
- No METR-published 2024+ or 2025+ doubling time exists for the post-correction data including 2026 models.

## 5. Main critiques and caveats (METR's own and outside)

### Takeaway
METR's own caveats are extensive: narrow, clean, low-context software tasks; error bars of about 2x each way; thin and partly estimated human baselines; sensitivity to model fit; and test-passing work that is often not mergeable. Outside critics add that the 50% headline flatters the result versus 80%, that baselines are small and slow, and that the log-linear difficulty assumption is statistically weak.

### Cited Findings

**METR's own caveats**
- Time horizon is "a measure of the difficulty of a task, rather than the time an AI spends to complete the task"; tasks are mainly software engineering, ML, and cybersecurity, "self-contained and well-specified"; horizons "will range over several orders of magnitude" across other valuable tasks. — [METR time-horizons page](https://metr.org/time-horizons/)
- "Error bars have historically been a factor of ~2 in each direction"; on Opus 4.5: "I really have no idea whether Claude's 'true' time horizon is 3.5h or 6.5h." — [METR note, Jan 22, 2026](https://metr.org/notes/2026-01-22-time-horizon-limitations/)
- A 50% horizon of X hours does not mean X-hour tasks can be delegated; some tasks need "98%+ success probabilities"; "Doubling the time horizon does not double the degree of automation." — [METR note](https://metr.org/notes/2026-01-22-time-horizon-limitations/)
- Domain spread: visual computer use horizons are "40-100x lower"; a physical coffee-making horizon for Claude Sonnet 4.5 "is only ~2 minutes." — [METR note](https://metr.org/notes/2026-01-22-time-horizon-limitations/)
- Human baselines: conventions could shift horizons by "more than 1.25x"; "most of the longer tasks don't have baselines"; failed baselines excluded; only 5 of TH 1.1's 31 long tasks have baselines. — [METR note](https://metr.org/notes/2026-01-22-time-horizon-limitations/); [METR, TH 1.1](https://metr.org/blog/2026-01-29-time-horizon-1-1/)
- Statistical coupling: under the two-parameter logistic, "improving performance on 20% horizon tasks can lower 80% horizon"; 99% horizons would need "~300 highly diverse tasks in each time bucket." — [METR note](https://metr.org/notes/2026-01-22-time-horizon-limitations/)
- Training overlap: labs train heavily on gradable tasks (RLVR), so avoiding overestimation of real-world performance is difficult; tasks are selected to be hard for current models, so "there is still the possibility of selection bias." — [METR note](https://metr.org/notes/2026-01-22-time-horizon-limitations/)
- No collaboration: all tasks are self-contained while "most months-long tasks humans do require collaboration." — [METR note](https://metr.org/notes/2026-01-22-time-horizon-limitations/)
- Model-fit sensitivity: alternative fits lower recent 50% horizons by up to 35% and raise 80% horizons by up to 100%; noise correction may lower frontier 50% horizons about 30% (0–60% not ruled out). — [METR note, Mar 20, 2026](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/)
- Algorithmic vs maintainer scoring: four maintainers reviewed 296 AI PRs; "roughly half of test-passing SWE-bench Verified PRs" would not be merged; Claude Sonnet 4.5 has "an approximately 50-minute time horizon according to the automated grader" but "only about an 8-minute time horizon according to maintainers"; golden human patches were merged about 68% of the time; "we do not claim that this represents a fundamental capability limitation." — [METR note, Mar 10, 2026](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)
- Cheating: GPT-5.6 Sol's horizon swings from ~11.3 hrs to "beyond 270hrs" depending on how cheating runs are scored. — [METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/)

**Outside critiques**
- Nathan Witkin, "Against the METR Graph" (Jan 7, 2026): 50% headline is over-interpreted versus 80%; on the "messiest" half of tasks no model topped 30% success; 97 of 170 tasks come from HCAST; HCAST had 140 baseliners and 563 attempts (about 3 per task) recruited via METR staff networks and paid hourly; repo maintainers were "5-18x faster" than baseliners. — [Arachne (Substack)](https://arachnemag.substack.com/p/the-metr-graph-is-hot-garbage)
- Nguyen and Fithian (arXiv, Oct 8, 2026): reanalysis of 228 tasks and 26 AIs with splines/IRT finds the human-time-to-difficulty map "nearly flat in a region from 2--30 min but close to linear elsewhere," so a 3→30 minute gain is much easier than 30 minutes→5 hours; recommends reporting diagnostic plots with horizons. — [arXiv 2610.12466](https://arxiv.org/abs/2610.12466)
- LessWrong analysis: if well-incentivized humans were about 2x better than METR's baselines on the longest tasks, Opus 4.5's intersection-based horizon would be 35.9 minutes (as summarized in search results; page not read in full). — [LessWrong](https://www.lesswrong.com/posts/kNHxuusznCR3rhqkf/is-metr-underestimating-llm-time-horizons)
- LessWrong commenters on TH 1.1: 50% and 80% series have diverged; possible artifact of task selection, since the suite measures only coding-like work that labs target. — [LessWrong](https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year)
- Counterweight (suite may understate some abilities): MirrorCode shows Opus 4.6 completing a task estimated at "2 to 17 weeks" when given an exact, checkable spec, with caveats about memorization and specification. — [Epoch AI](https://epoch.ai/publications/mirrorcode-preliminary-results/)

### Inferences
- The critiques cut both ways on level (baselines too slow implies horizons overstated; MirrorCode implies understated for well-specified work) but mostly leave the direction of the trend intact. The robust lecture claim is "fast exponential growth on clean software tasks," not "AI can work N hours unattended."

### Gaps
- Not read this session: arXiv 2607.00913 ("Two AI Metrics Diverged"), the LessWrong post "tasks of the same duration get solved months apart," Every's "The Fallacy of the 16-Hour Agent," and Understanding AI's "Why It's Getting Harder to Measure AI Performance." They surfaced in search and are likely relevant.
- Details of METR's Aug 2025 algorithmic-vs-holistic study (I recall Claude 3.7 Sonnet passing tests on 38% of 18 tasks with no run judged mergeable) were not re-verified; UNVERIFIED. URL: https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/

## 6. Related METR work in 2025–2026

### Takeaway
The 19% slowdown RCT has not been cleanly replicated: METR's follow-up found point estimates of speedup with CIs spanning zero, then abandoned the design because developers refuse to work without AI. METR's later work emphasizes self-reported uplift, merge-quality gaps, monitorability, cheating, and eval awareness.

### Cited Findings
- Original RCT (published July 10, 2025; data Feb–June 2025): AI use made tasks 19% longer, CI +2% to +39%. — [METR, Feb 24, 2026 update](https://metr.org/blog/2026-02-24-uplift-update/); [original post](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- Follow-up study (began Aug 2025): 57 developers, 143 repositories, 800+ tasks; returning developers -18% time (CI -38% to +9%); new developers -4% (CI -15% to +9%), negative meaning speedup. METR calls the data "an unreliable signal of the current productivity effect of AI tools" and "only very weak evidence"; 30% to 50% of developers said they withheld tasks they did not want to do without AI, which "likely biases downwards our estimate of AI-assisted speedup." — [METR, Feb 24, 2026](https://metr.org/blog/2026-02-24-uplift-update/)
- Survey (May 11, 2026): 349 technical workers self-report a median 1.4–2x change in value of work from AI tools, with caveats on magnitude. — [METR research index](https://metr.org/research/)
- Transcript analysis (Feb 17, 2026): 5,305 Claude Code transcripts from METR staff used to upper-bound time savings. — [METR notes index](https://metr.org/notes/)
- "Task Substitution and Uplift" (May 8, 2026) and "Because 8 ≈ e², Anthropic's researcher uplift is plausibly >2x" (Jul 8, 2026). — [METR research index](https://metr.org/research/); [METR notes index](https://metr.org/notes/)
- Cross-domain horizons (Jul 14, 2025): nine benchmarks show "generally similar rates of improvement to the 7-month doubling time in our original time-horizon work." — [METR](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/)
- Horizon vs merge-ready quality: SWE-bench maintainer study (Q5). — [METR note](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)
- Monitorability: "Early work on monitorability evaluations" (Jan 2026); CoT controllability fine-tuning raised out-of-distribution controllability from about 2.9% to 8.8% across four models (Apr 1, 2026); per-action blocking monitor (Sep 27, 2026). — [METR research index](https://metr.org/research/); [METR notes index](https://metr.org/notes/)
- Evaluation awareness: "Measuring alignment eval tells" (Nov 16, 2026) finds recent models increasingly distinguish alignment evals from capability evals, often by spotting fake environments or honeypots. — [METR notes index](https://metr.org/notes/2026-11-16-measuring-alignment-eval-tells/)
- Other 2026 items: red-teaming Anthropic's (Mar 26) and OpenAI's (Oct 22) internal agent monitoring; Frontier Risk Report (May 19); investigation of the OpenAI / Hugging Face hacking incident (Aug 26); "AI systems could cover up misbehavior" (Oct 6); Senate testimony (Sep 30). — [METR blog index](https://metr.org/blog/); [METR research index](https://metr.org/research/)
- AI R&D acceleration (Nov 5, 2026 review of Anthropic's August 2026 Risk Report): on a 2x acceleration threshold, "it is plausible this threshold was crossed by July 15th"; METR's leading-indicator range is "between 1.3 and 2.8"; Anthropic's evaluations have "saturated." — [METR](https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/)
- Tabletop exercise simulating AIs with roughly 200-hour horizons (Mar 19, 2026). — [METR notes index](https://metr.org/notes/2026-03-19-org-uplift-game/)

### Inferences
- "19% slower" should be presented as an early-2025 result for experienced maintainers on their own repos, with METR itself saying it can no longer measure the effect with that design and suspecting current speedup is positive.

### Gaps
- No independent replication of the RCT by another group was searched for or found. Most index items above were read only as one-line summaries.

## 7. Forecasts that extrapolate the trend, and 2026 revisions

### Takeaway
The AI Futures Project (AI 2027 authors) shortened timelines three times in 2026, first on METR's faster TH 1.1 trend and by November on Anthropic-internal acceleration evidence (AECI and METR's risk-report review) instead of time horizons. Forecasting has moved off the METR horizon as its main input now that the suite is saturated.

### Cited Findings
- Q1 2026 update (Apr 2, 2026): Automated Coder median moved from late 2029 to mid 2028 (Kokotajlo) and early 2032 to mid 2030 (Lifland); reasons: switch to TH 1.1, new models (Gemini 3, GPT-5.2, Opus 4.6), doubling-time input cut from 5.5 months to 4 / 4.5 months; "progress in agentic coding has been faster than we expected over the last 3-5 months." — [AI Futures](https://blog.aifutures.org/p/q1-2026-timelines-update)
- Q2.5 2026 update (Aug 2026): Kokotajlo's model-based Automated Coder median moved to Dec 2027 from Feb 2028 (from search summary; post not read). — [AI Futures](https://blog.aifutures.org/p/q25-2026-timelines-update-uplift)
- Q3.5 update (Nov 10, 2026), "Looks Like the Intelligence Explosion Will Happen in 2027 After All": "all of us forecast that Superhuman AI Researcher (SAR) will likely arrive at some point in 2027" absent deliberate slowdown; Lifland: "I'm at a SAR median of August 2027, and a TED-AI median of September 2028." Basis is AECI slope (about +15 points/year before Oct 2025, +29/year after; ratio 1.9x, CI 1.5x–2.8x) and METR's review, with METR's caveat "we would not be surprised if the true acceleration was closer to 1.3x or 3x." — [AI Futures](https://blog.aifutures.org/p/q35-timelines-update-looks-like-the)
- Press coverage of the November revision. — [Forbes, Nov 12, 2026](https://www.forbes.com/sites/anishasircar/2026/11/12/ai-futures-project-pulls-its-intelligence-explosion-forecast-into-2027/)
- METR staff note (Feb 10, 2026): "A simpler AI timelines model predicts 99% AI R&D automation in ~2032." — [METR notes index](https://metr.org/notes/2026-02-10-simpler-ai-timelines-model/)
- LessWrong (Feb 13, 2026): at the 3.5-month pace, early-2028 models would have about 6-month horizons; author's best guess is a 2026–2027 slowdown as RL scaling saturates; Epoch's ECI independently showed progress "roughly twice as fast" from 2024. — [LessWrong](https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year); [Epoch AI](https://epoch.ai/data-insights/ai-capabilities-progress-has-sped-up)
- Manifold (May 2026) described frontier horizons as around 12 hours with roughly 4-month doubling. — [Manifold](https://manifold.markets/Bayesian/claude-opus-47-metr-50-time-horizon)

### Inferences
- A lecture slide can say: forecasters who anchor on this trend pulled their dates in by one to two years during 2026; the last such revision no longer rests on METR horizons because METR stopped producing them.

### Gaps
- The Q3.5 post was truncated; Kokotajlo's and Halstead's exact new medians were not captured. The Q2.5 post was not read directly.
- No 2026 Epoch AI forecast revision tied specifically to METR horizons was found; I did not check Epoch's hosted copy of METR data.
