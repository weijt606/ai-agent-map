# MiMoCode

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/mimocode.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](mimocode.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: MiMoCode is Xiaomi's official terminal coding agent — a Claude-Code-shaped loop with a persistent cross-session memory system at its center, so the agent keeps a deep understanding of your project across runs instead of relearning it each time.

> **Distinct from [CodeWhale](codewhale.md):** CodeWhale is a third-party Rust TUI that *wraps* the DeepSeek + MiMo models. MiMoCode (`XiaomiMiMo/MiMo-Code`, launched 2026-06-10) is Xiaomi's own first-party CLI for the MiMo line. Same model family in the picture, different vendor and codebase.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Xiaomi (MiMo team) |
| Route | Direct execution — terminal coding agent |
| Open source | Yes |
| Implementation | TypeScript |
| License | MIT |
| Models | MiMo Auto (free zero-config channel, limited time); Xiaomi MiMo Platform; any mainstream LLM API |
| Best for | Developers who want a memory-first coding CLI tuned for long-horizon work on one project |
| Main cost | Brand new (days old) — feature surface and stability are still moving fast |
| GitHub repo | https://github.com/XiaomiMiMo/MiMo-Code |

## When To Pick It

- You want persistent project memory as a built-in, not an add-on: MiMoCode keeps a project `MEMORY.md`, automatic session checkpoints, scratch notes, and per-task progress, injected back on resume via SQLite FTS5 search.
- You want zero-config startup — the built-in **MiMo Auto** channel is free for a limited time and needs no API key, with one-step import from Claude Code if you already use it.
- You work in long-horizon sessions where context reconstruction (rebuilding context from the latest checkpoint + memory when the window fills) matters more than raw speed.

## When Not To Pick It

- You need a battle-tested tool — this launched on 2026-06-10 and is still very early; expect rapid change.
- You want vendor-neutral portability as the headline — MiMoCode supports custom providers, but it is built around the MiMo stack first; [Pi](pi.md) or [Aider](aider.md) is a more neutral base.
- You need cloud delegation, parallel agents, or detached background runs — that is [Codex](codex.md) or [Devin](devin.md) territory.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Terminal workflow | Strong | TUI-native; `build` / `plan` / `compose` agent modes switchable with Tab |
| Cross-session memory | Very strong | Project memory, checkpoints, notes, task progress — the core differentiator |
| Context management | Strong | Automatic checkpoints, context reconstruction, budgeted injection |
| Multi-provider support | Medium | MiMo Auto + Xiaomi platform default; custom OpenAI-compatible providers supported |
| Background execution | Not the goal | Foreground, single-developer loop |

## Operating Cost

Complexity is Low. Install is a one-line script or `npm install -g @mimo-ai/cli`, and first launch walks you through configuration; MiMo Auto removes the API-key step entirely for now. The real cost is maturity: this is a days-old project, so the memory system, agent modes, and provider story are all still moving.

## Bottom Line

MiMoCode is the memory-first entry in the terminal coding-agent field — Xiaomi's official CLI for the MiMo models, built so the agent carries project understanding across sessions rather than starting cold each run. If long-horizon work on a single codebase is your pain point and you are comfortable on a brand-new tool, it is worth a look; if you need stability or vendor neutrality, [Aider](aider.md) or [Pi](pi.md) is safer. Do not confuse it with [CodeWhale](codewhale.md), the third-party DeepSeek + MiMo TUI; for Moonshot's official Kimi CLI, see [Kimi Code](kimi-code.md).
