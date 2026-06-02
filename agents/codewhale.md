# CodeWhale

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/codewhale.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](codewhale.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: CodeWhale (formerly DeepSeek-TUI) is a Rust terminal coding agent built around the DeepSeek and MiMo model families — same shape as Claude Code or Codex CLI, but with low-cost Chinese-stack reasoning models as first-class citizens rather than fallback providers.

> **Rebrand (late May 2026):** The project renamed from `Hmbown/DeepSeek-TUI` to [`Hmbown/CodeWhale`](https://github.com/Hmbown/CodeWhale) and broadened from DeepSeek-only to **DeepSeek + MiMo** (Xiaomi's open model). It now ships a product site at [codewhale.net](https://codewhale.net/). Older links to `DeepSeek-TUI` redirect.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Hmbown (open source community) |
| Route | Direct execution — terminal coding agent |
| Open source | Yes |
| Implementation | Rust |
| Models | DeepSeek + MiMo (Xiaomi) |
| Best for | Developers who want a Claude-Code-style loop on top of DeepSeek / MiMo price-performance |
| Main cost | Tied to a narrow model set by design — if those roadmaps stall, the agent stalls with them |
| GitHub repo | https://github.com/Hmbown/CodeWhale |

## When To Pick It

- You want to run a terminal coding agent against DeepSeek or MiMo models specifically (cost, capability, regional availability) instead of going through a general-purpose harness.
- You prefer a minimal terminal surface over a desktop or IDE-based experience.
- You want the same single-process, single-developer loop that Claude Code and Aider popularized, but anchored on low-cost Chinese-stack reasoning models.

## When Not To Pick It

- You need broad provider portability — a more general harness like [Pi](pi.md) or [Aider](aider.md) is a safer base.
- You want a polished managed product; this is community-driven and the surface area is intentionally narrow.
- You need cloud delegation, parallel agents, or background runs — that is [Codex](codex.md) or [Devin](devin.md) territory.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Terminal workflow | Strong | TUI-native, single-process loop |
| DeepSeek / MiMo tuning | Very strong | Built around these models' tool-use and reasoning patterns |
| Multi-provider support | Light | The point is the DeepSeek + MiMo stack; broad portability is not the goal |
| Background execution | Not the goal | Foreground, single-developer loop |

## Operating Cost

Complexity is Low–Medium. Installing it is straightforward; the real cost is committing to a narrow model set. If DeepSeek or MiMo pricing or availability changes in your region, that affects the agent directly.

## Bottom Line

CodeWhale is the DeepSeek/MiMo-native terminal coding agent that first showed up in this map's heat snapshot as DeepSeek-TUI. It does not try to be a general harness — it is the same Claude-Code-shaped loop, refit around low-cost Chinese-stack models. If your selection is partly driven by cost or by access to DeepSeek / MiMo reasoning models, this is the most direct path to a Claude-Code-style experience on that stack. If portability matters more than price/performance, [Pi](pi.md) or [Aider](aider.md) is a better base.
