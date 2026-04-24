# Julep

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/julep.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](julep.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Julep is a Temporal-backed workflow engine for building stateful, multi-step AI agent workflows — self-hosted only since the managed cloud shut down.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Julep AI, Inc. |
| Route | Durable workflow engine for stateful AI agents |
| Open source | Yes, Apache 2.0 |
| Best for | Teams that need durable, multi-step agent workflows with persistent memory, branching, loops, and error handling |
| Main cost | Self-hosted only (managed cloud shut down Dec 2025); small team, long-term maintenance risk |
| Official website | https://julep.ai |
| GitHub repo | https://github.com/julep-ai/julep |

## When To Pick It

- You need durable multi-step agent workflows with automatic retries backed by Temporal.
- You want stateful agents with persistent long-term memory and adaptive context management.
- You need declarative task definitions (YAML or code) with branching, loops, parallelism, and error handling.
- You want built-in RAG pipeline and 100+ tool integrations.
- You are comfortable self-hosting Docker, Temporal, and PostgreSQL.

## When Not To Pick It

- You want a managed cloud service. The hosted backend shut down December 31, 2025.
- You need a large, active community for support. Julep's community is modest (~6.6k stars, small team of ~5).
- You have simple single-turn tasks. Julep's workflow engine is overkill.
- You are concerned about long-term maintenance risk from a small vendor.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Durable workflows | Very strong | Temporal-backed with automatic retries |
| Persistent memory | Strong | Long-term memory with adaptive context |
| Declarative tasks | Strong | YAML or code with branching, loops, parallelism |
| RAG pipeline | Medium | Built-in but not as deep as LlamaIndex |
| Tool integrations | Strong | 100+ integrations |
| Managed hosting | None | Cloud shut down; self-hosted only |
| Community size | Weak | ~6.6k stars, small team |

## Operating Cost

Complexity is High. Self-hosting is the only option — you operate Docker containers, Temporal, and PostgreSQL yourself. LLM API costs are pass-through. The small team size means you should evaluate long-term maintenance risk carefully.

## Bottom Line

Julep is a serious workflow engine for stateful agents — if you are comfortable self-hosting and accepting the risk of a small vendor. For teams that need Temporal-grade durability in their agent workflows, it fills a real gap.
