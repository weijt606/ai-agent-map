# Cost & Benchmarks

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/cost-and-benchmarks.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](cost-and-benchmarks.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

The [heat ranking](../README.md#recent-heat-ranking) tracks popularity and the [capability matrix](../capabilities/matrix.md) tracks shape. This page tracks the two things neither of those shows: **how capable a coding agent actually is, and what it costs to run.**

By mid-2026 these two questions merged into one. When the model layer moved to tiers and metered credits — Anthropic's Fable line on credits, OpenAI's GPT-5.6 in three price bands — "which model, at which tier, for this task" became the core selection decision. Both ceilings then moved again in the first days of September 2026 ([Fable 5.1](../agents/claude-fable-5.md) on the 1st, [GPT-6 Astra](../agents/gpt-6-astra.md) on the 3rd), and landed on the same headline price. See the [Market Pulse](../README.md#market-pulse) and [market-events](../market-events.md) for the timeline.

## Cost Has Two Layers

1. **The model you burn** — the tokens the agent sends to a frontier model. This is where capability and per-token price live, and for most serious coding agents it dominates the bill.
2. **How the agent charges for wrapping it** — open-source (you pay only the model), bundled subscription, metered credits, or a managed seat. This is what you actually sign up for.

## Layer 1 — Frontier Coding Models: Capability vs Price

The **Artificial Analysis Coding Agent Index** is the cross-model capability number this map tracks. Prices are per **1M tokens (input / output)**, taken from the vendors' own pricing pages.

| Model | AA Coding Agent Index | Other benchmark | Price (in / out per 1M) | Cache read | Notes |
| --- | :-: | --- | --- | :-: | --- |
| **GPT-6 Astra** (OpenAI) | — | DeepSWE v1.1 74.1% | **$10 / $50** | $1 | Current OpenAI ceiling, **Sept 3 2026**. Repricing to **$20 / $75 past 272k input tokens**; Fast mode 2×; the generally available version **refuses part of its cybersecurity capability** |
| **Claude Fable 5.1** (Anthropic) | — | **SWE-bench Pro 81.2** | **$10 / $50** | **$0.25** | Current Anthropic ceiling, **Sept 1 2026**. Same sticker as Fable 5; cache reads cut 75%. 1M context billed at standard rates across the whole window. Metered credits, not bundled |
| **GPT-5.6 Sol** (OpenAI) | **80** | — | **$4 / $20** (promotional) | — | Index leader as last measured. Cut from $5 / $30 on **Aug 21 2026** for three months — through at least **Nov 21 2026**. Long-context band $8 / $30 |
| **Claude Fable 5** (Anthropic) | **77.2** | — | $10 / $50 | $1 | Superseded by 5.1 on Sept 1; kept as the index reference point |
| **GPT-5.5** (OpenAI) | **76.4** | SWE-Bench Pro 58.6% | — (≈2× GPT-5.4) | — | Spring 2026 reference model, two generations back |
| **Claude Opus 5** (Anthropic) | — | SWE-bench Pro just under Fable 5.1's 81.2 | $5 / $25 | $0.50 | **The default you actually run** — half of Fable on both sides, 1M context as default and maximum. Fast mode $10 / $50 |
| **Claude Opus 4.8** (Anthropic) | **72.5** | — | $5 / $25 | $0.50 | Superseded by Opus 5 on July 24; still the automatic fallback when a request trips the safety classifier |
| **Claude Sonnet 5** (Anthropic) | — | — | **$2 / $10** | $0.20 | The volume tier; the introductory price was made permanent and the scheduled Sept 1 rise to $3 / $15 was cancelled |
| **GPT-5.6 Terra** (OpenAI) | — | — | $2 / $12 | — | Mid tier. Listed at $2.5 / $15 at the July 9 launch; the first-party pricing page now shows $2 / $12 |
| **GPT-5.6 Luna** (OpenAI) | — | — | $0.20 / $1.20 | — | Budget tier. Listed at $1 / $6 at launch; now $0.20 / $1.20 first-party |
| **Muse Spark 1.2** (Meta) — Standard | — | — | $1.25 / $4.25 | $0.15 | Coding-focused model behind Muse Code, which left beta **Aug 31 2026**. 3,000 req/min and 4M tokens/min. No index figure this map will copy is published |
| **Muse Spark 1.2** (Meta) — Contributor | — | — | **$0.10 / $0.20** | $0.002 | The same model at ~12× / ~21× off, **in exchange for permission to train future Meta models on your prompts and completions**. Capped at 60 req/min. Read this as a governance decision, not a budget one |

> Reference point for SWE-Bench Pro: Claude Opus 4.7 scored 64.3%, ahead of GPT-5.5's 58.6%. A dash (—) means the figure is not tracked in this map, not that it is zero — **the index has not published a figure this map will copy for Astra, Fable 5.1, or Opus 5**, and the map does not fill that gap with third-party leaderboard numbers. Prices are as of **September 6 2026** from [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) and [developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing); benchmark figures come from the vendor profiles ([Fable 5.1](../agents/claude-fable-5.md), [Opus 5](../agents/claude-opus-5.md), [GPT-6 Astra](../agents/gpt-6-astra.md), [GPT-5.5](../agents/gpt-5.5.md)) and [market-events](../market-events.md). Prices and index positions move — confirm against the vendor before budgeting.

The takeaways that survive week to week:

- **The two ceilings now carry the same sticker.** GPT-6 Astra and Claude Fable 5.1 are both $10 / $50. That is the first time this map has recorded the frontier tiers of both vendors landing on an identical headline price, and it moves the comparison off the sticker entirely — onto **cache reads** ($0.25 vs $1, a 4× gap) and onto **long-context pricing shape**.
- **Long context is priced differently by the two vendors, and that is now a design constraint.** Anthropic bills its 1M window at standard rates across the window. OpenAI reprices the whole request past **272k input tokens** — $20 / $75 instead of $10 / $50. An agent that accumulates context across a long session can cross that threshold without anyone deciding to; on the Claude side there is no threshold to cross.
- **Where the bill actually accumulates is cache, not input.** A long-running agent replays a large prompt every turn. At $0.25/M against $1/M, Fable 5.1's cache read is where its ~25% typical / up to 45% agentic cost reduction comes from — with no change to the per-token sticker. If you are comparing frontier models on the headline number alone you are comparing the wrong column.
- **Tiering is still the lever, and both ladders got deeper.** GPT-5.6's Sol/Terra/Luna sit under Astra; Opus 5 and Sonnet 5 sit under Fable 5.1. The price spread inside a single vendor is now larger than the spread between vendors — Sonnet 5 at $2/$10 against Fable 5.1 at $10/$50 is 5× on both sides. For most coding work the cheaper tier is the rational default; reach for the ceiling only when a task genuinely needs it.
- **The cheapest output on this table is not paid in money.** Muse Spark 1.2's Contributor rate ($0.20 output) is **250× below the two frontier ceilings**, and the difference is settled in training rights over your prompts and completions. For an agent workload that is a large discount on the side of the bill that dominates — and a disclosure decision an individual developer can make silently on a machine with the company repo checked out. It also does not compose: the 60 req/min cap is a real constraint on the parallel subagent workflows the same release advertises. Treat the Standard rate ($1.25 / $4.25) as the comparable number. Note also that Muse Code ships with **no public repository**, so it is not tracked on this map's boards.
- **Frontier price is partly promotional, which makes this table a live document.** Sol's August cut runs to at least **Nov 21 2026** and takes it below Opus 5 on output ($20 vs $25). Any model choice sized against a promotional rate needs a **November review**. See [market-events](../market-events.md).

## Layer 2 — How Coding Agents Bill

The wrapper's billing model decides who you pay and how predictable the bill is.

| Agent | Billing model | You pay | Predictability |
| --- | --- | --- | --- |
| [Claude Code](../agents/claude-code.md) | Subscription (Pro/Max) + **metered credits** for Fable 5 | Anthropic | Medium — Opus 4.8 is bundled; Fable 5 usage is variable |
| [Codex](../agents/codex.md) | Bundled in ChatGPT plans (Free → Pro); API for heavy CLI use | OpenAI | Medium — plan-bundled, with API overflow |
| [Cursor](../agents/cursor.md) | Subscription / seat (Teams pricing) | Cursor | High — flat seat, model usage inside limits |
| [GitHub Copilot](../agents/github-copilot.md) | Subscription / seat | GitHub | High — flat seat |
| [Devin](../agents/devin.md) | Managed seat + usage | Cognition | Low–Medium — managed execution adds usage cost |
| [Aider](../agents/aider.md), [Cline](../agents/cline.md), [Continue](../agents/continue.md) | **Open source, bring your own key** | The model provider directly | Low — you see raw token cost, no markup |
| [Pi](../agents/pi.md), [jcode](../agents/jcode.md), [OpenHands](../agents/openhands.md) | **Open source harness, BYO provider** | The model provider directly | Low — you own the loop and the bill |
| [Kimi Code](../agents/kimi-code.md), [MiMoCode](../agents/mimocode.md), [CodeWhale](../agents/codewhale.md) | Open source, vendor / low-cost models | Moonshot / Xiaomi / DeepSeek APIs | Low — Chinese-stack models keep per-token cost down |
| Muse Code (Meta) — *not tracked on this map; no public repository* | Subscription **$5–$50/month** (three plans, from Aug 31 2026) + API tokens | Meta | Medium — plan-bundled, with the Contributor rate available only if you grant training rights |

## Three Cost Patterns

- **"Free" agent, you pay the model.** Aider, Cline, Pi, jcode, OpenHands and the harnesses cost nothing to install — the entire bill is the model API you point them at. Cheapest and most transparent, but you own rate limits, keys, and overspend risk.
- **Bundled subscription.** Claude Code, Codex, Cursor, and Copilot fold model usage into a flat plan (with overflow to metered/API for heavy use). Most predictable for steady individual use; the ceiling is the plan's fair-use limits.
- **Metered credits / managed usage.** Fable 5 credits inside Claude Code, and managed products like Devin, bill by actual work done. This is where a single hard task can get expensive fast — and where picking the right *tier* (Layer 1) matters most.

There is also an **operational cost** the token bill hides: RAM, boot time, and the ops burden of self-hosting. Performance-first harnesses make this explicit — [jcode](../agents/jcode.md), for instance, advertises the lowest RAM and fastest boot in its class specifically so many parallel sessions stay cheap to run. Each profile's "Operating Cost" section covers this per project.

## How To Choose

1. **Estimate your dominant cost first.** Heavy daily coding on frontier models? Layer 1 (the model) dominates — optimize the tier. Light or bursty use? A bundled subscription is usually cheaper and simpler.
2. **Match the billing model to your predictability needs.** Teams that need a fixed line item want seat-based (Cursor, Copilot); builders who want transparency and no markup want an open-source agent on their own key.
3. **Only pay for index you'll use.** The capability spread across the frontier is modest; the price spread is large. Default to a cheaper tier and escalate per task, rather than running everything on the most expensive model.

For capability shape by dimension, see the [capability matrix](../capabilities/matrix.md); for the model-layer timeline, see [market-events](../market-events.md).
