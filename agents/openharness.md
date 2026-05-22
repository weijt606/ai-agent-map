# OpenHarness

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/openharness.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](openharness.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: OpenHarness is HKUDS's open agent harness — 10 subsystems, 43+ tools, anthropics/skills compatibility, and a personal-agent app (ohmo) on top — built to be the most transparent production-grade harness you can run yourself.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | HKUDS (Hong Kong University Data Systems Lab) |
| Route | Agent harness framework — inspectable production runtime |
| Open source | Yes (MIT, Python) |
| Best for | Researchers and engineers who want a fully open harness with permissions, skills, and multi-agent coordination — not just a loop |
| Main cost | Heavier than [mini-swe-agent](mini-swe-agent.md) by an order of magnitude; the value depends on actually using the wider feature surface |
| GitHub repo | https://github.com/HKUDS/OpenHarness |

## When To Pick It

- You want a harness that is inspectable end-to-end — 10 named subsystems (engine, tools, skills, plugins, permissions, hooks, commands, MCP, memory, coordinator) make the internals legible.
- You want anthropics/skills compatibility, MCP client support, and a Claude-style plugin system in the same project.
- You need multi-level permissions (default, auto, plan mode), path-based rules, and approval workflows out of the box.
- You want to drive Claude, OpenAI, Copilot, Moonshot/Kimi, GLM, MiniMax, NVIDIA NIM, or any OpenAI/Anthropic-compatible endpoint — and Ollama for local — through one runtime.
- You want a personal-agent surface (ohmo) for Feishu / Slack / Telegram / Discord on top of the same harness.

## When Not To Pick It

- You want a 100-line harness you can audit in one sitting — that is [mini-swe-agent](mini-swe-agent.md)'s point.
- You want a vendor-managed product. OpenHarness is academic-lab open source; you self-host.
- You want a polished UI for end users. OpenHarness is CLI/TUI-first; the value is the harness, not the chrome.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Subsystem clarity | Very strong | 10 named subsystems with explicit responsibilities |
| Tool surface | Very strong | 43+ built-in tools across file I/O, shell, search, web, MCP |
| Permission model | Strong | Multi-level modes, path-based rules, interactive approval |
| Skills / plugins | Strong | anthropics/skills-compatible, Claude-style plugin format |
| Provider coverage | Strong | All major cloud LLMs plus OpenAI/Anthropic-compatible endpoints plus Ollama |
| Multi-agent coordination | Medium | Coordinator subsystem exists; production patterns still maturing |

## Operating Cost

Complexity is Medium. Installation via `pip install openharness-ai` is straightforward; the cost is conceptual rather than operational — you take on responsibility for choosing which subsystems to activate, which providers to wire up, and how to manage permissions. The harness is not opinionated; you are.

## Bottom Line

OpenHarness sits between two extremes: heavier than [mini-swe-agent](mini-swe-agent.md) (which deliberately fits in 100 lines), lighter than vendor products like [Cursor](cursor.md) or [Claude Code](claude-code.md). The 10-subsystem architecture, anthropics/skills compatibility, and MCP support make it the most "infrastructure-shaped" harness in this map — if you want to study how a production agent runtime is put together, or build one of your own, this is the cleanest reference to fork. Note the shared HKUDS authorship with [CLI-Anything](cli-anything.md) — both projects sit on the same "make agents production-native" research line.
