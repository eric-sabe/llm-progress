<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Frontier AI evaluation survey — 19 November 2026

## Executive summary

The most important additions to your lecture are not another set of harder coding questions. They are evaluations of sustained development, project continuation, review quality, research automation, and the integrity of the evaluation process itself.

Five findings stand out:

1. **There is no verified consensus successor to SWE-bench Verified.** The replacement landscape is fragmented: SWE-rebench and SWE-bench-Live address freshness; ProgramBench addresses building software from scratch; SWE Atlas addresses comprehension, tests and refactoring; SWE-Marathon and LoopsBench address sustained execution. These measure different things rather than competing to supply one interchangeable score.[^1][^2][^3][^4][^5][^6]
2. MirrorCode is a substantial alternative to human-time-horizon measurement, but not a replacement series with the same interpretation. Its current leaderboard allows seven days and 10 billion tokens per attempt; it measures exact whole-program reimplementation, not the maximum duration of arbitrary unattended work. I did not verify an announced direct successor to METR’s frozen time-horizon series.[^7][^8]
3. The newest useful coding evaluations increasingly ask whether an agent preserves obligations over time. LoopsBench measures dependency-aware progress and regressions; ARE-bench resumes real research projects with unfinished files and inherited requirements; SWE Atlas v1.1 evaluates maintenance work beyond issue repair.[^4][^6][^9]
4. Independent evaluation is moving inside frontier labs. On 16 November, OpenAI announced embedded assessments with Apollo, METR, Transluce and Goodfire. This is a major methodological development—but “independent” now needs qualification about payment, access restrictions, publication rights and developer-controlled disclosure.[^10]
5. Several things in your current-use list now have material qualifications: Epoch rated ARC-AGI-3 “Flawed” on 30 October, OSWorld 2.1 “Flawed” on 28 September, and Vending-Bench 2 “Flawed” on 21 October. “Flawed” is Epoch’s review verdict, not a universal retirement decision.[^11]

### Reading conventions and limitations

- Cutoff: 19 November 2026, approximately 1:46 p.m. EST.
- Recent-change window: 20 September–19 November 2026.
- `I` = independently executed by a benchmark team or third-party evaluator; `V` = model/agent vendor’s own result; `M` = mixed submissions; `U` = execution provenance unverified.
- `D` = undated live page, retrieved 19 November 2026. This is not a publication date.
- `†` marks evidence older than six months—before 19 May 2026—and therefore possibly stale. An old launch date does not make a newer result stale.
- “Headroom” means remaining room under that benchmark’s scoring contract, not remaining distance to general intelligence.
- Where I could verify a benchmark but not a current primary-source leader, I say “unverified” rather than import a number from a comparison site.

This is a broad, evidence-qualified survey, not a claim that every late-2026 evaluation has been exhaustively discovered. The weakest coverage is current formal-proof leaderboard standings, several private enterprise evaluations, and complete funding histories for every evaluator.

# A. Benchmarks and methods not in your already-covered list

The tables use your requested fields, split by domain for readability. Publication/result dates appear in the launch or score cells. Source URLs point to the underlying source, not an aggregator unless explicitly identified.

## A1. Software engineering, maintenance and long-running coding

