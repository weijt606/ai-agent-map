# Mainstream Agent Selection Matrix

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/mainstream-agent-landscape.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](mainstream-agent-landscape.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

This is not a leaderboard. It is a first-pass matrix for shrinking the shortlist.

Each row answers one question: what kind of problem is this project best suited to solve?

## One-Page Comparison View

| Project | Route | Where it runs | Operating rhythm | Best for | Main cost |
| --- | --- | --- | --- | --- | --- |
| [Claude Code](../agents/claude-code.md) | Local collaboration coding agent | Terminal, IDE, desktop, web | High interaction | Teams who want to code with an agent in-flow | Less ideal for fully detached background execution |
| [Claude Managed Agents](../agents/claude-managed-agents.md) | Managed automation path | Anthropic managed / cloud execution | Scheduled, detached, programmatic | Background Claude workflows | Public boundary is spread across multiple concepts |
| [Codex](../agents/codex.md) | Cloud delegation coding agent | Isolated cloud execution plus CLI / IDE | Async delegation | Reviewable task execution with logs and tests | Less immediate than editor-native agents |
| [GitHub Copilot](../agents/github-copilot.md) | Agent platform | VS Code, local CLI, cloud, GitHub | Local-to-cloud handoff | Teams centered on VS Code and GitHub | Best value depends on ecosystem alignment |
| [Cline](../agents/cline.md) | Approval-first coding agent | Editor and local terminal | High approval, high control | Powerful editor-native automation with human control | Approval overhead is part of the model |
| [OpenHands](../agents/openhands.md) | Open-source SWE agent | Self-hosted, cloud, enterprise | Flexible | Teams evaluating serious open-source execution | Heavier setup and runtime requirements |
| [Devin](../agents/devin.md) | Managed executor | Managed cloud product | Delegate then review | Clear issue-to-PR style execution | Less room for self-hosting and deep customization |
| [Hermes Agent](../agents/hermes-agent.md) | Self-hosted multi-agent environment | CLI plus gateway | Long-lived | Memory, skills, delegation, channels | Needs ongoing operational curation |
| [OpenClaw](../agents/openclaw.md) | Runtime / gateway | Local-first self-hosted runtime | Always-on runtime style | Multi-channel, device-aware, tool-rich assistants | Too heavy for pure coding-only work |
| [LangChain](../agents/langchain.md) | High-level framework | Open-source library | Fast assembly | Building custom agents quickly | Less precise than lower-level orchestration |
| [LangGraph](../agents/langgraph.md) | Low-level orchestration framework | Open-source library | Platform building | Durable stateful agent workflows | Highest design and ops burden |
| [Froge Code](../agents/froge-code.md) | Review-first automation platform | Self-hosted platform | Multiple attempts plus human choice | Task-board-centric coding automation | Name still needs confirmation |

## How To Read This Table

1. Start with the route and eliminate the models that do not match your workflow.
2. Check where the system runs and remove anything that violates your deployment boundary.
3. Read the “main cost” column carefully. It is usually more important than the feature list.

## Three Things Not To Mix Up

- A framework is not the same thing as a finished agent.
- Feature support is not the same thing as primary strength.
- Operating cost is part of the product.