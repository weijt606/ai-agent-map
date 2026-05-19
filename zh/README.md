# AI Agent Map

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](README.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../README.md)
[![License](https://img.shields.io/badge/LICENSE-MIT-16a34a?style=for-the-badge&labelColor=166534)](../LICENSE)
[![Agent](https://img.shields.io/badge/AGENT-MAP-d97706?style=for-the-badge&labelColor=92400e)](agents/README.md)

<p align="center">
	<img src="../assets/ai-agent-map-pixel-zh.png" alt="像素风格的 AI Agent Map 主视觉，展示四大区域——日常编程 Agent、通用自主任务 Agent、框架与平台、运行时与工具——agent 图标分布在宝藏地图风格的插画场景中" width="100%" />
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
| 我要先得到一个候选 shortlist | [![进入 Agents](https://img.shields.io/badge/%E8%BF%9B%E5%85%A5-Agents-d97706?style=for-the-badge&labelColor=92400e)](agents/README.md) |
| 我的问题是“代码自动化怎么选” | [![阅读 代码自动化](https://img.shields.io/badge/%E9%98%85%E8%AF%BB-%E4%BB%A3%E7%A0%81%E8%87%AA%E5%8A%A8%E5%8C%96-2563eb?style=for-the-badge&labelColor=1d4ed8)](use-cases/coding-automation.md) |
| 我已经有候选，想做横向对比 | [![查看 主流矩阵](https://img.shields.io/badge/%E6%9F%A5%E7%9C%8B-%E4%B8%BB%E6%B5%81%E7%9F%A9%E9%98%B5-dc2626?style=for-the-badge&labelColor=991b1b)](comparisons/mainstream-agent-landscape.md) |
| 我在意审批、记忆、调度、部署这类能力维度 | [![浏览 能力维度](https://img.shields.io/badge/%E6%B5%8F%E8%A7%88-%E8%83%BD%E5%8A%9B%E7%BB%B4%E5%BA%A6-16a34a?style=for-the-badge&labelColor=166534)](capabilities/README.md) |

## 近期热门榜

热度不等于适合度。

这张表记录的是最近一周 GitHub 快照里特别热的 agent 项目。排名按 7 天增量。下面的总 star 数是这次更新仓库时重新核对过的当前值。

> **最后更新：** 2026-05-19 · **快照窗口：** 2026-05-12 → 2026-05-18（7 天增量，估算） · **Star 总数：** 更新时实时核对

项目名链接指向上游 GitHub 仓库。本仓库已写入的 profile，在"在本仓库中的状态"列单独给出链接。

| 排名 | 项目 | 当前 stars | 快照增量 | 在本仓库中的状态 | 应该怎么读 |
| --- | --- | --- | --- | --- | --- |
| #1（新） | [DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | 32.3k | +13,500 | 已收录 · [profile](agents/deepseek-tui.md)（本次新增） | DeepSeek 原生的终端 coding agent——本周单周飙升最大，也是目录里第一个围绕 DeepSeek 模型生态搭的条目 |
| #2（新） | [mattpocock/skills](https://github.com/mattpocock/skills) | 93.3k | +12,000 | 候补 | Matt Pocock 的 `.claude/skills` 个人技能集——本身不是 agent，但是 skills 浪潮的标志性样本（详见下方市场事件） |
| #3（新） | [openhuman](https://github.com/tinyhumansai/openhuman) | 19.4k | +11,500 | 候补 | 自称"个人 AI 超级智能"的桌面 agent——定位还在收敛，1-2 周后再决定要不要单独写 profile |
| #4（新） | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 25.7k | +9,000 | 不收录 | Anthropic 给金融服务行业出的垂直 SDK——agent 相关，但本质是行业加速包，不是通用 agent 表面 |
| #5（新） | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 43.6k | +7,500 | 候补 | Addy Osmani 整理的生产级工程 skills——同一波 skills 浪潮的又一个数据点 |
| #6（新） | [Superpowers](https://github.com/obra/superpowers) | 197.7k | +6,500 | 已收录 · [profile](agents/superpowers.md)（本次新增） | Jesse Vincent 主导的 agentic skills 框架 + 方法论——可组合 skills，加上对接 Claude Code、Codex、Cursor、GitHub Copilot、Gemini 等的插件 marketplace |
| #7（新） | [Ruflo](https://github.com/ruvnet/ruflo) | 53.0k | +5,500 | 已收录 · [profile](agents/ruflo.md)（本次新增） | Claude Code 的多 agent 编排平台（前身 Claude Flow）——跨机器联邦、100+ 专用 agent、神经记忆 |
| #8（新） | [agentmemory](https://github.com/rohitg00/agentmemory) | 13.6k | +5,000 | 候补 | AI coding agent 的持久记忆层——和 [MemGPT](agents/memgpt.md) 有重叠；如果下周仍持续涨再考虑写 profile |
| #9 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 157.3k | +4,500 | 已收录 · [profile](agents/hermes-agent.md) | 自托管多 agent 环境——连续第四周增长，绝对总数已突破 157k |
| #10 | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 77.2k | +4,500 | 不收录 | Tauric Research 的多 agent 金融框架——仍然热门，但范围判断不变：垂直领域、仅供研究 |

- 热度适合拿来发现新项目，不适合直接当选型顺序。
- 本次新增三个 in-scope profile：[Superpowers](agents/superpowers.md)、[DeepSeek-TUI](agents/deepseek-tui.md)、[Ruflo](agents/ruflo.md)。每一个都是此前 map 没覆盖的路线代表（skills 框架/方法论、DeepSeek 原生终端 agent、跨机器联邦式编排）。
- `mattpocock/skills` 和 `addyosmani/agent-skills` 故意放候补而非写 profile：精心整理的 `.claude/skills` 目录本质是"内容资产"，不是 agent 表面——底层的 skills 范式通过 [Superpowers](agents/superpowers.md) 这条 profile 已经覆盖了。
- `openhuman` 和 `agentmemory` 再观察一周；定位稳定后再决定要不要写 profile。
- `anthropics/financial-services` 故意不收录：Anthropic 在主力 agent 平台之外开始出垂直 SDK，但本仓库只追踪通用 agent 基础设施。趋势本身（"agent 厂商走垂直化"）值得记下，但 repo 本身不进 map。
- Codex CLI（83.7k，~+2.3k）、Pi（51.5k，~+3.0k）、oh-my-claudecode（34.3k，~+1.4k）、GenericAgent（11.8k，~+1.5k）、ml-intern（9.6k，~+0.7k）本周仍在涨但都被 skills 浪潮和 DeepSeek-TUI 挤出了前 10。

## 市场事件：`.claude/skills` 浪潮（2026 年 5 月）

在 2026-05-12 → 18 这次快照里，本周 GitHub 热门前 6 名里有 3 个是 `.claude/skills` 风格的 skills 仓库或基于 Anthropic skill 模式搭建的框架：

| 仓库 | Stars | 形态 |
| --- | --- | --- |
| [Superpowers](agents/superpowers.md) | 197.7k | 一整套 skills 框架 + 方法论，并通过 plugin 集成到 Claude Code、Codex、Cursor、GitHub Copilot、Gemini、OpenCode、Factory Droid |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 93.3k | Matt Pocock 的个人 `.claude/skills` 目录——18 个 skills，覆盖工程、生产力和杂项 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 43.6k | Addy Osmani 整理的 AI coding agent 生产级工程 skills |

这对选型意味着什么：

- Anthropic 引入的 `.claude/skills` 目录范式已经从"好奇心试水"变成"共享基础设施"——工程师现在把自己的 skill 库公开发布，就像以前公开 dotfiles 一样。
- 对正在选 coding agent 的人来说，底层 agent 本身的重要性比半年前下降了——堆在上面的 skill 层在做更多工作。
- 本仓库现在把"agentic skills 框架"作为一条独立路线，对应新写入的 [Superpowers](agents/superpowers.md) profile。纯粹的策展式 skill 合集（`mattpocock/skills`、`addyosmani/agent-skills`）作为候补条目跟踪，不单独写 profile，因为它们是内容资产、不是 agent 表面。

## 市场事件：GPT-5.5 进入 Agent 版图

2026 年 4 月 23 日，OpenAI 发布了 [GPT-5.5](agents/gpt-5.5.md)——定位是”a new class of intelligence for real work and powering agents”。这不是一个 GitHub 热门仓库，而是一次直接抬高多个已有 agent 表面能力上限的模型发布。

| 变了什么 | 对本仓库的影响 |
| --- | --- |
| Terminal-Bench 2.0 得分 82.7% | 发布时 agentic coding benchmark 最高——抬高了 Codex 和所有基于 OpenAI API 的 agent 上限 |
| 百万 token 上下文窗口 | 之前不现实的长上下文任务，现在对 API 搭 agent 的团队变得可行 |
| API 价格是 GPT-5.4 的 2 倍 | 对成本敏感的团队需要重新 benchmark 每任务成本 |
| SWE-Bench Pro 58.6% | 仍落后于 Claude Opus 4.7（64.3%）——选模型要看工作负载 |

GPT-5.5 不取代 [Codex](agents/codex.md) 作为产品条目，它是底层模型。详见 [GPT-5.5 profile](agents/gpt-5.5.md)。

### Codex 产品更新（2026-04-16）

GPT-5.5 发布前一周，OpenAI 先推出了 "Codex for (almost) everything"——在 [Codex](agents/codex.md) 这个产品表面本身做了重大能力扩展。

| 变了什么 | 为什么重要 |
| --- | --- |
| 后台 Computer Use | Codex 用自己的鼠标和键盘操作任意 macOS 应用，包括没有 API 的应用 |
| 并行多 agent 执行 | 多个 Codex agent 可以在同一台 Mac 上并行运行，不打扰前台工作 |
| 90+ 新 plugin | Atlassian Rovo、CircleCI、CodeRabbit、GitLab Issues、Microsoft Suite 等 |
| 内置浏览器 + 主动建议 | 直接在 app 内迭代前端设计，并基于项目上下文和记忆主动建议工作 |
| 周活 300 万开发者 | 2026 年 4 月数据，几乎是 3 月初的两倍 |

叠加 GPT-5.5 底层模型，这是这次快照窗口里影响最大的一次 agent 产品更新。

## 先把地图摊开

| 路线 | 代表项目 | 常见使用者 |
| --- | --- | --- |
| 直接执行型 | [Claude Code](agents/claude-code.md), [Aider](agents/aider.md), [Codex](agents/codex.md), [Pi](agents/pi.md), [DeepSeek-TUI](agents/deepseek-tui.md), [Devin](agents/devin.md), [Jules](agents/jules.md), [OpenHands](agents/openhands.md) | 想把明确 coding 任务交给 agent 的人 |
| 前沿 agentic 模型 | [GPT-5.5](agents/gpt-5.5.md) | 在选要接入自己 agent 系统的模型，或在评估 OpenAI 系 agent 能力上限的人 |
| Agentic skills 框架 | [Superpowers](agents/superpowers.md) | 想要一套方法论 + 可组合 skills 层、能接到 Claude Code、Codex、Cursor 等 agent 之上的人 |
| 工作流 / orchestration layer | [oh-my-claudecode](agents/oh-my-claudecode.md), [oh-my-codex](agents/oh-my-codex.md), [Ruflo](agents/ruflo.md) | 已经认可 Claude Code 或 Codex，只想在上面补强 orchestration 的人（Ruflo 把这条进一步推到跨机器联邦和 100+ 专用 agent） |
| 编辑器中心工作流 | [Cursor](agents/cursor.md), [Windsurf](agents/windsurf.md), [Continue](agents/continue.md) | 想让编辑器本身保持在工作流核心的人 |
| review-first 自动化 | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md) | 想把 review 和人工控制留在核心的人 |
| 管理式后台路径 | [Claude Managed Agents](agents/claude-managed-agents.md) | 需要 Anthropic 的定时、云端或后台工作流的人 |
| 通用自主 agent | [AutoGPT](agents/autogpt.md), [Agent Zero](agents/agent-zero.md), [BabyAGI](agents/babyagi.md), [Julep](agents/julep.md), [GenericAgent](agents/generic-agent.md), [ml-intern](agents/ml-intern.md) | 想要通用自主任务执行的人（ml-intern 是 ML 工程取向的特化版本） |
| 自建系统 | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md), [Haystack](agents/haystack.md), [Semantic Kernel](agents/semantic-kernel.md), [DSPy](agents/dspy.md), [Pydantic AI](agents/pydantic-ai.md) | 想自己搭 agent 平台的团队 |
| 运行时 & 工具 | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md) | 需要工作流自动化、代码执行、LLM 网关或可视化构建器的团队 |
| 自托管 / 本地 runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md) | 需要端侧隐私、长期运行、本地控制、渠道或设备能力的人 |

## 仓库结构

| 目录 | 作用 |
| --- | --- |
| [![进入 Agents](https://img.shields.io/badge/%E8%BF%9B%E5%85%A5-Agents-d97706?style=for-the-badge&labelColor=92400e)](agents/README.md) | 每个 agent 一页，快速看定位、边界和代价 |
| [![进入 用例](https://img.shields.io/badge/%E8%BF%9B%E5%85%A5-%E7%94%A8%E4%BE%8B-2563eb?style=for-the-badge&labelColor=1d4ed8)](use-cases/README.md) | 从真实问题出发的选型指南 |
| [![进入 对比](https://img.shields.io/badge/%E8%BF%9B%E5%85%A5-%E5%AF%B9%E6%AF%94-dc2626?style=for-the-badge&labelColor=991b1b)](comparisons/README.md) | 面向真实决策的横向比较 |
| [![进入 能力](https://img.shields.io/badge/%E8%BF%9B%E5%85%A5-%E8%83%BD%E5%8A%9B-16a34a?style=for-the-badge&labelColor=166534)](capabilities/README.md) | 统一能力词汇表 |

## 当前已覆盖的主流项目

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [Aider](agents/aider.md) | 直接执行 | 终端优先、贴近 git 的 AI 结对编程 |
| [Claude Code](agents/claude-code.md) | 直接执行 | 本地和 IDE 优先的 coding agent |
| [Claude Managed Agents](agents/claude-managed-agents.md) | 管理式后台路径 | Anthropic 管理式 / 云端执行工作流映射 |
| [Codex](agents/codex.md) | 直接执行 | 异步委派到云端隔离环境 |
| [oh-my-claudecode](agents/oh-my-claudecode.md) | 工作流层 | Claude Code 之上的 teams-first orchestration layer |
| [oh-my-codex](agents/oh-my-codex.md) | 工作流层 | 为 Codex CLI 增强工作流、teams 和持久状态 |
| [Cursor](agents/cursor.md) | 编辑器中心平台 | 覆盖本地编码、云端 agent 和集成的 AI 编辑器 |
| [GitHub Copilot](agents/github-copilot.md) | 平台 | VS Code + GitHub 里的多表面 agent 平台 |
| [Cline](agents/cline.md) | review-first 执行 | 编辑器内 approval-first coding agent |
| [Windsurf](agents/windsurf.md) | AI 原生 IDE | 以 Cascade 为中心的 AI IDE |
| [OpenHands](agents/openhands.md) | 开源执行 | 开源 AI 软件工程 agent |
| [Devin](agents/devin.md) | 托管执行 | 端到端软件工程执行 |
| [Jules](agents/jules.md) | 托管云端执行 | GitHub 连接、PR 回收的 coding delegation |
| [AI Edge Gallery](agents/ai-edge-gallery.md) | 端侧本地 runtime | 带 agent skills 的移动端本地 assistant 沙盒 |
| [Goose](agents/goose.md) | 开源本地平台 | 跨 desktop、CLI、API 的可扩展本地 agent |
| [Hermes Agent](agents/hermes-agent.md) | 多 agent / 自托管 | 带 memory、skills、gateway 的长期工作环境 |
| [OpenClaw](agents/openclaw.md) | runtime | 多渠道、多设备、本地优先运行层 |
| [LangChain](agents/langchain.md) | 平台 | 快速搭自定义 agent 的高层框架 |
| [LangGraph](agents/langgraph.md) | 平台 | 搭持久化、有状态 agent workflow 的底层框架 |
| [Continue](agents/continue.md) | 编辑器中心 | 支持自选模型的开源 IDE 扩展 |
| [GPT-5.5](agents/gpt-5.5.md) | 前沿 agentic 模型 | 驱动 Codex、ChatGPT 和 API 的 OpenAI agentic 模型 |
| [AutoGPT](agents/autogpt.md) | 自主 agent 平台 | 可视化 agent 构建器，带工作流、市场和多模型支持 |
| [CrewAI](agents/crewai.md) | 多 agent 框架 | 角色型 agent 协作，快速搭原型 |
| [LlamaIndex](agents/llamaindex.md) | 数据优先框架 | 基于文档和数据的 RAG 与 agentic 应用 |
| [n8n](agents/n8n.md) | 工作流自动化 | 带原生 AI agent 节点和 400+ 集成的可视化工作流平台 |
| [MemGPT](agents/memgpt.md) | 有状态 agent 平台 | 跨会话学习的持久记忆 agent（现名 Letta） |
| [Agent Zero](agents/agent-zero.md) | 自主 agent | 自构建自主 agent，动态创建工具 |
| [BabyAGI](agents/babyagi.md) | 实验性 | 开创性自主 agent 实验——教学用，非生产 |
| [Julep](agents/julep.md) | 工作流引擎 | Temporal 支撑的持久化有状态 AI agent 工作流引擎 |
| [Haystack](agents/haystack.md) | 框架 | deepset 的生产导向 RAG 和 agent 框架 |
| [Semantic Kernel](agents/semantic-kernel.md) | 框架 | 微软的 AI 编排 SDK，支持 .NET、Python、Java |
| [DSPy](agents/dspy.md) | 框架 | 程序化 prompt 优化——编程而非手调 LM |
| [Open Interpreter](agents/open-interpreter.md) | 运行时 | 自然语言到本地代码执行，无沙盒 |
| [LiteLLM](agents/litellm.md) | 基础设施 | 100+ LLM provider 的统一 API 网关 |
| [Pydantic AI](agents/pydantic-ai.md) | 框架 | 类型安全 Python agent 框架，结构化输出 |
| [Flowise](agents/flowise.md) | 可视化构建器 | 基于 LangChain 的拖拽式 LLM 应用和 agent 构建器 |
| [Froge Code](agents/froge-code.md) | review-first 自动化 | 当前按 Automagik Genie 暂定映射 |
| [Mercury Agent](agents/mercury-agent.md) | 自托管多通道 | 主打 CLI + Telegram 的权限硬化 agent，带 token 预算 |
| [Pi](agents/pi.md) | 直接执行 | 极简终端 coding agent harness，多 LLM provider 支持 |
| [ml-intern](agents/ml-intern.md) | 垂直领域自主 agent | Hugging Face 的自主 ML 工程师——基于 HF 生态做研究、写代码、发布 ML 成果 |
| [GenericAgent](agents/generic-agent.md) | 自演进自主 agent | 从小种子起步、每完成任务长出 skill tree 的自主 agent |
| [Superpowers](agents/superpowers.md) | Agentic skills 框架 | 一整套方法论 + 可组合 skills 层，可接到 Claude Code、Codex、Cursor 等 agent 之上 |
| [DeepSeek-TUI](agents/deepseek-tui.md) | 直接执行 | DeepSeek 原生的终端 coding agent |
| [Ruflo](agents/ruflo.md) | 工作流 / orchestration layer | 面向 Claude 的多 agent 编排平台，支持跨机器联邦、神经记忆和 100+ 专用 agent |

## 可以这样开始

如果还不确定从哪里切入，可以先按这些示意路径读一轮，再按自己的场景分支出去。

| 如果你更像这样 | 推荐阅读路径 | 这条路径会帮你回答什么 |
| --- | --- | --- |
| 我想找一个日常 coding agent，但还没想清楚终端还是编辑器 | [Aider](agents/aider.md) → [Claude Code](agents/claude-code.md) → [Cursor](agents/cursor.md) → [Cline](agents/cline.md) → [use-cases/coding-automation.md](use-cases/coding-automation.md) | 终端优先、本地协作、编辑器中心、强审批控制怎么取舍 |
| 我已经喜欢 Claude Code 或 Codex，但想补强 orchestration | [Claude Code](agents/claude-code.md) → [oh-my-claudecode](agents/oh-my-claudecode.md) → [Codex](agents/codex.md) → [oh-my-codex](agents/oh-my-codex.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | 底层 agent 够不够用，什么时候值得再加一层工作流 |
| 我想搞清楚 GPT-5.5 对 agent 版图到底意味着什么 | [GPT-5.5](agents/gpt-5.5.md) → [Codex](agents/codex.md) → [Claude Code](agents/claude-code.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | 前沿模型发布怎样抬高能力天花板，又怎样影响产品选型 |
| 我想要专用 AI IDE，而不是继续拼装工具 | [Cursor](agents/cursor.md) → [Windsurf](agents/windsurf.md) → [GitHub Copilot](agents/github-copilot.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | AI 原生编辑器和生态型平台怎么区分 |
| 我想把 ticket 交出去，过一会儿再回来验收 | [Codex](agents/codex.md) → [Jules](agents/jules.md) → [Devin](agents/devin.md) → [Claude Managed Agents](agents/claude-managed-agents.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | 异步云端委派和管理式后台自动化有什么差别 |
| 我需要开源、自托管或者更强本地控制面 | [Aider](agents/aider.md) → [OpenHands](agents/openhands.md) → [Goose](agents/goose.md) → [Hermes Agent](agents/hermes-agent.md) → [capabilities](capabilities/README.md) | 终端控制、开源执行和本地运行控制面的取舍 |
| 我不是买产品，而是要搭自己的 agent 体系 | [LangChain](agents/langchain.md) → [LangGraph](agents/langgraph.md) → [capabilities](capabilities/README.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | framework、runtime、product 三者边界怎么分 |

## 免责声明

表格里的 star 数和 7 天增量，都是仓库更新时点抓取的 GitHub 快照；不同周次之间会出现波动，少量取整误差也是正常的。每个项目的描述、厂商和能力总结，反映的是写作时点的公开信息，可能因项目演进、被收购、转型而过时。本仓库提供的是**选型参考**，不是背书、不是投资建议、也不是生产可用性保证。最终决策前请以各项目自己的官方文档为准。