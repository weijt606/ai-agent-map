# Langfuse

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/langfuse.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](langfuse.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Langfuse is the open-source reference for **watching** agents — an OpenTelemetry-based tracing, evaluation, and prompt-management platform that records what your agent did, scores it, and lets you replay it. It does not run your agent.

> **Boundary — this is not an agent.** Every other profile on this map is something that *acts*. Langfuse is the opposite: a telemetry receiver that sits outside your execution path ("trace events are queued locally and flushed in batches, so your application's response time is not affected"). It observes agents built with [LangChain](langchain.md), [LangGraph](langgraph.md), [CrewAI](crewai.md), [LlamaIndex](llamaindex.md), or a coding CLI — it never replaces one. It is profiled here because "how do I know my agent is working" is a real selection question, not because it competes with the agents.
>
> One genuine exception, scoped narrowly: **Langfuse Assistant** (public beta, Cloud only) is a real agent loop — but it operates *Langfuse itself*, not your application, and it pauses for explicit approval before any change to data or configuration.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Langfuse — **acquired by ClickHouse, January 2026** |
| Route | Observability & evaluation infrastructure (not an agent route) |
| Open source | Open-core — MIT core, commercial `ee/` directories |
| Implementation | TypeScript (server); Python v4 and JS/TS v5 SDKs, everything else via OpenTelemetry |
| License | MIT + Enterprise License (GitHub reports `NOASSERTION` because the file is dual) |
| Self-hostable | Yes, free and unlimited on the OSS tier (Docker / Kubernetes) |
| Best for | Teams running agents in production who need traces, cost/latency data, evals, and prompt versioning in one place they can self-host |
| Main cost | It is another service to operate; the parts enterprises usually want (RBAC, audit logs, SSO, retention, masking) are commercially licensed |
| GitHub repo | https://github.com/langfuse/langfuse |

## When To Pick It

- You have agents in production and cannot answer "what did it actually do, what did it cost, and did it get better or worse last week." Tracing with nested observations, sessions, users, and **agent graphs** is the headline, and token/cost/latency tracking comes with it.
- You want observability you can **self-host for free with no feature ceiling on the core** — tracing, evals, prompt management, datasets, and the SDKs are all MIT. This is the main reason to choose it over [LangSmith](../comparisons/observability-and-evals.md) or Braintrust, which are closed platforms.
- You want evaluation and prompt management in the same tool as tracing: LLM-as-a-judge, code evaluators, human annotation queues, datasets and experiments (including in CI/CD), plus prompt versioning with deployment labels and A/B testing.
- You are framework-agnostic or multi-framework. It integrates with essentially the whole ecosystem this map covers — [LangChain](langchain.md), [LangGraph](langgraph.md), [LlamaIndex](llamaindex.md), [CrewAI](crewai.md), OpenAI Agents SDK, Claude Agent SDK — and, unusually, with coding agents too ([Claude Code](claude-code.md), [Codex](codex.md), [Cursor](cursor.md), [Goose](goose.md), [Pi](pi.md), [OpenClaw](openclaw.md)).
- You are already on ClickHouse, or you expect the observability layer to be consolidated into a data platform you run.

## When Not To Pick It

- You want something that *does* work — this is instrumentation. If you need the agent itself, you are on the wrong page entirely.
- You want a single-vendor stack and already live in one framework's tooling. If you are all-in on LangChain, LangSmith is the path of least resistance (at the cost of it being closed).
- You are a solo developer on one small project. The free Hobby tier (50k units/month, 30 days retention, 2 users) is generous, but running another service for one hobby agent is usually not worth it — read the logs.
- You need enterprise governance **without** paying: RBAC, audit logs, SCIM, server-side data masking, retention policies, and SSO are all behind the Enterprise license on both cloud and self-host.
- You need a documented isolation guarantee for running evaluation code. Code evaluators state their constraints (no network egress, 2-second limit, standard libraries only), but the **sandbox mechanism is not documented** — verify it yourself if that matters.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Observability / tracing | Very strong | The core. OTel-based, nested observations, sessions, users, agent graphs, multi-modal, sampling, masking, environments |
| Evaluation | Strong | LLM-as-a-judge, code evaluators, human annotation queues, datasets and experiments, CI/CD experiments |
| Prompt management | Strong | Versioning, deployment labels, A/B tests, composability, client-side caching for guaranteed availability |
| Cost & latency analytics | Strong | Token and cost tracking, custom dashboards, Metrics API, monitors, spend alerts |
| Ecosystem coverage | Very strong | Dozens of framework integrations plus coding agents; MCP server in both directions and an Agent Skill |
| Deployment control | Strong | Free unlimited self-host, though the governance features are EE-gated |
| Agentic behavior | **Not the goal** | Not in your execution path. The Assistant is Cloud-only, beta, and operates Langfuse itself |

## Operating Cost

Complexity is Medium. Instrumentation is genuinely light — decorate or wrap your calls with the Python/JS SDK, or point any OTel exporter at it — but Langfuse is a stateful service with a database behind it, so self-hosting means you now operate an observability system alongside your agents. Cloud pricing runs Hobby $0 (50k units/month), Core $29/mo, Pro $199/mo, Enterprise $2,499/mo (annual), with graduated overage from $8.00 down to $6.00 per 100k units; self-hosting is free on OSS or custom-priced for Enterprise. The release cadence is fast — roughly 20 tagged releases a month — which is good for fixes and demanding if you pin versions.

> **Two things to verify yourself.** (1) The v4 line is ambiguous: the docs say "Langfuse v4 is live" while GitHub releases still show `v4.0.0-rc.3` alongside a `v3.224.2` stable — check which you are actually installing. (2) Post-acquisition, "remains 100% open source, roadmap unchanged" is a **vendor statement**, not a verifiable fact; the MIT license and continued OSS releases are consistent with it so far, but treat the commitment as a promise rather than a guarantee.

## Bottom Line

Langfuse is the answer to "my agents run, but I have no idea what they're doing" — and the open-source default in a field where the strongest commercial options are closed. Trace first, then add evals and prompt versioning as they earn their place; the fact that all three live in one self-hostable tool is the real argument for it. Just be precise about what you are adopting: this is the layer *under* your agent stack, not part of it, and the enterprise governance features are a paid tier on both deployment paths. For the full field — including which competitors are actually open source, which are merely source-available, and which are closed — see [observability & evaluation](../comparisons/observability-and-evals.md). For what it plugs into, see [LangGraph](langgraph.md), [CrewAI](crewai.md), and [LlamaIndex](llamaindex.md).
