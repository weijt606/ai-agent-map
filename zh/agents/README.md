# Agents

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](README.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/README.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

这里不是“agent 名单墙”。

这里更像 shortlist：先帮你看懂路线，再决定要不要点进具体页面。

## 先按路线找

| 路线 | 代表项目 | 适合谁 |
| --- | --- | --- |
| 直接执行 | [Claude Code](claude-code.md), [Aider](aider.md), [Codex](codex.md), [Kimi Code](kimi-code.md), [MiMoCode](mimocode.md), [CodeWhale](codewhale.md), [Devin](devin.md), [Jules](jules.md) | 想直接把 coding 任务交给 agent（在[终端编码 CLI agent](../comparisons/coding-cli-agents.md) 里对比） |
| Agent harness 框架 | [Pi](pi.md), [OpenHands](openhands.md), [SWE-agent](swe-agent.md), [mini-swe-agent](mini-swe-agent.md), [OpenHarness](openharness.md) | 想自己掌控 loop、工具表面和权限，不直接接受厂商成品 |
| 前沿 agentic 模型 | [GPT-5.5](gpt-5.5.md) | 在选要接入自己 agent 系统的模型，或在评估 OpenAI 系 agent 能力上限 |
| Agentic skills 框架 | [Superpowers](superpowers.md) | 想要一套方法论 + 可组合 skills 层、能接到 Claude Code、Codex、Cursor 等 agent 之上 |
| 工作流 / orchestration layer | [oh-my-claudecode](oh-my-claudecode.md), [oh-my-codex](oh-my-codex.md), [Ruflo](ruflo.md) | 已经在用 Claude Code 或 Codex，只想补强 teams、skills 和持久工作流（Ruflo 进一步推到跨机器联邦） |
| 编辑器中心工作流 | [Cursor](cursor.md), [Windsurf](windsurf.md), [Continue](continue.md) | 想让编辑器本身成为 agent 主表面 |
| review-first 自动化 | [Cline](cline.md), [GitHub Copilot](github-copilot.md), [Froge Code](froge-code.md), [CoStrict](costrict.md) | 想把 review 和人工节奏留在核心（CoStrict 瞄准企业严格流程 + 私有化部署） |
| 通用自主 agent | [AutoGPT](autogpt.md), [Agent Zero](agent-zero.md), [BabyAGI](babyagi.md), [Julep](julep.md), [GenericAgent](generic-agent.md), [ml-intern](ml-intern.md) | 想要通用自主任务执行（ml-intern 是 ML 工程取向的特化版） |
| 自建平台 | [LangChain](langchain.md), [LangGraph](langgraph.md), [CrewAI](crewai.md), [LlamaIndex](llamaindex.md), [Haystack](haystack.md), [Semantic Kernel](semantic-kernel.md), [DSPy](dspy.md), [Pydantic AI](pydantic-ai.md) | 想自己搭 agent system |
| 运行时 & 工具 | [n8n](n8n.md), [MemGPT](memgpt.md), [Open Interpreter](open-interpreter.md), [LiteLLM](litellm.md), [Flowise](flowise.md), [CodeGraph](codegraph.md), [CLI-Anything](cli-anything.md) | 需要工作流自动化、代码执行、LLM 网关、agent 上下文基础设施、agent 驱动 CLI 或可视化构建器 |
| 自托管 / 本地 runtime | [AI Edge Gallery](ai-edge-gallery.md), [Goose](goose.md), [Hermes Agent](hermes-agent.md), [OpenClaw](openclaw.md), [Mercury Agent](mercury-agent.md), [OpenHuman](openhuman.md) | 需要端侧隐私、本地控制、扩展、渠道、runtime ownership 或个人数据生活集成 |
| 管理式后台路径 | [Claude Managed Agents](claude-managed-agents.md) | 需要云端、定时、后台执行 |

## 近期热门快照

这不是质量排行榜。

它只是把最近一周 GitHub 快照里特别热的 agent 项目摆出来。顺序按 7 天增量；下面的 star 总数是这次更新目录时重新核对过的当前值。

> **最后更新：** 2026-07-14 · **快照窗口：** 2026-07-08 → 2026-07-14（自上次更新以来的增量，约 6 天，估算） · **Star 总数：** 更新时实时核对

项目名链接指向上游 GitHub 仓库。本目录已收录的 profile，在"目录状态"列单独给出链接。

| 排名 | 项目 | 当前 stars | 快照增量 | 目录状态 | 备注 |
| --- | --- | --- | --- | --- | --- |
| #1&#8288;（=） | [mattpocock/skills](https://github.com/mattpocock/skills) | 168.3k | +7,712 | 候补（Skills 浪潮） | 连续第四个窗口守住增量榜首——策展式 `.claude/skills` 目录越过 168k |
| #2&#8288;（↑） | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 77.9k | +5,052 | 候补（Skills 浪潮） | 上升一位到 #2——Addy Osmani 的策展式 agent-skills 集越过 77k |
| #3&#8288;（↓） | [Superpowers](https://github.com/obra/superpowers) | 253.8k | +4,445 | [Profile](superpowers.md) | 下滑一位但越过 253k——agentic skills 框架持续复利增长 |
| #4&#8288;（=） | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 214.2k | +2,915 | [Profile](hermes-agent.md) | 稳守 #4——已收录项目里绝对总数第一，越过 214k |
| #5&#8288;（↑） | [Pi](https://github.com/earendil-works/pi) | 70.5k | +1,907 | [Profile](pi.md) | 从 #7 跳升两位——Earendil 接手的 harness 越过 70k |
| #6&#8288;（↓） | [anthropics/skills](https://github.com/anthropics/skills) | 160.9k | +1,490 | 候补（Skills 浪潮源头） | 下滑一位——Anthropic 自家的 `.claude/skills` 参考仓库，越过 160k |
| #7&#8288;（↑） | [Codex CLI](https://github.com/openai/codex) | 97.7k | +1,459 | [Profile](codex.md) | 从 #9 上升两位——OpenAI 的 Codex CLI 逼近 98k |
| #8&#8288;（↓） | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 59.7k | +1,147 | [Profile](codegraph.md) | 降温两位到 #8——预索引代码知识图谱逼近 60k |
| #9&#8288;（↓） | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 92.8k | +1,038 | 不收录 | 垂直的金融研究多 agent 系统下滑一位越过 92k——作为领域垂直不收录 |
| #10&#8288;（=） | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 37.7k | +821 | 候补（Skills 浪潮） | 稳守 #10——面向 Claude Code 的学术研究管线越过 37k |

历史名次变化的趋势图见 [rankings/](../rankings/README.md)，那里还有按 star 总量排序的分类榜与垂类榜。

**市场事件：**
- **2026 年 7 月 8–14 —— curated skills 轮换、仍无黑马** —— [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 上升一位到 #2（+5.1k，越过 77k），反超滑到 #3 的 [Superpowers](superpowers.md)（越过 253k）。[mattpocock/skills](https://github.com/mattpocock/skills) 连续第四个窗口守住 #1 增量位（+7.7k，越过 168k）。下方唯一真正的重排是 [Pi](pi.md) 跳升两位到 #5、[Codex CLI](codex.md) 跳升两位到 #7，把 [anthropics/skills](https://github.com/anthropics/skills) 和 [codegraph](codegraph.md) 挤下去；[TradingAgents](https://github.com/TauricResearch/TradingAgents) 下滑到 #9。Skills 浪潮仍 5/10。本周新收录扫描没有新的达到收录门槛的 agent 表面；最新且体量最大的新仓库——[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)（7.3k，"loop engineering" 的模式与 CLI 工具集）和 [inkeep/open-knowledge](https://github.com/inkeep/open-knowledge)（2.8k，AI 原生的 markdown wiki 编辑器）——加入候补。
- **2026 年 7 月 2–8 —— curated skills 轮换、仍无黑马** —— [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 是本窗口涨幅最大的项目（+4.3k），从 #6 上升三位到 #3，把 curated 那一端重新炒热。[mattpocock/skills](https://github.com/mattpocock/skills) 连续第三个窗口守住 #1 增量位（+6.6k，越过 160k），而 [Hermes Agent](hermes-agent.md) 和 [anthropics/skills](https://github.com/anthropics/skills) 各降温一位。Skills 浪潮仍 5/10；[TradingAgents](https://github.com/TauricResearch/TradingAgents) 下滑到 #8。本周新收录扫描没有新的达到收录门槛的 agent 表面；最新且体量最大的新仓库——[langchain-ai/openwiki](https://github.com/langchain-ai/openwiki)（9.6k，一个替 agent 写并维护文档的 CLI）和 [vercel/eve](https://github.com/vercel/eve)（3.3k，Vercel 的 agent 构建框架）——加入候补。
- **2026 年 6 月 24 – 7 月 2 —— 榜首冻结** —— 本窗口没有黑马：[mattpocock/skills](https://github.com/mattpocock/skills) 连续第二个窗口守住 #1 增量位（+9.3k，越过 153k），[Superpowers](superpowers.md) 与 [Hermes Agent](hermes-agent.md) 稳守 #2/#3。Skills 浪潮内部（仍 5/10）：[anthropics/skills](https://github.com/anthropics/skills) 升到 #4，[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) 降到 #6；[TradingAgents](https://github.com/TauricResearch/TradingAgents) 以更高的 #7 重回表内。本周新收录扫描没有新的达到收录门槛的 agent 表面；最新的候补——[tigicion/dao-code](https://github.com/tigicion/dao-code)（1.2k，DeepSeek-V4 终端 coding CLI）和 [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design)（2.2k，把 Claude Design 打包成 Agent Skill）——加入候补。
- **2026 年 6 月 17–24 —— Skills 浪潮榜首轮换、MiMoCode 降温** —— [mattpocock/skills](https://github.com/mattpocock/skills) 拿到本窗口最大涨幅（+11.1k，越过 144k）夺回 #1 增量位，而上周的黑马 [MiMoCode](mimocode.md) 只涨了约 1.0k（9.6k → 10.6k），跌出增量前 10。[Codex CLI](codex.md) 以 #9 重回表内，[Hermes Agent](hermes-agent.md) 突破 200k。本周新收录扫描没有新的达到收录门槛的 agent 表面；最大的几个新仓库（[op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) 4.0k、[ruvnet/agent-harness-generator](https://github.com/ruvnet/agent-harness-generator) 0.3k）留在候补。
- **2026 年 5 月底 —— 更名** —— 本目录以 DeepSeek-TUI 收录的 agent 已改名为 [CodeWhale](codewhale.md)（`Hmbown/CodeWhale`，现 36.6k），并从只支持 DeepSeek 扩展到 **DeepSeek + MiMo**。旧的 `DeepSeek-TUI` 链接会重定向；本目录已统一改用新名。
- **2026 年 5 月底 —— 代码上下文黑马** —— [codegraph](codegraph.md) 单窗口翻倍多（16.4k → 37.5k），是目前最清晰的信号：「agent 上下文基础设施」正在成为独立需求中心。全新的 harness 框架 [jcode](https://github.com/1jehuang/jcode)（1jehuang，Rust，6.8k）加入候补，与 [SWE-agent](swe-agent.md) / [mini-swe-agent](mini-swe-agent.md) 和 [OpenHarness](openharness.md) 并列。
- **2026 年 5 月（降温）** —— `.claude/skills` 浪潮仍在继续，但从前 10 占 6 个收窄到 4 个（[mattpocock/skills](https://github.com/mattpocock/skills)、[Superpowers](superpowers.md)、[academic-research-skills](https://github.com/Imbad0202/academic-research-skills)、[anthropics/skills](https://github.com/anthropics/skills)），因为代码上下文和 harness 基础设施抢走了更多热度。Anthropic 自家的 [skills](https://github.com/anthropics/skills) 仍是整套范式的锚点。
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
| [CodeWhale](codewhale.md) | execution（DeepSeek + MiMo） | 是 | DeepSeek + MiMo 终端 coding agent（原 DeepSeek-TUI） | 已在 2026-05 飙升期核验 |
| [Ruflo](ruflo.md) | 多 agent 编排 | 是 | 跨机器联邦的 Claude 编排平台（前身 Claude Flow） | 改名后已核验 |
| [OpenHuman](openhuman.md) | 自托管 / 本地 runtime | 是 | 带 118+ 连接器、本地 Memory Tree、Ollama 支持的开源桌面生活集成 agent | 连续两周热度后已核验 |
| [CodeGraph](codegraph.md) | runtime / agent 上下文 | 是 | 为 Claude Code、Cursor、Codex CLI、opencode、Hermes Agent 服务的预索引代码知识图谱 + MCP server | 2026-05 trending 期间已核验 |
| [CLI-Anything](cli-anything.md) | runtime / agent-native 桥接 | 是 | 为任意软件自动生成 Click CLI，让 agent 能驱动没有 API 的应用 | 已按 v1（2026-05）+ HKUDS 维护核验 |
| [SWE-agent](swe-agent.md) | harness 框架 / 研究参考 | 是 | Princeton + Stanford 的 SWE-bench 原始 harness，single-YAML 配置 | 已按上游核验，团队精力已转移至 mini-swe-agent |
| [mini-swe-agent](mini-swe-agent.md) | harness 框架 / 极简 | 是 | SWE-agent 的 ~100 行 Python 接班版，SWE-bench Verified >74% | 已按上游 README 核验 |
| [OpenHarness](openharness.md) | harness 框架 / 生产级 | 是 | HKUDS 的 10 子系统开源 harness，43+ 工具、anthropics/skills、MCP | 已按 v0.1.9（2026-05）核验 |

## 写法标准

统一写法见 [evaluation-framework.md](evaluation-framework.md)。

## 命名说明

如果项目名称、定位或官方公开边界本身就有歧义，这个目录会直接把歧义写出来，而不是假装已经核验清楚。