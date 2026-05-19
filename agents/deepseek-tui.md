# DeepSeek-TUI

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/deepseek-tui.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](deepseek-tui.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: DeepSeek-TUI is a terminal coding agent built around the DeepSeek model family — same shape as Claude Code or Codex CLI, but with the DeepSeek stack as a first-class citizen rather than a fallback provider.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Hmbown (open source community) |
| Route | Direct execution — terminal coding agent |
| Open source | Yes |
| Best for | Developers who want a Claude-Code-style loop but on top of DeepSeek's price-performance curve |
| Main cost | Tied to one model family by design — if DeepSeek's roadmap stalls, the agent stalls with it |
| GitHub repo | https://github.com/Hmbown/DeepSeek-TUI |

## When To Pick It

- You want to run a terminal coding agent against DeepSeek models specifically (cost, capability, regional availability) instead of going through a general-purpose harness.
- You prefer a minimal terminal surface over a desktop or IDE-based experience.
- You want the same single-process, single-developer loop that Claude Code and Aider popularized, but without leaving DeepSeek's ecosystem.

## When Not To Pick It

- You need broad provider portability — a more general harness like [Pi](pi.md) or [Aider](aider.md) is a safer base.
- You want a polished managed product; this is community-driven and the surface area is intentionally narrow.
- You need cloud delegation, parallel agents, or background runs — that is [Codex](codex.md) or [Devin](devin.md) territory.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Terminal workflow | Strong | TUI-native, single-process loop |
| DeepSeek-specific tuning | Very strong | Built around DeepSeek's tool-use and reasoning patterns |
| Multi-provider support | Light | The point is DeepSeek; portability is not the goal |
| Background execution | Not the goal | Foreground, single-developer loop |

## Operating Cost

Complexity is Low–Medium. Installing it is straightforward; the real cost is committing to a single model family. If DeepSeek's pricing or availability changes in your region, that affects the agent directly.

## Bottom Line

DeepSeek-TUI is the first DeepSeek-native terminal coding agent to show up in this map's heat snapshot. It does not try to be a general harness — it is the same Claude-Code-shaped loop, refit around DeepSeek. If your selection is partly driven by cost or by access to DeepSeek's reasoning models, this is the most direct path to a Claude-Code-style experience on that stack. If portability matters more than price/performance, [Pi](pi.md) or [Aider](aider.md) is a better base.
