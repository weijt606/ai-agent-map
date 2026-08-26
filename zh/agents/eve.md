# eve

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](eve.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/eve.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话判断：eve 是 Vercel 的开源 agent 框架——一个 agent 就是**一个目录**（instructions、tools、skills、subagents、channels、schedules、connections），而大多数团队要自己拼的生产件（持久化执行、每个 agent 独立沙箱、审批闸门、evals）是框架自带的，不是搭在旁边的。

> **文件系统就是 API。** Vercel 自己的说法是"agent 的 Next.js"：你只在约定位置声明这个 agent 做什么，剩下的交给框架。好处是一个 eve 项目异常可读——agent 的能力变更可以在 pull request 里直接 diff 出来；代价是重启、审批、隔离这些事由框架负责，不再由你的胶水代码负责。

> **开源，但通往生产的路走 Vercel。** 仓库是 Apache-2.0，包就是普通的 npm 包，读它、fork 它都没人拦你。但文档里写明的部署方式是把它当成普通 Vercel 项目 `vercel deploy`，沙箱与模型访问都经过 Vercel 的 AI Gateway，自托管**没有**作为受支持路径写进文档。在把它当成一个中立的框架选择之前，先掂量这一点。

## 快速判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Vercel（`vercel/eve`，eve.dev）——2026 年 6 月 17 日在 Vercel Ship 发布，属于 Agent Stack 的一部分 |
| 路线 | 自建平台——自带生产件的 agent 框架 |
| 开源 | Apache-2.0，npm 包名 `eve` |
| 实现 | Node 上的 TypeScript；持久化执行建立在开源的 Workflow SDK 之上 |
| 核心思路 | 一个 agent 就是一个目录：`instructions.md`、`tools/`、`skills/`、`subagents/`、`channels/`、`schedules/`、`connections/` |
| 模型 | 经 AI Gateway 接任意模型，带 provider 回退；MCP server 与 OpenAPI 兼容 API 都可作为工具 |
| 交付面 | Slack、Discord、Teams、GitHub、Linear、Telegram、Twilio、HTTP——一个 agent，多个 channel 适配器 |
| 适合 | 把 agent 当作**长期运行的产品**来做的团队，否则这些会话、沙箱、审批的管道都得自己写 |
| 主要代价 | 2026 年 6 月起才公开预览，且部署故事以 Vercel 为中心 |
| GitHub 仓库 | https://github.com/vercel/eve |

## 什么时候选它

- 你在把 agent **当产品做**，不是当脚本写。会话通过 Workflow SDK 做检查点，能扛住崩溃**和重新部署**——后者正是手搓长任务 agent 最常死掉的地方。
- 你想要**把审批做成框架原语**。任意工具都能声明 `needsApproval`；暂停中的 agent 可以无限期等待且不消耗算力，所以"人工卡点"不需要你自己造一套队列。
- 你想要**不用自己设计的隔离**。每个 agent 都有自己的沙箱，模型生成的代码默认跑在你的应用运行时之外。
- 你想要**带独立上下文窗口的 subagent**，并且像调用工具一样调用它们——这是让长任务不淹死单个上下文的标准做法。
- 你想把 **eval 放进仓库**而不是表格里：`defineEval` 给出可评分的测试集，本地或 CI 里跑，和被测 agent 放在一起。
- 你想要**一个 agent 覆盖多个渠道**。channel 是适配器文件，所以 Slack、Discord、Teams、GitHub、Linear、Telegram、Twilio 和纯 HTTP 是配置而不是多套部署——这在本路线里很少见，同类框架基本止步于库的边界。
- 你需要定时自治：`defineSchedule` 把 cron 任务放进同一棵目录树。

## 什么时候不要选它

- 你想要一个编码 agent。eve 是用来**造** agent 的，它不待在你的终端里改仓库。那种需求请看 [Claude Code](claude-code.md)、[Codex](codex.md) 或 [Pi](pi.md)。
- **你需要把自托管当成一等路径。** 文档里通往生产的路就是 Vercel。如果部署控制权是硬性要求，[LangGraph](langgraph.md)、[Pydantic AI](pydantic-ai.md) 或 [harness 框架](../comparisons/agent-harness-frameworks.md)才是把运行时留在你手里的选择。
- 你不是 TypeScript 团队。这个框架从头到尾是 TS；Python 团队请看 [LangGraph](langgraph.md)、[CrewAI](crewai.md) 或 [LlamaIndex](llamaindex.md)。
- 你想一步一步控制状态图。eve 的抽象是"一个目录 + 一个持久会话"，不是显式状态机——[LangGraph](langgraph.md) 是完全相反的取舍。
- 你需要长期的生产验证。它 2026 年 6 月才公开；公司不年轻，框架很年轻。

## 能力形态

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 工具使用 | 很强 | 带类型的 `defineTool` 函数、MCP server、OpenAPI 兼容 API，都是一等工具 |
| 代码执行 | 强 | 每个 agent 一个沙箱，把模型生成的代码与应用运行时隔开 |
| 持久状态 | 强 | Workflow SDK 上的检查点会话能扛住崩溃与部署——这是持久性，不是记忆系统 |
| 编排 | 很强 | 持久会话、subagent、定时任务、审批都是框架原语 |
| 多 agent | 强 | subagent 有独立上下文窗口，像工具一样被调用 |
| 人工审批 | 很强 | 任意工具可加 `needsApproval`；暂停等待期间不产生算力开销 |
| 定时调度 | 强 | `defineSchedule` cron 任务就放在项目树里 |
| 交付面 | 很强 | 一份 agent 定义，八个以上渠道适配器 |
| 部署控制 | 中等 | Apache-2.0、可 fork，但文档里的生产路径是 Vercel |
| 评估 | 强 | `defineEval` 可评分测试集，本地或 CI |

## 值得知道的架构点

整个设计可以压缩成一条规则：**约定位置优于配置**。`agent/instructions.md` 是常驻系统提示；`agent/tools/*.ts` 是带类型的函数；`agent/skills/*.md` 是按需加载而非常驻的流程；`agent/subagents/` 是带独立上下文的子 agent；`agent/channels/*.ts` 把 agent 接到某个平台；`agent/schedules/*.ts` 是 cron 任务；`agent/connections/` 放带凭据的服务集成。`agent/agent.ts` 选模型。这套布局单看没有一处是新发明——它赌的是"把布局标准化"这件事本身，能让不是作者的人也读得懂、运维得了这个 agent。

底下的持久化执行来自开源的 **Workflow SDK**，这也是为什么会话能活过一次部署而不只是一次崩溃。还有一个小但说明问题的细节：`eve` 这个 npm 包把自己的文档一起发到 `node_modules/eve/docs`，好让在你仓库里干活的编码 agent 直接读本地文档而不是靠猜——这个框架从设计上就假定了以后维护它的是 agent。

## 运维成本

低到中等，而且成本异常地集中在**决策**上而不是管道上。`npx eve@latest init` 直接搭好一个能跑的项目和终端 UI，第一次运行之前没有基础设施要立。持续开销是 AI Gateway 上的模型花费、沙箱算力、以及 Vercel 上的平台费用——锁定也正好在这里。把对 Vercel 的依赖读成"自带电池的价格"：你之所以不用自己写检查点和沙箱生命周期，是因为有人在替你跑它们。

## 结论

eve 是迄今为止最清楚的一个信号：有意思的那一层已经从**循环本身**挪到了**循环周围的一切**。同一路线上的其他框架给你原语，把持久性、隔离、审批、渠道留给你自己解决；eve 把这些当成框架的职责，而把 agent 本身变成一个能在 pull request 里读完的目录。这让它成为本地图上"自建"路线里交付面和人工审批最强的一个，同时也是部署控制最弱的一个——这个取舍是摆在明面上的，而且它就是全部的决策点。想把状态图握在自己手里，看 [LangGraph](langgraph.md)；想拥有运行时而不是抽象，看 [agent harness 框架](../comparisons/agent-harness-frameworks.md)。路线级视角见[能力矩阵里的自建框架](../capabilities/matrix.md#自建框架)。
