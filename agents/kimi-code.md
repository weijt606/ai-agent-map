# Kimi Code

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/kimi-code.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](kimi-code.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Kimi Code is Moonshot AI's official terminal coding agent — the same Claude-Code-shaped loop (read/edit code, run shell, search files, fetch the web), tuned around the Kimi models first, but configurable to any OpenAI-compatible provider.

> **Lineage:** Kimi Code (`MoonshotAI/kimi-code`, TypeScript) is the next-generation successor to the original [`MoonshotAI/kimi-cli`](https://github.com/MoonshotAI/kimi-cli) (Python, 8.9k stars). The team has since archived `kimi-cli` (last release 1.52.0 on 2026-09-22; its README now says it is no longer maintained and existing installs will stop working). On first launch Kimi Code detects the older data in `~/.kimi/` and offers to migrate config, MCP servers, history and sessions (`kimi migrate` does the same). Treat Kimi Code as the only supported surface; the legacy `kimi-cli` docs stay online for reference.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Moonshot AI (Kimi) |
| Route | Direct execution — terminal coding agent |
| Open source | Yes |
| Implementation | TypeScript (kimi-code); Python (legacy kimi-cli) |
| License | MIT |
| Models | Kimi models out of the box; any OpenAI-compatible provider |
| Best for | Developers who want a vendor-official Kimi-native coding CLI with first-class IDE/ACP integration |
| Main cost | A young rebuild — `kimi-cli` was archived in September 2026, so older docs and issues still sit in the archived repo |
| GitHub repo | https://github.com/MoonshotAI/kimi-code |

## When To Pick It

- You want a first-party terminal coding agent from the team that builds the Kimi models, rather than a third-party harness pointed at a Kimi endpoint.
- You want a no-dependency install (the official script needs no Node.js) and a CLI that doubles as an ACP agent server for Zed, JetBrains, and other ACP-compatible editors.
- You already use Kimi for coding and want the model and the agent loop tuned together, with the option to swap in any OpenAI-compatible provider later.

## When Not To Pick It

- You need a mature, stable surface today — the project only recently replaced `kimi-cli` (archived September 2026), so expect churn.
- You want broad multi-vendor neutrality as the core value — a provider-agnostic harness like [Pi](pi.md) or [Aider](aider.md) is a safer base.
- You need cloud delegation, parallel agents, or detached background runs — that is [Codex](codex.md) or [Devin](devin.md) territory.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Terminal workflow | Strong | Single-process loop; can drop into a shell command mode |
| Kimi model tuning | Very strong | First-party; the agent and model ship from the same team |
| IDE / ACP integration | Strong | ACP agent server (`kimi acp`) plus a VS Code extension |
| Multi-provider support | Medium | Works with OpenAI-compatible providers, but Kimi is the default path |
| Background execution | Not the goal | Foreground, single-developer loop |

## Operating Cost

Complexity is Low–Medium. Install is a one-line script with no Node.js requirement. The real cost is youth: the original `kimi-cli` was archived in September 2026 in favor of `kimi-code`, so older docs and issues still live in the archived repo, and if you are coming from `kimi-cli` you have to migrate, because the old installs are no longer supported.

## Bottom Line

Kimi Code is the vendor-official answer to "I want a Claude-Code-style CLI, but Kimi-native." It is the clearest first-party path onto Moonshot's models, with real IDE reach through ACP and a VS Code extension. The caveat is age — it replaced `kimi-cli` only recently (archived September 2026), so the surface is still settling. If you want a provider-neutral base instead, [Pi](pi.md) or [Aider](aider.md) fits better; if you specifically want the official Kimi loop, this is it. For the Chinese-model-stack sibling that targets DeepSeek + MiMo, see [CodeWhale](codewhale.md); for Xiaomi's own official CLI, see [MiMoCode](mimocode.md).
