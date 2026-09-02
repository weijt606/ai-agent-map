# TrueForge

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/trueforge.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](trueforge.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: TrueForge is an agent harness you **deploy and call over HTTP** rather than a loop you fork — the model calls, MCP tools, `SKILL.md` packs, sandbox, approvals, subagents, and session state all run inside a server that exposes a chat UI, a REST API with a TypeScript SDK, and an embeddable UI SDK.

> **The third shape on this route.** A single-loop harness ([Pi](pi.md), [mini-swe-agent](mini-swe-agent.md)) *is* the loop, and you own it by forking it. A meta-harness ([QM](qm.md), [Omnigent](omnigent.md)) drives several other loops under one policy. TrueForge is neither: it runs **one** loop, but it runs it as a service with an API in front of it. The unit it optimizes for is not a repository or a person — it is **your product's backend**.

> **It publishes reproducible cost numbers, which almost nothing on this route does.** TrueForge benchmarks itself against [Claude Managed Agents](claude-managed-agents.md) and deepagents on 14 cross-system tasks from DevRev's Enterprise-Bench, same model and same MCP servers, and ships the harness to reproduce it in `benchmark/`. Read the numbers as a vendor's own benchmark — but read them, because a competitor's cost curve stated on the record is rarer than it should be.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | TrueFoundry (`truefoundry/trueforge`, trueforge.dev) — public since late July 2026 |
| Route | Agent harness framework — harness-as-a-server |
| Open source | MIT; npm `@truefoundry/trueforge` plus `-core`, `-sdk`, `-ui`; Helm chart |
| Implementation | TypeScript on Node ≥ 22.14 |
| Defining idea | The harness is a deployable server with three front doors: chat UI, HTTP API + SDK, embeddable UI |
| Models | OpenAI, Anthropic, Google Gemini, other catalog providers, or any OpenAI-compatible endpoint |
| Tools | Remote MCP servers with header auth or OAuth, including in-chat authorization; git-backed `SKILL.md` packs loaded on demand |
| Isolation | Sandbox-as-a-tool (Daytona today, more providers stated as planned), provisioned only when needed; secrets stay in the harness |
| Deployment | Local mode (one process, SQLite, `npx`) or hosted mode (Postgres + Redis; Docker Compose, Helm, or Railway), with optional OIDC |
| Best for | A team putting an agent behind their own product, who want the loop, sandbox, and approvals as infrastructure they run |
| Main cost | Six weeks public and still on 0.x release candidates; the contributor base is almost entirely one company |
| GitHub repo | https://github.com/truefoundry/trueforge |

## When To Pick It

- You are **embedding an agent in a product**, not running one in your terminal. The HTTP API and the embeddable `@truefoundry/trueforge-ui` are the primary interfaces; the bundled chat UI is a convenience, not the point.
- You want **the harness to be infrastructure you operate**. Postgres and Redis, a Helm chart, and optional OIDC are the give-away: this is designed to be a service in your cluster with a login, not a binary on a laptop.
- You want **configuration from catalogs rather than code**. Models, MCP servers, skills, and the sandbox are set up once from shipped YAML catalogs you can override; agents then pick from what you connected. That is a real operational difference from frameworks where each agent re-declares its own providers.
- You want **secrets to stay out of the sandbox**. Code and file execution is isolated as a *tool*, provisioned on demand, with credentials held by the harness rather than handed to the model's execution environment.
- You want **human checkpoints as product features**, not debug prompts: tool approval, ask-user-questions, and Generative UI all render inside the chat surface your users see.
- You care about **context cost** and want to see the working. The published comparison has TrueForge on Opus 4.8 solving 10.7/14 tasks at **$8.6 per run against Claude Managed Agents' $11.8** at the same accuracy, and on GLM-5.2 solving 11.7/14 at **$3.0** — with 3.7M tokens per run against deepagents' 16.5M on the same model, attributed to fewer tool calls (19 vs 32–40), deferred tool loading, and compaction rather than replay.

## When Not To Pick It

- **You want a coding agent.** TrueForge runs agents; it does not sit in your repository editing files. Use [Claude Code](claude-code.md), [Codex](codex.md), or [Pi](pi.md) for that.
- **You want the smallest thing you can read.** This is the opposite end of the route from [mini-swe-agent](mini-swe-agent.md). If the goal is to understand a loop end to end in one sitting, start there.
- **You need production maturity.** Public since late July 2026, versions are `0.x` and the current tags are release candidates. The README itself warns that local mode has no login by default and belongs on localhost only.
- **You need vendor-neutral governance.** MIT and forkable, but the commit history is overwhelmingly TrueFoundry staff, and fork PRs are asked to change source only because maintainers regenerate the SDK after merge. That is a company's project published openly, not a community one — a different risk from [eve](eve.md)'s (where the licence is open and the *deployment* is the lock-in), and worth naming separately.
- **Your isolation requirement names a provider.** Sandboxing runs on Daytona today; additional providers are stated as planned, not shipped.
- **You want scheduled autonomy or multi-channel delivery.** There is no cron primitive and no Slack/Discord/Telegram adapter set — [eve](eve.md) and [QM](qm.md) are the entries on this map that treat those as framework concerns.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Tool use | Very strong | Remote MCP with header auth or OAuth and in-chat authorization; catalogs; deferred tool loading and Code Mode to keep the surface off the context |
| Code execution | Strong | Sandbox as a tool, provisioned on demand; secrets held by the harness, not the sandbox |
| Memory | Weak | Session state and compaction are durability and context engineering, not a memory system — nothing here learns across sessions |
| Orchestration | Very strong | Subagents, deferred tools, large-result offloading, compaction, persisted sessions |
| Multi-agent | Medium | Subagents inside one harness; it does not drive other harnesses the way a meta-harness does |
| Human approval | Very strong | Tool approval and ask-user-questions are first-class and render in the end-user surface |
| Scheduling | Absent | No cron primitive |
| Delivery surfaces | Medium | Chat UI, HTTP API + TypeScript SDK, embeddable UI SDK — real surfaces, but no channel adapters |
| Deployment control | Very strong | MIT, self-hosted by design; SQLite locally or Postgres + Redis via Docker Compose, Helm, or Railway, with optional OIDC |

## Architecture Worth Knowing

The design decision that produces everything else is **putting the loop behind an API boundary**. Once the harness is a server, session state has to be persisted rather than held in a process, tools have to be declared centrally rather than passed in per call, and approvals have to be renderable to whoever is holding the client — which is why they arrive as Generative UI rather than a terminal prompt. The scale-down and scale-up modes fall out of the same choice: local mode is the same server with SQLite instead of Postgres and no login.

The second idea worth extracting is **catalogs as the configuration unit**. Models, MCP servers, skills, and sandboxes are connected once, from YAML you can customize, and agents select from what is available. That inverts the usual framework assumption that an agent definition carries its own provider configuration, and it is what makes a shared deployment governable: the set of things any agent can reach is an operator's decision, not a developer's.

Third, the context engineering is unusually explicit for a project this young — **deferred tool loading, Code Mode, large-result offloading, and compaction rather than replay** are named as features, and the benchmark attributes most of the cost gap to exactly those. Whether or not the published numbers hold up in your workload, the fact that the cost story is stated as a mechanism rather than a claim is the useful part.

## Operating Cost

Medium, and honest about it. `npx @truefoundry/trueforge@latest` gets you running with no infrastructure, but that path is explicitly not the deployment — the moment more than one person uses it you are running Postgres, Redis, and an OIDC provider, plus a sandbox provider account. Against that, the recurring model spend is the number the project is competing on, and it publishes a reproducible harness for checking it. Budget the operations, not the loop: the loop is the part TrueForge is taking off your hands.

## Bottom Line

TrueForge answers a question the harness route had been answering only by accident: **what if you want to own the loop but not host it in your terminal?** The single-loop harnesses give you something to fork; the meta-harnesses give you a policy layer over several of them; TrueForge gives you a running service with an API, a login, and an approval surface your users can see. That makes it the natural pick when the agent is a feature of your product rather than a tool on your machine — and it is the only entry on this route that argues its case with a reproducible cost comparison instead of a feature list. Weigh it against its age and its single-company contributor base, not against its licence: MIT is not the same as community-governed. For the route-level view, see [agent harness frameworks](../comparisons/agent-harness-frameworks.md) and [the harness rows in the capability matrix](../capabilities/matrix.md#own-the-loop-harness-frameworks). If you want the framework rather than the server, see [eve](eve.md); if you want the graph under your hands, see [LangGraph](langgraph.md).
