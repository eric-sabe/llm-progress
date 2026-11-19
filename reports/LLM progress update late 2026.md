# Benchmarks broke while agentic coding scaled

Last revised: 19 November 2026

## Summary

- Release cadence roughly doubled in 2026. Anthropic went from 6 launch events in 2025 to 13 in 2026, every major lab added a tier above its old flagship, and each shipped at least one access-gated model ([Claude release notes](https://platform.claude.com/docs/en/release-notes/overview), primary).
- The five benchmark columns the lecture used to chart (MMLU, GPQA Diamond, SWE-bench Verified, HumanEval, MATH) have all ended. The last frontier launch reporting GPQA Diamond was Claude Mythos 5 on 9 June 2026, and the last reporting SWE-bench Verified was Claude Opus 5 on 24 July 2026 ([Anthropic system cards](https://www.anthropic.com/system-cards), primary).
- SWE-bench Verified and its endorsed replacement SWE-bench Pro were both discredited within five months of each other ([Epoch review](https://epoch.ai/benchmarks/swe-bench-pro/review), primary).
- METR's time-horizon series ends at Claude Mythos Preview, about 17.4 hours and above METR's own 16-hour reliability limit. The page was frozen on 8 September 2026 and METR has named no replacement ([METR time horizons](https://metr.org/time-horizons/), primary).
- Two independent series still span the period: the Epoch Capabilities Index (GPT-6.2 Astra 174.17, Claude Fable 5.2 173.50) and ARC-AGI-2 (54.2% in December 2025, 95.8% in November 2026) ([Epoch data](https://epoch.ai/data/eci_scores.csv), [ARC Prize data](https://arcprize.org/media/data/evaluations.json), both primary).
- Adoption is measured and steep. Agents started more than 40% of GitHub pull requests in September 2026, up from 17% in March ([GitHub Octoverse](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/), primary).
- Delivered work moved much less than activity, and employment of 22-to-25-year-olds in AI-exposed occupations is 19% below a less-exposed-peer benchmark ([Harvard paper](https://fion.ac/jellyfish.pdf), [Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf), both primary).

## How this document is organized

Sections 1 to 4 hold the findings, in the order of the app's tabs: releases, benchmarks and progress measures, METR time horizons, and real-world evidence. Section 5 says what the evidence supports for the lecture. Section 6 records what was wrong in the data tables before November 2026. Section 7 lists every claim that is still unverified. Section 8 is the runbook for the next refresh.

Each fact appears once, with its link and a source-quality label:

| Label | Meaning |
|---|---|
| primary | Read on the owner's own page, data file, system card, changelog, filing, paper or repository |
| secondary | Press or third-party coverage only |
| vendor | The lab's own figure for its own model (it can be primary as a source and still vendor as a measurement) |
| independent | A third party ran the evaluation |
| unverified | No source could be confirmed. Do not put it on a slide as is |

The data tables in `working-data-tables/` are the final state of the data, and this report agrees with them except for the handful of rows listed in section 8.5.

## 1. Releases

### 1.1 Date convention

The timeline (`model-release-timeline.csv`) plots first public availability, taken from the lab's changelog where one exists. The `Access` column records gated, preview or "gated first" releases, and `Source_Quality` records when a date rests on press coverage. Labs split announcement and API availability by up to 19 days in 2026, so the convention matters:

| Model | Announcement | API release | Plotted | Source |
|---|---|---|---|---|
| GPT-5.3-Codex | 2026-02-05 | 2026-02-24 | 02-05 | [OpenAI launch post, archived](https://web.archive.org/web/2026/https://openai.com/index/introducing-gpt-5-3-codex/), [OpenAI changelog](https://developers.openai.com/api/docs/changelog), primary |
| GPT-5.5 | 2026-04-23 | 2026-04-24 | 04-23 | [OpenAI launch post, archived](https://web.archive.org/web/20261117144117/https://openai.com/index/introducing-gpt-5-5/), [OpenAI changelog](https://developers.openai.com/api/docs/changelog), primary |
| GPT-5.6 Sol, Terra, Luna | 2026-06-26, gated preview (secondary) | 2026-07-09 | 07-09 | [OpenAI changelog](https://developers.openai.com/api/docs/changelog), primary. Preview date from [Interesting Engineering](https://interestingengineering.com/culture/openai-debuts-gpt-5-6-models-with-limited-access-after-us-government-request), secondary |
| Gemini 4 Argon | 2026-09-30, limited preview (secondary) | 2026-10-13 | 10-13 | [Gemini changelog](https://ai.google.dev/gemini-api/docs/changelog), primary |

ARC Prize's `modelReleaseDate` is a leaderboard-entry date. It trailed the lab date for Opus 4.8 (06-01 against 05-28), Grok 4.5 (07-16 against 07-08) and GLM-5 (02-20 against 02-12), and led it by a day for GPT-5.4 and GPT-6 Astra ([ARC Prize models file](https://arcprize.org/media/data/models.json), primary). It is not a release date.

### 1.2 US lab releases, January to 19 November 2026

Anthropic, OpenAI, Google and xAI dates are primary, from the [Claude release notes](https://platform.claude.com/docs/en/release-notes/overview), the [OpenAI changelog](https://developers.openai.com/api/docs/changelog), the [Gemini changelog](https://ai.google.dev/gemini-api/docs/changelog) and the [xAI release notes](https://docs.x.ai/docs/release-notes). Other sources are named in the row.

| Date | Lab | Model | Access | Quality |
|---|---|---|---|---|
| 01-14 | OpenAI | GPT-5.2-Codex | GA (API) | primary |
| 02-05 | OpenAI | GPT-5.3-Codex | GA, API on 02-24 | primary |
| 02-05 | Anthropic | Claude Opus 4.6 | GA | primary |
| 02-17 | Anthropic | Claude Sonnet 4.6 | GA | primary |
| 02-19 | Google | Gemini 3.1 Pro Preview | Preview. No GA entry exists in the 2026 changelog | primary |
| 03-05 | OpenAI | GPT-5.4 | GA | primary ([launch post, archived](https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/)) |
| 03-10 | xAI | Grok 4.20 and Grok 4.20 Multi-agent | GA. Beta from about 02-17 per Epoch | primary |
| 03-17 | OpenAI | GPT-5.4 mini and nano | GA. Not carried in the CSV | primary |
| 04-02 | Google | Gemma 4 | Open weights | primary |
| 04-07 | Anthropic | Claude Mythos Preview | Invitation only. First tier above Opus | primary |
| 04-08 | Meta | Muse Spark | GA | secondary ([CNBC](https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html)) |
| 04-16 | Anthropic | Claude Opus 4.7 | GA | primary |
| 04-23 | OpenAI | GPT-5.5 | GA, API on 04-24 | primary |
| 05-19 | Google | Gemini 3.5 Flash | GA | primary |
| 05-28 | Anthropic | Claude Opus 4.8 | GA | primary |
| 06-02 | Microsoft | MAI-Thinking-1, MAI-Code-1-Flash | Preview, rolling out to about 10% of individual Copilot users | primary ([Build keynote transcript](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/)) |
| 06-09 | Anthropic | Claude Fable 5 (public), Claude Mythos 5 (Project Glasswing only) | GA and gated | primary |
| 06-30 | Anthropic | Claude Sonnet 5 | GA | primary |
| 07-08 | xAI | Grok 4.5 | GA. EU availability 07-17 | primary |
| 07-09 | OpenAI | GPT-5.6 Sol, Terra, Luna | Gated first, then API GA | primary |
| 07-21, 08-13, 09-02 | Google | Gemini 3.6, 3.7, 3.8 Flash | GA | primary |
| 07-24 | Anthropic | Claude Opus 5 | GA | primary |
| 08-07 | OpenAI | GPT-5.6 Cyber | Gated | primary |
| 08-10 | Meta | Muse Glimmer (30B, Apache 2.0) | Open weights | secondary ([Let's Data Science](https://letsdatascience.com/news/meta-releases-muse-glimmer-open-weight-ai-model-0688168e)) |
| 08-12 | xAI | Grok 4.6 | GA | primary |
| 09-01 | Anthropic | Claude Fable 5.1, Mythos 5.1 | GA and gated | primary |
| 09-03 | OpenAI | GPT-6 Astra | GA. New tier above Sol | primary |
| 09-21 | xAI | Grok 4.7 | GA | primary |
| 09-22 | Anthropic | Claude Opus 5.5 | GA | primary |
| 09-22 | OpenAI | GPT-6 Sol, GPT-6 Luna | GA | primary ([TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/) agrees) |
| 09-28 | Anthropic | Claude Sonnet 5.5 | GA | primary |
| 09-29 | OpenAI | GPT-6.1 Sol | GA | primary |
| 10-07 | Anthropic | Claude Haiku 5.5 | GA | primary |
| 10-12 | Meta | Muse Wonder, Muse Wonder Full | GA, tiered | primary ([Meta Newsroom](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)) |
| 10-13 | Google | Gemini 4 Argon | GA | primary |
| 10-15 | Meta | Muse Spark Open | Open weights, access-gated repository, custom Muse licence | primary ([Meta research blog](https://research.meta.ai/blog/muse-spark-open)) |
| 10-26 | OpenAI | GPT-6.1 Terra | GA | primary |
| 10-30, 11-05 | OpenAI | GPT-6 Rosalind (bio), GPT-6 Cyber | Gated | primary |
| 11-09 | Anthropic | Claude Fable 5.2, Mythos 5.2 | GA and verified organizations only | primary |
| 11-09 | Meta | Muse Ember | GA | secondary ([TechCrunch](https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/)) |
| 11-10, 11-12, 11-18 | Google | Gemini 4 Carbon, Hydrogen, Neon | Carbon gated first, then GA. Others GA | primary |
| 11-17 | OpenAI | GPT-6.2 Astra, GPT-6.2 Sol | GA | primary |
| 11-17 | Microsoft | MAI Code 2, Code 2 Flash, Cyber 2 Flash | Mixed | secondary ([The New Stack](https://thenewstack.io/microsoft-mai-code-2/)) |

Outside the ten labs the app draws, Mistral Large 4 went to public preview on 2026-10-06 and its weights (`Mistral-Large-4-1T-A52B`, restricted use) were first published on 2026-10-29 ([Mistral changelog](https://docs.mistral.ai/getting-started/changelog), [weights repository](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B), primary).

Flagships on 19 November 2026 are GPT-6.2 Astra, Claude Fable 5.2 (with Mythos 5.2 restricted and Opus 5.5 as Anthropic's recommended default), Gemini 4 Carbon, Grok 4.7, Muse Wonder Full and MAI Code 2. Google's model list describes Carbon as its strongest reasoning model, and the Neon guide places Neon between Hydrogen and Carbon ([Gemini models](https://ai.google.dev/gemini-api/docs/models), [Neon guide](https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-neon), primary). Grok 5 has not shipped ([geotoolbox](https://geotoolbox.ai/blog/grok-5), secondary).

Naming changed at three labs in mid-year, which is why the timeline's `Series` and `Type` columns gained new values. Anthropic added Fable and Mythos above Opus in June. OpenAI replaced mini, nano and pro suffixes with Sol, Terra and Luna in July and added Astra above Sol in September. Google moved from Pro and Flash to element names in October. Standalone "-codex" model names stop after GPT-5.3-Codex ([OpenAI changelog](https://developers.openai.com/api/docs/changelog), primary).

### 1.3 Gated releases

Every major lab shipped an access-restricted model in 2026, mostly on cybersecurity grounds. The app marks these with diamonds.

| Event | Detail | Source and quality |
|---|---|---|
| Mythos Preview, 04-07 | Invitation only | [Claude release notes](https://platform.claude.com/docs/en/release-notes/overview), primary |
| Mythos 5, 06-09 | Limited to Project Glasswing | same, primary |
| Fable 5 and Mythos 5 suspension | The US government applied export controls on Friday 12 June. Anthropic suspended access for all users because it could not verify nationality in real time. Controls were lifted 30 June and access was restored 1 July | [Anthropic statement](https://www.anthropic.com/news/redeploying-fable-5), primary |
| GPT-5.6 limited preview | Held to a limited preview at US government request, per press accounts of Altman's statement | [Interesting Engineering](https://interestingengineering.com/culture/openai-debuts-gpt-5-6-models-with-limited-access-after-us-government-request), secondary |
| GPT-6.1 Astra cancelled | Internal tests reportedly showed more deception and more unauthorized actions than its predecessor. The API changelog jumps from GPT-6 Astra to GPT-6.2 Astra with no 6.1 entry | [Android Authority](https://www.androidauthority.com/open-ai-gpt-6-1-astra-canceled-security-concerns-3716551/), secondary. [OpenAI changelog](https://developers.openai.com/api/docs/changelog), primary for the gap |
| Gemini 4 Carbon pre-release | Government and cyber-defender pre-release under Google's Fairwind Program before GA | [Google October recap](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/), primary |

### 1.4 Chinese and open-weight releases

The open-weight coding frontier in 2026 is a contest among four Chinese labs (DeepSeek, Moonshot, Z.ai, Alibaba). Most dates below come from trade press and most coding scores are vendor-run. Dates that were checked against a lab page or a weights repository are marked primary.

| Date | Lab | Model | Weights | Independent standing | Source and quality |
|---|---|---|---|---|---|
| 2026-01-27 | Moonshot | Kimi K2.5 | Open | ECI 148.22 (May vintage). ARC-AGI-2 11.8% | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap), secondary for the date |
| 2026-02-12 | Z.ai | GLM-5 | Open. Repository created 02-11 UTC | ECI 146.62 (May vintage). ARC-AGI-2 4.9% | [Z.ai release list](https://docs.z.ai/release-notes/new-released), [weights](https://huggingface.co/zai-org/GLM-5), primary |
| 2026-02-12 | MiniMax | M2.5 | Open | Vendor claim 80.2% SWE-bench Verified. ARC-AGI-2 4.9%. Not in the CSV | [NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/minimax-m2-5-frontier-ai-performance-at-a-fraction-of-the-cost/), secondary |
| 2026-04-07 | Z.ai | GLM-5.1 | Open | ECI 149.94 (May vintage) | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap), secondary for the date |
| 2026-04-16, 04-22 | Alibaba | Qwen3.6-35B-A3B, Qwen3.6-27B | Open | Vendor only | [Alibaba Cloud](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043), vendor |
| 2026-04-20 | Moonshot | Kimi K2.6 | Open | ECI 151.60, top open model in May | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap), secondary for the date |
| 2026-04-22 | DeepSeek | V4-Pro, V4-Flash | Open, MIT. Repositories created 04-22. Epoch dates the release 04-24 | Vendor only at launch | [DeepSeek on Hugging Face](https://huggingface.co/deepseek-ai), primary. Announcement day (22 to 24 April) not pinned |
| 2026-06-01 | MiniMax | M3 | Open claimed, timing disputed. Not in the CSV | Vendor only | [Codersera](https://codersera.com/blog/minimax-m3-release-date-whats-new-2026/), secondary |
| 2026-06-16 | Z.ai | GLM-5.2 | Open, MIT | ARC-AGI-2 22.8% | [Z.ai release list](https://docs.z.ai/release-notes/new-released), primary |
| 2026-07-16 | Moonshot | Kimi K3 (2.8T parameters) | First public weights commit 07-27, custom `kimi-k3` licence | ARC-AGI-2 60.4% | Date secondary (Epoch and ARC Prize agree, [ForkLog](https://forklog.com/en/news/moonshot-ai-unveils-kimi-k3-first-open-3t-class-ai-model)). Weights primary ([repository](https://huggingface.co/moonshotai/Kimi-K3)) |
| 2026-07-31, 08-13 | DeepSeek | V4-Flash-0731, V4-Pro-0813 | Open, MIT. Refreshed snapshots of V4, not a delayed GA | ARC-AGI-2 61.4% and 61.3% | [DeepSeek on Hugging Face](https://huggingface.co/api/models?author=deepseek-ai&search=V4), primary |
| 2026-08-03 | Alibaba | Qwen3.8-Max | Promised, unconfirmed | Vendor only | [DataNorth](https://datanorth.ai/news/alibaba-releases-qwen3-8-max), secondary |
| 2026-08-18 | Z.ai | GLM-5.3 (GLM-5.3-Flash on 08-26) | Open. Press dated the announcement 08-14 and reported a weights delay of about two weeks | AA Index v5: 32. GLM-5.3-Flash ARC-AGI-2 65.8% | [Z.ai release list](https://docs.z.ai/release-notes/new-released), primary. [Decrypt](https://decrypt.co/375684/china-z-ai-glm-5-3-top-open-weight-coding-model?amp=1), secondary |
| 2026-09-10 | DeepSeek | V4.1 Flash (1017 refresh on 10-17) | Open, MIT | AA Index v5.0.1: 32.6 for the 1017 build. ARC-AGI-2 72.9%, then 78.1% | [DeepSeek on Hugging Face](https://huggingface.co/deepseek-ai), primary |
| 2026-10-23 | Moonshot | Kimi K3.1 Pro | Public. Repository created 11-02, last modified 11-05, not gated, custom `kimi-k3.1-pro` licence. Label it open-weight with a restricted licence | AA Index v5: 46 | Date secondary ([The Next Web](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber), Epoch). Weights primary ([repository](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)) |
| 2026-11-16 | Alibaba | Qwen4-Max (`qwen4-max-preview` on 11-11) | API only. No Qwen4 weights repository exists | None yet | [Alibaba Model Studio release list](https://www.alibabacloud.com/help/en/model-studio/newly-released-models), primary |

For 2025 context the timeline carries DeepSeek R1 (2025-01-20), Kimi K2 (07-11), Qwen3-Coder (07-22), GLM-4.5 (07-28) and gpt-oss (08-05), sourced from an open-weight timeline page ([llm-releases.com](https://www.llm-releases.com/open-weight-models), secondary).

"Open-weight" in 2026 often means announced with weights to follow. Kimi K3 weights arrived 11 days after the announcement, GLM-5.3 and Kimi K3.1 Pro were delayed for safety or cyber review, and Kimi K3.1 Pro, Mistral Large 4 and Muse Spark Open carry restricted licences.

### 1.5 The open-closed gap

| Measure | Value | Source and quality |
|---|---|---|
| ECI gap, October 2025 | About 3 months | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap), primary, independent |
| ECI gap, May 2026 | About 4 months, 8 ECI points | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap), [Epoch Brief](https://epochai.substack.com/p/the-epoch-brief-june-1-2026), primary, independent |
| Artificial Analysis Index v5 (27 October, 60% private test sets) | Best announced open model trailed the leader by 12 points. Best model with downloadable weights trailed by 26 | [Implicator](https://www.implicator.ai/artificial-analysis-index-v5-open-model-gap/), secondary |
| Chinese flagship API prices | About one-fifth to one-sixth of US flagship prices. DeepSeek raised prices on 16 August citing capacity | [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack), secondary |

No months-based gap has been published after May 2026. The gap is smallest on vendor-run Terminal-Bench (0 to 2 points), larger on SWE-bench Pro (9 to 12) and largest on private-set composites, which fits Epoch's warning that public benchmarks flatter open models.

Distillation accusations escalated during the year. Anthropic's February disclosure named three labs and its September threat report named seven ([CNBC](https://www.cnbc.com/2026/02/24/anthropic-openai-china-firms-distillation-deepseek.html), secondary. [Anthropic threat report](https://www.anthropic.com/threat-intelligence-report-september-2026), primary). A White House accusation against Moonshot on 22 July came without published evidence and drew public doubt from researchers ([The New Stack](https://thenewstack.io/moonshot-fable5-distillation-accusations/), secondary).

## 2. Benchmarks and progress measures

### 2.1 When each legacy column stopped

`model-benchmark-scores.csv` keeps the five legacy columns as closed series with end markers.

| Column | Last frontier launch reporting it | Score | Source and quality |
|---|---|---|---|
| GPQA Diamond | Claude Mythos 5, 9 June 2026. The system card says Anthropic considers it saturated and will stop reporting it | 94.1% | [Fable 5 and Mythos 5 system card, section 8.8](https://www.anthropic.com/claude-fable-5-mythos-5-system-card), primary, vendor |
| SWE-bench Verified | Claude Opus 5, 24 July 2026. Absent from the Opus 5.5 and Fable 5.2 cards | 96.0% | [Anthropic system cards](https://www.anthropic.com/system-cards), primary, vendor |
| MMLU | Original MMLU: none in 2026. Labs report MMMLU (Opus 4.6 91.1%, Gemini 3.1 Pro 92.6%, Opus 4.7 91.5%) and then GMMLU, a different instrument (Opus 4.7 89.9%, Opus 4.8 90.4%, Mythos 5 93.2%, Opus 5.5 94.3%, Fable 5.2 96.0%) | See cells | [Opus 4.7 system card](https://www.anthropic.com/claude-opus-4-7-system-card), primary, vendor |
| HumanEval | None found from December 2025 onward. No Anthropic system card from Sonnet 5 onward mentions it | n/a | Absence finding |
| MATH / AIME | None found from December 2025 onward. Math reporting moved to FrontierMath, ArXivMath and RiemannBench | n/a | Absence finding |

The `MMLU_Instrument` column in the CSV says which rows are MMLU and which are MMMLU. The two must not be joined as one line.

Final GPQA Diamond values by model, all vendor figures from primary pages:

| Model | GPQA Diamond | Source |
|---|---|---|
| Claude Sonnet 4.6 | 89.9% (10-trial average) | [Sonnet 4.6 system card](https://www-cdn.anthropic.com/78073f739564e986ff3e28522761a7a0b4484f84.pdf) |
| Claude Opus 4.6 | 91.3% | same |
| GPT-5.2, GPT-5.3-Codex, GPT-5.4, GPT-5.4 Pro | 92.4%, 92.6%, 92.8%, 94.4% | [GPT-5.4 launch post, archived](https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/) |
| Gemini 3.1 Pro | 94.3% | [Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card) |
| Claude Opus 4.7 | 94.2% | [Opus 4.7 system card](https://www.anthropic.com/claude-opus-4-7-system-card) |
| GPT-5.5 | 93.6% | [GPT-5.5 launch post, archived](https://web.archive.org/web/20261117144117/https://openai.com/index/introducing-gpt-5-5/) |
| Claude Opus 4.8 | 93.6% | [Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card) |
| Claude Mythos 5 | 94.1% | [Fable 5 and Mythos 5 system card](https://www.anthropic.com/claude-fable-5-mythos-5-system-card) |

Artificial Analysis removed GPQA Diamond from its index as saturated on 4 September 2026 ([AA v4.2 changelog](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2), primary).

Final SWE-bench Verified values, vendor figures from [Anthropic system cards](https://www.anthropic.com/system-cards) (primary): Opus 4.7 87.6%, Opus 4.8 88.6%, Fable 5 95, Mythos 5 95.5%, Sonnet 5 85.2%, Opus 5 96.0%. Epoch's own harness gives an independent series for the same benchmark: Opus 4.7 83.5%, GPT-5.5 (pre-release) 80.6%, Gemini 3.5 Flash 79.3%, Opus 4.6 78.7% ([Epoch benchmark data, `swe_bench_verified.csv`](https://epoch.ai/data/benchmark_data.zip), primary, independent). Vendor 87.6% against independent 83.5% for Opus 4.7 is the cleanest pair.

### 2.2 SWE-bench Verified and its replacement both failed inside five months

| Date | Event | Source and quality |
|---|---|---|
| 2026-02-23 | OpenAI stopped reporting SWE-bench Verified. It audited 138 problems (27.6% of the set, chosen because o3 did not solve them consistently) and found material issues in test design or problem description in 59.4%. All frontier models it tested could reproduce gold patches or verbatim problem text for some tasks. The post names GPT-5.2, Claude Opus 4.5 and Gemini 3 Flash | [OpenAI post, archived](https://web.archive.org/web/20261117145122/https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/), primary |
| 2026-02-24 | Gabor audit of SWE-bench Pro: 83 of 100 problems had issues | [Epoch review](https://epoch.ai/benchmarks/swe-bench-pro/review), primary |
| 2026-05-26 | Datacurve audit of SWE-bench Pro: 24% false negatives and 8.5% false positives. Datacurve sells a competing benchmark | same, primary |
| 2026-07-08 | OpenAI withdrew its recommendation of SWE-bench Pro, estimating about 30% of tasks are broken. Its automated pipeline flagged 200 tasks (27.4%) and human annotation found 249 (34.1%). Frontier pass rates on the public split had risen from 23.3% to 80.3% in eight months | [OpenAI post, archived](https://web.archive.org/web/20261117004847/https://openai.com/index/separating-signal-from-noise-coding-evaluations/), primary |
| 2026-09-01 | Epoch rated SWE-bench Pro "Flawed". It credits reward-hacking documentation to Poolside | [Epoch review](https://epoch.ai/benchmarks/swe-bench-pro/review), primary |

Some outlets noted OpenAI was not on the Verified podium when it retired the benchmark, so the critiques come partly from interested parties ([Decrypt](https://decrypt.co/359012/openai-benchmark-measure-ai-coding-supremacy-contaminated), secondary). Any line that connects SWE-bench Verified points past early 2026 plots a number its creator has disowned.

### 2.3 Vendor against independent on SWE-bench Pro

Scale figures are from its public-set leaderboard, read 19 November 2026. Vendor figures are each lab's own harness on the same 731-task public set. All rows are primary.

| Model | Vendor | Scale (independent) | Gap | Sources |
|---|---|---|---|---|
| Claude Opus 4.6 | 53.4% | 51.90 ± 3.61 | 1.5, inside the interval | [Opus 4.7 system card](https://www.anthropic.com/claude-opus-4-7-system-card), [Scale](https://labs.scale.com/leaderboard/swe_bench_pro_public) |
| GPT-5.4 | 57.7% | 59.10 ± 3.56 | Scale 1.4 higher | [GPT-5.4 post, archived](https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/), Scale |
| Gemini 3.1 Pro | 54.2% (single attempt) | 46.10 ± 3.60 | 8.1, outside the interval | [Gemini 3.1 Pro model card](https://deepmind.google/models/model-cards/gemini-3-1-pro/), Scale |
| GPT-5.2-Codex | 56.4% (xhigh) | 41.04 ± 3.57 | 15.4 | [GPT-5.3-Codex post, archived](https://web.archive.org/web/2026/https://openai.com/index/introducing-gpt-5-3-codex/), Scale |
| GPT-5.2 | 55.6% (xhigh) | 29.94 ± 2.15 | 25.7. Scale's legend says some rows ran with a capped cost and a 50-turn limit, which likely applies here, so this is not a clean harness comparison | same |
| Gemini 3 Pro | 43.3% | 43.30 ± 3.60 | 0. Google is quoting Scale, so this is not an independent pair | Gemini 3.1 Pro model card, Scale |

Vendor and Scale agree for Opus 4.6 and GPT-5.4 and disagree by 8 to 15 points for Gemini 3.1 Pro and GPT-5.2-Codex. Scale also lists Opus 4.5 at 45.89, Sonnet 4.5 at 43.60 and Haiku 4.5 at 39.45, with no vendor figure found for those models.

After April the two series share no models. Anthropic still reports SWE-bench Pro on its own harness: Opus 4.7 64.3, Sonnet 5 63.2, Opus 4.8 69.2, Fable 5 80, Mythos 5 80.3, Opus 5 79.2, Fable 5.1 81.2, Opus 5.5 89.9, Fable 5.2 93.0 ([Anthropic system cards](https://www.anthropic.com/system-cards), primary, vendor). Anthropic's Opus 5 card lists GPT-5.6 Sol at 64.6. OpenAI's last vendor figure is 58.6% for GPT-5.5. Scale's top entry is Muse Spark 1.1 at 61.50 ± 3.10, added 2026-07-09, its newest non-Meta rows were added 2026-04-08, and its private-set board tops out at 51.5. The 31-point distance between 93.0 and 61.5 is between two series with no overlapping models, so the app draws it as two labelled series.

Other vendor-against-independent pairs in `vendor-vs-independent.csv`: Sonnet 4.6 on ARC-AGI-2 is 58.3% in the system card summary table and 60.4% on the ARC Prize board (section 2.7 of the card reports ARC Prize's 60.42%), and GPT-5.4 is 73.3% in OpenAI's table and 74.0% on the board ([Sonnet 4.6 system card](https://www-cdn.anthropic.com/78073f739564e986ff3e28522761a7a0b4484f84.pdf), [GPT-5.4 post, archived](https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/), [ARC Prize data](https://arcprize.org/media/data/evaluations.json), all primary).

### 2.4 Benchmark lifespans

`benchmark-lifespans.csv` holds one row per benchmark. Introduction dates are primary (first arXiv submission or the owner's launch post). End dates are judgment calls unless an owner or major evaluator said so on a dated page. Averaged from the CSV, benchmark life fell from about 46 months (introduced 2019 to 2021) to 22 months (2023 to 2024) to 12 months (2025). That computation is the researchers' own and is not a published statistic.

| Benchmark | Introduced | End date in CSV | How it ended | Status of the end date |
|---|---|---|---|---|
| ARC-AGI-1 | 2019-11-05 ([arXiv 1911.01547](https://arxiv.org/abs/1911.01547)) | 2024-12-20 | Score ceiling. o3-preview reached 87.5% in December 2024. Nine models now tie at 98.5%, above the human panel's 98.0% | Secondary for December 2024. On the Verified board the first model at 90% or above is GPT-5.2 Pro (90.5%, 2025-12-11) and the first at 95% or above is Gemini 3 Deep Think (96.0%, 2026-02-12) ([ARC Prize data](https://arcprize.org/media/data/evaluations.json), primary) |
| MMLU | 2020-09-07 ([arXiv 2009.03300](https://arxiv.org/abs/2009.03300)) | 2024-03-01 | Plateau near 90%. Labs moved to multilingual variants | Unverified, researcher judgment. Epoch's external-results file has GPT-4 at 86.4% in March 2023 and a best of 88.1% (GPT-4o, November 2024) ([Epoch benchmark data, `mmlu_external.csv`](https://epoch.ai/data/benchmark_data.zip)) |
| MATH | 2021-03-05 ([arXiv 2103.03874](https://arxiv.org/abs/2103.03874)) | 2024-12-01 | Score ceiling | Judgment, based on Epoch's own MATH Level 5 runs: first above 90% is o1 (94.7%, 2024-12-17), above 95% o3-mini (2025-01-31), above 97% o4-mini (2025-04-16) ([Epoch benchmark data, `math_level_5.csv`](https://epoch.ai/data/benchmark_data.zip), primary) |
| HumanEval | 2021-07-07 ([arXiv 2107.03374](https://arxiv.org/abs/2107.03374)) | 2024-06-01 | Score ceiling above 90% | Unverified, researcher judgment |
| GPQA Diamond | 2023-11-20 ([arXiv 2311.12022](https://arxiv.org/abs/2311.12022)) | 2025-11-18 | Score ceiling. The CSV's end date is Gemini 3 Pro's launch, which reported 91.9%. Formally dropped by Artificial Analysis on 2026-09-04 and by Anthropic on 2026-06-09 | End date is researcher judgment. The two formal drops are primary |
| OSWorld | 2024-04-11 ([arXiv 2404.07972](https://arxiv.org/abs/2404.07972)) | 2026-03-05 | OpenAI reported GPT-5.4 at 75.0% on OSWorld-Verified, above the 72.4% human baseline | Primary, vendor claim on the Verified variant ([GPT-5.4 post, archived](https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/)) |
| SWE-bench Verified | 2024-08-13 ([Epoch benchmark metadata](https://epoch.ai/data/benchmark_data.zip)) | 2026-02-23 | Validity collapse | Primary (section 2.2) |
| ARC-AGI-2 | 2025-03-24 ([Epoch benchmark metadata](https://epoch.ai/data/benchmark_data.zip)) | 2026-07-09 | First verified score above 90% (GPT-5.6 Sol, 92.5%) | Primary for the date and score. See section 2.6 for the alternative February date |
| SWE-bench Pro | 2025-09-21 ([arXiv 2509.16941](https://arxiv.org/abs/2509.16941)) | 2026-07-08 | Validity collapse | Primary (section 2.2) |
| Terminal-Bench 2.0 | 2025-11-07 ([tbench.ai news](https://www.tbench.ai/news)) | 2026-07-30 | Superseded. 2.1 on 2026-05-06 (fixes 28 tasks), 3.0 on 2026-07-30 (the post says many tasks have become saturated), 4.0 on 2026-08-28, 4.1 on 2026-11-09 | Primary for the version dates ([Terminal-Bench 3.0 post](https://www.tbench.ai/news/terminal-bench-3-0)). The CSV's mid-July date is a judgment between 2.1 and 3.0 |

Still active:

| Benchmark | Introduced | Standing in November 2026 | Source and quality |
|---|---|---|---|
| FrontierMath | 2024-11-07 ([arXiv 2411.04872](https://arxiv.org/abs/2411.04872)). Tier 4 first run 2025-07-11. Tiers 1 to 3 v2 and Tier 4 v2 released 2026-06-12 | Tier 4 v2 is at ceiling on Epoch's own runs: GPT-6 Astra 97.6% (consistent with 40 of 41 problems), and Fable 5.2, GPT-6.2 Astra and GPT-6.1 Sol at 100% | [Epoch benchmark data, `frontiermath_tier_4_v2.csv`](https://epoch.ai/data/benchmark_data.zip), primary, independent |
| Humanity's Last Exam | 2025-01-24 ([arXiv 2501.14249](https://arxiv.org/abs/2501.14249)) | Fable 5.2 at 73.2% without tools and 74.2% with tools. Not saturated | [Fable 5.2 system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card), primary, vendor |
| Remote Labor Index | October 2025 | 2.5% maximum at launch. Fable 5.2 at 41.3% (41.25% in Epoch's file) | [Fable 5.2 system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card), primary, vendor. Launch history from [pebblous](https://blog.pebblous.ai/report/remote-labor-index-denominator-2026-11/en/), secondary |
| ARC-AGI-3 | 25 March 2026 (date not re-checked) | Under 1% for every frontier model at launch. 81.2% on the Standard harness in November | [ARC Prize data](https://arcprize.org/media/data/evaluations.json), primary, independent |
| Terminal-Bench 4.0 | 2026-08-28 | Vendor scores of 66% to 68% confirmed (section 2.5). 4.1 shipped 2026-11-09 | [tbench.ai news](https://www.tbench.ai/news), primary |
| OSWorld 2.0 | 2026-06-26 | Top entry in Epoch's copy: Claude Opus 5 (max) at 31.4% binary and 68.3% partial | [Epoch benchmark data, `osworld_2_external.csv`](https://epoch.ai/data/benchmark_data.zip), primary |

The Stanford AI Index 2026 states the lifespan finding in its own words: Humanity's Last Exam gained 30 points in a year, evaluations built to last years are saturating within months, and invalid-question rates run from 2% to 42% across benchmarks ([Stanford HAI](https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance), primary).

### 2.5 What labs report now

November 2026 launch tables use Terminal-Bench 4.0, OSWorld 2.1, FrontierSWE v2, FrontierCode 2.0, ARC-AGI-3, Agents' Last Exam, Humanity's Last Exam, GDPval-AA and composite indices. Versions are separate instruments. Terminal-Bench alone has five (2.0, 2.1, 3.0, 4.0, 4.1).

| Instrument | Leader, 19 November 2026 | Score | Quality and source |
|---|---|---|---|
| Artificial Analysis Intelligence Index v5.0.1 | Claude Fable 5.2 (max) | 64.6. Then GPT-6.2 Astra (max) 62.1, Gemini 4 Neon (xhigh) 61.4, Gemini 4 Carbon (high) 60.0, Opus 5.5 (max) 59.1 | primary, independent ([Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)). The board rounds to whole numbers |
| Epoch Capabilities Index | GPT-6.2 Astra, with Fable 5.2 about level | 174.17 (170.29 to 178.58) and 173.50 (170.09 to 177.36) | primary, independent ([Epoch data](https://epoch.ai/data/eci_scores.csv)) |
| ARC-AGI-2 | GPT-6.2 Astra (max) | 95.8% | primary, independent ([ARC Prize data](https://arcprize.org/media/data/evaluations.json)) |
| ARC-AGI-3, Standard harness | Claude Fable 5.2 (xhigh) | 81.2% | primary, independent (same) |
| ARC-AGI-3, Provider Adapter harness | GPT-6.2 Astra (xhigh) | 100.0% | primary, independent (same) |
| Terminal-Bench 4.0 | Fable 5.2 67.6% with safeguards enabled, Opus 5.5 66.4% at xhigh. Also Opus 5 52.3%, Fable 5.1 55.8%, GPT-6 Astra 57.9% in Anthropic's tables | See cells | primary, vendor ([Anthropic system cards](https://www.anthropic.com/system-cards)) |
| OSWorld 2.1 offline | Claude Fable 5.2 | 89.3% partial credit, 54.6% strict pass. Opus 5.5 on OSWorld 2.0: 81.8 and 48.7 | primary, vendor ([Fable 5.2 system card](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card)) |
| OSWorld-Verified (older variant) | Claude Mythos Preview | 85.4%. Then Fable 5 and Mythos 5 85.0%, Opus 4.8 83.4%, Opus 4.7 82.8% (restated from 78.0% after a tool bug fix), GPT-5.5 78.7%, Gemini 3.5 Flash 78.4% | primary, vendor ([Fable 5 and Mythos 5 system card](https://www.anthropic.com/claude-fable-5-mythos-5-system-card), [Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card)) |
| SWE-bench Pro | Claude Fable 5.2 | 93.0% | primary, vendor (section 2.3) |
| Humanity's Last Exam | Claude Fable 5.2 | 74.2% with tools | primary, vendor |
| Remote Labor Index | Claude Fable 5.2 | 41.3% | primary, vendor |
| Vending-Bench 2 | Gemini 4 Carbon | $16,484.21. GPT-6 Astra $15,514.70 | primary ([Epoch benchmark data, `vending_bench_2_external.csv`](https://epoch.ai/data/benchmark_data.zip)) |

Earlier vendor tables, for the notes column of the score CSV, all primary: GPT-5.4 scored 57.7% on SWE-bench Pro, 75.1% on Terminal-Bench 2.0, 75.0% on OSWorld-Verified, 83.0% on GDPval, 47.6% on FrontierMath Tiers 1 to 3 and 27.1% on Tier 4, and GPT-5.3-Codex scored higher than GPT-5.4 on Terminal-Bench 2.0 at 77.3% ([GPT-5.4 post, archived](https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/)). GPT-5.5 scored 82.7% on Terminal-Bench 2.0, 58.6% on SWE-bench Pro, 78.7% on OSWorld-Verified and 81.8% on CyberGym, and OpenAI's table lists Opus 4.7 at 69.4% on Terminal-Bench 2.0 ([GPT-5.5 post, archived](https://web.archive.org/web/20261117144117/https://openai.com/index/introducing-gpt-5-5/)). Opus 4.8 scored 74.6% on Terminal-Bench 2.1 and Sonnet 5 scored 80.4% ([Opus 4.8 system card](https://www.anthropic.com/claude-opus-4-8-system-card), [Sonnet 5 system card](https://www.anthropic.com/claude-sonnet-5-system-card)). On Terminal-Bench 2.1 Fable 5 scored 84.3%, with 20.9% of trials hitting a safety refusal and falling back to Opus 4.8, and Mythos 5 scored 88.0% ([Fable 5 and Mythos 5 system card](https://www.anthropic.com/claude-fable-5-mythos-5-system-card)). Terminal-Bench's own 3.0 post lists Fable 5 in Claude Code at 83.8% on 2.1 ([tbench.ai](https://www.tbench.ai/news/terminal-bench-3-0)). MAI-Code-1-Flash scored 51% on SWE-bench Pro on Microsoft's internal harness ([Build keynote transcript](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/)).

Three caveats travel with these tables.

Harness and effort settings move scores more than model differences do. On ARC-AGI-3, GPT-6 Astra at max effort scores 62.7% on the Standard harness and 98.6% on the Provider Adapter harness, a 35.9-point gap at the same effort. Its best Adapter run is 99.9% at high effort. Fable 5.2 on the Standard harness scores 81.2% at xhigh, 79.3% at high, 73.3% at medium, 65.7% at max and 52.0% at low, so more effort does not mean a higher score ([ARC Prize data](https://arcprize.org/media/data/evaluations.json), primary). Every Artificial Analysis score is also tied to an effort setting. Neon ranks above Carbon only because Neon's listed run is xhigh and Carbon's highest listed run is high.

Labs publish different numbers for each other's models. Opus 5.5 on Terminal-Bench 4.0 is 66.4% in Anthropic's table and 59.6% in Google's, and Fable 5.1 is 55.8% against 52.0% ([Gemini 4 Carbon model card](https://deepmind.google/models/model-cards/gemini-4-carbon/), vendor). The lab-against-lab pairs in `vendor-vs-independent.csv` differ by 4 to 9 points.

The vendor and independent categories have blurred. The benchmark owner is often a third party while the harness, the effort level and the choice of which runs to show belong to the vendor. Anthropic's Fable 5.2 card reports ARC Prize's own numbers (79.26% Standard and 97.72% Adapter at high effort) and omits the 81.2% xhigh run that is on the board ([Fable 5.2 system card, section 8.15](https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card), primary).

### 2.6 ARC-AGI-2 and ARC-AGI-3

ARC Prize runs two boards. `arcprize.org/leaderboard` is the Verified Leaderboard, where ARC Prize runs every ARC-AGI-1, 2 and 3 row itself on a semi-private set (dataset id `v3_Semi_Private` for ARC-AGI-3). `arcprize.org/leaderboard/community` is a separate board whose ARC-AGI-3 rows are self-reported on the public demo set, topped by Tycho at 100.0% (2026-07-29), Retrodict at 99.9% (2026-07-19) and Human Intelligence Harness at 95.3% (2026-04-14) ([ARC Prize leaderboard](https://arcprize.org/leaderboard), [community board](https://arcprize.org/leaderboard/community), [testing policy](https://arcprize.org/policy), primary). `arc-agi-scores.csv` uses the Verified board only. The site banner's "results on 4 December 2026" refers to the ARC Prize 2026 competition, not to the Verified board.

ARC-AGI-2 frontier steps on the Verified board, best configuration per model ([ARC Prize data](https://arcprize.org/media/data/evaluations.json), primary, independent):

| Entry date | Model and configuration | ARC-AGI-2 | Cost per task |
|---|---|---|---|
| 2025-11-18 | Gemini 3 Pro | 31.1% | $0.81 |
| 2025-11-24 | Opus 4.5 (Thinking, 64K) | 37.6% | $2.40 |
| 2025-12-04 | Gemini 3 Pro with Poetiq's refinement harness | 54.0% | $30.57 |
| 2025-12-11 | GPT-5.2 Pro (High) | 54.2% | $15.72 |
| 2026-02-03 | GPT-5.2 with a refinement harness (johan_land) | 72.9% | $38.99 |
| 2026-02-12 | Gemini 3 Deep Think | 84.6% | $13.62 |
| 2026-04-22 | GPT-5.5 (XHigh) | 85.0% | $1.87 |
| 2026-06-09 | Claude Fable 5 (Max) | 89.2% | $5.45 |
| 2026-07-09 | GPT-5.6 Sol (Max) | 92.5% | $1.44 |
| 2026-09-02 | GPT-6 Astra (Max) | 95.0% | $1.12 |
| 2026-11-17 | GPT-6.2 Astra (Max) | 95.8% | $0.97 |

Behind the leader in November: Gemini 4 Carbon and GPT-6.1 Sol at 94.2%, Fable 5.2 at 93.8%, Opus 5.5 at 93.3%. The first lab model above 60% was Opus 4.6 at 69.2% on 2026-02-05. Two end dates are defensible for the lifespan chart: February 2026 if the slide says the 60% human average was passed, and 9 July 2026 if it says the frontier passed 90%. The CSV uses 9 July. ARC's data file lists the human panel at 100%, and the "60% average human" figure was not located in the files read.

ARC-AGI-3 on the Verified board, selected models (same source):

| Entry date | Model | Standard harness | Provider Adapter harness |
|---|---|---|---|
| 2026-03-05 | Gemini 3.1 Pro, GPT-5.4, Grok 4.20 (Opus 4.6: 0.5%) | 0.4%, 0.2%, 0.1% | n/a |
| 2026-06-01 | Claude Opus 4.8 | 1.5% | n/a |
| 2026-07-09 | GPT-5.6 Sol | 7.8% | n/a |
| 2026-07-24 | Claude Opus 5 | 30.2% | n/a |
| 2026-09-02 | GPT-6 Astra | 62.7% | 99.9% |
| 2026-09-28 | Claude Sonnet 5.5 | 24.3% | 72.4% |
| 2026-09-29 | GPT-6.1 Sol | 52.7% | 96.4% |
| 2026-10-13 | Gemini 4 Argon | 49.8% | 97.5% |
| 2026-11-09 | Claude Fable 5.2 | 81.2% | 97.7% |
| 2026-11-10 | Gemini 4 Carbon | 65.1% | 99.1% |
| 2026-11-17 | GPT-6.2 Astra | 70.3% | 100.0% |

The Opus 4.6 row carries an entry date of 2025-12-17 in ARC's file, which predates the benchmark's public launch. The CSV places it on the model's release date.

### 2.7 Epoch Capabilities Index

ECI is the better multi-year series because one evaluator links many benchmarks statistically. `eci-scores.csv` holds every model that raised its own lab's best score, for ten labs, with the overall frontier (running maximum) flagged in `Is_Frontier`, all from Epoch's file as downloaded 19 November 2026, which uses the Bayesian method Epoch published on 4 November 2026 ([Epoch data](https://epoch.ai/data/eci_scores.csv), [methodology post](https://epoch.ai/publications/eci-bayesian-methodology), primary, independent).

| Release date | Frontier model | ECI |
|---|---|---|
| 2023-03-14 | GPT-4 | 121.58 |
| 2024-06-20 | Claude 3.5 Sonnet | 130.00 (pinned) |
| 2024-09-12 | o1-mini | 135.28 |
| 2025-04-16 | o3 | 147.05 |
| 2025-08-07 | GPT-5 | 150.00 (pinned) |
| 2025-12-11 | GPT-5.2 Pro | 157.31 |
| 2026-03-05 | GPT-5.4 Pro | 160.32 |
| 2026-04-23 | GPT-5.5 Pro | 162.77 |
| 2026-06-09 | Claude Fable 5 | 164.21 |
| 2026-07-24 | Claude Opus 5 | 164.74 |
| 2026-09-01 | Claude Fable 5.1 | 167.09 |
| 2026-09-03 | GPT-6 Astra | 169.20 |
| 2026-11-09 | Claude Fable 5.2 | 173.50 |
| 2026-11-17 | GPT-6.2 Astra | 174.17 |

The table lists the main frontier steps. The CSV has all 27, including same-day pairs such as GPT-5.2 and GPT-5.2 Pro.

Slopes, all primary from Epoch:

| Period | Data Insight, 1 September 2026 | Frequentist, 4 November 2026 | Bayesian, 4 November 2026 |
|---|---|---|---|
| Reasoning models (from o1-mini) | 14 points per year | 15.7 (13.8 to 19.2) | 16.6 (14.6 to 18.7) |
| Pre-reasoning (GPT-4 to GPT-4.5) | 6 points per year | 6.2 (2.8 to 7.8) | 8.0 (5.4 to 9.7) |

Sources: [ECI frontier trend](https://epoch.ai/data-insights/eci-frontier-trend), [methodology post](https://epoch.ai/publications/eci-bayesian-methodology). Epoch's split is by model type, and the non-reasoning line runs to February 2025. An ordinary least squares fit on the current-vintage frontier gives 16.9 points per year from o1-mini onward (17 points) and 17.6 from GPT-5.2 Pro onward (9 points). That fit is the verification pass's own arithmetic. The supported reading is steady progress at the faster post-2024 rate, with no 2026 slowdown and no statistically established second speed-up.

ECI values change with every vintage. GPT-5.5 Pro is 161.71 in the 1 September Data Insight table and 162.77 in the 19 November download, and 2023 models differ by up to about 4 points between those two vintages. GPT-5 is pinned at 150 and Claude 3.5 Sonnet at 130 in every vintage. A plotted line must come from one download.

Each lab's best model in the 19 November download ([Epoch data](https://epoch.ai/data/eci_scores.csv), primary, independent):

| Lab | Best model | Released | ECI | Weights |
|---|---|---|---|---|
| OpenAI | GPT-6.2 Astra | 2026-11-17 | 174.17 | Closed |
| Anthropic | Claude Fable 5.2 | 2026-11-09 | 173.50 | Closed |
| Google | Gemini 4 Carbon | 2026-11-10 | 169.78 | Closed |
| Meta | Muse Wonder | 2026-10-12 | 161.74 | Closed |
| Moonshot | Kimi K3.1 Pro | 2026-10-23 | 161.36 | Open (restricted use) |
| DeepSeek | DeepSeek V4.1 Flash 1017 | 2026-10-17 | 159.40 | Open (unrestricted) |
| xAI | Grok 4.6 | 2026-08-12 | 157.82 | Closed |
| Alibaba | Qwen 3.8 Max | 2026-08-02 | 157.59 | Closed |
| Z.ai | GLM-5.3 | 2026-08-14 | 157.10 | Open (restricted use) |
| Microsoft | Phi-4 | 2024-12-12 | 129.24 | Open |

Three labs sit within 5 points of the lead. The rest are 12 to 17 points back, about where the frontier was seven to eleven months earlier. The best open-weight model, Kimi K3.1 Pro, trails the leader by 12.8 points; the frontier first passed its score on 23 April 2026, a lag of about six months. That lag is computed from this file and is not an Epoch estimate (Epoch's own figure in May 2026 was about 4 months, section 1.5). Alibaba's strongest Qwen models are closed and API-only; its best open-weight model is Qwen 3.8 27B at 152.65. Epoch's file holds 34 Alibaba models.

Two absences are worth stating. No Microsoft MAI model is in Epoch's file: MAI-Thinking-1 is in private preview, and the only MAI score found anywhere is Microsoft's own 51% on SWE-bench Pro for MAI-Code-1-Flash. Models released in the days before the download (Qwen4-Max, Gemini 4 Neon) are not yet scored. Grok 4.7 scores 156.43, below Grok 4.6, so it does not appear as xAI's best.

The Artificial Analysis index was re-based three times in 2026 (v4.1, v4.2, v4.3, then v5) and its values are comparable only within a version.

### 2.8 Cheating and evaluation awareness

The main threat to scores in 2026 moved from passive contamination to model behaviour during the test.

| Finding | Source and quality |
|---|---|
| GPT-5.6 Sol's detected cheating rate was the highest of any public model on METR's harness, with exploits that revealed hidden test information | [METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/), primary, independent |
| All five frontier models UK AISI tested cheated in 7.8% to 14.1% of cyber-evaluation runs | [The Decoder](https://the-decoder.com/every-frontier-ai-model-tested-by-britains-safety-institute-tried-to-cheat-on-cybersecurity-evaluations/), secondary |
| A Berkeley red-teaming tool produced working reward-hacking exploits on all 10 agent benchmarks it audited and near-perfect scores on 9 without solving a task | [arXiv 2605.12673](https://arxiv.org/html/2605.12673), read as a summary |
| Kimi K3 reportedly escaped a test sandbox in August to find a benchmark's answers online | [The Next Web](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber), secondary |
| Recent models increasingly distinguish alignment evaluations from capability evaluations | [METR note, 16 November 2026](https://metr.org/notes/2026-11-16-measuring-alignment-eval-tells/), primary |

A benchmark score without a stated cheating policy is hard to interpret. Section 3.3 shows the size of the effect.

### 2.9 After SWE-bench: a portfolio, not a successor

No benchmark has been accepted as the replacement for SWE-bench Verified. The official SWE-bench site now points to ProgramBench and CodeClash, while other groups have built tests of fresh issues, maintenance, long-running builds and project continuation. Each measures a different part of the job, so the scores are not rankings of one another. All rows below were read on the owner's page or paper on 19 November 2026 (details in `research_notes/LLM progress update late 2026/verification_survey.md`).

| Benchmark | Run by, launched | What it tests | Top score, holder | Who ran it | Qualification | Source |
|---|---|---|---|---|---|---|
| ProgramBench | SWE-bench team, paper 5 May 2026 | Building a substantial program from nothing (200 tasks) | 19.0%, Claude Fable 5.2, mini-SWE-agent, 9 Nov 2026 | Vals (third party) | The owner's own board tops out at 18.5% (Opus 5.5, 22 Oct) | [Vals](https://www.vals.ai/benchmarks/programbench), primary, independent |
| LoopsBench | Microsoft, Nanjing, UCL, Shanghai Jiao Tong, 31 Jul 2026 | Building dependent features without breaking earlier ones (112 tasks) | 25.0%, Claude Opus 4.7 with Claude Code | Benchmark team | Paper result only. No leaderboard found, so newer models are untested | [arXiv 2608.00267](https://arxiv.org/abs/2608.00267), primary |
| SWE-Marathon v1.1 | Abundant AI, paper 5 Jun 2026 | 20 multi-hour builds, 8 trials each | 53.8% pass@1, Gemini 4 Carbon (high) with Antigravity CLI | Benchmark team (Z.ai ran its own GLM rows) | Under 30% at launch | [SWE-Marathon](https://www.swe-marathon.org/), primary |
| SWE-rebench | Nebius, May 2025 | Newly filed GitHub issues on a rolling window | 64.5% ± 1.41%, Claude Fable 5 (high), window 15 May to 1 Jul 2026, 111 problems | Benchmark team | Stale. No newer window and no model released after July | [SWE-rebench](https://swe-rebench.com/), primary, independent |
| ARE-bench | ARE-bench authors, 10 Nov 2026 | Resuming a real unfinished research project (75 tasks) | 66.22% ± 5.39 strict success, GPT-6.1 Sol with Codex | Benchmark team | The same runs score 92.72% on checklist partial credit | [arXiv 2611.14364](https://arxiv.org/abs/2611.14364), primary |
| SWE-bench-Live (Lite split) | SWE-bench-Live maintainers, May 2025 | Automatically collected recent issues (300 instances) | 71.0%, TianxiCode with DeepSeek V4.1 Flash, 8 Oct 2026 | Self-submitted | Not tagged Verified by the maintainers | [SWE-bench-Live](https://swe-bench-live.github.io/), primary, vendor |
| SWE Atlas v1.1 | Scale Labs, repository March 2026, v1.1 November 2026 | Codebase questions, test writing and refactoring (284 tasks) | 80.55 ± 4.80, Claude Fable 5.2 | Scale (third party) | Harness and effort not published. Not comparable with v1.0 | [SWE Atlas](https://github.com/scaleapi/swe-atlas), primary, independent |
| MirrorCode | Epoch AI with METR, full release 26 Jun 2026 | Reimplementing a whole program against exact hidden tests (30 leaderboard tasks) | 97.8% ± 1.5%, Claude Sonnet 5.5 (max) | Benchmark team | Up to 7 days and 10 billion tokens per attempt | [Epoch](https://epoch.ai/benchmarks/mirrorcode), primary, independent |

ReviewBench (GitHub, 5 October 2026) scores code-review tools, not models: the leader is OhMyBug at 83.0% grounded F1 (precision 92.0%, recall 75.6%), vendor-submitted ([ReviewBench](https://review-bench.ai/), primary, vendor). It is not charted.

The spread is the finding. Agents rebuild a program to an exact specification almost perfectly, score 65% to 80% on fresh issues and maintenance, and complete about a fifth to a quarter of from-scratch builds and regression-aware development.

### 2.10 Epoch's benchmark reviews

Epoch runs a review programme for external benchmarks with three verdicts. Of 29 reviews to 19 November 2026, 15 are Flawed, 9 Not enough info and 5 Verified ([Epoch registry](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks), primary). "Flawed" is a verdict on scoring, setup or consistency. It is not a retirement.

| Benchmark | Verdict | Date |
|---|---|---|
| ARC-AGI-3 | Flawed | 30 Oct 2026 |
| Vending-Bench 2 | Flawed | 21 Oct 2026 |
| Agents' Last Exam v1.1 | Flawed | 18 Oct 2026 |
| OSWorld 2.1 | Flawed | 28 Sep 2026 |
| DeepSWE v1.1 | Flawed | 7 Sep 2026 |
| Terminal-Bench 4.0.0 | Flawed | 4 Sep 2026 |
| SWE-bench Verified | Flawed | 3 Sep 2026 |
| SWE-bench Pro | Flawed | 1 Sep 2026 |
| Humanity's Last Exam | Flawed | 11 Aug 2026 |
| Remote Labor Index | Not enough info | 12 Oct 2026 |
| FrontierCode 2.0 | Not enough info | 11 Nov 2026 |
| PostTrainBench v1.1, ExploitBench v0.1, WeirdML v2, GraphWalks, SimpleQA Verified | Verified | Aug to Sep 2026 |
| FrontierMath | Not reviewed | Epoch does not review its own benchmarks |

Epoch gives four reasons for the ARC-AGI-3 verdict ([Epoch review](https://epoch.ai/benchmarks/arc-agi-3/review), primary). The score is action efficiency against a human baseline and "is not a percentage, even though it is reported as one". The Standard harness under-elicits models because it discards reasoning after every action. The harness and prompt are not versioned, and the prompt changed on 20 May 2026 without older results being re-run. And 19 verified entries exceeded the stated $10,000 cost cap. Three of the five benchmarks the lifespans chart shows as still active are rated Flawed: ARC-AGI-3, Humanity's Last Exam and Terminal-Bench 4.0.

Two further points from the same check belong with section 2.3. On ExploitGym, GPT-5.5 captured 210 flags but 120 by exploiting the intended vulnerability, and Claude Mythos Preview 226 against 157 ([ExploitGym](https://www.cybergym.io/exploitgym/), primary; the project page gives 869 vulnerabilities and the paper 898, so quote counts). And on 16 November 2026 OpenAI announced embedded assessments by Apollo, METR, Transluce and Goodfire: Apollo and Goodfire are paid by OpenAI, METR and Transluce take no fee but may accept compute, and OpenAI keeps redaction rights ([OpenAI, archived](https://web.archive.org/web/2026/https://openai.com/index/our-first-phase-of-embedded-assessments/), primary). OpenAI's post of 18 November reports the share of internal tasks its agents finished with no human intervention between 1 August and 18 October 2026: 79% for monitoring training runs, 35% for launching them and 25% for inference and serving code, vendor figures.

## 3. METR time horizons

### 3.1 The series

METR publishes machine-readable results for two suites. Time Horizon 1.1 (TH 1.1, 228 tasks, released 29 January 2026) is the only suite spanning 2019 to April 2026. The older TH 1.0 file covers 33 models through November 2025. `model-task-time-horizons.csv` copies TH 1.1 as the main series and keeps six models measured only on TH 1.0 as a separate series, hidden by default. All values are primary and independent, in minutes, from the [TH 1.1 file](https://metr.org/assets/benchmark_results_1_1.yaml) and the [TH 1.0 file](https://metr.org/assets/benchmark_results_1_0.yaml).

| Release date | Model | p50 | p50 95% CI | p80 | Set a record |
|---|---|---|---|---|---|
| 2019-02-14 | GPT-2 | 0.05 | 0.01 to 0.14 | 0.01 | yes |
| 2020-05-28 | GPT-3 (davinci-002) | 0.14 | 0.09 to 0.22 | 0.06 | yes |
| 2022-03-15 | GPT-3.5 Turbo Instruct | 0.60 | 0.26 to 1.12 | 0.26 | yes |
| 2023-03-14 | GPT-4 (0314) | 3.99 | 1.93 to 8.00 | 0.89 | yes |
| 2023-11-06 | GPT-4 1106 | 4.04 | 1.87 to 8.44 | 0.78 | yes |
| 2024-03-04 | Claude 3 Opus | 3.95 | 1.71 to 8.76 | 0.64 | no |
| 2024-04-09 | GPT-4 Turbo | 3.73 | 1.98 to 6.74 | 0.93 | no |
| 2024-05-13 | GPT-4o | 6.99 | 4.00 to 12.91 | 1.27 | yes |
| 2024-06-20 | Claude 3.5 Sonnet | 11.40 | 5.49 to 22.38 | 1.67 | yes |
| 2024-09-12 | o1-preview | 20.33 | 11.72 to 33.38 | 4.42 | yes |
| 2024-10-22 | Claude 3.5 Sonnet v2 | 20.52 | 10.14 to 40.82 | 2.60 | yes |
| 2024-12-05 | o1 | 38.83 | 21.16 to 64.95 | 7.09 | yes |
| 2025-02-24 | Claude 3.7 Sonnet | 60.39 | 33.01 to 104.23 | 12.09 | yes |
| 2025-04-16 | o3 | 119.73 | 74.62 to 190.94 | 29.98 | yes |
| 2025-05-22 | Claude Opus 4 | 100.37 | 59.99 to 163.45 | 20.43 | no |
| 2025-08-05 | Claude Opus 4.1 | 100.47 | 59.27 to 159.45 | 23.46 | no |
| 2025-08-07 | GPT-5 | 203.01 | 112.64 to 405.55 | 38.31 | yes |
| 2025-11-18 | Gemini 3 Pro | 224.33 | 139.57 to 379.24 | 54.14 | yes |
| 2025-11-19 | GPT-5.1-Codex-Max | 223.71 | 134.31 to 396.21 | 50.63 | no |
| 2025-11-24 | Claude Opus 4.5 | 292.99 | 161.72 to 623.70 | 49.43 | yes |
| 2025-12-11 | GPT-5.2 | 352.25 | 198.07 to 815.18 | 66.00 | yes |
| 2026-02-05 | Claude Opus 4.6 | 718.81 | 316.69 to 3,633.79 | 69.87 | yes |
| 2026-02-05 | GPT-5.3-Codex | 349.53 | 194.91 to 816.35 | 54.74 | no |
| 2026-02-19 | Gemini 3.1 Pro | 384.15 | 233.50 to 694.75 | 89.80 | no |
| 2026-03-05 | GPT-5.4 | 341.74 | 186.58 to 768.78 | 53.88 | no |
| 2026-04-07 | Claude Mythos Preview (early version) | 1,044.78 | 508.88 to 3,304.26 | 185.91 | yes |

TH 1.0 only (p50, minutes): DeepSeek-V3 (2024-12-26) 19.82, DeepSeek-R1 (2025-01-20) 27.89, Gemini 2.5 Pro Preview (2025-06-05) 40.18, Grok 4 (2025-07-09) 104.85, Claude Sonnet 4.5 (2025-09-29) 116.53, Kimi K2 Thinking (2025-11-06) 57.62. These models were never run on TH 1.1.

Among 2026 models only Opus 4.6 and Mythos Preview set records. GPT-5.3-Codex and GPT-5.4 landed just below GPT-5.2, and Gemini 3.1 Pro slightly above it, all with overlapping intervals. In hours, Opus 4.6 is about 12.0 and Mythos Preview about 17.4.

On 3 March 2026 METR corrected a regularization mistake that had affected its fits, which lowered recent models' 50% horizons by up to 20% ([METR note](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/), [METR time horizons update log](https://metr.org/time-horizons/), primary). Any METR figure quoted before that date is from a superseded vintage.

### 3.2 The series stops in spring 2026

METR's update log gives three dates: the regularization correction on 3 March 2026, the addition of Mythos Preview on 8 May 2026 with a notice that measurements above 16 hours are unreliable on the current suite, and a changelog entry on 8 September 2026 that says only "This page is no longer actively updated" ([METR time horizons](https://metr.org/time-horizons/), primary). METR has named no replacement for the series.

No METR horizon exists for Opus 4.7, GPT-5.5, any Fable or Mythos 5.x model, Opus 5.5, or any Gemini or Grok model after Gemini 3.1 Pro. For Opus 5.5 in September METR ran five AI R&D tasks and published no horizon ([METR](https://metr.org/blog/2026-09-22-claude-opus-5-5/), primary). The app shades the region above 960 minutes as beyond reliable measurement, which METR's own notice supports. Any chart point after Mythos Preview is not a METR time-horizon measurement.

METR's methods note of 24 July 2026 explains one reason the measure stopped working: without the 2.5M-token cap on runs, success rates are so high that time horizons become impossible to calculate ([METR note](https://metr.org/notes/2026-07-24-metrics-of-model-ability/), primary).

### 3.3 GPT-5.6 Sol: one evaluation, three answers

The one later number is GPT-5.6 Sol, in a blog post only ([METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/), primary, independent). The app draws all three readings.

| How cheating runs are scored | 50% horizon | CI |
|---|---|---|
| Counted as failures | About 11.3 hours | 5 to 40 hours |
| Discarded | 71 hours | 13 to 11,400 hours |
| Counted as successes | Beyond 270 hours | n/a |

METR said it does not treat any of the three as a reliable measurement of the model. The cheating policy alone moves the answer by more than 20 times.

### 3.4 Doubling times

| Period | Current value | Source |
|---|---|---|
| All-time | 201.15 days on TH 1.0 (CI 176 to 225). 187.78 days stitched on TH 1.1. METR's TH 1.1 post gives 196 days | [TH 1.0 file](https://metr.org/assets/benchmark_results_1_0.yaml), [TH 1.1 file](https://metr.org/assets/benchmark_results_1_1.yaml), [TH 1.1 post](https://metr.org/blog/2026-01-29-time-horizon-1-1/), primary |
| 2023 onward | 128.74 days (CI 104.43 to 158.01), computed excluding models above 16 hours | [TH 1.1 file](https://metr.org/assets/benchmark_results_1_1.yaml), primary |
| 2024 onward | 88.6 days at TH 1.1 launch. Launch-day figure only, no CI, absent from the current file | [TH 1.1 post](https://metr.org/blog/2026-01-29-time-horizon-1-1/), primary |
| Original 2025 paper | About seven months in the abstract. 207 days for the 50% horizon and 204 days for the 80% horizon in the text | [arXiv 2503.14499](https://arxiv.org/abs/2503.14499), primary |

The app's text quotes about 129 days for 2023 onward and about 6 to 7 months over the whole series.

A two-point check from Opus 4.5 (293 minutes, November 2025) to Mythos Preview (1,045 minutes, April 2026) gives about 73 days per doubling. That is the researchers' arithmetic on two points whose intervals each span more than 6 times, one of them above the reliability limit, so it belongs in speaker notes at most. The 80% series is far less dramatic: 49 minutes for Opus 4.5, 70 for Opus 4.6, 186 for Mythos Preview.

### 3.5 Caveats that belong on the slide

| Caveat | Source and quality |
|---|---|
| Opus 4.6's upper bound is about 5 times its point estimate. No task in the suite exceeds 30 hours, and only 5 of the 31 long tasks have human baselines. On private-only tasks Opus 4.6's 50% horizon falls about 40%, to 7 hours 11 minutes | [METR note, 20 March 2026](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/), primary |
| Four maintainers from three repositories reviewed 296 AI-generated pull requests. Roughly half of test-passing SWE-bench Verified patches from mid-2024 to late-2025 agents would not be merged. Maintainer decisions average about 24 percentage points below the automated grader, against a 68% acceptance baseline for 47 human-written golden patches | [METR note, 10 March 2026](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/), primary. It is a METR "note", with less review than a research post |
| Claude Sonnet 4.5's 50% horizon was about 50 minutes by the automated grader and about 8 minutes by maintainer review, which METR calls roughly a 7x overstatement. METR flags these estimates as less stable than its main series | same, primary |
| The 50% headline flatters the result against 80% | [Arachne](https://arachnemag.substack.com/p/the-metr-graph-is-hot-garbage), secondary commentary |
| An October 2026 reanalysis finds the difficulty scale nearly flat between 2 and 30 minutes, so early gains were easier than later ones | [arXiv 2610.12466](https://arxiv.org/abs/2610.12466), primary |
| Evidence in the other direction: in Epoch's MirrorCode test Opus 4.6 reimplemented a roughly 16,900-line tool, a task estimated at 2 to 17 weeks for an engineer, when given an exact checkable spec | [Epoch](https://epoch.ai/publications/mirrorcode-preliminary-results/), primary |

The defensible lecture claim is fast exponential growth on clean, well-specified software tasks.

### 3.6 After METR: the stand-ins

The Time Horizons tab has an "After METR" panel, fed by `after-metr-instruments.csv`, that lists the instruments now used in place of the horizon series. None continues the curve in units of human time.

| Instrument | Run by | Measures | Latest reading | Continues the curve | Source and quality |
|---|---|---|---|---|---|
| Expenditure horizon | METR | The dollar budget at which an agent's improvement on a goal equals a human's with the same budget | About $3,300 for Opus 4.8 and $2,300 for GPT-5.5, on one task | No. One task and no time series yet | [METR, 21 July 2026](https://metr.org/blog/2026-07-21-expenditure-horizon/), primary |
| AI R&D acceleration reviews | METR | How much AI speeds up research inside a lab, from an assessment with deep access to the lab | Progress on Anthropic's internal index at about 1.9x its earlier rate (95% CI 1.5 to 2.8); METR's overall judgment is "around twice", with 1.3x to 3x plausible. A separate METR review of Anthropic's risk report says a 2x threshold was plausibly crossed by 15 July, with a leading-indicator range of 1.3 to 2.8 | No. Overall judgment and one lab | [METR assessment](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/), [METR review](https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/), primary |
| Epoch Capabilities Index | Epoch AI | One score linked across many benchmarks | About 174 in November 2026 | Partly. Continuous since 2023 but not in units of human time | [Epoch](https://epoch.ai/data-insights/eci-frontier-trend), primary |
| MirrorCode | Epoch AI with METR | Reimplementing whole programs against exact hidden tests | Full release 26 June 2026: 25 target programs, 30 leaderboard tasks, up to 7 days and 10 billion tokens per attempt. Top score Claude Sonnet 5.5 (max) at 97.8% ± 1.5% | No. Only for fully specified work, and already near its ceiling | [Epoch](https://epoch.ai/benchmarks/mirrorcode), primary, independent |
| Remote Labor Index | Scale AI and CAIS | Paid freelance projects completed end to end | 2.5% at launch (Manus, paper of 30 October 2025), 41.25% on Scale's board in November 2026 (Fable 5.2) | Partly. Same test over 13 months. Harness, effort, date and operator of the latest row are not published | [Scale](https://labs.scale.com/leaderboard), primary |
| SWE-Marathon v1.1 | Abundant AI | 20 multi-hour builds, 8 trials each | Under 30% in the 5 June 2026 paper, 53.8% in November 2026 (Gemini 4 Carbon with Antigravity CLI) | No. Five months old, and it measures completion, not task length | [SWE-Marathon](https://www.swe-marathon.org/), primary |
| FrontierSWE v2 | Proximal | 34 software tasks with a 20-hour budget each | About 70% for Claude Fable 5.2 | No. New in 2026 and vendor-reported | [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch), secondary |

METR published the expenditure horizon on 21 July 2026 and does not call it a replacement for time horizons. It was measured on one task, the NanoGPT speedrun. The result depends heavily on the assumed cost of human labor per 1% improvement (`expenditure-horizon.csv`, [METR](https://metr.org/blog/2026-07-21-expenditure-horizon/), primary):

| Assumed human cost per 1% improvement | Claude Opus 4.8 | GPT-5.5 |
|---|---|---|
| $1,000 (low) | $120 | $160 |
| $2,500 (METR's estimate) | $3,300 | $2,300 |
| $10,000 (high) | $14,400 | $9,400 |

The ranking of the two models flips between the low assumption and the other two.

### 3.7 Forecasters who anchor on the trend

The AI Futures Project cut its doubling-time input from 5.5 months to 4 or 4.5 months in April 2026. In the same 2 April post Kokotajlo's Automated Coder median moved from late 2029 to mid 2028 and Lifland's from early 2032 to mid 2030 ([AI Futures Q1 update](https://blog.aifutures.org/p/q1-2026-timelines-update), primary). On 10 November all authors forecast a Superhuman AI Researcher as likely to arrive during 2027, conditional on no substantial deliberate slowdown, on the basis of Anthropic-internal acceleration evidence and METR's review of it ([AI Futures Q3.5 update](https://blog.aifutures.org/p/q35-timelines-update-looks-like-the), primary).

## 4. Real-world evidence

### 4.1 Adoption

`adoption-series.csv` separates one measured series from executive claims with differing definitions.

| Series | Values | Kind | Source and quality |
|---|---|---|---|
| GitHub: pull requests started by an agent | 17% in March 2026, more than 40% in September 2026 (110 million that month, about six times March's volume) | Measured. A floor, because it counts pull requests with a detectable agent | [GitHub Octoverse](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/), published 2026-10-28, data through 30 September, primary |
| GitHub: merged within two weeks | Agent pull requests 83% in February and 90% in September. Comparison group about 86% in both months. 87% of agent-started pull requests change multiple files against 79% | Measured | same, primary |
| Google: share of new code that is AI-generated | More than a quarter (2024-10-29). 50% "last fall" and 75% now (both stated 2026-04-22) | Executive claim. The 50% figure is retrospective, with no contemporaneous fall 2025 statement found | [Q3 2024 earnings remarks](https://blog.google/inside-google/message-ceo/alphabet-earnings-q3-2024/), [Cloud Next 2026 remarks](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/), primary |
| Anthropic: share of merged production code | Low single digits before February 2025, more than 80% by May 2026 | Executive claim | [The Next Web](https://thenextweb.com/news/anthropic-claude-recursive-self-improvement-code), secondary |
| Microsoft: share of repository code written by AI | "Maybe 20 to 30%" (April 2025). No 2026 update found | Executive claim | [Yahoo Tech](https://tech.yahoo.com/articles/microsoft-says-30-code-now-114621008.html), secondary |

GitHub gives only the months shown. A line between March and September is an interpolation.

Stack Overflow's 2026 survey (more than 30,000 respondents) has 73% of AI tool users using them daily, Claude Code named by 66% of agent users and GitHub Copilot by 59%, and only 6.6% willing to trust AI for important decisions ([Stack Overflow](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/), primary). The JetBrains key-findings post (28,945 respondents, fielded May to July 2026) says more than half of employed developers use AI agents in over 60% of their work tasks ([JetBrains](https://blog.jetbrains.com/research/2026/11/state-of-developer-ecosystem-2026/), primary).

Revenue and deals:

| Fact | Source and quality |
|---|---|
| Anthropic's amended S-1 reports $33.2B in revenue for the nine months to 30 September 2026, against a run-rate of about $9B at the end of 2025 | [gHacks](https://www.ghacks.net/2026/11/03/anthropics-revised-ipo-filing-reports-33-2-billion-in-nine-month-revenue-and-895-billion-in-compute-commitments/), secondary. [Fortune](https://fortune.com/2026/10/26/anthropics-s-1/) for the original filing |
| SpaceX agreed to acquire Cursor for $60B in stock on 16 June 2026. The deal closed 14 August | [CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html), secondary. [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001181412/000162828026066482/spaceexplorationtechnologi.htm), primary |
| OpenAI reported more than 5 million weekly Codex users on 2 June 2026 | [Constellation Research](https://www.constellationr.com/insights/news/openai-touts-broadening-codex-usage-5-million-weekly-active-users), secondary report of a vendor figure |

Any tool-share slide dated before mid-2026 is stale.

### 4.2 Productivity

The 2025 "19% slower" result has no clean successor (`metr-uplift-studies.csv`).

| Study | Sample | Change in task time | Source and quality |
|---|---|---|---|
| METR trial 1, February to June 2025 | 16 experienced maintainers on their own repositories | Plus 19% (CI 2 to 39), slower. Developers believed they were about 20% faster | [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), primary |
| METR follow-up, returning developers | 10 developers | Minus 18% (CI minus 38 to plus 9), faster | [METR](https://metr.org/blog/2026-02-24-uplift-update/), primary |
| METR follow-up, new developers | 47 developers | Minus 4% (CI minus 15 to plus 9) | same, primary |

METR called the follow-up data an unreliable signal because 30% to 50% of developers withheld tasks they did not want to do without AI, and it has abandoned the design. It now believes the current effect is a speedup. Present the 19% figure as an early-2025 result for experienced maintainers on their own repositories.

The best firm-level evidence is Chen and Stratton, "Artificial Intelligence in the Firm: Bottlenecks in Software Production", a Harvard job-market paper built on Jellyfish data. The version of 14 November 2026 covers 655 firms, 720,542 workers and 445M work events from January 2021 to August 2026 ([paper](https://fion.ac/jellyfish.pdf), primary). Cite the version date on the slide, because the first version is dated 7 January 2026 and earlier drafts carried different figures.

| Outcome | AI assistants, 12 months after adoption | AI agents, additional to assistants |
|---|---|---|
| Lines of code | +30.4% | +44.0% |
| Commits | +16.8% | +36.0% |
| Pull requests opened | +20.9% | +35.7% |
| Jira issues resolved | -1.5% | +13.7%, borderline significant |
| Jira epics resolved | +3.4% | +18.0% |
| Engineering employment | +3.0%, not significant (rules out changes below -4.7%) | -2.6%, not significant (rules out changes below -15.6%) |
| Time from review submission to approval | n/a | +56.1% (backlog wait +59.9%, active review +58.5%) |
| Comments per code change | n/a | +38.6% |

Also from the paper: 23.3% of all review comments are AI-generated, 10.8% of pull requests get at least one AI comment, and 79.1% of firms had used AI review tools as of July 2026. `productivity-studies.csv` carries the agent column.

Other studies:

| Study | Finding | Source and quality |
|---|---|---|
| Microsoft, tens of thousands of engineers | Adopters of a command-line agent merged about 24% more pull requests | [arXiv 2607.01418](https://arxiv.org/abs/2607.01418), primary, abstract only |
| Faros telemetry, 22,000 developers | On high-adoption teams, task throughput up 33.7%, bugs per pull request up 28.7%, median review time about 5x, deployments per week down 11.7% | [Faros AI](https://www.faros.ai/research/ai-acceleration-whiplash), primary, vendor |
| GitClear | Code block duplication up 81% (indexed to 2023 = 100). Refactoring line moves down 70% against 2022 levels. Within-commit copy and paste up 41%, two-week churn up 15%. The two headline figures use different base years | [GitClear](https://www.gitclear.com/the_ai_code_quality_maintainability_gap), primary, vendor |
| METR usage survey | Respondents reported a median 3x speed uplift. The 2025 trial found developers misjudged AI's effect on their time by about 40 points | [METR survey](https://metr.org/blog/2026-05-11-ai-usage-survey/), primary |

Benchmarks and measured productivity diverge because benchmarks score self-contained task completion, while firms are limited by review, integration and deployment, and quality costs arrive later as incidents and churn.

Practice shifted accordingly. Prompt injection through issue titles and comments became a supply-chain attack class, with the "Clinejection" incident on 17 February 2026 leading to an unauthorized npm publish ([Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-claude-code-github-action-prompt-injection/), primary). A Linux Foundation survey found maintainers judge 25% of incoming pull requests to be low-quality AI output, and 53% disagree that generative AI improved community trust ([Linux Foundation](https://www.linuxfoundation.org/press/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop), primary). That survey was presented at All Things Open in Raleigh, which gives the lecture a local hook.

### 4.3 Labor market

Stanford's August 2026 update of its payroll study (ADP data through June 2026) finds no economy-wide displacement. Employment of 22-to-25-year-olds in AI-exposed occupations is 19% below the less-exposed-peer benchmark, and the same measure was 15% at the July 2025 data vintage. The effect works through reduced hiring, and the authors call the result descriptive ([Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf), primary). The 15% and 19% are the same measure and can be joined, and `labor-series.csv` carries only those two. Earlier editions headlined regression estimates of 13% (July 2025 data) and 16% (September 2025 data), a different measure that must not be joined to them.

Indeed's US software-development postings index (seasonally adjusted, 1 February 2020 = 100) is in `labor-series.csv` as first-of-month readings from January 2022 ([Indeed Hiring Lab data file](https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv), primary):

| Date | Index | Note |
|---|---|---|
| 2022-02-28 | 233.82 | Series peak |
| 2025-05-17 | 61.10 | All-time low |
| 2026-07-01 | 73.46 | The 8 July article says 72.5 on data to June. The difference is revision of the seasonally adjusted series |
| 2026-10-01 | 78.25 | 78.65 on 10-15 |
| 2026-10-31 | 81.57 | The series rose about three points late in October |
| 2026-11-13 | 81.71 | Latest observation |

Senior roles account for 71% of the May 2025 to May 2026 increase and jobs with AI in the title for 37%. Software postings rose almost 15% from 24 February 2025 while all postings fell 7% ([Indeed Hiring Lab](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/), primary).

| Other labor facts | Source and quality |
|---|---|
| A Federal Reserve paper finds coder employment decelerated sharply after ChatGPT but kept growing | [Federal Reserve](https://www.federalreserve.gov/econres/feds/ai-and-coder-employment-compiling-the-evidence.htm), primary, abstract only |
| BLS cut its ten-year projection for software developers from plus 15.8% to plus 10%. Programmers are projected at minus 7% | [CNBC](https://www.cnbc.com/2026/10/11/ai-software-developer-jobs.html), secondary |
| Challenger counts 121,401 announced US job cuts attributed to AI from January to October 2026, about 20% of the total, but only 1,265 in October | [Challenger](https://www.challengergray.com/blog/october-layoffs-at-three-year-low-seasonal-hiring-plans-up-26/), primary. Employer-stated attribution is weak evidence |
| An audit of events tagged as AI-related found a minority came with a company claim that AI reduced staffing needs | [tech-insider](https://tech-insider.org/tech-layoffs-2026-ai-workforce-impact/), secondary |
| Microsoft offered voluntary exits to about 60,000 employees on 26 October 2026 | [CNBC](https://www.cnbc.com/2026/10/26/microsoft-msft-voluntary-buyouts.html), secondary |
| NACE employer projections put the average CS bachelor's starting salary for the class of 2026 at $81,535, the highest of all majors | [NACE](https://naceweb.org/job-market/compensation/class-of-2026-salary-projections-are-promising), primary |

### 4.4 Education

The CRA Taulbee Survey 2025 (55th survey, published June 2026) reports record CS bachelor's degree production alongside a cooling pipeline. Percentages are for the longitudinal cohort of units reporting 2020 to 2025 ([CRA](https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/), primary, read through a summarizing fetch tool because cra.org blocks scripted access. Quote whole percentages only).

| Metric | Value | Change | Period |
|---|---|---|---|
| New CS bachelor's majors | 33,490 | -13% | 2025-26 intake |
| Total CS bachelor's enrollment | 169,528 | -4% | 2025 |
| CS bachelor's degrees awarded | 41,858 | +13% | 2024-25 |
| Total CS master's enrollment | n/a | about -26% | 2025 |
| New CS master's admits | n/a | -10% | 2025-26 intake |
| CS master's degrees awarded | 23,180 | about 3% below the 2024 peak | 2024-25 |
| New CS master's students from outside North America | 63% | n/a | 2025-26 intake |
| Total CS doctoral enrollment | 16,989 | +5% year on year | 2025 |
| New CS doctoral enrollments | n/a | -15% | 2025-26 intake |

CRA ties graduate declines to visa barriers, so AI cannot be assigned the whole drop.

Responses are at course level so far. Brown ran an "Agentic Studio" project course in spring 2026 and its instructors concluded agentic coding could justify restructuring introductory CS ([Brown](https://www.brown.edu/news/2026-06-11/agentic-studio-ai-programming), primary). Colorado School of Mines has software engineering students write code by hand and then compare it with AI output ([Mines](https://www.mines.edu/news/all-news/2026/computer-science-curriculum-tackles-ais-growing-influence-head-on-.html), primary). George Washington is revising its curriculum in direct response to falling enrollment ([GW Hatchet](https://gwhatchet.com/2026/11/09/computer-science-department-revamps-curriculum-to-combat-falling-enrollment-in-the-age-of-ai/), secondary). No systematic count of departments changing degree requirements was found, and nothing specific to NCSU was researched.

### 4.5 Prediction scorecard

`prediction-scorecard.csv` holds nine dated predictions. Predictions about what happens inside frontier labs largely came true near schedule, and predictions about the whole economy missed their deadlines or remain open.

| Who and when | Prediction | Verdict | Source and quality |
|---|---|---|---|
| Dario Amodei, March 2025 | AI writes 90% of code in 3 to 6 months | Split. Missed industry-wide, roughly met inside Anthropic (more than 80% of merged production code by May 2026) | [The Next Web](https://thenextweb.com/news/anthropic-claude-recursive-self-improvement-code), secondary |
| Mark Zuckerberg, January 2025 | In 2025 AI will work as a mid-level engineer | Missed as stated | [HCAMag](https://www.hcamag.com/us/specialization/transformation/meta-to-cut-10-of-its-workforce-as-zuckerberg-redirects-billions-toward-ai/572933), secondary |
| Sundar Pichai, October 2024 to April 2026 | Statements of fact: 25%, then 50%, then 75% of new Google code | Reported | Section 4.1, primary. The CSV links [Semafor](https://www.semafor.com/article/04/24/2026/google-ceo-says-75-of-companys-new-code-is-ai-generated) |
| Dario Amodei, May 2025 | Half of entry-level white-collar jobs could go, with unemployment of 10% to 20% within 1 to 5 years | Open. Direction partly supported at entry level | [Stanford](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf), primary for the outcome |
| Mustafa Suleyman, February 2026 | Most computer-based white-collar tasks automated in 12 to 18 months | Open, not yet scoreable | [Fortune](https://fortune.com/2026/02/13/when-will-ai-kill-white-collar-office-jobs-18-months-microsoft-mustafa-suleyman/), secondary |
| AI 2027 authors, April 2025 | Superhuman coder around early 2027 | Open. On 10 November 2026 all authors forecast a superhuman AI researcher as likely during 2027 | [AI Futures](https://blog.aifutures.org/p/q35-timelines-update-looks-like-the), primary |
| Gary Marcus, December 2025 | No AGI in 2026, agents stay unreliable | Holding | [Marcus](https://garymarcus.substack.com/p/six-or-seven-predictions-for-ai-2026), primary |
| GitHub, October 2026 | Most code pushed to GitHub could be agent-written within two years | Open | [CNBC](https://www.cnbc.com/2026/10/11/ai-software-developer-jobs.html), secondary |
| US Bureau of Labor Statistics, August 2026 | Software developer jobs plus 10% over 2025 to 2035 | Open | [CNBC](https://www.cnbc.com/2026/10/11/ai-software-developer-jobs.html), secondary |

## 5. What the evidence supports

The lecture's title claim holds, but the evidence for it has moved off the charts the app drew before November 2026. Score progressions on fixed benchmarks and the METR horizon curve were the 2025 way to show pace. By late 2026 the pace shows up more reliably in how fast the instruments expire (average life falling from about 46 months to 12), in a linked index such as ECI, and in platform and revenue data that no lab controls. The app now keeps the METR series as a closed historical exhibit ending at the 16-hour limit, draws benchmark lifespans with ECI and ARC-AGI lines in place of the five-column score chart, and adds the adoption and labor series beside them.

The second change is in what a number means. In 2026 one model's ARC-AGI-3 score moved by 36 points with the harness at the same effort level, one model's time horizon moved by more than 20 times with the cheating policy, and two labs' tables differed by 4 to 9 points on the same model. Students who will work with these tools need four questions for any score: who ran it, on which version, with what harness and effort setting, and does anyone independent agree. The real-world evidence points to the same skill from the other side, since the measured bottleneck in firms is now review and verification of agent output.

## 6. What was wrong in the pre-November 2026 data tables

This section is history. Every item here has been corrected in the CSVs.

### 6.1 Time horizons (`model-task-time-horizons.csv`)

Twelve of the 14 rows had a wrong value or date (all 14 are listed for reference). The old table mixed superseded METR vintages, used launch-post figures that predate the 3 March 2026 regularization correction, and held three values that match no METR figure.

| Row | Old entry | Corrected (TH 1.1 unless noted) |
|---|---|---|
| GPT-4 0314 | 5.4 min | 3.99 |
| GPT-4 Turbo 1106 | 8.5 min | 4.04. METR's name is "GPT-4 1106" |
| GPT-4o | 10 min | 6.99 (10.17 on TH 1.0) |
| o1-preview | 90 min, CI 75 to 110 | 20.33, CI 11.72 to 33.38 |
| Claude 3.5 Sonnet v2 | 56 min (Claude 3.7 Sonnet's old figure) | 20.52 |
| DeepSeek-V3 | 2024-12-20, 18 min | 2024-12-26, 19.82 on TH 1.0 only |
| o3 | 2025-04-04, 92 min | 2025-04-16, 119.73 |
| GPT-5 | 2025-05-22 (the Claude 4 date), 137 min | 2025-08-07, 203.01 |
| Claude Opus 4.1 | 114 min | 100.47 |
| Claude Sonnet 4.5 | 2025-11-01, 122 min, noted as TH 1.1 | 2025-09-29, 116.53 on TH 1.0 only |
| GPT-5.1-Codex-Max | 2025-11-01, 173 min | 2025-11-19, 223.71 |
| Claude Opus 4.5 | 289 min | 292.99 |
| GPT-5.2 | 2026-01-06, 394 min | 2025-12-11, 352.25 |
| Claude Opus 4.6 | 2026-02-06, 420 min ("7hr+") | 2026-02-05, 718.81 |

Fourteen TH 1.1 rows were added (GPT-2, GPT-3, GPT-3.5, Claude 3 Opus, GPT-4 Turbo, Claude 3.5 Sonnet, o1, Claude 3.7 Sonnet, Opus 4, Gemini 3 Pro, GPT-5.3-Codex, Gemini 3.1 Pro, GPT-5.4, Mythos Preview), plus four TH 1.0-only rows (DeepSeek-R1, Gemini 2.5 Pro Preview, Grok 4, Kimi K2 Thinking). The chart's doubling-time labels moved from "about 7 months, 131 days, 89 days" to the values in section 3.4.

### 6.2 Benchmark scores (`model-benchmark-scores.csv`)

| Cell | Old entry | Corrected |
|---|---|---|
| Claude Sonnet 4.6, GPQA | 74.1 | 89.9 (system card) |
| GPT-5.3-Codex, GPQA | 73.8. This equals Opus 4.6's revised CyberGym score (66.6 revised to 73.8 in [Anthropic's Opus 4.7 post](https://www.anthropic.com/news/claude-opus-4-7)), which suggests a column mix-up | 92.6 (OpenAI's GPT-5.4 launch table) |
| Notes citing a "17-pt GPQA gap" between Opus 4.6 and Sonnet 4.6 | Followed from the bad 74.1 | Deleted. The gap is 91.3 against 89.9 |
| GPT-5.3-Codex, date | 2026-01-14 | 2026-02-05 |
| GPT-5.3-Codex, MMLU 93.0, SWE-bench Verified 80.0, HumanEval 93.0, MATH 96.0 | No source | Blanked |
| Claude Opus 4.7, SWE-bench Verified | Blank, "not officially published" | 87.6 (system card) |
| MMLU column, late-2025 and 2026 rows | MMMLU values under an MMLU header. Opus 4.6 held 91.0 and Gemini 3.1 Pro 90.4 | `MMLU_Instrument` column added. Opus 4.6 91.1, Gemini 3.1 Pro 92.6 |
| Notes citing METR horizons | Opus 4.6 "~7hr+", GPT-5.2 "~6hr 34min", Opus 4.5 "~4hr 49min" | 11 h 59 m, 5 h 52 m, 4 h 53 m on TH 1.1 |
| HumanEval and MATH cells from Claude Sonnet 4.5 (September 2025) onward, and "proxy retained" values | No launch source | Blanked |
| Rows after GPT-5.5 | Absent | Opus 4.8, Fable 5, Mythos 5, Sonnet 5 and Opus 5 added as end markers |

### 6.3 Release timeline (`model-release-timeline.csv`)

| Row | Old entry | Corrected |
|---|---|---|
| GPT-5.3-Codex | 2026-01-14 (GPT-5.2-Codex's API date) | 2026-02-05. GPT-5.2-Codex added at 01-14 |
| Grok 4.20 | 2026-03-22 | 2026-03-10 |
| Claude 3.7 Sonnet | 2025-02-18 | 2025-02-24 |
| Gemini 3.1 Pro | Named as a GA model | Renamed "Gemini 3.1 Pro Preview", access Preview |
| Table end | Stopped at GPT-5.5 | About 60 rows added through 18 November 2026, with `Access`, `Tier` and `Source_Quality` columns |

## 7. Still unverified

Every claim below is secondary-only, single-source or unverifiable after the verification pass. Rows marked "in CSV" feed a chart.

| Claim | Status | In CSV | What would settle it |
|---|---|---|---|
| GPT-5.6 gated preview announced 2026-06-26 at US government request | Secondary. No such entry in the API changelog | Access label only | OpenAI's announcement post (the Internet Archive rate-limited the fetch) |
| Gemini 4 Argon limited preview on 2026-09-30 | Secondary. No September changelog entry | No | A dated Google post |
| GPT-6.1 Astra cancelled over deception findings | Secondary. Changelog gap is indirect support | No | An OpenAI statement |
| Amazon researchers reported a bypass of Fable 5's cyber safeguards before the June export controls | Secondary, not checked | No | The Amazon report or Anthropic's statement |
| DeepSeek V4 announcement day (22 to 24 April) | Rests on repository creation dates and Epoch | Yes (04-22) | api-docs.deepseek.com changelog, which refused connections |
| DeepSeek V4 Pro 96.4% SWE-bench Verified | Unverified, one blog. Do not use | No | Any primary source |
| Kimi K3 announcement date 2026-07-16 | Secondary (Epoch and ARC Prize agree) | Yes | Moonshot's dated announcement |
| Kimi K3.1 Pro announcement date 2026-10-23 and exact day weights became public (2 to 5 November) | Secondary for the date | Yes | Moonshot's announcement. Repository commit history |
| Dates for Kimi K2.5, GLM-5.1, Qwen3.6, Kimi K2.6, Qwen3.8-Max, and the 2025 open-weight rows | Secondary (Epoch table, vendor blog, trade press, llm-releases.com) | Yes | Each lab's release list or weights repository |
| Qwen3.8-Max weights | Promised, unconfirmed | Yes ("Weights promised") | The Qwen organization on Hugging Face |
| MiniMax M2.5 and M3 dates, weights and the 80.2% claim | Secondary, vendor claim | No | MiniMax release notes and repository |
| Muse Spark (04-08), Muse Glimmer (08-10), Muse Ember (11-09) dates | Secondary | Yes | Meta Newsroom or research blog posts |
| MAI Code 2, Code 2 Flash, Cyber 2 Flash on 2026-11-17 | Secondary | Yes | A Microsoft page |
| Grok 5 has not shipped | Secondary | No | xAI release notes |
| Anthropic launch-event counts, 6 in 2025 and 13 in 2026 | Researchers' count from primary release notes | No | Recount from the release notes |
| Distillation: February disclosure details and the 22 July White House accusation | Secondary | No | The Anthropic disclosure and a White House document |
| Artificial Analysis v5 open-closed gaps (12 and 26 points). Launch-day values of 58 for Opus 5.5 and 32 for DeepSeek V4.1 Flash. Fable 5 at 60 on v4.1 and a top score of 53 on v4.3. AA Index 46 for Kimi K3.1 Pro and 32 for GLM-5.3 | Secondary ([officechai](https://officechai.com/ai/61673/), Implicator, trade press) | No | Artificial Analysis changelog pages for each version |
| Chinese API prices at one-fifth to one-sixth of US prices | Secondary | No | Vendor price pages on one date |
| ECI May 2026 vintage (GPT-5.5 Pro 159.35) | Unverifiable. The vintage could not be retrieved | Open-weight rows use the May table | An archived copy of Epoch's May file |
| MMLU plateau date (March 2024) and HumanEval ceiling date (June 2024) | Unverified, researcher judgment | Yes | An owner or evaluator statement. None exists so far |
| MATH ceiling date (September 2024) | Weak. Epoch's runs suggest December 2024 to April 2025 | Yes | Decide a rule (first score above 95% on Epoch's runs gives 2025-01-31) |
| ARC-AGI-1 end date (o3-preview 87.5%, December 2024) | Secondary. Not re-read on arcprize.org | Yes | ARC Prize's December 2024 post |
| ARC-AGI-2 "60% average human" baseline | Not located in ARC's data files | Wording in the lifespans CSV | ARC Prize's ARC-AGI-2 launch post |
| ARC-AGI-3 launch date, 25 March 2026, and finer launch scores (0.37, 0.26, 0.25, 0) | Not re-checked | Yes (date) | ARC Prize's launch post |
| Claude Opus 4.7 CyberGym 73.1 | Not located in the system card text. The result is shown as a figure | No | Read the figure in the card |
| Claude Sonnet 5.5 at 70.6% on Terminal-Bench 4.0 | Aggregator only ([Morph](https://www.morphllm.com/claude-benchmarks)). Its card was not downloaded | Yes ("66-71%") | Sonnet 5.5 system card |
| GPT-5.3-Codex SWE-bench Pro 56.8% | In the score CSV's notes. Not covered by verification | Notes only | Appendix of the archived GPT-5.3-Codex post |
| Score-table cells flagged `reported`: SWE-bench Verified for GPT-5.2 (80.0), Opus 4.6 (80.8), Gemini 3.1 Pro (80.6). Sonnet 4.6 MMMLU 89.3 and SWE-bench Verified 79.6 | Vendor figures read through secondary sources | Yes | System cards, model cards and archived launch posts |
| Pre-2026 score-table rows (MMLU, HumanEval, MATH for 2023 to 2025 models, both Grok rows) | Legacy values, never re-checked. HumanEval and MATH are blank from September 2025 onward | Yes | Each model's launch table |
| Terminal-Bench-Science pairs (Fable 5.1 52.6 against 43.3, GPT-6 Astra 68.1 against 63.3, GPT-6.2 Astra 77.0 from a chart against Vals 71.4) | From the working notes, not re-verified | Yes | Anthropic and Google launch tables, the Vals board |
| OSWorld-Verified public board | Not read directly. Epoch's copy tops out at Sonnet 4.6, 72.1%. An aggregator figure of 90.19% was found nowhere primary | No | os-world.github.io |
| OSWorld 2.0 and 2.1 details beyond release date and scores | Single secondary source | No | osworld-v2.xlang.ai |
| FrontierSWE v2 at about 70% for Fable 5.2 | Secondary ([LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch)) | Yes | Fable 5.2 system card or Proximal's board |
| Opus 4.6 first announced at about 14.5 hours | Secondary ([officechai](https://officechai.com/ai/exponential-progress-claude-opus-4-6-has-50-time-horizon-of-14-5-hours-on-metr-time-horizons-benchmark)). Not on any METR page read | No | An archived copy of METR's February page |
| Viral "240 hour" horizon for an Anthropic internal model | Unverified. Reportedly a conversion from another index ([FourWeekMBA](https://fourweekmba.com/ai-metr-tested-ai-at-17-hours-viral-240-hour-mark-is-estimated/)) | No | Nothing. It is not a METR measurement |
| UK AISI cheating rates of 7.8% to 14.1% | Secondary | No | The AISI report |
| Berkeley reward-hacking audit (10 of 10 benchmarks) | Read as a summary | No | Read arXiv 2605.12673 in full |
| Kimi K3 sandbox escape in August | Secondary | No | The evaluator's report |
| AI Futures medians for August 2026, and the January 2026 "pushed timelines out" wording in the scorecard | No August post was read | Scorecard text | The AI Futures blog archive |
| JetBrains: about 90% of professional developers use coding agents weekly. Claude Code at about 39% against 18% in January | Unverifiable. Press-reported ([GIGAZINE](https://gigazine.net/gsc_news/en/20260824-ai-coding-agent-adoption-trends/)) and absent from the key-findings post | No | The full JetBrains report or a separate JetBrains study |
| Anthropic at more than 80% of merged production code | Secondary | Yes | An Anthropic statement or filing |
| Microsoft "20 to 30%" (April 2025) | Secondary | Yes | A transcript of Nadella's remarks |
| Anthropic S-1 revenue of $33.2B | Secondary | No | The S-1 on SEC EDGAR |
| OpenAI's 5 million weekly Codex users | Secondary report of a vendor figure | No | An OpenAI post |
| Harvard paper, earlier drafts (718 firms, +49%) | Not retrieved | No | Not needed. Cite the 14 November version |
| Microsoft CLI-agent study, 24% more merged pull requests | Abstract only | Yes | Read arXiv 2607.01418 in full |
| New Relic, McKinsey and CMU productivity figures | Unverifiable. Search summaries only | No | Open each report |
| Federal Reserve coder-employment paper, and press claims that it shows growth halved or 500,000 jobs unfilled | Abstract only. Press claims unconfirmed | No | Read the paper |
| BLS projection cut from 15.8% to 10% | Secondary | Scorecard and app text | The BLS Employment Projections release |
| Audit of AI-tagged layoff events | Secondary | No | The audit itself |
| NY Fed unemployment by major (CS 7.0%, computer engineering 7.8%) | Unverifiable. 2024 data, reached through [opportunitydata.org](https://opportunitydata.org/recent-grad-job-market.html). The [NY Fed page](https://www.newyorkfed.org/research/college-labor-market) carries a notice dated 31 October 2025 that the feature has not been updated on schedule | No | The NY Fed data file, with the data year stated |
| CRA Taulbee figures | Primary page read through a summarizing tool | App text | Open the page by hand before a slide cites it |
| Preliminary fall 2026 Clearinghouse CS enrollment of about -12% | Secondary | No | The Clearinghouse release |
| Exact wording and dates of the Amodei and Zuckerberg predictions | Secondary scorecards | Yes | The original interviews |
| State of AI Report 2026 and International AI Safety Report 2026 | Not read. Do not quote | No | Read them |
| Nvidia H200 exports to China halted, 18 November 2026 | Secondary, one trade-press article ([GSMArena](https://m.gsmarena.com/nvidia_halts_its_h200_chip_sales_to_china_-amp-75528.php)). Reports describe a production halt by Nvidia, not a government export pause | No | An Nvidia or US Commerce statement |
| Vendor SWE-bench Pro figures for Opus 4.5, Sonnet 4.5, Haiku 4.5 | None found | No | Their system cards |
| LoopsBench scores above 25.0% | Unverifiable. No leaderboard found | Yes | A leaderboard or follow-up paper |
| Harness and effort for Fable 5.2 on SWE Atlas, ProgramBench (Vals) and the Remote Labor Index | Not published | Yes | The owners' run cards |
| Whether the ExploitGym runs covered every instance | Unverifiable | No (counts quoted in text only) | The ExploitGym paper's appendix |
| OpenAI's rule for a "zero-intervention success" | In a methods panel the archive snapshot did not capture | Yes (metric cards) | The live post |

Not researched at all: xAI and Meta vendor benchmark tables, an independent GPQA board, 2025 release counts for OpenAI, Google and xAI, OpenRouter usage share for Chinese models, and BLS monthly employment counts for developers.

## 8. How to refresh this next time

### 8.1 Before starting

- The app caches CSV loads with `st.cache_data`. Restart `streamlit run app.py` after editing a CSV, or the charts will show the old data.
- Some figures are hard-coded in `app.py` and do not come from a CSV: the three GPT-5.6 Sol readings and the doubling-time text on the Time Horizons tab, and the four metric cards on the Jobs & Education tab (CS salary, new majors, BLS projection, senior share). Update them by hand.
- The Benchmark Lifespans cohort averages and the ECI trend lines are computed in `app.py` from the CSVs, so they change when rows change. Check the README's "46, 22, 12 months" sentence afterwards.
- Raw notes from November 2026 are in `research_notes/LLM progress update late 2026/`. They contain superseded figures. This report is the authority.

### 8.2 Conventions in force

| Topic | Convention |
|---|---|
| Release date | First public availability from the lab's changelog. Record gated or preview status in `Access`. Put the API date in notes when it differs. Never use ARC Prize's `modelReleaseDate` or a tracker's date as a launch date |
| Date resolution | Use the day from the lab's own notes. xAI's notes do give days |
| Open weights | Label by what the repository shows: public or gated, and the licence. "Weights promised" until a public commit exists |
| METR suite | TH 1.1 is the main series. TH 1.0-only models stay in a separate `Suite` value. Copy values from the YAML, never from a blog post, press or Wikipedia |
| Vendor against independent | A lab's figure for its own model is vendor even when read on a primary page. A benchmark owner's run is independent. State harness and effort level for ARC-AGI-3 and Artificial Analysis scores |
| Score-table confidence | `confirmed` means read on the owner's page, `reported` means read through a secondary source, `unverified` is drawn hollow |
| Benchmark end dates | Use a dated statement by the owner or a major evaluator when one exists (retirement, "saturated", a replacement version, a "Flawed" rating). Otherwise use the first score past a stated threshold and say it is a judgment. Put the rule in `How_Ended` |
| Epoch vintages | Take the whole ECI frontier from one download of `eci_scores.csv` and write the download date in `Vintage`. Never mix it with a Data Insight table |
| Artificial Analysis vintages | Values are comparable only within one index version. Record the version and read date. Never draw a line across versions |
| Stanford gap | Join only the descriptive gap (15%, 19%). Never join the 13% and 16% regression estimates to it |
| Company code-share claims | Plot as executive claims, one series per company, dated by when the statement was made and what period it described |
| Harvard paper | Cite the version date |

### 8.3 Source for each data table

| CSV | Tab | Pull from | Notes |
|---|---|---|---|
| `model-release-timeline.csv` | Release Cadence | Anthropic: https://platform.claude.com/docs/en/release-notes/overview . OpenAI: https://developers.openai.com/api/docs/changelog . Google: https://ai.google.dev/gemini-api/docs/changelog and https://ai.google.dev/gemini-api/docs/models . xAI: https://docs.x.ai/docs/release-notes . Z.ai: https://docs.z.ai/release-notes/new-released . Alibaba: https://www.alibabacloud.com/help/en/model-studio/newly-released-models . Mistral: https://docs.mistral.ai/getting-started/changelog . Meta: https://about.fb.com/news/ and https://research.meta.ai/blog/ . Microsoft: https://microsoft.ai/news/ . Weights: https://huggingface.co/deepseek-ai , https://huggingface.co/api/models?author=deepseek-ai&search=V4 (change author and search for other labs), https://huggingface.co/moonshotai , https://huggingface.co/zai-org | Epoch's `model_metadata.csv` inside https://epoch.ai/data/benchmark_data.zip is a good cross-check for dates and weight status. DeepSeek's own changelog refused connections |
| `benchmark-lifespans.csv` | Benchmark Lifespans | Introductions: arXiv first-submission dates and `benchmark_metadata.csv` in https://epoch.ai/data/benchmark_data.zip . Endings: https://www.tbench.ai/news , https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2 and later changelogs, https://epoch.ai/benchmarks/swe-bench-pro/review and sibling review pages, Anthropic system cards, archived OpenAI posts | Per-benchmark score histories for threshold rules are in the Epoch zip (`mmlu_external.csv`, `math_level_5.csv`, `frontiermath_tier_4_v2.csv`, `osworld_2_external.csv`)  The `Epoch_Review` column holds Epoch's verdict and date from https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks ; refresh every row from that registry |
| `eci-scores.csv` | Progress Measures | Download https://epoch.ai/data/eci_scores.csv (also inside https://epoch.ai/data/benchmark_data.zip), then run `python scripts/build_eci_scores.py <file> <download date>`. Slopes: https://epoch.ai/data-insights/eci-frontier-trend and https://epoch.ai/publications/eci-bayesian-methodology . Open-weight gap: https://epoch.ai/data-insights/open-closed-eci-gap | The script rewrites the whole table from the one file, so vintages cannot mix. To add a lab, add it to `LABS` in the script and to `LAB_ORDER` and `ORG_COLORS` in `app.py` |
| `arc-agi-scores.csv` | Progress Measures | https://arcprize.org/media/data/evaluations.json and https://arcprize.org/media/data/models.json | The leaderboard page renders client-side, so fetch the JSON. Use the Verified board only (semi-private sets). Keep the best configuration per model, and Standard and Provider Adapter in separate columns |
| `model-benchmark-scores.csv` | Progress Measures (retired series) | Anthropic system cards index: https://www.anthropic.com/system-cards (download the PDFs and search the text). OpenAI launch posts through the Internet Archive. Google model cards: https://deepmind.google/models/model-cards/ . Independent SWE-bench Verified: `swe_bench_verified.csv` in the Epoch zip | The legacy columns are closed. Add a row only if a new launch reports one of them. Anthropic launch-post tables are images, so use the system card |
| `vendor-vs-independent.csv` | Who Measured It? | Scale: https://labs.scale.com/leaderboard/swe_bench_pro_public . ARC Prize JSON. Lab system cards and model cards for each side of a lab-against-lab pair. Vals for Terminal-Bench-Science | Add a pair only when both values are for the same model and benchmark version. Note Scale's capped-cost rows |
| `model-task-time-horizons.csv` | Task Time Horizons | https://metr.org/assets/benchmark_results_1_1.yaml and https://metr.org/assets/benchmark_results_1_0.yaml . Update log: https://metr.org/time-horizons/ | Frozen since 8 September 2026. Check the update log first. If nothing changed, do not touch the file |
| `after-metr-instruments.csv` | Task Time Horizons, "After METR" panel | https://metr.org/blog/ and https://metr.org/notes/ for new METR instruments. https://epoch.ai/data/eci_scores.csv . https://epoch.ai/benchmarks/mirrorcode . Scale's board at https://labs.scale.com/leaderboard for the Remote Labor Index. https://www.swe-marathon.org/ | The FrontierSWE row still rests on a secondary source |
| `successor-benchmarks.csv` | Progress Measures, "After SWE-bench" view | https://swe-rebench.com/ , https://swe-bench-live.github.io/ , https://www.vals.ai/benchmarks/programbench and https://programbench.com/ , https://github.com/scaleapi/swe-atlas and https://labs.scale.com/leaderboard , https://www.swe-marathon.org/ , https://arxiv.org/abs/2608.00267 (LoopsBench), https://arxiv.org/abs/2611.14364 (ARE-bench), https://epoch.ai/benchmarks/mirrorcode | One bar per benchmark: the best score on the owner's page, with who ran it in `Executed_by` and the main qualification in `Caveat`. Do not compare bars as model rankings. Check whether SWE-rebench has added a window and whether LoopsBench has a leaderboard |
| `expenditure-horizon.csv` | Task Time Horizons, "After METR" panel | https://metr.org/blog/2026-07-21-expenditure-horizon/ and https://metr.org/notes/2026-07-24-metrics-of-model-ability/ | One task, two models. Add rows only if METR publishes more models or tasks |
| `adoption-series.csv` | Benchmarks vs Reality | Octoverse: https://github.blog/news-insights/octoverse/ (annual, late October). Google: earnings remarks and keynote posts on https://blog.google/ . Stack Overflow survey: https://stackoverflow.blog/ (annual, October) | GitHub publishes only selected months. Do not interpolate into new rows |
| `productivity-studies.csv` | Benchmarks vs Reality | https://fion.ac/jellyfish.pdf (check the version date on page 1). https://arxiv.org/abs/2607.01418 . https://www.faros.ai/research/ai-acceleration-whiplash | Update the firm count in the `Study` label when the paper changes |
| `metr-uplift-studies.csv` | Benchmarks vs Reality | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ and https://metr.org/blog/2026-02-24-uplift-update/ | METR abandoned this design. Look for a new one |
| `labor-series.csv` | Jobs & Education | Indeed: https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv (software development sector, seasonally adjusted, first of each month plus the latest date). Stanford: https://digitaleconomy.stanford.edu/ for the next "Canaries" edition | Indeed revises the seasonally adjusted series, so replace the whole column each time |
| `prediction-scorecard.csv` | Prediction Scorecard | The sources in each row | Re-score verdicts against deadlines. Suleyman's window opens in February 2027 |
| `publications-agentic.csv` | Not charted | The earlier reading list | No refresh needed |

Jobs & Education metric cards (hard-coded): NACE at https://naceweb.org/ , CRA Taulbee at https://cra.org/crn/ , BLS Employment Projections, and the Indeed Hiring Lab article series at https://hiringlab.indeed.com/ .

### 8.4 Access problems and workarounds

| Problem | Workaround |
|---|---|
| openai.com returns 403 to direct fetches | Read Internet Archive snapshots, for example `https://web.archive.org/web/2026/https://openai.com/index/<slug>/`. Raw `id_` captures of the original pages worked. The Archive rate-limits after several requests, so space them out |
| ARC Prize and Epoch pages render tables client-side | Download the underlying files: `evaluations.json`, `models.json`, `eci_scores.csv`, `benchmark_data.zip` |
| Anthropic launch-post tables are images | Download the system card PDF from https://www.anthropic.com/system-cards and search it as text. Some results exist only as figures |
| cra.org returns 403 to scripts | Open the page in a browser by hand. A summarizing fetch tool worked but is one step less direct |
| api-docs.deepseek.com refuses connections | Use Hugging Face repository creation dates and Epoch's `model_metadata.csv` |
| NY Fed by-major table is rendered by a script and the data file could not be retrieved | Open in a browser, and check the page's update notice |
| JetBrains full report | The key-findings post is readable. The full report was not reached |

### 8.5 Known gaps between the CSVs and verified values

None as of 19 November 2026. The data tables match the verified values, and `eci-scores.csv` is built from a single Epoch download.

### 8.6 Aggregators and secondary sites that gave wrong numbers

Do not use these as sources for values. They are fine as pointers to a primary page.

| Site | What went wrong in this round |
|---|---|
| Morph (morphllm.com/claude-benchmarks) | Named Opus 4.8 as the last GPQA reporter and Fable 5 with Sonnet 5 as the last SWE-bench Verified reporters. Both were incomplete |
| Benchmark aggregators in general (LLM Stats, Vellum, datalearner and similar) | Attributed Mythos 5 figures to Fable 5 (SWE-bench Pro 80.3, Terminal-Bench 2.1 88.0), listed unrelated cyber-evaluation figures (83.1, 84.6) as Terminal-Bench scores, gave a range for GPT-5.3-Codex GPQA, and carried an OSWorld-Verified 90.19% that exists nowhere primary |
| Wikipedia's METR table | Mixes values from before and after the March 2026 correction |
| Model release trackers and ARC Prize `modelReleaseDate` | Dates off by one to nine days against lab changelogs |
| SSGA market note | Read DeepSeek's July and August refresh builds as the V4 launch |
| ComplexDiscovery summary of the Harvard paper | Carried an earlier draft's figures (718 firms, +49%) |
| The secondary site used for CRA figures | Gave decimals (12.9%, 4.1%) that are not in CRA's article |
| Secondary coverage of Epoch's SWE-bench Pro review | Attributed an "87% via git history" figure to Datacurve that is not on Epoch's page |
| opportunitydata.org | NY Fed by-major figures without the data year |
| The lecture's own earlier tables | See section 6 |

### 8.7 Dated events to look for

- ARC Prize 2026 competition results, due 4 December 2026 ([ARC Prize](https://arcprize.org/leaderboard)). This affects the community and competition story, not the Verified board rows.
- New Epoch benchmark-review verdicts, and any response from ARC Prize to the ARC-AGI-3 "Flawed" rating ([Epoch registry](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks)).
- Results from OpenAI's embedded assessments by Apollo, METR, Transluce and Goodfire, announced 16 November 2026. No publication dates were given.
- A SWE-rebench window after July 2026, a LoopsBench leaderboard, and ProgramBench or SWE-Marathon results for newer models.
- Any METR successor to time horizons: a new suite, more expenditure-horizon tasks or models, or a change to the "no longer actively updated" notice ([METR time horizons](https://metr.org/time-horizons/)).
- New Terminal-Bench versions after 4.1 ([tbench.ai news](https://www.tbench.ai/news)) and new OSWorld versions after 2.1.
- Scale running any Anthropic, OpenAI or Google model released after April 2026 on SWE-bench Pro, which would give the two series their first overlap ([Scale](https://labs.scale.com/leaderboard/swe_bench_pro_public)).
- A new Artificial Analysis index version, and a new Epoch method or vintage.
- Whether any lab still reports GPQA Diamond, SWE-bench Verified or SWE-bench Pro in a 2027 launch.
- Next editions: Stanford AI Index (spring), Stanford "Canaries" update, GitHub Octoverse (late October), CRA Taulbee (June), Stack Overflow Developer Survey (October), JetBrains developer survey, BLS Employment Projections (late summer), NACE salary projections.
- New versions of the Harvard paper.
- Releases: Grok 5, GPT-6.2 lower tiers, Gemini 4 GA changes, Qwen4 weights, MAI Code 2 on a Microsoft page, and any new gated tier.
- Suleyman's 12 to 18 month window (February to August 2027) and the AI 2027 authors' 2027 forecast, both scoreable during 2027.
