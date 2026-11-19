# Verification pass: LLM progress update late 2026

Checked 19 November 2026 against primary sources. Scope: the "Open conflicts and items to verify" table in `reports/LLM progress update late 2026.md`, plus the priority items named in the verification brief.

Verdict key:

- CONFIRMED-PRIMARY: the claimed value was read on the owner's own page, data file, system card, changelog, paper or repository.
- CORRECTED: a primary source was read and gives a different value. Use the verified value.
- SECONDARY-ONLY: no primary source could be read. The value rests on press or a third-party tracker.
- UNVERIFIABLE: no source could be traced in this pass. Do not put it on a slide.

How blocked sources were reached: openai.com returns 403 to direct fetches, so the three OpenAI posts were read from Internet Archive snapshots dated 17 November 2026 (raw `id_` captures of the original pages). ARC Prize and Epoch pages render tables client-side, so their underlying JSON and CSV files were downloaded directly. Anthropic system cards were downloaded as PDFs and searched as text. cra.org returns 403 to scripted fetches and was read through a page-summarising fetch tool, so its figures are one step less direct than the rest. api-docs.deepseek.com refused every connection.

## Priority 1: ARC-AGI-2 and ARC-AGI-3

Finding on the conflict: both researchers were right, about two different boards. `arcprize.org/leaderboard` is ARC Prize's Verified Leaderboard (the site navigation labels it "Verified"), and every ARC-AGI-1, 2 and 3 row on it is run by ARC Prize on a semi-private set. `arcprize.org/leaderboard/community` is a separate Community Leaderboard whose ARC-AGI-3 rows are self-reported scores on the public demo set. The "results due 4 December 2026" notice refers to the ARC Prize 2026 competition, not to the Verified Leaderboard.

