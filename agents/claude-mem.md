# claude-mem

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/claude-mem.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](claude-mem.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: claude-mem is a memory layer you add to an existing agent. Lifecycle hooks record what the agent does, a model compresses that into observations and summaries, and the relevant ones are injected back at the start of the next session, with MCP search tools for digging further.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Alex Newman ([@thedotmack](https://github.com/thedotmack)) and contributors |
| Route | Runtime and tools — cross-session memory layer for other agents |
| Repository | [`thedotmack/claude-mem`](https://github.com/thedotmack/claude-mem) — Apache-2.0, TypeScript; 103.6k stars as of 2026-10-28 |
| Open source | Open core. The engine, Claude-Mem Server, CLI, SDKs, adapters, and MCP tools are Apache-2.0; hosted cloud, team/org sync, SSO, and other enterprise features are reserved as commercial |
| Paid tier | **CMEM Pro** (hosted observer, cloud sync, private MCP link): 30-day trial, then $30/month; Heavy $70/month, Max $100/month with billed overage |
| Works with | [Claude Code](claude-code.md) (plugin marketplace), [Codex](codex.md), [OpenCode](opencode.md) (1.3.4+, including 2.x), [OpenClaw](openclaw.md) gateways, [Pi](pi.md), [DeepSeek Harness](deepseek-harness.md), [Grok Bot](grok-bot.md), T3 Code, Antigravity CLI, Oh My Pi; the repo description also lists Gemini, [Hermes](hermes-agent.md), and Copilot |
| Best for | Developers who want project continuity across sessions without writing memory files by hand |
| Main cost | A local worker (Bun) plus Chroma for vector search; memory generation itself costs model calls, paid either on your plan, your own key, or the hosted observer |
| Current release | v15.3.0 (2026-10-26); install with `npx claude-mem install` |
| Website | https://cmem.ai · docs https://docs.claude-mem.ai |

## How It Works

Six lifecycle hooks (`SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`, `SessionEnd`) send what the agent does to a local **worker service**, an HTTP API with a web viewer, managed by Bun. An **observer** model turns the raw tool use into typed observations and session summaries, stored in **SQLite** with FTS5 keyword search and a **Chroma** vector database for hybrid semantic search. At the next `SessionStart`, the relevant context is injected automatically.

For deeper recall, the agent uses MCP tools in three steps the project calls progressive disclosure: `search` returns a compact index (about 50–100 tokens per result), `timeline` shows what happened around a hit, and `get_observations` fetches full details only for the chosen IDs. The README estimates this at roughly 10x token savings compared with fetching everything. Content wrapped in `<private>` tags is excluded from storage.

**Who runs the observer.** On a first install, the installer asks you to sign in to claude-mem in the browser (email magic link) and then pick a provider: the hosted claude-mem observer (CMEM Pro, which the vendor pitches as moving memory generation off your agent's subscription), your own OpenRouter or Gemini key, or your Anthropic plan. Passing `--provider`, setting `CLAUDE_MEM_ONLINE_OPTIN=false`, or running in CI skips the sign-in. The Grok Bot integration defaults to the hosted service. The README says sign-in needs no card, but the pricing page says the trial requires a credit or debit card.

## When To Pick It

- You want an agent to start each session knowing what happened in the last one, without maintaining `CLAUDE.md` or memory files by hand.
- You switch between harnesses and want one memory store for all of them. The project ships adapters for Claude Code, Codex, OpenCode, Pi, DeepSeek Harness, OpenClaw, and others.
- You want recall that is cheap in tokens: an index first, full details only on request.
- You are fine running a local worker, and you either have a model key for the observer or are willing to pay for the hosted one.

## When Not To Pick It

- You want memory you can read and edit as plain files. claude-mem stores it in SQLite and Chroma behind a web viewer; for a file-based approach see [MiMoCode](mimocode.md) or the `CLAUDE.md` convention.
- You do not want session activity leaving your machine. Local operation works, but the default install path steers you towards the hosted observer, and cloud sync stores your data with CMEM.
- You need team-shared memory today on an open licence. Team/org sync is reserved as commercial, and the TeamBrain pilot has no announced public pricing.
- You want code-structure context rather than history. That is what [CodeGraph](codegraph.md) and [Graft](graft.md) are for.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Cross-session memory | Very strong | Automatic capture through hooks, compressed observations, injection at session start |
| Retrieval | Strong | SQLite FTS5 plus Chroma hybrid search; three-step MCP recall |
| Cross-agent integration | Strong | Adapters and installers for a dozen harnesses, at different depths (Grok Bot, for instance, works by watching chat log files) |
| Privacy controls | Medium | `<private>` tags, credential redaction, an opt-out from the online sign-in |
| Local-only operation | Medium | Supported, but you supply the observer model and opt out of the hosted default |
| Standalone runtime | Not the goal | It remembers for an agent; it does not act |

## Operating Cost

Complexity is Medium. The installer sets up Bun, uv (for vector search), the hooks, and the worker, and a `doctor` command handles repair. The recurring cost is the observer: every session is summarised by a model, billed to your Anthropic plan, your OpenRouter or Gemini key, or CMEM Pro at $30/month and up. Releases are frequent. The project went from v15.0.2 to v15.3.0 between 2026-10-23 and 2026-10-26, so expect to update often.

One more thing to know before adopting it: the README ends with a section, "What About CMEM?", stating that CMEM is a crypto token "created by a 3rd party but officially embraced by the creator of Claude-Mem", with a contract address on Base. The cmem.ai product pages do not mention it. It does not change how the software works, but it is part of the project's public identity.

## Bottom Line

claude-mem is a bolt-on version of the passive-recall pattern: you keep your agent and add hooks that remember for it. If your pain is "every session starts cold", it addresses that directly and works across many harnesses. Before you sign in, decide where you want the observer to run, because the open-source engine and the hosted product are deliberately separate.

## Sources

- [claude-mem README](https://github.com/thedotmack/claude-mem#readme) · [Releases](https://github.com/thedotmack/claude-mem/releases) · [LICENSE (Apache-2.0)](https://github.com/thedotmack/claude-mem/blob/main/LICENSE) · [docs/license.md](https://github.com/thedotmack/claude-mem/blob/main/docs/license.md) · [docs/ip-boundary.md](https://github.com/thedotmack/claude-mem/blob/main/docs/ip-boundary.md) · [cmem.ai](https://cmem.ai/) · [cmem.ai pricing](https://cmem.ai/pricing) · [Documentation](https://docs.claude-mem.ai/)
