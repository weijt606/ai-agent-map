# Claude Fable 5.1

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/claude-fable-5.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](claude-fable-5.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Claude Fable 5.1 is Anthropic's Mythos-class ceiling as of September 1 2026 — same sticker price as Fable 5, a 75% cut to cache reads that makes long agent sessions materially cheaper, and the model you spend credits on rather than the one you run all day.

> This profile covers the Fable line. It keeps its original `claude-fable-5.md` path from the June 2026 entry so existing links stay valid.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anthropic |
| Route | Frontier agentic model (Mythos class) — the ceiling above [Opus 5](claude-opus-5.md) |
| Open source | No |
| Best for | The hardest agentic work: large migrations, multi-agent workflows, deep research, frontier coding |
| Main cost | $10 / $50 per M tokens; metered usage credits in Claude subscriptions since July 7 2026 |
| Cache read | **$0.25 / M** — 2.5% of input price, against the usual 10% |
| Official announcement | https://www.anthropic.com/news/claude-fable-5-mythos-5 |

## Why This Entry Exists

Like [GPT-6 Astra](gpt-6-astra.md), this is a model rather than an agent product. It is included because it introduced a new tier (Mythos, above Opus) into the model layer that most agents in this map run on, and because its pricing and availability arc directly changed how Claude Code and Claude-based agents are selected and budgeted.

Fable and **Mythos** share the same underlying model at each version; the difference is safety access. Fable 5.1 is the generally available version. Mythos 5.1 has lighter safeguards and is limited to vetted organizations through Project Glasswing — cyberdefense, infrastructure, and select life-science research.

## When To Pick It

- You want the strongest available Claude model for agentic work — engineering, research, or analysis.
- Your tasks are big enough to justify the price. The Fable 5 launch reference case is Stripe reporting a codebase migration "that would have taken a whole team two months by hand" completed in a day.
- **Your agent re-reads a large context on every turn.** This is the 5.1-specific reason: cache reads dropped from $1/M to $0.25/M, which Anthropic puts at roughly 25% off typical workloads and up to 45% off heavily agentic ones with no change to the sticker price.
- You hit false refusals on security-adjacent code. Anthropic reports around 60% fewer cybersecurity false positives for Claude Code users on 5.1.

## When Not To Pick It

- You are cost-sensitive — $10/$50 per million tokens is 2x [Opus 5](claude-opus-5.md) on both sides, and since July 7 2026 it is metered rather than bundled in subscriptions.
- Your workload does not need Mythos-class capability. **Opus 5 is the dependable default under it** and takes most of the distance at half the price; Sonnet 5 sits under that again at $2/$10.
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
| Long-session economics | Strong | Cache reads at 2.5% of input price — the cheapest cache read of any frontier model on this map |
| Availability stability | Medium | Pulled globally June 12 → July 1 2026 under short-lived export controls; now behind stricter safety classifiers with automatic Opus fallback |
| Open-source / self-host | None | Fully proprietary |

**Sourcing note.** Anthropic did **not** publish an SWE-bench Verified score for Fable 5 or Fable 5.1. The "95% on SWE-bench Verified" figure circulating for 5.1 comes from third-party leaderboards. The software-engineering number Anthropic itself reports is SWE-bench Pro 81.2, which is what this map records.

## Version And Availability Timeline (2026)

- **June 9** — Fable 5 released; became the default Claude Code model for Pro/Max subscribers.
- **June 12** — pulled globally under US export controls following a jailbreak report.
- **July 1** — restored worldwide behind stricter safety classifiers; a blocked request falls back to the Opus tier with notice.
- **July 7** — subscription bundling ended; Fable moved to metered usage credits.
- **July 24** — [Opus 5](claude-opus-5.md) shipped and became the default under it, changing what "spend a credit" is being compared against.
- **September 1** — **Fable 5.1 and Mythos 5.1** released. Cache reads cut 75%, benchmark gains above, ~60% fewer cybersecurity false positives in Claude Code, and invisible watermarking of Claude-generated text with a detection API in private preview for eligible organizations under EU law.

## Relationship To Claude Code

This profile covers the model. [Claude Code](claude-code.md) covers the product where most readers will actually meet it. The practical question inside Claude Code is per-task: **spend Fable 5.1 credits on the hardest work, stay on [Opus 5](claude-opus-5.md) for everything else.**

## Bottom Line

Fable made "which tier of intelligence do I pay for on this task" a real selection question on the Anthropic side, the way GPT-5.6's tiers did on the OpenAI side. The 5.1 refresh did not move the sticker; it moved the part of the bill that a long-running agent actually generates. Budget for the price, the metering, and the classifier fallback — and if your agent replays a large context, re-run the math, because it changed on September 1.
