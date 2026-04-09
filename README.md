# AI Agent Map

中文：
AI Agent Map 是一个开源知识库，用来帮助开发者和构建者选择可实际落地的 AI agent。它不做产品包装，不做“未来主义”路线图，也不替任何项目做营销。

English:
AI Agent Map is an open-source knowledge base for developers and builders who need to choose AI agents that can be used in real work. It is not a product, not a framework, and not a marketing layer.

Repository: https://github.com/weijt606/ai-agent-map

License: MIT

## 项目定位 | Positioning

中文：
这个仓库回答的不是“什么是 agent”，而是“遇到具体问题时，应该选哪一类 agent”。因此它既收录可以直接执行任务的 agent，也收录真正影响选型的 agent 平台、运行时和 orchestration 系统。

English:
This repository is not trying to define AI agents in the abstract. It tries to answer a narrower question: given a real problem, what kind of agent should you use? That is why it includes both execution agents and the platforms, runtimes, and orchestration systems that materially affect the choice.

## 它解决什么问题 | What Problem This Solves

中文：
今天关于 AI agent 的信息很多，但对工程选型并不友好，常见问题有三类：

- 只讲架构，不讲实际能做什么。 It explains architecture but not practical capability.
- 只列链接，不告诉你什么时候该用、什么时候别用。 It lists links but does not explain fit and anti-fit.
- 把 demo、研究项目、实验框架和可落地系统混在一起。 It mixes demos, research projects, experimental frameworks, and deployable systems.

English:
The current agent landscape is noisy. Most resources are either architecture-heavy, too shallow to be useful, or indiscriminate about what counts as usable in practice. This repo is meant to reduce that noise.

## 这和 Awesome List 有什么不同 | How This Is Different From Awesome Lists

| Question | Typical awesome list | AI Agent Map |
| --- | --- | --- |
| 主要单位 | Link collection | Decision support |
| 关注点 | Coverage breadth | Practical fit |
| 条目内容 | Short description | Capability boundary, use cases, anti-fit, complexity |
| 是否包含闭源产品 | Often inconsistent | Yes, if they matter in real selection decisions |
| 输出结果 | “有哪些项目” | “这类问题该选什么” |

中文：
如果一个框架或平台会真实影响工程决策，它也会被收录。比如 LangGraph 不是现成 agent，但很多团队真正要决定的是“买一个 agent”还是“自己搭一个 agent system”，这就是选型问题。

English:
If a framework or platform changes a real engineering decision, it belongs here. LangGraph is a good example: many teams are not choosing between two end-user agents, but between buying an agent and building an internal agent system.

## 如何使用这个仓库 | How To Use This Repo

1. 从真实问题开始，而不是从技术名词开始。 Start with a real problem, not a buzzword.
2. 先看 [use-cases](use-cases/README.md)，找到接近你的任务类型。 Read [use-cases](use-cases/README.md) first and find the scenario closest to your task.
3. 再看 [agents](agents/README.md)，理解候选 agent 的能力边界和反向适配。 Then read [agents](agents/README.md) to understand capability boundaries and anti-fit.
4. 如果你已经知道自己关心的能力维度，再去看 [capabilities](capabilities/README.md)。 If you already know which dimensions matter, use [capabilities](capabilities/README.md).
5. 最后再看 [comparisons](comparisons/README.md)，做相近方案之间的取舍。 Use [comparisons](comparisons/README.md) last to narrow between similar options.

## 如何找到适合你的 Agent | How To Find Your Agent

中文：
如果你只看一段，请看这里。

1. 你是想“直接把任务交给 agent 执行”，还是“搭一个系统来编排 agent”？
2. 你更需要“托管服务减少运维”，还是“自托管与自定义控制”？
3. 你想要“agent 自主推进”，还是“人主导 review 和合并”？
4. 你的任务更像“单个 coding 任务”，还是“长期运行、有状态、可恢复的工作流”？
5. 你需要的只是代码自动化，还是还需要消息渠道、调度、设备控制、MCP 等外围能力？

English:
If you only read one section, read this one.

1. Are you handing work directly to an agent, or building a system that orchestrates agents?
2. Do you prefer a managed service with less ops, or self-hosting with more control?
3. Do you want autonomy-first execution, or review-first human control?
4. Is your workload a single coding task, or a long-running, stateful workflow?
5. Do you only need coding automation, or also messaging, scheduling, device control, or MCP extensions?

### 快速分类 | Quick Routing

- 想直接把工程任务交给 agent 执行。 Start with `execution` agents such as [Devin](agents/devin.md).
- 想让多个 provider 或 agent 围绕任务板协作，并保留人工 review。 Start with `automation` systems such as [Froge Code](agents/froge-code.md).
- 想让 agent 有 delegation、subagents 或并行工作流。 Start with `multi-agent` systems such as [Hermes Agent](agents/hermes-agent.md).
- 想自己搭建状态机、审批流、长期运行 agent。 Start with `platform` systems such as [LangGraph](agents/langgraph.md) or [OpenClaw](agents/openclaw.md), depending on whether you need a framework or a runtime.

