# Agent Harness Frameworks

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/agent-harness-frameworks.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](agent-harness-frameworks.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

A "harness" is the minimal scaffolding around an LLM that turns it into an agent — the loop, the tool surface, the permission model, the skills hook. These are projects you can fork, audit, and own end-to-end, rather than vendor products you adopt as-is.

Current star totals for all nine live in the [rankings boards](../rankings/README.md); this page compares shape, not size.

Three shapes now sit under this route. **Single-loop harnesses** *are* the loop — you fork one and own it. **Meta-harnesses** run several of those loops under one layer, and are what you reach for once "which harness" stops being a single answer. **Harness-as-a-server** runs one loop, but behind an API, and is what you reach for when the agent belongs to your product rather than to your terminal.

## At A Glance

| Project | License | Sweet spot | Footprint |
| --- | --- | --- | --- |
| [Pi](../agents/pi.md) | MIT (TS) | Terminal-first coding harness with broad LLM provider coverage | Small core + opt-in skills/extensions |
| [jcode](../agents/jcode.md) | MIT (Rust) | Fast, low-footprint terminal harness for multi-session workflows, with passive semantic memory | Lean Rust binary — fastest boot / lowest RAM in class |
| [OpenHands](../agents/openhands.md) | Open source | Full open-source SWE agent (CLI + GUI + cloud option) | Heaviest — closer to a product |
| [SWE-agent](../agents/swe-agent.md) | MIT (Py) | Research reference behind SWE-bench, single-YAML config | Medium; upstream moving focus to mini-swe-agent |
| [mini-swe-agent](../agents/mini-swe-agent.md) | MIT (Py) | ~100-line successor; SWE-bench Verified >74% | Tiny — readable in one sitting |
| [OpenHarness](../agents/openharness.md) | MIT (Py) | 10-subsystem open harness with anthropics/skills + MCP + 43 tools | Medium; production-shaped, sibling to [CLI-Anything](../agents/cli-anything.md) |

## Meta-Harnesses

These do not ship a loop of their own. They run the harnesses above (and vendor products like [Claude Code](../agents/claude-code.md) and [Codex](../agents/codex.md)) behind one interface, and add the things a bare loop leaves out: identity, approval policy, sandboxing, scheduling, and a place other people can watch from.

| Project | License | Runs | The unit it optimizes for | Watch out for |
| --- | --- | --- | --- | --- |
| [QM](../agents/qm.md) | MIT (TS) | Pi, OpenCode, Codex, Claude Code | **A company.** Scope = a person, channel, group message, or project, each with its own memory, files, keychain, permissions, crons, and durable sandbox | Days old; a real deployment to operate (Postgres, sandboxes, your own cloud account); contributions accepted as written proposals, not code |
| [Omnigent](../agents/omnigent.md) | Apache-2.0 (Py) | Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, custom YAML agents | **A developer.** Session = the unit; it follows you across terminal, browser, phone, and desktop, and can run in one of nine cloud sandbox providers | Self-declared **alpha**; prerequisite chain spans three language ecosystems (`uv`, Node, tmux, `bwrap` on Linux) |

The distinction that matters when choosing between them: QM assumes **many people share one deployment** and gives each of them isolation; Omnigent assumes **one person drives many agents** and gives them continuity and policy. Neither is a substitute for the other.

## Harness-As-A-Server

One loop, run as a service. You do not fork it and you do not point it at other harnesses — you deploy it, connect providers to it once, and call it over HTTP from your own product.

| Project | License | Front doors | The unit it optimizes for | Watch out for |
| --- | --- | --- | --- | --- |
| [TrueForge](../agents/trueforge.md) | MIT (TS) | Bundled chat UI, HTTP API + TypeScript SDK, embeddable UI SDK | **Your product's backend.** Models, MCP servers, skills, and the sandbox are connected once from catalogs; agents pick from what an operator allowed | Six weeks public, still on 0.x release candidates; contributor base is almost entirely one company; sandboxing is Daytona-only today; no scheduling and no channel adapters |

The reason this is a separate shape and not a footnote on the single-loop list: putting the loop behind an API boundary forces choices the forkable harnesses never have to make. Session state must be persisted rather than held in a process, the tool surface must be declared centrally rather than passed per call, and approvals must be renderable to whoever holds the client — which is why they arrive as Generative UI rather than a terminal prompt. TrueForge is also the only entry on this route that argues its case with a **reproducible cost comparison** (14 cross-system tasks against [Claude Managed Agents](../agents/claude-managed-agents.md) and deepagents, same model and MCP servers, harness in `benchmark/`) rather than a feature list. Treat that as a vendor benchmark and read it anyway.

## How To Choose

- Pick by footprint, not by stars. The right harness is the one whose surface area you are willing to maintain.
- If you want the smallest credible base to fork: [mini-swe-agent](../agents/mini-swe-agent.md).
- If you want a production-shaped open runtime to self-host: [OpenHarness](../agents/openharness.md).
- If you want to publish SWE-bench numbers: [SWE-agent](../agents/swe-agent.md) is the canonical reference; mini-swe-agent is the working successor.
- If you want a terminal-first day-to-day coding harness: [Pi](../agents/pi.md), or [jcode](../agents/jcode.md) if speed, low RAM across many sessions, and built-in passive memory are the priorities.
- If you want a more complete SWE agent product that is still open source: [OpenHands](../agents/openhands.md).
- If the question is no longer "which harness" but "how do several of them behave under one policy": [Omnigent](../agents/omnigent.md) for one developer across devices, [QM](../agents/qm.md) for a whole team in Slack and the web. Both add a dependency in the middle of your agent loop — take that on when you genuinely run more than one harness, not before.
- If the agent is a **feature of your product** rather than a tool on your machine — it needs an API, a login, and an approval surface your users can see: [TrueForge](../agents/trueforge.md). The trade is that you now operate Postgres, Redis, and a sandbox provider; the loop is the part you stop operating.
