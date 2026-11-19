# Real-World Evidence on Agentic Coding: Adoption, Productivity, Labor Market, Predictions, Practice, Education (Jan 2025 – 19 Nov 2026)

Research date: 19 November 2026. Conventions used throughout:

- **[M]** = measured data (telemetry, payroll, survey statistics, filings). **[C]** = executive or company claim, not independently audited. **[F]** = forecast or prediction.
- **(primary)** = I opened the primary page or document this session. **(secondary)** = figure seen only in search-result summaries or third-party write-ups; verify before putting on a slide.
- Items marked **(background, not re-verified)** are pre-2026 facts from prior knowledge whose URLs I did not re-open this session.

---

## 1. Adoption: share of AI-written code, survey usage and trust, tool usage and revenue

### Takeaway
By autumn 2026 AI authorship of code is the norm at the frontier firms (Google about 75% of new code, Anthropic more than 80% of merged code) and on GitHub at large (agents started more than 40% of pull requests in September 2026, up from 17% in March). Usage is near-universal in surveys (JetBrains: about 90% of professional developers use agents weekly), while trust stays conditional, and the revenue curves of coding tools (Anthropic $33.2B in nine months, Cursor sold for $60B) are steeper than any benchmark curve.

### Cited Findings

#### 1a. Share of code written by AI at named companies (chart-ready series)

