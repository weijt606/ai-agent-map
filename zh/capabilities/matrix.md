# 能力矩阵

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](matrix.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../capabilities/matrix.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

热度榜回答"谁最火"。本页回答地图真正存在的那个更难的问题：**就某一项能力而言，谁把它当成核心强项。**

每一列都是[重点维度](README.md)之一。每个格子按"这项能力是招牌强项、只是顺带支持、还是根本不是重点"来打分——因为"都支持"这句话，把大部分真实差异都藏起来了。

## 怎么读一个格子

| 标记 | 含义 |
| --- | --- |
| ● | **核心强项**——选它的招牌理由 |
| ◐ | **扎实支持**——真有，但不是主戏 |
| ○ | **有限 / 顺带**——能做，但你会感到接缝 |
| — | **非目标**——不在这个工具的范围内 |

列名，取自[维度词表](README.md)的缩写：**Tool** = 工具调用 · **Exec** = 代码执行 · **Mem** = 记忆 · **Orch** = 编排 · **Multi** = 多 agent · **Appr** = 人工审批 · **Sched** = 调度 · **Surf** = 交互面 · **Deploy** = 部署控制。

> 打分刻意做得粗——它是选型辅助，不是 benchmark。反映的是每个项目在其 profile 里*自述*的重心，不是实验室实测。要看成本和编码能力的硬数字，见 [成本 & benchmark](../comparisons/cost-and-benchmarks.md)。

## 一个格子背后的证据

光一个符号无法核实、也无法反驳——半年后没人记得它当时对应哪个版本、在哪验证、什么时候验证。所以格子可以带一条**[证据记录](evidence-records.md)**：符号还在，但它和 `scope`、`source`、`version`、`review_date`、以及那个用来定分歧的字段 `evidence_type`（`documentation` = 宣传的 vs `source`/`demo`/`benchmark` = 实测的）一起走。记忆格子再进一步拆成生命周期子 schema——因为两个都打 ● 的记忆格子行为可能天差地别。

这一套正分阶段推进；[jcode](../agents/jcode.md) 的记忆格子已跑通全流程作为模板——下表它的 `Mem` 符号链到它的记录。schema、记忆子 schema 和分阶段计划见 **[证据记录](evidence-records.md)**。schema 出自 [u/teugent](https://www.reddit.com/r/AI_Agents/comments/1v56023/)。

## 终端编码 CLI

| 项目 | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Claude Code](../agents/claude-code.md) | ● | ● | ◐ | ◐ | ◐ | ◐ | ○ | ● | ◐ |
| [Codex](../agents/codex.md) | ● | ● | ○ | ◐ | ● | ◐ | ◐ | ● | ○ |
| [Aider](../agents/aider.md) | ◐ | ● | ○ | ○ | — | ● | — | ○ | ◐ |
| [Kimi Code](../agents/kimi-code.md) | ● | ● | ○ | ○ | — | ◐ | — | ◐ | ◐ |
| [MiMoCode](../agents/mimocode.md) | ● | ● | ● | ○ | — | ◐ | — | ○ | ◐ |
| [CodeWhale](../agents/codewhale.md) | ● | ● | ○ | ○ | — | ◐ | — | ○ | ◐ |
| [Grok Build](../agents/grok-build.md) | ● | ● | ○ | ◐ | — | ◐ | ○ | ◐ | ◐ |

看点：Claude Code 和 Codex 的**交互面**最广；Codex 在这组里唯一强在**多 agent**（并行云端 agent）；MiMoCode 是唯一把**记忆**当招牌的 CLI；Aider 在显式 diff 的**人工审批**上领先。Grok Build 是最新加入的一个，在厂商 CLI 里**工具调用** + **代码执行**这对组合最强（MCP、skills、插件、hooks、沙箱、工作区 checkpoint），但注意它的**部署控制**分数对应的是一棵源码可见、却不接受贡献的树。

## 自己掌控循环的 harness 框架

| 项目 | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Pi](../agents/pi.md) | ● | ● | ◐ | ◐ | ○ | ◐ | ○ | ○ | ● |
| [jcode](../agents/jcode.md) | ● | ● | [●](evidence-records.md#完整样例jcode-记忆格子) | ◐ | ◐ | ◐ | ○ | ○ | ● |
| [OpenHands](../agents/openhands.md) | ● | ● | ◐ | ● | ◐ | ◐ | ◐ | ◐ | ● |
| [SWE-agent](../agents/swe-agent.md) | ● | ● | ○ | ○ | — | ○ | — | ○ | ● |
| [mini-swe-agent](../agents/mini-swe-agent.md) | ◐ | ● | — | ○ | — | ○ | — | ○ | ● |
| [OpenHarness](../agents/openharness.md) | ● | ● | ◐ | ● | ◐ | ◐ | ◐ | ◐ | ● |
| [QM](../agents/qm.md) | ◐ | ● | ● | ● | ◐ | ● | ● | ● | ● |
| [Omnigent](../agents/omnigent.md) | ● | ● | ○ | ● | ● | ● | ○ | ● | ● |

看点：整条路线由**部署控制**定义（你拥有循环）。jcode 是唯一把**记忆**当招牌的 harness（被动语义图谱——见[记忆方案](../comparisons/memory-approaches.md)）；OpenHands 和 OpenHarness 的**编排**最重。

两个元 harness 打分面很宽，因为它们补的正是单循环 harness 刻意不做的那一层——而且两者分得很干净。[QM](../agents/qm.md) 是这条路线上唯一把**记忆**、**调度**和**交付表面**同时做成核心的，因为每个作用域自带记忆、cron 以及 Slack/web 的存在感；它的**工具使用**故意只给 ◐（工具面小而固定，靠 skill 扩展而不是靠铺广度）。[Omnigent](../agents/omnigent.md) 则在**多 agent** 上领先——在一个会话里混用多个 harness，包括让一个去评审另一个——而两者都靠策略引擎（而不是逐次编辑弹窗）把**人工审批**做成核心。读这两行时请带上成熟度：QM 才几天大，Omnigent 自标 alpha，所以这些分反映的是它们声明的设计重心，不是实战验证过的行为。

## 编辑器中心 & 评审优先

| 项目 | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Cursor](../agents/cursor.md) | ● | ◐ | ○ | ◐ | ◐ | ◐ | ◐ | ● | ○ |
| [Windsurf](../agents/windsurf.md) | ● | ◐ | ○ | ◐ | ○ | ◐ | ○ | ◐ | ○ |
| [Continue](../agents/continue.md) | ◐ | ○ | ○ | ○ | — | ◐ | — | ◐ | ◐ |
| [Cline](../agents/cline.md) | ● | ● | ○ | ○ | — | ● | — | ◐ | ◐ |
| [GitHub Copilot](../agents/github-copilot.md) | ● | ◐ | ○ | ◐ | ◐ | ◐ | ◐ | ● | ○ |
| [CoStrict](../agents/costrict.md) | ● | ● | ○ | ● | ◐ | ● | ○ | ◐ | ● |
| [Open Code Review](../agents/open-code-review.md) | ● | — | — | ● | ◐ | ◐ | ○ | ● | ● |

