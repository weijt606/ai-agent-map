# Graft

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/graft.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](graft.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Graft is a code context layer that writes your codebase's structure into **linked markdown files your agent reads like any other file** — no embeddings, no database, no index daemon — and wires itself into Claude Code, Codex, Cursor, Gemini CLI and five other agents with one `init`.

> **The distinguishing choice is the storage format, not the retrieval.** [CodeGraph](codegraph.md) indexes a repo into a queryable SQLite database and hands it to agents over MCP; an agent has to *call a tool* to see anything. Graft writes `graft/*.md` — one node per subsystem, with `[[wikilinks]]` between them — and the agent opens, greps and follows them with the file tools it already has. MCP is offered too, but it is the second door, not the only one.

> **It publishes a third-party-graded benchmark, which is rare on this route.** Most context layers report their own harness. Graft reports one of those *and* 50 instances of SWE-bench Verified graded by the official `swebench` 4.1.0 harness — real repos, maintainers' own tests. Read it as a vendor's own run on a 50-instance subset, but read it: the failure mode it documents (baseline patches one file and misses its siblings) is a specific, checkable claim rather than a token-savings percentage.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Trail (`trailhq/Graft`, trailhq.com) — the `trailhq` org was created 2026-08-24; the repo, badges and npm scope still carry the previous NanoNets name |
| Route | Runtime and tools — code context layer for other agents |
| Open source | MIT; npm `@nanonets/graft`, CLI `graft` |
| Implementation | TypeScript on Node; tree-sitter for the structural layer |
| Defining idea | The graph is a folder of linked markdown files in your repo, not a database behind a query API |
| Models | Bring your own — OpenAI-compatible, Anthropic native, OpenRouter, Fireworks, Groq, LiteLLM proxy, or a local model. The structural pass calls no model at all |
| Agents wired | Claude Code (skill file + hooks + statusline + MCP), Codex, OpenCode and other `AGENTS.md` readers, Cursor, Gemini CLI, Copilot, Kiro, Windsurf, Grok, AdaL |
| Languages | 23 — nine at full fidelity (TS/JS, Python, Go, Java, Kotlin, PHP, Swift, R), fourteen at symbol-plus-call-edge fidelity; optional LSP tier for compiler-grade edges |
| Best for | A team on a large repo whose agent burns most of a run rediscovering the codebase, and who wants the artifact to stay readable |
| Main cost | 0.x and moving fast; the graph is a local cache each teammate rebuilds; `init` can write machine-wide Codex config |
| GitHub repo | https://github.com/trailhq/Graft |

## When To Pick It

- **Your agent's cost is exploration, not generation.** The problem Graft names is the one this map keeps seeing in the [coding CLI route](../comparisons/coding-cli-agents.md): every task re-greps, re-opens and re-follows a repo the agent already mapped an hour ago, then throws it away. If your token bills are dominated by reads rather than edits, this is the layer that addresses it.
- **You want the artifact to be legible to humans too.** A node is a markdown file with a plain-English summary, the handful of lines that actually carry the logic, the source files it was built from with content hashes, and typed links (`depends_on`, `part_of`, `uses`, `implements`, `produces`). You can read it, review it, and write your own notes underneath — notes survive regeneration.
- **You do not want an index to babysit.** Every query re-stats the working tree against the last build's fingerprint (~3ms) and rebuilds only what moved, so answers describe the code as it is right now, including uncommitted edits. There is no daemon and no warm index.
- **You want the free tier to actually be free.** `graft build` and `graft check` are deterministic tree-sitter — no model, no key, no network. The LLM pass (`--deep`) that writes summaries and concept nodes is opt-in and runs under your own provider key.
- **You use more than one agent.** One `init` writes each agent's native instruction file rather than a shared lowest common denominator, and `--dry-run` prints every path it would touch before it touches anything.
- **You want the mechanism stated, not just the saving.** The published SWE-bench arm is 33/50 against a cold Claude Sonnet 5 baseline's 27/50 at 23% fewer tokens, and the write-up names the shape of each win rather than averaging it away.

## When Not To Pick It

- **Your repo is small.** An agent that can read the whole thing in a few tool calls gains nothing from a map of it, and you have added a build step.
- **You want one queryable store your tooling can join against.** [CodeGraph](codegraph.md)'s SQLite database is the better shape if something other than an agent needs to ask questions of the index.
- **You need a committed, shared artifact.** `graft build` adds `graft/` to `.gitignore` on purpose — what you commit is the wiring, and every teammate regenerates their own graph (and pays their own enrichment cost) to get the same picture.
- **Machine-wide writes are a problem.** Selecting the Codex host also edits `~/.codex/config.toml`, `~/.codex/hooks.json` and drops a hook shim — user-level, so it applies to every repo you open with Codex. It is labelled in the picker and skippable with `--no-global`, but it is not repo-scoped by default.
- **You need a stable surface.** npm is at `0.19.0` with no tagged GitHub releases, and the project shipped a vendor rename mid-life: the org is `trailhq`, the npm scope is still `@nanonets`, and the README's own badges point at both.
- **You want vendor-neutral governance.** Two accounts carry the overwhelming majority of commits, and the README routes repeatedly to a hosted product (Trail Brain). MIT and forkable is not the same as community-run — the same distinction this map draws for [TrueForge](trueforge.md).
- **Default-on telemetry is a blocker.** One batched anonymous usage ping ships by default. It is documented, inspectable with `graft telemetry debug`, off in CI and in source builds, and disabled by `DO_NOT_TRACK=1` — but it is opt-out, not opt-in.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Tool use | Strong | Six MCP tools (find code, file API, trace calls, find all, repo map, freshness) plus the plain-file path that needs no MCP at all |
| Code execution | Absent | Graft does not run your code; it parses it |
| Memory | Strong | This is the whole product — durable project understanding, regenerated rather than remembered, surviving every session |
| Orchestration | Absent | No loop, no turns; it is a layer under someone else's loop |
| Multi-agent | Medium | Wires eight-plus agents in one command, but each reads the graph independently; nothing coordinates them |
| Human approval | — | Not applicable; `--dry-run` and the file picker are the closest thing |
| Scheduling | Absent | Rebuilds are triggered by queries and post-edit hooks, not by a clock |
| Delivery surfaces | Medium | CLI (`grep`, `map`, `ask`, `viz`), MCP server, and the instruction files it writes into each agent |
| Deployment control | Very strong | MIT, local-only by default, your provider key, and the one network call you did not ask for is documented and disableable |

## Architecture Worth Knowing

The decision everything else follows from is **making the graph files instead of a database**. Once nodes are markdown in the working tree, retrieval stops being a special capability: the agent greps them, opens them, follows `[[wikilinks]]` out of them, with the same tools it uses on source. That removes the failure mode every embedding-based context layer shares — an agent that cannot see the index unless it remembers to call it — and it means the artifact is reviewable by a person, which an embedding table never is.

The second idea is **two tiers with a hard line between them**. Tier one is tree-sitter: every function, class and call edge, deterministic, no model, no key, `$0`. Tier two (`--deep`) is the LLM pass that writes the plain-English summaries and groups files into concept nodes. Separating them is what makes the freshness story work — every query can afford to re-check the tree because that check never calls a model. It is also what makes the project usable before you have decided on a provider.

Third, the node format carries **three depths in one file**: the summary says what the code does, the *crux* — the actual guard, skip condition or state change, stored as text rather than as a line range so it does not drift when unrelated code moves above it — shows how, and content-hashed source references point at the rest. The claim is that this collapses the usual two-step (find the address, then read the file) into one, and it is the part of the design that most directly explains the tool-call reduction the benchmarks report.

## Operating Cost

Low in money, real in habit. The structural graph is free and instant; the enrichment pass is a one-off LLM spend per repo, cached by content hash, with re-runs touching only changed files (the project's own numbers on a 124-file repo: 0.74s cold, 0.18s after one edit). The cost that actually matters is organisational: `graft/` is gitignored, so the graph is per-developer, and every teammate pays their own enrichment. Budget the convention, not the compute — the thing you have to keep alive is the agreement that everyone runs `graft build`.

## Bottom Line

Graft is the clearest current answer to a question the coding-agent route has mostly worked around: **why does every task start by re-learning the repo?** Its answer — write the understanding down as files the agent already knows how to read — is simpler than an index and, unusually, is argued with a third-party-graded benchmark rather than a savings percentage. Weigh it against its age (`0.19.0`, mid-rename, two-author core) and against the fact that the graph is a per-developer cache rather than a shared artifact. Pick it over [CodeGraph](codegraph.md) when you want something readable in the repo and zero infrastructure; pick CodeGraph when you want one queryable store behind MCP. For the route-level view, see [memory approaches](../comparisons/memory-approaches.md) and [the mainstream landscape table](../comparisons/mainstream-agent-landscape.md).