## 仓库结构 | Repository Structure

| Path | Purpose |
| --- | --- |
| [agents](agents/README.md) | 每个 agent 一个独立页面，记录能力、边界、复杂度和实战备注。 One page per agent with capability, fit, anti-fit, complexity, and usage notes. |
| [use-cases](use-cases/README.md) | 从真实问题出发的选型指南。 Problem-first guides that help readers choose from a use case. |
| [capabilities](capabilities/README.md) | 跨 agent 的能力维度词汇表。 Shared capability vocabulary across agents. |
| [comparisons](comparisons/README.md) | 只在有具体决策意义时做对比，不做无意义排行榜。 Scenario-based comparisons, not generic leaderboards. |

## 标准评估框架 | Agent Evaluation Framework

中文：
所有 agent 页面都尽量遵循同一个最小结构，避免“每个条目写法都不一样”。

English:
All agent pages follow the same minimal evaluation structure so that entries remain comparable.

必填字段 | Required fields:

- `name`
- `category` (`execution` / `automation` / `multi-agent` / `platform`)
- `capabilities`
- `best use cases`
- `not suitable for`
- `complexity level`
- `real-world usage notes`

完整说明见 [agents/evaluation-framework.md](agents/evaluation-framework.md)。

## 当前覆盖 | Current Coverage

中文：
仓库现在已经覆盖一批主流 agent、agentic coding 工具、runtime 和 orchestration 项目，既包含闭源产品，也包含开源框架与平台。

English:
The repository now covers a first mainstream set of coding agents, agentic coding tools, runtimes, and orchestration projects across both closed-source and open-source ecosystems.

| Agent | Category | Open Source | Focus |
| --- | --- | --- | --- |
| [Claude Code](agents/claude-code.md) | execution | No | 本地和 IDE 优先的 agentic coding workflow |
| [Claude Managed Agents](agents/claude-managed-agents.md) | automation | No | Anthropic 管理式 / 云端执行工作流映射 |
| [Codex](agents/codex.md) | execution | Mixed | 云端隔离环境中的异步 coding agent |
| [GitHub Copilot](agents/github-copilot.md) | platform | No | VS Code / CLI / cloud 多形态 agent 平台 |
| [Cline](agents/cline.md) | execution | Yes | 编辑器内、强审批、强工具接入的 coding agent |
| [OpenHands](agents/openhands.md) | execution | Yes | 可自托管、可云端部署的 AI-driven development agent |
| [Devin](agents/devin.md) | execution | No | 托管式端到端软件工程执行 |
| [Hermes Agent](agents/hermes-agent.md) | multi-agent | Yes | 自托管 memory + skills + subagents agent |
| [OpenClaw](agents/openclaw.md) | platform | Yes | 多渠道、多设备、本地优先 agent runtime |
| [LangChain](agents/langchain.md) | platform | Yes | 快速搭建自定义 agent 的高层框架 |
| [LangGraph](agents/langgraph.md) | platform | Yes | 状态化、长期运行 agent system 的底层框架 |
| [Froge Code](agents/froge-code.md) | automation | Yes | 按 Automagik Forge 暂定映射的 review-first 平台 |

补充对比见 [comparisons/mainstream-agent-landscape.md](comparisons/mainstream-agent-landscape.md)。

## 贡献方式 | Short Contribution Guide

中文：
欢迎贡献，但请保持这个仓库的问题导向。

English:
Contributions are welcome, but the repository should stay problem-first.

- 优先提交真实可用系统，不优先收录概念 demo。 Prefer real, usable systems over concept demos.
- 描述能力边界，不要复制官网 marketing 文案。 Describe capability boundaries instead of copying vendor marketing.
- 必须写清楚“适合什么”和“不适合什么”。 Every entry must state both fit and anti-fit.
- 如果项目名称、定位或成熟度存在歧义，要明确写出来。 If naming, positioning, or maturity is ambiguous, say so explicitly.
- 文档以中文为主，保留英文对应内容。 Chinese is primary, with English kept alongside it.

## 当前状态 | Current Status

中文：
这是仓库的第一版可公开基础版，已经具备统一的分类方式、评估框架、首批主流条目和首个 use case 指南。后续会继续补更多主流 agent 页面、纵向 use case 和高价值 comparison，而不是做无差别大列表。

English:
This is the first public baseline. It already includes a consistent structure, evaluation framework, a mainstream starting set of profiles, and an initial use-case guide. Next iterations should expand coverage through high-value agent pages, use cases, and comparisons rather than a blind link dump.