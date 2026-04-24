# Agents

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](README.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/README.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

这里不是“agent 名单墙”。

这里更像 shortlist：先帮你看懂路线，再决定要不要点进具体页面。

## 先按路线找

| 路线 | 代表项目 | 适合谁 |
| --- | --- | --- |
| 直接执行 | [Claude Code](claude-code.md), [Aider](aider.md), [Codex](codex.md), [Devin](devin.md), [Jules](jules.md), [OpenHands](openhands.md) | 想直接把 coding 任务交给 agent |
| 前沿 agentic 模型 | [GPT-5.5](gpt-5.5.md) | 在选要接入自己 agent 系统的模型，或在评估 OpenAI 系 agent 能力上限 |
| 工作流 / orchestration layer | [oh-my-claudecode](oh-my-claudecode.md), [oh-my-codex](oh-my-codex.md) | 已经在用 Claude Code 或 Codex，只想补强 teams、skills 和持久工作流 |
| 编辑器中心工作流 | [Cursor](cursor.md), [Windsurf](windsurf.md), [Continue](continue.md) | 想让编辑器本身成为 agent 主表面 |
| review-first 自动化 | [Cline](cline.md), [GitHub Copilot](github-copilot.md), [Froge Code](froge-code.md) | 想把 review 和人工节奏留在核心 |
| 通用自主 agent | [AutoGPT](autogpt.md) | 想用可视化方式搭建通用自主任务 agent |
| 自建平台 | [LangChain](langchain.md), [LangGraph](langgraph.md), [CrewAI](crewai.md), [LlamaIndex](llamaindex.md) | 想自己搭 agent system |
| 运行时 & 工具 | [n8n](n8n.md), [MemGPT](memgpt.md) | 需要带 AI agent 的工作流自动化，或有状态 agent 持久记忆 |
| 自托管 / 本地 runtime | [AI Edge Gallery](ai-edge-gallery.md), [Goose](goose.md), [Hermes Agent](hermes-agent.md), [OpenClaw](openclaw.md) | 需要端侧隐私、本地控制、扩展、渠道或更深的 runtime ownership |
| 管理式后台路径 | [Claude Managed Agents](claude-managed-agents.md) | 需要云端、定时、后台执行 |

## 近期热门快照

这不是质量排行榜。

它只是把 2026 年 4 月下旬 GitHub 热门快照里特别热的项目先摆出来。顺序沿用那张快照，下面的 star 总数则是这次更新目录时重新核对过的当前值。

| 排名 | 项目 | 当前 stars | 快照增量 | 目录状态 | 备注 |
| --- | --- | --- | --- | --- | --- |
| #1 | [Hermes Agent](hermes-agent.md) | 113.0k | +57,100 | 已收录 profile | 自托管多 agent 环境，增长爆发式 |
| #2 | [OpenScreen](https://github.com/siddharthvaddem/openscreen) | 32.4k | +4,500 | 不收录 | 仍然热门，但本质上是录屏 / 演示工具，不是 agent |
| #3 | [oh-my-codex](oh-my-codex.md) | 25.3k | +4,400 | 已收录 profile | 围绕 Codex 的高热度工作流和 orchestration layer |
| #4 | [oh-my-claudecode](oh-my-claudecode.md) | 31.0k | +3,400 | 已收录 profile | 围绕 Claude Code 的高热度工作流和 orchestration layer |
| #5 | [AI Edge Gallery](ai-edge-gallery.md) | 21.9k | +1,600 | 已收录，但附带范围说明 | 更适合被理解成端侧 assistant 沙盒，而不是 coding-first agent |

**市场事件（2026-04-23）：** OpenAI 发布了 [GPT-5.5](gpt-5.5.md)——不是 GitHub 热门仓库，而是直接抬高了 Codex、ChatGPT 和所有基于 OpenAI API 的 agent 能力天花板的模型发布。详见 [GPT-5.5 profile](gpt-5.5.md)。

## 当前已收录

| 项目 | 分类 | 开源 | 一句话定位 | 状态 |
| --- | --- | --- | --- | --- |
| [Aider](aider.md) | execution | 是 | 终端优先、带强 git loop 的 AI 结对编程 | 已核验 |
| [Claude Code](claude-code.md) | execution | 否 | 本地和 IDE 优先的 coding agent | 已核验 |
| [Claude Managed Agents](claude-managed-agents.md) | automation | 否 | Anthropic 管理式 / 云端执行工作流映射 | 已注明映射关系 |
| [Codex](codex.md) | execution | 否 | ChatGPT 内的云端软件工程 agent | 已按当前产品边界核验 |
| [oh-my-claudecode](oh-my-claudecode.md) | multi-agent | 是 | Claude Code 之上的工作流和 orchestration layer | 已核验，附带包名说明 |
| [oh-my-codex](oh-my-codex.md) | multi-agent | 是 | Codex CLI 之上的工作流和 orchestration layer | 已核验 |
| [Cursor](cursor.md) | platform | 否 | 覆盖本地编码、集成和后台 agent 的 AI 编辑器 | 已核验 |
| [GitHub Copilot](github-copilot.md) | platform | 否 | VS Code / GitHub 里的多表面 agent 平台 | 已核验 |
| [Cline](cline.md) | execution | 是 | approval-first 编辑器内 coding agent | 已核验 |
| [Windsurf](windsurf.md) | platform | 否 | 以 Cascade 为中心的 AI 原生 IDE | 已核验 |
| [OpenHands](openhands.md) | execution | 是 | 开源 AI 软件工程 agent | 已核验 |
| [Devin](devin.md) | execution | 否 | 托管式端到端软件工程执行 | 已核验 |
| [Jules](jules.md) | automation | 否 | Google 托管、带 GitHub 和 PR 流程的云端 coding agent | 已按当前文档核验 |
| [AI Edge Gallery](ai-edge-gallery.md) | platform | 是 | 带 agent skills 和 mobile actions 的端侧本地 assistant 沙盒 | 已核验，附带范围说明 |
| [Goose](goose.md) | platform | 是 | 跨 desktop、CLI 和 API 的可扩展本地 agent | 已核验 |
| [Hermes Agent](hermes-agent.md) | multi-agent | 是 | 自托管 memory + skills + subagents 环境 | 已核验 |
| [OpenClaw](openclaw.md) | platform | 是 | 多渠道、多设备、本地优先 runtime | 已核验 |
| [LangChain](langchain.md) | platform | 是 | 快速搭自定义 agent 的高层框架 | 已核验 |
| [LangGraph](langgraph.md) | platform | 是 | 长期运行、有状态 agent workflow 的底层框架 | 已核验 |
| [Continue](continue.md) | platform | 是 | 支持自选模型的开源 IDE 扩展 | 已核验 |
| [GPT-5.5](gpt-5.5.md) | model / agentic | 否 | 驱动 Codex、ChatGPT 和 API 的前沿 agentic 模型 | 已按发布材料核验 |
| [AutoGPT](autogpt.md) | autonomous | 是 | 可视化 agent 搭建平台，带工作流和市场 | 已核验 |
| [CrewAI](crewai.md) | multi-agent | 是 | 角色型多 agent 编排框架 | 已核验 |
| [LlamaIndex](llamaindex.md) | platform | 是 | 数据优先的 RAG 与 agent 框架 | 已核验 |
| [n8n](n8n.md) | runtime / tools | Fair-code | 带原生 AI agent 节点的可视化工作流自动化 | 已核验 |
| [MemGPT](memgpt.md) | runtime / tools | 是 | 带持久记忆的有状态 agent（现名 Letta） | 已核验 |
| [Froge Code](froge-code.md) | automation | 是 | 当前映射为 Automagik Genie | 对外命名仍在演进 |

## 写法标准

统一写法见 [evaluation-framework.md](evaluation-framework.md)。

## 命名说明

如果项目名称、定位或官方公开边界本身就有歧义，这个目录会直接把歧义写出来，而不是假装已经核验清楚。