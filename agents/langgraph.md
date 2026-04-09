# LangGraph

[![中文](https://img.shields.io/badge/中文-查看中文版-9ca3af?style=flat-square)](../zh/agents/langgraph.md)
[![English](https://img.shields.io/badge/English-Current%20Page-1f6feb?style=flat-square)](langgraph.md)

One-line take: LangGraph is for teams that already know they need durable, stateful, recoverable agent workflows and are prepared to build them.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | LangChain |
| Route | Low-level orchestration framework |
| Open source | Yes |
| Best for | Durable state, approval steps, and recoverable workflows |
| Main cost | Highest design and operations burden |
| Official entry | https://docs.langchain.com/oss/python/langgraph/overview |

## When To Pick It

- You need checkpointing, state, approval, and recovery as framework-level primitives.
- You are building an internal agent platform, not just trying a tool.
- You accept that this is platform engineering work.

## When Not To Pick It

- You want a ready-to-run coding agent today.
- You do not have engineering bandwidth for tools, prompts, evals, and observability.
- Your workload is simple enough for a script or managed product.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Durable execution | Strong | One of the core reasons to use it |
| Memory | Strong | Good fit for long-running workflows |
| Human-in-the-loop | Strong | Interrupts and approvals are natural here |
| Multi-agent orchestration | Strong | Useful for complex collaboration flows |
| Ready-to-run UX | Low | It is infrastructure, not a finished agent |

## Operating Cost

Complexity is High. The power comes from control, and the bill for that control is system design, testing, and runtime observability.

## Bottom Line

LangGraph is valuable because it lets you build your own agent system, not because it saves you from making engineering decisions.