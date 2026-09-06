# Claude Opus 5

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/claude-opus-5.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](claude-opus-5.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Claude Opus 5 is the model most Claude-based agents actually run on — it took the Opus tier's price ($5/$25, unchanged from Opus 4.8) and moved it close to Fable 5's capability, which makes the frontier tier a deliberate spend rather than the obvious choice.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anthropic |
| Route | Frontier agentic model — the Opus tier, and the practical default under the Mythos ceiling |
| Open source | No |
| Best for | Long-running agents, whole-repository work at 1M context, multi-agent coordination, document and spreadsheet tasks |
| Main cost | $5 / $25 per M tokens — same as Opus 4.8; Fast mode is $10 / $50 |
| API model id | `claude-opus-5` |
| Official announcement | https://www.anthropic.com/news/claude-opus-5 |

## Why This Entry Exists

This route already had the ceiling ([Claude Fable 5](claude-fable-5.md)) and the reference point ([GPT-5.5](gpt-5.5.md)). It did not have the model you actually point an agent at, which since **July 24 2026** has been Opus 5 — the default model on Claude Max and the strongest model available on Claude Pro.

That gap mattered, because the selection question on the Anthropic side is not "is the frontier better" (it is) but "how much of your work genuinely needs it". Opus 5 is the entry that answers the second half.

## When To Pick It

- You want one model to run an agent all day without thinking about a credit balance. Opus 5 is bundled into Claude subscriptions the way Fable 5 no longer is.
- Your work is **long-context**: the 1M-token window is both the default and the maximum, with instruction-following and tool-calling that hold up across it — there is no smaller-context variant to fall back to.
- You coordinate **subagents**. Anthropic's own framing is writer-verifier patterns with few cases of agents overwriting each other's work, which is the failure mode that makes multi-agent setups unusable.
- Your tasks are office-shaped as much as code-shaped — multi-sheet spreadsheets with non-trivial formulas, structured slide decks.
- You want to tune spend per task: the effort setting trades intelligence against token consumption without switching models.

## When Not To Pick It

- You need the absolute ceiling on the hardest single task — [Fable 5.1](claude-fable-5.md) still leads, and on cybersecurity work Mythos 5 is ahead of Opus 5 outright.
- You are cost-sensitive at volume. **Sonnet 5 is $2/$10** and Anthropic positions it close to Opus 4.8; if your agent's work is mostly routine, the Opus tier is a 2.5x bill for capability you may not be using.
- You want an open-source or self-hosted model — this tier is fully proprietary.
- You want a finished agent product rather than a model. Start at [Claude Code](claude-code.md).

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Agentic coding | Very strong | CursorBench 3.2 within 0.5% of Fable 5's peak, at half the price |
| Long context | Very strong | 1M tokens, default *and* maximum; 128K max output |
| Computer use | Very strong | OSWorld 2.0 — Anthropic reports it ahead of every model at any price point, and ahead of Fable 5 at roughly a third of the cost |
| Abstract reasoning | Very strong | ARC-AGI 3 at ~3x the next-best model |
| Workflow automation | Strong | Zapier AutomationBench at ~1.5x the next-best pass rate |
| Multi-agent coordination | Strong | Writer-verifier subagent teams; few overwrite collisions |
| Cybersecurity | Medium | Deliberately behind Mythos 5 on this axis |
| Open-source / self-host | None | Fully proprietary |

Frontier-Bench v0.1 is the headline number Anthropic leads with — state of the art, more than 2x Opus 4.8 at lower cost. Treat single-vendor benchmarks as a claim to check against your own workload, which is this map's standing position on all of them.

## The Tier Ladder (first-party API prices, September 2026)

| Model | Input / Output per M | Cache read | Where it sits |
| --- | --- | --- | --- |
| [Claude Fable 5.1](claude-fable-5.md) | $10 / $50 | **$0.25** | Mythos-class ceiling; the cache read is 2.5% of input, not the usual 10% |
| **Claude Opus 5** | **$5 / $25** | $0.50 | The default you run; Fast mode $10 / $50 |
| Claude Sonnet 5 | $2 / $10 | $0.20 | The volume tier — $2/$10 was introductory pricing, made permanent |

The 1M-token context window is billed at standard rates across the whole window on Claude 4.6 and later, so long context is not a separate price band on this side of the market. Compare with [GPT-6 Astra](gpt-6-astra.md), which doubles input price past 272k tokens.

## Where It Runs

- **Claude Code** — the default coding surface; a request blocked by the safety classifier falls back to Opus 4.8 with notice.
- **Claude.ai and Claude Cowork** — default on Max, top model on Pro.
- **Claude API** — `claude-opus-5`, plus Bedrock, Google Cloud, and Microsoft Foundry.
- **Fast mode** (research preview) — about 2.5x the output speed at 2x the price, first-party API only.

## Relationship To Claude Code And Fable 5.1

[Claude Code](claude-code.md) is where most readers meet this model; this profile is for the case where you are choosing what to wire into your own system. The practical split since July 2026: **Opus 5 for the run, Fable 5.1 credits for the hard part**, and Sonnet 5 underneath when the work is high-volume and routine. That is a per-task decision, and it is the decision this route exists to support.

## Bottom Line

Opus 5 is the reason the Anthropic side of the model layer stopped being a straight "pay for the ceiling" question. It holds the Opus price, takes most of the distance to Fable 5, and is the model your agent runs on when nobody is watching the credit meter. Budget the frontier tier for the tasks that actually need it.