| Name | Category | Run by | Launched | Measures | Top score and holder | Vendor or independent | Headroom | Source URL |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| SWE-rebench | Fresh repository engineering | Nebius benchmark team | May 2025†; exact initial day unverified | Rolling GitHub issues; resolved rate, pass@5, tokens and cost | Official retrieved window, 15 May–1 July 2026: Fable 5 high, 64.5% ±1.41%; \$4.40/problem. Not verified as the newest available window | I for model runs; external agent entries separately identified | 35.5 percentage points on this window; changes with window | [https://swe-rebench.com/](https://swe-rebench.com/) [^1][^12] |
| SWE-bench-Live | Fresh repository engineering | SWE-bench-Live research/maintainer team | May 2025† | Automatically assembled issue-resolution tasks; Python, multilingual and Windows tracks | Python 300-instance board: TianxiCode + DeepSeek-v4.1-Flash, 71.0%, 8 Oct 2026 | M; “Verified” means maintainers checked submission trajectories, not necessarily independently reran it | 29 points on that split | [https://swe-bench-live.github.io/](https://swe-bench-live.github.io/) [^2][^13] |
| ProgramBench | From-scratch software | SWE-bench team; Vals implementation | May 2026; exact day unverified | Building substantial software artifacts rather than patching filed issues | Vals implementation: Fable 5.2, 19.00%, 9 Nov; \$46.82/task, 2h05m average | I, Vals implementation; do not merge with other ProgramBench harnesses | 81 points under Vals’ full-resolution metric | [https://www.vals.ai/benchmarks/programbench](https://www.vals.ai/benchmarks/programbench) [^3][^14] |
| CodeClash | Goal-oriented development | SWE-bench researchers | Nov 2025† | Development toward a competitive goal, rather than a fixed issue specification | Current leader unverified | U | Unverified; not a conventional fixed-ceiling task score | [https://www.swebench.com/](https://www.swebench.com/) [^3] |
| SWE Atlas v1.1 | Maintenance and comprehension | Scale Labs/SEAL | Repository Mar 2026†; paper 8 May 2026†; v1.1 Nov 2026 | 284 tasks: codebase Q\&A, test writing, refactoring; functional and rubric grading | D: Fable 5.2 overall 80.55 ±4.80; Fable 5.1 test writing 78.89 ±8.60. Units as published | I, Scale; new judge and restricted networking in v1.1 | Approximately 19.5 overall points; uncertainty is substantial | [https://github.com/scaleapi/swe-atlas](https://github.com/scaleapi/swe-atlas) [^4][^15][^16] |
| SWE-Marathon v1.1 | Long-horizon engineering | Abundant AI, with community contributors | 5 June 2026 paper | 20 multi-hour tasks including compilers, ports, product clones, ML and optimization | D: Gemini 4 Carbon high / Antigravity CLI, 53.8% pass@1; eight trials/task | I for this leader; Z.ai executed its own GLM entries | 46.2 points; some individual tasks remain at 0% | [https://www.swe-marathon.org/](https://www.swe-marathon.org/) [^5] |
| LoopsBench | Persistent development and regression | Microsoft, Nanjing University, UCL, Shanghai Jiao Tong | 31 July 2026 | 112 dependency-DAG tasks; >5,300 development units; progress, regression, planning and state continuity | Paper: Opus 4.7 / Claude Code with outer continuation, 25.00% resolved | Research-team run; Microsoft-affiliated, not Anthropic-run | 75 points; latest November leader unverified | [https://arxiv.org/html/2608.00267v1](https://arxiv.org/html/2608.00267v1) [^6] |
| ReviewBench | Code review | GitHub | 5 Oct 2026 | 219 PRs, 187 repositories, 19 languages; multi-source bug ground truth and production-aligned review metrics | Current leader unverified | Benchmark creator is also a code-review vendor; entry provenance must be checked | Unverified; precision and recall matter separately | [https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/) [^17] |
| MacroscopeBench | Code review | Macroscope | Guide published 22 Sept 2026; original launch unverified | 12,000+ bugs, 1,500+ repositories, 14 languages; recall, precision, noise, cost, latency; three independent runs | Current primary-source leader not extracted/verified | V: code-review product vendor’s evaluation | No meaningful single headroom figure without precision/recall operating point | [https://macroscope.com/content/ai-code-review-benchmark-best-models](https://macroscope.com/content/ai-code-review-benchmark-best-models) [^18] |
| SWE-Lancer | Paid software work | OpenAI | Feb 2025† | Freelance engineering and managerial proposal selection, tied to historical payments | Current full-suite leader unverified. Harbor paper, 3 Sept 2026, reports a 463-task adaptation—not interchangeable with the original full benchmark | V for original OpenAI results; third-party adaptations exist | Unverified; distinguish task success from dollars “earned” | [https://proceedings.mlr.press/v267/miserendino25a.html](https://proceedings.mlr.press/v267/miserendino25a.html) [^19][^20] |
| CooperBench | Multi-agent coding | CooperBench research team | Jan 2026† | 652 collaborative tasks across 12 libraries and four languages; compatible features that can conflict during implementation | Published study: GPT-5 and Sonnet 4.5 around 25% cooperative success; current leader unverified | I with respect to those model vendors | Large; paper reports roughly 50% worse success than solo execution for those pairings | [https://cooperbench.com/](https://cooperbench.com/) [^21][^22][^23] |

A useful distinction for your lecture: no newly verified benchmark here makes human maintainer judgment the universal ground truth for all coding. ReviewBench’s senior-engineer validation, SWE Atlas’s quality rubrics, and ProgramBench’s behavioral evaluation solve different problems. They should not be described as equivalent to maintainers deciding whether to merge an actual contribution.[^17][^24][^25]

## A2. AI research, research engineering and evaluation automation

| Name | Category | Run by | Launched | Measures | Top score and holder | Vendor or independent | Headroom | Source URL |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| MLE-bench | ML engineering | OpenAI | 9 Oct 2024† | 75 Kaggle competitions; medal-level performance with resource constraints | Current full-suite leader unverified. Original o1-preview/AIDE result: bronze-or-better on 16.9%† | V for original result | Original number is stale; do not use to characterize November frontier | [https://arxiv.org/abs/2410.07095](https://arxiv.org/abs/2410.07095) [^26] |
| MLE-bench Lite | ML engineering subset | OpenAI dataset; third-party agent papers | Exact Lite launch unverified | Smaller competition subset | AiScientist paper, 15 Apr 2026†: 81.82% Any Medal | Research-team reported; not an independent replication; stale | 18.18 points on Lite only | [https://arxiv.org/html/2604.13018v1](https://arxiv.org/html/2604.13018v1) [^27] |
| RE-Bench | AI R\&D engineering | METR | 22 Nov 2024† | Seven open-ended research-engineering environments; human comparison at different budgets | Current leader unverified; launch comparison reverses between short and long budgets | I, METR | Not naturally a percentage ceiling; reference-normalized optimization scores | [https://arxiv.org/abs/2411.15114](https://arxiv.org/abs/2411.15114) [^28] |
| PaperBench | Research replication | OpenAI | 2 Apr 2025† | Replication of 20 ICML papers; 8,316 rubric items | Current full-protocol leader unverified. AiScientist reports 33.73 average, 15 Apr 2026†, with GPT-5.4 grading | Research-team reported; modified grading configuration | About 66 points on that reported rubric, but stale and configuration-specific | [https://arxiv.org/abs/2504.01848](https://arxiv.org/abs/2504.01848) [^29][^27] |
| MirrorCode | Whole-program autonomy | Epoch AI + METR | Preliminary 10 Apr 2026†; full release 26 June 2026 | Reimplement programs from behavior, documentation and visible tests; exact hidden-test equivalence | Current holder unverified. Epoch search catalog shows highest score 98%, but holder not exposed in retrieved material; not usable as a fully specified leaderboard claim | I for Epoch runs | Current configuration: 30 tasks, three runs, seven days and 10B tokens/attempt; numerical headroom unverified | [https://epoch.ai/benchmarks/mirrorcode](https://epoch.ai/benchmarks/mirrorcode) [^7][^30][^31] |
| PostTrainBench v1.2 | Autonomous model improvement | Tübingen/ELLIS/Max Planck/Thoughtful Lab researchers | 2026; paper March†; v1.2 30 Sept | Post-train four small base models; one H100, ten hours; downstream scores | Current primary-source leader unverified because score table did not render. Last source changelog: 12 Nov | M; research-team runs plus reviewed external submissions | Not “100 minus score” in a useful sense: score is downstream model quality | [https://posttrainbench.com/index.html](https://posttrainbench.com/index.html) [^32] |
| WeirdML v3 | ML problem solving and efficiency | WeirdML creators; tracked by Epoch | 18 Sept 2026 listing | Eleven unusual ML tasks; best-so-far effective score against tokens | D: Epoch lists highest score 42%; holder unverified | Creator-administered; exact independence unverified | Substantial; optimization/token frontier, not just final score | [https://epoch.ai/benchmarks/weirdml-v3](https://epoch.ai/benchmarks/weirdml-v3) [^33] |
| ARE-bench | Continuing real research projects | ARE-bench author team | 10 Nov 2026 | 75 tasks from real researcher sessions and dirty workspaces; inherited constraints and full delivery | GPT-6.1 Sol / Codex: 66.22% ±5.39 SD strict success; three rounds; task limits 30 min–48 h | Author-team evaluation; not a separate independent replication | 33.78 points; checklist partial credit is much higher | [https://arxiv.org/html/2611.14364](https://arxiv.org/html/2611.14364) [^9] |
| EvalResearchBench | Automating evaluation research | Oregon State, UCSD, Penn State, AG2 AI | 3 Oct 2026 | Agents design executable evaluations under three-hour, \$100 inference + \$100 pilot budgets; tested on sealed models and targets | Grok 4.7: 74.87% pairwise agreement; GPT-6 Astra highest score-concordance metric, 22.79 | Author-team evaluation | Target disagreement imposes about a 91% pairwise ceiling; no single universal winner | [https://arxiv.org/html/2610.04184v1](https://arxiv.org/html/2610.04184v1) [^34] |
| Lab R\&D acceleration assessment | Deployment/uplift method | METR at Anthropic | Report 5 Nov 2026; access 12 Aug–29 Oct | Internal progress, workflows and evidence of AI-driven acceleration | No leaderboard: estimated AECI progress rate 1.9× prior rate, 95% CI 1.5–2.8× | I, but high-access lab partnership | Not applicable; causal attribution remains a separate question | [https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/) [^35] |
| Research-acceleration telemetry | Deployment/uplift method | OpenAI | 6 Sept; update 18 Nov 2026 | Agent usage, delegated-task outcomes, code, experiments and internal capability trends | V: autonomous success 79% monitoring training, 35% launching training, 25% inference/serving code | V, internal measurements | Highly task-dependent; not a general autonomous-research score | [https://openai.com/index/research-acceleration-jagged-frontier/](https://openai.com/index/research-acceleration-jagged-frontier/) [^36] |

The particularly important PaperBench trap is that PaperBench Code-Dev is not full research replication. ARE-bench explicitly contrasts a reported 93.0% Code-Dev result with the untested requirements of execution and empirical reproduction. That is a construct distinction, not evidence that the full PaperBench benchmark is 93% solved.[^9]

## A3. Cybersecurity and safety-relevant agent capabilities

| Name | Category | Run by | Launched | Measures | Top score and holder | Vendor or independent | Headroom | Source URL |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| CyBench | Cyber capability | Stanford CRFM/RegLab researchers | 19 Aug 2024† | 40 professional CTF tasks; intermediate subtasks | Current independently run leader unverified | Original research-team runs; later lab results require separate labels | Current headroom unverified; old CTF performance is not vulnerability discovery | [https://cybench.github.io/](https://cybench.github.io/) [^37][^38] |
| CyberGym | Vulnerability reproduction | CyberGym/UC Berkeley team | 2025†; exact launch unverified | Reproduce real vulnerabilities from descriptions and code | TrendAI reports AESIR 97.0%, snapshot Aug 2026; primary benchmark execution details not verified here | V, specialized multi-model system using Opus 4.6 primarily | Nominal 3 points for that vendor claim; not a base-model ceiling | [https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/trendai-first-on-cybergym-top-exploit-benchmark](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/trendai-first-on-cybergym-top-exploit-benchmark) [^39] |
| ExploitGym | Full exploit development | CyberGym team | 2026; exact launch unverified | 869 vulnerabilities across userspace, V8 and Linux; intended-bug code execution | D: Mythos Preview 157 intended-bug successes; GPT-5.5 120. These are counts, not verified full-suite comparable rates | Benchmark-team presentation; trusted-access programs; subset coverage varies | Large; denominator must be checked per submission | [https://www.cybergym.io/exploitgym/](https://www.cybergym.io/exploitgym/) [^40] |
| ExploitBench / v8-bench v0.1 | Hardened exploitation | Seunghyun Lee, David Brumley; CMU/Bugcrowd affiliations | May–June 2026; exact launch day unverified | 41 V8 N-day bugs; ladder from reaching code through primitives to arbitrary execution with mitigations | Current leader unverified | Academic/vendor collaboration; Epoch separately reviewed benchmark | Large; ladder scores deliberately preserve partial progress | [https://exploitbench.ai/](https://exploitbench.ai/) [^41][^42][^43] |
| The Last Ones / AISI cyber ranges | Government cyber evaluation | UK AISI; joint work with US CAISI | Public range report 16 Mar 2026† | Multi-step intrusion in simulated corporate networks | 23 July report: leading US cyber-capable models average 28.5/32 steps; Kimi K3 17/32 under 100M-token limit. April report: Mythos Preview solved end-to-end 3/10 attempts† | I, government execution | Completion, average progress and repeatability remain distinct | [https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities](https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities) [^44][^45] |
| SandboxEscapeBench | Containment capability | UK AISI | 23 Mar 2026† | Container breakout using nested sandbox architecture | Current top score unverified | I, government | Unverified; includes multiple misconfiguration and exploit classes | [https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities](https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities) [^46][^47] |
| Multi-agent AI control evaluation | Distributed attacks on oversight | UK AISI research team | 8 July 2026 | Whether distributed agent attacks defeat per-instance monitors | No current scalar leaderboard verified | I, government research | Not applicable as a conventional leaderboard | [https://www.aisi.gov.uk/research](https://www.aisi.gov.uk/research) [^48] |
| Supply-chain attack propensity evaluation | Unauthorized behavior | UK AISI | 28 Sept 2026 | Unsanctioned supply-chain activity in simulations | Report says GPT-6 Astra does this more frequently than previous OpenAI models; exact rate unverified | I, government | A propensity measure, not a capability-completion percentage | [https://www.aisi.gov.uk/blog](https://www.aisi.gov.uk/blog) [^49][^48] |
| Embedded subversion/alignment assessments | Scheming and monitorability | Apollo, METR, Transluce, Goodfire | New OpenAI pilots 16 Nov 2026 | Training incentives, elicitable subversion, internal deployment behavior, detectable reasoning, quality of internal evals | No results yet for announced pilots | External assessors with materially different payment and access arrangements | Not a fixed-ceiling benchmark | [https://openai.com/index/our-first-phase-of-embedded-assessments/](https://openai.com/index/our-first-phase-of-embedded-assessments/) [^10] |
| Benchmark Reviews | Evaluation-of-evaluations | Epoch AI | Active by Aug 2026; exact launch day unverified | Reviewability, scoring errors, version consistency, elicitation and setup bias | No model score; verdicts Verified / Flawed / Not enough information | I for external benchmarks; excludes Epoch’s own benchmarks | Not applicable | [https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks](https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks) [^11] |

For a security audience, the most important taxonomy is: CTF solving → known-bug reproduction → exploit construction → autonomous discovery → end-to-end intrusion. These are different evaluation targets. ExploitGym explicitly demonstrates why even “captured the flag” can be a false positive for the intended skill: an agent may exploit a different bug.[^37][^40][^42]

## A4. Computer use, browsing, enterprise work and economics

| Name | Category | Run by | Launched | Measures | Top score and holder | Vendor or independent | Headroom | Source URL |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| BrowseComp | Persistent web research | OpenAI | 10 Apr 2025† | 1,266 hard-to-find, short-answer web questions | Current primary-source top holder unverified; excluded aggregator-only 92% claims | Original V; later M | Current headroom unverified; search leakage remains material | [https://openai.com/index/browsecomp/](https://openai.com/index/browsecomp/) [^50][^51] |
| BrowseComp-Plus | Reproducible retrieval research | Texttron research team | 8 Aug 2025† | BrowseComp-derived questions against approximately 100K fixed documents; retriever/model separation | Current primary-source leader unverified | Community submissions; provenance per row | Substantial; retriever setting must accompany score | [https://github.com/texttron/BrowseComp-Plus](https://github.com/texttron/BrowseComp-Plus) [^52] |
| WebArena-Verified | Browser task execution | WebArena-Verified maintainers; lab evaluations | Exact launch unverified | Browser interaction with web applications | OpenAI reports GPT-5.4 67.3%, DOM + screenshots; underlying result date unverified because localized launch page has misleading freshness metadata | V | 32.7 points on that configuration; not verified current leader | [https://openai.com/pa-IN/index/introducing-gpt-5-4/](https://openai.com/pa-IN/index/introducing-gpt-5-4/) [^53] |
| Online-Mind2Web | Live-web computer use | Mind2Web team; lab evaluations | 2025†; exact day unverified | Completion of live website tasks | OpenAI reports GPT-5.4 92.8%, screenshots only; current leader and original result date unverified | V | Nominal 7.2 points, configuration-specific | [https://openai.com/pa-IN/index/introducing-gpt-5-4/](https://openai.com/pa-IN/index/introducing-gpt-5-4/) [^53] |
| WorkArena / WorkArena++ | Enterprise browser workflows | ServiceNow Research | WorkArena Feb 2024†; ++ date unverified | ServiceNow tasks; 33 atomic task types and 682 composed tasks | Current leader unverified | Vendor-created benchmark; AgentLab/BrowserGym supports third-party execution | Unverified; atomic and composed results not interchangeable | [https://github.com/ServiceNow/WorkArena](https://github.com/ServiceNow/WorkArena) [^54] |
| BrowserGym / AgentLab | Standardized browser evaluation infrastructure | ServiceNow Research and collaborators | 2024† | Common browser action/observation interfaces and experiment management across benchmarks | No single top score | Open research infrastructure; commercial affiliation disclosed | Not applicable | [https://github.com/ServiceNow/BrowserGym](https://github.com/ServiceNow/BrowserGym) [^55][^56] |
| Gaia2 | Dynamic asynchronous agents | Meta ARE/Gaia2 researchers | ICLR 2026; exact initial release unverified | 800 scenarios plus augmentations; evolving environments, time constraints, noise, ambiguity and collaboration | Current leader unverified | Model-vendor research benchmark; later submissions require labels | Unverified | [https://proceedings.iclr.cc/paper_files/paper/2026/file/c26a67e0470774df98c12480ec5d2d7b-Paper-Conference.pdf](https://proceedings.iclr.cc/paper_files/paper/2026/file/c26a67e0470774df98c12480ec5d2d7b-Paper-Conference.pdf) [^57] |
| TheAgentCompany | Simulated employment | CMU-led author team | Dec 2024† | Work across code, chat, office systems and simulated colleagues | Current primary-source holder unverified; third-party catalogs disagree | M | Clearly not verified solved; exact current headroom unverified | [https://the-agent-company.com/](https://the-agent-company.com/) [^58][^59] |
| τ²-bench | Interactive customer service/reliability | Sierra | 2025†; exact day unverified | Policy-following, user interaction and tool-mediated service tasks; pass^k | Current official overall leader not verified in retrieved source | Sierra-run and external submissions | Must report domain and pass^k, not just an overall percentage | http://taubench.com/leaderboard/ [^60] |
| τ³-Banking | Enterprise knowledge/tool use | Sierra | 2026; exact launch unverified | Banking support with knowledge retrieval and tools | Official row dated 19 July 2026: Qwen 3.8 Max, 55.2%, xhigh, alltools, GPT-5.2 user simulator | Sierra benchmark result for another vendor’s model; full execution provenance not independently audited | 44.8 points on this track | http://taubench.com/leaderboard/ [^60] |
| MCP Atlas | Cross-server tool use | Scale Labs | 19 Sept 2025†; major harness update Apr 2026† | 1,000 tasks, 36 real MCP servers, 220 tools; claim-based pass scoring | D live comparison: Gemini 4 Argon 90.70 ±1.80; page’s prose/header contains older incompatible “top” values | I, Scale; some open-model inference via Fireworks | 9.3 points on live comparison, with source-staleness caveat | [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas) [^61][^62] |
| LHAW | Ambiguity and clarification | Scale Labs | 4 Nov 2026 | Underspecified variants of MCP Atlas, TheAgentCompany and SWE-bench Pro; 285 tasks | No single current overall leader verified | Benchmark-creator research | Substantial; compares ambiguity handling, not only execution | [https://labs.scale.com/blog/LHAW](https://labs.scale.com/blog/LHAW) [^63] |
| HiL-Bench | Human-in-the-loop judgment | Scale Labs | Exact launch unverified | Recognizing missing information and asking useful clarification questions | D: Fable 5.2 80.00 ±4.95, public set only; Muse Wonder 79.67 ±4.17 on separately labeled entry | I, Scale; unequal set labels prevent simple ranking claim | At least 20 nominal points; public/full splits must be separated | [https://labs.scale.com/leaderboard](https://labs.scale.com/leaderboard) [^16] |
| Multimodal Knowledge Agent, MKA | Visual knowledge work | Google DeepMind + Artificial Analysis | 10 Nov 2026 | 200 private expert tasks, 83 occupations, 3–8 human hours; visual files and deliverables; Stirrup harness | Google says Gemini 4 Carbon is \#2 and about 6× cheaper than leader; exact primary-source top score/holder unverified here | I execution by AA; co-designed with Google, so not institutionally unaffiliated | Significant; exact primary score unavailable | [https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/) [^64] |
| Epoch Automation Reports | Human-graded actual work | Epoch AI | Initial launch unverified; redesigned 17 Nov 2026 | Epoch’s design, analysis, data-center research and research tasks; employee-standard rubrics | Fable 5.2 / Claude Code 82% mean rubric score; highest reasoning setting | I; one run/task; humans grade; occasional interventions | 18 rubric points—not “82% of jobs automated” | [https://epoch.ai/benchmarks/epoch-automation-reports](https://epoch.ai/benchmarks/epoch-automation-reports) [^65] |
| Finance Agent v2/v2.1 | Financial analyst workflows | Vals AI | v2 launch unverified; v2.1 updated 18 Nov 2026 | Retrieval, analysis and modeling; severity weighting and dealbreaker gating | Current top score unverified | I, commercial evaluator | Unverified; a load-bearing factual error can zero a task | [https://www.vals.ai/home](https://www.vals.ai/home) [^66][^67] |
| Legal Research Bench | Tool-using legal research | Vals AI | Initial launch unverified; update 18 Nov 2026 | Case-law/web/document research; all-pass success | Gemini 4 Neon 56.25%, 18 Nov | I, Vals | 43.75 points under all-pass scoring | [https://www.vals.ai/benchmarks/legal_research](https://www.vals.ai/benchmarks/legal_research) [^68] |
| Immigration Bench | Current-policy professional work | Vals AI | Initial launch unverified; page publication 11 Sept 2026 | US immigration tasks, including recent policy | Fable 5.1 75.44%, as of 9 Nov | I, Vals | 24.56 points overall; recent-policy subgroup much weaker | [https://www.vals.ai/benchmarks/immigration](https://www.vals.ai/benchmarks/immigration) [^69] |

## A5. Science, formal proof, live evaluation, efficiency and non-US programs

| Name | Category | Run by | Launched | Measures | Top score and holder | Vendor or independent | Headroom | Source URL |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Autoform-Hard | Research mathematics in Lean | Vals AI; subset of Meta FAIR AutoformBench | 18 Nov 2026 | 56 previously unsolved formalization tasks; three hours/\$200; clean-room and independent-kernel checking | GPT-6.2 Astra 49/56; Sol and Fable 5.2 48/56 | I, Vals; one theorem separates top models | Seven tasks remain; about 12.5 points | [https://www.vals.ai/blogs/smoktunowicz-gap-theorem](https://www.vals.ai/blogs/smoktunowicz-gap-theorem) [^70][^71] |
| CritPt v2 | Research-level physics | Argonne/UIUC-led physics researchers; AA also runs it | Original public debut 21 Nov 2025†; v2 date unverified | 70 test challenges; multi-step research physics | Creator board D: GPT-6 Astra 83.1%, five runs ×70. AA has a distinct private 40-question hard subset with code execution | Creator-run result; independent AA variant is separate | 16.9 points on creator’s full test set | [https://github.com/CritPt-Benchmark/CritPt](https://github.com/CritPt-Benchmark/CritPt) [^72][^73][^74] |
| SciCode | Scientific programming | SciCode researchers; AA evaluation | Exact launch unverified | 288 test subproblems from 80 laboratory problems across 16 disciplines | Epoch D lists highest subproblem score 68%; holder unverified | AA-executed results sourced by Epoch | At least 32 subproblem points; not full-problem success | [https://epoch.ai/benchmarks/scicode](https://epoch.ai/benchmarks/scicode) [^75][^73] |
| FrontierScience | Expert science reasoning | OpenAI | 16 Dec 2025† | Physics, chemistry and biology reasoning | Current top score unverified | V for original results | Unverified | [https://openai.com/index/frontierscience/](https://openai.com/index/frontierscience/) [^76] |
| SciWorkBench | Scientific workflows | SciWorkBench author team | 17 Nov 2026 | Biology, chemistry, materials and physics; evidence-grounded experimental-science workflows | Top score not verified | Author-team evaluation | Unverified; very new preprint | [https://arxiv.org/html/2611.22490](https://arxiv.org/html/2611.22490) [^77] |
| DrugDiscoveryBench | Scientific coding | Scale Labs | Exact launch unverified | 82 computational early-stage drug-discovery tasks | D: Gemini 4 Carbon high / mini-SWE-agent, 71.50 ±2.10 | I, Scale | 28.5 nominal points | [https://labs.scale.com/leaderboard](https://labs.scale.com/leaderboard) [^16] |
| LiveBench 2.0 | Live cross-domain work/efficiency | LiveBench; sponsored by Abacus.AI | 6 Nov 2026 | Long-agentic, coding, browser, research, design and analysis suites; cost/successful task | D: Fable 5.2 xhigh and GPT-6.2 Astra tied at 84.9; respective costs/success \$9.850 and \$1.941 | Benchmark-run, commercial sponsorship; one run/suite | 15.1 aggregate points; large category differences; page date inconsistency noted below | [https://livebench.ai/](https://livebench.ai/) [^78] |
| LiveCodeBench | Refreshing competitive coding | LiveCodeBench researchers | 2024† | Contest code generation, repair, execution and output prediction | Official retrieved default window: o4-mini high 80.2%, 454 problems, Aug 2024–May 2025†. Vals’ separate run: Fable 5.1 90.52%, 1 Sept 2026 | Official I historical board; I separate Vals implementation | Cannot combine windows/harnesses; official visible board is stale | [https://livecodebench.github.io/leaderboard.html](https://livecodebench.github.io/leaderboard.html) [^79][^80][^81] |
| Agent Arena | Deployment/arena-style evaluation | Arena | Exact launch unverified; board dated 23 Oct 2026 | Real agent sessions; inferred success, satisfaction, steerability, shell reliability, hallucinated tools, cost | D overview: Opus 5.5 max 20.94% net-improvement metric; not a 20.94% task-completion rate | Platform-observed; not vendor self-report, but not randomized controlled benchmark | No natural fixed ceiling for relative improvement metric | [https://arena.ai/leaderboard/agent](https://arena.ai/leaderboard/agent) [^82][^83] |
| Arena WebDev | Human preference on app building | Arena | Exact launch unverified; coding page 9 Oct 2026 | Developer votes on front-end builds/apps | Current leader/score unverified | Platform human comparisons | Elo/preference has no fixed “100% solved” ceiling | [https://arena.ai/leaderboard/code](https://arena.ai/leaderboard/code) [^84] |
| ForecastBench | Forecasting and calibration | ForecastBench research team | 2024†; tournament opened Jan 2026 | Future events; market and dataset questions; human comparisons; Brier Index | Current primary-source leader unverified; 16 July report says likely parity with superforecasters | Benchmark team plus open tournament submissions | No simple percentage ceiling; resolution timing and track matter | [https://www.forecastbench.org/about/](https://www.forecastbench.org/about/) [^85][^86] |
| ForecastBench-Sim | Fast-resolving forecasting | ForecastBench-Sim author team | 17 June 2026 | Hidden future states in Freeciv simulations; Brier/CRPS across horizons | No definitive frontier ranking claimed | Author-team research | Measures calibration and horizon effects, not task autonomy | [https://arxiv.org/html/2606.18686](https://arxiv.org/html/2606.18686) [^87] |
| Vals Inference Provider Index | Provider fidelity/cost/reliability | Vals AI | Original launch unverified; page dated Oct/Nov 2026 ambiguously | Same open-weight model across providers; task accuracy, cost and speed | No single universal winner. Example dated 7 Nov: DeepSeek V4.1 Flash/Together 67.8% ±3.2 pp SE, \$0.497/task | I, Vals | Task/provider dependent | [https://www.vals.ai/benchmarks/inference_provider](https://www.vals.ai/benchmarks/inference_provider) [^88] |
| Vals Router Index | End-to-end routing efficiency | Vals AI | Active by 19 Nov; exact launch unverified | Model routers on the same agents, tasks and graders as single models | Current top score unverified | I, commercial evaluator | Quality/cost/latency frontier, not one ceiling | [https://www.vals.ai/home](https://www.vals.ai/home) [^66] |
| Harbor / Harbor-Index | Standardized agent evaluation | Harbor author team | Paper 3 Sept 2026 | Adapters and curated multi-benchmark execution; comparable agent configurations | No single frontier winner verified | Research infrastructure | Not applicable | [https://arxiv.org/html/2609.04298v1](https://arxiv.org/html/2609.04298v1) [^20] |
| optstop | Statistical evaluation efficiency | UK AISI | Paper 14 Aug; tool 27 Aug 2026 | Adaptive allocation of runs; stop when estimates precise/stable enough | No model leaderboard | I, government methodology | Reduces evaluation cost for specified precision | [https://www.aisi.gov.uk/blog/optimal-stopping-spending-evaluation-compute-where-it-counts](https://www.aisi.gov.uk/blog/optimal-stopping-spending-evaluation-compute-where-it-counts) [^89] |
| Transect | Long-trajectory observability | UK AISI | 7 Oct 2026 | Navigation, inspection and interpretation of long agent transcripts | No model leaderboard | I, government methodology | Not applicable | [https://www.aisi.gov.uk/category/science-of-evaluations](https://www.aisi.gov.uk/category/science-of-evaluations) [^90] |
| OpenCompass / CompassBench v3 | Chinese/global capability suite | Shanghai AI Laboratory/OpenCompass | Platform predates 2026†; v3 current Oct 2026 | Knowledge, reasoning, interaction, safety and agents; private and academic tracks | Text-only board, 29 Oct: Kimi K3.1 Pro max 78.47; agent dimension 72.53. Not the all-benchmark overall winner | Benchmark-team evaluation; lab also develops models, so not institutionally unaffiliated | 21.53 text-only aggregate points; score composition matters | [https://rank.opencompass.org.cn/](https://rank.opencompass.org.cn/) [^91][^92] |
| MedBench v5 | Chinese clinical/agent evaluation | MedBench/OpenCompass researchers | June 2026 paper | Dynamic, process-oriented medical multimodality; tools, research, RAG and multi-agent capabilities | Current top score unverified | Research/platform run; affiliations should accompany claims | Unverified | [https://medbench.opencompass.org.cn/](https://medbench.opencompass.org.cn/) [^93] |
| SG-LegalClarify | Non-US legal reasoning | Scale + Singapore IMDA | 12 Nov 2026 | Singapore-law reasoning and recognition of ambiguity | Current top score unverified | Joint commercial/government benchmark | Unverified | [https://scale.com/blog/scale-imda-legal-reasoning-benchmark](https://scale.com/blog/scale-imda-legal-reasoning-benchmark) [^94] |

### Important coverage gaps—not verified findings

I would not put current numerical claims for miniF2F, ProofNet, PutnamBench, LAB-Bench, government biological uplift studies, or newer sandbagging datasets into your slides based on this research alone. Their relevance is credible, but I did not verify current, version-pinned primary-source standings.

Likewise, I found secondary claims about OmnilingualGAIA2, newer privacy-review datasets and new auditing benchmarks, but did not verify their underlying primary artifacts sufficiently to promote them into the main table. For example, the claimed OmnilingualGAIA2 release and cross-language gap currently remain unverified in this survey.[^95]

# B. Changes in the last 60 days to things you already cover

| Item | Dated change | What should change in your lecture | Evidence/provenance |
| :-- | :-- | :-- | :-- |
| ARC-AGI-3 | Epoch review, 30 Oct 2026 | Add a serious construct-validity qualification: headline score combines completion with squared relative action efficiency; standard/provider harnesses produce radically different outcomes | Epoch review reports GPT-6 Astra max 62.7% Standard versus 98.6% Provider Adapter, drawing on ARC/OpenAI publications—not an Epoch rerun. [^96] |
| ARC-AGI-3 | Competition closed 2 Nov; results due 4 Dec | Separate semi-private public leaderboard results from fully private competition results | ARC’s official calendar. [^97][^98] |
| OSWorld 2.1 | Epoch “Flawed,” 28 Sept | Do not present “current” as equivalent to “validated”; inspect the version-specific review before using score changes | Review registry; detailed causal grounds not verified here. [^11] |
| Vending-Bench 2 | Epoch “Flawed,” 21 Oct | Add a validity flag; rating is not evidence that all vendor results are false | Review registry. [^11] |
| Remote Labor Index | Epoch “Not enough info,” 12 Oct; live board retrieved 19 Nov | Scale now lists Fable 5.2 41.25 versus Opus 5.5 21.25 and GPT-6 Astra 20.83; latest exact publication date/harness not verified | Benchmark-owner live board, not a new independent replication. Avoid plotting as a clean model-only time series. [^11][^16] |
| FrontierCode 2.0 | Epoch “Not enough info,” 11 Nov | Qualify external auditability separately from reported performance | Review registry. [^11] |
| Humanity’s Last Exam | HLE-Diamond introduced in AA v5, 28 Oct | Treat as a replacement dataset/track, not an improved score on unchanged HLE; 1,000 refined questions | AA announcement: half reasoning, half knowledge. [^74] |
| Artificial Analysis Intelligence Index v5 | 28 Oct | 60% now uses private test sets or held-out answers; adds Terminal-Bench-Science and introduces a separate Progress Index | AA primary announcement. [^74] |
| Epoch Capabilities Index | 4 Nov | Bayesian model replaces previous estimation approach, changing uncertainty treatment and model comparisons | Epoch benchmark news; 9 Nov Fable 5.2 result explicitly based initially only on Epoch-run benchmarks. [^99] |
| METR methods beyond frozen horizon page | 22 Oct monitoring exercise; 5 Nov Anthropic assessment; 16 Nov OpenAI pilots | METR has not stopped measuring agents; focus is broadening toward internal monitoring, alignment and R\&D acceleration | OpenAI’s primary announcement identifies the 22 Oct METR exercise; METR published the Anthropic assessment. [^10][^35] |

I did not verify additional last-60-day changes to your listed Terminal-Bench versions, FrontierSWE v2, GDPval variants, DeepSWE or FrontierMath that I would confidently add here. Their omission is not a claim of no change.

# C. Who is doing the measuring

“Independent” should be decomposed into independent execution, organizational independence, financial independence, and freedom to publish. These are not synonymous.


| Evaluator | Significant publication/activity since July 2026 | Independence and relationship notes |
| :-- | :-- | :-- |
| METR | 21 July: expenditure horizon; 22 Oct: OpenAI monitor red-teaming; 5 Nov: high-access Anthropic R\&D acceleration assessment; 16 Nov: OpenAI alignment/monitor pilots announced | OpenAI says METR accepts no assessment fee, but may accept compute/API credits. High access improves evidence while creating scope/disclosure dependencies. Complete current donor breakdown unverified here. [^100][^10][^35] |
| Epoch AI | Benchmark Reviews Aug–Nov; 4 Nov Bayesian ECI update; 17 Nov redesigned Automation Reports | Transparency page lists October 2026 Coefficient Giving support of \$22.73M, July compute support of \$600K, and lab contracts/collaborations including OpenAI and Google. Epoch excludes its own benchmarks from its review program. [^101][^11][^99][^65] |
| Artificial Analysis | 28 Oct Intelligence Index v5 and Progress Index; 10 Nov MKA with Google | Independently executes many evaluations, but MKA is explicitly co-developed with a model vendor. Do not label that benchmark “no lab involvement.” Complete current ownership/funding inventory unverified. [^74][^64] |
| ARC Prize Foundation | 2026 competition; September milestone; December final results forthcoming | Benchmark creator and competition organizer, not merely a third-party tester. Current funder/lab-relationship inventory unverified. [^97] |
| Scale Labs / SEAL | 28 July SWE Atlas test-writing update; Nov SWE Atlas v1.1; 3 Nov MCP paper; 4 Nov LHAW; 12 Nov SG-LegalClarify | Commercial training/evaluation supplier with model-lab and government relationships; not institutionally disinterested. Retrieved primary material did not establish the complete current ownership/funding picture. [^102][^4][^103][^63][^94] |
| Center for AI Safety | 1 July RLI update; 29 July wage-loss dashboard; live capability dashboard | RLI jointly developed with Scale. Wage-loss dashboard is economic interpretation, not a model capability benchmark or causal labor-market study. Full late-2026 funding inventory unverified. [^104][^105][^106] |
| Apollo Research | 21 July reward-seeking study; 29–30 Sept embedded-evaluation principles; 1 Oct scheming framework; 15 Oct GLM-5.3 behavior study; 16 Nov OpenAI pilot | Six evaluators/four months in announced pilot. Paid by OpenAI, compensation not contingent on findings. Scope/access limitations remain material. [^107][^108][^109][^10] |
| Transluce | 4 Nov evaluation-related publication listed; 16 Nov embedded OpenAI assessment announcement | Six-week pilot; selected models, raw reasoning access and internal evals. No assessment fee, possible compute support; editorial control with restrictions. Research index and article disagree on announcement date—see E. [^110][^111][^10] |
| Vals AI | Sept–Nov professional benchmarks; provider/router evaluation; 18 Nov Autoform-Hard; 19 Nov RollerCoasterTycoonBench announcement | Commercial evaluator. Disclosed NIST benchmark/data collaboration on 28 July and NIST consortium participation on 12 Nov. Full investor/revenue concentration unverified. [^67][^88][^66][^70][^112] |
| UK AISI | July cyber comparisons; Aug optstop and incident disclosure; Sept supply-chain propensity; Oct Transect, security hardening, incident investigation and ReproBAIT | Public institution; government independence from vendors does not make test sets fully public. Particularly valuable for cyber ranges and evaluation security. [^49][^48][^113] |
| US CAISI | Joint Kimi K3 cyber assessment, 23 July | Joint government evaluation verified. A complete standalone list of CAISI publications since July was not verified; do not substitute press reports for that inventory. [^44] |
| Goodfire | 16 Nov embedded assessment agreement | Commercial interpretability company, paid by OpenAI for this engagement; primary audience initially internal researchers, with public findings planned. [^10] |
| Abundant AI / BenchFlow contributors | June SWE-Marathon paper; current v1.1 benchmark and runs | Abundant says it ran all listed evaluations except Z.ai’s GLM entries. This is unusually helpful row-level provenance. Funding unverified. [^5] |
| Arena | Agent session rankings Oct; \$200M Series B announced 8 Oct | Commercial platform with actual-user data and different selection biases from controlled tests. Funding announcement verified, full investor/conflict details not audited here. [^82][^83] |
| ForecastBench team | Tournament opened Jan; 16 July superforecaster-parity analysis | Distinguishes controlled baselines from externally enhanced tournament systems. Funding inventory unverified. [^85][^86] |
| Tübingen/ELLIS/Max Planck/Thoughtful Lab PostTrainBench team | 28 July v1.1; 17 Sept response to Epoch review; 30 Sept v1.2; 12 Nov model additions | Academic-led, with external submissions explicitly labeled. Strong example of a benchmark maintaining an evolving compliance policy. [^32] |
| OpenCompass / Shanghai AI Laboratory | October 2026 v3 results | Significant non-US measurement infrastructure, including private benchmarks and arena tracks. The institution also develops models; assess institutional and row-level conflicts separately. [^91][^92] |
| Singapore AISI/IMDA, Canada AISI, France INESIA | July international evaluation-methods contributions; IMDA/Scale benchmark 12 Nov | July network report identifies Singapore’s systems-testing guidance, Canada’s selective-disclosure discussion and France’s decision-relevance framework. These are not interchangeable public model leaderboards. [^113][^94] |

For EU coverage specifically, I verified France’s INESIA participation and Epoch’s 2026 technical consultations with the EU AI Office. I did not verify a comprehensive EU-wide late-2026 frontier-agent leaderboard or an announced release calendar for one.[^101][^113]

# D. Methodological debates

### 1. Private testing versus public auditability

The late-2026 shift is toward private tasks, held-out answers and separate public demonstration sets. AA’s 28 October v5 announcement says 60% of its index now rests on private datasets or held-out answers. MKA keeps 200 scored tasks private while releasing ten examples; MirrorCode releases 22 targets and retains three private ones. The opposing concern is reviewability: Epoch’s registry marks several consequential benchmarks “Not enough information,” explicitly distinguishing insufficient access from demonstrated invalidity. Privacy reduces one failure mode while potentially weakening external error detection.[^64][^74][^7][^11]

### 2. Benchmark scores now need a configuration identity

The important shift is from reporting “model X scored Y” to reporting a system configuration: model, reasoning setting, harness, tool surface, network rules, compaction, budget and judge. SWE Atlas v1.1 reruns all models with a new judge and restricted networking; its scores are not directly comparable with v1.0. MirrorCode’s current leaderboard differs from its paper in task selection, languages and expenditure. MCP Atlas’s April update changed judge, retries and the budget from 20 turns to 100 tool calls. Versioning the task set alone is insufficient.[^61][^4][^7]

### 3. Capability ceilings and economically useful performance are different questions

AISI’s 2 July methods article argues that larger inference budgets change apparent capability and apparent progress rates. MirrorCode’s seven-day/10B-token allowance explores what agents can eventually accomplish; SWE-rebench and Vals emphasize cost and task-level efficiency; LiveBench 2.0 explicitly publishes cost per successful task. Neither max-elicitation nor fixed-budget evaluation should replace the other. For your lecture, show a success–cost curve or Pareto frontier before presenting a single “best model.”[^78][^88][^90][^1][^7]

### 4. Passing the final check is no longer enough

LoopsBench keeps earlier completed work alive as regression obligations. ARE-bench finds that partial checklist scores can look strong while strict full-delivery success remains much lower; it also shows that checking only the immediate deliverable hides failures to preserve research history and workspace constraints. Vals Finance Agent’s dealbreaker gating similarly rejects “mostly right” answers with a load-bearing error. This is a move toward evaluating whether the whole contract holds, not whether the artifact contains enough individually correct components.[^6][^66][^9]

### 5. Cheating policies are becoming part of benchmark design

The newer policies are operational rather than just exhortative. SWE-bench-Live requires trajectories to check that ground-truth fields were not exposed. PostTrainBench prohibits deriving synthetic training examples from specific test items, even without verbatim overlap; it uses majority-of-three contamination judgments, model-identity checks and reruns. ExploitGym counts only exploitation through the intended vulnerability. MirrorCode moves submissions into a separate scoring sandbox. These decisions define what the benchmark is measuring and can materially change rankings.[^2][^32][^40][^7]

### 6. Reliability needs repeated runs—and a specified event

SWE-Marathon runs eight trials per task; ARE-bench reports three-round means and standard deviations; CritPt uses five runs across 70 challenges. AISI’s optstop addresses the cost of obtaining sufficiently precise estimates. But pass@k—success at least once—and pass^k—success consistently across repeated attempts—answer different questions. “Number of nines” claims are especially weak unless they identify the failure event, workload distribution, dependence between failures and confidence interval. I did not verify a broadly accepted late-2026 cross-agent “nines” standard; the evidence supports better repeated-run reporting, not a settled reliability certification regime.[^5][^60][^72][^89][^9]

### 7. Human baselines are an assumption to audit, not a universal conversion factor

MirrorCode’s preliminary “weeks-long” interpretation used expert estimates; the authors explicitly said long-task human baselines were not yet available. RE-Bench’s controlled comparison demonstrates that relative performance depends strongly on time budget. Epoch’s ARC-AGI-3 review shows another issue: a baseline built from successful human players does not imply an average human scores 100. Your students should distinguish measured completion time, expert-estimated time, successful-subject baselines and a professional acceptance standard.[^28][^96][^114]

### 8. Deployment evidence is complementing—not yet replacing—benchmarks

OpenAI’s 18 November research-acceleration report uses delegated-task outcomes, usage and internal capability trends; METR’s 5 November assessment examines internal Anthropic evidence with unusually deep access. Arena measures actual agent sessions. These offer stronger ecological relevance but introduce selection effects, changing workflows, attribution problems and private instrumentation. OpenAI explicitly cautions that historical metrics involving human–AI collaboration may not predict future AI-driven progress. The emerging alternative is triangulation: controlled tasks, actual-work acceptance, deployment telemetry and intervention/uplift studies—not “revenue proves intelligence.”[^35][^36][^83]

## Successors and replacements: direct answers

### Has METR’s horizon series been replaced?

No direct replacement was verified.

The meaningful alternatives are:

- MirrorCode: whole-program scope under long budgets.
- SWE-Marathon: hard multi-hour engineering completion with repeated trials.
- LoopsBench: sustained dependency-aware development and regression control.
- AISI cyber horizons: domain-specific autonomous cyber-task duration.
- Actual-work studies: whether people or organizations obtain useful output with less effort.

These are complementary measures. None entitles you to say “agents can now work unattended for N weeks” without specifying human-time estimation, actual runtime, intervention rules and reliability.[^65][^115][^5][^6][^7]

### Is there an accepted SWE-bench Verified successor?

I found no evidence of consensus around one.

My interpretation is that the successor is becoming a measurement portfolio: freshness, creation, maintenance, long-running execution and professional acceptance. The fact that the official SWE-bench site now highlights ProgramBench and CodeClash, while other groups advance SWE Atlas, live issue sets and marathon tasks, supports fragmentation rather than a single coronation.[^3][^2][^4][^5]

# E. Contradictions, disputes and misleading comparisons

| Issue | Source/account A | Source/account B | Assessment |
| :-- | :-- | :-- | :-- |
| ARC-AGI-3 validity | ARC presents it as an agentic-intelligence benchmark | Epoch, 30 Oct, rates it Flawed, citing scoring, human baseline, elicitation, versioning and setup issues | Substantive methodological disagreement. Do not equate 98.6% with “98.6% of human intelligence.” No formal ARC rebuttal verified here. [^116][^96] |
| MCP Atlas current leader | Same page’s header says 83.6%; prose says Opus 4.5 leads at 62.3% | Live comparison on that page says Gemini 4 Argon 90.70 ±1.80 | Internal source inconsistency, probably stale prose, not evidence of replication failure. Cite the exact table and retrieval date. [^61] |
| PostTrainBench version composition | Header, footnotes and setup still say seven benchmarks including BFCL | 30 Sept changelog says v1.2 dropped BFCL and reweighted six | Primary page is internally inconsistent. Pin result version and inspect underlying data before plotting. [^32] |
| SWE-Marathon frontier | June paper: no configuration exceeds 30% | Current v1.1: Gemini 4 Carbon/Antigravity 53.8% | Not a contradiction after accounting for version, newer systems and evaluation changes. Aggregator snapshots still quoting 29% are stale. [^117][^5][^118] |
| LiveCodeBench leader | Official retrieved board: o4-mini high 80.2% on historical window | Vals: Fable 5.1 90.52% on its implementation | Different runs/windows, not a verified disagreement about one experiment. Generic “LiveCodeBench SOTA” is underspecified. [^79][^81] |
| SWE-rebench leader | Official retrieved window: Fable 5 high 64.5% | Aggregator, 18 Nov: Opus 4.6 65.3% | Aggregator-only “current” account is not accepted here; windows/configuration may differ. No basis for claiming a genuine model regression. [^1][^119] |
| ExploitGym apparent success | Flag captures: GPT-5.5 210, Mythos Preview 226 | Intended-vulnerability successes: 120 and 157 | Same experiments, different success definition. Flag-only scoring materially overstates the target capability. [^40] |
| RLI Fable 5 score | CAIS technical post, 1 July: 15.8% | CAIS newsletter, 6 July: 16.1% | Small unresolved primary-source discrepancy. Prefer the technical post for that historical snapshot; do not silently average. [^104][^120] |
| Embedded evaluations are “independent” | OpenAI, 16 Nov, emphasizes independent assessment and publication | Transluce discloses selected access and publication restrictions; critical coverage questions independence | Facts are partly shared; disagreement concerns adequacy. Independence is conditional, not absent or absolute. [^10][^111][^121] |
| Rate of AI progress | METR’s Anthropic assessment estimates 1.9× acceleration relative to that lab’s historical AECI trend | OpenAI reports OECI growth 16.4 points/year versus Epoch’s cited 14-point broader trend | Not commensurate growth estimates: different labs, indices, periods and interventions. Neither establishes a universal doubling law. [^35][^36] |
| LiveBench chronology | Page says latest update 11 Nov | Retrieved table includes GPT-6.2 models released later | Page metadata does not reliably timestamp individual rows. Use retrieval date, not “11 Nov result,” for those entries. [^78][^122] |
| Transluce announcement date | Research index labels announcement 13 Nov | Actual article says published 16 Nov | Prefer article date; chronology on index is inconsistent. [^110][^111] |

An especially useful lecture slide would place these in three columns: genuine validity dispute, different experimental conditions, and stale/inconsistent publication. Most apparent “benchmark contradictions” are not the same kind of problem.

# F. Calendar: next six months

Only one exact public results date was verified. Other entries are announced windows or project durations, not guaranteed publication deadlines.


| Date/window | Expected item | Certainty |
| :-- | :-- | :-- |
| 4 Dec 2026 | ARC Prize 2026 results: ARC-AGI-2, ARC-AGI-3 and paper tracks | Confirmed official announcement date; organizers reserve timeline changes. [^97][^98] |
| Approximately late Dec 2026–Jan 2027 | Completion window for Transluce’s six-week OpenAI pilot, depending on actual start | Duration announced 16 Nov; start/end and report-publication dates unverified. Do not calendar as a guaranteed release. [^111] |
| Early 2027 | Intended broader Transluce/OpenAI follow-on assessment, approximately eight weeks | Announced intent; agreement/details not finalized in Transluce’s announcement. [^111][^10] |
| Approximately March 2027, if started near announcement | End of Apollo’s four-month embedded pilot | Four-month duration announced 16 Nov; exact start/end/report date unverified. [^109] |
| Through 19 May 2027 | Further METR alignment/monitor assessments and Goodfire findings | Programs announced, but no verified fixed publication dates. [^10] |

I would not add speculative benchmark releases, expected model launches or routine leaderboard refreshes as “announced forthcoming results.”

# G. My judgment: the five things most likely to matter for a coding lecture a year from now

### 1. LoopsBench’s evaluation of persistent obligations

The important idea is not its current 25% score. It is measuring whether an agent can keep previous work correct while building dependent functionality. That is closer to a semester project, a multi-sprint product change or a repository migration than isolated issue resolution. Even if LoopsBench itself does not become dominant, regression-aware, stateful evaluation is likely to persist. This is my forecast, grounded in its task design rather than an adoption claim.[^6]

### 2. ProgramBench and SWE-Marathon’s move from patches to products

The lecture question will increasingly become “Can it deliver a substantial functioning system?” rather than “Can it reproduce this patch?” ProgramBench’s low full-resolution rate and SWE-Marathon’s unsolved product-clone tasks preserve useful headroom while exposing the gap between impressive demos and complete implementations. Their scores should remain separate because their tasks and harnesses differ.[^14][^5]

### 3. ARE-bench’s project-continuation model

Real engineering rarely begins in a clean directory with a perfect standalone prompt. ARE-bench makes inherited decisions, failed experiments, unfinished files and scientific meaning part of the acceptance contract. Its gap between checklist completion and strict delivery is an excellent teaching example of why “mostly correct” is not necessarily delegable. I expect this design pattern to spread beyond research assistants into enterprise coding evaluations.[^9]

### 4. PostTrainBench and direct measurement of AI R\&D

Agentic coding matters especially when the code improves the next generation of models. PostTrainBench measures a constrained version of that loop; METR’s internal assessment and OpenAI’s telemetry examine whether such assistance changes actual lab throughput. Teach these together, while separating autonomous task performance, human–AI uplift and evidence of accelerated model progress. They are related but not equivalent.[^32][^36][^35]

### 5. Evaluation integrity as an engineering discipline

Trajectory audits, clean-room proof replay, held-out tests, intended-vulnerability checks and embedded monitor assessments are becoming part of the measurement apparatus. A future frontier coding result is increasingly a security-sensitive experiment: the evaluated system can inspect, manipulate or route around parts of its environment. Students should learn to audit the evaluator—not merely read the leaderboard.[^40][^70][^2][^10]

## Conclusion

The strongest update to your lecture is a change in organizing principle:

> Evaluate what the agent can deliver, what it must preserve, how consistently it succeeds, what supervision and expenditure it needs, and whether the measurement itself survives adversarial behavior.

That framing accommodates the rapidly changing benchmark names without pretending that one percentage measures autonomous software engineering. The late-2026 evidence supports a broadening evaluation portfolio—not a clean succession from one saturated benchmark to the next.[^5][^10][^11][^6][^9]

<span style="display:none">[^123][^124][^125][^126][^127][^128][^129][^130][^131][^132][^133][^134][^135][^136][^137][^138][^139][^140][^141][^142][^143][^144][^145][^146][^147][^148][^149][^150][^151][^152][^153][^154][^155][^156][^157][^158][^159][^160][^161][^162][^163][^164][^165][^166][^167][^168][^169][^170][^171][^172][^173][^174][^175][^176][^177][^178][^179][^180][^181][^182][^183][^184][^185][^186][^187][^188][^189][^190][^191][^192][^193][^194][^195][^196][^197][^198][^199][^200][^201][^202][^203][^204][^205][^206][^207][^208][^209][^210][^211][^212][^213][^214][^215][^216][^217][^218][^219][^220][^221][^222][^223][^224][^225][^226][^227][^228][^229][^230][^231][^232][^233][^234][^235][^236][^237][^238][^239][^240][^241][^242][^243][^244][^245][^246][^247][^248][^249][^250][^251][^252][^253][^254][^255][^256][^257][^258][^259][^260][^261][^262][^263][^264][^265][^266][^267][^268][^269][^270][^271][^272][^273][^274][^275][^276][^277][^278][^279][^280][^281][^282][^283][^284][^285][^286][^287][^288][^289][^290][^291][^292][^293][^294][^295][^296][^297][^298][^299][^300][^301][^302][^303][^304][^305][^306][^307][^308][^309][^310][^311][^312][^313][^314][^315][^316][^317][^318][^319][^320][^321][^322][^323][^324][^325][^326][^327][^328][^329][^330][^331][^332][^333][^334][^335][^336][^337][^338][^339][^340][^341][^342][^343][^344][^345][^346][^347][^348][^349][^350][^351][^352][^353][^354]</span>

<div align="center">⁂</div>

[^1]: https://swe-rebench.com/

[^2]: https://swe-bench-live.github.io/

[^3]: https://www.swebench.com/

[^4]: https://github.com/scaleapi/swe-atlas

[^5]: https://www.swe-marathon.org/

[^6]: https://arxiv.org/html/2608.00267v1

[^7]: https://epoch.ai/benchmarks/mirrorcode

[^8]: https://metr.org/time-horizons/

[^9]: https://arxiv.org/html/2611.14364

[^10]: https://openai.com/index/our-first-phase-of-embedded-assessments/

[^11]: https://epoch.ai/data/benchmark-reviews-documentation/included-benchmarks

[^12]: https://swe-rebench.com/about

[^13]: https://arxiv.org/html/2505.23419

[^14]: https://www.vals.ai/benchmarks/programbench

[^15]: https://arxiv.org/html/2605.08366v1

[^16]: https://labs.scale.com/leaderboard

[^17]: https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/

[^18]: https://macroscope.com/content/ai-code-review-benchmark-best-models

[^19]: https://arxiv.org/html/2609.28850v1

[^20]: https://arxiv.org/html/2609.04298v1

[^21]: https://cooperbench.com/

[^22]: https://proceedings.colm.cc/paper_files/paper/2026/file/12a986b35a1d331e84caec382b58e329-Paper-Conference.pdf

[^23]: https://github.com/cooperbench/CooperBench

[^24]: https://icml.cc/virtual/2026/82786

[^25]: https://arxiv.org/html/2606.17799v1

[^26]: https://arxiv.org/abs/2410.07095

[^27]: https://arxiv.org/html/2604.13018v1

[^28]: https://arxiv.org/abs/2411.15114

[^29]: https://arxiv.org/abs/2504.01848

[^30]: https://epoch.ai/MirrorCode

[^31]: https://epoch.ai/benchmarks/search

[^32]: https://posttrainbench.com/index.html

[^33]: https://epoch.ai/benchmarks/weirdml-v3

[^34]: https://arxiv.org/html/2610.04184v1

[^35]: https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/

[^36]: https://openai.com/index/research-acceleration-jagged-frontier/

[^37]: https://crfm.stanford.edu/2024/08/19/cybench.html

[^38]: https://cybench.github.io/

[^39]: https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/trendai-first-on-cybergym-top-exploit-benchmark

[^40]: https://www.cybergym.io/exploitgym/

[^41]: https://exploitbench.ai/

[^42]: https://epoch.ai/benchmarks/exploitbench

[^43]: https://www.anthropic.com/research/exploit-evals

[^44]: https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities

[^45]: https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities

[^46]: https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities

[^47]: https://www.aisi.gov.uk/research/quantifying-frontier-llm-capabilities-for-container-sandbox-escape

[^48]: https://www.aisi.gov.uk/research

[^49]: https://www.aisi.gov.uk/blog

[^50]: https://openai.com/index/browsecomp/

[^51]: https://www.anthropic.com/research/eval-awareness-browsecomp

[^52]: https://github.com/texttron/BrowseComp-Plus

[^53]: https://openai.com/pa-IN/index/introducing-gpt-5-4/

[^54]: https://github.com/ServiceNow/WorkArena

[^55]: https://github.com/ServiceNow/BrowserGym

[^56]: https://www.servicenow.com/research/fr/publication/alexandre-lacoste-an-e-mais2024.html

[^57]: https://proceedings.iclr.cc/paper_files/paper/2026/file/c26a67e0470774df98c12480ec5d2d7b-Paper-Conference.pdf

[^58]: https://the-agent-company.com/

[^59]: https://epoch.ai/benchmarks/the-agent-company

[^60]: http://taubench.com/leaderboard/

[^61]: https://labs.scale.com/leaderboard/mcp_atlas

[^62]: https://scale.com/blog/mcp-atlas

[^63]: https://labs.scale.com/blog/LHAW

[^64]: https://blog.google/innovation-and-ai/models-and-research/gemini-models/multimodal-knowledge-agent-benchmark/

[^65]: https://epoch.ai/benchmarks/epoch-automation-reports

[^66]: https://www.vals.ai/home

[^67]: https://www.vals.ai/gov

[^68]: https://www.vals.ai/benchmarks/legal_research

[^69]: https://www.vals.ai/benchmarks/immigration

[^70]: https://www.vals.ai/blogs/smoktunowicz-gap-theorem

[^71]: https://x.com/ValsAI/status/2123129588066959380

[^72]: https://github.com/CritPt-Benchmark/CritPt

[^73]: https://artificialanalysis.ai/evaluations/critpt

[^74]: https://x.com/ArtificialAnlys/status/2115265133467635877

[^75]: https://epoch.ai/benchmarks/scicode

[^76]: https://openai.com/index/frontierscience/

[^77]: https://arxiv.org/html/2611.22490

[^78]: https://livebench.ai/

[^79]: https://livecodebench.github.io/leaderboard.html

[^80]: https://livecodebench.github.io/

[^81]: https://www.vals.ai/benchmarks/lcb

[^82]: https://arena.ai/leaderboard

[^83]: https://arena.ai/leaderboard/agent

[^84]: https://arena.ai/leaderboard/code

[^85]: https://www.forecastbench.org/about/

[^86]: https://www.forecastbench.org/leaderboards/

[^87]: https://arxiv.org/html/2606.18686

[^88]: https://www.vals.ai/benchmarks/inference_provider

[^89]: https://www.aisi.gov.uk/blog/optimal-stopping-spending-evaluation-compute-where-it-counts

[^90]: https://www.aisi.gov.uk/category/science-of-evaluations

[^91]: https://rank.opencompass.org.cn/

[^92]: https://opencompass.org.cn/rules/en/

[^93]: https://medbench.opencompass.org.cn/

[^94]: https://scale.com/blog/scale-imda-legal-reasoning-benchmark

[^95]: https://tessary.ai/answers/gaia/what-changed-in-the-latest-version-of-gaia2

[^96]: https://epoch.ai/benchmarks/arc-agi-3/review

[^97]: https://arcprize.org/competitions/2026

[^98]: https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-3

[^99]: https://epoch.ai/benchmarks

[^100]: https://metr.org/research/

[^101]: https://epoch.ai/about/transparency

[^102]: https://labs.scale.com/leaderboard/sweatlas-tw

[^103]: https://labs.scale.com/papers/mcpatlas

[^104]: https://safe.ai/blog/significant-increase-in-digital-labor-automation

[^105]: https://safe.ai/news/the-ai-wage-loss-dashboard-is-live

[^106]: https://dashboard.safe.ai/

[^107]: https://www.apolloresearch.ai/science/frontier-models-are-capable-of-incontext-scheming

[^108]: https://www.apolloresearch.ai/blog/principles-for-embedded-evaluations

[^109]: https://www.apolloresearch.ai/blog/pilot-towards-embedded-evaluations

[^110]: https://transluce.org/research

[^111]: https://transluce.org/embedded-assessment-pilot-with-openai

[^112]: https://www.vals.ai/blogs

[^113]: https://www.aisi.gov.uk/blog/international-evaluation-best-practice-and-open-questions-in-ai-measurement

[^114]: https://epoch.ai/publications/mirrorcode-preliminary-results

[^115]: https://www.aisi.gov.uk/category/cyber

[^116]: https://arcprize.org/

[^117]: https://ar5iv.labs.arxiv.org/html/2606.07682

[^118]: https://benchlm.ai/benchmarks/swemarathon

[^119]: https://benchlm.ai/benchmarks/swe-rebench

[^120]: https://newsletter.safe.ai/p/aisn-76-fable-5-restrictions-lifted

[^121]: https://www.motherjones.com/politics/2026/11/openai-altman-independent-assessment-oversight-control-ai-tech-security/

[^122]: https://www.vals.ai/updates

[^123]: https://casrai.org/news/rea-bench-responsible-agent-auditing-benchmark-2026

[^124]: https://casrai.org/news/privacypr-benchmark-privacy-aware-code-review-agents-2026

[^125]: https://www.anthropic.com/claude-fable-and-mythos-5-2

[^126]: https://benchlm.ai/llm-agent-benchmarks

[^127]: https://metr.org/

[^128]: https://www.globenewswire.com/news-release/2026/11/19/3406884/0/en/ortelan-s-praus-tops-models-from-four-frontier-ai-labs-on-jup-eval-a-new-open-benchmark-for-ai-judgment.html

[^129]: https://www.benchleader.com/benchmarks

[^130]: https://www.databricks.com/blog/introducing-databricks-ai-index-state-enterprise-ai-tokenomics

[^131]: https://xenospectrum.com/en/openai-healthcare-computer-use-agents/

[^132]: https://aiweekly.co/alerts/so-arena-scores-21-system-one-models-on-2919-tasks

[^133]: https://finance.yahoo.com/technology/ai/articles/einsia-ai-launches-visual-cipher-103900005.html

[^134]: https://www.neoteo.com/en/what-the-mka-agent-benchmark-tests-and-what-its-scores-mean

[^135]: https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/

[^136]: https://metr.org/june-2026-progress-report.pdf

[^137]: https://metr.org/team/nate-rush/

[^138]: https://metr.org/team/tom-cunningham/

[^139]: https://hawk.metr.org/

[^140]: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/

[^141]: https://metr.org/blog/2026-02-24-uplift-update/

[^142]: https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/

[^143]: https://hawk.metr.org/user-guide/sample-editing/

[^144]: https://metr.org/blog/2026-01-29-time-horizon-1-1/

[^145]: https://taskdev.metr.org/introduction/

[^146]: https://epoch.ai/models/doubao-seed-evolving-nov-2026

[^147]: https://epoch.ai/models/muse-ember

[^148]: https://epoch.ai/files/MirrorCode.pdf

[^149]: https://epoch.ai/models/claude-fable-5-2

[^150]: https://epoch.ai/frontiermath/tiers-1-4/the-benchmark

[^151]: https://epoch.ai/about/team/tom-adamczewski

[^152]: https://epoch.ai/data/ai-models

[^153]: https://epoch.ai/data/benchmarks.csv

[^154]: https://epoch.ai/models/gemini-4-hydrogen

[^155]: https://arxiv.org/html/2604.27319

[^156]: https://arxiv.org/html/2606.07682v1

[^157]: https://arxiv.org/html/2602.02660v3

[^158]: https://arxiv.org/html/2609.11873v3

[^159]: https://digitalmeld.io/blog/november-2026-cyber-outages-agentic-ai-defense/

[^160]: https://www.federalregister.gov/documents/2026/01/08/2026-00206/request-for-information-regarding-security-considerations-for-artificial-intelligence-agents?ref=blog.disclose.io

[^161]: https://benchlm.ai/benchmarks/cybergym

[^162]: https://www.ic3.gov/CSA/2026/261113.pdf

[^163]: https://sai.science/benchmark-safety-benchmark

[^164]: https://ringmast4r.substack.com/p/the-most-consequential-hundred-days

[^165]: https://www.ibtimes.co.uk/us-businesses-hit-cyber-incidents-outages-1832974

[^166]: https://economictimes.indiatimes.com/tech/technology/microsoft-xai-and-google-will-share-ai-models-with-us-government-for-security-reviews/printarticle/130830039.cms

[^167]: https://benchmarklist.com/benchmarks/cybergym/

[^168]: https://www.neoteo.com/en/openai-agents-reached-hugging-face-during-an-internal-test

[^169]: https://www.bx33661.com/en/blog/cybergym-ai-security-agent-benchmark-en/

[^170]: https://www.cio-platform.nl/en/weblog/nieuws-extern-detailpagina/2026/11/09/cybersecurity-assessment-2026-the-threat-is-accelerating-but-our-resilience-is-not-keeping-pace

[^171]: https://benchlm.ai/benchmarks/exploitgymhardened

[^172]: https://www.apolloresearch.ai/science/forecasting-frontier-language-model-agent-capabilities/

[^173]: https://www.apolloresearch.ai/

[^174]: https://www.apolloresearch.ai/blog/embedded-evaluators-are-necessary-for-meaningful-external-testing

[^175]: https://www.apolloresearch.ai/blog/an-opinionated-evals-reading-list

[^176]: https://www.apolloresearch.ai/blog/a-starter-guide-for-evals

[^177]: https://www.apolloresearch.ai/blog/apollo-update-may-2026

[^178]: https://www.apolloresearch.ai/science/the-evals-gap/

[^179]: https://www.apolloresearch.ai/science/we-need-a-science-of-evals

[^180]: https://watcher.apolloresearch.ai/rss.xml

[^181]: https://watcher-docs.apolloresearch.ai/concepts/analyzer

[^182]: https://www.apolloresearch.ai/governance/the-uk-ai-safety-summit-our-recommendations/

[^183]: https://watcher.apolloresearch.ai/demo/

[^184]: https://www.aisi.gov.uk/category/engineering

[^185]: https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities

[^186]: https://www.aisi.gov.uk/blog/investigating-alignment-failures-in-aisis-incident

[^187]: https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing

[^188]: https://www.aisi.gov.uk/blog/cheating-behaviour-in-frontier-model-evaluations

[^189]: https://www.developersdigest.tech/benchmarks/tau-bench

[^190]: https://arxiv.org/html/2609.29296v1

[^191]: https://llm-stats.com/benchmarks/browsecomp

[^192]: https://benchlm.ai/benchmarks/browsecomp-plus

[^193]: https://www.benchleader.com/benchmarks/browsecomp_plus

[^194]: https://benchlm.ai/benchmarks/browsecomp

[^195]: https://aclanthology.org/2026.findings-emnlp.1615.pdf

[^196]: https://llm-stats.com/benchmarks/browsecomp-plus

[^197]: https://openai.com/he-IL/index/introducing-gpt-5-5/

[^198]: https://awesomeagents.ai/leaderboards/web-agent-benchmarks-leaderboard/

[^199]: https://benchlm.ai/benchmarks/tau3-bench

[^200]: https://www.layer3labs.io/guides/ai-agent-benchmarks

[^201]: https://www.vals.ai/blogs/which-models-swear

[^202]: https://www.vals.ai/models/kimi_kimi-k3

[^203]: https://www.vals.ai/models/thinkingmachines_inkling

[^204]: https://www.vals.ai/models/openai_gpt-5.6-terra

[^205]: https://www.vals.ai/models/ant_ling-3.0-flash-2607

[^206]: https://www.vals.ai/news

[^207]: https://www.vals.ai/media

[^208]: https://www.vals.ai/benchmarks/vals_index

[^209]: https://benchlm.ai/benchmarks/scale-adversarial-robustness

[^210]: https://benchlm.ai/benchmarks/scale-math

[^211]: https://www.cnbc.com/2026/11/16/openai-independent-ai-safety-evaluators.html

[^212]: https://techcrunch.com/2026/11/16/openai-will-embed-apollo-researchers-to-investigate-ai-subversion/

[^213]: https://www.ababnews.com/en/news/b4e54933-82bb-4644-8bf3-66b2923a808b

[^214]: https://www.sphericalinsights.com/blogs/openai-partners-with-four-independent-evaluators-to-strengthen-ai-safety-and-risk-assessments-expert-view-by-spherical-insights

[^215]: https://x.com/OpenAI/status/2122359930628063248

[^216]: https://www.benzinga.com/markets/private-markets/26/11/63307780/openai-brings-four-outside-research-groups-into-ai-safety-testing

[^217]: https://newscord.org/article/openai-signs-agreements-with-apollo-metr-transluce-and-goodfire-for-embedded-saf--Story_20261116_OpenAIwillembedApollb0a09c2f

[^218]: https://www.washingtonpost.com/ripple/2026/10/27/remote-work-automation-just-crossed-troubling-threshold/

[^219]: https://arxiv.org/html/2601.17399v1

[^220]: https://benchlm.ai/benchmarks/livebench

[^221]: https://arcprize.org/competitions/2026/paper

[^222]: https://arcprize.org/events

[^223]: https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-2/

[^224]: https://chnllm.com/en/leaderboard.html

[^225]: https://www.economictimes.indiatimes.com/tech/artificial-intelligence/deepseek-touts-new-training-method-as-china-pushes-ai-efficiency/articleshow/126304724.cms

[^226]: https://llmleaderboard.com/benchmarks/livebench-design

[^227]: https://www.benchleader.com/benchmarks/livebench_global

[^228]: https://llm-stats.com/benchmarks/livebench

[^229]: https://arcprize.org/competitions/2026/arc-agi-2

[^230]: https://arena.ai/text/direct?model_a=gemini-4-carbon-high

[^231]: https://help.arena.ai/articles/7011479247-how-to-see-ai-rankings-in-arena-leaderboards

[^232]: https://arena.ai/?about

[^233]: https://arena.ai/leaderboard/image/image-edit/multi-image

[^234]: https://arena.ai/leaderboard/image/text-to-image

[^235]: https://arena.ai/leaderboard/video/image-to-video

[^236]: https://arena.ai/leaderboard/chat/text/creative-writing

[^237]: https://arena.ai/leaderboard/image/image-edit/single-image

[^238]: https://arena.ai/

[^239]: https://platform.arena.ai/docs

[^240]: https://canary.arena.ai/leaderboard/image/image-edit

[^241]: https://help.arena.ai/ru/articles/1544829667-how-to-create-videos-with-video-arena

[^242]: https://www.benchleader.com/benchmarks/forecastbench

[^243]: https://www.quia.com/shared/search?keywords=...1\&category=-1\&adv_search=false\&top100=false\&sortBy=0\&sortDirection=0

[^244]: https://livecodebench.github.io/leaderboard_v5.html

[^245]: https://huggingface.co/livecodebench

[^246]: https://luminabench.com/benchmarks/forecastbench/

[^247]: https://forecastbench.org/

[^248]: https://benchlm.ai/benchmarks/livecodebench-v6

[^249]: https://theaggregate.ai/benchmark?slug=forecastbench-baseline-zero-shot-market

[^250]: https://www.kaggle.com/benchmarks/open-benchmarks/livecodebench

[^251]: https://presenc.ai/research/livecodebench-leaderboard-2026

[^252]: https://benchmarklist.com/benchmarks/livecodebench_official/

[^253]: https://cooperbench.com/blog/curse-of-coordination

[^254]: https://arxiv.org/abs/2608.28266

[^255]: https://llmlearner.com/rankings/swe-marathon

[^256]: https://benchmarklist.com/benchmarks/swe_marathon/

[^257]: https://www.neoteo.com/es/patrones-de-diseno-multiagente-como-elegir-la-arquitectura-adecuada

[^258]: https://opencodepapers-b7572d.gitlab.io/papers/programbench-leaderboard.html

[^259]: https://sergei-parfenov.com/blog/five-of-my-eight-agents-left-out-the-same-caveat/

[^260]: https://www.igdb.com/games/reprobate--1

[^261]: https://dropday.ai/c/autoform-hard

[^262]: https://critpt.com/

[^263]: https://store.steampowered.com/app/3582880/Reprobate/

[^264]: https://mypriors.com/benchmarks

[^265]: https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/

[^266]: https://cellcog.ai/blog/artificial-analysis-intelligence-index-v5/

[^267]: https://handyai.substack.com/p/model-drop-gpt-62-astra-sol

[^268]: https://openrouter.ai/meta/muse-ember

[^269]: https://www.chaincatcher.com/en/article/2305785

[^270]: https://arxiv.org/abs/2504.12516

[^271]: https://openai.com/es-ES/index/introducing-chatgpt-agent/

[^272]: https://www.honeyhive.ai/learn/browsecomp

[^273]: https://parallel.ai/articles/browsecomp-benchmark

[^274]: https://mmbench.opencompass.org.cn/

[^275]: https://mmbench.opencompass.org.cn/leaderboard

[^276]: https://cnfinbench.opencompass.org.cn/evaluation-list

[^277]: https://lawbench.opencompass.org.cn/leaderboard

[^278]: https://doc.opencompass.org.cn/

[^279]: https://botchat.opencompass.org.cn/

[^280]: https://doc.opencompass.org.cn/zh_CN/latest/advanced_guides/advanced_guides/advanced_guides/advanced_guides/advanced_guides/advanced_guides/advanced_guides/advanced_guides/notes/advanced_guides/user_guides/advanced_guides/code_eval.html

[^281]: https://doc.opencompass.org.cn/user_guides/metrics.html

[^282]: https://doc.opencompass.org.cn/get_started/quick_start.html

[^283]: https://doc.opencompass.org.cn/user_guides/deepseek_r1.html

[^284]: https://doc.opencompass.org.cn/get_started/installation.html

[^285]: https://doc.opencompass.org.cn/zh_CN//notes/academic.html

[^286]: https://scale.com/events

[^287]: https://scale.com/events/scale-at-mwc-doha-2026

[^288]: https://scale.com/blog/why-i-joined-cesar-yazbeck

[^289]: https://static.scale.com/uploads/674f4cc7a74e35bcaae1c29a/MCP_Atlas.pdf

[^290]: https://scale.com/blog/scaleforhospitaloperations

[^291]: https://scale.com/blog/advancing-agents

[^292]: https://labs.scale.com/blog/improving-multi-turn-tool-use-with-grpo

[^293]: https://scale.com/blog/the-anatomy-of-ai-deployment

[^294]: https://scale.com/blog/category/data

[^295]: https://devops.com/at-ignite-microsoft-makes-the-case-for-good-enough-coding-models

[^296]: https://www.benchleader.com/benchmarks/scale_swe_atlas_tw

[^297]: https://benchlm.ai/benchmarks/scale-swe-atlas-overall

[^298]: https://www.semanticscholar.org/paper/HeurekaBench:-A-Benchmarking-Framework-for-AI-Panigrahi-Videnovi'c/411b35f014199bffc7db340bb732881e592ccb29/figure/1

[^299]: https://www.alphaxiv.org/abs/2608.21601v1

[^300]: https://safe.ai/work/research

[^301]: https://safe.ai/

[^302]: https://safe.ai/share/mlsn-17-measuring-general-ai-abilities

[^303]: https://newsletter.safe.ai/p/ai-safety-newsletter-66-aisn-66-evaluating

[^304]: https://newsletter.safe.ai/feed

[^305]: https://safe.ai/blog/significant-increase-in-digital-labor-automation?trk=article-ssr-frontend-pulse_little-text-block

[^306]: https://safe.ai/blog

[^307]: https://newsletter.safe.ai/archive

[^308]: https://safe.ai/news

[^309]: https://safe.ai/work

[^310]: https://newsletter.safe.ai/p/aisn-45-center-for-ai-safety-2024

[^311]: https://www.benchleader.com/benchmarks/the_agent_company

[^312]: https://reglab.stanford.edu/publications/cybench-a-framework-for-evaluating-cybersecurity-capabilities-and-risk-of-language-models/

[^313]: https://evaluatorbench.com/entity/epoch.html

[^314]: https://research.contrary.com/report/ai-benchmarks-climbing-the-wrong-hills

[^315]: https://epoch.ai/benchmarks/about

[^316]: https://github.com/gracebaekk/the-agent-company-leaderboard

[^317]: https://github.com/turbobeest/modelspec/blob/main/benchmarks/cybench.md

[^318]: https://benchmarks.darvinyi.com/benchmarks/the-agent-company

[^319]: https://usenaive.ai/benchmarks/the-agent-company

[^320]: https://benchgecko.ai/benchmark/the-agent-company

[^321]: https://benchlm.ai/benchmarks/posttrainbench

[^322]: https://servicenow.github.io/WorkArena/

[^323]: https://benchgecko.ai/benchmark/posttrainbench

[^324]: https://www.llmboard.ai/benchmarks/posttrainbench-505

[^325]: https://llmlearner.com/rankings/posttrain-bench

[^326]: https://open-llm-radar.com/benchmarks/gaia2

[^327]: https://github.com/osolmaz/huggingface-blog/blob/main/gaia2.md

[^328]: https://llm-stats.com/benchmarks/posttrainbench

[^329]: https://raw.githubusercontent.com/mlresearch/v306/main/assets/rank26a/rank26a.pdf

[^330]: https://epoch.ai/

[^331]: https://epoch.ai/benchmarks/post-train-bench

[^332]: https://epoch.ai/topics

[^333]: https://epoch.ai/benchmarks/post-train-bench/review

[^334]: https://epoch.ai/gradient-updates/rip-classic-benchmarks

[^335]: https://epoch.ai/data/data-centers/satellite-explorer/FluidstackLakeMariner/2025-03-18

[^336]: https://epoch.ai/eci

[^337]: https://epoch.ai/frontiermath

[^338]: https://epoch.ai/benchmarks/dtbench

[^339]: https://openai.com/research/index/

[^340]: https://openai.com/index/research-acceleration-view-inside-openai/

[^341]: https://openai.com/index/science-at-the-frontier/

[^342]: https://openai.com/news/research/

[^343]: https://openai.com/index/accelerating-engineering-for-the-physical-world/

[^344]: https://openai.com/news/safety-and-alignment/

[^345]: https://openai.com/about/

[^346]: https://openai.com/blog/?authors=lama-ahmad

[^347]: https://openai.com/index/the-state-of-enterprise-ai-2025-report/

[^348]: https://openai.com/index/accelerating-science-gpt-5/

[^349]: https://openai.com/

[^350]: https://openai.com/index/advancing-chip-design-with-our-models/

[^351]: https://openai.com/news/safety-alignment/?display=list

[^352]: https://www.perplexity.ai/search/1725ee01-3f92-4681-bc20-c4e687fd9bbc

[^353]: https://www.perplexity.ai/search/316ace4b-7289-46b9-a163-ce64887fff58

[^354]: https://www.perplexity.ai/search/20d61b79-5105-4b31-912d-59ae68a92289

