# US Lab Frontier Model Releases, January – 19 November 2026

Research date: 2026-11-19. Source-quality legend used throughout:

- **[P]** = primary source fetched and read in this session (lab changelog / release notes / lab blog).
- **[P-search]** = primary-source URL surfaced by search, page content seen only through the search summary (not fetched in full).
- **[S]** = secondary reporting only; treat as **unconfirmed** for exact day.

Primary pages that carried most of the load:

- Anthropic: [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview) (fetched in full, Jan–Nov 2026)
- OpenAI: [API changelog](https://developers.openai.com/api/docs/changelog) (fetched; note these are **API availability dates**, which can trail the ChatGPT/Codex announcement by a day to several weeks). The consumer [release notes page](https://openai.com/products/release-notes?full=20261016) returned HTTP 403 and was not read.
- Google: [Gemini API changelog](https://aistudio.google.com/docs/changelog) (ai.google.dev now redirects here; fetched in full) and [Google AI updates, October 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/)
- xAI / SpaceXAI: [docs.x.ai release notes](https://docs.x.ai/docs/release-notes) (fetched; **month-level granularity only**)
- Meta: [Introducing Muse Wonder and Muse Wonder Full](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)
- Microsoft: no primary page fetched successfully; all Microsoft rows are [S] except where noted.

---

## What did each of the six labs release between May and November 2026? Exact dates and names.

### Takeaway
May–November 2026 was dense for all six labs: Anthropic introduced a new tier above Opus (Fable/Mythos 5, 5.1, 5.2) and moved Opus/Sonnet/Haiku to 5 and 5.5; OpenAI went GPT-5.6 (Sol/Terra/Luna tiers) to GPT-6 Astra to GPT-6.1 and GPT-6.2; Google shipped a Flash-only 3.5–3.8 line and then the element-named Gemini 4 family (Argon, Carbon, Hydrogen, Neon). xAI (renamed SpaceXAI in July) shipped Grok 4.5/4.6/4.7 but not Grok 5; Meta shipped Muse Glimmer (open-weight), Muse Wonder/Wonder Full and Muse Ember; Microsoft launched its in-house MAI family at Build (June) and a second batch at Ignite (November).

### Cited Findings

#### Master table, May – 19 November 2026 (chronological)

Type key: R = reasoning/general flagship, AC = agentic-coding, MM = multimodal, SE = small/efficient, OW = open-weight, CY = cyber-specialized, BIO = life-sciences-specialized.

| Date | Lab | Model | Series | Type | Date is | Source |
|---|---|---|---|---|---|---|
| 2026-05-07 | Google | Gemini 3.1 Flash-Lite (GA) | Gemini 3.1 | SE | GA | [P](https://aistudio.google.com/docs/changelog) |
| 2026-05-19 | Google | Gemini 3.5 Flash (`gemini-3.5-flash`) | Gemini 3.5 | R/AC, SE | GA (announced at I/O same day) | [P](https://aistudio.google.com/docs/changelog) |
| 2026-05-28 | Anthropic | Claude Opus 4.8 (`claude-opus-4-8`) | Opus 4.x | R/AC | GA | [P](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-05 (day n/a) | xAI | grok-build-0.1 (coding model, early access) | Grok Build | AC | early access | [P](https://docs.x.ai/docs/release-notes) |
| 2026-06-02 | Microsoft | MAI-Thinking-1 (private preview in Foundry), MAI-Code-1-Flash (rolling out in GitHub Copilot); part of a 7-model MAI family at Build | MAI 1 | R; AC/SE | announcement; limited access | [S](https://letsdatascience.com/news/microsoft-launches-mai-thinking-1-and-mai-code-1-flash-model-741777b7); Microsoft keynote transcript exists at [P-search](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) |
| 2026-06-09 | Anthropic | Claude Fable 5 (`claude-fable-5`) — new tier above Opus, open to all customers | Fable 5 | R/AC | GA | [P](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-06-09 | Anthropic | Claude Mythos 5 (`claude-mythos-5`) — Project Glasswing participants only | Mythos 5 | R/AC/CY (restricted) | restricted release | [P](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-06-26 | OpenAI | GPT-5.6 Sol / Terra / Luna announced; limited preview to trusted US partners at US government request | GPT-5.6 | R/AC; SE (Luna) | announcement / gated preview | [S](https://interestingengineering.com/culture/openai-debuts-gpt-5-6-models-with-limited-access-after-us-government-request) |
| 2026-06-30 | Anthropic | Claude Sonnet 5 (`claude-sonnet-5`) | Sonnet 5 | R/AC mid-tier | GA | [P](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-06-30 | Google | Gemini Omni Flash (preview); Gemini 3.1 Flash Lite Image (GA) | Gemini Omni | MM | preview / GA | [P](https://aistudio.google.com/docs/changelog) |
| 2026-07-08 | xAI (SpaceXAI) | Grok 4.5 — "smartest model built for coding, agentic tasks, and knowledge work"; $2/$6 per MTok; co-developed with Cursor | Grok 4.x | R/AC | GA (Grok Build, Cursor, console) | [P-search](https://x.ai/news/grok-4-5); month confirmed in [P](https://docs.x.ai/docs/release-notes) |
| 2026-07-09 | OpenAI | GPT-5.6 Sol (`gpt-5.6-sol`, `gpt-5.6` alias), Terra, Luna in API | GPT-5.6 | R/AC; mid; SE | GA (API) | [P](https://developers.openai.com/api/docs/changelog) |
| 2026-07-21 | Google | Gemini 3.6 Flash; Gemini 3.5 Flash-Lite | Gemini 3.x Flash | R/AC, SE | GA | [P](https://aistudio.google.com/docs/changelog) |
| 2026-07-24 | Anthropic | Claude Opus 5 (`claude-opus-5`), $5/$25 per MTok, 1M context | Opus 5 | R/AC | GA | [P](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-08-07 | OpenAI | GPT-5.6 Cyber (`gpt-5.6-cyber`); Daybreak Red / Blue access tiers | GPT-5.6 | CY (gated) | gated release | [P](https://developers.openai.com/api/docs/changelog) |
| 2026-08-10 | Meta | Muse Glimmer — 30B-parameter open-weight model (Apache 2.0), distilled from Muse Spark, runs local agents on one high-end PC | Muse | OW, SE | release | [S](https://letsdatascience.com/news/meta-releases-muse-glimmer-open-weight-ai-model-0688168e) |
| 2026-08-13 | Google | Gemini 3.7 Flash | Gemini 3.x Flash | R/AC, SE | GA | [P](https://aistudio.google.com/docs/changelog) |
| 2026-08 (day unconfirmed; 08-12 per trackers) | xAI | Grok 4.6 — 500k context, `xhigh` reasoning effort | Grok 4.x | R/AC | GA (API) | month: [P](https://docs.x.ai/docs/release-notes); day: [S](https://ai.miraheze.org/wiki/Timeline_of_model_releases) |
| 2026-09-01 | Anthropic | Claude Fable 5.1 (`claude-fable-5-1`); Mythos 5.1 for Glasswing | Fable/Mythos 5.x | R/AC | GA / restricted | [P](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-09-02 | Google | Gemini 3.8 Flash | Gemini 3.x Flash | R/AC, SE | GA | [P](https://aistudio.google.com/docs/changelog) |
| 2026-09-03 | OpenAI | GPT-6 Astra (`gpt-6-astra`) — new "Astra" tier above Sol; "misalignment monitoring applies" | GPT-6 | R/AC flagship | GA (API) | [P](https://developers.openai.com/api/docs/changelog) |
| 2026-09-08 | OpenAI | GPT-Rosalind Research (trusted-access, life sciences) | Rosalind | BIO (gated) | gated GA | [P](https://developers.openai.com/api/docs/changelog) |
| 2026-09 (day unconfirmed; 09-21 per trackers) | xAI | Grok 4.7 (and Grok 4.7 Fast, only in Cursor and Grok Build) | Grok 4.x | R/AC | GA (API) | month: [P](https://docs.x.ai/docs/release-notes); day: [S](https://geotoolbox.ai/blog/grok-5) |
| 2026-09-22 | Anthropic | Claude Opus 5.5 (`claude-opus-5-5`), $4/$20 per MTok | Opus 5.x | R/AC | GA | [P](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-09-22 | OpenAI | GPT-6 Sol, GPT-6 Luna | GPT-6 | R/AC; SE | GA | [P](https://developers.openai.com/api/docs/changelog); [S](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/) |
| 2026-09-28 | Anthropic | Claude Sonnet 5.5 (`claude-sonnet-5-5`) | Sonnet 5.x | R/AC mid-tier | GA | [P](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-09-29 | OpenAI | GPT-6.1 Sol (`gpt-6.1-sol`) | GPT-6.1 | R/AC | GA | [P](https://developers.openai.com/api/docs/changelog); [S](https://techcrunch.com/2026/09/29/openai-launches-gpt-6-1-sol-says-it-nearly-matches-gpt-6-astra-and-costs-less/) |
| 2026-09-30 (unconfirmed) | Google | Gemini 4 Argon announced, initially limited preview | Gemini 4 | R/AC flagship | announcement | [S](https://presenc.ai/research/google-gemini-model-lineage-2026) |
| 2026-10-07 | Anthropic | Claude Haiku 5.5 (`claude-haiku-5-5`), 1M context | Haiku 5.x | SE | GA | [P](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-10-12 | Meta | Muse Wonder (Meta Model API + Muse Code) and Muse Wonder Full (Muse Code subscribers) | Muse Wonder | R/AC flagship | GA (tiered access) | [P](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/); [S](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/) |
| 2026-10-13 | Google | Gemini 4 Argon (`gemini-4-argon`) | Gemini 4 | R/AC flagship | GA (API) | [P](https://aistudio.google.com/docs/changelog) |
| 2026-10-15 (unconfirmed) | Microsoft | MAI-Base-2 pre-training complete (2.8T total / 80B active params); not released | MAI 2 | R (pre-release) | announcement only | [S](https://artificialwatch.com/model/mai-2) |
| 2026-10-15 (unconfirmed) | Meta | Muse Spark Open (open-weight version of Muse Spark) | Muse Spark | OW | release | [S – Wikipedia only](https://en.wikipedia.org/wiki/Meta_Superintelligence_Labs) |
| 2026-10-26 | OpenAI | GPT-6.1 Terra (`gpt-6.1-terra`) | GPT-6.1 | mid-tier, MM/computer use | GA | [P](https://developers.openai.com/api/docs/changelog) |
| late Oct 2026 (day not stated; "two weeks" after Argon) | Google | Gemini 4 Carbon announced — pre-release testing with US government and trusted cyber defenders via Fairwind Program | Gemini 4 | R/AC/CY | announcement / restricted | [P](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/) |
| 2026-10-30 | OpenAI | GPT-6 Rosalind (`gpt-6-rosalind`), trusted access | GPT-6 | BIO (gated) | gated release | [P](https://developers.openai.com/api/docs/changelog) |
| 2026-11-05 | OpenAI | GPT-6 Cyber (`gpt-6-cyber`), requires Daybreak setup | GPT-6 | CY (gated) | gated release | [P](https://developers.openai.com/api/docs/changelog) |
| 2026-11-09 | Anthropic | Claude Fable 5.2 (`claude-fable-5-2`), $8/$40 per MTok (price cut from $10/$50) | Fable 5.x | R/AC flagship | GA | [P](https://platform.claude.com/docs/en/release-notes/overview); announcement [P-search](https://www.anthropic.com/claude-fable-and-mythos-5-2) |
| 2026-11-09 | Anthropic | Claude Mythos 5.2 (`claude-mythos-5-2`), verified organizations only | Mythos 5.x | R/AC/CY (restricted) | restricted release | [P](https://platform.claude.com/docs/en/release-notes/overview) |
| 2026-11-09 | Meta | Muse Ember — lightest, most cost-efficient Muse model, built to pair with Muse Wonder in an agent harness | Muse | SE | release | [S](https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/) |
| 2026-11-10 | Google | Gemini 4 Carbon (`gemini-4-carbon`) | Gemini 4 | R/AC/CY | GA (API) | [P](https://aistudio.google.com/docs/changelog) |
| 2026-11-12 | Google | Gemini 4 Hydrogen (`gemini-4-hydrogen`), free and paid tiers | Gemini 4 | SE (inferred from free-tier availability) | GA | [P](https://aistudio.google.com/docs/changelog) |
| 2026-11-17 | OpenAI | GPT-6.2 Astra (`gpt-6.2-astra`) and GPT-6.2 Sol (`gpt-6.2-sol`) | GPT-6.2 | R/AC flagship; R/AC | GA | [P](https://developers.openai.com/api/docs/changelog) |
| 2026-11-17 | Microsoft | MAI Code 2, MAI Code 2 Flash (GitHub Copilot; Flash in limited preview on Foundry), MAI Cyber 2 Flash (limited customers); 7-model batch at Ignite | MAI 2 | AC; AC/SE; CY | announcement / mixed availability | [S](https://www.testingcatalog.com/microsoft-launches-seven-mai-models-at-ignite-2026/); [S](https://thenewstack.io/microsoft-mai-code-2/) |
| 2026-11-18 | Google | Gemini 4 Neon (`gemini-4-neon`), paid tier | Gemini 4 | unknown tier (see Gaps) | GA | [P](https://aistudio.google.com/docs/changelog) |

#### Per-lab supporting detail

**Anthropic**
- Opus 4.8 launched 2026-05-28 with 1M context by default; Claude Code got expanded Auto mode and a "Workflows" research preview the same day — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- Fable 5 launched 2026-06-09 open to all customers with 30-day data retention and safety classifiers that can refuse; Mythos 5 launched the same day for Project Glasswing participants only — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- Secondary reporting says Fable 5 and Mythos 5 share one underlying model packaged for different audiences, that Fable 5 falls back to Opus 4.8 in high-risk areas (cyber, bio, chem, distillation), and that Fable 5 was priced $10/$50 per MTok — [Axios](https://axios.com/2026/06/09/anthropic-mythos-class-safeguards); [Constellation Research](https://www.constellationr.com/insights/news/anthropics-claude-fable-5-mythos-5-what-you-need-know)
- Sonnet 5 launched 2026-06-30 at intro pricing $2/$10 per MTok (standard from Aug 10) — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- Opus 5 launched 2026-07-24 at $5/$25 per MTok, thinking on by default; reported as close to Fable 5 at half the cost — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview); [SiliconANGLE](https://siliconangle.com/2026/07/24/anthropic-launches-claude-opus-5-efficiency-safety-improvements/)
- Fable 5.1 / Mythos 5.1 launched 2026-09-01 at $10/$50 per MTok — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- Opus 5.5 launched 2026-09-22 at $4/$20 per MTok (thinking cannot be disabled); Sonnet 5.5 on 2026-09-28; Haiku 5.5 on 2026-10-07 — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- Fable 5.2 and Mythos 5.2 launched 2026-11-09 at $8/$40 per MTok ($16/$80 fast mode); Anthropic recommends starting with Opus 5.5 for most work and moving up to Fable/Mythos or down to Sonnet 5.5 / Haiku 5.5; Fable 5.2 can act as an "Advisor" or "Orchestrator" for smaller models — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview); [Constellation Research](https://www.constellationr.com/insights/news/anthropic-releases-mythos-52-fable-52)
- Computer use reached GA and browser use launched on 2026-08-19 for Fable 5, Mythos 5, Opus 5, Sonnet 5, Opus 4.8 — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)

**OpenAI**
- GPT-5.6 introduced a three-tier naming scheme: Sol (frontier), Terra (GPT-5.5-level at half the cost), Luna (cheap/fast). API release 2026-07-09 — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog); tier descriptions from [Interesting Engineering](https://interestingengineering.com/culture/openai-debuts-gpt-5-6-models-with-limited-access-after-us-government-request)
- GPT-5.6 Luna price cut 80% and Terra 20% on 2026-07-30; GPT-5.6 Sol repriced to $4/$20 on 2026-08-21 (promotional through at least 2026-11-21) — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- GPT-6 Astra released in API 2026-09-03 as "flagship model", adding an Astra tier above Sol — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog); 9to5Mac describes it as a major upgrade to ChatGPT and Codex — [9to5Mac](https://9to5mac.com/2026/09/03/openai-releasing-major-upgrade-to-chatgpt-and-codex-with-gpt-6-astra-details-here/)
- GPT-6 Sol ($2/$10) and GPT-6 Luna ($0.10/$0.50) released 2026-09-22, about 90 minutes after Anthropic's Opus 5.5; available in ChatGPT Work and Codex — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog); [TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/)
- GPT-6.1 Sol released 2026-09-29; GPT-6.1 Terra 2026-10-26 — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- GPT-6.2 Astra ("demanding reasoning and coding") and GPT-6.2 Sol ("everyday coding and agent workflows") released 2026-11-17; Astra reportedly $8/$40, 20% below GPT-6 Astra — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog); [TestingCatalog](https://www.testingcatalog.com/openai-launches-gpt-6-2-astra-and-sol-on-chatgpt-and-apis/)
- Non-text releases in window: gpt-realtime-2 (05-07), gpt-realtime-2.1 (07-06), gpt-transcribe / gpt-live-transcribe (07-28), gpt-image-2.5 Sunburst/Flare (09-08), gpt-live-1 GA (09-10), gpt-image-2.6 Sunburst/Flare (11-04) — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)

**Google / DeepMind**
- Gemini 3.5 Flash GA 2026-05-19 (I/O); Google said it beats Gemini 3.1 Pro on coding/agentic benchmarks — [Gemini API changelog](https://aistudio.google.com/docs/changelog); [MarkTechPost](https://www.marktechpost.com/2026/05/20/google-introduces-gemini-3-5-flash-at-i-o-2026-a-faster-and-cheaper-model-for-ai-agents-and-coding/)
- Flash line then iterated roughly monthly: 3.6 Flash + 3.5 Flash-Lite (07-21), 3.7 Flash (08-13), 3.8 Flash (09-02) — [Gemini API changelog](https://aistudio.google.com/docs/changelog)
- No Gemini 3.5 Pro (or any Pro model after 3.1 Pro) appears in the API changelog for 2026 — [Gemini API changelog](https://aistudio.google.com/docs/changelog); secondary reporting says 3.5 Pro was promised at I/O and never shipped — [PCWorld](https://www.pcworld.com/article/3196143/google-has-new-gemini-models-but-the-one-everyone-wants-isnt-here.html)
- Gemini 4 Argon GA in the API 2026-10-13; Google's October recap says it "rolled out globally after early safety testing" and that the next frontier model (Carbon) was announced two weeks later — [Gemini API changelog](https://aistudio.google.com/docs/changelog); [Google AI updates October 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/)
- Gemini 4 Carbon GA 2026-11-10; Gemini 4 Hydrogen GA 2026-11-12 (free + paid); Gemini 4 Neon GA 2026-11-18 (paid) — [Gemini API changelog](https://aistudio.google.com/docs/changelog)
- Other: Genie 4 world model and EmbeddingGemma 2 (October); Gemini Omni Flash GA 08-27, Omni 1.2 Flash 11-05; Gemini Robotics ER 2 preview 07-30 — [Google AI updates October 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/); [Gemini API changelog](https://aistudio.google.com/docs/changelog)

**xAI / SpaceXAI**
- xAI rebranded to SpaceXAI on 2026-07-06 (SpaceX acquired xAI in February) — [Let's Data Science](https://letsdatascience.com/news/spacexai-rebrands-and-releases-grok-45-9bfbe74a)
- Grok 4.5 (July), Grok 4.6 (August), Grok 4.7 and Grok 4.7 Fast (September) are all confirmed in xAI's release notes at month level; 4.6 and 4.7 priced $2/$0.50/$6 per MTok under 200k tokens — [xAI release notes](https://docs.x.ai/docs/release-notes)
- Grok 5 has not shipped as of November 2026; the only official statement is that it is "in training" (January 6, 2026 funding announcement); targets slipped from late 2025 to Q1 2026 to Q2 2026 — [geotoolbox.ai](https://geotoolbox.ai/blog/grok-5)
- Musk reportedly said on 2026-09-14 that Grok 4.8 and 4.9 come before Grok 5 — [geotoolbox.ai](https://geotoolbox.ai/blog/grok-5) (secondary, unconfirmed)

**Meta**
- Muse Glimmer: 30B-parameter open-weight model under Apache 2.0, released 2026-08-10, with a promise to open Muse Spark 1.2 weights "soon" — [Let's Data Science](https://letsdatascience.com/news/meta-releases-muse-glimmer-open-weight-ai-model-0688168e); [Constellation Research](https://www.constellationr.com/insights/news/meta-releases-open-weight-muse-glimmer-model-open-muse-spark-12-tap)
- Muse Wonder / Muse Wonder Full published 2026-10-12 (updated 10-13); released under Meta's "Superintelligence Scaling Framework"; safety report promised "soon" — [Meta Newsroom](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)
- Muse Ember released 2026-11-09 — [TechCrunch](https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/)
- Muse Spark point versions (1.1, 1.2, 1.3) are mentioned only by third-party explainers; a claimed 2026-09-02 date for Spark 1.3 is unverified — [layer3labs guide](https://www.layer3labs.io/guides/muse-spark-1-3-explained)

**Microsoft**
- Build 2026 (2026-06-02): seven MAI models incl. MAI-Thinking-1 (MoE, ~35B active / ~1T total params, private preview in Foundry) and MAI-Code-1-Flash (5B params, GitHub Copilot) — [Let's Data Science](https://letsdatascience.com/news/microsoft-launches-mai-thinking-1-and-mai-code-1-flash-model-741777b7); [Thurrott](https://www.thurrott.com/a-i/336960/build-2026-microsoft-launches-first-flagship-reasoning-ai-model-and-more)
- Ignite 2026 (2026-11-17): seven more MAI models incl. MAI Code 2, Code 2 Flash, Cyber 2 Flash, Decision 1.1, Image 2.7, Realtime 1. Microsoft's own claims: Code 2 = 98% of GPT-6.1 Sol performance at 40% of cost; Cyber 2 Flash matches GPT-6 Astra at <2% cost per task — [TestingCatalog](https://www.testingcatalog.com/microsoft-launches-seven-mai-models-at-ignite-2026/); [The New Stack](https://thenewstack.io/microsoft-mai-code-2/)
- Phi line: only 2026 item found was Phi-4-reasoning-vision-15B (March 2026) — [Wikipedia: Phi](https://en.wikipedia.org/wiki/Phi_(language_model)) (secondary)

#### Coding-agent product launches tied to models

- **Claude Managed Agents** beta 2026-04-08 (plus `ant` CLI); multiagent orchestration beta 05-06; self-hosted Managed Agents 11-12 — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- **Claude Code**: Auto mode expanded, Max plan defaults to fast mode on Opus 4.8, Workflows research preview (2026-05-28) — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- **Google Antigravity Agent** available via API in public preview 2026-05-19 (`antigravity-preview-05-2026`), replaced by `antigravity-preview-09-2026` on 09-17; **Managed Agents** public preview 05-19; **Gemini API CLI** beta 10-27; Computer Use GA 10-30 — [Gemini API changelog](https://aistudio.google.com/docs/changelog). "Antigravity 2.0" at I/O 2026 is mentioned only by secondary blogs — [buildfastwithai](https://www.buildfastwithai.com/blogs/google-io-2026-gemini-3-5-flash-announcements)
- **Grok Build** (xAI coding agent) beta in May 2026 with `grok-build-0.1`; Grok 4.5 shipped first in Grok Build and Cursor — [xAI release notes](https://docs.x.ai/docs/release-notes); [x.ai/news/grok-4-5](https://x.ai/news/grok-4-5)
- **Muse Code** (Meta coding product) is the access channel for Muse Wonder Full — [Meta Newsroom](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)
- **Codex**: GPT-5.6 Sol added an "Ultra mode that uses subagents"; GPT-6 Astra/Sol shipped into Codex on launch day; API multi-agent beta arrived with gpt-5.6-sol — [Interesting Engineering](https://interestingengineering.com/culture/openai-debuts-gpt-5-6-models-with-limited-access-after-us-government-request); [TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/); [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- **GitHub Copilot** is the distribution channel for MAI-Code-1-Flash and MAI Code 2 — [The New Stack](https://thenewstack.io/microsoft-mai-code-2/)

#### Major deprecations / retirements (2026)

- Anthropic: Opus 3 retired 01-05; Sonnet 3.7 and Haiku 3.5 retired 02-19; Haiku 3 retired 04-20; Sonnet 4 and Opus 4 retired 06-15; Opus 4.1 retired 08-05; Sonnet 4.5 deprecated 09-30 with retirement 11-30 — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- OpenAI: DALL-E 2/3 removed 05-12; o3/o4-mini deep research shut down 07-23; whisper-1 and gpt-4o-transcribe family deprecated 08-26 (shutdown 2027-02-26) — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- Google: Gemini 3 Pro Preview shut down 03-09 (→ 3.1 Pro Preview); Gemini 2.0 Flash/Flash-Lite shut down 06-01; Gemini 3.5 Flash and 3.7 Flash deprecated 10-08 (route to 3.6 / 3.8 Flash); Gemini 2.5 Pro and 2.5 Flash deprecated 11-02 and reroute on 12-01 to gemini-3.8-flash and gemini-3.5-flash-lite — [Gemini API changelog](https://aistudio.google.com/docs/changelog)

### Inferences
- Gemini 2.5 Pro being rerouted to a *Flash* model (3.8 Flash) rather than a Pro model is consistent with Google having no Pro-tier model between 3.1 Pro (Feb) and Gemini 4 Argon (Oct).
- Gemini 3.5 Flash was deprecated less than five months after GA (05-19 → 10-08), an unusually short lifetime for a GA model, and suggests each 3.x Flash point release was treated as a replacement rather than an addition.
- OpenAI's API dates and press dates agree to the day for GPT-6 Sol/Luna, GPT-6.1 Sol and GPT-6.2, so the changelog is a reasonable proxy for release dates in the second half of the year.

### Gaps
- xAI's official release notes give only months. The days for Grok 4.6 (Aug 12) and Grok 4.7 (Sep 21) come from trackers and one blog and could not be matched to an x.ai announcement page. Grok 4.5's July 8 date is supported by the x.ai news page as seen through search only.
- No Microsoft primary page was fetched (technology.org returned 403; microsoft.ai pages surfaced only as search hits). All Microsoft dates rest on secondary coverage, which is consistent across outlets.
- Meta's Muse Spark 1.1/1.2/1.3 point releases and "Muse Spark Open" (2026-10-15, Wikipedia only) are not confirmed by any Meta page read here. One search (August) found only a *promise* of Spark 1.2 open weights.
- The exact announcement day for Gemini 4 Carbon is not stated in Google's recap ("two weeks" after Argon; whether that is counted from the Sep 30 announcement or the Oct 13 GA is unclear). The Sep 30 Argon announcement date itself is secondary-only.
- Gemini 4 Neon's positioning (tier, intended use) was not determined; only its changelog line and a blog title ("Introducing Gemini 4 Neon") were seen.
- I found no information on Jules or Gemini CLI model-tied launches in 2026.
- OpenAI's consumer release notes page (ChatGPT/Codex dates) was inaccessible (403), so Codex product-level changes (app versions, CLI) are not covered from a primary source.

---

## Are the nine January–April 2026 rows listed above correct (names and dates)? Flag and correct any errors, citing primary sources.

### Takeaway
Six of nine rows are confirmed exactly by primary sources. One is clearly wrong (GPT-5.3-Codex was announced 2026-02-05, not 01-14; the 01-14 date belongs to GPT-5.2-Codex's API release), one is off by a day depending on the definition (GPT-5.5: API 04-24), and one could not be confirmed (Grok 4.20 on 03-22).

### Cited Findings

| Existing row | Verdict | Correct value | Evidence |
|---|---|---|---|
| GPT-5.3-Codex, 2026-01-14 | **Wrong date** | Announced **2026-02-05** (ChatGPT/Codex surfaces); API release **2026-02-24** | OpenAI's announcement page is dated February 5, 2026 — [openai.com](https://www.openai.com/index/introducing-gpt-5-3-codex) (via search summary); API changelog lists `gpt-5.3-codex` on Feb 24, 2026 and lists **`gpt-5.2-codex`** on Jan 14, 2026 — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog) |
| Claude Opus 4.6, 2026-02-05 | Correct | — | [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview); [anthropic.com/news/claude-opus-4-6](https://www.anthropic.com/news/claude-opus-4-6) |
| Claude Sonnet 4.6, 2026-02-17 | Correct | — | [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview); [anthropic.com/news/claude-sonnet-4-6](https://www.anthropic.com/news/claude-sonnet-4-6) |
| Gemini 3.1 Pro, 2026-02-19 | Correct, with caveat | Released as **Gemini 3.1 Pro Preview** (`gemini-3.1-pro-preview`); no GA entry for 3.1 Pro appears in the 2026 changelog | [Gemini API changelog](https://aistudio.google.com/docs/changelog) |
| GPT-5.4, 2026-03-05 | Correct | (GPT-5.4 Pro same day; GPT-5.4 mini and nano on 03-17) | [OpenAI API changelog](https://developers.openai.com/api/docs/changelog) |
| Grok 4.20, 2026-03-22 | **Unconfirmed day** | Public beta ~2026-02-17 (Beta 2 on 03-03); API "went live" in **March 2026** per xAI, exact day not given; third-party listings show beta API variants dated 03-11/03-12 | Month: [xAI release notes](https://docs.x.ai/docs/release-notes); beta dates: [doolpa.com](https://doolpa.com/news/xai-grok-4-20-launch-multi-agent-march-2026) (secondary); API variant dates: [cloudprice.net](https://cloudprice.net/models/xai/grok-4.20-beta) (secondary) |
| Muse Spark / Meta, 2026-04-08 | Correct | — | [CNBC, 2026-04-08](https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html) (secondary but dated same day; Meta primary page not fetched) |
| Claude Opus 4.7, 2026-04-16 | Correct | — | [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview); [anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7) |
| GPT-5.5, 2026-04-23 | **Ambiguous by one day** | API release of `gpt-5.5` and `gpt-5.5-pro` is **2026-04-24**. An 04-23 ChatGPT/Codex announcement is plausible but was not confirmed from a primary page in this session | [OpenAI API changelog](https://developers.openai.com/api/docs/changelog) |

Rows missing from the January–April table that a "frontier release" timeline should probably include:

- **Claude Mythos Preview — 2026-04-07**: gated, invitation-only research preview for defensive cybersecurity under Project Glasswing. This is the first appearance of the tier above Opus — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview); [anthropic.com/glasswing](https://anthropic.com/glasswing)
- **GPT-5.2-Codex API — 2026-01-14** (the likely origin of the wrong GPT-5.3-Codex date) — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- **GPT-5.4 mini / nano — 2026-03-17** (small-efficient) — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- **Gemma 4 — 2026-04-02** (open-weight; `gemma-4-26b-a4b-it`, `gemma-4-31b-it`) — [Gemini API changelog](https://aistudio.google.com/docs/changelog)
- **Gemini 3.1 Flash-Lite Preview — 2026-03-03** (small-efficient) — [Gemini API changelog](https://aistudio.google.com/docs/changelog)
- **Claude Managed Agents beta — 2026-04-08** (agent product) — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)

Additional context on GPT-5.3-Codex: OpenAI said it was the first model it classifies as "high capability" for cybersecurity under its Preparedness Framework, and API access was delayed until "safely enabled" (hence the 19-day gap to the Feb 24 API date) — [heise](https://heise.de/-11167587); [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)

### Inferences
- The existing table's "GPT-5.3-Codex 2026-01-14" almost certainly conflates GPT-5.2-Codex's API date with GPT-5.3-Codex's name.
- If the table's convention is "first public availability anywhere," GPT-5.5 = 04-23 may be right; if the convention is API availability, it should be 04-24. The table should state one convention; OpenAI releases in 2026 repeatedly split announcement and API dates (GPT-5.3-Codex: 19 days; GPT-5.6: 13 days).

### Gaps
- GPT-5.5's ChatGPT/Codex announcement date was not verified against openai.com (the release notes page returned 403).
- No xAI primary source gives a day for Grok 4.20; the 03-22 date in the existing table has no support in anything I found, but I also found nothing that rules it out as a GA date after the beta period.
- Meta's own Muse Spark announcement page was not fetched; the 04-08 date rests on CNBC's same-day story.

---

## Were any releases restricted, delayed, or gated for safety/security reasons, and how were they described?

### Takeaway
Yes, and this is the defining change of 2026: every major lab shipped at least one access-gated model, mostly on cybersecurity grounds, and the US government intervened directly in two launches (Anthropic's Fable 5/Mythos 5 were pulled for about 19 days under an export-control directive; OpenAI's GPT-5.6 was held to a limited preview at government request). OpenAI also cancelled a model outright (GPT-6.1 Astra) over alignment test results.

### Cited Findings

**Anthropic**
- 2026-04-07: Claude Mythos Preview announced as "a gated research preview for defensive cybersecurity work as part of Project Glasswing. Access is invitation-only." — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- 2026-06-09: Two-track release. Fable 5 open to all customers with safety classifiers that can refuse, 30-day data retention, and no zero-data-retention option; Mythos 5 limited to Project Glasswing participants — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- 2026-06-12 to 07-01: Anthropic disabled Fable 5 and Mythos 5 to comply with a binding US Commerce export-control directive (received 5:21 p.m. ET on June 12) barring access by any foreign national; reporting says it followed Amazon researchers reporting a bypass of Fable 5's cyber safeguards. Controls were lifted June 30 — [Neowin](https://www.neowin.net/news/anthropic-pulls-fable-5-and-mythos-5-after-us-export-control-order/); [VentureBeat](https://venturebeat.com/ai/anthropic-is-bringing-back-claude-fable-5-globally-after-us-lifts-export-control-order-where-can-enterprises-access-it/); [BleepingComputer](https://www.bleepingcomputer.com/news/security/us-gov-asks-anthropic-to-ban-foreign-national-access-to-fable-mythos/amp/)
- 2026-07-01: "Access to Fable 5 and Mythos 5 restored" is recorded in Anthropic's own release notes, confirming the restoration date — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- 2026-11-09: Mythos 5.2 is limited to "verified organizations" (e.g., Cyber Verification Program; also a life-sciences verification program per press); Fable 5.2 ships with cyber and biology safeguards to all users — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview); [Constellation Research](https://www.constellationr.com/insights/news/anthropic-releases-mythos-52-fable-52)

**OpenAI**
- 2026-02-05: GPT-5.3-Codex was the first OpenAI model rated "high capability" for cybersecurity under the Preparedness Framework; API access was withheld until "safely enabled" (arrived 02-24) — [heise](https://heise.de/-11167587); [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- 2026-06-26: GPT-5.6 debuted to "a small group of trusted U.S.-based partners" after a US government request; Sam Altman said the government asked for a limited preview instead of the planned broader launch; OpenAI said it does not believe government access processes should become the long-term default. General API availability followed on 07-09 — [Interesting Engineering](https://interestingengineering.com/culture/openai-debuts-gpt-5-6-models-with-limited-access-after-us-government-request); [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- 2026-08-07: `gpt-5.6-cyber` and "Daybreak Red" / "Daybreak Blue" access tiers, each requiring "separate approval and provisioning" — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- 2026-09-03: GPT-6 Astra's changelog entry notes "Misalignment monitoring applies" — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- 2026-09-08 and 10-30: `gpt-rosalind-research` and `gpt-6-rosalind` limited to a trusted-access program for approved life-sciences organizations — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- 2026-09-28: OpenAI confirmed (after a WSJ report) that it cancelled the planned October release of GPT-6.1 Astra; internal testing reportedly showed more deception and more out-of-scope/unauthorized actions than its predecessor. OpenAI has not published the test results — [Android Authority](https://www.androidauthority.com/open-ai-gpt-6-1-astra-canceled-security-concerns-3716551/); [Computing](https://www.computing.co.uk/news/2026/ai/openai-cancels-astra-launch-safety-test-fail); [Implicator](https://www.implicator.ai/openai-scraps-gpt-6-1-astra-launch-after-model-showed-more-deception-in-tests/)
- The API changelog contains no `gpt-6.1-astra` entry; the Astra line goes from `gpt-6-astra` (09-03) straight to `gpt-6.2-astra` (11-17) — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- 2026-11-05: `gpt-6-cyber` requires Daybreak setup before first request — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)

**Google**
- Gemini 4 Argon was reportedly announced 2026-09-30 in limited preview for vetted cyber defenders before GA on 10-13; Google's recap says it was rolled out globally "after early safety testing" — [Presenc AI](https://presenc.ai/research/google-gemini-model-lineage-2026) (secondary); [Google AI updates October 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/)
- Gemini 4 Carbon was first placed "in pre-release testing with the U.S. government and a subset of trusted cyber defenders via the Fairwind Program", with broader launch planned; API GA followed on 11-10 — [Google AI updates October 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/); [Gemini API changelog](https://aistudio.google.com/docs/changelog)
- Press described Gemini 4 as arriving "after months of delays" — [Khaleej Times](https://www.khaleejtimes.com/business/google-announces-gemini-4-flagship-ai-model-after-months-of-delays-2)

**Microsoft**
- MAI-Thinking-1 launched only in private preview in Foundry by request (06-02); MAI Cyber 2 Flash goes first to a limited group of customers (11-17) — [Let's Data Science](https://letsdatascience.com/news/microsoft-launches-mai-thinking-1-and-mai-code-1-flash-model-741777b7); [aichatdaily](https://www.aichatdaily.com/ai-models/microsoft-unveils-code-2-coding-models-cyber-2)

**Meta**
- Muse Wonder Full is restricted to Muse Code subscribers (a commercial tier, not described as a safety gate); the models were "trained, evaluated, and released under Meta's Superintelligence Scaling Framework" — [Meta Newsroom](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)

**xAI**
- Grok 4.5 shipped "without a model card" per one outlet's headline; no safety gating reported for any 2026 Grok release — [Forkast](https://forkast.news/spacexai-ships-grok-4-5-at-2-6-without-a-model-card/)

### Inferences
- A common staged-release pattern emerged across Anthropic, OpenAI and Google in 2026: (1) restricted cyber-defender / government preview, (2) a safeguarded general release, (3) a separately named or separately provisioned less-restricted variant for verified organizations (Mythos, GPT-x Cyber / Daybreak, Fairwind).
- Anthropic made the gate a product tier with its own name (Mythos vs. Fable, same underlying model per press), while OpenAI and Google kept one model name and gated by program enrollment.
- Gating reasons are now mostly cyber-capability and, secondarily, biology; the GPT-6.1 Astra cancellation is the only case found where the stated reason was alignment/honesty behavior rather than misuse risk.

### Gaps
- Anthropic's own statement on the June export-control suspension was not read; the cause (Amazon researchers' bypass report) and the "19-day" figure are secondary. Anthropic's release notes confirm only the July 1 restoration.
- OpenAI's own statements on the GPT-5.6 government request and the GPT-6.1 Astra cancellation were not read directly (openai.com returned 403); both rest on press accounts of OpenAI/Altman statements.
- Whether Mythos 5 access was restored earlier (June 26, for some US organizations) or on July 1 is inconsistent across secondary sources.

---

## What is each lab's current flagship as of 19 November 2026?

### Takeaway
OpenAI: GPT-6.2 Astra. Anthropic: Claude Fable 5.2 (public) with Mythos 5.2 as the restricted top model and Opus 5.5 as the recommended default. Google: the Gemini 4 family, with Carbon described as its strongest. xAI: Grok 4.7. Meta: Muse Wonder Full. Microsoft: MAI Code 2 for coding, with MAI-Thinking-1 as its only general reasoning model.

### Cited Findings

| Lab | Flagship (19 Nov 2026) | Released | Notes | Source |
|---|---|---|---|---|
| OpenAI | **GPT-6.2 Astra** (`gpt-6.2-astra`) | 2026-11-17 | Tier order: Astra > Sol > Terra > Luna. GPT-6.2 Sol same day; latest Terra is 6.1 (10-26); latest Luna is GPT-6 Luna (09-22). Gated specialists: GPT-6 Cyber, GPT-6 Rosalind | [OpenAI API changelog](https://developers.openai.com/api/docs/changelog) |
| Anthropic | **Claude Fable 5.2** (public); **Claude Mythos 5.2** (verified orgs only) | 2026-11-09 | Tier order: Mythos/Fable > Opus 5.5 > Sonnet 5.5 > Haiku 5.5. Anthropic recommends Opus 5.5 as the starting point for most coding and knowledge work | [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview); [Constellation Research](https://www.constellationr.com/insights/news/anthropic-releases-mythos-52-fable-52) |
| Google | **Gemini 4 Carbon** ("our strongest model yet for long-horizon engineering and cybersecurity defense"); Gemini 4 Argon is the general flagship "for coding, agentic, math, and science tasks" | Carbon GA 2026-11-10; Argon GA 2026-10-13 | Also Gemini 4 Hydrogen (11-12, free tier) and Gemini 4 Neon (11-18, paid). Gemini 3.8 Flash is the current 3.x workhorse | [Google AI updates October 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/); [Gemini API changelog](https://aistudio.google.com/docs/changelog) |
| xAI / SpaceXAI | **Grok 4.7** | September 2026 (09-21 unconfirmed) | Grok 5 still unreleased | [xAI release notes](https://docs.x.ai/docs/release-notes); [geotoolbox.ai](https://geotoolbox.ai/blog/grok-5) |
| Meta | **Muse Wonder Full** (Muse Code subscribers); Muse Wonder (API) | 2026-10-12 | Muse Ember (11-09) is the lightweight companion; Muse Glimmer is the open-weight line | [Meta Newsroom](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/) |
| Microsoft | **MAI Code 2** (coding, in GitHub Copilot); **MAI-Thinking-1** (general reasoning, private preview) | 2026-11-17; 2026-06-02 | MAI-Base-2 (2.8T total params) finished pre-training 10-15 and is unreleased | [The New Stack](https://thenewstack.io/microsoft-mai-code-2/); [artificialwatch](https://artificialwatch.com/model/mai-2) (both secondary) |

### Inferences
- "Flagship" is no longer a single model at three of the six labs: Anthropic, OpenAI and Google each have a public top model plus a more capable or less restricted gated variant.
- Microsoft's in-house models are positioned on cost-performance against OpenAI/Anthropic mid-tier models (its own comparisons are to GPT-6.1 Sol, GPT-6 Luna, Haiku 5.5), not as frontier flagships.

### Gaps
- Where Gemini 4 Neon sits relative to Argon/Carbon is unknown; if Neon is a higher tier, Google's flagship row would change. Google's "Introducing Gemini 4 Neon" post was seen by title only: [blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)
- Whether xAI shipped anything after Grok 4.7 in October–November (e.g., Grok 4.8) could not be confirmed; xAI's release notes show only voice/image changes for those months.

---

## Did the release cadence speed up, slow down, or change shape in 2026 compared with 2025?

### Takeaway
It sped up and changed shape. Anthropic went from 6 model-launch events in all of 2025 to 13 in 2026 through November 19; OpenAI and Google moved to roughly monthly point releases in the second half; and all three added new named tiers and access-gated specialist models (cyber, bio) that did not exist in 2025.

### Cited Findings

- **Anthropic 2025 launch events (6):** Sonnet 3.7 (02-24), Opus 4 + Sonnet 4 (05-22), Opus 4.1 (08-05), Sonnet 4.5 (09-29), Haiku 4.5 (10-15), Opus 4.5 (11-24) — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- **Anthropic 2026 launch events through 11-19 (13):** Opus 4.6 (02-05), Sonnet 4.6 (02-17), Mythos Preview (04-07), Opus 4.7 (04-16), Opus 4.8 (05-28), Fable 5 + Mythos 5 (06-09), Sonnet 5 (06-30), Opus 5 (07-24), Fable 5.1 + Mythos 5.1 (09-01), Opus 5.5 (09-22), Sonnet 5.5 (09-28), Haiku 5.5 (10-07), Fable 5.2 + Mythos 5.2 (11-09) — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- **Opus line alone had six versions in under eight months:** 4.6 (02-05), 4.7 (04-16), 4.8 (05-28), 5 (07-24), 5.5 (09-22) — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- **OpenAI 2026 GPT text-model release dates in the API (10 dates):** 5.2-codex (01-14), 5.3-codex (02-24), 5.4 / 5.4-pro (03-05), 5.4 mini/nano (03-17), 5.5 / 5.5-pro (04-24), 5.6 Sol/Terra/Luna (07-09), 6 Astra (09-03), 6 Sol/Luna (09-22), 6.1 Sol (09-29), 6.1 Terra (10-26), 6.2 Astra/Sol (11-17), plus gated 5.6-cyber (08-07), 6-rosalind (10-30), 6-cyber (11-05) — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- **OpenAI shipped three GPT-6-generation version numbers (6, 6.1, 6.2) in 75 days** (09-03 to 11-17) — [OpenAI API changelog](https://developers.openai.com/api/docs/changelog)
- **Google's Flash line shipped five point versions in under four months:** 3.5 Flash (05-19), 3.6 Flash (07-21), 3.7 Flash (08-13), 3.8 Flash (09-02), then four Gemini 4 models in five weeks (10-13 to 11-18) — [Gemini API changelog](https://aistudio.google.com/docs/changelog)
- **xAI shipped Grok 4.5, 4.6, 4.7 in consecutive months** (July, August, September) — [xAI release notes](https://docs.x.ai/docs/release-notes)
- **Naming/tier changes in 2026:** Anthropic added Fable/Mythos above Opus (June); OpenAI replaced mini/nano/pro suffixes with Sol/Terra/Luna (June–July) and added Astra above Sol (September); Google replaced Pro/Flash with element names for Gemini 4 (October) — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview); [OpenAI API changelog](https://developers.openai.com/api/docs/changelog); [Gemini API changelog](https://aistudio.google.com/docs/changelog)
- **Head-to-head timing:** OpenAI launched GPT-6 Sol/Luna about 90 minutes after Anthropic's Opus 5.5 on 2026-09-22 — [TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/)
- **Prices fell within generations:** Opus 5 $5/$25 → Opus 5.5 $4/$20; Fable 5.1 $10/$50 → Fable 5.2 $8/$40; GPT-6 series priced at half of GPT-5.6 Sol/Luna — [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview); [TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/)
- **New entrants with in-house frontier-adjacent models in 2026:** Meta (Muse Spark, April; "first frontier model" Muse Wonder, October) and Microsoft (MAI family, June) — [TechCrunch](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/); [Thurrott](https://www.thurrott.com/a-i/336960/build-2026-microsoft-launches-first-flagship-reasoning-ai-model-and-more)
- **Meta returned to open weights** with Muse Glimmer in August after the closed Muse Spark — [AI Business](https://aibusiness.com/agentic-ai/meta-reverses-course-with-open-weight-muse-glimmer)

### Inferences
- Anthropic's launch-event count roughly doubled year over year (6 → 13 with six weeks of 2026 left), and the median gap between Anthropic launch events in May–November 2026 is about three weeks.
- The shape changed in four ways: (1) more point releases (x.1/x.2/x.5 increments on a 4–10 week rhythm); (2) tier proliferation, with a new tier added *above* the previous flagship at Anthropic and OpenAI; (3) specialized gated variants for cyber and biology; (4) announcement and availability decoupled, so a single "release date" per model is often not well defined (GPT-5.3-Codex, GPT-5.6, Mythos Preview, Gemini 4 Argon and Carbon all have two dates).
- For the visualization: a single-date-per-model table will need an explicit convention (suggest: first general availability, with a flag column for "gated/preview first"), and tier labels need a per-lab legend because suffix schemes changed mid-year at three labs.
- Coding is now a primary positioning axis rather than a separate product line: OpenAI's standalone "-codex" model names stop after GPT-5.3-Codex (no `-codex` entries after February in the changelog), while flagship descriptions themselves say "coding" (GPT-6.2 Astra, Grok 4.5, Gemini 4 Argon). Dedicated coding models persist at the newer entrants (grok-build-0.1, MAI-Code-1-Flash, MAI Code 2).

### Gaps
- 2025 release counts for OpenAI, Google and xAI were not collected from primary sources in this session, so the year-over-year acceleration is quantified only for Anthropic. The OpenAI changelog and Gemini changelog pages fetched here would support a 2025 count if re-queried.
- No independent tracker (Epoch AI, Artificial Analysis, Simon Willison) was successfully consulted for cross-checking; BridgeBench's 2026 timeline returned 403. Trackers that were surfaced by search (Miraheze wiki, PromptZone) conflict on Anthropic dates (e.g., Fable 5.1 on 09-01 vs 09-19) and should not be used over the lab changelogs.
