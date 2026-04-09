# AI Agent Map

[![ZH](https://img.shields.io/badge/ZH-CURRENT-1f6feb?style=for-the-badge)](README.md)
[![EN](https://img.shields.io/badge/EN-English-9ca3af?style=for-the-badge)](../README.md)
[![License](https://img.shields.io/badge/LICENSE-MIT-2f855a?style=for-the-badge)](../LICENSE)
[![Agent](https://img.shields.io/badge/AGENT-MAP-24292f?style=for-the-badge)](agents/README.md)

<p align="center">
	<img src="../assets/banner-ferris-wheel.svg" alt="Illustrated banner showing a small traveler at a crossroads looking at a signpost of AI agents, with roads leading toward several mainstream options" width="100%" />
</p>

AI Agent Map 是一个更偏实用、偏可视化的仓库，用来横向比较主流 AI agent、agent 平台、runtime 和 orchestration 工具。

目标很简单：帮读者更快得到一个靠谱的 shortlist。

## 这个仓库想解决什么

- agent 世界很热闹，但真正帮助选型的内容不多。
- 很多资料会讲理念，却不讲适合什么、不适合什么、代价是什么。
- 大多数人需要的是比较层，不是链接堆。

这个仓库只关注选型：它擅长什么、边界在哪、使用成本是什么。

## 从哪里开始

| 你现在的问题更像什么 | 先看哪里 |
| --- | --- |
| 我要先得到一个候选 shortlist | [agents](agents/README.md) |
| 我的问题是“代码自动化怎么选” | [use-cases/coding-automation.md](use-cases/coding-automation.md) |
| 我已经有候选，想做横向对比 | [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) |
| 我在意审批、记忆、调度、部署这类能力维度 | [capabilities](capabilities/README.md) |

## 先把地图摊开

| 路线 | 代表项目 | 常见使用者 |
| --- | --- | --- |
| 直接执行型 | [Claude Code](agents/claude-code.md), [Codex](agents/codex.md), [Devin](agents/devin.md), [OpenHands](agents/openhands.md) | 想把明确 coding 任务交给 agent 的人 |
| 强审批 / 强控制 | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md) | 想把 review 和节奏控制留在人手里的人 |
| 自建系统 | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md) | 想自己搭 agent 平台的团队 |
| 自托管运行时 | [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md) | 需要长期运行、消息渠道、设备或高控制面的人 |

## 仓库结构

| 目录 | 作用 |
| --- | --- |
| [agents](agents/README.md) | 每个 agent 一页，快速看定位、边界和代价 |
| [use-cases](use-cases/README.md) | 从真实问题出发的选型指南 |
| [comparisons](comparisons/README.md) | 面向真实决策的横向比较 |
| [capabilities](capabilities/README.md) | 统一能力词汇表 |

## 当前已覆盖的主流项目

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [Claude Code](agents/claude-code.md) | 直接执行 | 本地和 IDE 优先的 coding agent |
| [Claude Managed Agents](agents/claude-managed-agents.md) | 自动化 | Anthropic 管理式 / 云端执行工作流映射 |
| [Codex](agents/codex.md) | 直接执行 | 异步委派到云端隔离环境 |
| [GitHub Copilot](agents/github-copilot.md) | 平台 | VS Code + GitHub 里的多表面 agent 平台 |
| [Cline](agents/cline.md) | 强控制执行 | 编辑器内 approval-first coding agent |
| [OpenHands](agents/openhands.md) | 开源执行 | 开源 AI 软件工程 agent |
| [Devin](agents/devin.md) | 托管执行 | 端到端软件工程执行 |
| [Hermes Agent](agents/hermes-agent.md) | 多 agent / 自托管 | 带 memory、skills、gateway 的长期工作环境 |
| [OpenClaw](agents/openclaw.md) | runtime | 多渠道、多设备、本地优先运行层 |
| [LangChain](agents/langchain.md) | 平台 | 快速搭自定义 agent 的高层框架 |
| [LangGraph](agents/langgraph.md) | 平台 | 搭持久化、有状态 agent workflow 的底层框架 |
| [Froge Code](agents/froge-code.md) | review-first 自动化 | 当前按 Automagik Forge 暂定映射 |

## 可以这样开始

如果还不确定从哪里切入，可以先按这些示意路径读一轮，再按自己的场景分支出去。

| 如果你更像这样 | 推荐阅读路径 | 这条路径会帮你回答什么 |
| --- | --- | --- |
| 我想找一个适合日常写代码、长期放在编辑器里的 agent | [Claude Code](agents/claude-code.md) → [GitHub Copilot](agents/github-copilot.md) → [Cline](agents/cline.md) → [use-cases/coding-automation.md](use-cases/coding-automation.md) | 直接执行、编辑器辅助、强审批控制三种路线怎么取舍 |
| 我想把 ticket 交出去，过一会儿再回来验收 | [Codex](agents/codex.md) → [Devin](agents/devin.md) → [Claude Managed Agents](agents/claude-managed-agents.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | 云端异步委派和托管执行有什么差别 |
| 我需要开源、自托管或者更强控制面 | [OpenHands](agents/openhands.md) → [Hermes Agent](agents/hermes-agent.md) → [OpenClaw](agents/openclaw.md) → [capabilities](capabilities/README.md) | 开源执行、runtime 控制、部署方式的取舍 |
| 我不是买产品，而是要搭自己的 agent 体系 | [LangChain](agents/langchain.md) → [LangGraph](agents/langgraph.md) → [capabilities](capabilities/README.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | framework、runtime、product 三者边界怎么分 |