# Claude Fable 5.1

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/claude-fable-5.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](claude-fable-5.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Claude Fable 5.1 is Anthropic's Mythos-class ceiling as of September 1 2026 — the model you spend credits on rather than the one you run all day.

> This profile covers the Fable line. It keeps its original `claude-fable-5.md` path from the June 2026 entry so existing links stay valid.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anthropic |
| Route | Frontier agentic model (Mythos class) — the ceiling above [Opus 5](claude-opus-5.md) |
| Open source | No |
| Best for | The hardest agentic work: large migrations, multi-agent workflows, deep research, frontier coding |
| Main cost | Metered usage credits in Claude subscriptions since July 7 2026 |
| Official announcement | https://www.anthropic.com/news/claude-fable-5-mythos-5 |

## Why This Entry Exists

Like [GPT-6 Astra](gpt-6-astra.md), this is a model rather than an agent product. It is included because it introduced a new tier (Mythos, above Opus) into the model layer that most agents in this map run on, and because its availability arc directly changed how Claude Code and Claude-based agents are selected.

Fable and **Mythos** share the same underlying model at each version; the difference is safety access. Fable 5.1 is the generally available version. Mythos 5.1 has lighter safeguards and is limited to vetted organizations through Project Glasswing — cyberdefense, infrastructure, and select life-science research.

## When To Pick It

- You want the top Claude tier for agentic work — engineering, research, or analysis. It is not the top Claude score on every benchmark: on Terminal-Bench 4.0, [Opus 5.5](../comparisons/benchmarks-and-billing.md) leads it 66.4% to 55.8% (Anthropic, Sept 22) and Sonnet 5.5 scores 70.6% (Sept 28).
- Your tasks are big enough to justify it. The Fable 5 launch reference case is Stripe reporting a codebase migration "that would have taken a whole team two months by hand" completed in a day.
- You hit false refusals on security-adjacent code. Anthropic reports around 60% fewer cybersecurity false positives for Claude Code users on 5.1.

## When Not To Pick It

- Your workload does not need Mythos-class capability. **Opus 5.5 has been the default under it since Sept 22** (Anthropic says it performs at Fable 5.1's level on most work); [Opus 5](claude-opus-5.md) is still available, and Sonnet 5.5 sits under them.
- You need an open-source or self-hosted model.
- You want a finished agent product, not a model — look at [Claude Code](claude-code.md) instead.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Agentic coding | Very strong | Terminal-Bench 4.0 up from 42.0% (Fable 5) to **55.8%** |
| Software engineering | Very strong | **SWE-bench Pro 81.2** — a slim lead over both Fable 5 and Opus 5 |
| Scientific work | Very strong | Terminal-Bench-Science more than doubled, 24.7% → **52.6%** |
| Knowledge work | Very strong | Top score on financial-analysis benchmarks at the Fable 5 launch |
| Vision | Very strong | Rebuilds web-app source code from screenshots; completed Pokémon FireRed autonomously |
| Availability stability | Medium | Pulled globally June 12 → July 1 2026 under short-lived export controls; now behind stricter safety classifiers with automatic Opus fallback |
| Open-source / self-host | None | Fully proprietary |

**Sourcing note.** Anthropic did **not** publish an SWE-bench Verified score for Fable 5 or Fable 5.1. The "95% on SWE-bench Verified" figure circulating for 5.1 comes from third-party leaderboards. The software-engineering number Anthropic itself reports is SWE-bench Pro 81.2, which is what this map records.

## Version And Availability Timeline (2026)

- **June 9** — Fable 5 released; became the default Claude Code model for Pro/Max subscribers.
- **June 12** — pulled globally under US export controls following a jailbreak report.
- **July 1** — restored worldwide behind stricter safety classifiers; a blocked request falls back to the Opus tier with notice.
- **July 7** — subscription bundling ended; Fable moved to metered usage credits.
- **July 24** — [Opus 5](claude-opus-5.md) shipped and became the default under it, changing what "spend a credit" is being compared against.
- **September 1** — **Fable 5.1 and Mythos 5.1** released. Benchmark gains above, ~60% fewer cybersecurity false positives in Claude Code, and invisible watermarking of Claude-generated text with a detection API in private preview for eligible organizations under EU law.
- **September 22** — Claude Opus 5.5 shipped and became the default Opus in Claude Code `v2.1.280`. Anthropic says it performs at Fable 5.1's level on most work, and it scores above Fable 5.1 on Terminal-Bench 4.0 (66.4% vs 55.8%).

## Relationship To Claude Code

This profile covers the model. [Claude Code](claude-code.md) covers the product where most readers will actually meet it. The practical question inside Claude Code is per-task: **spend Fable 5.1 credits on the hardest work, stay on Opus 5.5 (the default since Sept 22, replacing [Opus 5](claude-opus-5.md)) for everything else.**

## Bottom Line

Fable made "which tier of intelligence do I use on this task" a real selection question on the Anthropic side, the way GPT-5.6's tiers did on the OpenAI side. Plan for the metering and the classifier fallback.
