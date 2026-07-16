# Claude Code

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/claude-code.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](claude-code.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: if you want a high-frequency coding loop with an agent inside the terminal and IDE, Claude Code is one of the clearest starting points.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anthropic |
| Route | Local and IDE-first direct coding agent |
| Open source | No |
| Best for | High-frequency local coding collaboration |
| Main cost | You still own permissions, environment, and pacing |
| Official website | https://code.claude.com/docs/en/overview |

## When To Pick It

- You want the agent inside your local repo, not behind a distant task queue.
- You want instructions, MCP, and subagents to work in one flow.
- You want stronger agent capability without moving your work into a totally different platform.

## When Not To Pick It

- You only want detached background execution and later review.
- You need a fully open-source self-hosted stack.
- You do not want to manage permissions, tools, or local environment behavior.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Tool use | Strong | Reading code, editing files, and running commands are central |
| Code execution | Strong | The terminal loop is core to the product |
| MCP | Strong | A major reason it fits deeper local workflows |
| Subagents | Strong | Useful for specialization and context isolation |
| Scheduling | Medium | Available, but not the primary mental model |

## 2026 Model And Product Updates

The model layer under Claude Code moved a lot in mid-2026; the product's selection logic now includes a credit-budget question:

- **May 28 2026 — Opus 4.8**: fixed the comment-verbosity and tool-calling issues seen with Opus 4.7, and shipped **Dynamic workflows** (research preview) — Claude plans the work, then runs hundreds of parallel subagents in a single Claude Code session.
- **June 9 2026 — [Claude Fable 5](claude-fable-5.md)**: Anthropic's first Mythos-class model (a tier above Opus) became the default model in Claude Code for Pro and Max subscribers.
- **June 12 → July 1 2026**: Fable 5 was pulled globally under short-lived US export controls, then returned behind stricter safety classifiers — a blocked request falls back to Opus 4.8 automatically.
- **From July 7 2026**: Fable 5 is no longer bundled in subscriptions; it runs on metered usage credits, so the effective model ceiling in Claude Code now depends on your credit budget, with Opus 4.8 as the dependable default.

## Operating Cost

Complexity is Medium. Starting is straightforward, but good long-term use depends on clean project instructions, permission design, and disciplined tool setup. Since July 2026, budgeting Fable 5 credits versus staying on Opus 4.8 is part of the operating decision.

## Bottom Line

Claude Code behaves more like a durable development augmentation layer than a one-shot task inbox — and since mid-2026, one whose capability ceiling is a per-task model choice (Fable 5 on credits, Opus 4.8 as the default) rather than a fixed property.