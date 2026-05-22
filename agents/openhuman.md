# OpenHuman

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/openhuman.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](openhuman.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: OpenHuman is an open-source desktop agent built around personal data integration — it auto-syncs Gmail, Notion, GitHub, Slack, and 118+ other tools into a local Memory Tree so the assistant does not start every session cold.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | tinyhumansai (Senami Ekakel) |
| Route | Self-hosted / local runtime — life-integration variant |
| Open source | Yes (GPL-3.0, Rust + TypeScript on Tauri) |
| Best for | Individuals who want a private, locally-controlled assistant that already knows their work context |
| Main cost | You inherit GPL-3.0 (more constraining than MIT) and an opinionated data-pulling architecture |
| GitHub repo | https://github.com/tinyhumansai/openhuman |

## When To Pick It

- You want a desktop agent that already knows your Gmail, Notion, GitHub, calendar, and files — not one you have to brief manually every session.
- You care about privacy: data stays on your machine, and Ollama integration lets you run the whole loop locally.
- You want a Memory Tree (hierarchical summaries in SQLite) plus an Obsidian-compatible wiki — a transparent, browsable store of what the agent knows about you.
- You want LLM cost compression: the bundled "TokenJuice" layer reportedly trims up to 80% off token consumption before requests hit the model.

## When Not To Pick It

- You want a coding-first agent — OpenHuman is a personal life-and-work assistant, not a [Claude Code](claude-code.md) or [Aider](aider.md) competitor.
- You need a permissive license (MIT / Apache). GPL-3.0 will block some commercial integration paths.
- You want managed or cloud hosting. OpenHuman is desktop-first via Tauri, not a SaaS surface.
- You only need one or two integrations — the value scales with how many of the 118+ connectors you actually wire up.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Personal data integration | Very strong | 118+ third-party connectors with 20-minute auto-fetch loop |
| Persistent memory | Strong | Memory Tree in SQLite plus an Obsidian-compatible wiki; both user-editable |
| Multi-LLM routing | Strong | Multiple cloud providers plus Ollama for fully local execution |
| Voice and native tools | Medium | Built-in STT/TTS, file system access, git, web search |
| Coding-first workflow | Not the goal | Dedicated coding agents ([Claude Code](claude-code.md), [Aider](aider.md), [Pi](pi.md)) cover that space |

## Operating Cost

Complexity is Medium. The desktop install is straightforward, but the value depends on actually connecting your tools and letting the auto-fetch loop build up the Memory Tree over weeks. You also accept GPL-3.0 in your environment — read the license before adopting it inside a commercial product.

## Bottom Line

OpenHuman is what a "personal AI super intelligence" looks like in practice when shipped as open source: a desktop daemon that auto-pulls from 118+ tools, summarizes everything into a local Memory Tree, and routes between LLMs (cloud or local). After two consecutive weeks of strong GitHub growth in May 2026 the positioning is no longer vague — it is the life-integration variant of the self-hosted local runtime route, distinct from the coding-first agents and from the multi-channel runtimes like [Hermes Agent](hermes-agent.md) or [Mercury Agent](mercury-agent.md).
