# Benchmarks & Billing Models

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/benchmarks-and-billing.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](benchmarks-and-billing.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

The [heat ranking](../README.md#recent-heat-ranking) tracks popularity and the [capability matrix](../capabilities/matrix.md) tracks shape. This page tracks what neither of those shows: **how capable the models behind coding agents are, and how each agent bills.**

This map does not list or compare prices. They change often and each vendor's own pricing page is the source to check.

For the model timeline, see the [Market Pulse](../README.md#market-pulse) and [market-events](../market-events.md).

## Frontier Coding Models

The **Artificial Analysis Coding Agent Index** is the cross-model capability number this map tracks.

| Model | AA Coding Agent Index | Other benchmark | Notes |
| --- | :-: | --- | --- |
| **GPT-6 Astra** (OpenAI) | — | DeepSWE v1.1 74.1% | **Sept 3 2026.** The generally available version **refuses part of its cybersecurity capability** |
| **Claude Opus 5.5** (Anthropic) | — | **Terminal-Bench 4.0 66.4%** | **Sept 22 2026.** Anthropic states it performs at Fable 5.1's level on most work, with 30% faster output than Opus 5. 1M context. Ahead of Opus 5 on all nine published benchmarks; behind [GPT-6 Astra](../agents/gpt-6-astra.md) on AutomationBench (40.0 vs 41.4) and Terminal-Bench-Science (58.7 vs 64.6). Default Opus model in [Claude Code](../agents/claude-code.md) `v2.1.280` the same day |
| **Muse Wonder** (Meta) | — | — | **Oct 12 2026** — recorded here one window late. Meta's new top API model, "frontier coding, long-running agents, and advanced computer use", 1M context. A larger Muse Wonder Full is not on the API at all — only inside the Muse Code Power and Maximum subscription plans |
| **Claude Fable 5.1** (Anthropic) | — | **SWE-bench Pro 81.2** | **Sept 1 2026.** 1M context. Metered credits, not bundled |
| **GPT-6.1 Sol** (OpenAI) | — | — | **Sept 29 2026.** Bundled default in [Codex CLI](../agents/codex.md) `rust-v0.159.1` since the same day, replacing Astra |
| **Claude Sonnet 5.5** (Anthropic) | — | **Terminal-Bench 4.0 70.6%** | **Sept 28 2026.** 30%+ faster than Sonnet 5. Its Terminal-Bench 4.0 figure is **above Opus 5.5's 66.4%**; on every other shared benchmark it trails Opus 5.5. Default Sonnet model in [Claude Code](../agents/claude-code.md) `2.1.284` the same day, 1M context |
| **Gemini 4 Argon** (Google) | — | DeepSWE v1.1 77.9%; AutomationBench 51.3% | **Opened to the paid API Oct 13 2026** (`gemini-4-argon`), announced Sept 30 behind a cyber-defender gate; the no-guardrails build stays with Google's Fairwind Program. Implicit caching only; not on the Free tier; 1M output limit. Google's benchmark table was not run alongside the other vendors' |
| **GPT-6 Sol** (OpenAI) | — | — | **Sept 22 2026.** The GPT-6 mid tier. **Not the same model as GPT-5.6 Sol** — the names collide across generations, which is a real hazard in a config file |
| **GPT-5.6 Sol** (OpenAI) | **80** | — | Index leader as last measured |
| **Claude Fable 5** (Anthropic) | **77.2** | — | Superseded by 5.1 on Sept 1; kept as the index reference point |
| **GPT-5.5** (OpenAI) | **76.4** | SWE-Bench Pro 58.6% | Spring 2026 reference model, two generations back. **Retired from Codex and ChatGPT for ChatGPT sign-in on Oct 14 2026**; the API and API-key Codex sessions are unaffected |
| **Claude Opus 5** (Anthropic) | — | SWE-bench Pro just under Fable 5.1's 81.2 | Claude Code's default Opus until **Opus 5.5** replaced it on Sept 22; still available. 1M context as default and maximum |
| **Claude Opus 4.8** (Anthropic) | **72.5** | — | Superseded by Opus 5 on July 24; still the automatic fallback when a request trips the safety classifier |
| **Claude Sonnet 5** (Anthropic) | — | — | Superseded as Claude Code's default Sonnet by Sonnet 5.5 on Sept 28 |
| **GPT-5.6 Terra** (OpenAI) | — | — | Mid tier, July 9 2026 |
| **GPT-6.1 Terra** (OpenAI) | — | — | **Oct 26 2026.** "Fast, efficient", pitched at visual reasoning and computer use; 1.05M context. In Codex and ChatGPT Work on Plus and above the same day, **not as a default**. OpenAI's launch post was not readable to this map, so no benchmark is recorded |
| **Claude Haiku 5.5** (Anthropic) | — | — | **Oct 7 2026** (`claude-haiku-5-5`). 1M context. Its tokenizer counts ~30% more tokens than Haiku 4.5 for the same text. Default Haiku model on the API; Claude Code `v2.1.293` added it the same day without changing its own defaults |
| **GPT-6 Luna** (OpenAI) | — | — | **Sept 22 2026.** Same naming collision as Sol |
| **GPT-5.6 Luna** (OpenAI) | — | — | Lowest GPT-5.6 tier |
| **Muse Spark 1.3** (Meta) | — | — | Coding-focused model behind Muse Code, which left beta **Aug 31 2026**. No index figure this map will copy is published. The Contributor tier gives Meta **permission to train future models on your prompts and completions**, and is capped at 60 req/min against Standard's 3,000. Read that as a governance decision |

> Reference point for SWE-Bench Pro: Claude Opus 4.7 scored 64.3%, ahead of GPT-5.5's 58.6%. A dash (—) means the figure is not tracked in this map, not that it is zero — **the index has not published a figure this map will copy for Astra, Fable 5.1, or Opus 5**, and the map does not fill that gap with third-party leaderboard numbers. Benchmark figures come from the vendor profiles ([Fable 5.1](../agents/claude-fable-5.md), [Opus 5](../agents/claude-opus-5.md), [GPT-6 Astra](../agents/gpt-6-astra.md), [GPT-5.5](../agents/gpt-5.5.md)) and [market-events](../market-events.md). Index positions move — confirm against the source.

Muse Code ships with **no public repository**, so it is not tracked on this map's boards.

### The Open-Weights Tier

These models are self-hosted, so hardware and licence terms decide whether you can use them.

| Model | Licence | Total / activated params | Context | Vendor-reported headline |
| --- | --- | --- | --- | --- |
| [Kimi K3](../agents/kimi-k3.md) | **Kimi K3 License** (custom) | 2.8T / 16 of 896 experts | 1M | Terminal-Bench 2.1 **88.3**, against GPT-5.6 Sol 88.8 and Fable 5 88.0 |
| [GLM-5.3](../agents/glm-5.md) | **Apache-2.0** | not published per-variant | 1M (solid, from 5.2) | Open-source SOTA on Terminal Bench 3.0; GLM-5.2 at Terminal-Bench 2.1 **81.0**, SWE-bench Pro **62.1** |
| [DeepSeek V4-Pro](../agents/deepseek-v4.md) | **MIT** | 1.6T / 49B | 1M | SWE-bench Verified **80.6**, Terminal-Bench 2.0 67.9 |
| DeepSeek V4-Flash | **MIT** | 284B / 13B | 1M | Reasoning approaching Pro with a larger thinking budget. Point update **V4.1-Flash-1017** (Oct 17 2026): shorter outputs and better benchmarks than V4.1-Flash, per DeepSeek |
| Muse Spark Open (Meta) | **Muse Model License** (custom, "limited commercial terms") | 816B / 42B | 1M | Oct 15 2026. Meta calls it "the most capable US open-weight model to date"; optimized to run through MLX on Mac Studio M5 Ultra |
| [Qwen3-Coder-Next](../agents/qwen3-coder.md) | Varies by checkpoint | 80B / ~3B | 256K → 1M (Yarn) | Comparable to Claude Sonnet among open models on agentic coding |

Four things this tier changes:

1. **The gap at the top is now small enough to argue about.** Moonshot's own comparison puts K3 at 88.3 on Terminal-Bench 2.1 against Sol's 88.8 and Fable 5's 88.0. Treat vendor self-reports as claims — but the claim being *plausible* is itself new.
2. **Licence is the real axis, not capability.** MIT (DeepSeek), Apache-2.0 (GLM), bespoke (Kimi, and since Oct 15 Meta's Muse Model License), and per-checkpoint (Qwen) are four genuinely different legal positions at broadly similar capability. Check the licence before the benchmark.
3. **Parameter count is a deployment class, not a spec-sheet number.** 2.8T and 1.6T are clusters; Qwen3-Coder-Next's ~3B activated of 80B is a workstation. That difference decides more real deployments than any row above it.
4. **There is no like-for-like benchmark row, and this page will not fake one.** DeepSeek quotes SWE-bench Verified, Anthropic quotes SWE-bench Pro, OpenAI quotes DeepSWE, Zhipu quotes an in-house bench. They are different measurements; putting them in one sorted column would be the single most misleading thing this page could do.

## How Coding Agents Bill

| Agent | Billing model | You pay |
| --- | --- | --- |
| [Claude Code](../agents/claude-code.md) | Subscription (Pro/Max) + **metered credits** for Fable 5.1 | Anthropic |
| [Codex](../agents/codex.md) | Bundled in ChatGPT plans (Free → Pro); API for heavy CLI use | OpenAI |
| [Cursor](../agents/cursor.md) | Subscription / seat | Cursor |
| [GitHub Copilot](../agents/github-copilot.md) | Subscription / seat; where Copilot comes with GitHub Enterprise, metered from the first request (Oct 28 2026) | GitHub |
| [Devin](../agents/devin.md) | Managed seat + usage | Cognition |
| [Aider](../agents/aider.md), [Cline](../agents/cline.md), [Continue](../agents/continue.md) | **Open source, bring your own key** | The model provider directly |
| [Pi](../agents/pi.md), [jcode](../agents/jcode.md), [OpenHands](../agents/openhands.md) | **Open source harness, BYO provider** | The model provider directly |
| [Kimi Code](../agents/kimi-code.md), [MiMoCode](../agents/mimocode.md), [CodeWhale](../agents/codewhale.md) | Open source, vendor models | Moonshot / Xiaomi APIs; CodeWhale any provider (DeepSeek default) |
| Muse Code (Meta) — *not tracked on this map; no public repository* | Subscription plans (Everyday, High, Power, Maximum) + API tokens | Meta |

## Three Billing Patterns

- **Open-source agent, you pay the model provider.** Aider, Cline, Pi, jcode, OpenHands and the harnesses install without a licence fee, and you point them at a model API. You own rate limits and keys.
- **Bundled subscription.** Claude Code, Codex, Cursor, and Copilot fold model usage into a plan, with overflow to metered or API use for heavy use. The limit is the plan's fair-use terms.
- **Metered credits / managed usage.** Fable 5.1 credits inside Claude Code, and managed products like Devin, bill by actual work done.

There is also an **operating burden**: RAM, boot time, and the ops work of self-hosting. Performance-first harnesses make this explicit — [jcode](../agents/jcode.md), for instance, advertises the lowest RAM and fastest boot in its class so many parallel sessions can run. Each profile's "Operating Cost" section covers this per project.

For capability shape by dimension, see the [capability matrix](../capabilities/matrix.md); for the model-layer timeline, see [market-events](../market-events.md).
