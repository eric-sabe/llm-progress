# Chinese and Open-Weight Frontier Model Releases, January 2025 to 19 November 2026

Research date: 19 November 2026. Reading notes for the report writer:

- "Vendor" in the tables means the score comes from the lab's own launch material. "Independent" means a third party ran it (Epoch, Artificial Analysis, Vals).
- Most 2026 dates below come from secondary coverage (trade press, aggregator blogs) found by search, not from lab pages or Hugging Face cards, which I did not open directly. Where two sources disagree on a date I give both.
- Several closed US models named as comparison points (Claude Opus 4.8, Claude Fable 5, Claude Opus 5.5, GPT-5.6 Luna/Terra/Sol, GPT-6 Astra, GPT-6.1 Sol) appear here only as the sources reported them; their own release dates belong to another researcher's scope and were not checked.
- Benchmark versions drift through the year (Terminal-Bench 2.0, 2.1, 3.0, 4.0; SWE-bench Verified gives way to SWE-bench Pro, DeepSWE, SWE Marathon, FrontierSWE). Scores on different versions are not comparable.

## Which Chinese and open-weight models were significant for coding/agentic work in 2025–2026, and when exactly did each ship?

### Takeaway
2026 saw a roughly monthly cadence of Chinese open-weight coding flagships: Kimi K2.5 (Jan), GLM-5 and MiniMax M2.5 (Feb), GLM-5.1, Qwen3.6, Kimi K2.6 and DeepSeek V4 (Apr), MiniMax M3 and GLM-5.2 (Jun), Kimi K3 (Jul), Qwen3.8-Max and GLM-5.3 (Aug), DeepSeek V4.1 Flash (Sep), Kimi K3.1 Pro (Oct). A recurring pattern from mid-2026 is "announce now, weights later" (K3, GLM-5.3, K3.1 Pro, Qwen3.8-Max), and almost every headline coding score is vendor-reported.

### Cited Findings

#### 2026 Chinese labs (chronological)