看点：Cline 和 CoStrict 把**人工审批**当作全部重点；CoStrict 是这组里唯一在**部署控制**（私有化、本地部署）和**编排**（需求→评审的标准化流程）上都强的。

[Open Code Review](../agents/open-code-review.md) 在这一组里形状特别，值得仔细读：它在代码执行和记忆上是 **—**，因为它从不运行你的代码，除了可续跑的会话之外也不保留状态；人工审批只给 **◐**，不是因为把人晾在一边，而是因为它根本没有"审批闸口"可给——它只留评论然后停下。它的**编排** ● 对一个评审工具来说很反常，而这恰恰就是产品本身：确定性的文件选择、打包成并发子 agent、以及包在模型外面的规则匹配。它的**交付表面** ● 覆盖一个 CLI、四套 CI 系统，以及 Claude Code、Codex、Cursor、OpenCode 的插件。

## 托管 & 云端委派

| 项目 | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Devin](../agents/devin.md) | ● | ● | ◐ | ● | ◐ | ◐ | ● | ◐ | — |
| [Jules](../agents/jules.md) | ● | ● | ○ | ◐ | ◐ | ◐ | ◐ | ◐ | — |
| [Claude Managed Agents](../agents/claude-managed-agents.md) | ● | ● | ◐ | ● | ◐ | ◐ | ● | ◐ | — |

看点：这条路线的取舍全在最后一列——你放弃**部署控制**，换来前台 CLI 给不了的**调度**和后台执行。

## 叠在基座之上的编排层

| 项目 | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [oh-my-claudecode](../agents/oh-my-claudecode.md) | ◐ | ◐ | ◐ | ● | ◐ | ◐ | ◐ | ◐ | ◐ |
| [oh-my-codex](../agents/oh-my-codex.md) | ◐ | ◐ | ◐ | ● | ◐ | ◐ | ◐ | ◐ | ◐ |
| [Ruflo](../agents/ruflo.md) | ◐ | ◐ | ◐ | ● | ● | ○ | ◐ | ◐ | ◐ |

看点：**编排**就是它们存在的理由——给基座 agent 加上 teams、skills 和持久工作流。Ruflo 在**多 agent**上走得最远（多机联邦、100+ 专用 agent）。

## 自建框架

| 项目 | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [LangChain](../agents/langchain.md) | ● | ◐ | ◐ | ● | ◐ | ○ | ○ | — | ● |
| [LangGraph](../agents/langgraph.md) | ● | ◐ | ● | ● | ● | ◐ | ◐ | — | ● |
| [CrewAI](../agents/crewai.md) | ● | ◐ | ◐ | ● | ● | ○ | ○ | — | ● |
| [LlamaIndex](../agents/llamaindex.md) | ◐ | ○ | ◐ | ◐ | ◐ | ○ | ○ | — | ● |
| [eve](../agents/eve.md) | ● | ● | ◐ | ● | ● | ● | ● | ● | ◐ |