| Date | Company | Figure | Metric definition | Type | Source |
|---|---|---|---|---|---|
| Oct 2024 | Google | "more than a quarter" of new code | AI-generated, reviewed and accepted by engineers | [C] | [TechRadar](https://www.techradar.com/pro/alphabet-ceo-says-more-than-a-quarter-of-new-code-at-google-is-ai-generated) (secondary) |
| Apr 2025 | Microsoft | "maybe 20%, 30%" of code in repos | Nadella estimate, some projects | [C] | [Yahoo Tech](https://tech.yahoo.com/articles/microsoft-says-30-code-now-114621008.html) (secondary) |
| Fall 2025 | Google | 50% of new code | same as Google definition | [C] | [Pichai, Google blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/) (secondary via search) |
| Jan 2026 | Anthropic | "between 70% and 90%" (spokesperson); "pretty much 100%" (Boris Cherny, own work) | varies by speaker | [C] | [ProvenBrief tracker](https://provenbrief.com/story/the-ai-code-share-tracker-every-verified-public-number-on-ai-written-code-from-n) (secondary) |
| 24 Apr 2026 | Google | 75% of new code (some outlets: "nearly 75%") | AI-generated and approved by engineers | [C] | [Semafor](https://www.semafor.com/article/04/24/2026/google-ceo-says-75-of-companys-new-code-is-ai-generated); [Google blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/) |
| May 2026 | Anthropic | "more than 80%" of code merged to production codebase authored by Claude, up from low single digits before Feb 2025 | merged production code; leadership cites 90%+ when scripts are included | [C] | [The Next Web](https://thenextweb.com/news/anthropic-claude-recursive-self-improvement-code) (secondary) |
| Mid-2026 target | Meta | internal goal: 65% of engineers with more than 75% of code AI-assisted | internal target, reported, not confirmed by Meta leadership | [C]/[F] | [HCA Mag](https://www.hcamag.com/us/specialization/transformation/meta-to-cut-10-of-its-workforce-as-zuckerberg-redirects-billions-toward-ai/572933) (secondary) |

- Google has not disclosed how much AI-generated code is rejected or rewritten before shipping, and the companies measure different things (new lines vs merged code vs repo share), so the figures are not comparable on one axis — [DevOps.com](https://devops.com/google-ceo-says-75-of-new-code-is-ai-generated); [ProvenBrief](https://provenbrief.com/story/the-ai-code-share-tracker-every-verified-public-number-on-ai-written-code-from-n)
- Anthropic reportedly said its engineers ship about 8x more code than a year earlier and itself described the 8x productivity reading as "almost certainly overstated" — [Crypto Briefing](https://cryptobriefing.com/anthropic-engineers-8x-code-claude/) (secondary)
- No 2026 Microsoft update to the April 2025 "20–30%" figure and no Q3 2026 Alphabet earnings update to the 75% figure were found — see Gaps.

#### 1b. GitHub Octoverse 2026 [M] (primary; published 28 Oct 2026, updated 6 Nov 2026; data 1 Oct 2025 – 30 Sep 2026)

- Share of pull requests started by a detectable agent: 17% in March 2026, more than 40% in September 2026; about 110 million agent-started PRs in September, roughly 6x March — [GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
- Agent-PR merge within two weeks: 83% in February 2026, 90% in September 2026, against about 86% for PRs with no detected agent — [GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
- Agent PRs touch multiple files 87% of the time vs 79% for others — [GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
- Platform totals for the 12 months: 17.9 billion pushes (more than 2024 and 2025 combined), 34.3 billion commits (more than 3x two years earlier), 1.3 billion merged PRs (about 3.5 million per day), 45.4 billion Actions jobs, more than 225 million developers (US 38.3M, India 32.0M) — [GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
- 55% of Copilot monthly active users use agentic features, up from 35% a year earlier; Copilot cloud agent usage up 230% YoY; 61% of model-choosing users used more than one model in September — [GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
- Merged PRs with detected AI involvement by language: about 40–44% for TypeScript, Python, Rust; 21–34% for Java, C#, C++ — [GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
- AI-assisted code review and GitHub Advanced Security usage each grew more than 90% YoY; stacked PRs (preview 30 Jul 2026) used by more than 264,000 developers by September — [GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
- Counting caveat: detected agent use is a floor, and the metric counts PRs, not lines — [Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/10/29/github-octoverse-agents-started-more-than-40-percent-of-september-pull-requests.aspx)
- CNBC (11 Oct 2026) quoted an earlier GitHub figure that one in three PRs involve an agent, up from fewer than one in ten a year earlier, with GitHub's projection that "within the next two years, most of the code pushed to GitHub could be written by an agent" [F] — [CNBC](https://www.cnbc.com/2026/10/11/ai-software-developer-jobs.html)

#### 1c. Stack Overflow Developer Survey 2026 [M] (primary blog post, 6 Oct 2026; more than 30,000 respondents; full dataset promised later)

- 73% of those who use AI coding assistants or agents use them daily; of daily users, about a third spend 4+ hours a day with them — [Stack Overflow Blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)
- Tool categories used: coding assistants or agents 66%, general chat tools 63%; agents named: Claude Code 66%, GitHub Copilot 59% — [Stack Overflow Blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)
- Favorability: 62% of all respondents view AI at least somewhat positively, 71% among daily users — [Stack Overflow Blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)
- Uses: generating code in familiar areas 67%, debugging 61%, deploying or operating production systems 20% — [Stack Overflow Blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)
- Trust: 93% say source attribution is needed to trust AI output (press coverage reports 78.7% calling attribution "important", a differently worded item); only 6.6% would trust AI for important decisions; 17.2% do not use AI tools; 26.2% use automated agent workflows — [Stack Overflow Blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/); [DevOps Digest](https://devopsdigest.com/developers-positive-about-ai-trust-remains-conditional) (secondary)
- Model providers: Anthropic 75% and OpenAI 74% current usage; 49.0% want to work with Anthropic models next year vs 32% OpenAI — [IT Brief](https://itbrief.co.uk/story/stack-overflow-survey-shows-developers-trust-ai-with-caveats) (secondary)
- Cost governance: 38% of organizations limit usage, 28% reviewed spend data, 27% route different work to different models, 25% limit who gets AI — [Stack Overflow Blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)
- "Organization of one" respondents rose from 4% to 10%; 64% visit Stack Overflow less for simple questions — [Stack Overflow Blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)
- 2025 baseline for contrast: 84% using or planning to use AI, 29–33% trust in accuracy, 46% active distrust — [The Decoder](https://the-decoder.com/developers-rely-on-ai-tools-more-than-ever-but-trust-is-slipping/) (secondary; sources disagree between 29% and 33%)

#### 1d. JetBrains State of Developer Ecosystem 2026 [M] (secondary; JetBrains blog returned HTTP 403; fieldwork May–July 2026, more than 15,000 respondents)

- About 90% of professional developers use AI coding agents at work at least weekly; 68% daily — [Gulf News](https://gulfnews.com/technology/90-of-developers-surveyed-now-use-ai-coding-agents-at-work-jetbrains-says-1.500700542); [GIGAZINE](https://gigazine.net/gsc_news/en/20260824-ai-coding-agent-adoption-trends/)
- Claude Code adoption about 39% globally (47% US), up from 18% in January 2026; GitHub Copilot down to about 21% from 29–31%; Codex up to about 16% — [GIGAZINE](https://gigazine.net/gsc_news/en/20260824-ai-coding-agent-adoption-trends/); [DEV Community](https://dev.to/jamilxt/claude-code-overtakes-github-copilot-what-jetbrains-survey-of-15000-developers-says-about-ai-3nhc)
- More than half of employed developers use agents in over 60% of their work tasks; 60% of developers with 1–2 years' experience say AI solutions are better than their own vs 47% of those with 16+ years — [JetBrains blog](https://blog.jetbrains.com/research/2026/11/state-of-developer-ecosystem-2026/) (via search summary)

#### 1e. Other adoption surveys and telemetry

- DORA 2025 (about 5,000 respondents): 90% of technology professionals use AI at work, more than 80% believe it raised their productivity — [InfoQ](https://www.infoq.com/news/2026/03/ai-dora-report/) (secondary)
- Faros telemetry (22,000 developers, 4,000 teams): 60% of developers use at least one AI tool weekly; 25% of PRs are reviewed by an AI agent — [Faros AI](https://www.faros.ai/research/ai-acceleration-whiplash) (primary)
- Harvard/Jellyfish panel: by March 2026 nearly 80% of firms had used an AI review tool; AI produced 23.3% of review comments — [ComplexDiscovery summary of Chen and Stratton](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/)
- McKinsey "State of AI in 2026" (Aug 2026): 32% of organizations report deciding against buying a software product or feature because it could be built internally with agentic coding tools — [McKinsey](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/the-state-of-ai-in-2026-on-the-road-to-roi.pdf) (via search summary)

#### 1f. Tool usage and revenue trajectories (chart-ready; mostly [C] or press-reported)

| Product | Date | Data point | Source |
|---|---|---|---|
| Claude Code | Nov 2025 | $1B annualized run-rate | [gradually.ai](https://www.gradually.ai/en/claude-code-statistics/) (secondary) |
| Claude Code | 12 Feb 2026 | run-rate above $2.5B (Anthropic Series G announcement); no newer product-level figure found | [gradually.ai](https://www.gradually.ai/en/claude-code-statistics/) (secondary) |
| Anthropic (company) | end 2025 | about $9B run-rate | [VentureBeat](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth) |
| Anthropic | spring 2026 | $30B run-rate | [VentureBeat](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth) |
| Anthropic | early May 2026 | more than $47B run-rate | [getpanto](https://www.getpanto.ai/blog/claude-ai-statistics) (secondary) |
| Anthropic | late Jul 2026 | about $65B run-rate (Bloomberg, anonymous sources) | [getpanto](https://www.getpanto.ai/blog/anthropic-ai-statistics) (secondary) |
| Anthropic | 26 Oct 2026 | S-1 filed (Nasdaq "ANT"): H1 2026 revenue $16.3B, Q2 $11.6B; net loss $80.7B of which $72.4B is a non-cash convertible-note charge | [Fortune](https://fortune.com/2026/10/26/anthropics-s-1/) |
| Anthropic | 2–3 Nov 2026 | amended S-1: $33.2B revenue for nine months to 30 Sep 2026 (Q3 about $17B) | [gHacks](https://www.ghacks.net/2026/11/03/anthropics-revised-ipo-filing-reports-33-2-billion-in-nine-month-revenue-and-895-billion-in-compute-commitments/) (secondary) |
| Cursor (Anysphere) | Nov 2025 | $1B ARR (company-disclosed) | [Wikipedia](https://en.wikipedia.org/wiki/Cursor_(company)) |
| Cursor | Feb 2026 / Apr 2026 / early Jun 2026 | $2B / $3B (Bloomberg) / more than $4B (Forbes) | [NewsBytes](https://www.newsbytesapp.com/news/business/ai-coding-tool-cursor-hits-2b-annual-run-rate/tldr); [Second Talent](https://www.secondtalent.com/resources/cursor-statistics/) (secondary) |
| Cursor | 16 Jun 2026 | SpaceX agrees to acquire for $60B in stock | [CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html) |
| Cursor | 14 Aug 2026 | deal effective; 8-K GAAP consideration $42.5B | [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/spacex-closes-60bn-acquisition-ai-085713131.html); [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001181412/000162828026066482/spaceexplorationtechnologi.htm) |
| Cursor | 29 Aug 2026 | OpenAI to end model access via Cursor on 12 Nov 2026; OpenAI models about 5% of Cursor traffic | [CNBC](https://www.cnbc.com/2026/08/29/openai-cursor-spacex-model-access.html) |
| OpenAI Codex | Jan 2026 | about 600,000 weekly users | [Tech Insider](https://tech-insider.org/ie/openai-codex-5-million-users-2026/) (secondary) |
| OpenAI Codex | Mar 2026 | 1.6–2M weekly users | [gradually.ai](https://www.gradually.ai/en/codex-statistics/) (secondary) |
| OpenAI Codex | 2 Jun 2026 | more than 5M weekly active users, about 20% non-developers (vendor-reported) | [Constellation Research](https://www.constellationr.com/insights/news/openai-touts-broadening-codex-usage-5-million-weekly-active-users) |
| OpenAI Codex | Jul 2026 | 7–8M weekly users (aggregator-reported) | [gradually.ai](https://www.gradually.ai/en/codex-statistics/) (secondary, low confidence) |
| GitHub Copilot | Jan 2026 | 4.7M paid subscribers, up 75% YoY | [aibusiness.vc](https://aibusiness.vc/b2b/github-copilot-2b-arr) (secondary) |
| GitHub Copilot | Apr 2026 | nearly 140,000 organizations | [Second Talent](https://www.secondtalent.com/resources/github-copilot-statistics/) (secondary) |
| GitHub Copilot | Jul 2026 | 50M users (all-time/total users, Nadella on FY26 Q4 call) | [whizi](https://whizi.io/resources/copilot-statistics/) (secondary) |
| Cognition (Devin + Windsurf) | May 2026 | $492M run-rate at Series D ($26B valuation) | [valueaddvc](https://valueaddvc.com/blog/how-does-cognition-make-money-devin-pricing-windsurf-enterprise-and-the-492m-arr-breakdown) (secondary) |
| Cognition | 2 Jun 2026 | Windsurf rebranded into Devin | [Wikipedia](https://en.wikipedia.org/wiki/Cognition_AI) |
| Cognition | Sep 2026 | about $900M run-rate, $47–48B valuation | [clinkbill](https://clinkbill.com/arr-leaderboard/cognition) (secondary, low confidence) |

### Inferences
- The "90% of code" threshold has been reached or approached inside the labs that build the tools (Anthropic, Google at 75%) but the only broad-population measure, GitHub's agent-started PR share, sits near 40% and counts PRs rather than lines. A lecture chart should plot these as separate series with their definitions.
- Trust did not rise with usage: daily use is the norm, yet almost no respondents would rely on AI for important decisions and attribution is demanded by nearly all. Adoption is being driven by speed and employer mandate, with verification cost moved onto the developer.
- Market leadership changed inside 2026: Claude Code overtook Copilot in JetBrains and Stack Overflow data, and Cursor ceased to be independent. Any tool-share slide dated before mid-2026 is stale.
- Revenue is the cleanest "revealed preference" adoption series: Anthropic's audited nine-month revenue ($33.2B) is roughly 3.7x its entire end-2025 run-rate.

### Gaps
- JetBrains primary page was blocked (403); all JetBrains numbers are from press coverage and should be checked against the report.
- No 2026 Microsoft or Meta executive figure for AI-written code share was found; Meta's numbers are reported internal targets.
- No Codex-specific or Copilot-specific revenue figure and no post-February Claude Code run-rate were found. Gemini CLI, Antigravity, Replit and Lovable usage numbers were not retrieved.
- Stack Overflow 2026 headline "trust in accuracy" percentage comparable to 2025's 29–33% was not in the launch post; the full dataset was still pending.
- Stanford AI Index 2026 and any "State of AI Report 2026" (Air Street) were seen only through third-party digests; the Air Street report itself was not located.

---

## 2. Productivity: controlled trials, field studies, telemetry, code quality

### Takeaway
Measured gains at the level of the individual and of code volume are real and growing (Microsoft: about 24% more merged PRs; Harvard/Jellyfish: about 30% more lines, 23% more PRs), but the gain shrinks or vanishes by the time it reaches finished work (Jira issues resolved: statistically zero, with an upper bound near +12%), because review time rose about 49% and quality signals worsened. METR's 2025 "19% slower" result has not been replaced by a clean number: its 2026 follow-up leaned toward speedup but was declared unreliable because developers would no longer agree to work without AI.

### Cited Findings

#### 2a. Randomized and quasi-experimental evidence (chart-ready)

| Study | Period of data | Sample | Result | Type | Source |
|---|---|---|---|---|---|
| Google internal RCT | summer 2024 | 96 Google engineers, lab task | about 21% less time, wide CI | [M] | [metaroles summary](https://metaroles.ai/posts/coding-agents-developer-productivity) (secondary; original paper not opened) |
| METR RCT #1 | Feb–Jun 2025 | 16 experienced OSS developers, 246 tasks in own repos | 19% slower with AI (95% CI +2% to +39% longer); developers believed they were about 20% faster | [M] | [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) (background); restated in [METR Feb 2026](https://metr.org/blog/2026-02-24-uplift-update/) (primary) |
| METR follow-up, returning developers | Aug 2025 onward | 10 developers | time change −18% (CI −38% to +9%), i.e. point estimate is a speedup, CI includes slowdown | [M] | [METR, 24 Feb 2026](https://metr.org/blog/2026-02-24-uplift-update/) (primary) |
| METR follow-up, new developers | Aug 2025 onward | 47 developers; total 57 devs, 143 repos, 800+ tasks | time change −4% (CI −15% to +9%) | [M] | [METR, 24 Feb 2026](https://metr.org/blog/2026-02-24-uplift-update/) (primary) |
| METR self-report survey | Feb–Apr 2026 | 349 technical workers | median self-reported value uplift 1.4x–2x; median speed uplift 3x; 1.3x recalled for Mar 2025, 2x for Mar 2026, 2.5x forecast for Mar 2027 | [M] self-report | [METR, 11 May 2026](https://metr.org/blog/2026-05-11-ai-usage-survey/) (primary) |
| Microsoft CLI-agent rollout (Murphy-Hill, Butler, Savelieva) | early 2026, four-month window | tens of thousands of Microsoft engineers | adopters merged about 24% more PRs than counterfactual; lift persisted over four months; spread mainly through social networks | [M] | [arXiv 2607.01418](https://arxiv.org/abs/2607.01418) (primary abstract) |
| Chen and Stratton (Harvard), "Artificial Intelligence in the Firm: Bottlenecks in Software Production" | Jan 2021 – Mar 2026 | 718 firms, 725,938 workers (Jellyfish + Revelio) | lines added +30% (+1,494 on 5,017), commits +20%, PRs +23%; Jira issues resolved +0.12 on 3.67 (SE 0.17, not distinguishable from zero; CI excludes more than about +12%); PR time-to-merge +3.45 days on 7.03 (+49%); formal change requests about doubled from 13%; review comments per PR +35% | [M] | [ComplexDiscovery](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/); paper: [fion.ac/jellyfish.pdf](https://fion.ac/jellyfish.pdf) |
| Linux Foundation OSS survey | 2026 | not stated in release | self-reported time reductions: 52% for code authoring, 19% for proposal discussions; 21% take longer on high-complexity tasks with GenAI | [M] self-report | [Linux Foundation, 20 Oct 2026](https://www.linuxfoundation.org/press/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop) (primary) |

- METR's own verdict on the follow-up: the data give "an unreliable signal"; 30–50% of developers said they declined to submit some tasks because they did not want to do them without AI; pay fell from $150/hour to $50/hour, adding selection; time measurement breaks down when developers run several agents concurrently. METR nevertheless states it believes developers are more sped up in early 2026 than in early 2025 — [METR](https://metr.org/blog/2026-02-24-uplift-update/)
- METR lists replacement designs under consideration (shorter intensive experiments, observational OSS data, fixed-task experiments, developer-level randomization) without committing to one; a commentator reports no newer METR RCT result as of mid-October 2026 — [METR](https://metr.org/blog/2026-02-24-uplift-update/); [devs-group](https://devs-group.ch/en/blog/ai-productivity-studies-2026/) (secondary)
- METR's survey caveats: the 2025 RCT found developers overestimated AI's effect on their time by about 40 percentage points; in a review of seven respondents claiming 10x or more, some claims were overstated and two were not visible in public output; METR staff reported the lowest gains of any subgroup — [METR](https://metr.org/blog/2026-05-11-ai-usage-survey/)
- Chen and Stratton on headcount: an overall employment decline larger than 2.9% is ruled out at adopting firms; the engineering-only bound is a noisier 13.8%; authors call these short-run partial-equilibrium effects. The paper is a job-market paper, version dated 4 Aug 2026, not peer reviewed. A November 2026 version reportedly covers 655 firms and 720,542 engineers and finds resolved issues +13.7% (borderline significant) — [ComplexDiscovery](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/); [beri.net](https://www.beri.net/article/harvard-jellyfish-study-ai-coding-agents-code-review-bottleneck-output-employment-engineering-org-design) (secondary; versions differ)
- Stanford AI Index 2026 cites software-development productivity gains of about 26%, weaker on judgment-heavy tasks — [HAI](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report) (via search summary)

#### 2b. Telemetry: Faros "AI Acceleration Whiplash" 2026 [M, vendor] (primary page; 22,000 developers, 4,000 teams, two years of telemetry; high- vs low-AI-adoption teams)

| Metric | Change, high vs low AI adoption |
|---|---|
| Task throughput per developer | +33.7% |
| Epics completed | +66.2% |
| PR merge rate | +16.2% |
| PR size | +51% |
| Bugs per PR | +28.7% |
| Bugs per developer | +54% |
| Incidents per PR | +242.7% (about 3x) |
| Monthly incidents | +57.9% |
| Median PR review time | about 5x (+441.5% in one secondary write-up) |
| Code churn | +861% (about 10x) |
| Deployments per week | −11.7% |

- Source for the table — [Faros AI](https://www.faros.ai/research/ai-acceleration-whiplash)
- Faros's 2025 "AI Productivity Paradox" (10,000+ developers) had found 21% more tasks, 98% more merged PRs, and 91% longer review time; the 2025 and 2026 reports are separate datasets, not a panel — [mstone.ai](https://mstone.ai/blog/ai-code-review-bottleneck/) (secondary)

#### 2c. DORA

- DORA 2025 State of AI-assisted Software Development: higher AI adoption is associated with higher delivery throughput and higher delivery instability; "AI as amplifier"; seven-capability AI model — [InfoQ](https://www.infoq.com/news/2026/03/ai-dora-report/)
- DORA "ROI of AI-Assisted Software Development (2026.01)": introduces a J-curve (early dip then gains); its worked example ($11.6M annual value, $8.4M first-year investment, 39% ROI, about eight-month payback) is a modeled scenario, not measured data; prices a change-failure-rate rise from 5% to 6% at $344,000 downtime cost — [InfoQ, May 2026](https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/); [dora.dev](https://dora.dev/insights/) (secondary summaries)

#### 2d. Code quality: GitClear "Maintainability Gap" 2026 [M, vendor] (623 million code changes, 2023–2026)

- Duplicated code blocks per million changed lines: 40.3 in 2023 to 73.0 in 2026 YTD (+81%, record high) — [GitClear](https://www.gitclear.com/the_ai_code_quality_maintainability_gap) (via search summary)
- Within-commit copy/paste +41%; error-masking +47%; two-week churn +15%; refactoring ("moved" code) −70%; changes to code older than one year −74%; function connectivity −35% — [GitClear](https://www.gitclear.com/the_ai_code_quality_maintainability_gap); [tenten](https://developer.tenten.co/623-million-code-changes-show-ai-duplication-at-a-record-high-while-refactoring-moves-fell-70) (secondary)
- Counter-evidence: a longitudinal study of 151 open-source repositories (revised April 2026) reportedly found no general increase in churn; GitClear measures trends over the adoption period, not line-level AI attribution — [tsukumo](https://tsukumo.ch/blog/does-ai-hurt-code-quality) (secondary)
- New Relic 2026 State of AI Coding (200 US tech leaders): most rate AI code as higher quality at review, yet 78% report more incidents once shipped — [New Relic](https://newrelic.com/resources/report/2026-state-of-ai-coding) (via search summary)
- CMU difference-in-differences on agent adoption in OSS repos: static-analysis warnings up about 18% and cognitive complexity up about 39%; velocity gains large and front-loaded only where agents were the first AI tool — [arXiv 2601.13597](https://arxiv.org/pdf/2601.13597) (via search summary)

#### 2e. Agent pull requests in open source (academic)

- 220,612 closed PRs across 489 popular Python repositories: agent PRs merged about 65% vs about 85% for human PRs; per agent, Devin 43%, Codex 73%, Claude Code 84% — [arXiv 2607.21832](https://arxiv.org/html/2607.21832v1); figures via [Robert Stowe](https://robertstowe.com/agent-pull-requests-merge-at-65-humans-at-85/) (secondary)
- 33,596 AIDev PRs, five agents: human co-authored PRs merged 53.8% vs 79.8% for fully autonomous ones, a pattern that reverses within agents (Simpson's paradox) — [arXiv 2606.22711](https://arxiv.org/html/2606.22711v1)
- Repository popularity confounds acceptance: 73.67% merge rate in high-popularity repos vs 90.63% elsewhere (about 2 million agent PRs) — [IJRASET](https://www.ijraset.com/best-journal/ai-coding-agents-on-github-repository-popularity-as-a-hidden-confounder-in-the-acceptance-of-2-million-agentauthored-pull-requests)
- Concurrency cost: textual merge conflicts in 19.8% of same-agent PR pairs and 41.7% of cross-agent pairs — [arXiv 2607.04697](https://arxiv.org/html/2607.04697v2)
- 1.02 million PRs: agent-involved review patterns gave faster decisions without better review quality — [arXiv 2607.13196](https://arxiv.org/pdf/2607.13196)
- Octoverse contrast: across all of GitHub, agent PRs now merge within two weeks slightly more often (90%) than others (86%) — [GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)

### Inferences
- Why benchmarks and measured productivity diverge, as the evidence supports it: (1) benchmarks score self-contained task completion, while firms are bottlenecked on review, integration and deployment (Chen and Stratton, Faros); (2) output proxies (lines, PRs) inflate faster than delivered work (issues resolved, deployments per week); (3) quality costs arrive downstream as incidents, churn and duplication; (4) self-reports overstate gains (METR's 40-point perception gap, 3x self-reported speed vs 1.4–2x value).
- The slope over time appears positive: METR's point estimates moved from +19% time (early 2025) to −18%/−4% (late 2025), and the Harvard paper's later version edges toward a detectable gain in finished work. A fair lecture framing is "from negative or zero toward modestly positive, with wide error bars", not "no effect".
- The classic RCT design is failing for a reason that is itself evidence of adoption: experienced developers will not accept a no-AI arm.
- Agent merge rates in curated academic samples (about 65%) and platform-wide Octoverse data (90% within two weeks) differ because the first is weighted to popular OSS repos with outside contributors and the second is dominated by private and own-repo work.

### Gaps
- No Uplevel 2026 study was found; the 2024 Uplevel result (41% more bugs with Copilot, no throughput gain) is the latest I know of and was not re-verified.
- Google's 2024 RCT original paper and any 2026 Google internal productivity study were not opened. No NBER working paper with a randomized agent trial was found.
- The Microsoft arXiv paper's design details, adoption rates and any quality measures are in the full text, which I did not read.
- GitClear and JetBrains primary pages were not opened directly; DORA has not published a 2026 State-of-DevOps-style survey report that I could find (the 2026.01 item is an ROI model).

---

## 3. Labor market: developer employment, postings, new graduates, AI-attributed layoffs

### Takeaway
There is still no measured economy-wide displacement, and aggregate software-developer demand recovered through 2026 (Indeed software postings up from an index low of 61.1 in May 2025 to about 74–79 by August–October 2026), but the recovery is concentrated in senior and AI-titled roles. The entry-level signal strengthened: Stanford's August 2026 update finds employment of 22–25-year-olds in AI-exposed occupations 19% below where it would be had it tracked less-exposed peers (15% a year earlier), operating through reduced hiring. Employers attributed 121,401 announced US job cuts to AI in January–October 2026, but that attribution faded sharply by October and is contested.

### Cited Findings

#### 3a. Stanford Digital Economy Lab, "Canaries in the Coal Mine?" August 2026 update [M] (primary PDF; ADP payroll, 3.5–5 million workers per month, through June 2026)

- Six facts: (1) no evidence of economy-wide displacement; (2) employment of ages 22–25 in AI-exposed occupations is 19% below where it would be had it kept pace with less-exposed peers, with no comparable gap for experienced workers; (3) the divergence has widened steadily since August 2025; (4) it operates mainly through reduced hiring, not separations; (5) declines are concentrated where AI use substitutes for tasks, with flat or rising employment where it complements; (6) adjustment is through employment, not base pay — [Brynjolfsson, Chandar, Chen](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)
- In levels: employment of 22–25-year-olds in the two most-exposed quintiles fell about 11% between November 2022 and June 2026, while the same age group in the three least-exposed quintiles grew about 10% — [Stanford](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)
- Series for a chart: by the descriptive "kept-pace" measure, 15% at the July 2025 vintage and 19% at June 2026. Earlier headline regression estimates were 13% (July 2025 data) and 16% (September 2025 data); the authors changed the headline measure, so do not plot 13 → 19 as one series — [Stanford](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)
- Authors' own caveats: descriptive, not causal; effects attenuate when controlling for occupational education; some divergent trends predate ChatGPT; the divergence is more pronounced in ADP than in national survey benchmarks. Robust to excluding tech firms and computer occupations and to interest-rate and remote-work controls — [Stanford](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)
- The widely quoted "software developers aged 22–25 down nearly 20% from the late-2022 peak" comes from the August 2025 edition and is repeated by the Stanford AI Index 2026 — [CNBC](https://www.cnbc.com/2026/10/11/ai-software-developer-jobs.html); [HAI](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report)
- A public "AI Economic Indicators" tracker accompanies the paper — [Stanford Digital Economy Lab](https://digitaleconomy.stanford.edu/project/indicators/)

#### 3b. Indeed Hiring Lab software-development postings [M] (index, 1 Feb 2020 = 100)

| Date | Index / figure | Source |
|---|---|---|
| May 2025 | 61.1 (series low) | [Blue Line Search](https://bluelinesearch.ai/insights/software-dev-postings-26-below-prepandemic-indeed-august-2026) (secondary) |
| 8 Jul 2026 | about 72.5 (27.5% below baseline); up almost 15% since 24 Feb 2025 while all postings fell 7% | [Indeed Hiring Lab](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/) (primary) |
| 14 Aug 2026 | 74.4; all postings 101.8 | [Indeed Hiring Lab snapshot](https://hiringlab.indeed.com/2026/08/24/us-labor-market-snapshot-august-2026/) (via search summary) |
| 9 Oct 2026 | 78.1, about 21% higher YoY | [The Uptime Report](https://theuptimereport.com/tech-job-postings/) (secondary) |
| 16 Oct 2026 | 78.9 | [DEV Community](https://dev.to/stackchief/the-2026-software-engineer-job-market-in-6-numbers-51ec) (secondary) |

- Composition of the rebound (May 2025 – May 2026): senior roles account for 71% of the increase; postings with AI in the title account for 37% (categories overlap). Indeed calls this consistent with "seniority-biased technological change" and stresses correlation, not causation — [Indeed Hiring Lab](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/)
- Entry-level postings fell 7.5% YoY as of May 2026; entry-level roles were 4.5% of software-development postings in Q1 2026 — [Extern](https://www.extern.com/post/will-ai-replace-software-engineers-guide); [solvebar](https://solvebar.com/blog/entry-level-software-jobs-2026-junior-developers) (secondary, unverified against a primary)

#### 3c. BLS and Federal Reserve

- BLS Employment Projections 2025–35 (August 2026): software developers +10%, about 1.72M to 1.89M (+174,700); computer programmers −7%. The prior 2024–34 edition had software developers at +15.8% (+267,000) — [CNBC](https://www.cnbc.com/2026/10/11/ai-software-developer-jobs.html); [BLS TED](https://www.bls.gov/opub/ted/2026/artificial-intelligence-information-technology-and-employment-2024-34.htm)
- Steve Rattner's analysis of BLS data: software-developer employment grew May 2023 – May 2025 roughly in line with all occupations — [CNBC](https://www.cnbc.com/2026/10/11/ai-software-developer-jobs.html)
- Federal Reserve Board, Crane and Soto, "AI and Coder Employment: Compiling the Evidence" (FEDS 2026-018, March 2026): using O*NET linked to CPS, coder employment "decelerated sharply" after ChatGPT; the slowdown is not explained by exposure to slowing industries and looks like an occupation-specific shock; coder employment kept growing, much more slowly than before 2022 — [Federal Reserve](https://www.federalreserve.gov/econres/feds/ai-and-coder-employment-compiling-the-evidence.htm) (primary abstract)
- Press coverage of that paper claims growth roughly halved and about 500,000 developer jobs "never filled"; I could not confirm either number in the abstract — [Decrypt](https://decrypt.co/365693/fed-confirms-tech-developers-fears-ai-jobs) (secondary, unverified)
- St. Louis Fed FRED Blog (Aug 2026), "Is AI reducing employment for software coders?", summarizes the same deceleration — [FRED Blog](https://fredblog.stlouisfed.org/2026/08/is-ai-reducing-employment-for-software-coders/)
- Dallas Fed (Scott Davis, Jan 2026): 22–25-year-olds bear the AI-related employment effect; returns to experience are rising in AI-exposed occupations; "If AI were simply automating jobs, we would expect both wages and employment to decline" — [Fortune, 4 Mar 2026](https://fortune.com/2026/03/04/gen-z-lack-of-experience-job-wage-loss-older-worker-experience-dallas-fed/)
- Goldman Sachs note (22 Oct 2026): about 10,000 jobs below trend in AI-exposed industries over three months; "some signs of AI-related hiring headwinds" — [Tech Insider](https://tech-insider.org/ai-hiring-headwinds-goldman-sachs-briggs-10000-jobs-2026/) (secondary)
- Swedish register-data study (June 2026, 4.6 million job ads): little evidence AI cut total jobs; hiring slowed for the youngest workers — [ProMarket](https://www.promarket.org/2026/06/17/ai-is-not-reducing-employment-but-rather-who-gets-hired/)

#### 3d. New graduates: NY Fed, NACE, enrollment

- NY Fed outcomes by major (2024 ACS, released Feb 2026; recent graduates aged 22–27): computer engineering 7.8% unemployment (second highest of 73 majors; anthropology 7.9%), computer science 7.0%; underemployment low at 15.8% (CE) and 19.1% (CS) against about 42% for all recent graduates; early-career median pay about $87,000 (CS) and $90,000 (CE) — [VnExpress](https://e.vnexpress.net/news/tech/tech-news/us-s-computer-engineering-grads-post-second-highest-unemployment-rate-5048192.html); [opportunitydata.org](https://opportunitydata.org/recent-grad-job-market.html) (secondary; some sites still cite the older 6.1% / 7.5%)
- Recent graduates overall: about 5.6% unemployment in Q2 2026 vs about 4.2% for all workers — [research.com](https://research.com/news/the-new-york-fed-tracked-graduates-for-five-years-these-majors-left-the-most-people-unemployed) (secondary)
- NACE Winter 2026 Salary Survey [F, employer projections]: CS bachelor's average starting salary $81,535 (+6.9% from $76,251), highest of all majors; engineering $81,198; CS master's $94,212 (+10.9% from $84,960) — [NACE](https://naceweb.org/job-market/compensation/class-of-2026-salary-projections-are-promising); [NACE master's](https://naceweb.org/job-market/compensation/class-of-2026-computer-sciences-grads-expected-to-be-highest-paid-at-masters-level)
- NACE: Class of 2026 hiring described as flat overall with salaries climbing — [NACE press](https://naceweb.org/about-us/press/2026/salaries-expected-to-climb-for-class-of-2026-grads-despite-flat-hiring); Fortune coverage 26 Feb 2026 — [Fortune](https://fortune.com/2026/02/26/computer-science-class-of-2026-graduates-job-prospects-high-salaries-gen-z-career-advice-new-report/)
- CRA Taulbee 2025 (published May–June 2026): record CS bachelor's degree production; within the longitudinal sample, new bachelor's enrollment −12.9%, total undergraduate CS enrollment −4.1%, total CS master's enrollment about −26%, new master's −10.3%, new doctoral −15%; 63% of new CS master's students come from outside North America, so CRA ties the graduate decline to visa barriers — [CRA, June 2026](https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/); [CRA, May 2026](https://cra.org/crn/2026/05/cra-update-a-sneak-peek-at-computing-degree-enrollment-trends-from-the-2025-cra-taulbee-survey/); undergraduate percentages via [Startup Fortune](https://startupfortune.com/computer-science-enrollment-falls-for-the-first-time-in-20-years-as-ai-reshapes-who-gets-hired/) (secondary)
- National Student Clearinghouse preliminary fall 2026: computer and information science enrollment −12.4% at four-year colleges, −12.3% at two-year colleges, −10.4% in graduate programs; AI's causal role not established — [StrongMocha](https://strongmocha.com/general/could-worries-about-ai-jobs-be-shaping-computer-science-enrollment/) (secondary)
- CRA CERP pulse survey: traditional CS, IS and SE programs more often report declines, while AI, cybersecurity, data science and computer engineering more often report stable or growing enrollment — [CRA, Apr 2026](https://cra.org/crn/2026/04/cerp-pulse-survey-a-snapshot-of-2025-26-graduate-computing-enrollment-patterns/)

#### 3e. Layoffs attributed to AI

- Challenger, Gray & Christmas, October 2026 report (released 5 Nov 2026) [M, employer-stated reasons]: 43,994 cuts in October (lowest October since 2023, −71% YoY); 617,189 YTD. AI cited for 1,265 cuts in October (lowest month of 2026) and 121,401 YTD (about 20%); 193,226 AI-cited cuts cumulative since 2023. "Market/Economic Conditions" (130,531 YTD) overtook AI as the top reason. Technology sector: 5,576 in October, 171,501 YTD, +21% vs 141,159 in the same period of 2025 — [Challenger](https://www.challengergray.com/blog/october-layoffs-at-three-year-low-seasonal-hiring-plans-up-26/) (primary)
- AI's share of announced cuts was about 5% in 2025 and about 23% in H1 2026 — [Latin Times](https://www.latintimes.com/ai-cited-us-tech-layoffs-2026-601307) (secondary)
- TrueUp count: 206,817 tech layoffs across 712 events as of 13 Nov 2026 — [Latin Times](https://www.latintimes.com/ai-cited-us-tech-layoffs-2026-601307) (secondary)
- Skeptical audit: of 119 layoff events tagged AI-related on Layoffs.fyi from January to early November 2026, only 27 came with a company claim that AI had reduced staffing needs; many were "refocusing on AI" (cost cuts to fund AI spend) — [tech-insider](https://tech-insider.org/tech-layoffs-2026-ai-workforce-impact/) (secondary)
- Microsoft: first voluntary retirement program (April 2026); 4,800 layoffs announced July 2026; on 26 Oct 2026 voluntary exit packages offered to about 60,000 employees (about a quarter of the workforce; US, Canada, India, UK; level 70 and below; decision deadline early December). Nadella on 18–19 Nov 2026 framed it as an "AI-first" reorganization and declined to rule out layoffs: "I wish I could just sit here and say it'll all be the same. I cannot" — [CNBC](https://www.cnbc.com/2026/10/26/microsoft-msft-voluntary-buyouts.html); [TechCrunch](https://techcrunch.com/2026/11/18/microsoft-ceo-satya-nadella-explains-why-he-asked-60k-employees-to-quit); [Windows Latest](https://www.windowslatest.com/2026/11/19/asked-if-60000-exit-offers-mean-ai-layoffs-at-microsoft-satya-nadella-said-i-wish-i-could-just-sit-here-and-say-itll-all-be-the-same-i-cannot/)
- Meta: about 8,000 jobs cut (about 10% of workforce) and about 6,000 open roles cancelled in spring 2026; Meta describes this as efficiency and says AI coding mandates and layoffs are unrelated — [HCA Mag](https://www.hcamag.com/us/specialization/transformation/meta-to-cut-10-of-its-workforce-as-zuckerberg-redirects-billions-toward-ai/572933); [Business Matters](https://bmmagazine.co.uk/news/meta-layoffs-8000-jobs-ai-investment-2026/) (secondary; sources disagree on dates)
- Coinbase tied its cut to engineers shipping faster with AI; Salesforce began undisclosed cuts the week of 16 Nov 2026 — [Invezz](https://invezz.com/ie/news/2026/11/12/ai-layoffs-in-2026-so-far-121401-us-job-cuts-and-the-firms-jobs-and-regions-hit/); [theworkersrights](https://theworkersrights.com/salesforce-layoffs-2026-ai-skills-job-security) (secondary)

#### 3f. Anthropic Economic Index

- Releases through 2026: January 2026 report found augmentation (52% of conversations) overtook automation (45%) on Claude.ai; March 2026 report found automation "decreased sharply" in API data; latest full report "Cadences" dated 26 June 2026 (data 10 Apr – 10 Jun 2026, linked survey of about 9,700 respondents) — [jobroute](https://www.jobroute.ai/blog/anthropic-economic-index-2026-what-three-releases-show) (secondary); index page: [Anthropic](https://www.anthropic.com/economic-index)
- Earlier coding baselines: 79% of Claude Code conversations classed as automation vs 49% on Claude.ai (2025); 77% of API records automation vs 12% augmentation (September 2025 report) — [Anthropic primitives post](https://www.anthropic.com/research/economic-index-primitives); [zenvanriel](https://zenvanriel.com/ai-engineer-blog/anthropic-economic-index-ai-workforce-impact-data/) (secondary)

### Inferences
- The three strongest datasets agree on shape and disagree on magnitude: Stanford/ADP (large entry-level gap), Fed/CPS (deceleration in coder employment, still growing), Indeed (postings recovering, senior-weighted). A defensible summary for students: fewer entry doors, not fewer developers.
- 2026 broke the simple "AI is destroying developer jobs" storyline in postings data: since Claude Code's launch date, software postings outgrew the market by about 22 points. The same data say the new demand is for people who can direct and review agents.
- Salary and unemployment data for CS graduates point in opposite directions (highest projected starting pay, among the highest unemployment rates). This is consistent with a bimodal market in which those hired are paid well and more are not hired at all, and with the Stanford finding that adjustment is through employment rather than pay.
- Employer-stated AI attribution is a weak measure: it peaked in spring–summer 2026 and collapsed to 1,265 in October while tech cuts stayed elevated YTD, and audits find most "AI layoffs" are capital reallocation.
- NY Fed major-level unemployment uses 2024 ACS data, so it predates most agentic-coding adoption; it should not be shown as a 2026 outcome.

### Gaps
- I did not open BLS CPS/OEWS tables; no 2026 monthly or annual BLS employment count for software developers is in these notes. The BLS TED link's title refers to 2024–34 and may not be the August 2026 release.
- ADP's own research publications, NY Fed Liberty Street analysis of AI and hiring, Yale Budget Lab tracker updates, and OpenAI economic research were not retrieved.
- SignalFire and Handshake Class-of-2026 reports were seen only through blogs with mutually inconsistent figures (new-grad hiring at big tech "down more than 50%" vs "about 65%" since 2019); not usable without the originals.
- No verified Class-of-2026 placement outcome data (as opposed to projections) was found; NACE first-destination results for 2026 are not yet published.
- Amazon 2026 layoffs and any Jassy attribution to AI were not found in this session.
- The software-developer-specific 22–25 series in the August 2026 Stanford update (as opposed to the all-exposed-occupations figure) was not extracted; it is in the paper's figures.

---

## 4. Prediction scorecard

### Takeaway
Predictions about what AI can do inside frontier labs have largely come true on or near schedule (most code at Anthropic and Google is AI-written), while predictions about economy-wide effects (90% of all code, mass white-collar automation) have not been met by their deadlines or are still open. Skeptics' near-term calls (no AGI in 2026, agents not yet reliable) have mostly held, though their predictions of weak commercial returns sit badly beside 2026 revenue figures.

### Cited Findings

| Who | Date made | Prediction | Deadline | Status at 19 Nov 2026 | Sources |
|---|---|---|---|---|---|
| Dario Amodei | 10 Mar 2025 (CFR) | AI writing 90% of code in 3–6 months; "essentially all" in 12 months | Sep 2025; Mar 2026 | Missed as an industry-wide claim; met or nearly met inside Anthropic (more than 80% of merged code by May 2026; Cherny "pretty much 100%"). Amodei later said it was true "at least at some places" and called it a weak criterion. Broadest measure: agents start more than 40% of GitHub PRs (Sep 2026); Google 75%. | [Traictory](https://traictory.com/news/2026-08-30-amodei-90-percent-code-prediction); [Zvi on Dwarkesh interview](https://thezvi.substack.com/p/on-dwarkesh-patels-2026-podcast-with); [GitHub](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/) |
| Dario Amodei | May 2025 (Axios) | AI could eliminate half of entry-level white-collar jobs and push unemployment to 10–20% within 1–5 years | 2026–2030 | Open. Direction partly supported for entry level (Stanford: 19% relative shortfall for ages 22–25 in exposed jobs); no economy-wide displacement; overall unemployment about 4.2%. | [Axios](https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic) (background, not re-verified); [Stanford](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf) |
| Mark Zuckerberg | Jan 2025 (Rogan) | In 2025 Meta and others will have AI that can act as a mid-level engineer | end 2025 | Not met as stated in 2025; a prediction ledger notes agents handled substantial bounded work but "mid-level engineer" bundles judgment and ownership, and Meta shifted the timeline into 2026. | [kingy.ai ledger](https://kingy.ai/blog/ai-prediction-ledger/) (secondary) |
| Mark Zuckerberg | Apr 2025 (LlamaCon) | Within a year maybe half of development done by AI (scope ambiguous: Llama project or Meta) | Apr 2026 | Unverified. Meta published no measured share; reports describe internal targets (65% of engineers with more than 75% AI-assisted code by mid-2026). | [HCA Mag](https://www.hcamag.com/us/specialization/transformation/meta-to-cut-10-of-its-workforce-as-zuckerberg-redirects-billions-toward-ai/572933) (secondary) |
| Satya Nadella | Apr 2025 | Statement, not forecast: 20–30% of Microsoft repo code written by AI | n/a | No updated figure found. Microsoft research shows about 24% more merged PRs for CLI-agent adopters; company offered exits to about 60,000 staff in Oct 2026. | [Yahoo Tech](https://tech.yahoo.com/articles/microsoft-says-30-code-now-114621008.html); [arXiv 2607.01418](https://arxiv.org/abs/2607.01418); [CNBC](https://www.cnbc.com/2026/10/26/microsoft-msft-voluntary-buyouts.html) |
| Sundar Pichai | Oct 2024 → Apr 2026 | Statements: 25% → 50% (fall 2025) → 75% (Apr 2026) of new Google code AI-generated | n/a | Measured trajectory, self-reported. | [Google blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/); [Semafor](https://www.semafor.com/article/04/24/2026/google-ceo-says-75-of-companys-new-code-is-ai-generated) |
| Mustafa Suleyman | Feb 2026 (FT) | Most computer-based white-collar tasks fully automated within 12–18 months | Feb–Aug 2027 | Open; not yet scoreable. Nine months in, evidence shows modest measured productivity gains and entry-level hiring effects, not broad automation. | [Fortune](https://fortune.com/2026/02/13/when-will-ai-kill-white-collar-office-jobs-18-months-microsoft-mustafa-suleyman/); [eWeek](https://www.eweek.com/news/microsoft-ai-ceo-18-months-white-collar-jobs/) |
| GitHub | Oct 2026 | If current pace holds, within two years most code pushed to GitHub could be agent-written | about Oct 2028 | Open. Base: 17% → more than 40% of PRs agent-started in six months. | [CNBC](https://www.cnbc.com/2026/10/11/ai-software-developer-jobs.html) |
| AI 2027 authors (Kokotajlo et al.) | Apr 2025 | Superhuman coder around early 2027 in the scenario | 2027 | Open. Authors pushed timelines out (27 Jan 2026 clarification; Kokotajlo's automated-coder median moved to late 2029, then back to mid-2028), then on 10 Nov 2026 said all six now expect a superhuman AI researcher in 2027; Kokotajlo's median moved from Dec 2028 (Aug 2026) to May 2027 (Nov 2026). | [Forbes, 12 Nov 2026](https://www.forbes.com/sites/anishasircar/2026/11/12/ai-futures-project-pulls-its-intelligence-explosion-forecast-into-2027/) (page blocked; via search summary); [Wikipedia: AI Futures Project](https://en.wikipedia.org/wiki/AI_Futures_Project) |
| BLS | Aug 2026 | Software developer employment +10% over 2025–35 (prior edition: +15.8% over 2024–34); programmers −7% | 2035 | Open; the downward revision is itself a data point. | [CNBC](https://www.cnbc.com/2026/10/11/ai-software-developer-jobs.html) |
| Gary Marcus | Dec 2025 / Jan 2026 | No AGI in 2026 (or 2027); 2025 was peak bubble; backlash to generative AI will grow; agents will stay unreliable | end 2026 | "No AGI" holding. Self-graded 16 of 17 high-confidence 2025 predictions correct. His claim that LLMs "will never be all that profitable" sits against Anthropic's $33.2B nine-month revenue alongside an $80.7B H1 net loss (mostly non-cash). | [Marcus Substack](https://garymarcus.substack.com/p/six-or-seven-predictions-for-ai-2026); [Marcus on X](https://x.com/GaryMarcus/status/2062409773866455385); [Fortune](https://fortune.com/2026/10/26/anthropics-s-1/) |

- A third-party tracker lists Amodei's 90% claim as "Missed" with the essentially-all deadline passing in March 2026, and cites more than 320,000 agent-attributed commits per month in open source by April 2026 as substantial but not 90% — [AI Forecast Ledger](https://aiforecastledger.com/); [Traictory](https://traictory.com/news/2026-08-30-amodei-90-percent-code-prediction) (secondary)
- The AI Futures Project also published "AI 2040: Plan A" on 9 July 2026, and Kokotajlo testified to a US Senate subcommittee on 30 Sep 2026 — [Wikipedia](https://en.wikipedia.org/wiki/AI_Futures_Project)

### Inferences
- Pattern for the lecture: "inside-the-lab" predictions verified, "whole-economy" predictions missed or pending. Diffusion, review capacity and organizational bottlenecks (Section 2) are the gap between the two.
- Deadline predictions failed mostly on scope words ("all code", "most tasks") rather than on direction. Every measured adoption series moved the way the forecasters said, later and narrower.
- Forecasters on both sides revised in 2026: AI 2027 authors moved timelines out and then back in within ten months, which is a useful illustration of forecast instability for students.

### Gaps
- No verified, dated 2025–2026 predictions with deadlines were retrieved this session for Sam Altman, Jensen Huang, Demis Hassabis, Yann LeCun, or Narayanan and Kapoor; two targeted searches returned nothing usable. From prior knowledge (not re-verified, no URLs checked): Altman wrote in January 2025 that 2025 might see the first AI agents "join the workforce"; Hassabis has given roughly 5–10 year AGI timelines; LeCun has argued LLMs are a dead end for human-level AI; Narayanan and Kapoor's "AI as Normal Technology" (April 2025) predicts slow, decades-long diffusion. These need sourcing before use.
- Morgan Stanley's retraining view, already in the deck, was not re-checked against 2026 outcomes.
- Amodei's original CFR wording and the Axios interview were not re-opened; dates are from secondary scorecards and prior knowledge.
- The Forbes article on the 10 Nov 2026 AI Futures update returned 403; revision dates and medians are from search summaries and conflict in places (one guide gives Kokotajlo's automated-coder median as November 2027 as of August 2026).

---

## 5. Practice: how day-to-day software engineering changed in 2026

### Takeaway
The constraint moved from writing code to reviewing, integrating and securing it. Review time rose 49% to roughly 5x depending on the dataset, AI now writes about a quarter of review comments, agents became an attack surface in CI/CD, AI found real vulnerabilities at scale for both defenders and attackers, and open-source maintainers responded with disclosure rules, bans and new GitHub controls.

### Cited Findings

#### 5a. Review bottleneck and workflow

- PR submission-to-merge time +49% (7.03 → about 10.5 days) after agent adoption; formal change requests nearly doubled; share of workers doing any review +14%; share writing code unchanged — [Chen and Stratton via ComplexDiscovery](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/)
- Median review time about 5x and PR size +51% on high-AI teams — [Faros AI](https://www.faros.ai/research/ai-acceleration-whiplash)
- AI reviewers: nearly 80% of firms used an AI review tool by March 2026; AI wrote 23.3% of review comments; 10.8% of PRs got at least one AI comment (Jellyfish panel); 25% of PRs reviewed by an AI agent (Faros) — [ComplexDiscovery](https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/); [Faros AI](https://www.faros.ai/research/ai-acceleration-whiplash)
- Sonar 2026 State of Code (1,100+ developers): 38% say reviewing AI code takes more effort than reviewing colleagues' code; 96% do not fully trust AI code to be functionally correct — [DEV Community](https://dev.to/code-board/the-review-bottleneck-why-more-ai-code-means-slower-teams-in-2026-1e5n) (secondary)
- Background and cloud agents at scale: Copilot cloud agent usage +230% YoY; 55% of Copilot MAU use agentic features; agent PRs are larger (87% multi-file) — [GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
- Parallel agents collide: merge conflicts in 19.8% of same-agent PR pairs and 41.7% of cross-agent pairs — [arXiv 2607.04697](https://arxiv.org/html/2607.04697v2)
- Tooling response: GitHub stacked PRs (preview 30 Jul 2026, 264,000+ users by September); multi-model routing (63% of paying Copilot users used Auto selection in September) — [GitHub Blog](https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)
- Spec-driven governance is proposed in the research literature as a way to cut volume and defect density of generated code; committed agent configuration files ("a few pages of Markdown") are associated with lower quality cost after agent adoption — [arXiv 2605.01160](https://arxiv.org/pdf/2605.01160); [arXiv 2608.25241](https://arxiv.org/pdf/2608.25241) (titles and summaries only)
- Developers run multiple agents concurrently, enough to break time-tracking in METR's experiment — [METR](https://metr.org/blog/2026-02-24-uplift-update/)
- Cost governance has become routine engineering management (38% of organizations cap usage) — [Stack Overflow Blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)
- Build-versus-buy shifted: 32% of organizations declined a software purchase because agents could build it in-house — [McKinsey](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/the-state-of-ai-in-2026-on-the-road-to-roi.pdf) (via search summary)

#### 5b. Security incidents involving coding agents

- "Clinejection" (17 Feb 2026): a malicious GitHub issue title chained an authorization bypass, indirect prompt injection and environment-variable exfiltration into an unauthorized npm publish of the Cline package; malicious version available about eight hours — [Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-claude-code-github-action-prompt-injection/)
- "Comment and Control" (2026): crafted GitHub comments, PR titles and issue bodies hijacked Claude Code, Gemini CLI and GitHub Copilot Agent running in GitHub Actions; described as the first cross-vendor demonstration of one injection pattern — [iTechGuides](https://www.itechguides.com/how-ai-coding-agents-become-supply-chain-risks-through-prompt-injection/) (secondary)
- "PromptPwnd" class (Aikido Security): at least five Fortune 500 companies found with vulnerable AI-agent CI workflows as of mid-2026 — [iTechGuides](https://www.itechguides.com/how-ai-coding-agents-become-supply-chain-risks-through-prompt-injection/) (secondary)
- Hugging Face disclosed on 16 Jul 2026 an autonomous-agent intrusion that included an attempted supply-chain compromise of an open-source project using fake identities and social engineering of a maintainer — [PointGuard AI tracker](https://www.pointguardai.com/ai-security-incident-tracker) (secondary)
- Agents can be steered into installing attacker-chosen packages via setup instructions — [arXiv 2607.15143](https://arxiv.org/pdf/2607.15143)

#### 5c. AI finding vulnerabilities at scale

- Anthropic Frontier Red Team: more than 500 validated high-severity vulnerabilities found in open-source projects using Claude Opus 4.6 — [Anthropic](https://www.anthropic.com/research/zero-days)
- Google Big Sleep: 20 previously unknown vulnerabilities in open-source software by August 2025; blocked exploitation of SQLite CVE-2025-6965 — [Blue Ridge](https://blue-ridge.co/ai-is-finding-the-vulnerabilities-first/) (secondary)
- January 2026 OpenSSL release: all 12 disclosed zero-days reportedly AI-found; the same post notes curl cancelled its bug bounty — [LessWrong](https://www.lesswrong.com/posts/7aJwgbMEiKq5egQbd/ai-found-12-of-12-openssl-zero-days-while-curl-cancelled-its) (secondary)
- Offense: Google Threat Intelligence reported on 11 May 2026 the first observed case of a threat actor using AI to both discover and weaponize a zero-day — [LLM-Hacking](https://www.llm-hacking.com/hacks/ai-zero-day-autonomous-malware-gtig.md/) (secondary)
- Noise: AI-generated reports to the Linux kernel rose to 5–10 per day since January 2026; Greg Kroah-Hartman reportedly found 4 of 30 frontier-model-flagged issues legitimate — [Techzine](https://www.techzine.eu/blogs/security/141699/why-open-source-faces-its-biggest-security-threat-in-2026/) (secondary)

#### 5d. Open-source maintainers' responses

- Linux Foundation survey (20 Oct 2026, presented at All Things Open in Raleigh): 59% of maintainers report rising contribution volume since GenAI (69% at large projects); 25% of incoming PRs judged low-quality "AI slop" (31% at large projects); 53% disagree that GenAI improved community trust; 35% of projects have a formal policy permitting GenAI, 32% have none and no plans; 46% say GenAI increases the need for mentorship — [Linux Foundation](https://www.linuxfoundation.org/press/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop) (primary); [The Register](https://www.theregister.com/ai-and-ml/2026/10/21/ai-cuts-coding-time-but-its-also-filling-open-sources-inbox-with-crap/5304389)
- Policy catalogue (12 Nov 2026): 23 projects ban AI-generated contributions, 191 restrict them, 6 explicitly allow — [DEV Community](https://dev.to/dev_barron/23-open-source-projects-now-refuse-ai-generated-prs-6-things-their-policies-say-reviewers-are-2j44) (secondary); academic survey of policies: [arXiv 2609.07542](https://arxiv.org/html/2609.07542)
- Kubernetes (26 Jun 2026): AI assistance must be disclosed; PRs whose authors cannot personally explain the change are closed — [Kubernetes blog](https://kubernetes.io/blog/2026/06/26/open-source-maintainership-in-the-age-of-ai/)
- GitHub added repository controls to disable PRs entirely, restrict them to collaborators, or cap concurrent open PRs from outside contributors — [Crypto Briefing](https://cryptobriefing.com/github-restricts-pull-requests-ai-slop/) (secondary)

### Inferences
- The engineer's job description changed in the measured data: more people review, the same share write, and a quarter of review commentary is now machine-generated. "Reviewing agent output" is the 2026 core skill the evidence supports teaching.
- Security effects are two-sided and both are measured: agents enlarge the attack surface (prompt injection through issues and comments is a new vulnerability class) while AI-driven discovery finds bugs faster than maintainers can triage them.
- Open source is the visible commons problem: generation is nearly free, review is not, so maintainers ration attention through policy.

### Gaps
- No survey quantifying adoption of spec-driven development, multi-agent orchestration frameworks or background agents as named practices was found; evidence is indirect (Octoverse usage growth, research papers).
- Several incident accounts come from trackers and blogs; the Hugging Face disclosure, Aikido research, GTIG report and the curl bug-bounty cancellation should be confirmed at primary sources. No "Claude Mythos" material was found.
- No measured count of production incidents or CVEs causally attributed to AI-generated code (as opposed to agent tooling) was found beyond vendor telemetry (Faros incidents per PR, New Relic survey).

---

## 6. Education: how CS programs are responding in 2026

### Takeaway
Programs face falling intake (new CS bachelor's enrollment −12.9% in the Taulbee cohort; preliminary fall 2026 Clearinghouse data about −12%) at the same moment that degree output is at a record high. Responses so far are mostly at course level: agent-centred project courses, AI literacy for all majors, "write by hand, then compare with AI" assignments, and proposals to turn introductory programming into early software engineering.

### Cited Findings

- Enrollment pressure: see Section 3d (CRA Taulbee, NSC, CERP pulse) — [CRA, June 2026](https://cra.org/crn/2026/06/cra-update-new-cra-taulbee-survey-findings-show-record-degree-production-alongside-a-cooling-enrollment-pipeline/)
- Brown University ran "Agentic Studio" in spring 2026, a project course on what coding agents can and cannot do and the human engineer's role; instructors concluded agentic coding could justify restructuring introductory CS — [Brown University, 11 Jun 2026](https://www.brown.edu/news/2026-06-11/agentic-studio-ai-programming)
- Colorado School of Mines: AI literacy for all undergraduates through CSCI128; in upper-level Software Engineering students write code by hand and then compare with generative-AI output; AI-focused graduate degree under consideration — [Mines, 2026](https://www.mines.edu/news/all-news/2026/computer-science-curriculum-tackles-ais-growing-influence-head-on-.html)
- George Washington University is revising its CS curriculum explicitly in response to falling enrollment: keep a fundamentals core, add AI development techniques and specialized tracks (cybersecurity, AI/ML) — [GW Hatchet, 9 Nov 2026](https://gwhatchet.com/2026/11/09/computer-science-department-revamps-curriculum-to-combat-falling-enrollment-in-the-age-of-ai/)
- MIT "Missing Semester" 2026 edition integrates AI tools and autonomous coding agents with emphasis on oversight — [I Programmer](https://www.i-programmer.info/news/150-training-a-education/19146-mits-missing-semester-of-your-cs-education-2026-edition.html)
- CACM opinion: introductory courses should become early software-engineering courses; a radical option has students write designs and specifications while agents write most code — [CACM](https://cacm.acm.org/opinion/teaching-novice-computing-and-programming-in-the-agentic-ai-era/)
- Curriculum proposals: "ASE-26: a curriculum for agentic software engineering as a discipline" and a workshop white paper recommending AI be woven through the curriculum, not added as one course — [arXiv 2606.01152](https://arxiv.org/abs/2606.01152); [arXiv 2606.07545](https://arxiv.org/html/2606.07545v1)
- Students are moving toward specialized computing degrees (AI, data science, cybersecurity) and away from general CS, per CRA — [CRA CERP, Apr 2026](https://cra.org/crn/2026/04/cerp-pulse-survey-a-snapshot-of-2025-26-graduate-computing-enrollment-patterns/)
- Skills signal from industry surveys: 79% of developers want to build AI skills, 52% are learning new coding skills; juniors are more likely than seniors to rate AI solutions above their own (60% vs 47%) — [Stack Overflow Blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/); [JetBrains](https://blog.jetbrains.com/research/2026/11/state-of-developer-ecosystem-2026/) (via search summary)
- Open-source maintainers: 46% say GenAI increases the need for mentorship — [Linux Foundation](https://www.linuxfoundation.org/press/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop)

### Inferences
- The evidence in Sections 2, 3 and 5 points to the same curricular priorities: specification, review, testing, security and system-level judgment, since those are where measured bottlenecks and senior-weighted hiring now sit.
- The junior over-trust finding (60% rate AI above their own work) combined with METR's perception gap is a concrete argument for teaching verification before delegation.
- Enrollment declines at graduate level are confounded by visa policy, so attributing the whole CS enrollment drop to AI job fears would overstate the case.

### Gaps
- No systematic count of how many US CS departments have changed degree requirements for agentic coding was found; the evidence is a handful of institutional announcements and proposals.
- ACM/IEEE curricular guidance updates and ABET positions for 2026 were not searched.
- No outcome data yet on whether redesigned courses improve graduate placement.
- Nothing NCSU-specific was searched.
