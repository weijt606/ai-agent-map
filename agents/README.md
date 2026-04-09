# Agents

中文：
这个目录收录独立的 agent 页面。每个页面都遵循同一套评估框架，重点写能力边界、适用场景、反向适配和复杂度，而不是简单摘抄项目介绍。

English:
This directory contains standalone agent pages. Each page follows the same evaluation framework, focusing on capability boundaries, fit, anti-fit, and complexity rather than copied product summaries.

## 当前条目 | Current Profiles

| Agent | Category | Open Source | Best Fit | Status |
| --- | --- | --- | --- | --- |
| [Claude Code](claude-code.md) | execution | No | IDE and terminal-first coding automation | Verified public positioning |
| [Claude Managed Agents](claude-managed-agents.md) | automation | No | Managed and cloud-style Claude task execution | Mapped from current Anthropic docs |
| [Codex](codex.md) | execution | Mixed | Cloud task delegation with isolated environments | Verified public positioning |
| [GitHub Copilot](github-copilot.md) | platform | No | Multi-surface agent workflows in VS Code and GitHub | Verified public positioning |
| [Cline](cline.md) | execution | Yes | Approval-first editor-native coding agent | Verified public project |
| [OpenHands](openhands.md) | execution | Yes | Self-hosted or hosted AI-driven development agent | Verified public project |
| [Devin](devin.md) | execution | No | Direct software engineering execution | Verified public positioning |
| [OpenClaw](openclaw.md) | platform | Yes | Local-first runtime with tools, channels, and routing | Verified public project |
| [Hermes Agent](hermes-agent.md) | multi-agent | Yes | Self-hosted CLI and messaging agent with memory and delegation | Verified public project |
| [LangChain](langchain.md) | platform | Yes | Fast path to building custom agents on top of LangGraph | Verified public project |
| [Froge Code](froge-code.md) | automation | Yes | Review-first coding automation orchestration | Name needs confirmation |
| [LangGraph](langgraph.md) | platform | Yes | Build custom stateful agent systems | Verified public project |

## 覆盖说明 | Coverage Notes

中文：
这个目录的策略是先覆盖高频选型对象，再继续扩到更多细分 agent。当前优先覆盖的是 coding agents、managed agents、self-hosted runtimes 和主流 orchestration frameworks。

English:
The current strategy is to cover the most common decision targets first, then expand into more specialized agents. The current priority areas are coding agents, managed agents, self-hosted runtimes, and mainstream orchestration frameworks.

## 评估框架 | Evaluation Framework

统一结构见 [evaluation-framework.md](evaluation-framework.md)。

The shared structure lives in [evaluation-framework.md](evaluation-framework.md).

## 命名说明 | Naming Notes

中文：
如果一个条目的公开名称存在歧义，本仓库不会强行“猜对”，而是会保留显式的核验说明。这比写出错误结论更有价值。

English:
If a project name is publicly ambiguous, the repository keeps an explicit verification note instead of pretending the name has been resolved. That is more useful than a confident but wrong profile.