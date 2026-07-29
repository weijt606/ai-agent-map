# Langfuse

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](langfuse.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/langfuse.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话判断：Langfuse 是**观察** agent 的开源标杆——基于 OpenTelemetry 的追踪、评估与 prompt 管理平台，记录你的 agent 做了什么、给它打分、让你回放。它不负责跑你的 agent。

> **边界——它不是 agent。** 本地图上其他每一个 profile 都是会*行动*的东西。Langfuse 正相反：它是一个待在你执行路径之外的遥测接收端（"trace 事件在本地排队、分批 flush，所以不影响你应用的响应时间"）。它观察的是用 [LangChain](langchain.md)、[LangGraph](langgraph.md)、[CrewAI](crewai.md)、[LlamaIndex](llamaindex.md) 或某个 coding CLI 搭出来的 agent——它从不替代 agent。把它收进来，是因为"我怎么知道我的 agent 在正常工作"是一个真实的选型问题，不是因为它和那些 agent 竞争。
>
> 有一个范围很窄的例外：**Langfuse Assistant**（公开 beta，仅 Cloud）确实是一个真正的 agent 循环——但它操作的是 *Langfuse 自己*，不是你的应用，而且在改动任何数据或配置前会停下来要求你明确批准。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | Langfuse——**2026 年 1 月被 ClickHouse 收购** |
| 路线 | 观测与评估基础设施（不是 agent 路线） |
| 开源 | 开放内核——核心 MIT，`ee/` 目录为商业许可 |
| 实现 | TypeScript（服务端）；Python v4 与 JS/TS v5 SDK，其余语言走 OpenTelemetry |
| 许可证 | MIT + Enterprise License（因为许可文件是双份的，GitHub 显示 `NOASSERTION`） |
| 可自托管 | 可以，OSS 档免费且不限量（Docker / Kubernetes） |
| 适合 | 已经把 agent 跑在生产、需要把 trace、成本/延迟、评估和 prompt 版本管理放在一处并且能自托管的团队 |
| 主要代价 | 它是又一个要运维的服务；企业通常最想要的那些（RBAC、审计日志、SSO、保留策略、脱敏）都是商业许可 |
| GitHub 仓库 | https://github.com/langfuse/langfuse |

## 什么时候选它

- 你的 agent 已经在生产跑，但你回答不了"它到底做了什么、花了多少钱、这周比上周变好还是变差"。带嵌套 observation、session、user 和 **agent 图**的追踪是招牌，token/成本/延迟统计顺带就有。
- 你想要一套**可以免费自托管、且核心功能没有阉割**的观测系统——追踪、评估、prompt 管理、数据集和 SDK 全是 MIT。这是选它而不是 [LangSmith](../comparisons/observability-and-evals.md) 或 Braintrust（两者都是闭源平台）的主要理由。
- 你希望评估和 prompt 管理跟追踪在同一个工具里：LLM-as-a-judge、代码评估器、人工标注队列、数据集与实验（含 CI/CD 里的实验），外加带部署标签和 A/B 测试的 prompt 版本管理。
- 你是框架无关或多框架并用。它几乎覆盖了本地图涉及的整个生态——[LangChain](langchain.md)、[LangGraph](langgraph.md)、[LlamaIndex](llamaindex.md)、[CrewAI](crewai.md)、OpenAI Agents SDK、Claude Agent SDK——而且少见地也接 coding agent（[Claude Code](claude-code.md)、[Codex](codex.md)、[Cursor](cursor.md)、[Goose](goose.md)、[Pi](pi.md)、[OpenClaw](openclaw.md)）。
- 你本来就在用 ClickHouse，或者你预期观测层最终会并进你自己运维的数据平台。

## 什么时候别选它

- 你想要的是会*干活*的东西——这只是仪表盘和埋点。如果你需要的是 agent 本身，那你翻错页了。
- 你想要单一厂商的整套栈，而且已经生活在某个框架的工具链里。如果你全押 LangChain，LangSmith 是阻力最小的路径（代价是它闭源）。
- 你是单人小项目。免费 Hobby 档（每月 5 万 unit、30 天保留、2 个用户）已经够大方，但为一个业余 agent 多运维一个服务通常不值——直接看日志。
- 你需要企业级治理但**不想付费**：RBAC、审计日志、SCIM、服务端数据脱敏、保留策略和 SSO，在云端和自托管两条路上都在 Enterprise 许可后面。
- 你需要一份关于"跑评估代码"的隔离保证文档。代码评估器写明了约束（无网络出口、2 秒上限、仅标准库），但**沙箱机制没有文档**——如果这点重要，请自己验证。

## 能力形态

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 观测 / 追踪 | 很强 | 核心能力。基于 OTel，嵌套 observation、session、user、agent 图、多模态、采样、脱敏、多环境 |
| 评估 | 强 | LLM-as-a-judge、代码评估器、人工标注队列、数据集与实验、CI/CD 实验 |
| Prompt 管理 | 强 | 版本管理、部署标签、A/B 测试、可组合、客户端缓存保证可用性 |
| 成本与延迟分析 | 强 | token 与成本统计、自定义看板、Metrics API、监控、消费告警 |
| 生态覆盖 | 很强 | 几十个框架集成外加 coding agent；双向 MCP server 和一个 Agent Skill |
| 部署控制 | 强 | 自托管免费不限量，但治理类功能被 EE 门禁 |
| Agent 行为 | **非目标** | 不在你的执行路径里。Assistant 仅 Cloud、beta，且操作的是 Langfuse 自己 |

## 使用成本

复杂度中等。埋点本身很轻——用 Python/JS SDK 装饰或包一层调用，或者把任意 OTel exporter 指过来——但 Langfuse 是个有数据库的有状态服务，所以自托管意味着你在 agent 之外又多运维一套观测系统。云端价格：Hobby $0（每月 5 万 unit）、Core $29/月、Pro $199/月、Enterprise $2,499/月（年付），超量按每 10 万 unit 从 $8.00 阶梯降到 $6.00；自托管在 OSS 档免费，Enterprise 档另行询价。发版节奏很快——大约每月 20 个 tag——修得快，但如果你锁版本就有点累。

> **两件需要你自己核实的事。** （1）v4 这条线含糊：文档说 "Langfuse v4 is live"，而 GitHub releases 上仍是 `v4.0.0-rc.3` 与稳定版 `v3.224.2` 并存——确认你实际装的是哪个。（2）收购之后那句"仍然 100% 开源、路线图不变"是**厂商表述**，不是可核实的事实；MIT 许可和持续的 OSS 发版目前与之一致，但请把它当承诺、不是保证。

## 结论

Langfuse 回答的是"我的 agent 在跑，但我完全不知道它在干什么"——而且在一个最强的商业选项都闭源的领域里，它是开源默认解。先上 trace，等评估和 prompt 版本管理各自证明价值了再加；三者共处在一个可自托管的工具里，才是选它的真正理由。只要说清楚你采用的是什么：这是你 agent 栈*下面*的一层，不是其中一部分，而且企业治理功能在两条部署路径上都是付费档。完整的领域对比——谁真开源、谁只是源码可见、谁是闭源——见[观测与评估](../comparisons/observability-and-evals.md)。想知道它接在什么上面，见 [LangGraph](langgraph.md)、[CrewAI](crewai.md) 和 [LlamaIndex](llamaindex.md)。
