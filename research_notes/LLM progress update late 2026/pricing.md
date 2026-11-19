# API list prices for frontier models

Read date: 19 November 2026. Prices are USD per million tokens, standard tier, base context window, with no batch discount. Cached input is the provider's cache-read (cache-hit) price.

## How to read this file

- **PRIMARY** means the figure was read this session from the provider's own pricing page, docs, changelog or pricing API. **ARCHIVE** means it was read from an Internet Archive snapshot of the provider's page, with the snapshot date in the note. No row rests on press or aggregator sources, so SECONDARY is unused. **UNVERIFIABLE** marks a price that could not be traced.
- Release dates marked `*` come from the model ID suffix or general knowledge and were not re-verified against a provider page this session. Unmarked dates come from the provider's changelog, release notes or deprecation schedule. A blank date means it was not captured.
- "Price effective" is filled only where the price changed after launch. Where a model has two rows (launch price and later price), both are in the CSV.
- Derived figures are flagged in the note. Nothing was converted from CNY: every price below was published in USD by the provider.
- Page-data extraction: OpenAI, xAI and Artificial Analysis render tables client-side, so their figures were read from the JSON embedded in the page HTML. xAI stores prices in units of 1e-4 USD per million tokens (20000 = $2.00).

## OpenAI

| Model | Release | Input $/MTok | Output $/MTok | Cached input $/MTok | Price effective | Verdict | Note | Source |
|---|---|---|---|---|---|---|---|---|
| GPT-4 (gpt-4, 8K) | 2023-03-14* | 30.00 | 60.00 | n/a | launch | PRIMARY | Price from the current model page; launch-day page not re-fetched. 8K context. | [link](https://developers.openai.com/api/docs/models/gpt-4) |
| GPT-4 Turbo (gpt-4-turbo) | 2023-11-06* | 10.00 | 30.00 | n/a | launch | PRIMARY | Price from the current model page. | [link](https://developers.openai.com/api/docs/models/gpt-4-turbo) |
| GPT-4o (gpt-4o) | 2024-05-13* | 2.50 | 10.00 | 1.25 | date not traced | PRIMARY | Current list price, marked deprecated on the pricing page. The higher May 2024 launch price was not traced this session. | [link](https://developers.openai.com/api/docs/pricing) |
| o1 | 2024-12-17* | 15.00 | 60.00 | 7.50 | launch | PRIMARY | Price from the current model page. | [link](https://developers.openai.com/api/docs/models/o1) |
| o3 (launch price) | 2025-04-16* | 10.00 | 40.00 | 2.50 | launch | ARCHIVE | Snapshot dated 2025-04-30. | [link](https://web.archive.org/web/20250430193406/https://openai.com/api/pricing/) |
| o3 (after cut) | 2025-04-16* | 2.00 | 8.00 | 0.50 | 2025-06-10 | PRIMARY | Changelog entry dated Jun 10 (2025) says o3 prices were reduced; the amount of the cut is the difference from the archived launch price. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-5 (gpt-5) | 2025-08-07 | 1.25 | 10.00 | 0.125 | launch | PRIMARY | Marked deprecated on the pricing page. Release date from the API changelog. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-5.2 (gpt-5.2) | 2025-12-11 | 1.75 | 14.00 | 0.175 | launch | PRIMARY | Release date from the API changelog. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-5.4 (gpt-5.4) | 2026-03-05 | 2.50 | 15.00 | 0.25 | launch | PRIMARY | Prompts over 272K input tokens: 2x input and 1.5x output for the full request. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-5.5 (gpt-5.5) | 2026-04-24 | 5.00 | 30.00 | 0.50 | launch | PRIMARY | Over 272K: 2x input and 1.5x output. API release date from the changelog. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-5.6 Sol (launch price) | 2026-07-09 | 5.00 | 30.00 | 0.50 | launch | ARCHIVE | Snapshot dated 2026-07-16. Consistent with the changelog's stated 20% and 33% reductions. | [link](https://web.archive.org/web/20260716103153/https://developers.openai.com/api/docs/pricing) |
| GPT-5.6 Sol (promotional price) | 2026-07-09 | 4.00 | 20.00 | 0.40 | 2026-08-21 | PRIMARY | Described as promotional pricing available until 2026-11-30. Over 272K: $8 / $30. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-5.6 Terra (launch price) | 2026-07-09 | 2.50 | 15.00 | 0.25 | launch | ARCHIVE | Snapshot dated 2026-07-16. | [link](https://web.archive.org/web/20260716103153/https://developers.openai.com/api/docs/pricing) |
| GPT-5.6 Terra (after cut) | 2026-07-09 | 2.00 | 12.00 | 0.20 | 2026-07-30 | PRIMARY | Changelog: Terra costs 20% less from July 30. Over 272K: $4 / $18. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-5.6 Luna (launch price) | 2026-07-09 | 1.00 | 6.00 | 0.10 | launch | ARCHIVE | Snapshot dated 2026-07-16. | [link](https://web.archive.org/web/20260716103153/https://developers.openai.com/api/docs/pricing) |
| GPT-5.6 Luna (after cut) | 2026-07-09 | 0.20 | 1.20 | 0.02 | 2026-07-30 | PRIMARY | Changelog: Luna costs 80% less from July 30. Over 272K: $0.40 / $1.80. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-6 Astra (gpt-6-astra) | 2026-09-03 | 10.00 | 50.00 | 1.00 | launch | PRIMARY | Over 272K: $20 / $75. Fast mode 2x; Ultrafast $60 / $300. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-6 Sol (gpt-6-sol) | 2026-09-22 | 2.00 | 10.00 | 0.20 | launch | PRIMARY | Over 272K: $4 / $15. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-6 Luna (gpt-6-luna) | 2026-09-22 | 0.10 | 0.50 | 0.01 | launch | PRIMARY | Over 272K: $0.20 / $0.75. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-6.1 Sol (gpt-6.1-sol) | 2026-09-29 | 2.00 | 10.00 | 0.10 | launch | PRIMARY | Cached input is 5% of input. Over 272K: $4 / $15. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-6.1 Terra (gpt-6.1-terra) | 2026-10-26 | 1.00 | 5.00 | 0.05 | launch | PRIMARY | Over 272K: $2 / $7.50. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-6.2 Astra (gpt-6.2-astra) | 2026-11-17 | 8.00 | 40.00 | 0.40 | launch | PRIMARY | Over 272K: $16 / $60. Changelog entry is dated Nov 17. | [link](https://developers.openai.com/api/docs/pricing) |
| GPT-6.2 Sol (gpt-6.2-sol) | 2026-11-17 | 2.00 | 10.00 | 0.10 | launch | PRIMARY | Over 272K: $4 / $15. | [link](https://developers.openai.com/api/docs/pricing) |

## Anthropic

| Model | Release | Input $/MTok | Output $/MTok | Cached input $/MTok | Price effective | Verdict | Note | Source |
|---|---|---|---|---|---|---|---|---|
| Claude 3 Opus | 2024-03-04* | 15.00 | 75.00 | 1.50 | launch | ARCHIVE | Snapshot dated 2025-05-28. Model is retired and absent from the current page. | [link](https://web.archive.org/web/20250528184604/https://docs.anthropic.com/en/docs/about-claude/pricing) |
| Claude 3.5 Sonnet | 2024-06-20* | 3.00 | 15.00 | 0.30 | launch | ARCHIVE | Snapshot dated 2025-05-28. | [link](https://web.archive.org/web/20250528184604/https://docs.anthropic.com/en/docs/about-claude/pricing) |
| Claude 3.7 Sonnet | 2025-02-24* | 3.00 | 15.00 | 0.30 | launch | ARCHIVE | Snapshot dated 2025-05-28. | [link](https://web.archive.org/web/20250528184604/https://docs.anthropic.com/en/docs/about-claude/pricing) |
| Claude Opus 4 | 2025-05-22* | 15.00 | 75.00 | 1.50 | launch | PRIMARY | Listed as retired on the current page. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Opus 4.1 | 2025-08-05 | 15.00 | 75.00 | 1.50 | launch | PRIMARY | Listed as retired. Date from the model ID suffix 20250805. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Sonnet 4.5 | 2025-09-29 | 3.00 | 15.00 | 0.30 | launch | PRIMARY | Deprecated 2026-09-30. Date from the model ID suffix 20250929. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Opus 4.5 | 2025-11-24 | 5.00 | 25.00 | 0.50 | launch | PRIMARY | A two-thirds cut from Opus 4.1 at the same tier. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Opus 4.6 | 2026-02-05 | 5.00 | 25.00 | 0.50 | launch | PRIMARY | 1M context at standard pricing since 2026-03-13. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Sonnet 4.6 | 2026-02-17 | 3.00 | 15.00 | 0.30 | launch | PRIMARY |  | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Opus 4.7 | 2026-04-16 | 5.00 | 25.00 | 0.50 | launch | PRIMARY | Pricing page: models from 4.7 on use a tokenizer producing roughly 30% more tokens for the same text. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Opus 4.8 | 2026-05-28 | 5.00 | 25.00 | 0.50 | launch | PRIMARY |  | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Fable 5 | 2026-06-09 | 10.00 | 50.00 | 1.00 | launch | PRIMARY |  | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Sonnet 5 | 2026-06-30 | 2.00 | 10.00 | 0.20 | 2026-08-10 | PRIMARY | Launched at introductory $2 / $10; on 2026-08-10 it became the standard price and the scheduled rise to $3 / $15 was cancelled. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Opus 5 | 2026-07-24 | 5.00 | 25.00 | 0.50 | launch | PRIMARY |  | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Fable 5.1 | 2026-09-01 | 10.00 | 50.00 | 0.25 | launch | PRIMARY | Cache reads at 0.025x input. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Opus 5.5 | 2026-09-22 | 4.00 | 20.00 | 0.20 | launch | PRIMARY | Cache reads at 0.05x input. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Sonnet 5.5 | 2026-09-28 | 2.00 | 10.00 | 0.10 | launch | PRIMARY | Cache read cut from $0.20 to $0.10 on 2026-10-07; base prices unchanged. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Haiku 5.5 | 2026-10-07 | 0.10 | 0.50 | 0.01 | launch | PRIMARY | Prompts over 100K tokens: $0.50 / $2.50 with $0.05 cache read. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |
| Claude Fable 5.2 | 2026-11-09 | 8.00 | 40.00 | 0.20 | launch | PRIMARY | Fast mode $16 / $80. | [link](https://platform.claude.com/docs/en/about-claude/pricing) |

## Google

| Model | Release | Input $/MTok | Output $/MTok | Cached input $/MTok | Price effective | Verdict | Note | Source |
|---|---|---|---|---|---|---|---|---|
| Gemini 1.5 Pro | 2024-05* | 3.50 | 10.50 | 0.875 | launch | ARCHIVE | Snapshot dated 2024-07-01. Prompts over 128K: $7.00 / $21.00. Later price cuts not traced. | [link](https://web.archive.org/web/20240701171821/https://ai.google.dev/pricing) |
| Gemini 2.5 Pro | 2025-06-17* | 1.25 | 10.00 | 0.125 | launch | PRIMARY | Over 200K: $2.50 / $15.00. Deprecated; requests route to gemini-3.8-flash on 2026-12-01. | [link](https://aistudio.google.com/docs/pricing) |
| Gemini 3 Pro Preview | 2025-11-18 | 2.00 | 12.00 | 0.20 | launch | ARCHIVE | Snapshot dated 2025-12-10. Over 200K: $4.00 / $18.00. Shut down 2026-03-09. | [link](https://web.archive.org/web/20251210221523/https://ai.google.dev/gemini-api/docs/pricing) |
| Gemini 3.1 Pro Preview | 2026-02-19 | 2.00 | 12.00 | 0.20 | launch | PRIMARY | Over 200K: $4.00 / $18.00. | [link](https://aistudio.google.com/docs/pricing) |
| Gemini 3.5 Flash | n/a | 1.50 | 9.00 | 0.15 | launch | ARCHIVE | Same price in the 2026-06-11 snapshot. Deprecated 2026-10-08 and routed to 3.6 Flash. Release date not captured. | [link](https://web.archive.org/web/20260906110741/https://ai.google.dev/gemini-api/docs/pricing) |
| Gemini 3.6 Flash | 2026-07-21 | 0.75 | 3.75 | 0.075 | launch | PRIMARY | Scheduled to double to $1.50 / $7.50 on 2027-01-01. | [link](https://aistudio.google.com/docs/pricing) |
| Gemini 3.7 Flash | 2026-08-13 | 0.75 | 3.75 | 0.075 | launch | ARCHIVE | Snapshot dated 2026-09-06. Deprecated 2026-10-08 and routed to 3.8 Flash. | [link](https://web.archive.org/web/20260906110741/https://ai.google.dev/gemini-api/docs/pricing) |
| Gemini 3.8 Flash | 2026-09-02 | 0.75 | 3.75 | 0.075 | launch | PRIMARY | Scheduled to double to $1.50 / $7.50 on 2027-01-01. | [link](https://aistudio.google.com/docs/pricing) |
| Gemini 4 Argon | 2026-10-13 | 2.00 | 10.00 | 0.10 | launch | PRIMARY | Price through 2026-11-30; $4.00 / $20.00 from 2026-12-01. | [link](https://aistudio.google.com/docs/pricing) |
| Gemini 4 Carbon | 2026-11-10 | 2.00 | 10.00 | 0.10 | launch | PRIMARY | Introductory price through 2026-11-30; $4.00 / $20.00 with $0.20 caching from 2026-12-01. | [link](https://aistudio.google.com/docs/pricing) |
| Gemini 4 Hydrogen | 2026-11-12 | 1.50 | 7.50 | 0.075 | launch | PRIMARY | Single rate across the 1M window. | [link](https://aistudio.google.com/docs/pricing) |
| Gemini 4 Neon | 2026-11-18 | 3.00 | 15.00 | 0.15 | launch | PRIMARY | Single rate across the 1M window. | [link](https://aistudio.google.com/docs/pricing) |

## xAI

| Model | Release | Input $/MTok | Output $/MTok | Cached input $/MTok | Price effective | Verdict | Note | Source |
|---|---|---|---|---|---|---|---|---|
| Grok 3 (grok-3) | 2025-04* | 3.00 | 15.00 | 0.75 | launch | ARCHIVE | Snapshot dated 2025-08-01. | [link](https://web.archive.org/web/20250801003158/https://docs.x.ai/docs/models) |
| Grok 4 (grok-4-0709) | 2025-07-09* | 3.00 | 15.00 | 0.75 | launch | ARCHIVE | Prompts over 128K: $6.00 / $30.00. | [link](https://web.archive.org/web/20250801003158/https://docs.x.ai/docs/models) |
| Grok 4.20 (launch price) | 2026-03-10 | 2.00 | 6.00 | 0.20 | launch | ARCHIVE | Snapshot dated 2026-04-02. | [link](https://web.archive.org/web/20260402074148/https://docs.x.ai/developers/models) |
| Grok 4.20 (current price) | 2026-03-10 | 1.25 | 2.50 | 0.20 | launch | PRIMARY | Date of the cut not found. From 200K prompt tokens: $2.50 / $5.00 on the whole request. | [link](https://docs.x.ai/docs/models) |
| Grok 4.5 | 2026-07-08 | 2.00 | 6.00 | 0.30 | launch | PRIMARY | From 200K prompt tokens: $4.00 / $12.00. | [link](https://docs.x.ai/docs/models) |
| Grok 4.6 | 2026-08-12 | 2.00 | 6.00 | 0.50 | launch | PRIMARY | From 200K prompt tokens: $4.00 / $12.00. | [link](https://docs.x.ai/docs/models) |
| Grok 4.7 | 2026-09-21 | 2.00 | 6.00 | 0.50 | launch | PRIMARY | From 200K prompt tokens: $4.00 / $12.00. A second price set of $2.20 / $6.60 in the page data appears to be a regional endpoint. | [link](https://docs.x.ai/docs/models) |

## Meta

| Model | Release | Input $/MTok | Output $/MTok | Cached input $/MTok | Price effective | Verdict | Note | Source |
|---|---|---|---|---|---|---|---|---|
| Muse Spark 1.1 / 1.2 / 1.3 | n/a | 1.25 | 4.25 | 0.15 | launch | PRIMARY | Contributor variants (data used for training) cost $0.10 / $0.20. Release dates not captured. | [link](https://dev.meta.ai/products/meta-model-api) |
| Muse Wonder (muse-wonder-1.0) | n/a | 4.00 | 20.00 | 0.20 | launch | PRIMARY | 1M context. Release date not captured. | [link](https://dev.meta.ai/products/meta-model-api) |
| Muse Wonder Full | UNVERIFIABLE | UNVERIFIABLE | UNVERIFIABLE | UNVERIFIABLE | launch | UNVERIFIABLE | No API price: the page lists dashes and says it is available by subscription in Muse Code. | [link](https://dev.meta.ai/products/meta-model-api) |

## DeepSeek

| Model | Release | Input $/MTok | Output $/MTok | Cached input $/MTok | Price effective | Verdict | Note | Source |
|---|---|---|---|---|---|---|---|---|
| DeepSeek-V3 (deepseek-chat) | 2024-12-26* | 0.27 | 1.10 | 0.07 | 2025-02-08 | ARCHIVE | Snapshot dated 2025-04-01. Launch promotion of $0.14 / $0.28 ran until 2025-02-08 (snapshot 2025-01-03). Off-peak 50% discount at 16:30-00:30 UTC. | [link](https://web.archive.org/web/20250401093024/https://api-docs.deepseek.com/quick_start/pricing) |
| DeepSeek-R1 (deepseek-reasoner) | 2025-01-20* | 0.55 | 2.19 | 0.14 | launch | ARCHIVE | Snapshot dated 2025-04-01. Off-peak 75% discount at 16:30-00:30 UTC. | [link](https://web.archive.org/web/20250401093024/https://api-docs.deepseek.com/quick_start/pricing) |
| DeepSeek-V4-Flash (preview price) | 2026-04-24 | 0.14 | 0.28 | 0.0028 | 2026-04-26 | ARCHIVE | Snapshot dated 2026-05-01. Cache-hit price cut to a tenth of launch on 2026-04-26. | [link](https://web.archive.org/web/20260501050639/https://api-docs.deepseek.com/quick_start/pricing) |
| DeepSeek-V4-Pro (preview list price) | 2026-04-24 | 1.74 | 3.48 | 0.0145 | launch | ARCHIVE | Sold at a 75% discount ($0.435 / $0.87); the 2026-08-01 snapshot shows only the discounted figures. | [link](https://web.archive.org/web/20260501050639/https://api-docs.deepseek.com/quick_start/pricing) |
| DeepSeek-V4-Flash (after rise, peak) | 2026-04-24 | 0.44 | 1.32 | 0.014 | 2026-08-16 | ARCHIVE | From the price table image in the provider's 2026-08-13 news post, read via archive. Off-peak is half: $0.22 / $0.66. Peak hours 01:00-04:00 and 06:00-10:00 UTC. | [link](https://web.archive.org/web/2026id_/https://api-docs.deepseek.com/news/news260813.md) |
| DeepSeek-V4-Pro (GA, peak) | 2026-08-13 | 1.32 | 3.96 | 0.044 | 2026-08-16 | ARCHIVE | Still current in the 2026-11-18 snapshot. Off-peak is half: $0.66 / $1.98. | [link](https://web.archive.org/web/20261118170941/https://api-docs.deepseek.com/quick_start/pricing/) |
| DeepSeek-V4.1-Flash (1017, peak) | 2026-09-10 | 0.30 | 1.20 | 0.006 | launch | ARCHIVE | Snapshot dated 2026-11-18; the live page reset the connection. Off-peak is half: $0.15 / $0.60. Peak is weekdays only. Price at the 2026-09-10 launch not checked. | [link](https://web.archive.org/web/20261118170941/https://api-docs.deepseek.com/quick_start/pricing/) |

## Moonshot

| Model | Release | Input $/MTok | Output $/MTok | Cached input $/MTok | Price effective | Verdict | Note | Source |
|---|---|---|---|---|---|---|---|---|
| Kimi K2 (kimi-k2-0711-preview) | 2025-07-11* | 0.60 | 2.50 | 0.15 | launch | ARCHIVE | Snapshot dated 2026-05-15. | [link](https://web.archive.org/web/20260515072943id_/https://platform.kimi.ai/docs/pricing/chat-k2.md) |
| Kimi K2.5 | n/a | 0.60 | 3.00 | 0.10 | launch | ARCHIVE | Snapshot dated 2026-05-15. Release date not captured. | [link](https://web.archive.org/web/20260515072717id_/https://platform.kimi.ai/docs/pricing/chat-k25.md) |
| Kimi K2.6 | n/a | 0.95 | 4.00 | 0.16 | launch | PRIMARY | K2 series closed to new users from 2026-10-31. Release date not captured. | [link](https://platform.moonshot.ai/docs/pricing/chat) |
| Kimi K3 | n/a | 3.00 | 15.00 | 0.30 | launch | PRIMARY | Listed by 2026-08-09 (archive). 1M context. Release date not captured. | [link](https://platform.moonshot.ai/docs/pricing/chat) |
| Kimi K3.1 Pro | n/a | 2.00 | 10.00 | 0.20 | launch | PRIMARY | Highspeed variant $4 / $20. Release date not captured. | [link](https://platform.moonshot.ai/docs/pricing/chat) |

## Z.ai

| Model | Release | Input $/MTok | Output $/MTok | Cached input $/MTok | Price effective | Verdict | Note | Source |
|---|---|---|---|---|---|---|---|---|
| GLM-5 | 2026-02-12 | 1.00 | 3.20 | 0.20 | launch | PRIMARY | Dates from the Z.ai release notes. | [link](https://docs.z.ai/guides/overview/pricing) |
| GLM-5.1 | 2026-04-07 | 1.40 | 4.40 | 0.26 | launch | PRIMARY |  | [link](https://docs.z.ai/guides/overview/pricing) |
| GLM-5.2 | 2026-06-16 | 1.40 | 4.40 | 0.26 | launch | PRIMARY |  | [link](https://docs.z.ai/guides/overview/pricing) |
| GLM-5.3 | 2026-08-18 | 1.40 | 4.40 | 0.26 | launch | PRIMARY |  | [link](https://docs.z.ai/guides/overview/pricing) |

## Alibaba

| Model | Release | Input $/MTok | Output $/MTok | Cached input $/MTok | Price effective | Verdict | Note | Source |
|---|---|---|---|---|---|---|---|---|
| Qwen3.6-Max (qwen3.6-max-preview) | n/a | 1.30 | 7.80 | n/a | launch | ARCHIVE | Snapshot dated 2026-07-18; international deployment. 128K-256K prompts: $2 / $12. Absent from the current page. | [link](https://web.archive.org/web/20260718154131/https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| Qwen3.8-Max | 2026-09-02 | 2.00 | 6.00 | n/a | launch | PRIMARY | International (Singapore) USD price. Date inferred from the snapshot name qwen3.8-max-0902. Cache discount offered but rate not captured. | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |
| Qwen4-Max | n/a | 1.50 | 4.50 | n/a | launch | PRIMARY | International (Singapore) USD price as published; no CNY conversion. Release date not captured. | [link](https://www.alibabacloud.com/help/en/model-studio/model-pricing) |

## Microsoft

| Model | Release | Input $/MTok | Output $/MTok | Cached input $/MTok | Price effective | Verdict | Note | Source |
|---|---|---|---|---|---|---|---|---|
| MAI-Thinking-1 (Global) | n/a | 2.00 | 8.00 | 0.20 | 2026-08-01 | PRIMARY | Azure Retail Prices API meter, effective date as reported by the API. | https://prices.azure.com/api/retail/prices (filter: contains(meterName,'MAI'), armRegionName eq 'eastus2') |
| MAI-Cyber-1-Flash (Global) | n/a | 0.60 | 3.50 | 0.06 | 2026-08-01 | PRIMARY | Azure Retail Prices API. | https://prices.azure.com/api/retail/prices (filter: contains(meterName,'MAI'), armRegionName eq 'eastus2') |
| MAI-Code-2-Flash (Global) | n/a | 0.05 | 0.25 | 0.005 | 2026-11-01 | PRIMARY | Azure Retail Prices API. | https://prices.azure.com/api/retail/prices (filter: contains(meterName,'MAI'), armRegionName eq 'eastus2') |

## Not found

| Provider | Model | Status |
|---|---|---|
| Meta | Muse Wonder Full | UNVERIFIABLE: no API price exists; subscription only in Muse Code ($50 or $200 a month tiers are shown on the model page). |
| Google | Gemini 1.5 Pro later price cuts | Not traced; only the July 2024 snapshot was read. |
| OpenAI | GPT-4o May 2024 launch price | Not traced; the 2024 archive snapshot did not yield a readable table. |
| xAI | Date of the Grok 4.20 price cut | Not found in the release notes. |
| DeepSeek | Live pricing page | Direct fetch failed (connection reset); the 2026-11-18 archive snapshot was used instead. |
| Moonshot, Alibaba, Meta | Several release dates | Not captured from provider pages. |

## Provider statements on price changes across generations

| Provider | Date | Statement (paraphrased from the provider's page) | Source |
|---|---|---|---|
| OpenAI | 2025-06-10 | o3 prices reduced for all API requests; archive shows $10 / $40 before and the pricing page shows $2 / $8 after. | [changelog](https://developers.openai.com/api/docs/changelog) |
| OpenAI | 2026-07-30 | GPT-5.6 Luna costs 80% less and GPT-5.6 Terra 20% less, three weeks after launch. | [changelog](https://developers.openai.com/api/docs/changelog) |
| OpenAI | 2026-08-21 | GPT-5.6 Sol cut to $4 / $20, a 20% input and 33% output reduction, labelled promotional (through 2026-11-30 per the pricing page). | [changelog](https://developers.openai.com/api/docs/changelog) |
| OpenAI | 2026-09-29 | GPT-6.1 Sol positioned as complex coding and professional work at a lower cost than GPT-6 Astra. | [changelog](https://developers.openai.com/api/docs/changelog) |
| OpenAI | 2026-11-17 | GPT-6.2 Astra lists at $8 / $40 against GPT-6 Astra's $10 / $50 (table comparison; no explicit statement read). | [pricing](https://developers.openai.com/api/docs/pricing) |
| Anthropic | 2025-11-24 | Opus 4.5 lists at $5 / $25 against Opus 4.1's $15 / $75 (table comparison). | [pricing](https://platform.claude.com/docs/en/about-claude/pricing) |
| Anthropic | 2026-04-16 | Opus 4.7 launched at the same $5 / $25 as Opus 4.6; the pricing page adds that 4.7 and later use a tokenizer producing about 30% more tokens. | [release notes](https://platform.claude.com/docs/en/release-notes/overview) |
| Anthropic | 2026-08-10 | Sonnet 5's introductory $2 / $10 became standard; the planned rise to $3 / $15 was cancelled. Sonnet 4.6 was $3 / $15. | [release notes](https://platform.claude.com/docs/en/release-notes/overview) |
| Anthropic | 2026-09-22 | Opus 5.5 launched at $4 / $20, with Opus 5 at $5 / $25. | [release notes](https://platform.claude.com/docs/en/release-notes/overview) |
| Anthropic | 2026-11-09 | Fable 5.2 costs $8 / $40, with Fable 5.1 at $10 / $50. Cache reads fell from 0.1x to 0.025x of input between Fable 5 and 5.1. | [release notes](https://platform.claude.com/docs/en/release-notes/overview) |
| Google | 2026-11-10 | Gemini 4 Carbon launched at introductory $2 / $10 through 2026-11-30, then $4 / $20. Argon carries the same schedule. | [changelog](https://aistudio.google.com/docs/changelog) |
| Google | 2026 | Gemini 3.6 and 3.8 Flash list at $0.75 / $3.75 through 2026-12-31 and double on 2027-01-01. Gemini 3.5 Flash was $1.50 / $9.00. | [pricing](https://aistudio.google.com/docs/pricing) |
| DeepSeek | 2026-08-13 | With the V4 line-up, pricing was updated and peak and off-peak rates introduced, effective 16:00 UTC on 2026-08-16. V4-Flash rose from $0.14 / $0.28 to $0.44 / $1.32 at peak ($0.22 / $0.66 off-peak). | [news post, archived](https://web.archive.org/web/2026id_/https://api-docs.deepseek.com/news/news260813.md) |
| xAI | 2026 | Grok 4.20 fell from $2 / $6 (April 2026 snapshot) to $1.25 / $2.50; Grok 4.5 to 4.7 each launched at $2 / $6. | [models](https://docs.x.ai/docs/models) |

## All rows (CSV)

```csv
provider,model,release_date,input_usd_per_mtok,output_usd_per_mtok,cached_input_usd_per_mtok,price_effective_date,verdict,source_url,note
OpenAI,"GPT-4 (gpt-4, 8K)",2023-03-14*,30.00,60.00,,,PRIMARY,https://developers.openai.com/api/docs/models/gpt-4,Price from the current model page; launch-day page not re-fetched. 8K context.
OpenAI,GPT-4 Turbo (gpt-4-turbo),2023-11-06*,10.00,30.00,,,PRIMARY,https://developers.openai.com/api/docs/models/gpt-4-turbo,Price from the current model page.
OpenAI,GPT-4o (gpt-4o),2024-05-13*,2.50,10.00,1.25,date not traced,PRIMARY,https://developers.openai.com/api/docs/pricing,"Current list price, marked deprecated on the pricing page. The higher May 2024 launch price was not traced this session."
OpenAI,o1,2024-12-17*,15.00,60.00,7.50,,PRIMARY,https://developers.openai.com/api/docs/models/o1,Price from the current model page.
OpenAI,o3 (launch price),2025-04-16*,10.00,40.00,2.50,,ARCHIVE,https://web.archive.org/web/20250430193406/https://openai.com/api/pricing/,Snapshot dated 2025-04-30.
OpenAI,o3 (after cut),2025-04-16*,2.00,8.00,0.50,2025-06-10,PRIMARY,https://developers.openai.com/api/docs/pricing,Changelog entry dated Jun 10 (2025) says o3 prices were reduced; the amount of the cut is the difference from the archived launch price.
OpenAI,GPT-5 (gpt-5),2025-08-07,1.25,10.00,0.125,,PRIMARY,https://developers.openai.com/api/docs/pricing,Marked deprecated on the pricing page. Release date from the API changelog.
OpenAI,GPT-5.2 (gpt-5.2),2025-12-11,1.75,14.00,0.175,,PRIMARY,https://developers.openai.com/api/docs/pricing,Release date from the API changelog.
OpenAI,GPT-5.4 (gpt-5.4),2026-03-05,2.50,15.00,0.25,,PRIMARY,https://developers.openai.com/api/docs/pricing,Prompts over 272K input tokens: 2x input and 1.5x output for the full request.
OpenAI,GPT-5.5 (gpt-5.5),2026-04-24,5.00,30.00,0.50,,PRIMARY,https://developers.openai.com/api/docs/pricing,Over 272K: 2x input and 1.5x output. API release date from the changelog.
OpenAI,GPT-5.6 Sol (launch price),2026-07-09,5.00,30.00,0.50,,ARCHIVE,https://web.archive.org/web/20260716103153/https://developers.openai.com/api/docs/pricing,Snapshot dated 2026-07-16. Consistent with the changelog's stated 20% and 33% reductions.
OpenAI,GPT-5.6 Sol (promotional price),2026-07-09,4.00,20.00,0.40,2026-08-21,PRIMARY,https://developers.openai.com/api/docs/pricing,Described as promotional pricing available until 2026-11-30. Over 272K: $8 / $30.
OpenAI,GPT-5.6 Terra (launch price),2026-07-09,2.50,15.00,0.25,,ARCHIVE,https://web.archive.org/web/20260716103153/https://developers.openai.com/api/docs/pricing,Snapshot dated 2026-07-16.
OpenAI,GPT-5.6 Terra (after cut),2026-07-09,2.00,12.00,0.20,2026-07-30,PRIMARY,https://developers.openai.com/api/docs/pricing,Changelog: Terra costs 20% less from July 30. Over 272K: $4 / $18.
OpenAI,GPT-5.6 Luna (launch price),2026-07-09,1.00,6.00,0.10,,ARCHIVE,https://web.archive.org/web/20260716103153/https://developers.openai.com/api/docs/pricing,Snapshot dated 2026-07-16.
OpenAI,GPT-5.6 Luna (after cut),2026-07-09,0.20,1.20,0.02,2026-07-30,PRIMARY,https://developers.openai.com/api/docs/pricing,Changelog: Luna costs 80% less from July 30. Over 272K: $0.40 / $1.80.
OpenAI,GPT-6 Astra (gpt-6-astra),2026-09-03,10.00,50.00,1.00,,PRIMARY,https://developers.openai.com/api/docs/pricing,Over 272K: $20 / $75. Fast mode 2x; Ultrafast $60 / $300.
OpenAI,GPT-6 Sol (gpt-6-sol),2026-09-22,2.00,10.00,0.20,,PRIMARY,https://developers.openai.com/api/docs/pricing,Over 272K: $4 / $15.
OpenAI,GPT-6 Luna (gpt-6-luna),2026-09-22,0.10,0.50,0.01,,PRIMARY,https://developers.openai.com/api/docs/pricing,Over 272K: $0.20 / $0.75.
OpenAI,GPT-6.1 Sol (gpt-6.1-sol),2026-09-29,2.00,10.00,0.10,,PRIMARY,https://developers.openai.com/api/docs/pricing,Cached input is 5% of input. Over 272K: $4 / $15.
OpenAI,GPT-6.1 Terra (gpt-6.1-terra),2026-10-26,1.00,5.00,0.05,,PRIMARY,https://developers.openai.com/api/docs/pricing,Over 272K: $2 / $7.50.
OpenAI,GPT-6.2 Astra (gpt-6.2-astra),2026-11-17,8.00,40.00,0.40,,PRIMARY,https://developers.openai.com/api/docs/pricing,Over 272K: $16 / $60. Changelog entry is dated Nov 17.
OpenAI,GPT-6.2 Sol (gpt-6.2-sol),2026-11-17,2.00,10.00,0.10,,PRIMARY,https://developers.openai.com/api/docs/pricing,Over 272K: $4 / $15.
Anthropic,Claude 3 Opus,2024-03-04*,15.00,75.00,1.50,,ARCHIVE,https://web.archive.org/web/20250528184604/https://docs.anthropic.com/en/docs/about-claude/pricing,Snapshot dated 2025-05-28. Model is retired and absent from the current page.
Anthropic,Claude 3.5 Sonnet,2024-06-20*,3.00,15.00,0.30,,ARCHIVE,https://web.archive.org/web/20250528184604/https://docs.anthropic.com/en/docs/about-claude/pricing,Snapshot dated 2025-05-28.
Anthropic,Claude 3.7 Sonnet,2025-02-24*,3.00,15.00,0.30,,ARCHIVE,https://web.archive.org/web/20250528184604/https://docs.anthropic.com/en/docs/about-claude/pricing,Snapshot dated 2025-05-28.
Anthropic,Claude Opus 4,2025-05-22*,15.00,75.00,1.50,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,Listed as retired on the current page.
Anthropic,Claude Opus 4.1,2025-08-05,15.00,75.00,1.50,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,Listed as retired. Date from the model ID suffix 20250805.
Anthropic,Claude Sonnet 4.5,2025-09-29,3.00,15.00,0.30,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,Deprecated 2026-09-30. Date from the model ID suffix 20250929.
Anthropic,Claude Opus 4.5,2025-11-24,5.00,25.00,0.50,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,A two-thirds cut from Opus 4.1 at the same tier.
Anthropic,Claude Opus 4.6,2026-02-05,5.00,25.00,0.50,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,1M context at standard pricing since 2026-03-13.
Anthropic,Claude Sonnet 4.6,2026-02-17,3.00,15.00,0.30,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,
Anthropic,Claude Opus 4.7,2026-04-16,5.00,25.00,0.50,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,Pricing page: models from 4.7 on use a tokenizer producing roughly 30% more tokens for the same text.
Anthropic,Claude Opus 4.8,2026-05-28,5.00,25.00,0.50,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,
Anthropic,Claude Fable 5,2026-06-09,10.00,50.00,1.00,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,
Anthropic,Claude Sonnet 5,2026-06-30,2.00,10.00,0.20,2026-08-10,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,Launched at introductory $2 / $10; on 2026-08-10 it became the standard price and the scheduled rise to $3 / $15 was cancelled.
Anthropic,Claude Opus 5,2026-07-24,5.00,25.00,0.50,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,
Anthropic,Claude Fable 5.1,2026-09-01,10.00,50.00,0.25,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,Cache reads at 0.025x input.
Anthropic,Claude Opus 5.5,2026-09-22,4.00,20.00,0.20,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,Cache reads at 0.05x input.
Anthropic,Claude Sonnet 5.5,2026-09-28,2.00,10.00,0.10,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,Cache read cut from $0.20 to $0.10 on 2026-10-07; base prices unchanged.
Anthropic,Claude Haiku 5.5,2026-10-07,0.10,0.50,0.01,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,Prompts over 100K tokens: $0.50 / $2.50 with $0.05 cache read.
Anthropic,Claude Fable 5.2,2026-11-09,8.00,40.00,0.20,,PRIMARY,https://platform.claude.com/docs/en/about-claude/pricing,Fast mode $16 / $80.
Google,Gemini 1.5 Pro,2024-05*,3.50,10.50,0.875,,ARCHIVE,https://web.archive.org/web/20240701171821/https://ai.google.dev/pricing,Snapshot dated 2024-07-01. Prompts over 128K: $7.00 / $21.00. Later price cuts not traced.
Google,Gemini 2.5 Pro,2025-06-17*,1.25,10.00,0.125,,PRIMARY,https://aistudio.google.com/docs/pricing,Over 200K: $2.50 / $15.00. Deprecated; requests route to gemini-3.8-flash on 2026-12-01.
Google,Gemini 3 Pro Preview,2025-11-18,2.00,12.00,0.20,,ARCHIVE,https://web.archive.org/web/20251210221523/https://ai.google.dev/gemini-api/docs/pricing,Snapshot dated 2025-12-10. Over 200K: $4.00 / $18.00. Shut down 2026-03-09.
Google,Gemini 3.1 Pro Preview,2026-02-19,2.00,12.00,0.20,,PRIMARY,https://aistudio.google.com/docs/pricing,Over 200K: $4.00 / $18.00.
Google,Gemini 3.5 Flash,,1.50,9.00,0.15,,ARCHIVE,https://web.archive.org/web/20260906110741/https://ai.google.dev/gemini-api/docs/pricing,Same price in the 2026-06-11 snapshot. Deprecated 2026-10-08 and routed to 3.6 Flash. Release date not captured.
Google,Gemini 3.6 Flash,2026-07-21,0.75,3.75,0.075,,PRIMARY,https://aistudio.google.com/docs/pricing,Scheduled to double to $1.50 / $7.50 on 2027-01-01.
Google,Gemini 3.7 Flash,2026-08-13,0.75,3.75,0.075,,ARCHIVE,https://web.archive.org/web/20260906110741/https://ai.google.dev/gemini-api/docs/pricing,Snapshot dated 2026-09-06. Deprecated 2026-10-08 and routed to 3.8 Flash.
Google,Gemini 3.8 Flash,2026-09-02,0.75,3.75,0.075,,PRIMARY,https://aistudio.google.com/docs/pricing,Scheduled to double to $1.50 / $7.50 on 2027-01-01.
Google,Gemini 4 Argon,2026-10-13,2.00,10.00,0.10,,PRIMARY,https://aistudio.google.com/docs/pricing,Price through 2026-11-30; $4.00 / $20.00 from 2026-12-01.
Google,Gemini 4 Carbon,2026-11-10,2.00,10.00,0.10,,PRIMARY,https://aistudio.google.com/docs/pricing,Introductory price through 2026-11-30; $4.00 / $20.00 with $0.20 caching from 2026-12-01.
Google,Gemini 4 Hydrogen,2026-11-12,1.50,7.50,0.075,,PRIMARY,https://aistudio.google.com/docs/pricing,Single rate across the 1M window.
Google,Gemini 4 Neon,2026-11-18,3.00,15.00,0.15,,PRIMARY,https://aistudio.google.com/docs/pricing,Single rate across the 1M window.
xAI,Grok 3 (grok-3),2025-04*,3.00,15.00,0.75,,ARCHIVE,https://web.archive.org/web/20250801003158/https://docs.x.ai/docs/models,Snapshot dated 2025-08-01.
xAI,Grok 4 (grok-4-0709),2025-07-09*,3.00,15.00,0.75,,ARCHIVE,https://web.archive.org/web/20250801003158/https://docs.x.ai/docs/models,Prompts over 128K: $6.00 / $30.00.
xAI,Grok 4.20 (launch price),2026-03-10,2.00,6.00,0.20,,ARCHIVE,https://web.archive.org/web/20260402074148/https://docs.x.ai/developers/models,Snapshot dated 2026-04-02.
xAI,Grok 4.20 (current price),2026-03-10,1.25,2.50,0.20,,PRIMARY,https://docs.x.ai/docs/models,Date of the cut not found. From 200K prompt tokens: $2.50 / $5.00 on the whole request.
xAI,Grok 4.5,2026-07-08,2.00,6.00,0.30,,PRIMARY,https://docs.x.ai/docs/models,From 200K prompt tokens: $4.00 / $12.00.
xAI,Grok 4.6,2026-08-12,2.00,6.00,0.50,,PRIMARY,https://docs.x.ai/docs/models,From 200K prompt tokens: $4.00 / $12.00.
xAI,Grok 4.7,2026-09-21,2.00,6.00,0.50,,PRIMARY,https://docs.x.ai/docs/models,From 200K prompt tokens: $4.00 / $12.00. A second price set of $2.20 / $6.60 in the page data appears to be a regional endpoint.
Meta,Muse Spark 1.1 / 1.2 / 1.3,,1.25,4.25,0.15,,PRIMARY,https://dev.meta.ai/products/meta-model-api,Contributor variants (data used for training) cost $0.10 / $0.20. Release dates not captured.
Meta,Muse Wonder (muse-wonder-1.0),,4.00,20.00,0.20,,PRIMARY,https://dev.meta.ai/products/meta-model-api,1M context. Release date not captured.
Meta,Muse Wonder Full,UNVERIFIABLE,UNVERIFIABLE,UNVERIFIABLE,UNVERIFIABLE,,UNVERIFIABLE,https://dev.meta.ai/products/meta-model-api,No API price: the page lists dashes and says it is available by subscription in Muse Code.
DeepSeek,DeepSeek-V3 (deepseek-chat),2024-12-26*,0.27,1.10,0.07,2025-02-08,ARCHIVE,https://web.archive.org/web/20250401093024/https://api-docs.deepseek.com/quick_start/pricing,Snapshot dated 2025-04-01. Launch promotion of $0.14 / $0.28 ran until 2025-02-08 (snapshot 2025-01-03). Off-peak 50% discount at 16:30-00:30 UTC.
DeepSeek,DeepSeek-R1 (deepseek-reasoner),2025-01-20*,0.55,2.19,0.14,,ARCHIVE,https://web.archive.org/web/20250401093024/https://api-docs.deepseek.com/quick_start/pricing,Snapshot dated 2025-04-01. Off-peak 75% discount at 16:30-00:30 UTC.
DeepSeek,DeepSeek-V4-Flash (preview price),2026-04-24,0.14,0.28,0.0028,2026-04-26,ARCHIVE,https://web.archive.org/web/20260501050639/https://api-docs.deepseek.com/quick_start/pricing,Snapshot dated 2026-05-01. Cache-hit price cut to a tenth of launch on 2026-04-26.
DeepSeek,DeepSeek-V4-Pro (preview list price),2026-04-24,1.74,3.48,0.0145,,ARCHIVE,https://web.archive.org/web/20260501050639/https://api-docs.deepseek.com/quick_start/pricing,Sold at a 75% discount ($0.435 / $0.87); the 2026-08-01 snapshot shows only the discounted figures.
DeepSeek,"DeepSeek-V4-Flash (after rise, peak)",2026-04-24,0.44,1.32,0.014,2026-08-16,ARCHIVE,https://web.archive.org/web/2026id_/https://api-docs.deepseek.com/news/news260813.md,"From the price table image in the provider's 2026-08-13 news post, read via archive. Off-peak is half: $0.22 / $0.66. Peak hours 01:00-04:00 and 06:00-10:00 UTC."
DeepSeek,"DeepSeek-V4-Pro (GA, peak)",2026-08-13,1.32,3.96,0.044,2026-08-16,ARCHIVE,https://web.archive.org/web/20261118170941/https://api-docs.deepseek.com/quick_start/pricing/,Still current in the 2026-11-18 snapshot. Off-peak is half: $0.66 / $1.98.
DeepSeek,"DeepSeek-V4.1-Flash (1017, peak)",2026-09-10,0.30,1.20,0.006,,ARCHIVE,https://web.archive.org/web/20261118170941/https://api-docs.deepseek.com/quick_start/pricing/,Snapshot dated 2026-11-18; the live page reset the connection. Off-peak is half: $0.15 / $0.60. Peak is weekdays only. Price at the 2026-09-10 launch not checked.
Moonshot,Kimi K2 (kimi-k2-0711-preview),2025-07-11*,0.60,2.50,0.15,,ARCHIVE,https://web.archive.org/web/20260515072943id_/https://platform.kimi.ai/docs/pricing/chat-k2.md,Snapshot dated 2026-05-15.
Moonshot,Kimi K2.5,,0.60,3.00,0.10,,ARCHIVE,https://web.archive.org/web/20260515072717id_/https://platform.kimi.ai/docs/pricing/chat-k25.md,Snapshot dated 2026-05-15. Release date not captured.
Moonshot,Kimi K2.6,,0.95,4.00,0.16,,PRIMARY,https://platform.moonshot.ai/docs/pricing/chat,K2 series closed to new users from 2026-10-31. Release date not captured.
Moonshot,Kimi K3,,3.00,15.00,0.30,,PRIMARY,https://platform.moonshot.ai/docs/pricing/chat,Listed by 2026-08-09 (archive). 1M context. Release date not captured.
Moonshot,Kimi K3.1 Pro,,2.00,10.00,0.20,,PRIMARY,https://platform.moonshot.ai/docs/pricing/chat,Highspeed variant $4 / $20. Release date not captured.
Z.ai,GLM-5,2026-02-12,1.00,3.20,0.20,,PRIMARY,https://docs.z.ai/guides/overview/pricing,Dates from the Z.ai release notes.
Z.ai,GLM-5.1,2026-04-07,1.40,4.40,0.26,,PRIMARY,https://docs.z.ai/guides/overview/pricing,
Z.ai,GLM-5.2,2026-06-16,1.40,4.40,0.26,,PRIMARY,https://docs.z.ai/guides/overview/pricing,
Z.ai,GLM-5.3,2026-08-18,1.40,4.40,0.26,,PRIMARY,https://docs.z.ai/guides/overview/pricing,
Alibaba,Qwen3.6-Max (qwen3.6-max-preview),,1.30,7.80,,,ARCHIVE,https://web.archive.org/web/20260718154131/https://www.alibabacloud.com/help/en/model-studio/model-pricing,Snapshot dated 2026-07-18; international deployment. 128K-256K prompts: $2 / $12. Absent from the current page.
Alibaba,Qwen3.8-Max,2026-09-02,2.00,6.00,,,PRIMARY,https://www.alibabacloud.com/help/en/model-studio/model-pricing,International (Singapore) USD price. Date inferred from the snapshot name qwen3.8-max-0902. Cache discount offered but rate not captured.
Alibaba,Qwen4-Max,,1.50,4.50,,,PRIMARY,https://www.alibabacloud.com/help/en/model-studio/model-pricing,International (Singapore) USD price as published; no CNY conversion. Release date not captured.
Microsoft,MAI-Thinking-1 (Global),,2.00,8.00,0.20,2026-08-01,PRIMARY,"https://prices.azure.com/api/retail/prices (filter: contains(meterName,'MAI'), armRegionName eq 'eastus2')","Azure Retail Prices API meter, effective date as reported by the API."
Microsoft,MAI-Cyber-1-Flash (Global),,0.60,3.50,0.06,2026-08-01,PRIMARY,"https://prices.azure.com/api/retail/prices (filter: contains(meterName,'MAI'), armRegionName eq 'eastus2')",Azure Retail Prices API.
Microsoft,MAI-Code-2-Flash (Global),,0.05,0.25,0.005,2026-11-01,PRIMARY,"https://prices.azure.com/api/retail/prices (filter: contains(meterName,'MAI'), armRegionName eq 'eastus2')",Azure Retail Prices API.
```

## Artificial Analysis: cost to run the Intelligence Index

Source: embedded page data on https://artificialanalysis.ai/models and https://artificialanalysis.ai/leaderboards/models, read 19 November 2026. Verdict: PRIMARY (operator's own pages). Index version: **Artificial Analysis Intelligence Index v5.0.1**, nine evaluations (AA-Briefcase v1.1, AutomationBench-AA, Terminal-Bench 4.0, FrontierCode-AA 2.0, AA-Omniscience v1.1, GDP.pdf, HLE-Diamond, CritPt v2 Hard Subset, Terminal-Bench-Science 0.1).

Caveats:

- "Cost to run" is the `intelligenceIndexCost.total` field: total USD to run the whole index, including cache reads and writes. The models page charts one configuration per model family (27 entries), so the table below is that set and not a strict top 25 by score. One zero-priced open-weights entry (K2 Horizon) is omitted.
- Values were paired with model names by position in the embedded JSON. The leading rows cross-check against the leaderboard page; treat lower rows as needing a spot check before publication.
- Blended price: AA publishes several blends. "3:1" is three parts input to one part output with no caching. "7:2:1" is seven parts cache-hit, two parts input, one part output.
- AA prices Gemini 4 Carbon at $4 / $20, the post-1-December rate, although Google's page charges $2 / $10 until 30 November.
- "Cost per task" is AA's weighted average USD per index task, from the leaderboard page. Blank means not captured for that configuration.

| Model (configuration) | Index score | Cost to run index (USD) | Cost per task (USD) | Input $/MTok | Output $/MTok | Blended 3:1 | Blended 7:2:1 |
|---|---|---|---|---|---|---|---|
| Claude Fable 5.2 (max) | 64.6 | 22,191.42 | 26.54 | 8 | 40 | 16.0 | 5.74 |
| GPT-6.2 Astra (max) | 62.1 | 4,530.46 | 4.0 | 8 | 40 | 16.0 | 5.88 |
| Gemini 4 Neon (xhigh) | 61.4 | 7,787.91 | 6.44 | 3 | 15 | 6.0 | 2.205 |
| Gemini 4 Carbon (high) | 60.0 | 8,239.69 | 7.76 | 4 | 20 | 8.0 | 2.94 |
| Claude Opus 5.5 (max) | 59.1 | 8,909.67 | 10.04 | 4 | 20 | 8.0 | 2.94 |
| GPT-6.2 Sol (max) | 57.3 | 1,108.28 | 1.01 | 2 | 10 | 4.0 | 1.47 |
| Claude Sonnet 5.5 (max) | 54.5 | 7,980.63 | 10.02 | 2 | 10 | 4.0 | 1.47 |
| Gemini 4 Hydrogen (xhigh) | 53.9 | 4,085.72 | 3.16 | 1.5 | 7.5 | 3.0 | 1.1025 |
| GPT-6.1 Terra (max) | 51.3 | 972.34 | 0.96 | 1 | 5 | 2.0 | 0.735 |
| Kimi K3.1 Pro | 46.5 | 3,152.80 | 3.68 | 2 | 10 | 4.0 | 1.54 |
| Muse Wonder (max) | 43.6 | 5,414.45 | n/a | 4 | 20 | 8.0 | 2.94 |
| Qwen4 Max | 42.9 | 2,394.31 | n/a | 1.5 | 4.5 | 2.25 | 0.8025 |
| Claude Haiku 5.5 (max) | 36.5 | 339.47 | n/a | 0.1 | 0.5 | 0.2 | 0.077 |
| Muse Ember (max) | 36.0 | 117.12 | n/a | 0.1 | 0.5 | 0.2 | 0.0728 |
| Grok 4.7 (xhigh) | 35.5 | 5,905.50 | n/a | 2 | 6 | 3.0 | 1.35 |
| Tencent Hy4 | 34.6 | 1,021.46 | n/a | 0.834 | 2.501 | 1.2508 | 0.4463 |
| DeepSeek V4.1 Flash 1017 (max) | 32.6 | 520.63 | n/a | 0.3 | 1.2 | 0.525 | 0.1842 |
| GLM-5.3 (max) | 31.7 | 3,495.62 | n/a | 1.4 | 4.4 | 2.15 | 0.902 |
| Inkling 2 Small | 30.6 | 791.81 | n/a | 0.3 | 1 | 0.475 | 0.181 |
| MiMo-V2.6-Pro | 29.9 | 220.73 | n/a | 0.435 | 0.87 | 0.5438 | 0.1765 |
| Ling 3.1 Flash 1019 | 29.6 | 2,009.23 | n/a | 0.3 | 0.9 | 0.45 | 0.192 |
| GPT-6 Luna (max) | 27.9 | 136.06 | n/a | 0.1 | 0.5 | 0.2 | 0.077 |
| Mistral Large 4 (high) | 26.1 | 1,359.61 | n/a | 0.7 | 2.1 | 1.05 | 0.399 |
| Qwen3.8 27B (xhigh) | 20.1 | 2,390.04 | n/a | 0.5 | 3 | 1.125 | 0.47 |
| Beam 1.0 | 17.7 | 249.83 | n/a | 0.4 | 1.2 | 0.6 | 0.228 |
| Nemotron 3.5 Super VL | 13.6 | 416.10 | n/a | 0.15 | 0.5 | 0.2375 | 0.115 |

```csv
model,aa_index_version,read_date,index_score,cost_to_run_index_usd,cost_per_task_usd,input_usd_per_mtok,output_usd_per_mtok,blended_3to1_usd_per_mtok,blended_7to2to1_usd_per_mtok,verdict,source_url
Claude Fable 5.2 (max),v5.0.1,2026-11-19,64.6,22191.42,26.54,8,40,16.0,5.74,PRIMARY,https://artificialanalysis.ai/models
GPT-6.2 Astra (max),v5.0.1,2026-11-19,62.1,4530.46,4.0,8,40,16.0,5.88,PRIMARY,https://artificialanalysis.ai/models
Gemini 4 Neon (xhigh),v5.0.1,2026-11-19,61.4,7787.91,6.44,3,15,6.0,2.205,PRIMARY,https://artificialanalysis.ai/models
Gemini 4 Carbon (high),v5.0.1,2026-11-19,60.0,8239.69,7.76,4,20,8.0,2.94,PRIMARY,https://artificialanalysis.ai/models
Claude Opus 5.5 (max),v5.0.1,2026-11-19,59.1,8909.67,10.04,4,20,8.0,2.94,PRIMARY,https://artificialanalysis.ai/models
GPT-6.2 Sol (max),v5.0.1,2026-11-19,57.3,1108.28,1.01,2,10,4.0,1.47,PRIMARY,https://artificialanalysis.ai/models
Claude Sonnet 5.5 (max),v5.0.1,2026-11-19,54.5,7980.63,10.02,2,10,4.0,1.47,PRIMARY,https://artificialanalysis.ai/models
Gemini 4 Hydrogen (xhigh),v5.0.1,2026-11-19,53.9,4085.72,3.16,1.5,7.5,3.0,1.1025,PRIMARY,https://artificialanalysis.ai/models
GPT-6.1 Terra (max),v5.0.1,2026-11-19,51.3,972.34,0.96,1,5,2.0,0.735,PRIMARY,https://artificialanalysis.ai/models
Kimi K3.1 Pro,v5.0.1,2026-11-19,46.5,3152.80,3.68,2,10,4.0,1.54,PRIMARY,https://artificialanalysis.ai/models
Muse Wonder (max),v5.0.1,2026-11-19,43.6,5414.45,,4,20,8.0,2.94,PRIMARY,https://artificialanalysis.ai/models
Qwen4 Max,v5.0.1,2026-11-19,42.9,2394.31,,1.5,4.5,2.25,0.8025,PRIMARY,https://artificialanalysis.ai/models
Claude Haiku 5.5 (max),v5.0.1,2026-11-19,36.5,339.47,,0.1,0.5,0.2,0.077,PRIMARY,https://artificialanalysis.ai/models
Muse Ember (max),v5.0.1,2026-11-19,36.0,117.12,,0.1,0.5,0.2,0.0728,PRIMARY,https://artificialanalysis.ai/models
Grok 4.7 (xhigh),v5.0.1,2026-11-19,35.5,5905.50,,2,6,3.0,1.35,PRIMARY,https://artificialanalysis.ai/models
Tencent Hy4,v5.0.1,2026-11-19,34.6,1021.46,,0.834,2.501,1.2508,0.4463,PRIMARY,https://artificialanalysis.ai/models
DeepSeek V4.1 Flash 1017 (max),v5.0.1,2026-11-19,32.6,520.63,,0.3,1.2,0.525,0.1842,PRIMARY,https://artificialanalysis.ai/models
GLM-5.3 (max),v5.0.1,2026-11-19,31.7,3495.62,,1.4,4.4,2.15,0.902,PRIMARY,https://artificialanalysis.ai/models
Inkling 2 Small,v5.0.1,2026-11-19,30.6,791.81,,0.3,1,0.475,0.181,PRIMARY,https://artificialanalysis.ai/models
MiMo-V2.6-Pro,v5.0.1,2026-11-19,29.9,220.73,,0.435,0.87,0.5438,0.1765,PRIMARY,https://artificialanalysis.ai/models
Ling 3.1 Flash 1019,v5.0.1,2026-11-19,29.6,2009.23,,0.3,0.9,0.45,0.192,PRIMARY,https://artificialanalysis.ai/models
GPT-6 Luna (max),v5.0.1,2026-11-19,27.9,136.06,,0.1,0.5,0.2,0.077,PRIMARY,https://artificialanalysis.ai/models
Mistral Large 4 (high),v5.0.1,2026-11-19,26.1,1359.61,,0.7,2.1,1.05,0.399,PRIMARY,https://artificialanalysis.ai/models
Qwen3.8 27B (xhigh),v5.0.1,2026-11-19,20.1,2390.04,,0.5,3,1.125,0.47,PRIMARY,https://artificialanalysis.ai/models
Beam 1.0,v5.0.1,2026-11-19,17.7,249.83,,0.4,1.2,0.6,0.228,PRIMARY,https://artificialanalysis.ai/models
Nemotron 3.5 Super VL,v5.0.1,2026-11-19,13.6,416.10,,0.15,0.5,0.2375,0.115,PRIMARY,https://artificialanalysis.ai/models
```

### Top 25 configurations by index score, with cost per task

From the leaderboard page. The same model appears at several reasoning-effort settings, which shows how much cost moves with effort at a fixed list price.

| Rank | Model (configuration) | Index score | Cost per task (USD) |
|---|---|---|---|
| 1 | Claude Fable 5.2 (max) | 64.6 | 26.54 |
| 2 | Claude Fable 5.2 (xhigh) | 62.2 | 14.83 |
| 3 | GPT-6.2 Astra (max) | 62.1 | 4.00 |
| 4 | Claude Fable 5.2 (high) | 61.8 | 9.08 |
| 5 | GPT-6.2 Astra (xhigh) | 61.6 | 2.52 |
| 6 | Gemini 4 Neon (xhigh) | 61.4 | 6.44 |
| 7 | GPT-6.2 Astra (high) | 60.1 | 2.07 |
| 8 | Gemini 4 Carbon (high) | 60.0 | 7.76 |
| 9 | Gemini 4 Neon (high) | 59.6 | 3.74 |
| 10 | Claude Opus 5.5 (max) | 59.1 | 10.04 |
| 11 | Gemini 4 Carbon (medium) | 58.3 | 6.59 |
| 12 | Claude Opus 5.5 (xhigh) | 57.4 | 6.05 |
| 13 | GPT-6.2 Sol (max) | 57.3 | 1.01 |
| 14 | GPT-6.2 Astra (medium) | 57.0 | 1.62 |
| 15 | Claude Fable 5.2 (medium) | 56.4 | 3.80 |
| 16 | GPT-6.2 Sol (xhigh) | 55.7 | 0.65 |
| 17 | GPT-6.2 Sol (high) | 54.9 | 0.56 |
| 18 | Gemini 4 Neon (medium) | 54.9 | 1.90 |
| 19 | Claude Sonnet 5.5 (max) | 54.5 | 10.02 |
| 20 | Gemini 4 Carbon (low) | 54.2 | 7.19 |
| 21 | Claude Fable 5.2 (low) | 53.9 | 3.10 |
| 22 | Gemini 4 Hydrogen (xhigh) | 53.9 | 3.16 |
| 23 | GPT-6.2 Sol (medium) | 52.7 | 0.41 |
| 24 | Claude Opus 5.5 (high) | 51.8 | 3.46 |
| 25 | GPT-6.1 Terra (max) | 51.3 | 0.96 |

```csv
rank,model,aa_index_version,read_date,index_score,cost_per_task_usd,verdict,source_url
1,Claude Fable 5.2 (max),v5.0.1,2026-11-19,64.6,26.54,PRIMARY,https://artificialanalysis.ai/leaderboards/models
2,Claude Fable 5.2 (xhigh),v5.0.1,2026-11-19,62.2,14.83,PRIMARY,https://artificialanalysis.ai/leaderboards/models
3,GPT-6.2 Astra (max),v5.0.1,2026-11-19,62.1,4.00,PRIMARY,https://artificialanalysis.ai/leaderboards/models
4,Claude Fable 5.2 (high),v5.0.1,2026-11-19,61.8,9.08,PRIMARY,https://artificialanalysis.ai/leaderboards/models
5,GPT-6.2 Astra (xhigh),v5.0.1,2026-11-19,61.6,2.52,PRIMARY,https://artificialanalysis.ai/leaderboards/models
6,Gemini 4 Neon (xhigh),v5.0.1,2026-11-19,61.4,6.44,PRIMARY,https://artificialanalysis.ai/leaderboards/models
7,GPT-6.2 Astra (high),v5.0.1,2026-11-19,60.1,2.07,PRIMARY,https://artificialanalysis.ai/leaderboards/models
8,Gemini 4 Carbon (high),v5.0.1,2026-11-19,60.0,7.76,PRIMARY,https://artificialanalysis.ai/leaderboards/models
9,Gemini 4 Neon (high),v5.0.1,2026-11-19,59.6,3.74,PRIMARY,https://artificialanalysis.ai/leaderboards/models
10,Claude Opus 5.5 (max),v5.0.1,2026-11-19,59.1,10.04,PRIMARY,https://artificialanalysis.ai/leaderboards/models
11,Gemini 4 Carbon (medium),v5.0.1,2026-11-19,58.3,6.59,PRIMARY,https://artificialanalysis.ai/leaderboards/models
12,Claude Opus 5.5 (xhigh),v5.0.1,2026-11-19,57.4,6.05,PRIMARY,https://artificialanalysis.ai/leaderboards/models
13,GPT-6.2 Sol (max),v5.0.1,2026-11-19,57.3,1.01,PRIMARY,https://artificialanalysis.ai/leaderboards/models
14,GPT-6.2 Astra (medium),v5.0.1,2026-11-19,57.0,1.62,PRIMARY,https://artificialanalysis.ai/leaderboards/models
15,Claude Fable 5.2 (medium),v5.0.1,2026-11-19,56.4,3.80,PRIMARY,https://artificialanalysis.ai/leaderboards/models
16,GPT-6.2 Sol (xhigh),v5.0.1,2026-11-19,55.7,0.65,PRIMARY,https://artificialanalysis.ai/leaderboards/models
17,GPT-6.2 Sol (high),v5.0.1,2026-11-19,54.9,0.56,PRIMARY,https://artificialanalysis.ai/leaderboards/models
18,Gemini 4 Neon (medium),v5.0.1,2026-11-19,54.9,1.90,PRIMARY,https://artificialanalysis.ai/leaderboards/models
19,Claude Sonnet 5.5 (max),v5.0.1,2026-11-19,54.5,10.02,PRIMARY,https://artificialanalysis.ai/leaderboards/models
20,Gemini 4 Carbon (low),v5.0.1,2026-11-19,54.2,7.19,PRIMARY,https://artificialanalysis.ai/leaderboards/models
21,Claude Fable 5.2 (low),v5.0.1,2026-11-19,53.9,3.10,PRIMARY,https://artificialanalysis.ai/leaderboards/models
22,Gemini 4 Hydrogen (xhigh),v5.0.1,2026-11-19,53.9,3.16,PRIMARY,https://artificialanalysis.ai/leaderboards/models
23,GPT-6.2 Sol (medium),v5.0.1,2026-11-19,52.7,0.41,PRIMARY,https://artificialanalysis.ai/leaderboards/models
24,Claude Opus 5.5 (high),v5.0.1,2026-11-19,51.8,3.46,PRIMARY,https://artificialanalysis.ai/leaderboards/models
25,GPT-6.1 Terra (max),v5.0.1,2026-11-19,51.3,0.96,PRIMARY,https://artificialanalysis.ai/leaderboards/models
```
