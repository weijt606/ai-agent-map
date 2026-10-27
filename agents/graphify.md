# Graphify

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/graphify.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](graphify.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Graphify turns a project folder (code, plus docs, SQL schemas, configs, PDFs, images and video if you want them) into a knowledge graph saved as files, `graph.json`, `GRAPH_REPORT.md` and `graph.html`, that your coding agent queries through a `/graphify` skill, a CLI or a local MCP server instead of grepping the source. The code pass is local tree-sitter parsing with no model and no vector store; every edge is labelled with where it came from.

> **Two products share the name.** The open-source part is the `graphifyy` package on PyPI (double y; the README warns that other `graphify*` packages are not affiliated), Apache-2.0, runs locally and needs no account. **Graphify Cloud** is a separate hosted service from the same company (Free, Pro, Teams, Enterprise) that keeps one live graph across repositories and adds PR review, formal verification and Sentry/Jira connectors. The README promotes Cloud heavily, including an "80% fewer tokens" figure; the README does not link a method for that number. Everything below is about the local package unless it says Cloud.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Graphify Labs (graphify.com; the README carries a Y Combinator S26 badge). The repo was created on 2026-04-03 and later moved into the `Graphify-Labs` org, which was created on 2026-06-28; the old `safishamsi/graphify` path redirects |
| Route | Runtime and tools — code knowledge graph / agent context layer |
| Open source | Yes (Apache-2.0); PyPI `graphifyy`, CLI `graphify` |
| Implementation | Python 3.10+; tree-sitter for code, NetworkX node-link JSON for the graph, Leiden (or NetworkX Louvain fallback) for communities |
| Defining idea | A graph you traverse rather than an embedding index you search: each edge is tagged `EXTRACTED`, `INFERRED` (with a confidence score) or `AMBIGUOUS` |
| Inputs | Code and configuration (including SQL, Terraform/HCL, package and MCP manifests) parsed locally; Markdown, PDFs, Office files, images and transcribed audio/video added through an optional semantic pass |
| Models | None for code. The semantic pass uses the assistant's own model when run through the skill, or a configured backend for headless `graphify extract` (Gemini, Kimi, Claude, OpenAI, DeepSeek, Azure OpenAI, Bedrock, Ollama, or the `claude` CLI) |
| Agents wired | [Claude Code](claude-code.md), [Codex](codex.md), [Cursor](cursor.md), [Gemini CLI](gemini-cli.md), [GitHub Copilot](github-copilot.md) CLI and VS Code Copilot Chat, [OpenCode](opencode.md), [Aider](aider.md), [OpenClaw](openclaw.md), [Hermes](hermes-agent.md), [Kimi Code](kimi-code.md), [Pi](pi.md), [Devin](devin.md) CLI, Kiro, Amp, Kilo Code, Factory Droid, Trae, CodeBuddy, Google Antigravity, and the cross-framework `.agents/skills` location |
| Hosted tier | Graphify Cloud: Free ($0, up to 3 indexed repos), Pro ($15/month or $10/month billed annually), Teams ($29/seat/month first-100-teams offer, $40 standard, minimum 2 seats), Enterprise (custom, self-hosted). Prices as listed on the docs pricing page, updated Oct 8 2026 |
| Best for | Developers who want their agent to ask a project-wide graph before opening files, and who want the graph to cover docs and design material alongside the code |
| Main cost | The graph is a snapshot you keep current with hooks, `watch` or `update`; the semantic pass over non-code files spends model tokens; release cadence is fast (0.9.x, several releases a week in October 2026) |
| GitHub repo | https://github.com/Graphify-Labs/graphify |

## How It Works

Running `/graphify .` in an assistant, or `graphify extract` in a shell, writes three files into `graphify-out/`: `graph.json` (the full graph), `GRAPH_REPORT.md` (the most-connected "god nodes", detected communities and suggested questions) and `graph.html` (a clickable force-directed view).

The build has separate paths. **Code** is parsed with tree-sitter locally, with no LLM and nothing sent off the machine; a code-only corpus needs no API key, and `--code-only` or `GRAPHIFY_BACKEND=none` keeps a mixed repo that way. **Audio and video** are transcribed locally with faster-whisper. **Docs, PDFs and images** go through a semantic pass on whatever model the skill's assistant runs, or on the backend you configure. Fragments are then resolved across files, merged into one graph, and clustered into communities. Files are fingerprinted by SHA256, so re-runs only re-extract what changed.

The project's language counts disagree between its own pages — the README says about 40 languages, the older `docs/how-it-works.md` says 25 — so treat the [Supported inputs](https://docs.graphify.com/concepts/supported-inputs) page as the list, and note that it says coverage "varies by construct".

Querying is three verbs over the saved graph: `query` (a scoped subgraph for a plain-language question, with a token budget), `path A B` (shortest path between two concepts) and `explain` (one node and its connections). A name that matches several nodes is refused with the candidates listed rather than guessed. The same graph is exposed by a **local MCP server** (`graphify-mcp`, ten tools such as `query_graph`, `get_neighbors`, `shortest_path` and `god_nodes`) over stdio, or over Streamable HTTP with an API key for a shared endpoint.

To make an assistant use the graph by default, `graphify <platform> install` writes the platform's own mechanism: a hook before search and file-read tools on Claude Code and Gemini CLI, instruction files (`AGENTS.md`, `.cursor/rules/` and so on) elsewhere, and a native extension for Pi. An optional work-memory layer records query outcomes (`graphify save-result`, marked `useful`, `dead_end` or `corrected`) and `graphify reflect` turns them into a `LESSONS.md` that later queries can surface.

Keeping it current is your job: `graphify hook install` rebuilds in the background after commits and branch switches, `graphify watch` rebuilds on file changes, and the docs say to run `graphify update .` after a pull or merge.

## How It Differs From CodeGraph And Graft (Trail Code)

All three parse a repository with tree-sitter and hand the result to an existing coding agent. They differ in where the result lives and how the agent reaches it.

- **[CodeGraph](codegraph.md)** stores its index in a local SQLite database (with FTS5) and serves it over MCP; the agent sees it by calling a tool. Its scope is source code.
- **[Graft](graft.md)** (now Trail Code) writes the graph as linked markdown files in `graft/`, one node per subsystem with `[[wikilinks]]`, which the agent reads with its ordinary file tools; MCP is a second route. `graft/` is gitignored by design, so each developer rebuilds their own copy.
- **Graphify** writes a single `graph.json` plus a report and an HTML view, queried through a skill and CLI or through its own MCP server. Its team guide offers committing `graphify-out/graph.json` with a pre-commit hook and a union merge driver, building per clone, or running a shared MCP server. Its scope reaches past code into docs, PDFs, images and media through the optional semantic pass, and every edge carries a provenance tag. A markdown wiki (`--wiki`) and Obsidian export are available, but the graph's native form is JSON, not files the agent browses.

## When To Pick It

- **Your agent spends its turns finding its way around.** The skill and hooks point the assistant at `graphify query` before it greps or opens files one by one.
- **Design docs, ADRs, specs or papers sit next to the code.** Graphify maps them into the same graph and links `# NOTE:` / `# WHY:` comments and ADR/RFC citations to the code they explain.
- **You want to know what was read and what was guessed.** `EXTRACTED`, `INFERRED` with a confidence score, and `AMBIGUOUS` are on every edge; the docs also warn that dynamic dispatch, generated code and stale scans leave gaps.
- **You need a code-only build to stay offline.** Code parsing needs no key and no network; `GRAPHIFY_BACKEND=ollama` keeps the semantic pass local too.
- **You use several assistants.** One `graphify install --platform <name>` per assistant, with project-scoped installs (`--project`) that write files you can commit.
- **You want a shared graph without a hosted service.** Committing `graph.json` or running `graphify-mcp` over HTTP inside your network are both documented paths.

## When Not To Pick It

- **Your repo is small.** The project's own token table shows roughly no reduction on a 6-file corpus; the value it claims grows with corpus size.
- **You want the graph to be a set of files the agent reads directly.** That is [Graft](graft.md)'s design; Graphify's graph is JSON behind a query interface.
- **You want benchmarks run by someone else.** The published numbers (LOCOMO recall@10 0.497, LongMemEval-S 76%, 82.0% key-fact coverage on a six-question ERPNext suite) come from Graphify's own harness, last updated 2026-07-05. Two of the three suites measure conversational memory rather than code navigation.
- **Your data cannot reach a model provider.** Docs, PDFs and images are sent to the assistant's model or the configured backend; auto-detection picks a provider from whichever API key is set (it prints which one), and the README notes that the Kimi backend routes to Moonshot servers in China. Pin `--backend` or use `GRAPHIFY_BACKEND=none`.
- **A local query log is a problem.** There is no telemetry, but every `query`, `path`, `explain` and MCP `query_graph` call is logged to `~/.cache/graphify-queries.log` by default (question, corpus, nodes returned, duration); `GRAPHIFY_QUERY_LOG_DISABLE=1` turns it off.
- **You want vendor-neutral governance.** One account holds 1,217 commits against 158 for the next contributor, and the README routes repeatedly to the paid Cloud product.

## Bottom Line

Graphify is a local, Apache-2.0 context layer that builds a provenance-tagged knowledge graph from a project and puts it in front of the coding agent through a skill, hooks, a CLI and an MCP server. What separates it from the two code-graph layers already in this map is scope (docs, PDFs and media in the same graph) and storage (one `graph.json` that the team can commit, with a merge driver, rather than a SQLite index or a folder of markdown). Weigh it against a fast-moving 0.9.x release line, self-reported benchmarks, and a README that is also a funnel for a hosted product. For the route-level view, see [memory approaches](../comparisons/memory-approaches.md).

## Sources

- [GitHub repository and README](https://github.com/Graphify-Labs/graphify) · [Releases (v0.9.96, Oct 26 2026)](https://github.com/Graphify-Labs/graphify/releases) · [LICENSE (Apache-2.0)](https://github.com/Graphify-Labs/graphify/blob/v8/LICENSE) · [BENCHMARKS.md](https://github.com/Graphify-Labs/graphify/blob/v8/BENCHMARKS.md) · [docs/how-it-works.md](https://github.com/Graphify-Labs/graphify/blob/v8/docs/how-it-works.md)
- Docs: [How Graphify works](https://docs.graphify.com/concepts/architecture) · [Supported inputs](https://docs.graphify.com/concepts/supported-inputs) · [Connect the graph MCP server](https://docs.graphify.com/mcp/overview) · [MCP tool reference](https://docs.graphify.com/reference/mcp-tools) · [Serve a graph over HTTP](https://docs.graphify.com/mcp/shared-http) · [Keep the graph current](https://docs.graphify.com/guides/incremental-updates) · [Record useful findings](https://docs.graphify.com/guides/work-memory) · [Share context with your team](https://docs.graphify.com/guides/team-workflows) · [Plans and pricing](https://docs.graphify.com/pricing/overview)
