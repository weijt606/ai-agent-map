# MemGPT (Letta)

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/memgpt.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](memgpt.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: MemGPT (now Letta) is a platform for building stateful AI agents with persistent memory that learn and self-improve over time.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Letta, Inc. |
| Route | Stateful agent platform with persistent memory |
| Open source | Yes, Apache 2.0 |
| Best for | Agents that need to remember across sessions — long-running assistants, personalized workflows, context that grows over time |
| Main cost | Memory management adds extra LLM calls; self-hosting requires Docker and PostgreSQL |
| Official website | https://www.letta.com |
| GitHub repo | https://github.com/letta-ai/letta |

## Naming

MemGPT is the research-paper design pattern (self-editing memory for LLMs). Letta is the framework, company, and product built on that pattern. The original `cpacker/MemGPT` repo now redirects to `letta-ai/letta`.

## When To Pick It

- You need agents that remember across sessions — not just within a conversation, but across days and weeks.
- You want automatic context management that works within fixed context windows by self-editing memory.
- You need stateful agents that maintain core memory, archival memory, and recall memory.
- You want agents that learn from past experience and improve over time (Skill Learning).
- You need git-based versioning for agent memory (Context Repositories).

## When Not To Pick It

- You already use LangGraph, CrewAI, or AutoGen and want to add a memory layer. Letta replaces your agent stack, not slots in beside it.
- You need multi-agent orchestration or visual debugging out of the box.
- Your tasks are stateless and short-lived — everything fits in a single context window.
- You want the simplest possible memory solution. Mem0 is lighter.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Persistent memory | Very strong | Core memory + archival memory + recall memory |
| Context management | Very strong | Self-editing memory tools to work within context windows |
| Statefulness | Very strong | State persists across sessions |
| Skill learning | Strong | Agents improve from past experience |
| Memory versioning | Medium | Context Repositories with git-based versioning |
| Multi-agent orchestration | Weak | Not the primary focus |
| Visual debugger | Weak | Limited tooling compared to alternatives |

## Operating Cost

Complexity is Medium to High. Self-hosting requires Docker and PostgreSQL. The MemGPT architecture adds extra LLM calls for memory management operations (reading, writing, searching memory), which increases token spend compared to stateless approaches. Baseline hosting cost is around $5–10/month on Railway, plus LLM API costs.

## Bottom Line

If your agent needs to remember, Letta is the most serious open-source option. The trade-off is clear: you get true persistent memory and self-improving agents, but you pay in extra LLM calls and infrastructure complexity.
