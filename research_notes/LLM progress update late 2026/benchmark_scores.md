# Frontier model benchmark scores, December 2025 to 19 November 2026

Research date: 19 November 2026. Reading conventions for every table below:

- **V** = vendor-reported (lab launch post, model card or system card). **I** = independently measured (leaderboard operator or third-party evaluator). **V-via-X** = a vendor figure that I read through secondary source X because the primary page was an image, a PDF I did not open, or returned HTTP 403 (all openai.com pages returned 403 in this session).
- **UNVERIFIED** = I could not confirm the figure against a primary or leaderboard source in this session. Do not publish these without a check.
- Benchmark versions matter. Terminal-Bench 2.0, 2.1 and 4.0, OSWorld-Verified, OSWorld 2.0 and 2.1, FrontierMath v1 and v2, GDPval and GDPval-AA Elo are different instruments. Scores are not comparable across versions.
- Official leaderboards I could read directly: arcprize.org, Scale Labs SWE-Bench Pro public, Artificial Analysis, arena.ai front page, epoch.ai/benchmarks front page. tbench.ai rendered with empty tables. Epoch's per-benchmark pages rendered without scores. I did not reach swebench.com, lastexam.ai, os-world.github.io or livebench.ai.

## What are the current state-of-the-art scores and holders on each benchmark as of 19 November 2026?

### Takeaway
Claude Fable 5.2 (Anthropic, 9 Nov 2026) and GPT-6.2 Astra (OpenAI, 17 Nov 2026) split the top positions, with Gemini 4 Carbon (Google, 10 Nov 2026) third; Fable 5.2 leads the Artificial Analysis index, ARC-AGI-3, HLE and vendor-reported SWE-bench Pro, while Astra leads ARC-AGI-2 and ties on the Epoch Capabilities Index. The benchmark set itself turned over during 2026: SWE-bench Verified, Terminal-Bench 2.0, OSWorld-Verified and GPQA Diamond are no longer in any November 2026 launch table and have been replaced by Terminal-Bench 4.0, OSWorld 2.1, FrontierSWE v2, FrontierCode 2.0, ARC-AGI-3 and Agents' Last Exam.

### Cited Findings

**Release timeline (dates from the ARC Prize leaderboard unless noted)**

