# Agents

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](README.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/README.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

这里不是“agent 名单墙”。

这里更像 shortlist：先帮你看懂路线，再决定要不要点进具体页面。

## 先按路线找

| 路线 | 代表项目 | 适合谁 |
| --- | --- | --- |
| 直接执行 | [Claude Code](claude-code.md), [Aider](aider.md), [Codex](codex.md), [Pi](pi.md), [DeepSeek-TUI](deepseek-tui.md), [Devin](devin.md), [Jules](jules.md), [OpenHands](openhands.md) | 想直接把 coding 任务交给 agent |
| 前沿 agentic 模型 | [GPT-5.5](gpt-5.5.md) | 在选要接入自己 agent 系统的模型，或在评估 OpenAI 系 agent 能力上限 |
| Agentic skills 框架 | [Superpowers](superpowers.md) | 想要一套方法论 + 可组合 skills 层、能接到 Claude Code、Codex、Cursor 等 agent 之上 |
| 工作流 / orchestration layer | [oh-my-claudecode](oh-my-claudecode.md), [oh-my-codex](oh-my-codex.md), [Ruflo](ruflo.md) | 已经在用 Claude Code 或 Codex，只想补强 teams、skills 和持久工作流（Ruflo 进一步推到跨机器联邦） |
| 编辑器中心工作流 | [Cursor](cursor.md), [Windsurf](windsurf.md), [Continue](continue.md) | 想让编辑器本身成为 agent 主表面 |
| review-first 自动化 | [Cline](cline.md), [GitHub Copilot](github-copilot.md), [Froge Code](froge-code.md) | 想把 review 和人工节奏留在核心 |
| 通用自主 agent | [AutoGPT](autogpt.md), [Agent Zero](agent-zero.md), [BabyAGI](babyagi.md), [Julep](julep.md), [GenericAgent](generic-agent.md), [ml-intern](ml-intern.md) | 想要通用自主任务执行（ml-intern 是 ML 工程取向的特化版） |
| 自建平台 | [LangChain](langchain.md), [LangGraph](langgraph.md), [CrewAI](crewai.md), [LlamaIndex](llamaindex.md), [Haystack](haystack.md), [Semantic Kernel](semantic-kernel.md), [DSPy](dspy.md), [Pydantic AI](pydantic-ai.md) | 想自己搭 agent system |
| 运行时 & 工具 | [n8n](n8n.md), [MemGPT](memgpt.md), [Open Interpreter](open-interpreter.md), [LiteLLM](litellm.md), [Flowise](flowise.md) | 需要工作流自动化、代码执行、LLM 网关或可视化构建器 |
| 自托管 / 本地 runtime | [AI Edge Gallery](ai-edge-gallery.md), [Goose](goose.md), [Hermes Agent](hermes-agent.md), [OpenClaw](openclaw.md), [Mercury Agent](mercury-agent.md) | 需要端侧隐私、本地控制、扩展、渠道或更深的 runtime ownership |
| 管理式后台路径 | [Claude Managed Agents](claude-managed-agents.md) | 需要云端、定时、后台执行 |

## 近期热门快照

这不是质量排行榜。

它只是把最近一周 GitHub 快照里特别热的 agent 项目摆出来。顺序按 7 天增量；下面的 star 总数是这次更新目录时重新核对过的当前值。

> **最后更新：** 2026-05-19 · **快照窗口：** 2026-05-12 → 2026-05-18（7 天增量，估算） · **Star 总数：** 更新时实时核对

项目名链接指向上游 GitHub 仓库。本目录已收录的 profile，在"目录状态"列单独给出链接。

| 排名 | 项目 | 当前 stars | 快照增量 | 目录状态 | 备注 |
| --- | --- | --- | --- | --- | --- |
| #1（新） | [DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | 32.3k | +13,500 | [Profile](deepseek-tui.md)（本周新增） | DeepSeek 原生的终端 coding agent——本快照单周飙升最大 |
| #2（新） | [mattpocock/skills](https://github.com/mattpocock/skills) | 93.3k | +12,000 | 候补 | Matt Pocock 的个人 `.claude/skills` 集——本身不是 agent，但是 skills 浪潮的标志性样本 |
| #3（新） | [openhuman](https://github.com/tinyhumansai/openhuman) | 19.4k | +11,500 | 候补 | 自称"个人 AI 超级智能"的桌面 agent——定位还在收敛 |
| #4（新） | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 25.7k | +9,000 | 不收录 | Anthropic 金融服务行业垂直 SDK——agent 相关，但不是通用 agent 基础设施 |
| #5（新） | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 43.6k | +7,500 | 候补 | Addy Osmani 的 AI coding agent 生产级工程 skills——同一波 skills 浪潮的另一个数据点 |
| #6（新） | [Superpowers](https://github.com/obra/superpowers) | 197.7k | +6,500 | [Profile](superpowers.md)（本周新增） | Jesse Vincent 的 agentic skills 框架——可组合 skills + 对接 Claude Code、Codex、Cursor、GitHub Copilot、Gemini 等的插件 marketplace |
| #7（新） | [Ruflo](https://github.com/ruvnet/ruflo) | 53.0k | +5,500 | [Profile](ruflo.md)（本周新增） | Claude Code 的多 agent 编排平台（前身 Claude Flow）——跨机器联邦、神经记忆、100+ 专用 agent |
| #8（新） | [agentmemory](https://github.com/rohitg00/agentmemory) | 13.6k | +5,000 | 候补 | AI coding agent 的持久记忆层——和 [MemGPT](memgpt.md) 有重叠 |
| #9 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 157.3k | +4,500 | [Profile](hermes-agent.md) | 连续第四周增长——已收录项目里仍是绝对总数最高 |
| #10 | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 77.2k | +4,500 | 不收录 | Tauric Research 的多 agent 金融框架——仍热门，但范围判断不变（仅供研究、垂直领域） |

**市场事件：**
- **2026 年 5 月（本次快照）** —— `.claude/skills` 浪潮：本周热门前 6 中有 3 个是 skills 框架或策展式 skills 仓库（Superpowers、mattpocock/skills、agent-skills）。新写入的 [Superpowers](superpowers.md) profile 覆盖框架那一端。
- **2026-04-08** —— Earendil（Armin Ronacher 的公司）从 Mario Zechner 手中收购 [Pi](pi.md) 项目，仓库从 `badlogic/pi-mono` 迁到 `earendil-works/pi`；Earendil 同时启动云端 agent 平台 Lefos。
- **2026-04-16** —— OpenAI 推出 "Codex for (almost) everything"，在 [Codex](codex.md) 产品表面加入后台 Computer Use、并行多 agent 执行、内置浏览器，以及 90+ plugin。同时披露周活 300 万开发者，约为 3 月初的 2 倍。
- **2026-04-23** —— OpenAI 发布 [GPT-5.5](gpt-5.5.md)，是 Codex、ChatGPT 和所有基于 OpenAI API 的 agent 的底层模型。

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
| [Agent Zero](agent-zero.md) | autonomous | 是 | 自构建自主 agent，动态创建工具 | 已核验 |
| [BabyAGI](babyagi.md) | experimental | 是 | 开创性自主 agent 实验——教学用 | 已核验 |
| [Julep](julep.md) | workflow engine | 是 | Temporal 支撑的持久化有状态 agent 工作流引擎 | 已核验 |
| [Haystack](haystack.md) | platform | 是 | deepset 的生产导向 RAG 和 agent 框架 | 已核验 |
| [Semantic Kernel](semantic-kernel.md) | platform | 是 | 微软 AI 编排 SDK，.NET / Python / Java | 已核验 |
| [DSPy](dspy.md) | platform | 是 | 程序化 prompt 优化框架 | 已核验 |
| [Open Interpreter](open-interpreter.md) | runtime / tools | 是 | 自然语言到本地代码执行 | 已核验 |
| [LiteLLM](litellm.md) | infrastructure | 是 | 100+ LLM provider 的统一 API 网关 | 已核验 |
| [Pydantic AI](pydantic-ai.md) | platform | 是 | 类型安全 Python agent 框架，结构化输出 | 已核验 |
| [Flowise](flowise.md) | runtime / tools | 是 | 拖拽式 LLM 应用和 agent 可视化构建器 | 已核验 |
| [Froge Code](froge-code.md) | automation | 是 | 当前映射为 Automagik Genie | 对外命名仍在演进 |
| [Mercury Agent](mercury-agent.md) | multi-channel runtime | 是 | 权限硬化的 CLI + Telegram 自托管 agent，带 token 预算 | 已按当前仓库核验 |
| [Pi](pi.md) | execution / toolkit | 是 | 极简终端 coding agent harness，多 LLM provider 支持 | 2026-04 被 Earendil 收购后已核验 |
| [ml-intern](ml-intern.md) | autonomous（垂直领域） | 是 | 基于 Hugging Face 生态的自主 ML 工程 agent | 已核验 |
| [GenericAgent](generic-agent.md) | autonomous（自演进） | 是 | 从小种子起步、每完成任务长 skill tree 的自主 agent | 候补 2 周后已核验 |
| [Superpowers](superpowers.md) | skills 框架 / 方法论 | 是 | 可组合 agentic skills 框架，集成 Claude Code、Codex、Cursor、Copilot、Gemini | 已按 v5.1（2026-05）核验 |
| [DeepSeek-TUI](deepseek-tui.md) | execution（DeepSeek 原生） | 是 | DeepSeek 原生的终端 coding agent | 已在 2026-05 飙升期核验 |
| [Ruflo](ruflo.md) | 多 agent 编排 | 是 | 跨机器联邦的 Claude 编排平台（前身 Claude Flow） | 改名后已核验 |

## 写法标准

统一写法见 [evaluation-framework.md](evaluation-framework.md)。

## 命名说明

如果项目名称、定位或官方公开边界本身就有歧义，这个目录会直接把歧义写出来，而不是假装已经核验清楚。