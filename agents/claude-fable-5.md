# Claude Fable 5

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/claude-fable-5.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](claude-fable-5.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Claude Fable 5 is Anthropic's first generally available Mythos-class model — a tier above Opus — and since June 2026 it is the capability ceiling for Claude-based agents, priced and rationed accordingly.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anthropic |
| Route | Frontier agentic model (Mythos class) powering Claude Code, Claude.ai, and API surfaces |
| Open source | No |
| Best for | The hardest agentic work: large migrations, multi-agent workflows, deep research, frontier coding |
| Main cost | $10/M input, $50/M output; metered usage credits in Claude subscriptions since July 7 2026 |
| Official announcement | https://www.anthropic.com/news/claude-fable-5-mythos-5 |

## Why This Entry Exists

Like [GPT-5.5](gpt-5.5.md), this is a model rather than an agent product. It is included because it introduced a new tier (Mythos, above Opus) into the model layer that most agents in this map run on, and because its June–July availability arc directly changed how Claude Code and Claude-based agents are selected and budgeted.

Fable 5 and **Claude Mythos 5** share the same underlying model: Fable 5 is the generally available version with additional safety measures for dual-use capabilities; Mythos 5 is available without those measures only to approved organizations (cyberdefense, infrastructure, Project Glasswing partners, and select bio researchers).

## When To Pick It

- You want the strongest available Claude model for agentic work — engineering, research, or analysis.
- Your tasks are big enough to justify the price: the launch reference case is Stripe reporting a codebase migration "that would have taken a whole team two months by hand" completed in a day.
- You run complex multi-agent workflows and want fewer turns per result.
- You already work in Claude Code / Claude.ai and can budget usage credits for the hardest tasks.

## When Not To Pick It

- You are cost-sensitive — $10/$50 per million tokens is 2x Opus 4.8 on both sides, and since July 7 2026 it is metered rather than bundled in subscriptions.
- Your workload does not need Mythos-class capability — Opus 4.8 is the dependable default under it and handles most work.
- You need an open-source or self-hosted model.
- You want a finished agent product, not a model — look at [Claude Code](claude-code.md) instead.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Agentic coding | Very strong | 77.2 on the Artificial Analysis Coding Agent Index — above GPT-5.5 (76.4) and Opus 4.8 (72.5), below GPT-5.6 Sol (80) |
| Knowledge work | Very strong | Top score on financial-analysis benchmarks at launch |
| Vision | Very strong | Rebuilds web-app source code from screenshots; completed Pokémon FireRed autonomously |
| Scientific work | Very strong | ~10x speedup reported in protein-design workflows; first model to consistently produce novel molecular-biology hypotheses |
| Multi-agent workflows | Strong | "More engineering power in fewer turns" is the recurring practitioner report |
| Availability stability | Medium | Pulled globally June 12 → July 1 2026 under short-lived export controls; now behind stricter safety classifiers with automatic Opus 4.8 fallback |
| Open-source / self-host | None | Fully proprietary |

## Availability Timeline (2026)

- **June 9** — released; became the default Claude Code model for Pro/Max subscribers.
- **June 12** — pulled globally under US export controls following a jailbreak report.
- **July 1** — restored worldwide behind stricter safety classifiers; a blocked request falls back to Opus 4.8 with notice.
- **July 7** — subscription bundling ended; Fable 5 moved to metered usage credits.

## Relationship To Claude Code

This profile covers the model. [Claude Code](claude-code.md) covers the product where most readers will actually meet it. Since July 2026 the practical question inside Claude Code is per-task: spend Fable 5 credits on the hardest work, stay on Opus 4.8 for everything else.

## Bottom Line

Fable 5 made "which tier of intelligence do I pay for on this task" a real selection question on the Anthropic side, the way GPT-5.6's Sol/Terra/Luna tiers did on the OpenAI side. The capability jump is real; so are the price, the metering, and the safety-classifier fallback — budget for all three.
