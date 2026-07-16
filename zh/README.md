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
| 我想看存量排行和每周趋势图 | [![查看 排行](https://img.shields.io/badge/%E6%9F%A5%E7%9C%8B-%E6%8E%92%E8%A1%8C-7c3aed?style=for-the-badge&labelColor=5b21b6)](rankings/README.md) |
| 我想看问题导向的指南或全部对比页 | [用例](use-cases/README.md) · [对比](comparisons/README.md) |

## 近期热门榜

热度不等于适合度。

这张表记录的是最近一周 GitHub 快照里特别热的 agent 项目。排名按 7 天增量。下面的总 star 数是这次更新仓库时重新核对过的当前值。

> **最后更新：** 2026-07-14 · **快照窗口：** 2026-07-08 → 2026-07-14（自上次更新以来的增量，约 6 天，估算） · **Star 总数：** 更新时实时核对

项目名链接指向上游 GitHub 仓库。本仓库已写入的 profile，在"在本仓库中的状态"列单独给出链接。

| 排名 | 项目 | 当前 stars | 快照增量 | 在本仓库中的状态 | 应该怎么读 |
| --- | --- | --- | --- | --- | --- |
| #1&#8288;（=） | [mattpocock/skills](https://github.com/mattpocock/skills) | 168.3k | +7,712 | 候补（Skills 浪潮） | 连续第四个窗口守住增量榜首——Matt Pocock 的 `.claude/skills` 个人技能集越过 168k |
| #2&#8288;（↑） | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 77.9k | +5,052 | 候补（Skills 浪潮） | 上升一位到 #2——Addy Osmani 的 curated agent-skills 集越过 77k |
| #3&#8288;（↓） | [Superpowers](https://github.com/obra/superpowers) | 253.8k | +4,445 | 已收录 · [profile](agents/superpowers.md) | 下滑一位但越过 253k——浪潮的框架锚点持续复利增长 |
| #4&#8288;（=） | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 214.2k | +2,915 | 已收录 · [profile](agents/hermes-agent.md) | 稳守 #4——已收录项目里绝对总数第一，越过 214k |
| #5&#8288;（↑） | [Pi](https://github.com/earendil-works/pi) | 70.5k | +1,907 | 已收录 · [profile](agents/pi.md) | 从 #7 跳升两位——Earendil 接手的 harness 越过 70k |
| #6&#8288;（↓） | [anthropics/skills](https://github.com/anthropics/skills) | 160.9k | +1,490 | 候补（Skills 浪潮源头） | 下滑一位——Anthropic 自家的 `.claude/skills` 参考仓库，上游源头，越过 160k |
| #7&#8288;（↑） | [Codex CLI](https://github.com/openai/codex) | 97.7k | +1,459 | 已收录 · [profile](agents/codex.md) | 从 #9 上升两位——OpenAI 的 Codex CLI 逼近 98k |
| #8&#8288;（↓） | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 59.7k | +1,147 | 已收录 · [profile](agents/codegraph.md) | 降温两位到 #8——预索引代码知识图谱逼近 60k |
| #9&#8288;（↓） | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 92.8k | +1,038 | 不收录 | 垂直的金融研究多 agent 系统下滑一位并越过 92k——总数高、增长稳，但作为领域垂直不收录 |
| #10&#8288;（=） | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 37.7k | +821 | 候补（Skills 浪潮） | 稳守 #10——面向 Claude Code 的学术研究管线越过 37k |

- 热度适合拿来发现新项目，不适合直接当选型顺序。
- 本窗口头条仍是 curated skills 的轮换、无黑马：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 上升一位到 #2（+5.1k，越过 77k），反超滑到 #3 的 [Superpowers](agents/superpowers.md)（越过 253k）。它们上面 [mattpocock/skills](https://github.com/mattpocock/skills) 连续第四个窗口守住 #1 增量位（+7.7k，越过 168k）。下方唯一真正的重排是 [Pi](agents/pi.md) 跳升两位到 #5、[Codex CLI](agents/codex.md) 跳升两位到 #7，把 [anthropics/skills](https://github.com/anthropics/skills) 和 [codegraph](agents/codegraph.md) 挤下去。
- **新收录扫描** 本窗口没有新的达到收录门槛的 agent 表面。最新且体量最大的新仓库是 [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)（7.3k，JavaScript——"loop engineering" 的模式、脚手架与 CLI 工具集）和 [inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)（2.8k，TypeScript——AI 原生的 markdown wiki 编辑器）；两者与仍在涨的 [langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)（10.9k）、[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill)（5.0k）、[vercel/eve](https://github.com/vercel/eve)（3.5k）、[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)（2.6k）、[tigicion/dao-code](https://github.com/tigicion/dao-code)（1.6k）一起留在候补。都还没达到收录门槛。

<details>
<summary>更多窗口笔记：skills 浪潮占比、OpenClaw、以及榜外仍在涨的项目</summary>

- `.claude/skills` 浪潮仍占前 10 的 5 个（`mattpocock/skills`、`addyosmani/agent-skills`、`Superpowers`、`anthropics/skills`、`academic-research-skills`）。策略不变：curated 集合作为 Skills 浪潮条目跟踪，框架那一端通过 [Superpowers](agents/superpowers.md) 覆盖。
- [TradingAgents](https://github.com/TauricResearch/TradingAgents) 下滑到 #9（+1.0k，越过 92k），但作为金融研究垂直不收录；[Codex CLI](agents/codex.md) 升到 #7（逼近 98k）、[Pi](agents/pi.md) 升到 #5（越过 70k）。
- [OpenClaw](agents/openclaw.md) 仍是绝对总数第一，382.8k star（+0.7k）；它已有 profile，但因为这种体量的项目周环比增量噪声太大，不进按增量排名的表。
- 本周仍在涨但没进前 10（按增量）：[Ruflo](agents/ruflo.md) 64.3k（+0.8k）、[scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 30.8k（+0.4k）、[openhuman](agents/openhuman.md) 34.8k（+0.4k）、[CLI-Anything](agents/cli-anything.md) 45.3k（+0.3k）、[MiMoCode](agents/mimocode.md) 11.9k（+0.3k）、[agentmemory](https://github.com/rohitg00/agentmemory) 25.1k（+0.3k）、[financial-services](https://github.com/anthropics/financial-services) 33.5k（+0.2k）、[CodeWhale](agents/codewhale.md) 39.7k（+0.2k）、[12-factor-agents](https://github.com/humanlayer/12-factor-agents) 24.2k（+0.2k）、[jcode](https://github.com/1jehuang/jcode) 8.3k（+0.1k）、[Kimi Code](agents/kimi-code.md) 3.1k（+0.1k）、[CoStrict](agents/costrict.md) 4.3k（基本持平）。

</details>

### 排名趋势

每周 Top 10 自开始追踪以来的名次变化——一条折线一个项目，折线中断表示该周掉出榜单：

<p align="center">
  <img src="../assets/heat-trend-zh.svg" alt="每周热度排行趋势图（bump chart）" width="100%" />
</p>

按类别的完整存量排行——Agent 榜、Agent 基础设施榜、Skill 榜及各自的垂类榜，按 star 总量排序——见 [rankings/](rankings/README.md)。

## 市场脉搏

当下影响选型的三条结构性主线——完整的日期与来源档案见[市场事件](market-events.md)：

- **`.claude/skills` 浪潮持续复利**（2026-05 起）：curated skill 合集和 skills 框架已连续两个月占据每周热度前 10 的约一半。很多任务里技能层已经和底层 agent 同样重要。本仓库通过 [Superpowers](agents/superpowers.md) 覆盖框架端，合集则在 [Skill 垂类榜](rankings/skill-verticals.md)里追踪。
- **模型层变成预算决策**：Anthropic 的 Mythos 级 [Claude Fable 5](agents/claude-fable-5.md)（6 月 9 日）位于 Opus 4.8 之上、按额度计费；OpenAI 的 GPT-5.6（7 月 9 日）分三个价格档——两侧都把"这个任务买哪一档智能"变成了 agent 选型的一部分。春季参照点：[GPT-5.5](agents/gpt-5.5.md)。
- **产品边界在向上坍缩**：OpenAI 把 Codex 并入 ChatGPT 应用（7 月 9 日）——OpenAI 侧的"选哪个 coding agent"正在变成"你怎么用 ChatGPT"。详见 [Codex](agents/codex.md)。

## 先把地图摊开

| 路线 | 代表项目 | 常见使用者 |
| --- | --- | --- |
| 直接执行型 | [Claude Code](agents/claude-code.md), [Aider](agents/aider.md), [Codex](agents/codex.md), [Kimi Code](agents/kimi-code.md), [MiMoCode](agents/mimocode.md), [CodeWhale](agents/codewhale.md), [Devin](agents/devin.md), [Jules](agents/jules.md) | 想把明确 coding 任务交给 agent 的人（见[终端编码 CLI 对比](comparisons/coding-cli-agents.md)） |
| Agent harness 框架 | [Pi](agents/pi.md), [OpenHands](agents/openhands.md), [SWE-agent](agents/swe-agent.md), [mini-swe-agent](agents/mini-swe-agent.md), [OpenHarness](agents/openharness.md) | 想自己掌控 agent loop、工具表面和权限，而不是直接接受厂商成品的人（见 [harness 框架对比](comparisons/agent-harness-frameworks.md)） |
| 前沿 agentic 模型 | [Claude Fable 5](agents/claude-fable-5.md), [GPT-5.5](agents/gpt-5.5.md) | 在选要接入自己 agent 系统的模型，或在评估 Anthropic / OpenAI 系 agent 能力上限的人 |
| Agentic skills 框架 | [Superpowers](agents/superpowers.md) | 想要一套方法论 + 可组合 skills 层、能接到 Claude Code、Codex、Cursor 等 agent 之上的人 |
| 工作流 / orchestration layer | [oh-my-claudecode](agents/oh-my-claudecode.md), [oh-my-codex](agents/oh-my-codex.md), [Ruflo](agents/ruflo.md) | 已经认可 Claude Code 或 Codex，只想在上面补强 orchestration 的人（Ruflo 把这条进一步推到跨机器联邦和 100+ 专用 agent） |
| 编辑器中心工作流 | [Cursor](agents/cursor.md), [Windsurf](agents/windsurf.md), [Continue](agents/continue.md) | 想让编辑器本身保持在工作流核心的人 |
| review-first 自动化 | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md), [CoStrict](agents/costrict.md) | 想把 review 和人工控制留在核心的人（CoStrict 加了企业严格流程 + 私有化部署） |
| 管理式后台路径 | [Claude Managed Agents](agents/claude-managed-agents.md) | 需要 Anthropic 的定时、云端或后台工作流的人 |
| 通用自主 agent | [AutoGPT](agents/autogpt.md), [Agent Zero](agents/agent-zero.md), [BabyAGI](agents/babyagi.md), [Julep](agents/julep.md), [GenericAgent](agents/generic-agent.md), [ml-intern](agents/ml-intern.md) | 想要通用自主任务执行的人（ml-intern 是 ML 工程取向的特化版本） |
| 自建系统 | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md), [Haystack](agents/haystack.md), [Semantic Kernel](agents/semantic-kernel.md), [DSPy](agents/dspy.md), [Pydantic AI](agents/pydantic-ai.md) | 想自己搭 agent 平台的团队 |
| 运行时 & 工具 | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [CLI-Anything](agents/cli-anything.md) | 需要工作流自动化、代码执行、LLM 网关、agent 上下文基础设施、agent 驱动 CLI 或可视化构建器的团队 |
| 自托管 / 本地 runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md), [OpenHuman](agents/openhuman.md) | 需要端侧隐私、长期运行、本地控制、渠道、设备或个人数据生活集成能力的人 |

## 当前已覆盖的主流项目

已收录 54 个项目，按形态分组。展开任意一组，或到 [agents/](agents/README.md) 浏览完整的路线表与覆盖表。

<details>
<summary><strong>编码 agent、编辑器与编排</strong>（23 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [Aider](agents/aider.md) | 直接执行 | 终端优先、贴近 git 的 AI 结对编程 |
| [Claude Code](agents/claude-code.md) | 直接执行 | 本地和 IDE 优先的 coding agent |
| [Claude Managed Agents](agents/claude-managed-agents.md) | 管理式后台路径 | Anthropic 管理式 / 云端执行工作流映射 |
| [Codex](agents/codex.md) | 直接执行 | ChatGPT 应用内的 coding agent，支持异步云端委派 |
| [oh-my-claudecode](agents/oh-my-claudecode.md) | 工作流层 | Claude Code 之上的 teams-first orchestration layer |
| [oh-my-codex](agents/oh-my-codex.md) | 工作流层 | 为 Codex CLI 增强工作流、teams 和持久状态 |
| [Cursor](agents/cursor.md) | 编辑器中心平台 | 覆盖本地编码、云端 agent 和集成的 AI 编辑器 |
| [GitHub Copilot](agents/github-copilot.md) | 平台 | VS Code + GitHub 里的多表面 agent 平台 |
| [Cline](agents/cline.md) | review-first 执行 | 编辑器内 approval-first coding agent |
| [Windsurf](agents/windsurf.md) | AI 原生 IDE | 以 Cascade 为中心的 AI IDE |
| [OpenHands](agents/openhands.md) | 开源执行 | 开源 AI 软件工程 agent |
| [Devin](agents/devin.md) | 托管执行 | 端到端软件工程执行 |
| [Jules](agents/jules.md) | 托管云端执行 | GitHub 连接、PR 回收的 coding delegation |
| [Continue](agents/continue.md) | 编辑器中心 | 支持自选模型的开源 IDE 扩展 |
| [Froge Code](agents/froge-code.md) | review-first 自动化 | 当前按 Automagik Genie 暂定映射 |
| [Pi](agents/pi.md) | 直接执行 | 极简终端 coding agent harness，多 LLM provider 支持 |
| [CodeWhale](agents/codewhale.md) | 直接执行 | DeepSeek + MiMo 终端 coding agent（原 DeepSeek-TUI） |
| [Kimi Code](agents/kimi-code.md) | 直接执行 | Moonshot AI 官方、Kimi 原生的终端 coding CLI（kimi-cli 继任者） |
| [MiMoCode](agents/mimocode.md) | 直接执行 | 小米官方的 MiMo 终端 coding agent，内置跨会话记忆 |
| [CoStrict](agents/costrict.md) | review-first 自动化 | Cline 血统的企业 coding agent，含严格标准化流程、AI 代码评审、私有化部署 |
| [SWE-agent](agents/swe-agent.md) | Agent harness 框架 | Princeton + Stanford 的 SWE-bench 原始 harness，single-YAML 配置 |
| [mini-swe-agent](agents/mini-swe-agent.md) | Agent harness 框架 | SWE-agent 的 ~100 行 Python 接班版，SWE-bench Verified 仍 >74% |
| [OpenHarness](agents/openharness.md) | Agent harness 框架 | HKUDS 的 10 子系统开源 agent harness，43+ 工具、兼容 anthropics/skills、支持 MCP |

</details>

<details>
<summary><strong>自主与自托管 agent</strong>（13 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [AI Edge Gallery](agents/ai-edge-gallery.md) | 端侧本地 runtime | 带 agent skills 的移动端本地 assistant 沙盒 |
| [Goose](agents/goose.md) | 开源本地平台 | 跨 desktop、CLI、API 的可扩展本地 agent |
| [Hermes Agent](agents/hermes-agent.md) | 多 agent / 自托管 | 带 memory、skills、gateway 的长期工作环境 |
| [OpenClaw](agents/openclaw.md) | runtime | 多渠道、多设备、本地优先运行层 |
| [AutoGPT](agents/autogpt.md) | 自主 agent 平台 | 可视化 agent 构建器，带工作流、市场和多模型支持 |
| [Agent Zero](agents/agent-zero.md) | 自主 agent | 自构建自主 agent，动态创建工具 |
| [BabyAGI](agents/babyagi.md) | 实验性 | 开创性自主 agent 实验——教学用，非生产 |
| [Open Interpreter](agents/open-interpreter.md) | 运行时 | 自然语言到本地代码执行，无沙盒 |
| [Mercury Agent](agents/mercury-agent.md) | 自托管多通道 | 主打 CLI + Telegram 的权限硬化 agent，带 token 预算 |
| [ml-intern](agents/ml-intern.md) | 垂直领域自主 agent | Hugging Face 的自主 ML 工程师——基于 HF 生态做研究、写代码、发布 ML 成果 |
| [GenericAgent](agents/generic-agent.md) | 自演进自主 agent | 从小种子起步、每完成任务长出 skill tree 的自主 agent |
| [OpenHuman](agents/openhuman.md) | 自托管 / 本地 runtime | 桌面生活集成 agent，118+ 连接器、本地 Memory Tree、支持 Ollama |
| [Julep](agents/julep.md) | 工作流引擎 | Temporal 支撑的持久化有状态 AI agent 工作流引擎 |

</details>

<details>
<summary><strong>框架与基础设施</strong>（15 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [LangChain](agents/langchain.md) | 平台 | 快速搭自定义 agent 的高层框架 |
| [LangGraph](agents/langgraph.md) | 平台 | 搭持久化、有状态 agent workflow 的底层框架 |
| [CrewAI](agents/crewai.md) | 多 agent 框架 | 角色型 agent 协作，快速搭原型 |
| [LlamaIndex](agents/llamaindex.md) | 数据优先框架 | 基于文档和数据的 RAG 与 agentic 应用 |
| [n8n](agents/n8n.md) | 工作流自动化 | 带原生 AI agent 节点和 400+ 集成的可视化工作流平台 |
| [MemGPT](agents/memgpt.md) | 有状态 agent 平台 | 跨会话学习的持久记忆 agent（现名 Letta） |
| [Haystack](agents/haystack.md) | 框架 | deepset 的生产导向 RAG 和 agent 框架 |
| [Semantic Kernel](agents/semantic-kernel.md) | 框架 | 微软的 AI 编排 SDK，支持 .NET、Python、Java |
| [DSPy](agents/dspy.md) | 框架 | 程序化 prompt 优化——编程而非手调 LM |
| [LiteLLM](agents/litellm.md) | 基础设施 | 100+ LLM provider 的统一 API 网关 |
| [Pydantic AI](agents/pydantic-ai.md) | 框架 | 类型安全 Python agent 框架，结构化输出 |
| [Flowise](agents/flowise.md) | 可视化构建器 | 基于 LangChain 的拖拽式 LLM 应用和 agent 构建器 |
| [Ruflo](agents/ruflo.md) | 工作流 / orchestration layer | 面向 Claude 的多 agent 编排平台，支持跨机器联邦、神经记忆和 100+ 专用 agent |
| [CodeGraph](agents/codegraph.md) | 运行时 & 工具 | 为 Claude Code、Cursor、Codex CLI、opencode、Hermes Agent 提供预索引的代码知识图谱 + MCP server |
| [CLI-Anything](agents/cli-anything.md) | 运行时 & 工具 | 为任意软件自动生成 Click CLI，让 agent 能驱动没有 API 的应用 |

</details>

<details>
<summary><strong>模型与技能</strong>（3 个）</summary>

| 项目 | 路线 | 一句话定位 |
| --- | --- | --- |
| [Claude Fable 5](agents/claude-fable-5.md) | 前沿 agentic 模型 | Anthropic 的 Mythos 级前沿模型——Claude 系 agent 在 Opus 之上的能力天花板 |
| [GPT-5.5](agents/gpt-5.5.md) | 前沿 agentic 模型 | OpenAI 2026 春季的 agentic 模型（7 月已由 GPT-5.6 接棒） |
| [Superpowers](agents/superpowers.md) | Agentic skills 框架 | 一整套方法论 + 可组合 skills 层，可接到 Claude Code、Codex、Cursor 等 agent 之上 |

</details>

## 可以这样开始

如果还不确定从哪里切入，可以先按这些示意路径读一轮，再按自己的场景分支出去。

| 如果你更像这样 | 推荐阅读路径 | 这条路径会帮你回答什么 |
| --- | --- | --- |
| 我想找一个日常 coding agent，但还没想清楚终端还是编辑器 | [Aider](agents/aider.md) → [Claude Code](agents/claude-code.md) → [终端编码 CLI 对比](comparisons/coding-cli-agents.md) → [Cursor](agents/cursor.md) → [Cline](agents/cline.md) → [use-cases/coding-automation.md](use-cases/coding-automation.md) | 哪个厂商 CLI 配你的模型、终端优先 vs 编辑器中心 vs 强审批控制怎么取舍 |
| 我已经喜欢 Claude Code 或 Codex，但想补强 orchestration | [Claude Code](agents/claude-code.md) → [oh-my-claudecode](agents/oh-my-claudecode.md) → [Codex](agents/codex.md) → [oh-my-codex](agents/oh-my-codex.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | 底层 agent 够不够用，什么时候值得再加一层工作流 |
| 我想搞清楚 2026 模型竞赛怎么改变 agent 选型 | [Claude Fable 5](agents/claude-fable-5.md) → [GPT-5.5](agents/gpt-5.5.md) → [Codex](agents/codex.md) → [Claude Code](agents/claude-code.md) → [市场事件](market-events.md) | 前沿模型分档（Mythos、GPT-5.6）怎样抬高能力天花板，又怎样影响产品选型 |
| 我想要专用 AI IDE，而不是继续拼装工具 | [Cursor](agents/cursor.md) → [Windsurf](agents/windsurf.md) → [GitHub Copilot](agents/github-copilot.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | AI 原生编辑器和生态型平台怎么区分 |
| 我想把 ticket 交出去，过一会儿再回来验收 | [Codex](agents/codex.md) → [Jules](agents/jules.md) → [Devin](agents/devin.md) → [Claude Managed Agents](agents/claude-managed-agents.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | 异步云端委派和管理式后台自动化有什么差别 |
| 我需要开源、自托管或者更强本地控制面 | [Aider](agents/aider.md) → [OpenHands](agents/openhands.md) → [Goose](agents/goose.md) → [Hermes Agent](agents/hermes-agent.md) → [capabilities](capabilities/README.md) | 终端控制、开源执行和本地运行控制面的取舍 |
| 我不是买产品，而是要搭自己的 agent 体系 | [LangChain](agents/langchain.md) → [LangGraph](agents/langgraph.md) → [capabilities](capabilities/README.md) → [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md) | framework、runtime、product 三者边界怎么分 |

## 免责声明

表格里的 star 数和 7 天增量，都是仓库更新时点抓取的 GitHub 快照；不同周次之间会出现波动，少量取整误差也是正常的。每个项目的描述、厂商和能力总结，反映的是写作时点的公开信息，可能因项目演进、被收购、转型而过时。本仓库提供的是**选型参考**，不是背书、不是投资建议、也不是生产可用性保证。最终决策前请以各项目自己的官方文档为准。