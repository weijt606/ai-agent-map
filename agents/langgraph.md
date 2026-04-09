---
name: "LangGraph"
vendor: "LangChain"
category: "platform"
open_source: true
complexity: "high"
verification: "verified-public-project"
last_reviewed: "2026-04-09"
description: "Low-level orchestration framework for building stateful, long-running agent systems."
description_zh: "用于构建状态化、长期运行 agent system 的底层 orchestration framework。"
homepage: "https://docs.langchain.com/oss/python/langgraph/overview"
repo: "https://github.com/langchain-ai/langgraph"
---

# LangGraph

中文：
LangGraph 不是现成 agent，而是构建 agent system 的底层 orchestration framework。它适合那些已经确定自己需要长期运行、可恢复、可审计的 agent workflow 的团队。

English:
LangGraph is not a ready-to-use agent. It is a low-level orchestration framework for building agent systems. It fits teams that already know they need long-running, resumable, and auditable agent workflows.

## 基本信息 | Snapshot

| Field | Value |
| --- | --- |
| Name | LangGraph |
| Vendor | LangChain |
| Category | platform |
| Open Source | Yes |
| Complexity | High |
| Delivery Model | Library / framework |
| Homepage | https://docs.langchain.com/oss/python/langgraph/overview |
| Repo | https://github.com/langchain-ai/langgraph |

## 能力画像 | Capability Profile

| Capability | Assessment | Notes |
| --- | --- | --- |
| Durable execution | Strong | Public docs position resumable, failure-tolerant execution as a core differentiator. |
| Memory | Strong | Supports both working memory and persistent memory patterns. |
| Human-in-the-loop | Strong | Public docs explicitly support interrupt and approval patterns. |
| Multi-agent orchestration | Strong | Graph and subgraph patterns make delegation and coordination possible. |
| Tool use | Medium | Tool use is powerful but depends on what you integrate; LangGraph itself is infrastructure, not a turnkey tool runtime. |
| Ready-to-run UX | Low | It is not a packaged end-user agent. You still have to build the agent behavior and operator experience. |

## 最适合的使用场景 | Best Use Cases

- 想自己搭建可恢复、有状态、可审计的 agent workflow。 Good for teams building resumable, stateful, and auditable agent workflows.
- 需要审批流、人工介入、长任务恢复和复杂控制逻辑。 Useful when you need approval steps, human intervention, recovery, and complex control flow.
- 想把 agent 当成内部平台能力，而不是买现成成品。 Good when the real decision is to build an internal agent platform instead of buying a packaged agent.

## 不适合的场景 | Not Suitable For

- 今天就想立刻拿到一个现成 coding agent。 Not a fit if you want a ready-to-run coding agent today.
- 没有工程资源维护 prompts、tools、memory policy、eval 和 observability。 Weak fit if you lack engineering capacity to maintain prompts, tools, memory policy, evals, and observability.
- 任务简单到脚本、单 agent 工具或托管产品就能解决。 Overkill for simple workloads that a script, a single agent tool, or a managed product can already solve.

## 复杂度判断 | Complexity

中文：
复杂度为 High。LangGraph 的价值来自可控性和可塑性，而这两点都要求团队自己承担设计和运维成本。

English:
Complexity is High. LangGraph is valuable because it is controllable and flexible, and both of those advantages require the team to own design and operations.

## 实战备注 | Real-World Usage Notes

- LangGraph 的强项是“让你搭出自己的 agent system”，不是“替你决定 agent 怎么工作”。 LangGraph is strong at letting you build your own system, not at deciding the agent behavior for you.
- 如果你对 checkpoint、state、approval、recovery 很在意，它通常比现成工具更合适。 If checkpointing, state, approval, and recovery matter, it is often a better fit than a packaged tool.
- 真正的难点不在 API，而在 workflow 设计、测试和运行期可观测性。 The real difficulty is not the API surface, but workflow design, testing, and runtime observability.