| item | claimed value | verdict | verified value | source URL | note |
|---|---|---|---|---|---|
| Which board carries the 2026 lab-model ARC-AGI-3 rows | Disputed: independent entry vs self-reported community entry | CONFIRMED-PRIMARY | Verified Leaderboard, dataset id `v3_Semi_Private`, run by ARC Prize | https://arcprize.org/leaderboard ; https://arcprize.org/media/data/evaluations.json ; https://arcprize.org/policy | ARC's testing policy states that the semi-private set is the one used for frontier model testing on the Verified Leaderboard |
| ARC-AGI-3 top score, Standard harness | Claude Fable 5.2, 81.2% | CONFIRMED-PRIMARY | 81.2% at xhigh effort, entry dated 2026-11-09, run cost $21.9K | https://arcprize.org/media/data/evaluations.json | Same model: 79.3% high, 73.3% medium, 65.7% max, 52.0% low |
| Fable 5.2 ARC-AGI-3, vendor statement | 79.26% high, 65.66% max, "ARC Prize verified" | CONFIRMED-PRIMARY | 79.26% (Standard) and 97.72% (Provider Adapter) at high; 65.66% and 94.90% at max | https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card (section 8.15) | Anthropic reports ARC Prize's numbers. The 81.2% xhigh run is on the board but not in the card |
| ARC-AGI-3 top score, Provider Adapter harness | GPT-6.2 Astra 100.0% | CONFIRMED-PRIMARY | 100.0% at xhigh, entry dated 2026-11-17 | https://arcprize.org/media/data/evaluations.json | Standard-harness best for the same model is 70.3% (max) |
| GPT-6 Astra harness swing | 62.7% Standard, 99.9% Adapter | CONFIRMED-PRIMARY | 62.7% is the max-effort Standard run. 99.9% is the high-effort Adapter run. At max effort the Adapter run is 98.6% | https://arcprize.org/media/data/evaluations.json | The "37-point swing" compares different effort levels. Same-effort gap at max is 35.9 points |
| ARC-AGI-3 scores at launch | All frontier models under 1% in March 2026 | CONFIRMED-PRIMARY | Gemini 3.1 Pro 0.4%, GPT-5.4 0.2%, Grok 4.20 0.1% (entries dated 2026-03-05); Opus 4.6 0.5% | https://arcprize.org/media/data/evaluations.json | The notes' 0.37/0.26/0.25/0 figures are finer-grained launch values from secondary coverage. The benchmark launch date of 25 March 2026 was not re-checked |
| Community-board ARC-AGI-3 entries | Self-reported, up to 99.9% (July), 95.3% Human Intelligence Harness (April) | CORRECTED | Top entry is Tycho at 100.0% (2026-07-29). Retrodict 99.9% (2026-07-19). Human Intelligence Harness 95.3% (2026-04-14). All on "ARC-AGI-3 Public Demo" | https://arcprize.org/leaderboard/community | The page states that scores are self-reported unless noted, and that only ARC-AGI-1 and 2 semi-private results are run and verified by ARC Prize |
| "Official results due 4 December" | Applies to ARC-AGI-3 scores | CORRECTED | Applies to the ARC Prize 2026 competition only | https://arcprize.org/leaderboard (site banner) | Site banner says ARC Prize 2026 has finished and results come on 4 December 2026 |
| ARC-AGI-2 top score | GPT-6.2 Astra 95.8% | CONFIRMED-PRIMARY | 95.8% at max effort, entry dated 2026-11-17, $0.97 per task ($24.2K is the leaderboard's cost column for the ARC-AGI-3 run) | https://arcprize.org/media/data/evaluations.json | Next: GPT-6 Astra 95.0%, Gemini 4 Carbon and GPT-6.1 Sol 94.2%, Fable 5.2 93.8%, Opus 5.5 93.3% |
| ARC-AGI-2, December 2025 starting point | 54.2% (GPT-5.2 Pro) | CONFIRMED-PRIMARY | 54.2%, GPT-5.2 Pro (High), entry dated 2025-12-11 | https://arcprize.org/media/data/evaluations.json | Poetiq's Gemini 3 Pro refinement harness was at 54.0% on 2025-12-04 |
| ARC-AGI-2 "saturated mid-2026, human-panel average passed" | mid-2026 | CORRECTED | Verified frontier first exceeded 60% on 2026-02-03 (GPT-5.2 refinement harness, 72.9%) and 2026-02-05 for a lab model (Opus 4.6, 69.2%). First above 90%: GPT-5.6 Sol, 92.5%, 2026-07-09 | https://arcprize.org/media/data/evaluations.json | ARC's data file lists the human panel at 100%. The "60% average human" figure was not located in the data files read. If the slide says "human average passed", the date is February 2026. If it says "above 90%", the date is July 2026 |
| ARC-AGI-1 ceiling | Six or more models tie at 98.5% | CONFIRMED-PRIMARY | 98.5% for Fable 5, GPT-6 Astra, Opus 5.5, Gemini 3.8 Flash, GPT-6.1 Sol, Gemini 4 Argon, Fable 5.2, Gemini 4 Carbon, GPT-6.2 Astra | https://arcprize.org/media/data/evaluations.json | Human panel on the same set: 98.0% |
| Sonnet 4.6 ARC-AGI-2 | 58.3% (system card) vs 60.4% (ARC Prize) | CONFIRMED-PRIMARY | Both. Summary table says 58.3%. Section 2.7 says ARC Prize measured 60.42% with 120k thinking tokens at High effort | https://www-cdn.anthropic.com/78073f739564e986ff3e28522761a7a0b4484f84.pdf | Board value 60.4% |
| GPT-5.4 ARC-AGI-2 | 73.3% (OpenAI) vs 74.0% (ARC Prize) | CONFIRMED-PRIMARY | OpenAI table: 73.3% "ARC-AGI-2 (Verified)". ARC Prize: 74.0% at xhigh, 83.3% for GPT-5.4 Pro | https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/ ; https://arcprize.org/media/data/evaluations.json | |
| ARC Prize dates vs lab dates | ARC dates are entry dates and can trail launch | CONFIRMED-PRIMARY | ARC `modelReleaseDate`: Opus 4.8 2026-06-01, Grok 4.5 2026-07-16, GLM-5 2026-02-20, GLM-5.2 2026-06-13, GPT-5.4 2026-03-04, GPT-6 Astra 2026-09-02 | https://arcprize.org/media/data/models.json | Can also lead: GPT-5.4 and GPT-6 Astra are one day before the API date |

### ARC-AGI-2 score history, November 2025 to November 2026

Best verified configuration per model, semi-private set. `is_new_frontier` marks rows that raised the running maximum (the frontier before this window was 29.4%). Date is ARC Prize's entry date for the model.

```csv
leaderboard_entry_date,provider,best_config,arc_agi_2_semi_private_pct,cost_per_task_usd,is_new_frontier,source_url
2025-11-13,OpenAI,"GPT-5.1 (Thinking, High)",17.6,1.17,,https://arcprize.org/media/data/evaluations.json
2025-11-18,Google,Gemini 3 Pro,31.1,0.81,yes,https://arcprize.org/media/data/evaluations.json
2025-11-24,Anthropic,"Opus 4.5 (Thinking, 64K)",37.6,2.4,yes,https://arcprize.org/media/data/evaluations.json
2025-12-01,DeepSeek,Deepseek V3.2,4.0,0.12,,https://arcprize.org/media/data/evaluations.json
2025-12-04,poetiq,Gemini 3 Pro (Refinement),54.0,30.57,yes,https://arcprize.org/media/data/evaluations.json
2025-12-11,OpenAI,GPT-5.2,0.8,0.08,,https://arcprize.org/media/data/evaluations.json
2025-12-11,OpenAI,GPT-5.2 (XHigh),52.9,1.9,,https://arcprize.org/media/data/evaluations.json
2025-12-11,OpenAI,GPT-5.2 Pro (High),54.2,15.72,yes,https://arcprize.org/media/data/evaluations.json
2025-12-17,Google,Gemini 3 Flash Preview (High),33.6,0.23,,https://arcprize.org/media/data/evaluations.json
2026-01-27,Moonshot AI,Kimi K2.5,11.8,0.28,,https://arcprize.org/media/data/evaluations.json
2026-02-03,johan_land,GPT-5.2 (Refinement),72.9,38.99,yes,https://arcprize.org/media/data/evaluations.json
2026-02-05,Anthropic,"Claude Opus 4.6 (120K, High)",69.2,3.47,,https://arcprize.org/media/data/evaluations.json
2026-02-12,Google,Gemini 3 Deep Think (2/26),84.6,13.62,yes,https://arcprize.org/media/data/evaluations.json
2026-02-12,Google,Gemini 3 Deep Think (Preview) ²,45.1,77.16,,https://arcprize.org/media/data/evaluations.json
2026-02-12,Minimax,Minimax M2.5,4.9,0.17,,https://arcprize.org/media/data/evaluations.json
2026-02-17,Anthropic,Claude Sonnet 4.6 (High),60.4,2.7,,https://arcprize.org/media/data/evaluations.json
2026-02-19,Google,Gemini 3.1 Pro (Preview),77.1,0.96,,https://arcprize.org/media/data/evaluations.json
2026-02-20,Z.ai,GLM-5,4.9,0.27,,https://arcprize.org/media/data/evaluations.json
2026-03-04,OpenAI,GPT-5.4 (XHigh),74.0,1.52,,https://arcprize.org/media/data/evaluations.json
2026-03-04,OpenAI,GPT-5.4 Pro (XHigh),83.3,16.41,,https://arcprize.org/media/data/evaluations.json
2026-03-09,xAI,Grok 4.20 (Reasoning),65.1,0.92,,https://arcprize.org/media/data/evaluations.json
2026-03-17,OpenAI,GPT-5.4 Mini (XHigh),18.9,0.75,,https://arcprize.org/media/data/evaluations.json
2026-03-17,OpenAI,GPT-5.4 Nano (XHigh),5.7,0.16,,https://arcprize.org/media/data/evaluations.json
2026-04-16,Anthropic,Claude 4.7 (Max),75.8,7.43,,https://arcprize.org/media/data/evaluations.json
2026-04-22,OpenAI,GPT-5.5 (XHigh),85.0,1.87,yes,https://arcprize.org/media/data/evaluations.json
2026-04-23,OpenAI,GPT-5.5 Pro (High),84.6,10.51,,https://arcprize.org/media/data/evaluations.json
2026-05-19,Google,Gemini 3.5 Flash (High),72.1,0.85,,https://arcprize.org/media/data/evaluations.json
2026-06-01,Anthropic,Claude Opus 4.8 (High),72.1,2.74,,https://arcprize.org/media/data/evaluations.json
2026-06-09,Anthropic,Claude Fable 5 (Max),89.2,5.45,yes,https://arcprize.org/media/data/evaluations.json
2026-06-13,Z.ai,GLM-5.2,22.8,0.25,,https://arcprize.org/media/data/evaluations.json
2026-07-09,OpenAI,GPT-5.6 Luna (Max),59.5,0.67,,https://arcprize.org/media/data/evaluations.json
2026-07-09,OpenAI,GPT-5.6 Sol (Max),92.5,1.44,yes,https://arcprize.org/media/data/evaluations.json
2026-07-09,OpenAI,GPT-5.6 Terra (Max),83.9,1.09,,https://arcprize.org/media/data/evaluations.json
2026-07-15,Thinking Machines,Inkling,36.5,0.64,,https://arcprize.org/media/data/evaluations.json
2026-07-16,xAI,Grok 4.5 (High),52.6,0.78,,https://arcprize.org/media/data/evaluations.json
2026-07-16,Moonshot AI,Kimi K3 (Max),60.4,1.59,,https://arcprize.org/media/data/evaluations.json
2026-07-21,Google,Gemini 3.5 Flash-Lite (High),10.3,0.14,,https://arcprize.org/media/data/evaluations.json
2026-07-21,Google,Gemini 3.6 Flash (High),60.4,0.61,,https://arcprize.org/media/data/evaluations.json
2026-07-24,Anthropic,Claude Opus 5 (Max),90.4,2.06,,https://arcprize.org/media/data/evaluations.json
2026-07-30,OpenAI,GPT-5.6 Luna 2026-07-30 (Max),59.6,0.18,,https://arcprize.org/media/data/evaluations.json
2026-07-30,Thinking Machines,Inkling Small (XHigh),40.1,0.23,,https://arcprize.org/media/data/evaluations.json
2026-07-31,DeepSeek,DeepSeek V4 Flash 0731 (Max),61.4,0.04,,https://arcprize.org/media/data/evaluations.json
2026-08-11,xAI,Grok 4.6 (XHigh),67.1,0.76,,https://arcprize.org/media/data/evaluations.json
2026-08-13,DeepSeek,DeepSeek V4 Pro 0813 (Max),61.3,0.6,,https://arcprize.org/media/data/evaluations.json
2026-08-13,Google,Gemini 3.7 Flash (High),84.6,0.25,,https://arcprize.org/media/data/evaluations.json
2026-08-14,Dots Studio,Dots3-Note Preview (Max),76.8,0.08,,https://arcprize.org/media/data/evaluations.json
2026-08-14,Alibaba,Qwen3.8-27B (XHigh),42.4,0.45,,https://arcprize.org/media/data/evaluations.json
2026-08-26,Z.ai,GLM-5.3-Flash (Max),65.8,0.09,,https://arcprize.org/media/data/evaluations.json
2026-09-01,Anthropic,Claude Fable 5.1 (Max),90.0,4.49,,https://arcprize.org/media/data/evaluations.json
2026-09-02,OpenAI,GPT-6 Astra (Max),95.0,1.12,yes,https://arcprize.org/media/data/evaluations.json
2026-09-02,Google,Gemini 3.8 Flash (High),89.2,0.4,,https://arcprize.org/media/data/evaluations.json
2026-09-10,DeepSeek,DeepSeek V4.1 Flash (Max),72.9,0.13,,https://arcprize.org/media/data/evaluations.json
2026-09-21,xAI,Grok 4.7 (XHigh),61.4,2.01,,https://arcprize.org/media/data/evaluations.json
2026-09-22,Anthropic,Claude Opus 5.5 (High),93.3,0.41,,https://arcprize.org/media/data/evaluations.json
2026-09-22,OpenAI,GPT-6 Luna (Max),59.3,0.06,,https://arcprize.org/media/data/evaluations.json
2026-09-22,OpenAI,GPT-6 Sol (Max),89.6,0.44,,https://arcprize.org/media/data/evaluations.json
2026-09-28,Anthropic,Claude Sonnet 5.5 (XHigh),83.9,0.55,,https://arcprize.org/media/data/evaluations.json
2026-09-29,OpenAI,GPT-6.1 Sol (Max),94.2,0.25,,https://arcprize.org/media/data/evaluations.json
2026-10-07,Anthropic,Claude Haiku 5.5 (XHigh),61.3,0.08,,https://arcprize.org/media/data/evaluations.json
2026-10-13,Google,Gemini 4 Argon (High),91.2,0.32,,https://arcprize.org/media/data/evaluations.json
2026-10-15,Meta AI,Muse Spark Open (XHigh),57.5,0.73,,https://arcprize.org/media/data/evaluations.json
2026-10-15,NVIDIA,Nemotron 3.5 Super VL (Medium),1.9,0.02,,https://arcprize.org/media/data/evaluations.json
2026-10-16,Reflection,Beam 1.0 (XHigh),23.5,0.61,,https://arcprize.org/media/data/evaluations.json
2026-10-17,DeepSeek,DeepSeek V4.1 Flash 1017 (Max),78.1,0.16,,https://arcprize.org/media/data/evaluations.json
2026-10-19,Inception,Mercury 3 Preview (High),61.8,0.06,,https://arcprize.org/media/data/evaluations.json
2026-11-05,Thinking Machines,Inkling 2 Small (XHigh),81.7,0.27,,https://arcprize.org/media/data/evaluations.json
2026-11-09,Anthropic,Claude Fable 5.2 (XHigh),93.8,0.98,,https://arcprize.org/media/data/evaluations.json
2026-11-10,Google,Gemini 4 Carbon (Medium),94.2,0.38,,https://arcprize.org/media/data/evaluations.json
2026-11-17,OpenAI,GPT-6.2 Astra (Max),95.8,0.97,yes,https://arcprize.org/media/data/evaluations.json
2026-11-17,OpenAI,GPT-6.2 Sol (Max),85.8,0.26,,https://arcprize.org/media/data/evaluations.json
```

### ARC-AGI-3 verified scores by harness

Best configuration per model and harness, semi-private set. The Opus 4.6 row carries an entry date of 2025-12-17 in ARC's file, which predates the benchmark's public launch and should be treated as a data-entry quirk.

```csv
leaderboard_entry_date,provider,harness,best_config,arc_agi_3_semi_private_pct,run_cost_usd,source_url
2025-12-17,Anthropic,standard,Anthropic Opus 4.6 (Max),0.5,8866,https://arcprize.org/media/data/evaluations.json
2026-03-05,Google,standard,Gemini 3.1 Pro (Preview),0.4,2214,https://arcprize.org/media/data/evaluations.json
2026-03-05,OpenAI,standard,GPT-5.4 (High),0.2,5187,https://arcprize.org/media/data/evaluations.json
2026-03-05,xAI,standard,Grok 4.20 (Beta Reasoning),0.1,3775,https://arcprize.org/media/data/evaluations.json
2026-04-16,Anthropic,standard,Opus 4.7 (High),0.2,10000,https://arcprize.org/media/data/evaluations.json
2026-04-23,OpenAI,standard,GPT-5.5 (High),0.4,10000,https://arcprize.org/media/data/evaluations.json
2026-06-01,Anthropic,standard,Claude Opus 4.8 (High),1.5,10000,https://arcprize.org/media/data/evaluations.json
2026-07-09,OpenAI,standard,GPT-5.6 Luna (Low),0.2,2307,https://arcprize.org/media/data/evaluations.json
2026-07-09,OpenAI,standard,GPT-5.6 Sol (Max),7.8,25064,https://arcprize.org/media/data/evaluations.json
2026-07-09,OpenAI,standard,GPT-5.6 Terra (Max),0.8,7918,https://arcprize.org/media/data/evaluations.json
2026-07-16,xAI,standard,Grok 4.5 (High),0.3,6893,https://arcprize.org/media/data/evaluations.json
2026-07-24,Anthropic,standard,Claude Opus 5 (High),30.2,20657,https://arcprize.org/media/data/evaluations.json
2026-08-11,xAI,standard,Grok 4.6 (XHigh),2.1,5612,https://arcprize.org/media/data/evaluations.json
2026-09-02,Google,standard,Gemini 3.8 Flash (High),10.4,4398,https://arcprize.org/media/data/evaluations.json
2026-09-02,Google,provider_adapter,Gemini 3.8 Flash - Provider Adapter (High),35.0,4522,https://arcprize.org/media/data/evaluations.json
2026-09-02,OpenAI,standard,GPT-6 Astra (Max),62.7,26098,https://arcprize.org/media/data/evaluations.json
2026-09-02,OpenAI,provider_adapter,GPT-6 Astra - Provider Adapter (High),99.9,18817,https://arcprize.org/media/data/evaluations.json
2026-09-10,DeepSeek,standard,DeepSeek V4.1 Flash (Max),0.9,1165,https://arcprize.org/media/data/evaluations.json
2026-09-10,DeepSeek,provider_adapter,DeepSeek V4.1 Flash - Provider Adapter (Low),3.3,878,https://arcprize.org/media/data/evaluations.json
2026-09-21,xAI,standard,Grok 4.7 (XHigh),1.8,2732,https://arcprize.org/media/data/evaluations.json
2026-09-21,xAI,provider_adapter,Grok 4.7 - Provider Adapter (High),10.0,4774,https://arcprize.org/media/data/evaluations.json
2026-09-22,OpenAI,standard,GPT-6 Luna (XHigh),0.2,263,https://arcprize.org/media/data/evaluations.json
2026-09-22,OpenAI,provider_adapter,GPT-6 Luna - Provider Adapter (Max),0.6,237,https://arcprize.org/media/data/evaluations.json
2026-09-22,OpenAI,standard,GPT-6 Sol (Max),4.6,5554,https://arcprize.org/media/data/evaluations.json
2026-09-22,OpenAI,provider_adapter,GPT-6 Sol - Provider Adapter (Max),23.0,8722,https://arcprize.org/media/data/evaluations.json
2026-09-28,Anthropic,standard,Claude Sonnet 5.5 (XHigh),24.3,7394,https://arcprize.org/media/data/evaluations.json
2026-09-28,Anthropic,provider_adapter,Claude Sonnet 5.5 - Provider Adapter (XHigh),72.4,8170,https://arcprize.org/media/data/evaluations.json
2026-09-29,OpenAI,standard,GPT-6.1 Sol (Max),52.7,7632,https://arcprize.org/media/data/evaluations.json
2026-09-29,OpenAI,provider_adapter,GPT-6.1 Sol - Provider Adapter (XHigh),96.4,4360,https://arcprize.org/media/data/evaluations.json
2026-10-07,Anthropic,standard,Claude Haiku 5.5 (Max),0.5,388,https://arcprize.org/media/data/evaluations.json
2026-10-07,Anthropic,provider_adapter,Claude Haiku 5.5 - Provider Adapter (Max),2.8,437,https://arcprize.org/media/data/evaluations.json
2026-10-13,Google,standard,Gemini 4 Argon (Low),49.8,5821,https://arcprize.org/media/data/evaluations.json
2026-10-13,Google,provider_adapter,Gemini 4 Argon - Provider Adapter (Low),97.5,4770,https://arcprize.org/media/data/evaluations.json
2026-10-15,Meta AI,standard,Muse Spark Open (XHigh),0.1,3908,https://arcprize.org/media/data/evaluations.json
2026-10-15,Meta AI,provider_adapter,Muse Spark Open - Provider Adapter (XHigh),0.4,2996,https://arcprize.org/media/data/evaluations.json
2026-10-17,DeepSeek,standard,DeepSeek V4.1 Flash 1017 (Max),0.2,1004,https://arcprize.org/media/data/evaluations.json
2026-10-17,DeepSeek,provider_adapter,DeepSeek V4.1 Flash 1017 - Provider Adapter (Max),5.8,1179,https://arcprize.org/media/data/evaluations.json
2026-10-19,Inception,standard,Mercury 3 Preview (High),0.1,333,https://arcprize.org/media/data/evaluations.json
2026-10-19,Inception,provider_adapter,Mercury 3 Preview - Provider Adapter (High),0.2,299,https://arcprize.org/media/data/evaluations.json
2026-11-05,Thinking Machines,standard,Inkling 2 Small (XHigh),0.3,858,https://arcprize.org/media/data/evaluations.json
2026-11-05,Thinking Machines,provider_adapter,Inkling 2 Small - Provider Adapter (XHigh),2.6,704,https://arcprize.org/media/data/evaluations.json
2026-11-09,Anthropic,standard,Claude Fable 5.2 (XHigh),81.2,21949,https://arcprize.org/media/data/evaluations.json
2026-11-09,Anthropic,provider_adapter,Claude Fable 5.2 - Provider Adapter (High),97.7,18625,https://arcprize.org/media/data/evaluations.json
2026-11-10,Google,standard,Gemini 4 Carbon (Low),65.1,7244,https://arcprize.org/media/data/evaluations.json
2026-11-10,Google,provider_adapter,Gemini 4 Carbon - Provider Adapter (Medium),99.1,4560,https://arcprize.org/media/data/evaluations.json
2026-11-17,OpenAI,standard,GPT-6.2 Astra (Max),70.3,24169,https://arcprize.org/media/data/evaluations.json
2026-11-17,OpenAI,provider_adapter,GPT-6.2 Astra - Provider Adapter (XHigh),100.0,4112,https://arcprize.org/media/data/evaluations.json
2026-11-17,OpenAI,standard,GPT-6.2 Sol (Max),54.9,5466,https://arcprize.org/media/data/evaluations.json
2026-11-17,OpenAI,provider_adapter,GPT-6.2 Sol - Provider Adapter (Max),98.2,1494,https://arcprize.org/media/data/evaluations.json
```

## Priority 2: Epoch Capabilities Index

| item | claimed value | verdict | verified value | source URL | note |
|---|---|---|---|---|---|
| ECI leader, 19 Nov 2026 | GPT-6.2 Astra 174, Fable 5.2 about level | CONFIRMED-PRIMARY | GPT-6.2 Astra 174.17 (170.29 to 178.58); Claude Fable 5.2 173.50 (170.09 to 177.36); Gemini 4 Carbon 169.78; GPT-6 Astra 169.20 | https://epoch.ai/data/eci_scores.csv | Intervals overlap almost entirely. "About level" is the right wording |
| Post-reasoning frontier slope | 14 to 17 points per year since Sept 2024 | CONFIRMED-PRIMARY | 14 per year (Data Insight, 1 Sep 2026). 15.7 (13.8 to 19.2) frequentist and 16.6 (14.6 to 18.7) Bayesian (methodology post, 4 Nov 2026) | https://epoch.ai/data-insights/eci-frontier-trend ; https://epoch.ai/publications/eci-bayesian-methodology | Epoch's split is by model type, not calendar year: "Reasoning (from o1-mini)" vs "Pre-reasoning (GPT-4 to GPT-4.5)". The non-reasoning line runs to February 2025 |
| Pre-reasoning frontier slope | 6 to 8 points per year | CONFIRMED-PRIMARY | 6 per year (Data Insight). 6.2 (2.8 to 7.8) frequentist and 8.0 (5.4 to 9.7) Bayesian | same | |
| ECI values differ by vintage | GPT-5.5 Pro 159.35 (May), 161.71 (Sept); method changed in November | CONFIRMED-PRIMARY for Sept and Nov. UNVERIFIABLE for May | 161.71 in the 1 Sep 2026 Data Insight table. 162.77 in the current download. Method change published 2026-11-04 | https://epoch.ai/data-insights/eci-frontier-trend ; https://epoch.ai/data/eci_scores.csv | The May 159.35 vintage could not be retrieved. GPT-5 is pinned at 150 and Claude 3.5 Sonnet at 130 in every vintage |
| "2026 models sit on or slightly above the line" | Researcher reading | CONFIRMED-PRIMARY for the data; the fit is my arithmetic | Ordinary least squares on the current-vintage frontier points gives 16.9 per year from o1-mini onward (17 points) and 17.6 per year from GPT-5.2 Pro onward (9 points) | https://epoch.ai/data/eci_scores.csv | My calculation, not Epoch's. It supports "no slowdown" and does not establish a speed-up |

### ECI frontier, current vintage (use this one for a single plotted line)

Running maximum over all models with a release date and score in Epoch's file as downloaded 19 November 2026 (257 scored models, 2023-02-24 to 2026-11-17). The full per-model file is at the source URL.

```csv
release_date,model,organization,eci,eci_ci_low,eci_ci_high,vintage,source_url
2023-02-24,LLaMA-65B,Meta AI,101.38,92.98,108.66,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2023-03-14,GPT-4 (Mar 2023),OpenAI,121.58,117.72,125.02,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2024-01-25,GPT-4 Turbo (Nov 2023),OpenAI,124.75,121.47,127.68,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2024-02-29,Claude 3 Opus,Anthropic,125.58,122.65,128.17,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2024-04-09,GPT-4 Turbo (Apr 2024),OpenAI,125.82,122.84,128.62,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2024-05-13,GPT-4o (May 2024),OpenAI,128.13,125.37,130.68,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2024-06-20,Claude 3.5 Sonnet,Anthropic,130.0,,,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2024-09-12,o1-mini,OpenAI,135.28,133.1,137.29,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2024-12-17,o1,OpenAI,141.18,139.48,142.79,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2025-03-31,Gemini 2.5 Pro (Mar 2025),Google DeepMind,144.05,142.08,146.0,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2025-04-16,o3,OpenAI,147.05,145.6,148.55,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2025-06-10,o3-pro,OpenAI,147.46,145.58,149.37,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2025-08-07,GPT-5,OpenAI,150.0,,,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2025-10-07,GPT-5 Pro,OpenAI,151.27,149.32,153.32,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2025-11-18,Gemini 3 Pro,Google DeepMind,153.04,151.45,154.78,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2025-12-11,GPT-5.2 Pro,OpenAI,157.31,155.11,159.77,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2026-03-05,GPT-5.4 Pro,OpenAI,160.32,157.87,163.03,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2026-04-23,GPT-5.5 Pro,OpenAI,162.77,160.14,165.77,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2026-06-09,Claude Fable 5,Anthropic,164.21,161.78,166.86,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2026-07-24,Claude Opus 5,Anthropic,164.74,162.3,167.66,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2026-09-01,Claude Fable 5.1,Anthropic,167.09,164.43,170.11,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2026-09-03,GPT-6 Astra,OpenAI,169.2,166.33,172.48,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2026-11-09,Claude Fable 5.2,Anthropic,173.5,170.09,177.36,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
2026-11-17,GPT-6.2 Astra,OpenAI,174.17,170.29,178.58,download 2026-11-19 (Bayesian method),https://epoch.ai/data/eci_scores.csv
```

### ECI frontier as published with the stated slopes (1 September 2026 vintage)

These are the points Epoch fitted for the "14 vs 6 points per year" statement. Values differ from the current vintage by up to about 4 points for 2023 models and about 1 to 2 points for 2026 models. Do not mix the two blocks in one line.

```csv
release_date,model,organization,eci,eci_ci90_low,eci_ci90_high,series,vintage,source_url
2023-03-14,GPT-4 (Mar 2023),OpenAI,126.19,120.78,130.06,Non-reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2024-02-29,Claude 3 Opus,Anthropic,126.51,122.14,128.87,Non-reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2024-04-09,GPT-4 Turbo (Apr 2024),OpenAI,127.61,123.00,128.84,Non-reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2024-05-13,GPT-4o (May 2024),OpenAI,128.80,124.17,130.67,Non-reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2024-06-20,Claude 3.5 Sonnet,Anthropic,130.00,,,Non-reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2024-09-24,Gemini 1.5 Pro (Sept 2024),Google DeepMind,132.69,128.52,133.75,Non-reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2024-10-22,Claude 3.5 Sonnet (October 2024),Anthropic,134.29,129.85,138.73,Non-reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2024-12-11,Gemini 2.0 Flash (Dec 2024),Google DeepMind,135.16,124.33,136.92,Non-reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2025-02-05,Gemini 2.0 Flash (Feb 2025),Google DeepMind,135.80,132.72,137.61,Non-reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2025-02-27,GPT-4.5,OpenAI,137.63,134.93,139.43,Non-reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2024-09-12,o1-mini,OpenAI,136.64,132.97,138.02,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2024-12-17,o1,OpenAI,142.67,140.92,143.72,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2025-03-31,Gemini 2.5 Pro (Mar 2025),Google DeepMind,144.63,142.62,147.29,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2025-04-16,o3,OpenAI,147.06,145.34,148.51,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2025-06-10,o3-pro,OpenAI,147.51,145.97,151.30,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2025-08-07,GPT-5,OpenAI,150.00,,,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2025-10-07,GPT-5 Pro,OpenAI,150.29,148.88,152.47,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2025-11-18,Gemini 3 Pro,Google DeepMind,153.06,151.28,155.05,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2025-12-11,GPT-5.2 Pro,OpenAI,155.07,153.04,157.24,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2026-02-05,GPT-5.3 Codex,OpenAI,156.22,153.70,159.65,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2026-03-05,GPT-5.4 Pro,OpenAI,158.55,156.10,161.24,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2026-04-23,GPT-5.5 Pro,OpenAI,161.71,158.95,164.88,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
2026-06-09,Claude Fable 5,Anthropic,162.48,159.33,165.76,Reasoning SOTA,Data Insight 2026-09-01,https://epoch.ai/data-insights/eci-frontier-trend
```

## Priority 3: SWE-bench Pro, vendor-reported vs Scale-measured

Scale figures are from the public-set leaderboard, read 19 November 2026. Asterisked Scale rows use the mini-swe-agent harness. Vendor figures are each lab's own harness on the same 731-task public set.

| item | claimed value | verdict | verified value | source URL | note |
|---|---|---|---|---|---|
| Claude Opus 4.6 | Vendor 53.4%, Scale 51.90 ± 3.61 | CONFIRMED-PRIMARY | Vendor 53.4% (Opus 4.7 system card table). Scale 51.90 ± 3.61 (thinking) | https://www.anthropic.com/claude-opus-4-7-system-card ; https://labs.scale.com/leaderboard/swe_bench_pro_public | Gap 1.5 points, inside the interval |
| GPT-5.4 | Vendor 57.7%, Scale 59.10 ± 3.56 | CONFIRMED-PRIMARY | Vendor 57.7% (OpenAI launch post, 5 Mar 2026). Scale 59.10 ± 3.56 (xHigh) | https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/ ; Scale URL above | Scale is 1.4 points higher |
| Gemini 3.1 Pro | Vendor 54.2%, Scale 46.10 ± 3.60 | CONFIRMED-PRIMARY | Vendor 54.2% (Google model card, "single attempt"). Scale 46.10 ± 3.60 (thinking) | https://deepmind.google/models/model-cards/gemini-3-1-pro/ ; Scale URL above | Gap 8.1 points, outside the interval |
| Gemini 3 Pro | Not in report | CONFIRMED-PRIMARY | Google's card lists 43.3%. Scale lists 43.30 ± 3.60 | same | Identical, so Google is quoting Scale. Not an independent pair |
| GPT-5.2-Codex | Not in report | CONFIRMED-PRIMARY | Vendor 56.4% (xhigh, GPT-5.3-Codex post appendix). Scale 41.04 ± 3.57 | https://web.archive.org/web/2026/https://openai.com/index/introducing-gpt-5-3-codex/ ; Scale URL above | Gap 15.4 points. This pair contradicts "vendor and Scale agree within the interval for OpenAI" |
| GPT-5.2 | Not in report | CONFIRMED-PRIMARY | Vendor 55.6% (xhigh). Scale 29.94 ± 2.15 | same | Gap 25.7 points. Scale's legend says some rows ran with a capped cost and 50-turn limit, which likely applies here, so do not present this gap as a clean harness comparison |
| Claude Opus 4.5, Sonnet 4.5, Haiku 4.5 | Not in report | UNVERIFIABLE (vendor side) | Scale: 45.89, 43.60, 39.45 (each ± about 3.6) | Scale URL above | No vendor SWE-bench Pro figure for these models was found in the cards read |
| Scale's top entry and coverage | 61.5%, no model after April except Meta's | CONFIRMED-PRIMARY | Muse Spark 1.1 at 61.50 ± 3.10, added 2026-07-09. The newest non-Meta rows were added 2026-04-08 | Scale URL above | Scale's private-set board tops out at 51.5 (Muse Spark 1.1) |
| Anthropic's later vendor figures | Opus 5.5 89.9%, Fable 5.2 93.0% | CONFIRMED-PRIMARY | Opus 4.7 64.3, Sonnet 5 63.2, Opus 4.8 69.2, Fable 5 80, Mythos 5 80.3, Opus 5 79.2, Fable 5.1 81.2, Opus 5.5 89.9, Fable 5.2 93.0 | Anthropic system cards for each model, https://www.anthropic.com/system-cards | None of these models has a Scale run. Anthropic's Opus 5 card also lists GPT-5.6 Sol at 64.6 |
| OpenAI's last vendor figure | 58.6% (GPT-5.5) | CONFIRMED-PRIMARY | 58.6% | https://web.archive.org/web/20261117144117/https://openai.com/index/introducing-gpt-5-5/ | OpenAI's July audit says frontier pass rates on the public split rose from 23.3% to 80.3% in eight months |

## Priority 4: benchmark introduction and saturation dates

Introduction dates are first arXiv submission or the owner's launch post. "Saturated or retired" dates are only marked confirmed where an owner or major evaluator said so on a dated page. For MMLU, HumanEval and MATH no such statement was found, so the report's dates remain the researchers' judgement.

| item | claimed value | verdict | verified value | source URL | note |
|---|---|---|---|---|---|
| MMLU introduced | Sep 2020 | CONFIRMED-PRIMARY | 2020-09-07 | https://arxiv.org/abs/2009.03300 | |
| MMLU saturated | 2023 to 2024 | UNVERIFIABLE | No retirement statement found. In Epoch's external-results file the best recorded score is 88.1% (GPT-4o, Nov 2024) and GPT-4 reached 86.4% in March 2023 | https://epoch.ai/data/benchmark_data.zip (mmlu_external.csv) | Label as "plateau, researcher judgement" |
| HumanEval introduced | Jul 2021 | CONFIRMED-PRIMARY | 2021-07-07 | https://arxiv.org/abs/2107.03374 | |
| HumanEval saturated | mid-2024 | UNVERIFIABLE | No source traced. Not in Epoch's data. No Anthropic system card from Sonnet 5 onward mentions it | | |
| MATH introduced | Mar 2021 | CONFIRMED-PRIMARY | 2021-03-05 | https://arxiv.org/abs/2103.03874 | |
| MATH saturated | Sep 2024 | CORRECTED (weakly) | On Epoch's own MATH Level 5 runs the first score above 90% is o1 at 94.7% (2024-12-17), above 95% is o3-mini (2025-01-31), above 97% is o4-mini (2025-04-16) | https://epoch.ai/data/benchmark_data.zip (math_level_5.csv) | September 2024 is o1-preview's launch month. Epoch's runs put the ceiling at December 2024 to April 2025. Level 5 subset only |
| ARC-AGI-1 introduced | Nov 2019 | CONFIRMED-PRIMARY | 2019-11-05 | https://arxiv.org/abs/1911.01547 | |
| ARC-AGI-1 saturated | Dec 2024 | SECONDARY-ONLY | The o3-preview 87.5% result (Dec 2024) was not re-read on arcprize.org in this pass. On the Verified board, the first listed model at 90% or above is GPT-5.2 Pro (90.5%, 2025-12-11) and the first at 95% or above is Gemini 3 Deep Think (96.0%, 2026-02-12) | https://arcprize.org/media/data/evaluations.json | Two defensible dates: Dec 2024 (preview result that prompted ARC-AGI-2) or Dec 2025 to Feb 2026 (public models pass 90% and 95%) |
| GPQA Diamond introduced | Nov 2023 | CONFIRMED-PRIMARY | 2023-11-20 | https://arxiv.org/abs/2311.12022 | |
| GPQA Diamond dropped by Artificial Analysis | 4 Sep 2026 | CONFIRMED-PRIMARY | Index v4.2 changelog, published 2026-09-04, removes GPQA Diamond and describes it as saturated | https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2 | |
| GPQA Diamond, last frontier launch reporting it | Claude Opus 4.8, about 1 June 2026, 93.6% | CORRECTED | Claude Mythos 5, 94.1%, system card of 9 June 2026, with a statement that Anthropic considers GPQA Diamond saturated and plans to stop reporting it | https://www.anthropic.com/claude-fable-5-mythos-5-system-card (section 8.8) | Opus 4.8 at 93.6% is confirmed in its own card (28 May 2026), with Opus 4.7 at 94.2% and Gemini 3.1 Pro at 94.3%. GPQA is absent from the Sonnet 5, Opus 5, Opus 5.5 and Fable 5.2 cards |
| SWE-bench Verified introduced | Aug 2024 | CONFIRMED-PRIMARY | 2024-08-13 per Epoch metadata; OpenAI's 2026 post says it created the benchmark in 2024 | https://epoch.ai/data/benchmark_data.zip (benchmark_metadata.csv) | Original 2024 OpenAI post not re-read |
| SWE-bench Verified abandoned by OpenAI | 23 Feb 2026; 59.4% of 138 audited tasks flawed | CONFIRMED-PRIMARY | Post dated February 23, 2026. It states that 59.4% of the 138 audited problems had material issues in test design or problem description. The 138 were 27.6% of the set, chosen because o3 did not solve them consistently | https://web.archive.org/web/20261117145122/https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ | The post also says all frontier models tested could reproduce gold patches or verbatim problem text for some tasks. Sections name GPT-5.2, Claude Opus 4.5 and Gemini 3 Flash |
| SWE-bench Verified, last frontier launch reporting it | Fable 5 (9 June, 95.0%) and Sonnet 5 (30 June, 85.2%) | CORRECTED | Claude Opus 5, 96.0%, system card of 24 July 2026. Sonnet 5 85.2% (30 June), Mythos 5 95.5% and Fable 5 95 (9 June), Opus 4.8 88.6% (28 May), Opus 4.7 87.6% | Anthropic system cards, https://www.anthropic.com/system-cards | Absent from the Opus 5.5 (22 Sep) and Fable 5.2 (9 Nov) cards |
| OSWorld introduced | Apr 2024 | CONFIRMED-PRIMARY | 2024-04-11 | https://arxiv.org/abs/2404.07972 | |
| OSWorld human baseline passed | Mar 2026, vendor-reported | CONFIRMED-PRIMARY | OpenAI, 5 March 2026: GPT-5.4 at 75.0% on OSWorld-Verified, described as above human performance of 72.4% | https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/ | Vendor claim on the Verified variant |
| ARC-AGI-2 introduced | Mar 2025 | CONFIRMED-PRIMARY | 2025-03-24 per Epoch metadata | https://epoch.ai/data/benchmark_data.zip (benchmark_metadata.csv) | ARC Prize launch post not re-read. Saturation date: see Priority 1 |
| SWE-bench Pro introduced | Sep 2025 | CONFIRMED-PRIMARY | 2025-09-21 | https://arxiv.org/abs/2509.16941 | |
| SWE-bench Pro withdrawn by OpenAI | 8 Jul 2026, about 30% broken | CONFIRMED-PRIMARY | Post dated July 8, 2026, estimating about 30% of tasks are broken. Automated pipeline flagged 200 tasks (27.4%); human annotation found 249 (34.1%) | https://web.archive.org/web/20261117004847/https://openai.com/index/separating-signal-from-noise-coding-evaluations/ | |
| SWE-bench Pro rated Flawed by Epoch | 1 Sep 2026; 83 of 100; Datacurve 87% | CONFIRMED-PRIMARY for date, verdict and 83 of 100. CORRECTED for Datacurve | Reviewed Sep. 1, 2026, verdict Flawed. Gabor audit (24 Feb 2026): 83 of 100 had issues. Datacurve (26 May 2026): 24% false negatives and 8.5% false positives | https://epoch.ai/benchmarks/swe-bench-pro/review | The "87% of improper passes via git history" figure is not on Epoch's page. Epoch credits reward-hacking documentation to Poolside |
| Terminal-Bench 2.0 introduced | Nov 2025 | CONFIRMED-PRIMARY | 2025-11-07 | https://www.tbench.ai/news | Paper: arXiv 2601.11868, 2026-01-17 |
| Terminal-Bench 2.0 superseded | mid-2026 | CONFIRMED-PRIMARY | 2.1 on 2026-05-06 (fixes 28 tasks); 3.0 on 2026-07-30 (the post says many tasks have become saturated); 4.0 on 2026-08-28; 4.1 on 2026-11-09 | https://www.tbench.ai/news ; https://www.tbench.ai/news/terminal-bench-3-0 | Five instruments, not four. The saturation statement is in the 3.0 post and refers to 2.1-era tasks |
| Humanity's Last Exam introduced | Not in lifespan table | CONFIRMED-PRIMARY | 2025-01-24 (arXiv); Epoch lists 2025-01-23 | https://arxiv.org/abs/2501.14249 | Top vendor score: Fable 5.2 at 73.2% without tools and 74.2% with tools (system card). Not saturated |
| FrontierMath introduced | Not in lifespan table | CONFIRMED-PRIMARY | 2024-11-07 (arXiv). Tier 4 first run 2025-07-11. Tiers 1 to 3 v2 and Tier 4 v2 released 2026-06-12 | https://arxiv.org/abs/2411.04872 ; https://epoch.ai/data/benchmark_data.zip | Tier 4 v2 is at ceiling in Epoch's own runs: see Priority 7 |

## Priority 5: release dates in conflict

| item | claimed value | verdict | verified value | source URL | note |
|---|---|---|---|---|---|
| Claude Opus 4.8 | 05-28 vs 06-01 | CONFIRMED-PRIMARY | 2026-05-28 | https://platform.claude.com/docs/en/release-notes/overview | 06-01 is ARC Prize's entry date. Epoch also lists 05-28 |
| GPT-5.6 Sol, Terra, Luna | API 07-09; gated preview announced 06-26 | CONFIRMED-PRIMARY for 07-09. SECONDARY-ONLY for 06-26 | 2026-07-09, release of the GPT-5.6 model family | https://developers.openai.com/api/docs/changelog | No 26 June entry exists in the API changelog. The announcement post was not retrievable |
| Claude Opus 5.5 | 09-22 | CONFIRMED-PRIMARY | 2026-09-22 | https://platform.claude.com/docs/en/release-notes/overview | Same notes: Fable 5 06-09, Sonnet 5 06-30, Opus 5 07-24, Fable 5.1 09-01, Sonnet 5.5 09-28, Haiku 5.5 10-07, Fable 5.2 11-09 |
| Gemini 4 Argon | GA 10-13; limited preview 09-30 | CONFIRMED-PRIMARY for 10-13. SECONDARY-ONLY for 09-30 | 2026-10-13 GA | https://ai.google.dev/gemini-api/docs/changelog | No September entry for Argon in the changelog. Carbon GA 11-10, Hydrogen 11-12, Neon 11-18 are all confirmed there |
| Grok 4.20 | "March 2026" only; table has 03-22 | CORRECTED | 2026-03-10: entry announcing Grok 4.20 and Grok 4.20 Multi-agent as live | https://docs.x.ai/docs/release-notes | xAI's notes do give days. 03-22 is unsupported. Epoch dates the model 2026-02-17 (beta); ARC rows are dated 03-05 and 03-09 |
| GPT-5.5 | 04-23 vs 04-24 | CONFIRMED-PRIMARY | Announced 2026-04-23 (launch post date; the post says API access will follow shortly). API release 2026-04-24 | https://web.archive.org/web/20261117144117/https://openai.com/index/introducing-gpt-5-5/ ; https://developers.openai.com/api/docs/changelog | Both dates are real. Pick by the table's convention |
| DeepSeek V4 | April launch with MIT weights vs July and August dates | CORRECTED | Weights repositories `DeepSeek-V4-Pro` and `DeepSeek-V4-Flash` created 2026-04-22, licence MIT. Dated refresh builds `DeepSeek-V4-Flash-0731` (2026-07-31) and `DeepSeek-V4-Pro-0813` (2026-08-13), also MIT. V4.1 Flash 2026-09-10, V4.1 Flash 1017 on 2026-10-17 | https://huggingface.co/deepseek-ai ; https://huggingface.co/api/models?author=deepseek-ai&search=V4 | The July and August dates are refreshed snapshots, not a delayed GA. Epoch dates the original release 2026-04-24. DeepSeek's own changelog was unreachable, so the announcement day (22 to 24 April) is not pinned. The 96.4% SWE-bench Verified claim was not found anywhere primary |
| Kimi K3.1 Pro weights | Unconfirmed vs "published 4 November" | CORRECTED | Weights are public: `moonshotai/Kimi-K3.1-Pro`, 96 safetensors shards, not gated, custom licence `kimi-k3.1-pro`. Repository created 2026-11-02, last modified 2026-11-05 | https://huggingface.co/moonshotai/Kimi-K3.1-Pro | Exact day of public visibility is not recoverable from the repository (between 2 and 5 November). Epoch lists the model release as 2026-10-23, "Open weights (restricted use)". Label it open-weight with a restricted licence |
| GPT-5.4 | 03-05 vs 03-04 | CONFIRMED-PRIMARY | 2026-03-05 (launch post date and API changelog) | https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/ | 03-04 is ARC Prize's entry date |
| GPT-6 Astra | 09-03 vs 09-02 | CONFIRMED-PRIMARY | 2026-09-03 | https://developers.openai.com/api/docs/changelog | 09-02 is ARC Prize's entry date |
| Grok 4.5 | 07-08 vs 07-16 | CONFIRMED-PRIMARY | 2026-07-08 on the xAI API; EU availability 2026-07-17 | https://docs.x.ai/docs/release-notes | 07-16 is ARC Prize's entry date |
| Grok 4.6, Grok 4.7 | Month only; days from trackers | CORRECTED | Grok 4.6 on 2026-08-12. Grok 4.7 on 2026-09-21 | https://docs.x.ai/docs/release-notes | Days are in xAI's own notes |
| GLM-5 | 02-11 vs 02-20 | CORRECTED | 2026-02-12 on Z.ai's release list; weights repository created 2026-02-11 (UTC) | https://docs.z.ai/release-notes/new-released ; https://huggingface.co/zai-org/GLM-5 | 02-20 is ARC Prize's entry date |
| GLM-5.2 | 06-13 vs 06-16 | CONFIRMED-PRIMARY | 2026-06-16 (Z.ai release list and weights repository) | same | 06-13 is ARC Prize's entry date. Z.ai also lists GLM-5.3 on 2026-08-18 and GLM-5.3-Flash on 2026-08-26 |
| Kimi K3 | 07-16 vs 07-17 | SECONDARY-ONLY | 2026-07-16 (Epoch and ARC Prize agree; press mostly agrees). Weights: first public commit on 2026-07-27 | https://epoch.ai/data/benchmark_data.zip (model_metadata.csv) ; https://huggingface.co/moonshotai/Kimi-K3 | Moonshot's dated announcement was not found. Licence on the repository is custom (`kimi-k3`) |
| GPT-5.3-Codex | Announced 02-05, API 02-24 | CONFIRMED-PRIMARY | Launch post dated February 5, 2026. API release 2026-02-24 | https://web.archive.org/web/2026/https://openai.com/index/introducing-gpt-5-3-codex/ ; https://developers.openai.com/api/docs/changelog | Upgrades the announcement date from "search summary" to primary |
| Qwen4-Max | 16 Nov | CONFIRMED-PRIMARY | 2026-11-16 (`qwen4-max`, international deployment). `qwen4-max-preview` on 2026-11-11 | https://www.alibabacloud.com/help/en/model-studio/newly-released-models | API model. No Qwen4 weights repository exists under the Qwen organisation on Hugging Face |
| Mistral Large 4 | GA 5 Nov | CORRECTED | Public preview 2026-10-06 (Mistral changelog). Weights `Mistral-Large-4-1T-A52B` first public commit 2026-10-29. Changelog entry of 29 October updates `mistral-large-4` and `mistral-large-4-0` | https://docs.mistral.ai/getting-started/changelog ; https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B | No 5 November entry found. Epoch lists Preview 2026-10-06 and the release 2026-10-29, open weights with restricted use. Use 10-29 |
| Muse Spark Open | 15 Oct | CONFIRMED-PRIMARY | 2026-10-15 | https://research.meta.ai/blog/muse-spark-open | Meta's post says the weights are released that day. Repository is access-gated with a custom Muse licence |

## Priority 6: real-world series

| item | claimed value | verdict | verified value | source URL | note |
|---|---|---|---|---|---|
| Google AI-generated code, 2024 | More than a quarter (October 2024) | CONFIRMED-PRIMARY | Q3 2024 earnings remarks, 2024-10-29: more than a quarter of all new code at Google is AI-generated, then reviewed and accepted by engineers | https://blog.google/inside-google/message-ceo/alphabet-earnings-q3-2024/ | |
| Google AI-generated code, 2025 | 50% (fall 2025) | CONFIRMED-PRIMARY (retrospective) | 50% "last fall", stated by Pichai on 2026-04-22 | https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/ | No contemporaneous fall 2025 statement was found. The Q3 2025 earnings remarks contain no such figure. Plot it as "fall 2025, as stated April 2026" |
| Google AI-generated code, 2026 | 75% of new code (April 2026) | CONFIRMED-PRIMARY | 75% of all new code at Google is AI-generated and approved by engineers, per Pichai on 2026-04-22 | same | Semafor's article is dated 2026-04-24. The statement itself is 04-22 |
| Octoverse 2026: agent-started pull requests | 17% in March, more than 40% in September, about 110 million that month | CONFIRMED-PRIMARY | More than 40% of pull requests started with an agent's first draft by September 2026, up from 17% in March; 110 million in September, about six times March's volume | https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/ | Published 2026-10-28. Only these two months are given. No monthly series is published in the post, so a line between them is an interpolation |
| Octoverse 2026: merge within two weeks | Agent 90% vs about 86% for others | CONFIRMED-PRIMARY | Agent pull requests 83% in February 2026 and 90% in September 2026; comparison group about 86% in both | same | Also: 87% of agent-started pull requests change multiple files vs 79% |
| Stanford "Canaries", August 2026 | 19%, up from 15% a year earlier; earlier 13% and 16% are a different measure | CONFIRMED-PRIMARY | Employment of workers aged 22 to 25 in AI-exposed occupations is 19% below the less-exposed-peer benchmark as of June 2026 data. The same measure was 15% at the July 2025 data vintage. Earlier editions headlined regression estimates of 13% (July 2025 data) and 16% (September 2025 data) | https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf | The 15% and 19% are the same descriptive measure and can be joined. The 13% and 16% cannot. Authors call the result descriptive |
| Indeed software-development postings, low | 61.1 in May 2025 | CONFIRMED-PRIMARY | 61.10 on 2025-05-17 (seasonally adjusted, 1 Feb 2020 = 100), the all-time low of the series | https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv | Indeed Hiring Lab's public data repository |
| Indeed, July 2026 | About 72.5 | CONFIRMED-PRIMARY | Article of 2026-07-08 says postings remain 27.5% below the pre-pandemic level (index 72.5, data to June 2026). The current data file shows 73.46 on 2026-07-01 and 74.35 on 2026-07-08 | https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/ ; data URL above | The roughly one-point difference is revision of the seasonally adjusted series |
| Indeed, October 2026 | About 78 to 79 (secondary) | CONFIRMED-PRIMARY, with a correction for month-end | 78.25 on 2026-10-01, 78.65 on 2026-10-15, 81.57 on 2026-10-31, 81.71 on 2026-11-13 (latest) | data URL above | "78 to 79" holds for the first half of October. The series jumped about three points late in the month |
| Indeed, senior share of rebound | 71% | CONFIRMED-PRIMARY | 71% of the May 2025 to May 2026 increase in software development postings came from senior roles, and 37% from jobs with AI in the title | https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/ | Also: software postings up almost 15% since 24 Feb 2025 while all postings fell 7% |
| CRA Taulbee: new bachelor's enrollment | Down 12.9% | CORRECTED (rounding) | New CS majors 33,490, down 13 percent across the longitudinal cohort | https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/ | Read through a summarising fetch tool because cra.org blocks scripted access. The article gives whole percentages. 12.9% is not in the article |
| CRA Taulbee: total undergraduate CS enrollment | Down 4.1% | CORRECTED (rounding) | 169,528, down 4 percent across the longitudinal cohort | same | Bachelor's degrees awarded: 41,858, up 13%. Data are for academic year 2024-25, with new-student figures for 2025-26 |
| CRA Taulbee: master's intake from abroad | 63% from outside North America | CONFIRMED-PRIMARY | 63% of newly admitted CS master's students. Master's enrollment down about 26%, new admits down 10% | same | |
| Harvard/Jellyfish paper: sample | 718 firms | CORRECTED | Current version (14 Nov 2026): 655 firms, 720,542 workers, 445M work events, January 2021 to August 2026. First version dated 7 January 2026 | https://fion.ac/jellyfish.pdf | 718 is not in the current version and presumably belongs to an earlier draft that was not retrieved |
| Harvard/Jellyfish: code output | Lines +30%, commits +20%, pull requests +23% "after agent adoption" | CORRECTED | AI assistants, 12 months after adoption: lines +30.4%, commits +16.8%, pull requests +20.9%. AI agents, additional: lines +44.0%, commits +36.0%, pull requests opened +35.7% | same | The report's numbers resemble the assistant effects and are attributed to agents. Agent effects are larger |
| Harvard/Jellyfish: delivered work | Jira issues resolved did not move; November version +13.7% borderline | CONFIRMED-PRIMARY for the November version | Assistants: issues −1.5%, epics +3.4%. Agents: issues +13.7% (borderline significant), epics +18.0%. Employment: +3.0% (assistants), −2.6% (agents), neither significant | same | The "no measurable change, interval excludes gains above 12%" wording is from the earlier draft and is not in the current version |
| Harvard/Jellyfish: review bottleneck | Time-to-merge +49% | CORRECTED | After agent adoption, time from review submission to approval +56.1% (backlog wait +59.9%, active review +58.5%). Comments per change +38.6% | same | +49% is not in the current version |
| Harvard/Jellyfish: AI in review | 23.3% of review comments by AI by March 2026 | CONFIRMED-PRIMARY for the value. CORRECTED for the date | 23.3% of all review comments are AI-generated; 10.8% of pull requests get at least one AI comment; 79.1% of firms had used AI review tools as of July 2026 | same | The current version dates the adoption figure to July 2026 |
| METR maintainer review: sample and headline | 296 AI pull requests; roughly half of test-passing patches would not be merged | CONFIRMED-PRIMARY | 4 maintainers from 3 repositories reviewed 296 AI-generated pull requests. METR finds roughly half of test-passing SWE-bench Verified patches from mid-2024 to late-2025 agents would not be merged by maintainers | https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/ | Maintainer merge decisions average about 24 percentage points below the automated grader. Scores are normalised to a 68% golden-patch baseline |
| METR maintainer review: Sonnet 4.5 horizons | About 50 minutes automated, about 8 minutes by maintainers | CONFIRMED-PRIMARY | About 50 minutes by the automated grader and about 8 minutes by maintainer review, which METR calls roughly a 7x overstatement | same | METR flags these estimates as less stable than its main series. It is a METR "note", with less review than a research post |

### Real-world data series

Google share of new code that is AI-generated (company statements, different occasions, not a measured series):

```csv
statement_date,period_described,share_pct,qualifier_paraphrased,speaker,source_url
2024-10-29,2024-Q3,25,more than a quarter of all new code; reviewed and accepted by engineers,Sundar Pichai,https://blog.google/inside-google/message-ceo/alphabet-earnings-q3-2024/
2026-04-22,fall 2025 (retrospective),50,stated retrospectively as the level last fall,Sundar Pichai,https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/
2026-04-22,2026-04,75,75% of all new code; approved by engineers,Sundar Pichai,https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/
```

GitHub Octoverse 2026, agent pull requests (only the months GitHub states):

```csv
month,metric,value,unit,source_url
2026-03,share of pull requests started with an agent,17,percent,https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
2026-09,share of pull requests started with an agent,40,percent (stated as more than 40),https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
2026-09,agent-started pull requests,110,million,https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
2026-02,agent pull requests merged within two weeks,83,percent,https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
2026-09,agent pull requests merged within two weeks,90,percent,https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
2026-02,non-agent pull requests merged within two weeks,86,percent (about),https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
2026-09,non-agent pull requests merged within two weeks,86,percent (about),https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
```

Stanford "Canaries in the Coal Mine", employment shortfall for ages 22 to 25 in AI-exposed occupations:

```csv
data_vintage,measure,shortfall_pct,joinable_series,source_url
2025-07,descriptive gap vs less-exposed peers,15,A,https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf
2026-06,descriptive gap vs less-exposed peers,19,A,https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf
2025-07,regression estimate adjusting for firm-level shocks (earlier edition headline),13,B,https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf
2025-09,regression estimate adjusting for firm-level shocks (earlier edition headline),16,B,https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf
```

Indeed Hiring Lab, US software development job postings index (seasonally adjusted, total postings, 1 February 2020 = 100; first day of each month from January 2022, plus the latest observation; all-time low 61.10 on 2025-05-17, peak 233.82 on 2022-02-28):

```csv
date,indeed_software_dev_postings_index_sa_feb2020_100,source_url
2022-01-01,212.98,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-02-01,225.13,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-03-01,233.51,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-04-01,225.6,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-05-01,223.46,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-06-01,224.84,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-07-01,211.25,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-08-01,194.15,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-09-01,180.27,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-10-01,168.06,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-11-01,155.06,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2022-12-01,142.34,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-01-01,130.27,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-02-01,121.14,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-03-01,105.94,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-04-01,99.5,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-05-01,98.19,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-06-01,94.03,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-07-01,82.59,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-08-01,81.51,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-09-01,78.64,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-10-01,75.09,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-11-01,74.16,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2023-12-01,72.44,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-01-01,72.58,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-02-01,71.08,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-03-01,70.82,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-04-01,70.7,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-05-01,69.2,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-06-01,70.15,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-07-01,70.08,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-08-01,69.73,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-09-01,68.56,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-10-01,69.18,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-11-01,68.58,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2024-12-01,67.45,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-01-01,67.52,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-02-01,66.77,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-03-01,62.58,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-04-01,62.57,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-05-01,63.19,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-06-01,64.08,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-07-01,65.35,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-08-01,66.19,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-09-01,65.02,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-10-01,64.28,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-11-01,65.78,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2025-12-01,66.64,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-01-01,67.21,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-02-01,69.42,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-03-01,70.7,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-04-01,72.76,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-05-01,72.94,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-06-01,73.41,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-07-01,73.46,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-08-01,75.15,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-09-01,74.85,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-10-01,78.25,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-11-01,81.62,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
2026-11-13,81.71,https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/job_postings_by_sector_US.csv
```

CRA Taulbee Survey 2025 (55th survey, published June 2026; percentage changes are for the longitudinal cohort of units reporting 2020 to 2025):

```csv
metric,value,change,period,source_url
new CS bachelor's majors,33490,-13%,2025-26 intake,https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/
total CS bachelor's enrollment,169528,-4%,2025,https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/
CS bachelor's degrees awarded,41858,+13%,2024-25,https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/
total CS master's enrollment,,-26% (roughly),2025,https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/
new CS master's admits,,-10%,2025-26 intake,https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/
CS master's degrees awarded,23180,about 3% below 2024 peak,2024-25,https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/
share of new CS master's students from outside North America,63%,,2025-26 intake,https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/
total CS doctoral enrollment,16989,+5% year on year,2025,https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/
new CS doctoral enrollments,,-15%,2025-26 intake,https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/
```

Chen and Stratton, "Artificial Intelligence in the Firm: Bottlenecks in Software Production" (Harvard job-market paper, version of 14 November 2026; 655 firms, 720,542 workers):

```csv
tool_generation,outcome,effect_pct,note,source_url
AI assistants,lines of code,30.4,12 months after adoption,https://fion.ac/jellyfish.pdf
AI assistants,commits,16.8,12 months after adoption,https://fion.ac/jellyfish.pdf
AI assistants,pull requests,20.9,12 months after adoption,https://fion.ac/jellyfish.pdf
AI assistants,Jira issues resolved,-1.5,near zero,https://fion.ac/jellyfish.pdf
AI assistants,Jira epics resolved,3.4,near zero,https://fion.ac/jellyfish.pdf
AI assistants,engineering employment,3.0,rules out changes below -4.7%,https://fion.ac/jellyfish.pdf
AI agents,lines of code,44.0,additional to assistants,https://fion.ac/jellyfish.pdf
AI agents,commits,36.0,additional to assistants,https://fion.ac/jellyfish.pdf
AI agents,pull requests opened,35.7,additional to assistants,https://fion.ac/jellyfish.pdf
AI agents,Jira issues resolved,13.7,borderline significant,https://fion.ac/jellyfish.pdf
AI agents,Jira epics resolved,18.0,,https://fion.ac/jellyfish.pdf
AI agents,engineering employment,-2.6,rules out changes below -15.6%,https://fion.ac/jellyfish.pdf
AI agents,time from review submission to approval,56.1,,https://fion.ac/jellyfish.pdf
AI agents,time waiting in review backlog,59.9,,https://fion.ac/jellyfish.pdf
AI agents,time in active review,58.5,,https://fion.ac/jellyfish.pdf
AI agents,comments per code change,38.6,,https://fion.ac/jellyfish.pdf
all,share of review comments generated by AI,23.3,level not effect,https://fion.ac/jellyfish.pdf
all,share of firms that have used AI code review tools,79.1,level as of July 2026,https://fion.ac/jellyfish.pdf
```

METR maintainer review of SWE-bench Verified patches (note of 10 March 2026):

```csv
metric,value,unit,source_url
AI-generated pull requests reviewed,296,count,https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
maintainers,4,count (3 repositories),https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
human-written golden patches reviewed for noise baseline,47,count,https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
golden baseline maintainer acceptance,68,percent,https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
gap between automated grader and maintainer merge decisions,24,percentage points (about),https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
slower improvement under maintainer review,9.6,percentage points per year,https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
Claude Sonnet 4.5 50% horizon by automated grader,50,minutes (approximately),https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
Claude Sonnet 4.5 50% horizon by maintainer review,8,minutes (about),https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
```

## Priority 7: everything else on the list

| item | claimed value | verdict | verified value | source URL | note |
|---|---|---|---|---|---|
| Gemini 4 Neon tier | Unclear whether Carbon is the flagship; AA ranks Neon above Carbon | CONFIRMED-PRIMARY | Google's model list describes Carbon as its strongest reasoning model, and the Neon guide places Neon between Hydrogen and Carbon. Neon GA 2026-11-18 | https://ai.google.dev/gemini-api/docs/models ; https://ai.google.dev/gemini-api/docs/whats-new-gemini-4-neon | Carbon can be labelled Google's flagship. Neon's higher AA score is an effort artefact: Neon at xhigh scores 61.4, Carbon's highest listed effort (high) scores 60.0 |
| Microsoft MAI rows | No primary page fetched | CONFIRMED-PRIMARY for June. UNVERIFIABLE for November | Build 2026 keynote transcript, published 2026-06-02, announces MAI Thinking 1 and MAI Code 1 Flash (51% on SWE-Bench Pro on Microsoft's internal harness; rolling out to about 10% of individual Copilot users) | https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/ | The 17 November MAI Code 2 rows were not checked against a Microsoft page |
| Fable 5 SWE-bench Pro | 80.0 vs 80.3 | CORRECTED | Fable 5: 80. Mythos 5: 80.3 | https://www.anthropic.com/claude-fable-5-mythos-5-system-card (Table 8.1.A) | The two numbers belong to two models |
| Fable 5 Terminal-Bench 2.1 | 88.0, 83.1, 84.6 or unpublished | CORRECTED | Fable 5: 84.3% (with 20.9% of trials hitting a safety refusal and falling back to Opus 4.8). Mythos 5: 88.0% | same (Table 8.1.A and section 8.3) | 83.1 and 84.6 appear in the card only as unrelated cyber-evaluation figures. Terminal-Bench's own 3.0 post lists Fable 5 in Claude Code at 83.8% on 2.1 |
| Fable 5 SWE-bench Verified | 95.0% | CONFIRMED-PRIMARY | Fable 5: 95. Mythos 5: 95.5 | same | |
| Opus 4.8 legacy scores | SWE-bench Verified, GPQA 93.6% from one aggregator | CONFIRMED-PRIMARY | SWE-bench Verified 88.6, SWE-bench Pro 69.2, GPQA Diamond 93.6, OSWorld-Verified 83.4, Terminal-Bench 2.1 74.6 | https://www.anthropic.com/claude-opus-4-8-system-card (Table 8.1.A) | |
| Sonnet 5 legacy scores | SWE-bench Verified 85.2% | CONFIRMED-PRIMARY | SWE-bench Verified 85.2%, SWE-bench Pro 63.2%, Terminal-Bench 2.1 80.4% | https://www.anthropic.com/claude-sonnet-5-system-card (section 8.2) | |
| Opus 4.7 scores | SWE-bench Verified 87.6, SWE-bench Pro 64.3, OSWorld-Verified 78.0, CyberGym 73.1 | CONFIRMED-PRIMARY except CyberGym | SWE-bench Verified 87.6%, SWE-bench Pro 64.3%, OSWorld 78.0% at launch (restated as 82.8% in the Opus 4.8 card after a tool bug fix), MMMLU 91.5% | https://www.anthropic.com/claude-opus-4-7-system-card | CyberGym 73.1 was not located in the system card text (the result is shown as a figure). The launch post confirms Opus 4.6's CyberGym was revised from 66.6 to 73.8 |
| Sonnet 4.6 GPQA Diamond | 89.9% (replacing 74.1) | CONFIRMED-PRIMARY | 89.9%, averaged over 10 trials. Opus 4.6: 91.3% | https://www-cdn.anthropic.com/78073f739564e986ff3e28522761a7a0b4484f84.pdf | Google's Gemini 3.1 Pro card repeats both |
| GPT-5.3-Codex GPQA Diamond | "Leave blank, no confirmed vendor figure" | CORRECTED | 92.6% (OpenAI's GPT-5.4 launch table lists GPT-5.3-Codex at 92.6%, GPT-5.2 at 92.4%, GPT-5.4 at 92.8%, GPT-5.4 Pro at 94.4%) | https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/ | The cell can be filled with a vendor label |
| MMMLU values | Opus 4.6 91.1, Gemini 3.1 Pro 92.6 | CONFIRMED-PRIMARY | Opus 4.7 91.5%, Opus 4.6 91.1%, Gemini 3.1 Pro 92.6% | https://www.anthropic.com/claude-opus-4-7-system-card | GMMLU (a different instrument): Opus 4.7 89.9%, Opus 4.8 90.4%, Mythos 5 93.2%, Opus 5.5 94.3%, Fable 5.2 96.0% |
| OpenAI GPT-5.5 table | Terminal-Bench 2.0 82.7, SWE-bench Pro 58.6, OSWorld-Verified 78.7, GPQA 93.6, CyberGym 81.8; no SWE-bench Verified | CONFIRMED-PRIMARY | All five values as claimed. Post dated April 23, 2026 | https://web.archive.org/web/20261117144117/https://openai.com/index/introducing-gpt-5-5/ | OpenAI's table lists Claude Opus 4.7 at 69.4% on Terminal-Bench 2.0 and 78.0% on OSWorld-Verified |
| OpenAI GPT-5.4 table | SWE-bench Pro 57.7, Terminal-Bench 2.0 75.1, OSWorld-Verified 75.0, GDPval 83.0, GPQA 92.8 | CONFIRMED-PRIMARY | All as claimed. FrontierMath Tier 1 to 3 47.6%, Tier 4 27.1%. HLE without tools 39.8% | https://web.archive.org/web/20261117141647/https://openai.com/index/introducing-gpt-5-4/ | GPT-5.3-Codex scored higher than GPT-5.4 on Terminal-Bench 2.0 (77.3%) in OpenAI's own table |
| OSWorld-Verified top score | 78.7% (GPT-5.5) vs aggregator 82.8% and 90.19% | CORRECTED | Highest vendor figures found: Claude Mythos Preview 85.4%, Fable 5 and Mythos 5 85.0%, Opus 4.8 83.4%, Opus 4.7 82.8% (restated), GPT-5.5 78.7%, Gemini 3.5 Flash 78.4% | https://www.anthropic.com/claude-fable-5-mythos-5-system-card ; https://www.anthropic.com/claude-opus-4-8-system-card | 82.8% is Anthropic's restated Opus 4.7 score. 90.19% was not found in any primary source. The public os-world.github.io board was not read directly; Epoch's copy of it tops out at Sonnet 4.6, 72.1% |
| FrontierMath Tier 4 v2 | GPT-6 Astra 97.6%, not confirmed on Epoch's hub | CONFIRMED-PRIMARY | GPT-6 Astra 97.6% (high, xhigh and max) in Epoch's own results file. Fable 5.2, GPT-6.2 Astra and GPT-6.1 Sol are at 100% | https://epoch.ai/data/benchmark_data.zip (frontiermath_tier_4_v2.csv) | Tier 4 v2 is saturated on Epoch's runs. 97.6% is consistent with 40 of 41 problems |
| Terminal-Bench 4.0 release date | 28 Aug 2026, single secondary source | CONFIRMED-PRIMARY | 2026-08-28 | https://www.tbench.ai/news | |
| Terminal-Bench 4.0 vendor scores | Fable 5.2 67.6%, Opus 5.5 66.4% | CONFIRMED-PRIMARY | Fable 5.2 67.6% with safeguards enabled. Opus 5.5 66.4% at xhigh; Opus 5 52.3%; Fable 5.1 55.8%; GPT-6 Astra 57.9% | Fable 5.2 and Opus 5.5 system cards, https://www.anthropic.com/system-cards | Sonnet 5.5 at 70.6% was not checked (its card was not downloaded) |
| OSWorld 2.0 details | Single secondary source | CONFIRMED-PRIMARY (partly) | Epoch metadata: released 2026-06-26, leaderboard at osworld-v2.xlang.ai. Top entry in Epoch's copy: Claude Opus 5 (max) 31.4% binary, 68.3% partial | https://epoch.ai/data/benchmark_data.zip (osworld_2_external.csv) | Vendor tables report partial and strict separately: Opus 5.5 81.8 / 48.7; Fable 5.2 on OSWorld 2.1 offline 89.3 / 54.6. Other OSWorld 2.0 details in the notes were not re-checked |
| Fable 5.2 headline scores | HLE 74.2% with tools; OSWorld 2.1 89.3% partial and 54.6% strict; RLI 41.3%; SWE-bench Pro 93.0% | CONFIRMED-PRIMARY | All as claimed | https://www.anthropic.com/claude-fable-5-2-mythos-5-2-system-card | Epoch's file lists Fable 5.2 on RLI at 41.25% |
| Vending-Bench 2 | Gemini 4 Carbon $16,484 | CONFIRMED-PRIMARY | $16,484.21 in Epoch's external-results file; GPT-6 Astra $15,514.70 | https://epoch.ai/data/benchmark_data.zip (vending_bench_2_external.csv) | |
| Artificial Analysis index values | Fable 5.2 65, GPT-6.2 Astra 62, Neon 61, Carbon 60, Opus 5.5 59 (58 at launch), DeepSeek V4.1 Flash 33 (32) | CONFIRMED-PRIMARY | Read 19 Nov 2026, Intelligence Index v5.0.1: Fable 5.2 (max) 64.6; GPT-6.2 Astra (max) 62.1; Gemini 4 Neon (xhigh) 61.4; Gemini 4 Carbon (high) 60.0; Opus 5.5 (max) 59.1; DeepSeek V4.1 Flash 1017 (max) 32.6 | https://artificialanalysis.ai/leaderboards/models | The leaderboard rounds to whole numbers. The earlier 58 and 32 launch values were not re-checked. Every score is tied to an effort setting |
| METR 2025 paper doubling time | 212 days (CI 171 to 249), recalled | CORRECTED | The current arXiv version says approximately seven months in the abstract and gives 207 days for the 50% horizon and 204 days for the 80% horizon in the text. 212 does not appear | https://arxiv.org/abs/2503.14499 ; https://arxiv.org/html/2503.14499 | An earlier arXiv version may have carried 212; it was not checked. METR's Time Horizon 1.1 post gives 196 days all-time and 89 days since 2024. Safest: cite the current data file's 201.15 days as the report recommends |
| Opus 4.6 original 14.5-hour announcement | Secondary only | SECONDARY-ONLY | Not found on METR's time-horizons page, the TH 1.1 post or the March 2026 note. Current file value 718.8 minutes (about 12.0 hours), CI 316.7 to 3,633.8 | https://metr.org/assets/benchmark_results_1_1.yaml ; https://metr.org/time-horizons/ | METR's update log confirms: regularization correction 3 March 2026; Mythos Preview and the 16-hour notice added 8 May 2026; "no longer actively updated" 8 September 2026 |
| AI Futures forecast medians | Conflicting Kokotajlo medians for August 2026 | CONFIRMED-PRIMARY for April and November. UNVERIFIABLE for August | 2 Apr 2026: Kokotajlo's Automated Coder median moved from late 2029 to mid 2028, and Lifland's from early 2032 to mid 2030. 10 Nov 2026: all authors forecast a Superhuman AI Researcher as likely to arrive during 2027 | https://blog.aifutures.org/p/q1-2026-timelines-update ; https://blog.aifutures.org/p/q35-timelines-update-looks-like-the | No August post was read. The report's handling (quote only the 10 November statement) stands. The forecast is worded as likely, and is conditional on no substantial deliberate slowdown |
| JetBrains survey figures | About 90% of professional developers use coding agents weekly; Claude Code about 39% vs 18% in January | UNVERIFIABLE | The JetBrains key-findings post was read. It has 28,945 respondents, fielded May to July 2026, and says more than half of employed developers use AI agents in over 60% of their work tasks. It contains neither claimed figure | https://blog.jetbrains.com/research/2026/11/state-of-developer-ecosystem-2026/ | The claimed figures may be in the full report or in a separate JetBrains study. Do not attribute them to this post |
| GitClear figures | Duplicated code blocks up 81% (2023 to 2026); refactoring moves down 70% | CONFIRMED-PRIMARY, with a baseline correction | Code block duplication +81% (the page indexes risk signals to 2023 = 100). Refactoring line moves down 70% "vs 2022 levels" | https://www.gitclear.com/the_ai_code_quality_maintainability_gap | The two figures use different base years. GitClear is a vendor. Also on the page: within-commit copy/paste +41%, two-week churn +15% |
| New Relic, McKinsey, CMU figures | Search summaries only | UNVERIFIABLE | Not attempted in this pass | | Leave off slides |
| NY Fed major-level unemployment | CS 7.0%, computer engineering 7.8%, 2024 data | UNVERIFIABLE | The NY Fed page loads, but the by-major table is rendered by a script and its data file could not be retrieved. The page carries a notice dated 31 October 2025 saying the feature has not been updated on schedule because source data were suspended | https://www.newyorkfed.org/research/college-labor-market | The notice supports the report's caution that these are stale. Label the data year or omit |
| State of AI Report 2026; International AI Safety Report 2026 | Not read | UNVERIFIABLE | Not attempted in this pass | | Do not quote |
| H200 export pause | 18 Nov 2026, single source | SECONDARY-ONLY | GSMArena article dated 18 November 2026 says Nvidia is abandoning H200 exports to China. Other coverage traces to a Financial Times report that Nvidia stopped H200 production for China, with unclear dating | https://m.gsmarena.com/nvidia_halts_its_h200_chip_sales_to_china_-amp-75528.php | No Nvidia or US Commerce statement found. Reports describe a production halt by Nvidia, not a new government "export pause" |
| Fable 5 and Mythos 5 June suspension | Restoration date primary; cause and duration press-reported | CORRECTED (now primary) | Anthropic's statement: the US government applied export controls to Fable 5 and Mythos 5 on Friday 12 June 2026; Anthropic suspended access for all users because it could not verify nationality in real time; the controls were lifted on 30 June and access was restored on 1 July 2026 | https://www.anthropic.com/news/redeploying-fable-5 ; https://platform.claude.com/docs/en/release-notes/overview | Cause and duration (12 June to 1 July) no longer need "reported". The Amazon-researcher detail in the report was not checked |
| Epoch SWE-bench Verified runs | Not in report | CONFIRMED-PRIMARY | Epoch's own harness: Opus 4.7 83.5%, GPT-5.5 (pre-release) 80.6%, Gemini 3.5 Flash 79.3%, Opus 4.6 78.7% | https://epoch.ai/data/benchmark_data.zip (swe_bench_verified.csv) | An independent series exists for the "not researched" gap named at the end of the report. Vendor 87.6% vs Epoch 83.5% for Opus 4.7 |

## What could not be verified

- DeepSeek's own changelog (connection refused), so the V4 announcement day rests on repository creation dates and Epoch.
- The OpenAI GPT-5.6 preview announcement of 26 June and the GPT-6 Astra launch table (Internet Archive rate-limited further requests).
- The Google Gemini 4 Argon limited preview of 30 September.
- Vendor SWE-bench Pro figures for Claude Opus 4.5, Sonnet 4.5 and Haiku 4.5.
- Saturation dates for MMLU and HumanEval, and the ARC-AGI-2 "60% human average".
- JetBrains adoption figures, NY Fed by-major figures, the New Relic, McKinsey and CMU figures, both annual reports, and the H200 item beyond one trade-press article.
- Earlier drafts of the Harvard paper (718 firms, +49% time-to-merge) and the May vintage of ECI.
- CRA figures were read through a summarising tool, so quote them as whole percentages exactly as shown above and re-open the page by hand before a slide cites them.
