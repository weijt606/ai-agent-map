# Continue

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/continue.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](continue.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Continue is the open-source IDE extension that lets you bring any model — cloud or local — into VS Code or JetBrains for autocomplete, chat, editing, and agentic workflows.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Continue Dev, Inc. |
| Route | Open-source editor-centric AI assistant |
| Open source | Yes, Apache 2.0 |
| Best for | Teams that want model freedom, local/private hosting, or enterprise-wide assistant config without vendor lock-in |
| Main cost | You own model setup — configuration overhead is higher than turnkey alternatives |
| Official website | https://continue.dev |
| GitHub repo | https://github.com/continuedev/continue |

## When To Pick It

- You want full control over which model powers your coding assistant — cloud APIs, local Ollama, or self-hosted endpoints.
- You work in VS Code or JetBrains and want an open-source alternative to GitHub Copilot or Cursor.
- Your team needs to share and distribute custom assistant configs through Continue Hub.
- You care about data privacy and want to run everything locally without sending code to third-party APIs.
- You want AI-powered PR checks that run as GitHub status checks via source-controlled rules.

## When Not To Pick It

- You want a plug-and-play experience with zero configuration. Copilot or Cursor are simpler to start with.
- You want a standalone AI-native IDE, not an extension. Look at Cursor or Windsurf instead.
- You want the most polished multi-file editing UX out of the box. Cursor's purpose-built editor is more integrated.
- You need terminal-first or CLI agent workflows. Look at Claude Code or Aider instead.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Autocomplete | Strong | Tab completion with any model |
| Chat | Strong | Inline chat in the editor |
| Code editing | Strong | Inline edit and refactor |
| Agent mode | Medium | Agentic workflows available but less mature than Cursor or Cline |
| Model flexibility | Very strong | Cloud, local, or self-hosted — any provider |
| Team config | Strong | Hub and Mission Control for distributing assistant settings |
| CI integration | Medium | PR checks via markdown rules |
| Standalone runtime | None | Extension only, requires VS Code or JetBrains |

## Operating Cost

Complexity is Medium. The tool itself is free, but you own the model layer — that means choosing a provider, managing API keys or local GPU resources, and configuring the assistant. Teams with existing infrastructure will find this easy; individuals who just want coding help may find the setup overhead not worth it compared to a subscription product.

## Bottom Line

Continue is the strongest open-source option for teams that want a coding assistant without vendor lock-in on the model layer. The trade-off is clear: you get full control, but you also own the configuration and model cost.