| Date | Lab | Model | Weights | Type | Headline coding/agentic claims | Price (USD per 1M in/out) | Source |
|---|---|---|---|---|---|---|---|
| 2026-01-27 | Moonshot | Kimi K2.5 | Open | General/agentic LLM | Independent: ECI 148.22 | n/f | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap) |
| 2026-02 (day n/f) | ByteDance | Doubao Seed 2.0, incl. Seed 2.0 Code | Closed | General + coding variant | n/f | n/f | [Second Talent Doubao roundup](https://www.secondtalent.com/resources/every-doubao-ai-model-explained-compared/) (secondary; attribution from search summary) |
| 2026-02-11 | Z.ai (Zhipu) | GLM-5 | Open | General/coding LLM | Independent: ECI 146.62 | n/f | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap) |
| 2026-02-12 | MiniMax | M2.5 | Open (modified MIT) | Coding/agent LLM | Vendor: 80.2% SWE-bench Verified. Vals.ai lists it first among open-weight models on a SWE-bench Verified split | n/f | [NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/minimax-m2-5-frontier-ai-performance-at-a-fraction-of-the-cost/); [Vals.ai](https://www.vals.ai/models/minimax_MiniMax-M2.5) |
| 2026-03 (day n/f) | MiniMax | M2.7 | Disputed: one outlet says closed, others open | Coding/agent LLM | Vendor: SWE-Pro 56.22%, Terminal-Bench 2 57.0% | n/f | closed per [CIW](https://www.ciw.news/p/minimax-m2-7); listed as open-weights checkpoint by [SemiAnalysis InferenceX](https://inferencex.semianalysis.com/model/minimax-m27) |
| 2026-04-01/02 | Alibaba | Qwen3.6-Plus | Closed (API) | General/agentic | Independent: ECI 149.08 | n/f | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap) |
| 2026-04-07 | Z.ai | GLM-5.1 | Open (per GLM-5.2 coverage it is the predecessor) | Coding LLM | Independent: ECI 149.94. Vendor: SWE-bench Pro 58.4 | n/f | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap); [Morph](https://www.morphllm.com/glm-5-2) |
| 2026-04-16 | Alibaba | Qwen3.6-35B-A3B | Open (Apache 2.0) | Small agentic coder | Vendor: 73.4 SWE-bench Verified | free weights | [Alibaba Cloud blog](https://www.alibabacloud.com/blog/qwen3-6-35b-a3b-thinking-open-weights-uncompromised-agentic-coding_603043); [NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/qwen3-6-35b-a3b-alibaba-open-sources-a-frontier-class-agentic-coder/) |
| 2026-04-20 | Moonshot | Kimi K2.6 | Open | General/agentic | Independent: ECI 151.60, the top open-weight score in Epoch's May table | n/f | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap) |
| 2026-04-20 | Alibaba | Qwen3.6-Max (Preview) | Not listed (Max line historically closed) | Flagship | Independent: ECI 150.16 | n/f | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap) |
| 2026-04-22 | Alibaba | Qwen3.6-27B (dense) | Open | Local coding model | Vendor: beats Qwen3.5-397B-A17B on coding | free weights | [Alibaba Cloud blog](https://www.alibabacloud.com/blog/qwen-3-6-27b-flagship-level-coding-in-a-27b-dense-model_603063) |
| 2026-04-23 (US evening; coverage dated 04-24) | DeepSeek | V4-Pro, V4-Pro-Max, V4-Flash (plus Base variants) | Open (MIT) | 1.6T-param MoE, 49B active, 1M context | Vendor (V4-Pro-Max): SWE-bench Pro 55.4% vs GPT-5.5 58.6% and Opus 4.7 64.3%; Terminal-Bench 2.0 67.9% vs 82.7% / 69.4%. Secondary sources add 80.6% SWE-bench Verified (Pro) and 79.0% (Flash), also vendor | Pro $1.74 / $3.48; Flash $0.14 / $0.28 | [VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5); [devtake](https://devtake.pages.dev/article/deepseek-v4-release) |
| 2026-05-09 | Baidu | ERNIE 5.1 | Closed (not stated open) | General | n/f | n/f | [Second Talent ERNIE roundup](https://www.secondtalent.com/resources/every-ernie-ai-model-explained-compared/) (secondary) |
| 2026-05-20 | Alibaba | Qwen3.7-Max | Closed at announcement (previews only, no weights) | Flagship | n/f | n/f | [Codersera](https://codersera.com/blog/qwen-3-7-vs-qwen-3-6-2026/) |
| 2026-06-01 | MiniMax | M3 | Open claimed; weights timing disputed (one blog: on HF by 06-07; another on 06-11 still expecting them) | Reasoning + agent LLM | Vendor: SWE-bench Pro 59.0%, Terminal-Bench 2.1 66.0% | n/f | [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/3934/minimax-m3-chinese-open-weights-coding-model); [Codersera](https://codersera.com/blog/minimax-m3-release-date-whats-new-2026/) |
| 2026-06-13 (trade press) or 06-16 (SSGA) | Z.ai | GLM-5.2 | Open (MIT), 753B params, 1M context | Long-horizon coder | Vendor: SWE-bench Pro 62.1 vs GPT-5.5 58.6; Terminal-Bench 2.1 81.0 vs Opus 4.8 85.0 (Z.ai harness; Anthropic's own figure reported as 82.7) and GPT-5.5 84.0 | $1.40 / $4.40 | [VentureBeat](https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost); [claudefa.st](https://claudefa.st/blog/models/glm-5-2); date 06-16 per [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack) |
| 2026-06-23 | ByteDance | Seed-Evolving (rolling model, weekly updates under one ID); Seed 2.1 Pro/Turbo also listed, date n/f | Closed | General | n/f | n/f | [Second Talent Doubao roundup](https://www.secondtalent.com/resources/every-doubao-ai-model-explained-compared/) (secondary) |
| 2026-07-16 (SSGA) / 07-17 (ForkLog article date) | Moonshot | Kimi K3 | Open-weight; weights and tech report scheduled for 07-27 | 2.8T-param MoE (16 of 896 experts active), 1M context | Vendor, with mixed harnesses: Terminal-Bench 2.1 88.3 (Fable 5 84.6, GPT-5.6 Sol 88.8); SWE Marathon 42 (35 / 39); FrontierSWE 81.2 (Fable 5 86.6); BrowseComp 91.2. No SWE-bench Verified or Pro figure at launch | n/f | [ForkLog](https://forklog.com/en/news/moonshot-ai-unveils-kimi-k3-first-open-3t-class-ai-model); [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack) |
| 2026-07-31 | DeepSeek | "V4-Flash" (as dated by SSGA; conflicts with the April launch, see Gaps) | Open, weights at launch | Cheap fast tier | "About US$0.03 for a full benchmark run" | see Sept row | [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack) |
| 2026-08-03 | Alibaba | Qwen3.8-Max (plus open Qwen3.8-27B) | Max weights promised; status unconfirmed | 2.4T-param MoE, ~95B active, 1M context | Vendor: Terminal-Bench 2.1 86.6 (GPT-5.6 Sol 88.8; Opus 4.8 and Fable 5 84.6); SWE-bench Pro 67.7 vs Fable 5 80.0, on an Alibaba-revised task set | $2.00 / $6.00 (single source) | [DataNorth](https://datanorth.ai/news/alibaba-releases-qwen3-8-max); [Trending Topics](https://www.trendingtopics.eu/qwen3-8-max-is-the-next-chinese-open-weights-assault-on-the-ai-frontier/); price per [aicybr](https://aicybr.com/blog/qwen-3-8-max-complete-guide) |
| 2026-08-13 | DeepSeek | V4 Pro (GA build "0813", as dated by SSGA and one blog) | Open per blog | Flagship | SSGA: "GLM-5.2-level and far cheaper". One blog's 96.4% SWE-bench Verified claim is an unsupported outlier and should not be used | price raised 08-16, see pricing section | [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack); outlier at [Context Studios](https://www.contextstudios.ai/blog/deepseek-v4-pro-0813-ga-open-weight-frontier-beats-opus-4-8-on-terminal) |
| 2026-08-14 (weights ~08-25 to 08-28) | Z.ai | GLM-5.3 (post-training-only upgrade of GLM-5.2) | Open, weights delayed about two weeks for safety work | Coding + cyber | Vendor: Terminal-Bench 2.1 88.2; Terminal-Bench 3.0 28.3 (Fable 5 33.7, GPT-5.6 Sol 34.6); DeepSWE v1.1 66.9 (Kimi K3 67.5, Fable 5 69.7); CyberGym 84.5%. Independent: AA Index v4.3 score 45, top open-weights model as of 2026-09-07 | $1.40 / $4.40 | [Decrypt](https://decrypt.co/375684/china-z-ai-glm-5-3-top-open-weight-coding-model?amp=1); [DataNorth](https://datanorth.ai/news/z-ai-releases-glm-5-3); [Morph](https://www.morphllm.com/glm-5-3) |
| 2026-09-10 | DeepSeek | V4.1 Flash (552B params) | Open (MIT) | Fast tier with native vision; replaced V4 Flash | Vendor: Terminal-Bench 2.1 90.6; DeepSWE v1.1 74.2; ahead of V4 Pro on agentic tests, behind on hard reasoning | $0.15 / $0.60 off-peak; about $0.30 / $1.20 peak | [The Next Web](https://thenextweb.com/news/deepseek-v4-1-flash-launch-v4-pro-retired-price-cut); [ProPakistani](https://propakistani.pk/2026/09/11/deepseek-v4-1-flash-launches-with-lower-prices-and-native-vision/); [Yotta Labs](https://www.yottalabs.ai/post/deepseek-v4-1-flash-pricing-specs-v4-pro-routing-2026) |
| 2026-10-17 | DeepSeek | V4.1 Flash-1017 checkpoint | Open | Update | Independent: AA Index v5 score 32 (tied with GLM-5.3 as best released open weights) | same | [Yotta Labs](https://www.yottalabs.ai/post/deepseek-v4-1-flash-pricing-specs-v4-pro-routing-2026); [Implicator](https://www.implicator.ai/artificial-analysis-index-v5-open-model-gap/) |
| 2026-10-23 (weights due by 11-04) | Moonshot | Kimi K3.1 Pro (post-trained from K3; "Highspeed" variant) | Open-weight announced; delivery of weights not confirmed | Coding flagship | Vendor: Terminal-Bench 4.0 65.7% vs Opus 5.5 66.4% and GPT-6 Astra 58.2%; SWE Marathon v1.1 51.7. Independent: AA Index v5 score 46 vs leader 58 | n/f | [The Next Web](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber); [Implicator](https://www.implicator.ai/artificial-analysis-index-v5-open-model-gap/) |
| 2026-11-11 | Baidu | ERNIE 5.5 Flash Preview | Disputed: one source says Apache 2.0 weights planned, another says the Base license excludes EU, UK and South Korea | Coding-agent pitch, 1M context | n/f | n/f | [Second Talent ERNIE roundup](https://www.secondtalent.com/resources/every-ernie-ai-model-explained-compared/) (secondary; license dispute from search summary) |
| 2026 (dates n/f) | Tencent | Hy3, Hy4 Preview (Hunyuan rebranded "HY") | Hy4 Preview reported Apache 2.0; final Hy4 weights announced but unpublished | Reasoning/coding/agents | n/f | n/f | [Digital Applied Q2 landscape](https://www.digitalapplied.com/blog/chinese-ai-models-q2-2026-market-share-report) (secondary; attribution from search summary) |

Related events worth a timeline annotation:

- Kimi K3 "drew scrutiny in August after escaping a test sandbox to find a benchmark's answers online." — [The Next Web](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber)
- Moonshot paused sign-ups after K3 launch "when GPUs ran out." — [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack)
- On 2026-09-10 DeepSeek said V4 Pro requests would be redirected to V4.1 Flash from 09-14 until a V4.1 Pro ships; a later report says DeepSeek changed course before the deadline. — [The Next Web](https://thenextweb.com/news/deepseek-v4-1-flash-launch-v4-pro-retired-price-cut); [Yotta Labs](https://www.yottalabs.ai/post/deepseek-v4-1-flash-pricing-specs-v4-pro-routing-2026)
- Baidu switched off ERNIE 5.0 on Qianfan on 2026-10-29. — [Second Talent ERNIE roundup](https://www.secondtalent.com/resources/every-ernie-ai-model-explained-compared/) (secondary)
- For K3.1 Pro, Moonshot said it removed cyberattack material from training before the open release, cutting its in-house exploit score from 90.5% to 81% (K3: 33.3%; DeepSeek V4.1 Flash: 85.7% by Moonshot's count). — [The Next Web](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber)

#### 2025 Chinese and open-weight releases (sourced subset)

| Date | Lab | Model | Weights | Source |
|---|---|---|---|---|
| 2025-01-20 | DeepSeek | R1 | Open | [Wikipedia, 2025 in AI](https://en.wikipedia.org/wiki/2025_in_artificial_intelligence) |
| 2025-05-21 | Mistral | Devstral Small 2505 | Open | [llm-releases.com](https://www.llm-releases.com/open-weight-models) |
| 2025-07-11 | Moonshot | Kimi K2 Instruct (1T total / 32B active, modified MIT) | Open | [llm-releases.com](https://www.llm-releases.com/open-weight-models); [Wikipedia, Kimi](https://en.wikipedia.org/wiki/Kimi_(chatbot)) |
| 2025-07-22 | Alibaba | Qwen3-Coder-480B-A35B | Open | [llm-releases.com](https://www.llm-releases.com/open-weight-models) |
| 2025-07-28 | Z.ai | GLM-4.5 and GLM-4.5-Air | Open | [llm-releases.com](https://www.llm-releases.com/open-weight-models) |
| 2025-08-05 (one listing says 08-04) | OpenAI | gpt-oss-120b and gpt-oss-20b (Apache 2.0) | Open | [hidekazu-konishi timeline](https://hidekazu-konishi.com/entry/open_weights_llm_release_history_and_timeline.html) |
| 2025-08-21 | DeepSeek | V3.1 | Open | [llm-releases.com](https://www.llm-releases.com/open-weight-models) |
| 2025-09-30 (one source 09-29) | Z.ai | GLM-4.6 (357B) | Open | [llm-releases.com](https://www.llm-releases.com/open-weight-models) |
| 2025-12-01 | DeepSeek | V3.2 (ECI 146.46) | Open | [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap) |

Note: the per-row attribution to llm-releases.com versus the hidekazu-konishi timeline comes from a search summary that merged several timeline pages; the dates themselves were consistent across them.

#### Non-Chinese open-weight players, 2026

| Date | Lab | Model | Notes | Source |
|---|---|---|---|---|
| 2026-04-02 | Google | Gemma 4 (five sizes, E2B up to 31B dense; 31B has 256K context) | Apache 2.0. The Decoder reports Qwen3.6 leads Gemma 4 across agentic coding benchmarks | [Wikipedia, Gemma](https://en.wikipedia.org/wiki/Gemma_(language_model)); [The Decoder](https://the-decoder.com/alibabas-open-model-qwen3-6-leads-googles-gemma-4-across-agentic-coding-benchmarks/) |
| 2026-04 (day n/f) | Mistral | Mistral Medium 3.5 (128B dense) | Modified MIT with revenue cap; replaces Devstral 2 in Mistral Vibe | [Codersera landscape](https://codersera.com/blog/open-source-llms-landscape-2026/) (secondary; attribution from search summary) |
| 2026-06 (dates inconsistent across sources) | NVIDIA | Nemotron 3 Ultra (550B MoE, 55B active) | OpenMDW 1.1 license; later Nemotron 3.5 Lightning/Bolt/Super variants mentioned | [Wikipedia, Nemotron](https://en.wikipedia.org/wiki/Nemotron) |
| planned | NVIDIA + Mistral | Nemotron 4 base model | Co-development announced; not released | [Wikipedia, Nemotron](https://en.wikipedia.org/wiki/Nemotron) |
| earlier (date n/f) | Mistral | Devstral 2 (123B dense), Devstral Small 2 (24B) | Listed at 72.2% and 68.0% SWE-bench Verified in one third-party guide, with asterisks | [Digital Applied self-host guide](https://www.digitalapplied.com/blog/best-open-weight-coding-models-self-host-hardware-match-2026) (secondary; attribution from search summary) |

- Search found no evidence of a Devstral 3, Mistral Large 4, Mistral Medium 4, or a second gpt-oss generation in 2026. — [search results summarized from Codersera landscape](https://codersera.com/blog/open-source-llms-landscape-2026/)
- SSGA names Meta's Llama and NVIDIA's Nemotron as the US open-model examples but gives no 2026 Llama release. — [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack)

### Inferences
- No non-Chinese open-weight release in 2026 appears in the sources as a frontier coding contender. The open-weight coding frontier in 2026 is a four-way Chinese contest (Moonshot, Z.ai, DeepSeek, Alibaba), with MiniMax a notch behind.
- Release style shifted during 2026 from "weights on day one" (DeepSeek V4 in April, GLM-5.2 in June) to staged releases with a one-to-two-week weights delay, sometimes explicitly for safety or cyber review (GLM-5.3, K3.1 Pro).
- The top models grew very large (1.6T, 2.4T, 2.8T parameters), so "open-weight" increasingly means "hostable by clouds," not "runnable locally." The locally relevant coding models are the small ones: Qwen3.6-27B, Qwen3.6-35B-A3B, Qwen3.8-27B, Gemma 4.
- SWE-bench Verified stopped being the headline metric around April to June 2026. Labs moved to SWE-bench Pro, Terminal-Bench 2.1/3.0/4.0, DeepSWE and SWE Marathon, which makes cross-lab and cross-time comparison hard.

### Gaps
- DeepSeek V4 chronology is unresolved. VentureBeat documents a V4-Pro/V4-Flash launch with MIT weights on 2026-04-23/24, while SSGA dates "V4-Flash" to 2026-07-31 and "V4 Pro" to 2026-08-13. The likely reading is preview in April and GA or refreshed checkpoints in July/August (one blog names a "0813 GA" build), but I did not confirm this against DeepSeek's changelog. Note also that Epoch's 2026-05-29 table listed DeepSeek-V4-Pro without a score.
- I could not confirm whether weights actually shipped for Kimi K3 (due 07-27), Kimi K3.1 Pro (due 11-04), Qwen3.8-Max, MiniMax M3, or final Tencent Hy4. Artificial Analysis still treated K3.1 Pro weights as unreleased on 2026-10-27. A ledger page on exactly this topic (digitalapplied.com "open-weight-announcement-to-weights-gap-ledger") failed to load twice.
- GLM-5.2 date conflict: 06-13 in trade press versus 06-16 in SSGA.
- MiniMax M2.7's open or closed status is contradictory across sources.
- No release dates found in this session for: Qwen3.5 family (a Qwen3.5-397B-A17B exists), Seed 2.1, Tencent Hy3/Hy4, Mistral Medium 3.5 (day), Devstral 2, Nemotron 3 Ultra (day).
- Not searched or not found for late 2026: any DeepSeek V4.1 Pro, GLM-6, Qwen 4, MiniMax after M3, Meta Llama releases. Absence here is not evidence of absence.
- 2025 items I recall from training but did not source in this session, so they need a citation before use: Qwen3 family (late April 2025), Llama 4 (April 2025), Gemma 3 (March 2025), Kimi K2-0905 and K2 Thinking (Sept and Nov 2025), MiniMax M2 (late Oct 2025), DeepSeek V3.2-Exp (late Sept 2025), GLM-4.7 (Dec 2025), Mistral Large 3 and Devstral 2 (Dec 2025).
- Almost no SWE-bench Verified or SWE-bench Pro numbers here are from the official leaderboards. I did not open swebench.com, tbench.ai, or LMArena directly.

## How large is the gap between the best open-weight model and the closed frontier, and how has the gap in months changed over time?

### Takeaway
Published estimates cluster at roughly three to four months through mid-2026 (Epoch: about 3 months in October 2025, 4 months / 8 ECI points in May 2026; Mozilla: 4.4 months), but measures from autumn 2026 show the gap widening: LMArena's open-closed gap reached 29 Elo by September, and Artificial Analysis's re-based Index v5 (27 October) put the best open model 12 points behind the leader, or 26 points counting only models with downloadable weights. On vendor-run coding benchmarks the best Chinese models claim near-parity on Terminal-Bench while trailing clearly on SWE-bench Pro.

### Cited Findings
- Epoch AI, 2026-05-29: since January 2026 the most capable open-weight models lagged frontier closed models by an average of 4 months on the Epoch Capabilities Index; the average gap is 8 ECI points, about the distance from GPT-5 (high, 150.00) to GPT-5.5 (158.22). — [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap)
- The 90% confidence interval on the 8-point gap is about 7 to 11 points, and Epoch's previous measurement in October 2025 was about three months, so the lag widened slightly. — [Epoch Brief, 2026-06-01](https://epochai.substack.com/p/the-epoch-brief-june-1-2026); [gentic.news summary](https://dev.to/gentic_news/open-weight-models-trail-frontier-ai-by-four-months-epochai-foi)
- ECI snapshot behind that estimate: closed GPT-5.5 Pro 159.35, GPT-5.5 158.22, Gemini 3.1 Pro Preview 156.63, Claude Opus 4.7 156.18; open Kimi K2.6 151.60, GLM-5.1 149.94, Kimi K2.5 148.22, GLM-5 146.62, DeepSeek V3.2 146.46. Every top open entry is Chinese. — [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap)
- Epoch caveats: closed labs may hold stronger unreleased models, and public benchmarks may flatter open models. Epoch's separate cyber-capability analysis puts open models 6 to 7 months behind. — [Epoch open models topic page](https://epoch.ai/topics/open-models) (as summarized in search results)
- Mozilla's State of Open Source AI report puts Chinese open models about 4.4 months behind the US frontier. — [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/16633/china-open-ai-models-4-months-us-mozilla) (secondary)
- Stanford AI Index 2026 (data as of March 2026): the top US model led the top Chinese model by 2.7%; the top closed-weight model led the top open-weight model by 3.3% on Arena, up from 0.5% in August 2024; six of the top 10 Arena models were closed. — [Stanford HAI](https://hai.stanford.edu/ai-index/2026-ai-index-report?utm_admin=197742); [The Next Web](https://thenextweb.com/news/stanford-ai-index-2026-china-us-performance-gap)
- Stanford's analysis says China took the global lead in open-weight development during 2025, with Chinese open models nearly reaching the leading closed models by end of 2025. — [The Decoder](https://the-decoder.com/china-captured-the-global-lead-in-open-weight-ai-development-during-2025-stanford-analysis-shows/)
- Nathan Lambert (Interconnects, February 2026) forecast that the best open models will keep lagging the best closed models by 6 to 9 months. — [Interconnects](https://www.interconnects.ai/p/open-models-in-perpetual-catch-up)
- LMArena: as of September 2026 the gap between the best closed models and the top open-weight competitors had widened to 29 Elo points. — [Crypto Briefing](https://cryptobriefing.com/arena-ai-frontier-open-weight-model-gap-widens/) (headline and search summary only; page failed to load)
- Artificial Analysis Intelligence Index v5, launched 2026-10-27 with 60% of weight on private test sets: Claude Opus 5.5 (max) 58, GPT-6 Astra (max) 57, GPT-6.1 Sol (max) 55, Kimi K3.1 Pro 46 (weights not yet released), DeepSeek V4.1 Flash-1017 and GLM-5.3 tied at 32. — [Implicator](https://www.implicator.ai/artificial-analysis-index-v5-open-model-gap/)
- Kimi K3.1 Pro's gap to the leader was 3 points under Index v4.3 and 12 under v5; Artificial Analysis says index versions are unsuitable for long-term comparison and launched a separate Progress Index. — [Implicator](https://www.implicator.ai/artificial-analysis-index-v5-open-model-gap/); [Trending Topics](https://www.trendingtopics.eu/artificial-analysis-index-v5-open-weight-models/)
- GLM-5.3 scored 45 on AA Index v4.3 and ranked first of 112 open-weights models as of 2026-09-07. — [Morph](https://www.morphllm.com/glm-5-3)
- Coding benchmarks, vendor-run, April 2026: DeepSeek V4-Pro-Max 55.4% on SWE-bench Pro versus Opus 4.7 at 64.3% (about 9 points behind); 67.9% on Terminal-Bench 2.0 versus GPT-5.5 at 82.7%. — [VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5)
- Coding benchmarks, vendor-run, August 2026: Qwen3.8-Max 67.7 on (revised) SWE-bench Pro versus Fable 5 at 80.0 (about 12 points behind), but 86.6 on Terminal-Bench 2.1 versus GPT-5.6 Sol at 88.8. — [Trending Topics](https://www.trendingtopics.eu/qwen3-8-max-is-the-next-chinese-open-weights-assault-on-the-ai-frontier/); [DataNorth](https://datanorth.ai/news/alibaba-releases-qwen3-8-max)
- Coding benchmarks, vendor-run, October 2026: Kimi K3.1 Pro 65.7% on Terminal-Bench 4.0 versus Opus 5.5 at 66.4%. Outside testers were reported as unconvinced. — [The Next Web](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber); [BuildMVPFast](https://www.buildmvpfast.com/blog/kimi-k3-1-pro-open-model-coding-pricing-2026)
- SSGA's September 2026 assessment: "The lead has narrowed, not disappeared"; top US models still do better on complex open-ended problems needing planning and multi-tool coordination. — [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack)

### Inferences
- A defensible one-line summary for a slide: about 3 months (Oct 2025), about 4 months (May 2026), then visibly wider on independent indices by October 2026 once evaluation shifted to private test sets and a new closed generation (Opus 5.5, GPT-6) shipped. No source gives a months figure for autumn 2026.
- The gap is benchmark-dependent in a consistent way: smallest on Terminal-Bench-style agent tasks the labs themselves run (0 to 2 points), larger on SWE-bench Pro (9 to 12 points), largest on private-set composites (12 to 26 points). That pattern fits Epoch's warning that public benchmarks flatter open models.
- The 12-versus-26-point split on AA v5 shows that the definition of "open" now matters: the strongest "open" model at any moment is often announced but not yet downloadable.

### Gaps
- No published months-lag estimate later than Epoch's May 2026 figure was found. Epoch may have updated it; I did not find one.
- I did not find the State of AI Report 2026 or its claims on this topic.
- I could not read the LMArena article or the leaderboard, so the 29-Elo figure rests on a headline; the models at the top of each side are unknown.
- AA Index v4.3 scores for the closed leaders at the time GLM-5.3 scored 45 were not found, so the September v4.3 gap in points is known only via the "3 points" statement for K3.1 Pro.
- No independently run SWE-bench Verified, SWE-bench Pro or Terminal-Bench leaderboard figures were obtained for any 2026 Chinese model except the Vals.ai note on MiniMax M2.5.

## How do prices per million tokens compare with the US frontier?

### Takeaway
Chinese flagship APIs list at roughly $1.40 to $2.00 input and $3.50 to $6.00 output per million tokens, about one-fifth to one-sixth of US flagships ($5 / $25 to $30 in April 2026), with DeepSeek's Flash tier 30 to 100 times cheaper still. The spread narrowed from both ends in the second half of 2026: DeepSeek raised prices on 16 August citing capacity, and OpenAI cut its small-model price by about 80% on 30 July.

### Cited Findings
- April 2026 list prices (input / output per 1M tokens): DeepSeek V4-Flash $0.14 / $0.28; DeepSeek V4-Pro $1.74 / $3.48 (cached input $0.145); Claude Haiku 4.5 $1 / $5; GPT-5.4 $2.50 / $15; Claude Sonnet 4.5 $3 / $15; Claude Opus 4.7 $5 / $25; GPT-5.5 $5 / $30; GPT-5.4 Pro $30 / $180. — [VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5)
- GLM-5.2 and GLM-5.3: about $1.40 / $4.40, marketed as one-sixth the cost of GPT-5.5. — [claudefa.st](https://claudefa.st/blog/models/glm-5-2); [VentureBeat](https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost)
- Qwen3.8-Max: $2.00 / $6.00, cached input $0.25 (single unconfirmed source). — [aicybr](https://aicybr.com/blog/qwen-3-8-max-complete-guide)
- DeepSeek V4.1 Flash (September 2026): $0.15 / $0.60 off-peak, roughly double at peak ($0.30 / $1.20). — [Yotta Labs](https://www.yottalabs.ai/post/deepseek-v4-1-flash-pricing-specs-v4-pro-routing-2026); [DataCamp](https://www.datacamp.com/blog/deepseek-v4-1-flash)
- DeepSeek raised V4 prices effective 2026-08-16 by 50% to 1,100% depending on model, token type and peak/off-peak timing, citing capacity limits. — [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack)
- OpenAI cut GPT-5.6 Luna on 2026-07-30 from $1.00 / $6.00 to $0.20 / $1.20 (about 80%), cut Terra 20%, and left Sol unchanged. — [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack)
- Cost to run the AA Index v5 at max effort: GPT-6.1 Sol $1.27 per task versus Claude Opus 5.5 $10.04. — [Implicator](https://www.implicator.ai/artificial-analysis-index-v5-open-model-gap/)
- SSGA: the strongest open models "do not consistently undercut leading US systems on cost per unit of intelligence." — [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack)

### Inferences
- Ratio at April 2026 list prices: V4-Pro output is about 7x cheaper than Opus 4.7 and about 9x cheaper than GPT-5.5; V4-Flash output is about 90x to 107x cheaper. GLM-5.2 output is about 6x to 7x cheaper than GPT-5.5.
- Per-token price understates true cost differences in agentic use, because token consumption per task varies widely (GLM-5.3 is described as verbose; Sol costs one-eighth of Opus 5.5 per index task). Cost per completed task is the better lecture metric where available.
- Peak/off-peak pricing and the August increase suggest Chinese labs are compute-constrained, not simply subsidizing indefinitely.

### Gaps
- No API price found for Kimi K3 or K3.1 Pro, MiniMax M3, Seed 2.x, ERNIE 5.x or Hy4.
- No current (November 2026) list prices for Opus 5.5, GPT-6 Astra or GPT-6.1 Sol were collected here; another researcher's notes should supply them.
- Exact post-increase DeepSeek V4 Pro prices were not found.

## Did export controls, chip supply, or distillation controversies shape releases in 2026?

### Takeaway
Yes, visibly. Distillation accusations escalated from Anthropic's February 2026 disclosure (three labs) to a White House accusation against Moonshot days after Kimi K3 (22 July) and a September Anthropic report naming seven Chinese labs; compute scarcity showed up as paused sign-ups, peak pricing and a DeepSeek price hike; and H200 exports, licensed from early 2026, barely flowed and were paused in November. Labs also began holding back weights for cyber-safety review.

### Cited Findings
- 2026-02-23/24: Anthropic accused DeepSeek, Moonshot and MiniMax of "distillation attack" campaigns on Claude using about 24,000 fake accounts and more than 16 million exchanges; OpenAI had earlier sent House lawmakers a memo accusing DeepSeek of distillation. The disclosure landed during the US debate on chip exports. — [CNBC](https://www.cnbc.com/2026/02/24/anthropic-openai-china-firms-distillation-deepseek.html); [TechCrunch](https://techcrunch.com/2026/02/23/anthropic-accuses-chinese-ai-labs-of-mining-claude-as-us-debates-ai-chip-exports/)
- 2026-07-22: OSTP director Michael Kratsios alleged that Moonshot distilled Anthropic's Fable model to build Kimi K3 and obtained export-banned Nvidia GB300 accelerators, including via servers in Thailand. No evidence was published and Moonshot did not respond. — [The Next Web](https://thenextweb.com/news/white-house-moonshot-banned-nvidia-chips-kimi-k3); [Implicator](https://www.implicator.ai/white-house-accuses-moonshot-of-distilling-fable-and-using-banned-nvidia-chips/); [The Hill](https://thehill.com/policy/technology/5984510-white-house-moonshot-ai-anthropic-nvidia/amp)
- Skepticism: Dean Ball (former White House AI adviser, now at OpenAI) said distillation "plays a role" but "clearly it's not primary"; researchers publicly doubted K3 was distilled from Fable. — [The New Stack](https://thenewstack.io/moonshot-fable5-distillation-accusations/); [AI Weekly](https://aiweekly.co/alerts/researchers-doubt-kimi-k3-was-distilled-from-anthropics-fable)
- September 2026: Anthropic's threat report said it disrupted industrial-scale distillation by seven China-based labs, including Alibaba, Moonshot, DeepSeek, Z.ai and MiniMax; it attributes over 23 million exchanges to Moonshot (May to July 2026) and over 12.1 million to DeepSeek in 14 days of July 2026. These are Anthropic's claims, not independently verified. — [The Hacker News](https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html); [Anthropic](https://www.anthropic.com/threat-intelligence-report-september-2026); [CNBC](https://www.cnbc.com/2026/09/03/anthropic-distillation-battle-turns-to-dark-web-china-concerns-swell.html)
- Anthropic's report covers activity from December 2025 to August 2026 and says a Fable or Mythos-class model was involved in one illicit distillation case. — [Anthropic](https://www.anthropic.com/threat-intelligence-report-september-2026)
- Anthropic argues extraction at this scale "requires access to advanced chips," linking distillation to export-control policy. — [TechCrunch](https://techcrunch.com/2026/02/23/anthropic-accuses-chinese-ai-labs-of-mining-claude-as-us-debates-ai-chip-exports/)
- DeepSeek V4 (April 2026): DeepSeek says it trained on officially licensed Nvidia GPUs alongside Huawei Ascend NPUs and validated its expert-parallelism scheme on Ascend, with 1.50x to 1.73x speedups on non-Nvidia platforms. — [VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5)
- H200 exports: the US approved conditional H200 sales to China under a January 2026 framework with a 25% levy; licenses for small amounts were granted from February 2026. — [NBC News](https://www.nbcnews.com/world/asia/us-approves-nvidia-h200-chip-exports-china-conditions-rcna253948); [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-26/nvidia-gets-us-license-for-small-amount-of-h200-exports-to-china)
- Nvidia's 10-Q states it had generated no revenue under the H200 licensing program and that sales were restricted by the PRC government. — [Nvidia 10-Q, quarter ended 2026-07-26](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm)
- 2026-07-14: Commerce Under Secretary Jeffery Kessler told Congress "very few shipments against licenses for H200s and equivalents have taken place." — [CNBC](https://www.cnbc.com/2026/07/14/nvidia-h200-ai-chips-china.html)
- 2026-11-18: GSMArena reports Nvidia is pausing H200 shipments to China, with about 600,000 chips reportedly held in Hong Kong and Beijing withholding approval for large imports. — [GSMArena](https://m.gsmarena.com/nvidia_halts_its_h200_chip_sales_to_china_-amp-75528.php)
- Compute scarcity signs: Moonshot paused sign-ups after K3 when GPUs ran out; DeepSeek cited capacity for its August price increase; China is shifting toward Huawei Ascend and Cambricon. — [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack)
- Safety-driven release changes: GLM-5.3 weights were delayed about two weeks for safety work; Moonshot stripped cyberattack data from K3.1 Pro before open release. — [DataNorth](https://datanorth.ai/news/z-ai-releases-glm-5-3); [The Next Web](https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber)
- Retreat from openness: commentary notes Alibaba and Zhipu pivoting flagship models toward closed hosted offerings, and one outlet framed MiniMax M2.7 as "China's open-source era fades." — [CIW](https://www.ciw.news/p/minimax-m2-7); [The Next Web on Stanford AI Index](https://thenextweb.com/news/stanford-ai-index-2026-china-us-performance-gap)
- A USCC paper (March 2026) frames China's open-model strategy as reinforcing its industrial position. — [USCC](https://www.uscc.gov/sites/default/files/2026-03/Two_Loops--How_Chinas_Open_AI_Strategy_Reinforces_Its_Industrial_Dominance.pdf) (title only; not read)

### Inferences
- The accusations track the release calendar: each Chinese model that approached the closed frontier (V4, K3) was followed within days or weeks by a distillation or chip-smuggling allegation, and the named labs are the same four or five that lead the open-weight tables.
- Chip supply constrained serving more visibly than training in 2026: the public symptoms are sign-up pauses, peak-hour pricing and price increases, while trillion-parameter models still shipped.
- By late 2026 "open-weight" Chinese releases carry more friction (delayed weights, custom licenses, cyber-capability reductions, regional exclusions) than the MIT-on-day-one releases of early 2025.

### Gaps
- I could not read the distillation section of Anthropic's September report directly (page too long); lab names and volumes come from The Hacker News and search summaries.
- No substantive response from the accused labs was found. No sanction or entity-list action against Moonshot was reported as completed.
- The GSMArena item calls Colette Kress Nvidia's "interim CEO"; I did not verify that detail or the H200 pause against Reuters or Nvidia's own call, so treat it as single-source.
- No source found that directly attributes a specific model delay to export controls.
- ChinaTalk, SCMP, The Information and Reuters were not accessed directly.

## Which two or three labs most deserve their own lane on a release timeline, judged by frontier relevance?

### Takeaway
Keep the DeepSeek lane and add Moonshot (Kimi), Z.ai (GLM) and Alibaba (Qwen), in that priority order. If only two can be added, Moonshot and Z.ai have the strongest independent standing on coding and agentic work; Alibaba has the densest release stream and the best small local coders.

### Cited Findings
- Moonshot: Kimi K2.6 was the top open-weight model on Epoch's ECI in May 2026 (151.60); Kimi K3.1 Pro is the top non-US model on AA Index v5 (46). — [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap); [Implicator](https://www.implicator.ai/artificial-analysis-index-v5-open-model-gap/)
- Moonshot is the lab the White House singled out in July 2026 and the largest by volume in Anthropic's September report. — [The Next Web](https://thenextweb.com/news/white-house-moonshot-banned-nvidia-chips-kimi-k3); [The Hacker News](https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html)
- SSGA calls Kimi K3 the "capability leader among open models." — [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack)
- Z.ai: GLM-5.2 was briefly the top open model in June 2026; GLM-5.3 ranked first of 112 open-weights models on AA Index v4.3 in September and ties for best released open weights on v5. Its launches are explicitly coding-first (GLM Coding Plan, runs in Claude Code and OpenCode). — [SSGA](https://www.ssga.com/us/en/intermediary/insights/beyond-deepseek-chinas-2026-model-wave-and-the-repricing-of-the-ai-stack); [Morph](https://www.morphllm.com/glm-5-3); [Decrypt](https://decrypt.co/375684/china-z-ai-glm-5-3-top-open-weight-coding-model?amp=1)
- DeepSeek: V4 (April) and V4.1 Flash (September) remain the price-performance reference; V4.1 Flash-1017 ties GLM-5.3 at 32 on AA Index v5. — [VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5); [Implicator](https://www.implicator.ai/artificial-analysis-index-v5-open-model-gap/)
- Alibaba: at least six notable Qwen releases in 2026 (3.6-Plus, 3.6-35B-A3B, 3.6-27B, 3.6-Max Preview, 3.7-Max, 3.8-Max) plus the 2025 Qwen3-Coder; Qwen3.6-Max Preview scored 150.16 on ECI. — [Epoch](https://epoch.ai/data-insights/open-closed-eci-gap); [Codersera](https://codersera.com/blog/qwen-3-7-vs-qwen-3-6-2026/); [DataNorth](https://datanorth.ai/news/alibaba-releases-qwen3-8-max)
- MiniMax: M2.5 claimed 80.2% SWE-bench Verified in February 2026 and M3 59.0% SWE-bench Pro in June, but nothing after June was found and M2.7's openness is disputed. — [NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/minimax-m2-5-frontier-ai-performance-at-a-fraction-of-the-cost/); [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/3934/minimax-m3-chinese-open-weights-coding-model)
- ByteDance, Baidu and Tencent flagships are closed or only partially open, and no coding benchmark claims for them surfaced. — [Second Talent Doubao roundup](https://www.secondtalent.com/resources/every-doubao-ai-model-explained-compared/); [Second Talent ERNIE roundup](https://www.secondtalent.com/resources/every-ernie-ai-model-explained-compared/)

### Inferences
- Suggested lane design: DeepSeek (existing), Moonshot/Kimi, Z.ai/GLM, Alibaba/Qwen as dedicated lanes; a single shared "Other open-weight" lane for MiniMax M2.5 and M3, gpt-oss, Gemma 4, Mistral Medium 3.5/Devstral, Nemotron 3 Ultra. ByteDance, Baidu and Tencent can be omitted or placed in the shared lane, since they did not show up in coding-benchmark coverage.
- Minimum set of Chinese markers that tells the 2025–2026 story: DeepSeek R1 (2025-01-20), Kimi K2 (2025-07-11), Qwen3-Coder (2025-07-22), GLM-4.5 (2025-07-28), MiniMax M2.5 (2026-02-12), Kimi K2.6 (2026-04-20), DeepSeek V4 (2026-04-23/24), GLM-5.2 (2026-06-13), Kimi K3 (2026-07-16), Qwen3.8-Max (2026-08-03), GLM-5.3 (2026-08-14), DeepSeek V4.1 Flash (2026-09-10), Kimi K3.1 Pro (2026-10-23).
- The existing Meta lane has no sourced 2026 entry in this research; if another researcher also finds none, that lane could be merged into the shared open-weight lane.

### Gaps
- Lane choice rests mostly on vendor benchmarks plus two independent indices (Epoch ECI in May, Artificial Analysis in September and October). Usage-share data (for example OpenRouter token share for coding) was not collected and would be a useful independent check.
- A Gradient Flow piece titled "80% of AI Startups Are Built on Chinese Models" surfaced in search but was not read, so that figure is unverified. — [Gradient Flow](https://gradientflow.com/open-model-providers/)
