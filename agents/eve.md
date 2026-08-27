# eve

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/eve.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](eve.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: eve is Vercel's open framework for building agents — an agent is a *directory of files* (instructions, tools, skills, subagents, channels, schedules, connections), and the production parts most teams assemble by hand (durable execution, per-agent sandboxes, approval gates, evals) ship inside the framework rather than beside it.

> **The filesystem is the API.** Vercel's own framing is "Next.js for agents": you declare what the agent does in conventional locations and the framework owns the rest. That makes an eve project unusually readable — you can diff an agent's capabilities in a pull request — and it makes the framework, not your glue code, responsible for restarts, approvals, and isolation.

> **Open source, but the production path runs through Vercel.** The repo is Apache-2.0 and the package is plain npm, so nothing stops you reading or forking it. The documented deployment story, however, is `vercel deploy` as an ordinary Vercel project, with sandboxes and model access through Vercel's AI Gateway. Self-hosting is not documented as a supported path. Weigh that before treating it as a neutral framework choice.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Vercel (`vercel/eve`, eve.dev) — launched June 17 2026 at Vercel Ship, as part of the Agent Stack |
| Route | Build-your-own platform — production-batteries-included agent framework |
| Open source | Apache-2.0, published to npm as `eve` |
| Implementation | TypeScript on Node; durable execution built on the open-source Workflow SDK |
| Defining idea | An agent is a directory: `instructions.md`, `tools/`, `skills/`, `subagents/`, `channels/`, `schedules/`, `connections/` |
| Models | Any model through AI Gateway, with provider fallbacks; MCP servers and OpenAPI-compatible APIs as tools |
| Surfaces | Slack, Discord, Teams, GitHub, Linear, Telegram, Twilio, HTTP — one agent, many channel adapters |
| Best for | A product team building a *durable, long-running* agent as an application, who would otherwise write the session, sandbox, and approval plumbing themselves |
| Main cost | Public preview since June 2026, and a deployment story centered on Vercel |
| GitHub repo | https://github.com/vercel/eve |

## When To Pick It

- You are building an agent **as a product**, not as a script. Sessions checkpoint through the Workflow SDK and survive crashes *and redeploys* — the failure mode that kills most hand-rolled long-running agents.
- You want **approval as a framework primitive**. Any tool can declare `needsApproval`; a paused agent waits indefinitely without consuming compute, so human-gated steps are not a bespoke queue you have to build.
- You want **isolation you did not have to design**. Every agent gets its own sandbox, so model-generated code runs away from your application runtime by default.
- You want **subagents with their own context windows**, callable like tools — the standard way to keep a long task from drowning one context.
- You want **evals in the repo**, not in a spreadsheet: `defineEval` gives scored suites you can run locally or in CI alongside the agent they test.
- You want **one agent across many channels**. Channels are adapter files, so Slack, Discord, Teams, GitHub, Linear, Telegram, Twilio, and plain HTTP are configuration rather than separate deployments — rare in this route, where most frameworks stop at the library boundary.
- You want scheduled autonomy: `defineSchedule` puts cron work in the same tree as everything else.

## When Not To Pick It

- You want a coding agent. eve builds agents; it does not sit in your terminal editing your repo. Use [Claude Code](claude-code.md), [Codex](codex.md), or [Pi](pi.md) for that.
- **You need to self-host as a first-class path.** The documented route to production is Vercel. If deployment control is a hard requirement, [LangGraph](langgraph.md), [Pydantic AI](pydantic-ai.md), or a [harness framework](../comparisons/agent-harness-frameworks.md) leave you holding the runtime.
- You are not a TypeScript shop. The framework is TS end to end; Python teams should look at [LangGraph](langgraph.md), [CrewAI](crewai.md), or [LlamaIndex](llamaindex.md).
- You want a graph you control step by step. eve's abstraction is a directory and a durable session, not an explicit state machine — [LangGraph](langgraph.md) is the opposite trade.
- You need something with a long production track record. It has been public since June 2026; the framework is young even if the company is not.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Tool use | Very strong | Typed `defineTool` functions, MCP servers, and OpenAPI-compatible APIs, all as first-class tools |
| Code execution | Strong | Per-agent sandbox isolates agent-generated code from the application runtime |
| Durable state | Strong | Checkpointed sessions on the Workflow SDK survive crashes and deploys — durability, not a memory system |
| Orchestration | Very strong | Durable sessions, subagents, schedules, and approvals as framework primitives |
| Multi-agent | Strong | Subagents with isolated context windows, invoked like tools |
| Human approval | Very strong | `needsApproval` on any tool; paused runs cost nothing while they wait |
| Scheduling | Strong | `defineSchedule` cron tasks in the project tree |
| Delivery surfaces | Very strong | Eight-plus channel adapters from one agent definition |
| Deployment control | Medium | Apache-2.0 and forkable, but the documented production path is Vercel |
| Evaluation | Strong | `defineEval` scored suites, local or CI |

## Architecture Worth Knowing

The whole design collapses into one rule: **conventional locations beat configuration**. `agent/instructions.md` is the always-on system prompt; `agent/tools/*.ts` are typed functions; `agent/skills/*.md` are procedures loaded on demand rather than always resident; `agent/subagents/` are child agents with their own context; `agent/channels/*.ts` bind the agent to a platform; `agent/schedules/*.ts` are cron jobs; `agent/connections/` hold credentialed service integrations. `agent/agent.ts` picks the model. Nothing about the layout is novel on its own — the bet is that standardizing it is what makes agents reviewable and operable by people who did not write them.

Underneath, durable execution comes from the open-source **Workflow SDK**, which is what lets a session outlive a deploy rather than merely a crash. One small but telling detail: the `eve` npm package ships its own documentation to `node_modules/eve/docs`, so a coding agent working in your repo can read the framework's docs locally instead of guessing — the framework is designed on the assumption that agents will be maintaining it.

## Operating Cost

Low to medium, and unusually front-loaded toward *decisions* rather than plumbing. `npx eve@latest init` scaffolds a working project and a terminal UI, and there is no infrastructure to stand up before the first run. The recurring costs are model spend through AI Gateway, sandbox compute, and platform costs on Vercel — which is also where the lock-in sits. Read the Vercel dependency as the price of the batteries: the reason you are not writing checkpointing and sandbox lifecycle yourself is that someone else is running them.

## Bottom Line

eve is the clearest statement yet that the interesting layer has moved from *the loop* to *everything around the loop*. Its contemporaries on this route hand you primitives and leave durability, isolation, approvals, and channels as your problem; eve treats those as the framework's job and treats the agent itself as a directory you can read in a pull request. That makes it the strongest build-your-own option on this map for delivery surfaces and human approval, and the weakest for deployment control — the trade is explicit and it is the whole decision. If you want the graph under your hands, see [LangGraph](langgraph.md); if you want to own the runtime instead of the abstraction, see [agent harness frameworks](../comparisons/agent-harness-frameworks.md). For the route-level view, see [build-your-own frameworks in the capability matrix](../capabilities/matrix.md#build-your-own-frameworks).
