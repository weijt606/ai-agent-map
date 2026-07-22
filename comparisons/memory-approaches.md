# Agent Memory Approaches

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/memory-approaches.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](memory-approaches.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

Memory is the axis that separates a stateless tool from an agent that actually knows your project or your life. Through 2026 it became one of the loudest differentiators on this map — [MiMoCode](../agents/mimocode.md) and [jcode](../agents/jcode.md) both lead with it, [Letta](../agents/memgpt.md) is built entirely around it, and it shows up as a headline strength for the self-hosted runtimes.

But "has memory" hides more than it reveals. These projects mean very different things by the word. This page sorts them by *how* they remember, so you can match the mechanism to what you actually need to persist.

## The Six Approaches At A Glance

| Approach | How it remembers | Representative | Best when you need to persist |
| --- | --- | --- | --- |
| Self-editing managed memory | Agent edits its own core / archival / recall stores within the context window | [Letta (MemGPT)](../agents/memgpt.md) | Long-running conversational state that the agent curates itself |
| Passive semantic recall | Every turn embedded as a vector; a memory graph auto-injects relevant history | [jcode](../agents/jcode.md) | Cross-session continuity without calling memory tools by hand |
| File / keyword project memory | Human-readable files (`MEMORY.md`, checkpoints) retrieved by keyword search | [MiMoCode](../agents/mimocode.md), Claude Code (`CLAUDE.md`) | Project understanding that survives runs and stays inspectable |
| Pre-indexed code knowledge graph | Codebase parsed into a queryable graph/DB, queried on demand | [CodeGraph](../agents/codegraph.md) | Architecture-level code context, not conversation |
| Personal-data memory tree | Connectors sync your tools into a hierarchical summary store | [OpenHuman](../agents/openhuman.md) | What the agent knows about *you* — mail, notes, calendar |
| Long-lived runtime memory | Memory as one subsystem of an always-on self-hosted environment | [Hermes Agent](../agents/hermes-agent.md), [Mercury Agent](../agents/mercury-agent.md) | Durable state across channels, devices, and time |

## Self-Editing Managed Memory — [Letta (MemGPT)](../agents/memgpt.md)

The research pattern (MemGPT) made concrete: the agent maintains **core memory**, **archival memory**, and **recall memory**, and edits them with explicit tools to stay useful inside a fixed context window. This is the most principled, most portable design — it is a framework you build stateful agents on, not a finished CLI. The cost is real: extra LLM calls and infrastructure. If your agent's whole job is to remember and self-improve over time, this is the serious open-source baseline.

## Passive Semantic Recall — [jcode](../agents/jcode.md)

jcode embeds each turn as a semantic vector and queries a **memory graph** by cosine similarity, auto-injecting relevant history into the conversation — optionally with a verifier side-agent that checks relevance before injection. The point is that recall happens *without the model calling memory tools*, so it neither forgets nor burns tokens babysitting memory. Explicit memory tools and session search (traditional RAG over past sessions) are still there when you want them. The trade: it is one more subsystem to understand if you want to tune what gets recalled.

## File / Keyword Project Memory — [MiMoCode](../agents/mimocode.md), Claude Code

The pragmatic, transparent end. [MiMoCode](../agents/mimocode.md) keeps a project `MEMORY.md`, automatic session checkpoints, scratch notes, and per-task progress, and injects them back on resume via **SQLite FTS5** keyword search. [Claude Code](../agents/claude-code.md)'s `CLAUDE.md` convention is the lightest version of the same idea. The strength is that the memory is a plain file you can read, edit, and commit — no black box. The limit is keyword retrieval: it recalls what matches, not what is semantically related.

## Pre-Indexed Code Knowledge Graph — [CodeGraph](../agents/codegraph.md)

A different kind of memory: not the conversation, the **codebase**. CodeGraph parses a repo (Tree-sitter + SQLite + FTS5) into a local, queryable knowledge graph and serves it over MCP, so agents like Claude Code, Cursor, and Codex answer architecture questions with far fewer tool calls and tokens. It is context infrastructure you attach to another agent, and it pays off on medium-to-large repos where scanning from scratch is expensive.

## Personal-Data Memory Tree — [OpenHuman](../agents/openhuman.md)

Memory pointed at your life, not your code. [OpenHuman](../agents/openhuman.md) auto-syncs Gmail, Notion, GitHub, Slack, and 118+ tools into a local **Memory Tree** — hierarchical summaries in SQLite, mirrored to an Obsidian-compatible wiki you can browse and edit. The value is that the assistant never starts a session cold about *you*; the cost is that it takes weeks of the auto-fetch loop to build up, and you accept GPL-3.0 and the data-residency question that comes with syncing everything locally.

## Long-Lived Runtime Memory — [Hermes Agent](../agents/hermes-agent.md), [Mercury Agent](../agents/mercury-agent.md)

Here memory is one subsystem inside an always-on, self-hosted environment rather than the whole product. [Hermes Agent](../agents/hermes-agent.md) pairs memory with skills, delegation, and channels; [Mercury Agent](../agents/mercury-agent.md) pairs persistent memory with a permission-hardened, always-on daemon and approval workflows. You get durable state across channels and time, but you also own the daemon, the operations, and the curation.

## How To Choose

1. **Name what must survive.** Conversation state → [Letta](../agents/memgpt.md) or [jcode](../agents/jcode.md). Project understanding → [MiMoCode](../agents/mimocode.md) or the `CLAUDE.md` convention. Code architecture → [CodeGraph](../agents/codegraph.md). Personal data → [OpenHuman](../agents/openhuman.md). Long-lived multi-channel state → [Hermes](../agents/hermes-agent.md) / [Mercury](../agents/mercury-agent.md).
2. **Decide passive vs explicit.** Passive recall ([jcode](../agents/jcode.md), self-editing [Letta](../agents/memgpt.md)) is lower-effort but harder to audit; file-based memory ([MiMoCode](../agents/mimocode.md)) is fully inspectable but only as good as its keyword search.
3. **Watch the hidden cost.** Every memory system trades tokens, LLM calls, or ops burden for continuity. Read the profile's "Operating Cost" section, and weigh it against [cost & benchmarks](cost-and-benchmarks.md).

A vendor-neutral bolt-on layer, [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory), is tracked on the watchlist for teams that want to add memory to an agent that has none. For the capability view, memory is one column in the [capability matrix](../capabilities/matrix.md).