- GPT-5.2 and GPT-5.2 Pro 11 Dec 2025; Gemini 3 Flash Preview 17 Dec 2025; Kimi K2.5 27 Jan 2026; Claude Opus 4.6 5 Feb 2026; Gemini 3 Deep Think (2/26) 12 Feb 2026; Claude Sonnet 4.6 17 Feb 2026; Gemini 3.1 Pro Preview 19 Feb 2026; GLM-5 20 Feb 2026; GPT-5.4 and GPT-5.4 Pro 4 Mar 2026; Grok 4.20 9 Mar 2026; Claude Opus 4.7 16 Apr 2026; GPT-5.5 and GPT-5.5 Pro 22-23 Apr 2026; Gemini 3.5 Flash 19 May 2026; Claude Opus 4.8 1 Jun 2026; Claude Fable 5 9 Jun 2026; GLM-5.2 13 Jun 2026; GPT-5.6 Sol/Terra/Luna 9 Jul 2026; Kimi K3 and Grok 4.5 16 Jul 2026; Claude Opus 5 24 Jul 2026; Grok 4.6 11 Aug 2026; DeepSeek V4 Pro 13 Aug 2026; Claude Fable 5.1 1 Sep 2026; GPT-6 Astra 2 Sep 2026; Grok 4.7 21 Sep 2026; Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna 22 Sep 2026; Claude Sonnet 5.5 28 Sep 2026; GPT-6.1 Sol 29 Sep 2026; Claude Haiku 5.5 7 Oct 2026; Gemini 4 Argon 13 Oct 2026; Muse Spark Open 15 Oct 2026; DeepSeek V4.1 Flash 1017 17 Oct 2026; Claude Fable 5.2 9 Nov 2026; Gemini 4 Carbon 10 Nov 2026; GPT-6.2 Astra and GPT-6.2 Sol 17 Nov 2026 — [ARC Prize leaderboard](https://arcprize.org/leaderboard)
- The ARC Prize date is the date of the leaderboard entry, which can trail the launch. Example conflicts: Gemini 4 Argon is listed 13 Oct on ARC Prize but a tracker gives 30 Sep; Opus 4.8 is 1 Jun on ARC Prize but 28 May on Morph; one source dates GPT-5.6's announcement to 26 Jun — [search summary of demandsphere tracker](https://demandsphere.com/research/demandsphere-radar/ai-frontier-model-tracker/changelog); [Morph Claude benchmarks](https://www.morphllm.com/claude-benchmarks); [OpenAI GPT-5.6 page, via search](https://openai.com/index/gpt-5-6/)
- Other November 2026 releases not on the ARC table: Gemini 4 Hydrogen 12 Nov; Mistral Large 4 GA 5 Nov; Qwen4-Max 16 Nov; Kimi K3.1 Pro weights published 4 Nov. Fable 5.2 launched alongside Mythos 5.2, the same model without the public safeguards — [nhimg frontier comparison, via search](https://nhimg.org/frontier-ai-models-compared); [Zvi Mowshowitz](https://thezvi.substack.com/p/fable-and-mythos-52-the-system-card)
- Gemini 4 Neon appears on Artificial Analysis and Arena but I found no launch date for it — [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)

**State of the art by benchmark**

| Benchmark | SOTA holder | Score | Config | V / I | Date | Source |
|---|---|---|---|---|---|---|
| Artificial Analysis Intelligence Index (v5.0.x) | Claude Fable 5.2 | 65 (64.6) | Max effort, default fallback | I | 17 Nov 2026 | [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models) |
| Epoch Capabilities Index | GPT-6.2 Astra, tied with Fable 5.2 | 174 (174.2 vs 173.5 per one secondary) | not stated | I | Nov 2026 | [Epoch benchmarks hub](https://epoch.ai/benchmarks); [The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/) |
| Arena (LMArena) Agent Arena Index | Claude Fable 5.2 (Max) | 1,448 | Max | I | Nov 2026 | [arena.ai](https://arena.ai/leaderboard) |
| ARC-AGI-1 | Six-way tie: GPT-6.2 Astra, Gemini 4 Carbon, Fable 5.2, Gemini 4 Argon, GPT-6.1 Sol, Opus 5.5 and others | 98.5% | effort column blank | I | Nov 2026 | [ARC Prize](https://arcprize.org/leaderboard) |
| ARC-AGI-2 | GPT-6.2 Astra | 95.8% | $24.2K run cost shown | I | 17 Nov 2026 | [ARC Prize](https://arcprize.org/leaderboard) |
| ARC-AGI-3 (Standard harness) | Claude Fable 5.2 | 81.2% on the leaderboard; 79.26% at high effort per Anthropic's table | high effort | I and V | 9 Nov 2026 | [ARC Prize](https://arcprize.org/leaderboard); [LLM Stats on Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch) |
| ARC-AGI-3 (Provider Adapter harness) | GPT-6.2 Astra | 100.0% | max | I | 17 Nov 2026 | [ARC Prize](https://arcprize.org/leaderboard) |
| SWE-bench Pro (vendor scaffold) | Claude Fable 5.2 | 93.0% | max effort, safeguards on, Anthropic harness | V-via-LLM Stats | 9 Nov 2026 | [LLM Stats on Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch) |
| SWE-bench Pro public (Scale standardized) | Muse Spark 1.1 | 61.50 ± 3.10 | mini-swe-agent, 250-turn limit, uncapped cost | I | board read Nov 2026; no entry date shown | [Scale Labs](https://labs.scale.com/leaderboard/swe_bench_pro_public) |
| SWE-bench Verified | Claude Fable 5 (last high score found) | 95.0% | not stated | V-via-Morph, UNVERIFIED against primary | 9 Jun 2026 | [Morph](https://www.morphllm.com/claude-benchmarks) |
| Terminal-Bench 2.0 | GPT-5.5 (Codex CLI) | 82.7% vendor; 82.0% on tbench.ai per a secondary | reasoning effort not stated | V; I-via-secondary | Apr 2026 | [Vellum](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5); [marc0.dev leaderboard, via search](https://hn.jakechampion.name/reader/https://www.marc0.dev/en/leaderboard) |
| Terminal-Bench 2.1 | GPT-5.6 Sol Ultra | 91.9% (single-agent Sol 88.8%) | Ultra = parallel agents, about 3x cost | V-via-search | Jul 2026 | [OpenAI GPT-5.6 page, via search](https://openai.com/index/gpt-5-6/) |
| Terminal-Bench 4.0 | Claude Sonnet 5.5 70.6% (V-via-Morph); Fable 5.2 67.6% ± 1.8; Mythos 5.2 without safeguards 70.5% | see cells | Fable 5.2 at max, safeguards on | V | Sep to Nov 2026 | [Morph](https://www.morphllm.com/claude-benchmarks); [LLM Stats on Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch) |
| OSWorld-Verified | GPT-5.5 | 78.7% | not stated | V-via-Vellum | Apr 2026 | [Vellum](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5) |
| OSWorld 2.1 offline | Claude Fable 5.2 | 89.3% partial credit; 54.6% strict pass | max | V | 9 Nov 2026 | [LLM Stats on Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch) |
| Humanity's Last Exam | Claude Fable 5.2 | 74.2% with tools; 73.2% without tools | max | V | 9 Nov 2026 | [LLM Stats on Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch) |
| GPQA Diamond | Mythos Preview 94.6%; among GA models GPT-5.4 Pro 94.4%, Gemini 3.1 Pro 94.3%, Opus 4.7 94.2% | see cells | not stated | V-via-Vellum | Feb to Apr 2026 | [Vellum on Opus 4.7](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained) |
| FrontierMath Tier 4 (v2, 43 problems) | GPT-6 Astra | 97.6% | not stated | V-via-search, UNVERIFIED against Epoch hub | Sep 2026 | [OpenAI GPT-6 Astra page, via search](https://openai.com/index/gpt-6-astra/) |
| FrontierMath Erdős (Lean-verified, 68 open problems) | GPT-6.2 Astra | 7 of 68 (prior record 3 of 68, GPT-6.1 Sol) | not stated | I (Epoch) | Nov 2026 | [The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/); [Epoch hub](https://epoch.ai/benchmarks) |
| GDPval (original, win-or-tie rate) | GPT-5.5 | 84.9% | not stated | V-via-Vellum | Apr 2026 | [Vellum](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5) |
| GDPval-AA v2.1 (Elo) | Claude Opus 5.5 | 1866 in Anthropic's Nov table (1846 in its Sep launch table); Fable 5.2 1831 | max | V (Anthropic tables of an AA-run benchmark) | Nov 2026 | [LLM Stats on Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch); [LLM Stats on Opus 5.5](https://llm-stats.com/blog/research/claude-opus-5-5-launch) |
| Vending-Bench 2 | Gemini 4 Carbon | $16,484 final balance | not stated | V (Google model card) | Nov 2026 | [DeepMind model card](https://deepmind.google/models/model-cards/gemini-4-carbon/) |
| Cyber: ExploitGym | Gemini 4 Carbon | 54.8% | via Fairwind Program access | V | Nov 2026 | [DeepMind model card](https://deepmind.google/models/model-cards/gemini-4-carbon/) |
| Cyber: CyberGym (April 2026 state) | GPT-5.5 | 81.8% (GPT-5.4 79.0%, Opus 4.7 73.1%) | not stated | V-via-Vellum | Apr 2026 | [Vellum](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5) |
| FrontierSWE v2 | Claude Fable 5.2 | 69.9% | max; 34 tasks, 20-hour budget, Proximal harness | V | Nov 2026 | [LLM Stats on Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch) |
| FrontierCode 2.0 | Claude Fable 5.2 | 49.1% | xhigh; $14.19 per task; Cognition run | V | Nov 2026 | [LLM Stats on Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch) |
| Agents' Last Exam v1.1 | GPT-6.2 Astra (no absolute score in text); Gemini 4 Carbon 77.4% is the highest number I have | see cells | not stated | V | Nov 2026 | [The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/); [DeepMind model card](https://deepmind.google/models/model-cards/gemini-4-carbon/) |

**Composite index detail**

- Artificial Analysis Intelligence Index top ten: Fable 5.2 65 (Max), GPT-6.2 Astra 62 (Max), Gemini 4 Neon 61 (Xhigh), Gemini 4 Carbon 60 (High), Opus 5.5 59 (Max), GPT-6.2 Sol 57 (Max), Sonnet 5.5 55 (Max), Gemini 4 Hydrogen 54 (Xhigh), GPT-6.1 Terra 51 (Max), Gemini 4 Argon 50 (High). Further down: Muse Wonder Full 50, Kimi K3.1 Pro 46, Qwen4 Max 43, Haiku 5.5 36, Grok 4.7 35, Tencent Hy4 35, DeepSeek V4.1 Flash 1017 33, GLM-5.3 32 — [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models)
- The index is described as built from nine evaluations, and Google's model card cites it as "AA Index v5.0"; GPT-6 Astra scores 57 on it — [The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/); [DeepMind model card](https://deepmind.google/models/model-cards/gemini-4-carbon/)
- Arena Agent Arena Index top ten: Fable 5.2 (Max) 1,448; Opus 5.5 (Max) 1,336; Gemini 4 Neon (High) 1,333; Gemini 4 Carbon (High) 1,303; Sonnet 5.5 (Max) 1,296; GPT-6.2 Astra (Max) 1,291; GPT-6 Astra (Max) 1,282; Opus 5.5 (High) 1,273; Fable 5.1 (Max) 1,272; Gemini 4 Hydrogen (High) 1,271. On WebDev Arena GPT-6.2 Astra ranks #3 and GPT-6.2 Sol #5; Elo values were not on the page — [arena.ai](https://arena.ai/leaderboard)
- Epoch reports that Fable 5.2 set an ECI record on 9 Nov from pre-launch testing, and its headline now shows GPT-6.2 Astra at 174 — [Epoch hub](https://epoch.ai/benchmarks)

**ARC Prize verified leaderboard, flagship rows (independent)**

| Model | Entry date | ARC-AGI-1 | ARC-AGI-2 | ARC-AGI-3 Standard | ARC-AGI-3 Adapter |
|---|---|---|---|---|---|
| GPT-5.2 | 11 Dec 2025 | 86.2 | 52.9 | — | — |
| GPT-5.2 Pro | 11 Dec 2025 | 90.5 | 54.2 | — | — |
| Opus 4.5 | 24 Nov 2025 | 80.0 | 37.6 | — | — |
| Gemini 3 Pro | 18 Nov 2025 | 75.0 | 31.1 | — | — |
| Claude Opus 4.6 (120K) | 5 Feb 2026 | 94.0 | 69.2 | 0.5 | — |
| Gemini 3 Deep Think (2/26) | 12 Feb 2026 | 96.0 | 84.6 | — | — |
| Claude Sonnet 4.6 | 17 Feb 2026 | 86.5 | 60.4 | — | — |
| Gemini 3.1 Pro Preview | 19 Feb 2026 | 98.0 | 77.1 | 0.4 | — |
| GPT-5.4 | 4 Mar 2026 | 93.7 | 74.0 | 0.2 | — |
| GPT-5.4 Pro | 4 Mar 2026 | 94.5 | 83.3 | — | — |
| Grok 4.20 (Reasoning) | 9 Mar 2026 | 89.5 | 65.1 | 0.1 | — |
| Claude Opus 4.7 | 16 Apr 2026 | 93.5 | 75.8 | 0.2 | — |
| GPT-5.5 | 22 Apr 2026 | 95.0 | 85.0 | 0.4 | — |
| GPT-5.5 Pro | 23 Apr 2026 | 96.5 | 84.6 | — | — |
| Claude Opus 4.8 | 1 Jun 2026 | 92.5 | 72.1 | 1.5 | — |
| Claude Fable 5 | 9 Jun 2026 | 98.5 | 89.2 | — | — |
| GPT-5.6 Sol | 9 Jul 2026 | 97.5 | 92.5 | 7.8 | — |
| Kimi K3 | 16 Jul 2026 | 94.5 | 60.4 | — | — |
| Grok 4.5 | 16 Jul 2026 | 87.2 | 52.6 | 0.3 | — |
| Claude Opus 5 | 24 Jul 2026 | 97.5 | 90.4 | 30.2 | — |
| DeepSeek V4 Pro 0813 | 13 Aug 2026 | 90.5 | 61.3 | — | — |
| Claude Fable 5.1 | 1 Sep 2026 | 97.5 | 90.0 | — | — |
| GPT-6 Astra | 2 Sep 2026 | 98.5 | 95.0 | 62.7 | 99.9 |
| Grok 4.7 | 21 Sep 2026 | 90.2 | 61.4 | 1.8 | 10.0 |
| Claude Opus 5.5 | 22 Sep 2026 | 98.5 | 93.3 | — | — |
| GPT-6 Sol | 22 Sep 2026 | 95.5 | 89.6 | 4.6 | 23.0 |
| Claude Sonnet 5.5 | 28 Sep 2026 | 96.5 | 83.9 | 24.3 | 72.4 |
| GPT-6.1 Sol | 29 Sep 2026 | 98.5 | 94.2 | 52.7 | 96.4 |
| Claude Haiku 5.5 | 7 Oct 2026 | 89.0 | 61.3 | 0.5 | 2.8 |
| Gemini 4 Argon | 13 Oct 2026 | 98.5 | 91.3 | 49.8 | 97.5 |
| Muse Spark Open | 15 Oct 2026 | 89.0 | 57.5 | 0.1 | 0.4 |
| DeepSeek V4.1 Flash 1017 | 17 Oct 2026 | 94.5 | 78.1 | 0.2 | 5.8 |
| Claude Fable 5.2 | 9 Nov 2026 | 98.5 | 93.8 | 81.2 | 97.7 |
| Gemini 4 Carbon | 10 Nov 2026 | 98.5 | 94.2 | 65.1 | 99.1 |
| GPT-6.2 Sol | 17 Nov 2026 | 97.5 | 85.8 | 54.9 | 98.2 |
| GPT-6.2 Astra | 17 Nov 2026 | 98.5 | 95.8 | 70.3 | 100.0 |

All rows — [ARC Prize leaderboard](https://arcprize.org/leaderboard). The page's effort column was blank and the extract covered about 80 of 124 entries. ARC Prize 2026 has closed with results due 4 December 2026.

**Scale Labs SWE-Bench Pro public set (independent, standardized harness)**

- Muse Spark 1.1 61.50 ± 3.10; gpt-5.4 (xHigh) 59.10 ± 3.56; Muse Spark 55.00 ± 3.60; claude-opus-4-6 (thinking) 51.90 ± 3.61; gemini-3.1-pro (thinking) 46.10 ± 3.60; claude-opus-4-5 45.89 ± 3.60; claude-4-5-Sonnet 43.60; gemini-3-pro-preview 43.30; gpt-5.2-codex 41.04; gemini-3-flash 34.63; gpt-5.2 29.94; kimi-k2-instruct 27.67; deepseek-v3p2 15.56; glm-4.6 9.67. Top five run on the mini-swe-agent harness with a 250-turn limit and uncapped cost — [Scale Labs](https://labs.scale.com/leaderboard/swe_bench_pro_public)
- The Scale board has no entry for Opus 4.7, GPT-5.5 or any model released after April 2026 other than the Meta Muse Spark models — [Scale Labs](https://labs.scale.com/leaderboard/swe_bench_pro_public)

**November 2026 three-way comparison on the new benchmark set**

| Benchmark | Fable 5.2 | GPT-6.2 Astra | Gemini 4 Carbon | Opus 5.5 | GPT-6 Astra | Source |
|---|---|---|---|---|---|---|
| Terminal-Bench 4.0 | 67.6% | not published as a number; Vals ranks it 5th | 65.2% (AA-run) | 66.4% (xhigh) | 57.9% (high, OpenAI-run); 59.1% in Google's table | [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch); [DeepMind](https://deepmind.google/models/model-cards/gemini-4-carbon/); [The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/) |
| Terminal-Bench-Science 0.1 | 74.6% | about 77% per OpenAI chart; 71.43% per Vals | 64.8% | 58.7% | 68.1% in Anthropic's table; 63.3% in Google's | same, plus [Vals, via search](https://www.vals.ai/models/openai_gpt-6.2-astra) |
| FrontierSWE v2 | 69.9% | not found | 61.2% | 62.3% | 65.5% | [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch); [DeepMind](https://deepmind.google/models/model-cards/gemini-4-carbon/) |
| FrontierCode 2.0 | 49.1% (xhigh) | leads GPT-6.2 Sol by 0.5 points; no absolute value | 41.1% (medium) | 45.5% (max) | 42.8% (max) | [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch); [The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/) |
| OSWorld 2.1 offline, partial credit | 89.3% | not found | 81.5% | 87.2% | 79.5% in Anthropic's table; 80.9% in Google's | same |
| HLE with tools | 74.2% | second on AA's HLE-Diamond; no value | not reported | 67.7% | 57.2% | same |
| AutomationBench (Zapier) | 51.4% | not found | 53.9% | 42.5% | 41.4% | same |
| Vending-Bench 2 | not reported | not found | $16,484 | $9,235 | $15,515 | [DeepMind](https://deepmind.google/models/model-cards/gemini-4-carbon/) |
| SWE-bench Pro | 93.0% | not reported | not reported | 89.9% | not reported | [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch) |

### Inferences
- "State of the art" in November 2026 depends on which generation of benchmark is asked about. The four benchmarks in the visualization's notes (SWE-Bench Pro, Terminal-Bench 2.0, ARC-AGI-2, OSWorld-Verified) each have a final high-water mark set between April and July 2026, and three of the four have been superseded by a harder version.
- ARC-AGI-1 is saturated at 98.5% (at least six models share the identical top score, which suggests a ceiling on the evaluation set). ARC-AGI-2 went from 54.2% (GPT-5.2 Pro, December 2025) to 95.8% (GPT-6.2 Astra, November 2026) in eleven months. ARC-AGI-3 went from under 1% in March 2026 to 81.2% in November 2026. These three independent series are the cleanest single-source trend lines for the lecture.
- For a "model by benchmark" chart that spans the whole period, ARC-AGI-2 and the Artificial Analysis index are the only instruments that were run on essentially every model by one evaluator.

### Gaps
- tbench.ai rendered with empty tables, so I have no first-hand reading of the official Terminal-Bench 2.0 or 4.x boards. The page headings show a "Terminal-Bench 4.1" board alongside 2.0; I found no scores for 4.1.
- Epoch's FrontierMath page gave the v2 dataset description (338 problems: 295 in Tiers 1-3, 43 in Tier 4, released 12 June 2026) but no scores. The 97.6% Tier 4 figure for GPT-6 Astra comes from a search summary of OpenAI's page and should be checked on the Epoch hub. Source for dataset facts: [Epoch FrontierMath](https://epoch.ai/benchmarks/frontiermath)
- I did not retrieve: swebench.com (SWE-bench Verified independent board), lastexam.ai or Scale HLE, os-world.github.io, livebench.ai, LiveCodeBench, Aider Polyglot, MLE-bench, CyBench, the Scale SWE-Bench Pro commercial set, or Text Arena and WebDev Arena Elo values. I found no November 2026 launch that reported LiveCodeBench, Aider Polyglot, MLE-bench or CyBench, but absence in my searches is weak evidence.
- xAI (Grok 4.20 to 4.7) and Meta (Muse Spark, Muse Wonder, Muse Ember) vendor-reported scores were not researched; only their independent ARC, Scale and AA rows are recorded here.
- Chinese and open-weight models (Kimi K3, K3.1 Pro, Qwen4-Max, DeepSeek V4/V4.1, GLM-5.x, MiniMax M3.x) have only ARC Prize and AA index values here; their launch-post claims were not researched.
- GPT-6.2 Astra's absolute scores for most OpenAI-reported benchmarks are in chart images; the text coverage gives only deltas.

## For each model released since December 2025, which benchmarks did the lab report at launch, and which did it stop reporting?

### Takeaway
Through April 2026 all three major labs still reported some mix of SWE-bench Verified, SWE-Bench Pro, Terminal-Bench 2.0, OSWorld-Verified, GPQA Diamond, ARC-AGI-2 and HLE. Between June and September 2026 those were dropped in stages; by the Opus 5.5 launch (22 September 2026) Anthropic reported none of SWE-bench Verified, GPQA Diamond, ARC-AGI, Terminal-Bench 2.x or OSWorld-Verified, and the November 2026 launch tables from all three labs contain none of the five legacy columns in the visualization.

### Cited Findings

**Launch-reported scores by model (vendor figures unless marked)**

| Model (launch) | Reported at launch | Source and quality |
|---|---|---|
| Claude Opus 4.6 (5 Feb 2026) | SWE-bench Verified 80.8%; SWE-bench Pro 53.4%; Terminal-Bench 2.0 65.4%; OSWorld-Verified 72.7%; GPQA Diamond 91.3%; HLE 40.0% no tools, 53.3% with tools; MCP-Atlas 75.8%; MMMLU 91.1% | V-via-[Vellum](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained), from Anthropic's Opus 4.7 comparison table |
| Claude Sonnet 4.6 (17 Feb 2026) | SWE-bench Verified 79.6%; OSWorld-Verified 72.5%; GPQA Diamond 89.9%; ARC-AGI-2 58.3% (verified) and 60.4% (high effort) | V-via-search of pages citing the system card; system card PDF not opened. [Anthropic system card PDF](https://www-cdn.anthropic.com/78073f739564e986ff3e28522761a7a0b4484f84.pdf); [officechai](https://officechai.com/2026/02/17/claude-sonnet-4-6-benchmarks/) |
| Gemini 3.1 Pro (19 Feb 2026) | SWE-bench Verified 80.6%; SWE-bench Pro 54.2%; Terminal-Bench 2.0 68.5%; GPQA Diamond 94.3%; HLE 44.4% no tools, 51.4% with tools; ARC-AGI-2 77.1%; MMMLU 92.6% | V-via-[Vellum](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained) and [Vellum GPT-5.5](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5) |
| GPT-5.4 (4 Mar 2026) | SWE-Bench Pro 57.7%; Terminal-Bench 2.0 75.1% (OpenAI's own harness); OSWorld-Verified 75.0%; GDPval 83.0%; FrontierMath T1-3 47.6%, T4 27.1%; GPQA Diamond 92.8% (Pro 94.4%); ARC-AGI-2 73.3%; HLE no tools 39.8% | V-via-[Vellum GPT-5.5](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5) |
| Claude Opus 4.7 (16 Apr 2026) | SWE-bench Verified 87.6%; SWE-bench Pro 64.3%; Terminal-Bench 2.0 69.4% (Terminus-2 harness, thinking disabled, 5 attempts averaged); OSWorld-Verified 78.0%; GPQA Diamond 94.2%; HLE 46.9% / 54.7%; MCP-Atlas 77.3%; Finance Agent v1.1 64.4%; BrowseComp 79.3%; CharXiv 82.1% / 91.0%; MMMLU 91.5%; CyberGym 73.1% | V-via-[Vellum](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained); footnotes from [Anthropic launch post](https://www.anthropic.com/news/claude-opus-4-7); CyberGym from [Vellum GPT-5.5](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5) |
| Claude Mythos Preview (April 2026 comparison column, not GA) | SWE-bench Verified 93.9%; SWE-bench Pro 77.8%; Terminal-Bench 2.0 82.0%; OSWorld-Verified 79.6%; GPQA 94.6%; HLE 56.8% / 64.7% | V-via-[Vellum](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained) |
| GPT-5.5 (23 Apr 2026) | Terminal-Bench 2.0 82.7%; SWE-Bench Pro 58.6%; OSWorld-Verified 78.7%; GDPval 84.9% (Pro 82.3%); FrontierMath T1-3 51.7% (Pro 52.4%), T4 35.4% (Pro 39.6%); GPQA Diamond 93.6%; ARC-AGI-2 85.0%; HLE no tools 41.4% (Pro 43.1%); CyberGym 81.8%. No SWE-bench Verified | V-via-[Vellum GPT-5.5](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5) |
| Claude Opus 4.8 (28 May / 1 Jun 2026) | SWE-bench Verified 88.6%; SWE-bench Pro 69.2%; Terminal-Bench 2.1 74.6%; OSWorld 83.4% (version not stated); GPQA Diamond 93.6% | V-via-[Morph](https://www.morphllm.com/claude-benchmarks), UNVERIFIED against primary |
| Claude Fable 5 (9 Jun 2026) | SWE-bench Verified 95.0%; SWE-bench Pro 80.0%; Terminal-Bench 2.1 reported variously as 88.0%, 83.1% or "not published" | V-via-[Morph](https://www.morphllm.com/claude-benchmarks); Terminal-Bench conflict from [emergent.sh, via search](https://emergent.sh/learn/gpt-5-6-sol-vs-claude-fable-5). UNVERIFIED |
| Claude Sonnet 5 (30 Jun 2026) | SWE-bench Verified 85.2%; SWE-bench Pro 63.2% | [Morph](https://www.morphllm.com/claude-benchmarks), sourced there to a tracker. UNVERIFIED |
| GPT-5.6 Sol (9 Jul 2026) | Terminal-Bench 2.1 88.8% (Sol Ultra 91.9%); SWE-Bench Pro 64.6%; OSWorld 2.0 65.7%; DeepSWE v1.1 72.7%; later-quoted Terminal-Bench 4.0 37.3%. OpenAI published an audit on 8 Jul 2026 saying about 30% of SWE-Bench Pro tasks have flawed or misleading test setups. No GPQA, FrontierMath v1 or OSWorld-Verified figure found | V-via-search of [OpenAI GPT-5.6](https://openai.com/index/gpt-5-6/) and [OpenAI GPT-6 Astra](https://openai.com/index/gpt-6-astra/); one secondary says the 64.6% is a leaderboard figure and not from OpenAI. UNVERIFIED |
| Claude Opus 5 (24 Jul 2026) | SWE-bench Verified and Pro "not published"; Terminal-Bench 2.1 89.1% at max effort measured by Artificial Analysis (I); in later Anthropic tables: Terminal-Bench 4.0 52.3%, HLE with tools 63.6%, OSWorld 2.0 partial 74.0%, GDPval-AA v2.1 Elo 1708; FrontierMath T4 v2 73.2% per OpenAI's table | [Morph](https://www.morphllm.com/claude-benchmarks); [LLM Stats on Opus 5.5](https://llm-stats.com/blog/research/claude-opus-5-5-launch); [OpenAI GPT-6 Astra, via search](https://openai.com/index/gpt-6-astra/) |
| Claude Fable 5.1 (1 Sep 2026) | Terminal-Bench 4.0 55.8%; SWE-bench Pro 81.2%; HLE 65.6% with tools, 60.9% without; OSWorld 2.0 partial 80.7%, OSWorld 2.1 83.5%; FrontierSWE v2 56.3%; GDPval-AA v2.1 Elo 1735 (1763 in Nov table) | V-via-[LLM Stats Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch) and [LLM Stats Opus 5.5](https://llm-stats.com/blog/research/claude-opus-5-5-launch) |
| GPT-6 Astra (2 Sep 2026) | Terminal-Bench 4.0 57.9% (high); OSWorld 2.0 72.6%; FrontierMath Tier 4 v2 97.6%; DeepSWE v1.1 74.1%; ARC-AGI-3 62.7% Standard and 99.9% Adapter. No SWE-bench Pro figure found | V-via-search of [OpenAI GPT-6 Astra](https://openai.com/index/gpt-6-astra/); ARC from [ARC Prize](https://arcprize.org/leaderboard) |
| Claude Opus 5.5 (22 Sep 2026) | Announcement table: Terminal-Bench 4.0 66.4% (xhigh, safeguards on, SE ±2.6); FrontierCode v1.1 Main 54.4%; CursorBench 4.0 57.8%; AutomationBench 40.0%; HLE with tools 67.7%; Terminal-Bench-Science 0.1 58.7%; OSWorld 2.0 partial 81.8% (strict 48.7%); Chartography with tools 89.0%; GDPval-AA v2.1 Elo 1846. System card: SWE-bench Pro 89.9%; SWE-bench Multilingual 93.9%; SWE-bench Multimodal 61.4%; DeepSWE v1.1 74.2%; FrontierSWE v2 62.3%; ProgramBench 91.2%; HLE no tools 64.4%; GMMLU 94.3% | V-via-[LLM Stats on Opus 5.5](https://llm-stats.com/blog/research/claude-opus-5-5-launch) |
| Claude Sonnet 5.5 (28 Sep 2026) | Terminal-Bench 4.0 70.6%; OSWorld 2.1 80.1%; SWE-bench Pro 81.3% | V-via-[Morph](https://www.morphllm.com/claude-benchmarks); Pro figure from BenchLM via search. UNVERIFIED |
| Claude Haiku 5.5 (7 Oct 2026) | Terminal-Bench 4.0 39.2% | V-via-[Morph](https://www.morphllm.com/claude-benchmarks) |
| Gemini 4 Argon (30 Sep / 13 Oct 2026) | In Google's Carbon card: AA Index 50; Vals Index 69.2%; FrontierSWE 2 55.0%; Terminal-Bench 4.0 57.1%; Agents' Last Exam v1.1 69.0%; OSWorld-2.1 offline 74.7%; Vending-Bench 2 $13,718; ExploitGym 42.0% | V — [DeepMind model card](https://deepmind.google/models/model-cards/gemini-4-carbon/) |
| Claude Fable 5.2 (9 Nov 2026) | SWE-bench Pro 93.0%; SWE-bench Multilingual 96.6%; SWE-bench Multimodal 74.1%; Terminal-Bench 4.0 67.6% (SE about 1.8); FrontierSWE v2 69.9%; FrontierCode 2.0 49.1% (xhigh) and 45.7% (max); CursorBench 4.0 60.0%; ProgramBench 85.6%; HLE 74.2% with tools, 73.2% without; ARC-AGI-3 79.26% (high) and 65.66% (max, ARC Prize verified); OSWorld 2.1 offline 89.3% partial, 54.6% strict; Remote Labor Index 41.3%; Terminal-Bench-Science 0.1 74.6%; AutomationBench 51.4%; GDPval-AA v2.1 Elo 1831; OfficeQA Pro 72.9%. All at max effort with safeguards on unless noted | V-via-[LLM Stats on Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch) |
| Gemini 4 Carbon (10 Nov 2026) | AA Index v5.0 59; Vals Index v2.2 70.4%; SWE-sweep 9.6%; FrontierSWE 2 61.2%; Terminal-Bench 4.0 (AA) 65.2%; Agents' Last Exam v1.1 77.4%; OSWorld-2.1 offline 81.5%; AutomationBench 53.9%; Vending-Bench 2 $16,484; Chartography 72.5%; GraphWalks 96.2%; RiemannBench 80.0%; Terminal-Bench-Science 0.1 64.8%; CWE-bench 71.0%; ExploitGym 54.8%; SEC-bench Pro 88.2% | V — [DeepMind model card](https://deepmind.google/models/model-cards/gemini-4-carbon/) |
| GPT-6.2 Astra and Sol (17 Nov 2026) | Agents' Last Exam v1.1 (+5.2 points over GPT-6 Astra, 5.5 points ahead of Fable 5.2); Harvey LAB-AA; internal GDPval-v2 (+6.2 points over GPT-6 Astra with 22% fewer output tokens); AA-3D Elo 1,318 (Sol 1,259, Fable 5.2 1,271); Terminal-Bench-Science (+9 points); Vals Science Index; FrontierCode 2.0; internal ExploitBench above 50%. Absolute scores mostly in charts | V-via-[The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/) |

**What was dropped**

- Anthropic did not publish SWE-bench Verified, GPQA Diamond, MMMLU, tau-bench or ARC-AGI results for Opus 5.5; SWE-bench Multilingual and Multimodal took the place of Verified — [codersera, via search](https://codersera.com/blog/claude-opus-5-5-complete-guide-2026/amp/); consistent with the benchmark list in [LLM Stats on Opus 5.5](https://llm-stats.com/blog/research/claude-opus-5-5-launch)
- For Claude Opus 5 (24 July 2026), SWE-bench Verified and SWE-bench Pro were "not published" — [Morph](https://www.morphllm.com/claude-benchmarks)
- Google's Gemini 4 Carbon model card contains no SWE-bench Verified, SWE-bench Pro, GPQA Diamond, HLE, ARC-AGI or Terminal-Bench 2.x row — [DeepMind model card](https://deepmind.google/models/model-cards/gemini-4-carbon/)
- Coverage of the GPT-6.2 launch lists no SWE-bench (any variant), GPQA, ARC-AGI, FrontierMath Tiers 1-4 or OSWorld number from OpenAI — [The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/)
- Anthropic's Opus 4.7 post already carried a footnote that memorization screens flagged some SWE-bench Verified, Pro and Multilingual problems — [Anthropic](https://www.anthropic.com/news/claude-opus-4-7)
- Zvi Mowshowitz's review of the Fable/Mythos 5.2 system card quotes none of the standard capability benchmarks; the card's emphasis is METR AI R&D acceleration (1.88x point estimate, 95% CI 1.62x to 2.28x), cyber ranges, and alignment evaluations, and ExploitBench is described as "essentially saturated" — [Zvi Mowshowitz](https://thezvi.substack.com/p/fable-and-mythos-52-the-system-card)

### Inferences
- The visualization's five legacy columns cannot be filled for any model after mid-2026 from vendor sources. A second table keyed to the benchmarks that labs now report (Terminal-Bench 4.0, OSWorld 2.1, SWE-bench Pro, HLE, ARC-AGI-2/3, AA index) is the only way to carry the series to November 2026.
- SWE-bench Pro is being reported by Anthropic only. OpenAI's July 2026 audit of the benchmark and the absence of a Pro number in the GPT-6 and GPT-6.2 launches suggest OpenAI has stopped treating it as valid, in the same way it earlier stopped reporting SWE-bench Verified.
- Each lab's November table leans on benchmarks run by outside owners (Artificial Analysis, Vals, Cognition, Proximal, Zapier, Scale, ARC Prize) and reported in the vendor's table. The vendor/independent distinction is blurrier than in 2025: the benchmark is third-party but the harness, effort setting and selection of which runs to show are the vendor's.

### Gaps
- GPT-5.2 (11 Dec 2025), Claude Opus 4.5 (24 Nov 2025), Gemini 3 Pro (18 Nov 2025), GPT-5.2-Codex and GPT-5.3-Codex launch tables were not re-fetched this session. From my training knowledge, not verified today: GPT-5.2 Thinking reported SWE-bench Verified 80.0%, SWE-Bench Pro 55.6%, GPQA Diamond 92.4%, ARC-AGI-2 52.9%, FrontierMath T1-3 40.3%, GDPval 70.9%, AIME 2025 100%; Opus 4.5 reported SWE-bench Verified 80.9%, Terminal-Bench 2.0 59.3%, OSWorld 66.3%, ARC-AGI-2 37.6%; Gemini 3 Pro reported SWE-bench Verified 76.2%, GPQA Diamond 91.9%, HLE 37.5%, ARC-AGI-2 31.1%, Terminal-Bench 2.0 54.2%; GPT-5.3-Codex reported SWE-Bench Pro 56.8%, Terminal-Bench 2.0 77.3%, OSWorld-Verified 64.7%. The ARC-AGI-2 values match today's ARC Prize board; the rest need a primary-source check.
- Every OpenAI primary page returned 403; all OpenAI vendor figures here come through Vellum, The Decoder or search summaries.
- Anthropic's Opus 4.7 benchmark table is an image; figures come through Vellum. One aggregator (Morph) lists Opus 4.7 OSWorld-Verified as 82.3%, which conflicts with the 78.0% in both the Vellum and OpenAI-sourced tables; I treat 78.0% as correct and 82.3% as an aggregator error.
- GPT-5.6 Terra/Luna, GPT-6 Sol/Luna, GPT-6.1 Sol/Terra, Gemini 3.5 to 3.8 Flash, Gemini 4 Neon and Hydrogen: launch-reported benchmarks not researched.
- Exact launch dates conflict across sources for Opus 4.8, GPT-5.6, Opus 5.5 and Gemini 4 Argon (see timeline bullet).

## Are the four suspect values listed above correct? Give the verified figures.

### Takeaway
Two are wrong and two are right. The GPQA figures of 73.8 (GPT-5.3-Codex) and 74.1 (Sonnet 4.6) are not supported: Sonnet 4.6's vendor figure is 89.9%, and GPT-5.3-Codex has no confirmed vendor GPQA figure, with aggregators showing 91.5% to 92.6%. Opus 4.7 SWE-Bench Pro 64.3% and GPT-5.5 Terminal-Bench 2.0 82.7% are the correct vendor-reported figures, but neither has a matching independent measurement at that level.

### Cited Findings

| Suspect value | Verdict | Verified figure | Config and provenance | Source |
|---|---|---|---|---|
| GPT-5.3-Codex GPQA Diamond 73.8 | Not supported | No vendor figure confirmed. Aggregators list 91.5% (xhigh, no tools; datalearner and one other board) and 92.6% (labelled self-reported, dated 5 Mar 2026). | Treat the cell as empty or "about 91.5, third-party, UNVERIFIED" | [datalearner, via search](https://www.datalearner.com/en/ai-models/compare/gpt-5-3-codex/vs/gpt-5-2-codex); [benchlm, via search](https://benchlm.ai/models/gpt-5.3-codex) |
| Claude Sonnet 4.6 GPQA Diamond 74.1 | Wrong | 89.9% | Vendor-reported in Anthropic's Sonnet 4.6 system card (17 Feb 2026), per multiple secondary sources; Opus 4.6 is 91.3% in the same table. One page does list 74.1%, which is the likely origin of the bad value | [search summary citing system card](https://officechai.com/2026/02/17/claude-sonnet-4-6-benchmarks/); [Anthropic system card PDF, not opened](https://www-cdn.anthropic.com/78073f739564e986ff3e28522761a7a0b4484f84.pdf) |
| Claude Opus 4.7 SWE-Bench Pro 64.3 | Correct as a vendor figure | 64.3% (Opus 4.6 53.4%, GPT-5.4 57.7%, Gemini 3.1 Pro 54.2%, Mythos Preview 77.8%) | Anthropic-reported, Anthropic harness; footnote says memorization screens flagged some problems and the gain over Opus 4.6 holds when they are excluded. The same 64.3% appears in OpenAI's GPT-5.5 comparison table. No Scale Labs standardized entry exists for Opus 4.7 | [Vellum](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained); [Anthropic](https://www.anthropic.com/news/claude-opus-4-7); [Vellum GPT-5.5](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5); [Scale Labs](https://labs.scale.com/leaderboard/swe_bench_pro_public) |
| GPT-5.5 Terminal-Bench 2.0 82.7 | Correct as a vendor figure | 82.7% (GPT-5.4 75.1%, Opus 4.7 69.4%, Gemini 3.1 Pro 68.5%) | OpenAI-reported, OpenAI's own evaluation with the Codex harness; reasoning effort not stated in sources I could read. The public tbench.ai board is reported to list Codex CLI with GPT-5.5 at 82.0% | [Vellum GPT-5.5](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5); [marc0.dev leaderboard, via search](https://hn.jakechampion.name/reader/https://www.marc0.dev/en/leaderboard) |

- The Terminal-Bench 2.0 comparison in OpenAI's table is not like-for-like: Anthropic's 69.4% for Opus 4.7 used the Terminus-2 harness with thinking disabled, averaged over five attempts per task, and Anthropic's own table flags GPT-5.4's 75.1% as coming from a self-reported harness — [Anthropic](https://www.anthropic.com/news/claude-opus-4-7); [Vellum](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained)
- Anthropic's Opus 4.7 post states that Opus 4.6's CyberGym score was revised from 66.6 to 73.8 — [Anthropic](https://www.anthropic.com/news/claude-opus-4-7)

### Inferences
- The two bad GPQA values (73.8 and 74.1) are about 16 to 18 points below every credible figure for models of that generation, which all sit between 89.9% and 94.6%. They are most likely another benchmark's number pasted into the GPQA column. The value 73.8 coincides exactly with Opus 4.6's revised CyberGym score, which may be a coincidence or may indicate the kind of column mix-up involved.
- The Sonnet 4.6 row also needs its ARC-AGI-2 note checked: the system-card figure is 58.3% and the ARC Prize board shows 60.4%.

### Gaps
- I did not open OpenAI's GPT-5.3-Codex launch post (403). My recollection is that the post reported no GPQA Diamond figure at all, which would make any GPQA value for that model third-party. This needs a manual check of openai.com.
- I did not open the Sonnet 4.6 system card PDF to read 89.9% directly; the figure rests on several secondary sources agreeing and citing the card.
- I could not read tbench.ai directly, so the 82.0% leaderboard figure for GPT-5.5 is second-hand.

## Where do vendor-reported and independently measured scores disagree, and by how much?

### Takeaway
The largest disagreement is on SWE-bench Pro, where vendor scaffolds run roughly 2 to 30 points above Scale's standardized harness and the top of the vendor series (93.0%) is more than 30 points above the top of the independent series (61.5%), with no overlap in models after April 2026. Elsewhere the gaps are single digits and come mostly from harness and effort settings, and labs also publish different numbers for each other's models.

### Cited Findings

| Benchmark | Model | Vendor figure | Independent figure | Gap | Source |
|---|---|---|---|---|---|
| SWE-bench Pro | Claude Opus 4.6 | 53.4% (Anthropic) | 51.90 ± 3.61 (Scale, thinking, mini-swe-agent) | 1.5 points, inside the CI | [Vellum](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained); [Scale Labs](https://labs.scale.com/leaderboard/swe_bench_pro_public) |
| SWE-bench Pro | GPT-5.4 | 57.7% (OpenAI) | 59.10 ± 3.56 (Scale, xHigh) | Independent is 1.4 points higher | same |
| SWE-bench Pro | Gemini 3.1 Pro | 54.2% (Google) | 46.10 ± 3.60 (Scale, thinking) | 8.1 points | same |
| SWE-bench Pro | frontier, Nov 2026 | 93.0% Fable 5.2; 89.9% Opus 5.5 (Anthropic) | 61.50 ± 3.10 Muse Spark 1.1 is Scale's top entry; no Scale run of any Anthropic 5.x model | Not directly comparable; 31.5 points between the tops of the two series | [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch); [Scale Labs](https://labs.scale.com/leaderboard/swe_bench_pro_public) |
| Terminal-Bench 2.0 | GPT-5.5 | 82.7% (OpenAI) | 82.0% (tbench.ai, Codex CLI, second-hand) | 0.7 points | [Vellum GPT-5.5](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5); [marc0.dev, via search](https://hn.jakechampion.name/reader/https://www.marc0.dev/en/leaderboard) |
| Terminal-Bench-Science 0.1 | GPT-6.2 Astra | about 77% (OpenAI chart) | 71.43% (Vals) | about 5.5 points | [VentureBeat, via search](https://venturebeat.com/technology/essentially-unusable-openai-launches-gpt-6-2-astra-and-sol-to-negative-reception-from-ai-power-users); [Vals, via search](https://www.vals.ai/models/openai_gpt-6.2-astra) |
| ARC-AGI-2 | Claude Sonnet 4.6 | 58.3% (system card) | 60.4% (ARC Prize) | 2.1 points | [officechai](https://officechai.com/2026/02/17/claude-sonnet-4-6-benchmarks/); [ARC Prize](https://arcprize.org/leaderboard) |
| ARC-AGI-2 | GPT-5.4 | 73.3% (OpenAI table) | 74.0% (ARC Prize) | 0.7 points | [Vellum GPT-5.5](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5); [ARC Prize](https://arcprize.org/leaderboard) |
| ARC-AGI-2 | Claude Opus 4.6 | 68.8% (Anthropic) | 69.2% (ARC Prize, 120K) | 0.4 points | [officechai, via search](https://officechai.com/2026/02/17/claude-sonnet-4-6-benchmarks/); [ARC Prize](https://arcprize.org/leaderboard) |
| ARC-AGI-3 Standard | Claude Fable 5.2 | 79.26% at high effort; 65.66% at max effort (described as ARC Prize verified) | 81.2% on the ARC Prize board | 1.9 points vs high; 15.5 points vs max | [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch); [ARC Prize](https://arcprize.org/leaderboard) |
| OSWorld-Verified | Claude Sonnet 4.6 | 72.5% (Anthropic) | 72.1% (OSWorld leaderboard per an aggregator) | 0.4 points | [search summary](https://officechai.com/2026/02/17/claude-sonnet-4-6-benchmarks/) |

**Vendors disagree with each other about the same model**

- GPT-6 Astra on Terminal-Bench-Science 0.1: 68.1% in Anthropic's table, 63.3% in Google's — [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch); [DeepMind](https://deepmind.google/models/model-cards/gemini-4-carbon/)
- GPT-6 Astra on Terminal-Bench 4.0: 57.9% (OpenAI-run, high effort) vs 59.1% (Artificial Analysis-run, in Google's table) — same sources
- GPT-6 Astra on OSWorld 2.1 offline: 79.5% in Anthropic's table vs 80.9% in Google's — same sources
- Claude Opus 5.5 on Terminal-Bench 4.0: 66.4% (Anthropic, xhigh) vs 59.6% (Google's table, AA-run): 6.8 points — same sources
- Claude Fable 5.1 on Terminal-Bench 4.0: 55.8% (Anthropic) vs 52.0% (Google's table) — same sources
- Claude Fable 5.1 on Terminal-Bench-Science: 52.6% (Anthropic) vs 43.3% (Google's table): 9.3 points — same sources
- Anthropic's own numbers for one model moved between launches: Opus 5.5 GDPval-AA v2.1 Elo 1846 in September, 1866 in November; OSWorld 81.8% on v2.0 in September, 87.2% on v2.1 offline in November — [LLM Stats on Opus 5.5](https://llm-stats.com/blog/research/claude-opus-5-5-launch); [LLM Stats on Fable 5.2](https://llm-stats.com/blog/research/claude-fable-5-2-launch)

**Scaffold and effort effects that are larger than model-to-model gaps**

- ARC-AGI-3: GPT-6 Astra scores 62.7% on the Standard harness and 99.9% on the Provider Adapter harness, a 37-point swing; Claude Sonnet 5.5 goes from 24.3% to 72.4% — [ARC Prize](https://arcprize.org/leaderboard)
- Fable 5.2 scores lower at max effort than at xhigh on FrontierCode 2.0 (45.7% vs 49.1%) and lower at max than at high on ARC-AGI-3 (65.66% vs 79.26%) — [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch)
- OSWorld 2.1 partial-credit vs strict-pass scoring: Fable 5.2 89.3% vs 54.6% — [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch)
- Morph's summary is that vendor scaffolds score 15 to 30 points above Scale's standardized harness on SWE-bench Pro — [Morph](https://www.morphllm.com/claude-benchmarks)
- Fable 5.2's public deployment falls back to Opus 4.8 on some requests (53% of attempts in one Gray Swan prompt-injection test), and Artificial Analysis labels its Anthropic rows "Default Fallback"; Mythos 5.2 without safeguards scores 70.5% on Terminal-Bench 4.0 against Fable 5.2's 67.6% — [search summary of Notebookcheck](https://www.notebookcheck.net/Claude-Fable-5-2-fallbacks-make-AI-agents-more-vulnerable.1446771.0.html); [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models); [LLM Stats](https://llm-stats.com/blog/research/claude-fable-5-2-launch)
- Artificial Analysis found GPT-6.2 Astra flat on its Coding Agent Index against GPT-6 Astra and GPT-6.2 Sol down 3 points against GPT-6.1 Sol, while OpenAI's launch materials emphasise gains — [The Decoder](https://the-decoder.com/openai-launches-gpt-6-2-astra-and-sol-with-lower-api-prices-and-some-benchmark-gains/)

### Inferences
- For models through April 2026, vendor and Scale SWE-bench Pro figures agree within the confidence interval for OpenAI and Anthropic and differ by 8 points for Google. The widely quoted "vendor numbers are 15 to 30 points inflated" claim is not supported for those models by the Scale data; the large gap is between the newest vendor numbers and a Scale board that has not run those models.
- For the lecture, any cell after April 2026 on SWE-bench Pro should be labelled "vendor scaffold". A single line connecting 64.3% (Opus 4.7, April) to 93.0% (Fable 5.2, November) is a vendor-only series with no independent confirmation above 61.5%.
- Cross-lab comparison tables are unreliable to roughly ±5 points on agentic benchmarks even within one month, given how far the same model's score moves between two labs' tables.

### Gaps
- No independent SWE-bench Verified (swebench.com or Epoch) or independent GPQA Diamond (Epoch) figures were retrieved, so vendor-vs-independent gaps on those two legacy benchmarks are not quantified here.
- No independent HLE figures (Scale/CAIS board) were retrieved to compare with Anthropic's 74.2%.
- Epoch's FrontierMath runs vs OpenAI's reported FrontierMath figures were not compared.

## For each of the five legacy benchmarks (MMLU, GPQA, SWE-bench Verified, HumanEval, MATH/AIME), when was the last frontier launch that reported it?

### Takeaway
On the evidence found, GPQA Diamond was last reported at a frontier launch by Claude Opus 4.8 (about 1 June 2026, 93.6%) and SWE-bench Verified by Claude Fable 5 and Sonnet 5 (June 2026, 95.0% and 85.2%); both figures come from one aggregator and need primary confirmation. MMLU survives only as multilingual variants in Anthropic system cards (MMMLU through Opus 4.7, GMMLU for Opus 5.5), and I found no launch in the December 2025 to November 2026 window that reported HumanEval or MATH.

### Cited Findings

| Legacy benchmark | Last frontier launch found reporting it | Score | Confidence | Source |
|---|---|---|---|---|
| GPQA Diamond | Claude Opus 4.8, 28 May / 1 Jun 2026. Before that: GPT-5.5 (23 Apr 2026) 93.6%, Opus 4.7 (16 Apr 2026) 94.2% | 93.6% | Medium for Opus 4.8 (aggregator only); high that it was still reported in April 2026 | [Morph](https://www.morphllm.com/claude-benchmarks); [Vellum GPT-5.5](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5) |
| SWE-bench Verified | Claude Sonnet 5, 30 Jun 2026 (85.2%); Claude Fable 5, 9 Jun 2026 (95.0%). Opus 5 (24 Jul 2026) did not publish one. Last OpenAI-comparable entry in April tables: none for GPT-5.4 or GPT-5.5 | 85.2% / 95.0% | Medium (aggregator only) | [Morph](https://www.morphllm.com/claude-benchmarks); [Vellum](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained) |
| MMLU | Original MMLU: no launch in the window found. Multilingual MMMLU: Opus 4.7 91.5%, Gemini 3.1 Pro 92.6% (April 2026 table). GMMLU (42 languages): Opus 5.5 94.3% in the system card, 22 Sep 2026 | see cells | High for the variants; original MMLU last-report date not established | [Vellum](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained); [LLM Stats on Opus 5.5](https://llm-stats.com/blog/research/claude-opus-5-5-launch) |
| HumanEval | None found in the window | — | Last-report date not established | — |
| MATH / AIME | None found by search in the window. Math reporting moved to FrontierMath (GPT-5.4, GPT-5.5, GPT-6 Astra), ArXivMath (Opus 5.5: 91.2% no tools, 96.9% with tools) and RiemannBench (Gemini 4 Carbon 80.0%) | — | Last-report date not established by search | [Vellum GPT-5.5](https://www.vellum.ai/md/blog/everything-you-need-to-know-about-gpt-5-5); [LLM Stats on Opus 5.5](https://llm-stats.com/blog/research/claude-opus-5-5-launch); [DeepMind](https://deepmind.google/models/model-cards/gemini-4-carbon/) |

- GPT-5.4 and GPT-5.5 have no SWE-bench Verified entry in the April 2026 comparison tables, while Anthropic and Google models do, which shows OpenAI had stopped reporting it by March 2026 — [Vellum](https://website.vellum.ai/blog/claude-opus-4-7-benchmarks-explained)
- Secondary commentary in 2026 describes MMLU as above 92% for every frontier system by Q1 2026, HumanEval as saturated and contaminated, and AIME 2025 as 98%+ and saturated; none of these sources names a lab disclosure — [app-lab.ai, via search](https://app-lab.ai/blog/ai-model-benchmarks-explained/)
- By the September 2026 Opus 5.5 launch, SWE-bench Verified, GPQA Diamond, MMMLU and ARC-AGI were all absent from Anthropic's reporting — [codersera, via search](https://codersera.com/blog/claude-opus-5-5-complete-guide-2026/amp/)

### Inferences
- The five legacy columns ended in this order: HumanEval and original MMLU before the window opened; MATH/AIME around the turn of 2025-26; SWE-bench Verified for OpenAI by March 2026 and for Anthropic after June 2026; GPQA Diamond after about June 2026. From July 2026 onward no flagship launch found reports any of the five.
- GPQA Diamond topped out in a 93.6% to 94.6% band across four labs' models between February and June 2026 with no further movement, which is the signature of a ceiling (label noise) and explains why it was dropped. SWE-bench Verified ended at 95.0%.
- The visualization can state truthfully that the empty cells are structural, and can show the last reported value with its date as an end marker for each legacy column.

### Gaps
- No source found that directly answers "last launch to report" for original MMLU, HumanEval or MATH/AIME. From my training knowledge, not verified today: OpenAI's GPT-5.2 launch (11 Dec 2025) reported AIME 2025 at 100%, which would make it the last AIME report I know of; HumanEval and original MMLU were last seen in flagship launch tables around 2024 (GPT-4o / Claude 3.5 Sonnet generation); I am not aware of any 2025-26 flagship that reported the MATH dataset. These three statements need primary-source checks before publication.
- Whether Gemini 3.5/3.7/3.8 Flash model cards or Grok 4.5 to 4.7 launches reported GPQA Diamond or SWE-bench Verified after June 2026 was not checked; if any did, the "last reported" dates above move later.
- The Opus 4.8 GPQA (93.6%) and SWE-bench Verified (88.6%), and the Fable 5 (95.0%) and Sonnet 5 (85.2%) SWE-bench Verified figures rest on Morph alone and should be confirmed against Anthropic's system cards at anthropic.com/system-cards.
