# Cost & Benchmarks

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/cost-and-benchmarks.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](cost-and-benchmarks.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

The [heat ranking](../README.md#recent-heat-ranking) tracks popularity and the [capability matrix](../capabilities/matrix.md) tracks shape. This page tracks the two things neither of those shows: **how capable a coding agent actually is, and what it costs to run.**

By mid-2026 these two questions merged into one. When the model layer moved to tiers and metered credits — Anthropic's Fable 5 on credits, OpenAI's GPT-5.6 in three price bands — "which model, at which tier, for this task" became the core selection decision. See the [Market Pulse](../README.md#market-pulse) and [market-events](../market-events.md) for the timeline.

## Cost Has Two Layers

1. **The model you burn** — the tokens the agent sends to a frontier model. This is where capability and per-token price live, and for most serious coding agents it dominates the bill.
2. **How the agent charges for wrapping it** — open-source (you pay only the model), bundled subscription, metered credits, or a managed seat. This is what you actually sign up for.

## Layer 1 — Frontier Coding Models: Capability vs Price

The **Artificial Analysis Coding Agent Index** is the cross-model capability number this map tracks. Prices are per **1M tokens (input / output)**.

| Model | AA Coding Agent Index | Other benchmark | Price (in / out per 1M) | Notes |
| --- | :-: | --- | --- | --- |
| **GPT-5.6 Sol** (OpenAI) | **80** | — | $5 / $30 | Current index leader; also has a multi-agent "Ultra" setting |
| **GPT-5.6 Terra** (OpenAI) | — | — | $2.5 / $15 | Mid tier of the July 9 GPT-5.6 launch |
| **GPT-5.6 Luna** (OpenAI) | — | — | $1 / $6 | Budget tier of GPT-5.6 |
| **Claude Fable 5** (Anthropic) | **77.2** | — | $10 / $50 | Mythos-class; runs on metered credits, not bundled in subscriptions |
| **GPT-5.5** (OpenAI) | **76.4** | SWE-Bench Pro 58.6% | — (≈2× GPT-5.4) | Spring 2026 reference model |
| **Claude Opus 4.8** (Anthropic) | **72.5** | — | $5 / $25 | Half of Fable 5 on both sides (per the [Fable 5 profile](../agents/claude-fable-5.md)); the dependable default inside Claude Code |

> Reference point for SWE-Bench Pro: Claude Opus 4.7 scored 64.3%, ahead of GPT-5.5's 58.6%. A dash (—) means the figure is not tracked in this map, not that it is zero. Numbers are as of **July 2026** and sourced from the vendor profiles ([Claude Fable 5](../agents/claude-fable-5.md), [GPT-5.5](../agents/gpt-5.5.md)); prices and index positions move — always confirm against the vendor before budgeting.

The takeaways that survive week to week:

- **The index spread is real but not enormous** — roughly 72–80 across the current frontier. The *price* spread is far larger (Luna at $1/$6 vs Fable 5 at $10/$50 output is a ~8× gap on output tokens). For most coding work the cheaper tier is the rational default; reach for the top of the index only when a task genuinely needs it.
- **Tiering is now the lever.** GPT-5.6's Sol/Terra/Luna and Claude's Fable 5-vs-Opus-4.8 split mean the same agent can cost very differently depending on which model you point it at. This is a per-task decision, not a one-time setup.

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
