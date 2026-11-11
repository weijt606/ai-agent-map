# Claude Opus 5

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/claude-opus-5.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](claude-opus-5.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Claude Opus 5 was the model most Claude-based agents actually ran on from July to September 2026 — it moved the Opus tier close to Fable 5's capability, which makes the frontier tier a deliberate choice rather than the obvious one.

> **Superseded as default (2026-09-22):** Claude Code `v2.1.280` made **Claude Opus 5.5** the default Opus model on September 22 2026. Anthropic says it performs at Fable 5.1's level on most work. Sonnet 5.5 became the default Sonnet on September 28. Opus 5 remains available (`claude-opus-5`); the "default" wording below describes July 24 to September 22 2026. See [benchmarks & billing](../comparisons/benchmarks-and-billing.md).

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anthropic |
| Route | Frontier agentic model — the Opus tier, and the practical default under the Mythos ceiling from July 24 to September 22 2026 |
| Open source | No |
| Best for | Long-running agents, whole-repository work at 1M context, multi-agent coordination, document and spreadsheet tasks |
| API model id | `claude-opus-5` |
| Official announcement | https://www.anthropic.com/news/claude-opus-5 |

## Why This Entry Exists

This route already had the ceiling ([Claude Fable 5](claude-fable-5.md)) and the reference point ([GPT-5.5](gpt-5.5.md)). It did not have the model you actually point an agent at, which from **July 24 2026** was Opus 5 — the default model on Claude Max and the strongest model available on Claude Pro — until Opus 5.5 took that place on September 22.

That gap mattered, because the selection question on the Anthropic side is not "is the frontier better" (it is) but "how much of your work genuinely needs it". Opus 5 is the entry that answers the second half.

## When To Pick It

- You want one model to run an agent all day without thinking about a credit balance. Opus 5 is bundled into Claude subscriptions the way Fable 5 no longer is.
- Your work is **long-context**: the 1M-token window is both the default and the maximum, with instruction-following and tool-calling that hold up across it — there is no smaller-context variant to fall back to.
- You coordinate **subagents**. Anthropic's own framing is writer-verifier patterns with few cases of agents overwriting each other's work, which is the failure mode that makes multi-agent setups unusable.
- Your tasks are office-shaped as much as code-shaped — multi-sheet spreadsheets with non-trivial formulas, structured slide decks.
- You want to tune spend per task: the effort setting trades intelligence against token consumption without switching models.

## When Not To Pick It

- You need the absolute ceiling on the hardest single task — [Fable 5.2](claude-fable-5.md) still leads, and on cybersecurity work Mythos 5 is ahead of Opus 5 outright.
- You want an open-source or self-hosted model — this tier is fully proprietary.
- You want a finished agent product rather than a model. Start at [Claude Code](claude-code.md).

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Agentic coding | Very strong | CursorBench 3.2 within 0.5% of Fable 5's peak |
| Long context | Very strong | 1M tokens, default *and* maximum; 128K max output |
| Computer use | Very strong | OSWorld 2.0 — Anthropic reports it ahead of every model at launch (July 2026) |
| Abstract reasoning | Very strong | ARC-AGI 3 at ~3x the next-best model |
| Workflow automation | Strong | Zapier AutomationBench at ~1.5x the next-best pass rate |
| Multi-agent coordination | Strong | Writer-verifier subagent teams; few overwrite collisions |
| Cybersecurity | Medium | Deliberately behind Mythos 5 on this axis |
| Open-source / self-host | None | Fully proprietary |

Frontier-Bench v0.1 is the headline number Anthropic leads with — state of the art, more than 2x Opus 4.8. Treat single-vendor benchmarks as a claim to check against your own workload, which is this map's standing position on all of them.

## The Tier Ladder (October 2026)

| Model | Where it sits |
| --- | --- |
| [Claude Fable 5.2](claude-fable-5.md) | Mythos-class ceiling |
| Claude Opus 5.5 | Default Opus in Claude Code since Sept 22 2026 |
| **Claude Opus 5** | The default from July 24 to Sept 22 2026, still available |
| Claude Sonnet 5.5 | Default Sonnet in Claude Code since Sept 28 2026 |
| Claude Sonnet 5 | The volume tier |
| Claude Haiku 5.5 | The floor, Oct 7 2026 |

## Where It Runs

- **Claude Code** — the default Opus model from July 24 until `v2.1.280` switched to Opus 5.5 on Sept 22; still selectable. A request blocked by the safety classifier falls back to Opus 4.8 with notice.
- **Claude.ai and Claude Cowork** — default on Max and top model on Pro at launch.
- **Claude API** — `claude-opus-5`, plus Bedrock, Google Cloud, and Microsoft Foundry.
- **Fast mode** (research preview) — about 2.5x the output speed, first-party API only.

## Relationship To Claude Code And Fable 5.1

[Claude Code](claude-code.md) is where most readers meet this model; this profile is for the case where you are choosing what to wire into your own system. The practical split from July to September 2026 was **Opus 5 for the run, Fable 5.1 credits for the hard part**, and Sonnet 5 underneath when the work is high-volume and routine. Since late September the same split runs on Opus 5.5 and Sonnet 5.5. That is a per-task decision, and it is the decision this route exists to support.

## Bottom Line

Opus 5 is the reason the Anthropic side of the model layer stopped being a straight "use the ceiling" question. It takes most of the distance to Fable 5, and was the model your agent ran on when nobody was watching the credit meter, until Opus 5.5 replaced it as the default on September 22. Save the frontier tier for the tasks that actually need it.
