# Mainstream Agent Landscape

中文：
这不是排行榜，而是一个帮助你快速定位主流 agent 项目的选型矩阵。每一行回答的是“它最适合拿来解决什么问题”，而不是“谁更强”。

English:
This is not a leaderboard. It is a selection matrix for mainstream agent projects. Each row answers what problem the system is best suited to solve, not which one is universally strongest.

## 一页式选型矩阵 | One-Page Selection Matrix

| Agent | Type | Deployment posture | Best for | Main trade-off |
| --- | --- | --- | --- | --- |
| [Claude Code](../agents/claude-code.md) | Local-first coding agent | Managed product across terminal, IDE, desktop, web | Tight local coding workflows with MCP, instructions, and subagents | Less ideal for fully detached background-only execution |
| [Claude Managed Agents](../agents/claude-managed-agents.md) | Managed automation surface | Managed / programmable Anthropic execution paths | Scheduled, background, or embedded Claude agent workflows | Product boundary is spread across several Anthropic concepts |
| [Codex](../agents/codex.md) | Cloud coding agent | Managed cloud plus CLI / IDE surfaces | Async coding delegation in isolated environments | Less editor-native and more asynchronous |
| [GitHub Copilot](../agents/github-copilot.md) | Agent platform | VS Code local, CLI, cloud, third-party | GitHub and VS Code centered local-to-cloud handoff | Best inside Microsoft / GitHub tooling |
| [Cline](../agents/cline.md) | Approval-first coding agent | Local editor and terminal workflows | Powerful coding automation with explicit approvals | Approval overhead is part of the cost |
| [OpenHands](../agents/openhands.md) | Open-source SWE agent | Self-hosted, cloud, enterprise | Open-source AI-driven development with multiple operating modes | Heavier setup and runtime burden |
| [Devin](../agents/devin.md) | Managed SWE executor | Managed cloud product | Direct issue-to-PR style engineering execution | Lower control and self-hosting flexibility |
| [Hermes Agent](../agents/hermes-agent.md) | Self-hosted multi-agent | Self-hosted CLI and gateway | Long-lived agent environment with memory, skills, and delegation | Needs ongoing operational curation |
| [OpenClaw](../agents/openclaw.md) | Runtime / gateway | Local-first self-hosted runtime | Multi-channel, multi-device, tool-rich assistants | Overkill for pure coding automation |
| [LangChain](../agents/langchain.md) | High-level framework | Open-source library | Quickly building custom agents | Less precise for advanced durable orchestration |
| [LangGraph](../agents/langgraph.md) | Low-level orchestration framework | Open-source library | Stateful, durable, approval-heavy agent systems | Highest design and ops burden |
| [Froge Code](../agents/froge-code.md) | Review-first coding automation | Self-hosted platform, mapped to Forge | Task-board-centric coding automation and multi-attempt review | Name still needs confirmation |

## 快速判断 | Fast Heuristics

- 想边写边配合：先看 [Claude Code](../agents/claude-code.md) 或 [Cline](../agents/cline.md)。
- 想异步丢任务：先看 [Codex](../agents/codex.md) 或 [Devin](../agents/devin.md)。
- 想要开源可运行系统：先看 [OpenHands](../agents/openhands.md)、[Hermes Agent](../agents/hermes-agent.md) 或 [OpenClaw](../agents/openclaw.md)。
- 想自己搭平台：先看 [LangChain](../agents/langchain.md) 和 [LangGraph](../agents/langgraph.md)。
- 想 review-first：先看 [Froge Code](../agents/froge-code.md) 或 [GitHub Copilot](../agents/github-copilot.md) 的 cloud workflow。

## 读这个矩阵时不要犯的错 | What Not To Do

- 不要把 framework 和成品 agent 放在同一条评价线上。 Do not evaluate frameworks and finished agents on the same axis.
- 不要把“支持某能力”当成“在这个能力上最好”。 Do not confuse feature support with primary strength.
- 不要忽视操作成本。 The operating cost is part of the product.