看点：库这一批里，LangGraph 在持久**记忆**和**多 agent**状态上最强；LlamaIndex 的记忆是数据/检索，不是对话。

[eve](../agents/eve.md) 是打破这一组形态的那一行，值得当作对照来读。它上面的每一个在**交互面**上都是 **—**，因为库不决定 agent 最后出现在哪里；eve 自带八个以上渠道适配器，所以它是这里唯一一个**交互面**、**定时**、**人工审批**同时为核心的条目（`needsApproval` 能让一次运行无限期暂停且不耗算力）。它的**代码执行** ● 指的是每个 agent 一个沙箱，不是一个辅助工具；**记忆**故意只给 ◐——能扛过重新部署的检查点会话是状态，不是记忆系统。它让出的那一列，恰好是上面每个库都握着的：**部署控制**只有 ◐，因为文档里的生产路径是 Vercel，哪怕 license 是 Apache-2.0。

## 运行时、网关 & 上下文基础设施

| 项目 | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [n8n](../agents/n8n.md) | ● | ◐ | ○ | ● | ◐ | ◐ | ● | ◐ | ● |
| [Letta (MemGPT)](../agents/memgpt.md) | ◐ | ○ | ● | ◐ | ◐ | ○ | ○ | — | ● |
| [Open Interpreter](../agents/open-interpreter.md) | ● | ● | ○ | ○ | — | ◐ | ○ | ◐ | ● |
| [Flowise](../agents/flowise.md) | ● | ◐ | ◐ | ● | ◐ | ○ | ◐ | ◐ | ● |
| [LiteLLM](../agents/litellm.md) | — | — | — | ○ | — | — | — | — | ● |
| [Langfuse](../agents/langfuse.md) | — | ○ | ○ | — | — | ◐ | ○ | ◐ | ● |
| [CodeGraph](../agents/codegraph.md) | ◐ | — | ● | — | — | — | — | ◐ | ● |
| [CLI-Anything](../agents/cli-anything.md) | ● | ◐ | — | — | — | — | — | ◐ | ● |

看点：这组是黏合层，所以形状很偏。n8n 在**调度**（事件/cron 触发）上领先；Letta 是自编辑**记忆**的参照；CodeGraph 的"记忆"是代码知识图谱（上下文，不是对话）；LiteLLM 是纯网关——唯一真正的列是**部署控制**。[Langfuse](../agents/langfuse.md) 在这里几乎什么都不得分，而这是设计使然：它*观察* agent 而不行动，所以它真正的列是**部署控制**（自托管免费不限量）和**人工审批**（标注队列、LLM-as-a-judge 评审）——见[观测与评估](../comparisons/observability-and-evals.md)。

## 自托管、多渠道 & 自主

| 项目 | Tool | Exec | Mem | Orch | Multi | Appr | Sched | Surf | Deploy |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [Hermes Agent](../agents/hermes-agent.md) | ● | ● | ● | ● | ● | ◐ | ◐ | ● | ● |
| [OpenClaw](../agents/openclaw.md) | ● | ● | ◐ | ● | ● | ◐ | ◐ | ● | ● |
| [Mercury Agent](../agents/mercury-agent.md) | ● | ◐ | ● | ◐ | ◐ | ● | ● | ◐ | ● |
| [Goose](../agents/goose.md) | ● | ● | ◐ | ◐ | ◐ | ◐ | ○ | ◐ | ● |
| [OpenHuman](../agents/openhuman.md) | ● | ○ | ● | ◐ | — | ◐ | ● | ◐ | ● |
| [AutoGPT](../agents/autogpt.md) | ● | ◐ | ◐ | ● | ◐ | ○ | ◐ | ◐ | ● |
| [AI Edge Gallery](../agents/ai-edge-gallery.md) | ◐ | ○ | ○ | — | — | ◐ | — | ◐ | ● |

看点：Hermes 是全图覆盖面最广的单个 profile——几乎每个维度都强。Mercury 把招牌级**人工审批**和**调度**配在一起（权限硬化、常驻）；OpenHuman 把**记忆** + **调度**做成了生活集成的闭环。

## 用它做选型

1. **圈出对你的工作流必需的列**——不是那些听起来不错的。
2. 只保留在这些列上打 **●** 的行。你需要 ● 的地方却只有 ◐ 或 ○，就是那些项目日后悄悄让你失望的地方。
3. 对幸存者，翻到账本的成本一侧：[成本 & benchmark](../comparisons/cost-and-benchmarks.md) 看价格和编码能力，profile 自己的"使用成本"一节看每项强项背后的运维负担。

完整路线视图见 [agents/](../agents/README.md)；随时间的热度见 [rankings/](../rankings/README.md)。
