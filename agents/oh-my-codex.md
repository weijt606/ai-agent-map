# oh-my-codex

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/oh-my-codex.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](oh-my-codex.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: oh-my-codex is a stronger operating layer for Codex CLI, not a separate execution engine.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Yeachan Heo and contributors |
| Route | Workflow / orchestration layer for Codex CLI |
| Open source | Yes |
| Best for | Codex users who want reusable skills, team execution, hooks, and persistent runtime state |
| Main cost | You are adding more ceremony, setup, and runtime concepts on top of Codex rather than simplifying the stack |
| Official website | https://yeachan-heo.github.io/oh-my-codex-website/ |
| GitHub repo | https://github.com/Yeachan-Heo/oh-my-codex |

## When To Pick It

- You already use Codex CLI and want a more opinionated day-to-day workflow around it.
- You want a consistent clarify-plan-execute loop with `$deep-interview`, `$ralplan`, `$team`, and `$ralph`.
- You want durable project state, plans, logs, and memory under `.omx/` instead of relying on a thin one-shot CLI layer.

## When Not To Pick It

- You want plain Codex with as little extra workflow surface as possible.
- You do not want tmux, hooks, skills, or another runtime layer to manage.
- You want managed cloud delegation rather than a local operator-focused Codex stack.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Workflow standardization | Very strong | The canonical clarify-plan-execute loop is the core value |
| Multi-agent execution | Strong | Team mode is useful when the task is large enough |
| Persistent state | Strong | `.omx/` is a real differentiator for plans, logs, and mode tracking |
| Native Codex integration | Strong | Hooks and Codex-aware workflow surfaces are central |
| Low-ceremony usage | Medium | It is easy to start, but not the lightest way to keep using Codex |

## Operating Cost

Complexity is Medium. The setup is manageable, but OMX works best when you are comfortable with Codex CLI, Node, and often tmux on macOS or Linux. The real trade-off is that you get stronger orchestration only by accepting a thicker operating layer.

## Bottom Line

If Codex CLI is already the engine you trust and you want a more structured operating model around it, oh-my-codex deserves a serious look.