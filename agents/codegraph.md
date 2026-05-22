# CodeGraph

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/codegraph.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](codegraph.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: CodeGraph is a local code knowledge graph plus MCP server — it pre-indexes a codebase into a queryable SQLite database so agents like Claude Code, Cursor, and Codex CLI can answer architectural questions with materially fewer tool calls and tokens.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | colbymchenry (open source) |
| Route | Runtime and tools — code knowledge graph / agent context layer |
| Open source | Yes (MIT) |
| Best for | Teams using [Claude Code](claude-code.md), [Cursor](cursor.md), [Codex](codex.md) CLI, opencode, or [Hermes Agent](hermes-agent.md) who want measurably cheaper code exploration |
| Main cost | An extra indexing layer to keep in sync; payoff scales with codebase size and exploration frequency |
| GitHub repo | https://github.com/colbymchenry/codegraph |

## When To Pick It

- You already use [Claude Code](claude-code.md), [Cursor](cursor.md), [Codex](codex.md) CLI, opencode, or [Hermes Agent](hermes-agent.md). CodeGraph plugs in via MCP — no new agent surface to learn.
- Your codebase is large enough that agent exploration costs noticeable tokens per task.
- You want measurable wins on the same exploration workload — the project reports median 35% cheaper, 59% fewer tokens, 49% faster, 70% fewer tool calls across real-world benchmarks.
- You need local-only operation: no external APIs, no cloud, no data transmission.

## When Not To Pick It

- Your codebase is small enough that an agent can scan it directly without a knowledge graph.
- You only use an agent that does not yet speak MCP — there is no value without the connector.
- You need an indexer that handles every exotic language. CodeGraph covers 19+ via tree-sitter; the long tail is not guaranteed.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Cross-agent integration | Very strong | First-class MCP plugins for [Claude Code](claude-code.md), [Cursor](cursor.md), [Codex](codex.md) CLI, opencode, [Hermes Agent](hermes-agent.md) |
| Local-only operation | Very strong | Tree-sitter + SQLite + FTS5 — no external dependencies |
| Language coverage | Strong | 19+ languages including TypeScript, Python, Go, Rust, Java |
| Live syncing | Strong | Native OS file watchers keep the graph current |
| Impact analysis | Strong | Caller/callee tracing, framework-aware routing recognition |

## Operating Cost

Complexity is Low to Medium. Initial indexing happens automatically; the steady-state cost is keeping the database alive and the file watcher running. The payoff scales with how often the agent has to ask "where is this function called?" — for small repos the overhead is not worth it, for medium-to-large repos the token savings dominate.

## Bottom Line

CodeGraph is the first profile in this map dedicated to "agent context infrastructure" — the realization that as agents do more code exploration, the cheapest way to make them better is not to upgrade the agent but to give it pre-computed structure. The MCP-first design slots cleanly into already-tracked agents ([Claude Code](claude-code.md), [Cursor](cursor.md), [Codex](codex.md) CLI, opencode, [Hermes Agent](hermes-agent.md)). If you spend serious tokens on code Q&A, the published 35-70% improvements are the bar to evaluate against.
