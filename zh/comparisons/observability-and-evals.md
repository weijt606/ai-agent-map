# Agent 观测与评估

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](observability-and-evals.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/observability-and-evals.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

本地图其他每一页回答的都是"该让哪个 agent 干活"。这一页回答的是你上线之后立刻会遇到的那个问题：**你怎么知道它干成了？**

一旦 agent 开始无人值守地跑，故障形态就不再是崩溃，而是*静默的质量漂移*——循环照样跑完，只是输出变差了、变贵了、或者错得很微妙。日志抓不到这个。这一层就是为了抓它而存在。

## 这些工具做什么、不做什么

**它们观察 agent，不运行 agent。** 本页每个项目都待在你的执行路径之外：你的应用发出 trace，平台负责存储、可视化和打分。它们都不替代 [LangGraph](../agents/langgraph.md)、[CrewAI](../agents/crewai.md) 或某个 coding CLI——它们给你已经选好的东西装上仪表。

共同的功能集已经收敛到四件事：

| 能力 | 它回答什么 |
| --- | --- |
| **追踪（Tracing）** | agent 究竟做了什么——每一步、每次工具调用、每个 token、每毫秒 |
| **评估（Evaluation）** | 做得好不好——LLM-as-a-judge、代码断言、人工评审 |
| **Prompt 管理** | 这个结果是哪个 prompt 版本产出的，能不能回滚 |
| **数据集与实验** | 我要发的这个改动，比线上现有的更好吗 |

多数团队第一天就需要追踪，有真实用户后需要评估，其余的只有当 prompt 迭代变成团队协作时才需要。

## 这个领域

star 数与许可证核对于 **2026-07-29**，依据各项目自己的仓库。

| 项目 | 开源？ | 许可证 | Stars | 自托管 | 形态 |
| --- | --- | --- | --: | --- | --- |
| **[Langfuse](../agents/langfuse.md)** | 开放内核 | MIT + EE | 32.0k | 免费、不限量 | 开源默认解——追踪 + 评估 + prompt 管理合在一个可自托管的平台 |
| **Comet Opik** | 是 | Apache-2.0 | 20.9k | 可以 | 最接近的完全宽松许可对手；评估侧强，Comet 背书 |
| **Arize Phoenix** | **否——源码可见** | **Elastic 2.0** | 10.8k | 可以 | 追踪和漂移分析强，但许可证未获 OSI 认可 |
| **Traceloop / OpenLLMetry** | 是 | Apache-2.0 | 7.3k | 可以 | OpenTelemetry 原生的埋点层；UI 较薄，标准化叙事最干净 |
| **Helicone** | 是 | Apache-2.0 | 6.0k | 可以 | 代理优先——最容易接入，因为它可以挡在 API 调用前面 |
| **W&B Weave** | 仅 SDK | Apache-2.0 | 1.1k | 否（后端 SaaS） | 如果你的 ML 团队本来就住在 Weights & Biases 里，这是自然选择 |
| **LangSmith** | **否——闭源** | SDK 为 MIT | — | 仅企业版 | LangChain 的第一方平台；对 LangChain/LangGraph 集成最深 |
| **Braintrust** | **否——闭源** | SDK 开源 | — | 仅企业版 | 评估优先的工作流，受把 prompt 当 CI 产物的团队欢迎 |

> **这张表里的"开源"是四种不同的东西**——而这正是多数对比含糊带过的区别。Apache-2.0（Opik、Traceloop、Helicone）是真正宽松的。**开放内核**（Langfuse）指核心是 MIT，但治理类功能——RBAC、审计日志、SCIM、SSO、保留策略、脱敏——是商业许可。**源码可见**（Phoenix，Elastic 2.0）允许你读和改，但限制你把它作为服务对外提供，而且*不是* OSI 认可的开源。**闭源**（LangSmith、Braintrust）只公开客户端 SDK。看 LICENSE 文件，别看营销页。

## 怎么选

1. **从你的框架出发，但别停在那儿。** 如果你全押 LangChain/[LangGraph](../agents/langgraph.md)，LangSmith 是阻力最小的路径——你拿开放性换集成深度。其他所有人都该从 [Langfuse](../agents/langfuse.md) 开始，它横跨 [LlamaIndex](../agents/llamaindex.md)、[CrewAI](../agents/crewai.md)、OpenAI Agents SDK、Claude Agent SDK，甚至接 [Claude Code](../agents/claude-code.md)、[Codex](../agents/codex.md)、[Goose](../agents/goose.md)、[Pi](../agents/pi.md) 这些 coding agent。
2. **先判断自托管是硬需求还是偏好。** 如果 prompt 或 trace 里带受监管数据，这一条会迅速收窄选择：Langfuse、Opik、Traceloop、Helicone 都能完全跑在你自己的基础设施上；LangSmith 和 Braintrust 不行，Weave 的后端是 SaaS。
3. **让接入成本匹配你技术栈的成熟度。** Helicone 的代理模式起步最快（把 base URL 指过去就行）。OTel 原生埋点（Traceloop，以及 Langfuse 的 OTel 路径）前期投入更大，但避免锁定，因为 trace 是标准格式。
4. **等你真有东西可评估了再为评估付费。** 数据集和 LLM-as-a-judge 在你有生产流量可采样、有回归要抓的时候才值真金白银——在那之前不值。先上追踪。
5. **签字前先读治理档位。** 这些工具里大部分能让安全评审过关的功能——SSO、RBAC、审计日志、数据脱敏——都是付费的。这是许可问题，不是技术问题，而且它决定的迁移比功能列表决定的多。

## 三个别搞混的点

- **观测不等于评估。** 追踪告诉你发生了什么；评估告诉你好不好。这里大多数工具两样都发，于是很容易买了一个、另一个从没配过——而光有追踪抓不住质量漂移。
- **代理、SDK、OpenTelemetry 是三回事。** Helicone 的代理从 API 边界看流量；SDK 看得到你应用的内部结构；OTel 看你埋了什么、而且可移植。它们产出的 trace 粒度不同，而且这个选择日后很难反悔。
- **面向 agent 不等于是 agent。** 其中几个暴露 MCP server，好让*你的* agent 去查观测数据——[Langfuse](../agents/langfuse.md) 就是，而且还发了一个 Agent Skill。这让它们*可被 agent 访问*，不等于它们是 agent。这个领域里唯一真正的 agent 循环 Langfuse Assistant，操作的是观测工具自己，且仅 Cloud、beta、需批准。

## 市场提示

**ClickHouse 于 2026 年 1 月收购 Langfuse**——这一层迄今最大的整合，也是一个信号：agent 观测正在被吸收进通用数据基础设施，而不是继续作为独立品类存在。Langfuse 方面的表述是它仍然完全开源、路线图不变；请把这当厂商承诺，不是已核实的保证。详见[市场事件](../market-events.md)。

想知道这些工具在给什么装仪表，见[主流 agent 选型矩阵](mainstream-agent-landscape.md)和[能力矩阵](../capabilities/matrix.md)。已收录的开源标杆见 [Langfuse](../agents/langfuse.md)。
