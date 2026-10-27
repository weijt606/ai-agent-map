# Paperclip

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/paperclip.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](paperclip.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Paperclip is an open-source, self-hosted control plane that runs a team of AI agents the way a company runs staff. Agents get roles, reporting lines and budgets; work arrives as tickets tied to goals; recurring jobs run on schedules; and approvals, spend limits and an audit log sit on top. It does not build agents. You bring Claude Code, Codex, OpenClaw, Hermes or any other agent that "can receive a heartbeat", and Paperclip manages the organization they work in.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Paperclip Labs, Inc. (`paperclipai/paperclip`, paperclip.ing) |
| Route | Workflow / orchestration layer, organized around tickets and an org chart rather than a single agent's session |
| Repository | [`paperclipai/paperclip`](https://github.com/paperclipai/paperclip): MIT, TypeScript, 107.9k stars as of 2026-10-28 |
| Open source | Yes (MIT). "Open source. Self-hosted. No Paperclip account required." |
| Form factor | A Node.js server with a React web UI and an embedded PostgreSQL database; installed with `npx paperclipai@latest onboard --yes` or Docker |
| Agents | Adapters for OpenClaw, Claude Code, Codex, Cursor (and Cursor Cloud), Gemini CLI, OpenCode, Pi, Hermes (and Hermes Gateway), Grok Build and Kimi Code, plus custom processes, HTTP endpoints and adapter plugins |
| Models | Chosen per agent; since `v2026.1023.0`, agents can also run through your own gateway (OpenRouter, Amazon Bedrock, Google Gemini, or any OpenAI Responses, Anthropic Messages or Chat Completions endpoint) |
| Hosted tier | A "Paperclip Cloud" waitlist is linked from the README; the site describes no pricing, and the README roadmap marks "Cloud deployments" as in progress |
| Best for | Someone running many agents on ongoing work (code, but also research, operations and content) who needs to know who is doing what, what it costs, and what needs sign-off |
| Main cost | A server and a database to operate, a new concept set (companies, heartbeats, routines, governance), and releases that regularly carry breaking changes |

## What It Is

The README describes it as "a Node.js server and React UI that orchestrates a team of AI agents to run a business", and adds: "It looks like a task manager. Under the hood: org charts, budgets, governance, goal alignment, and agent coordination." The flow it advertises is three steps: define a goal, "hire" a team of agents into roles (CEO, CTO, engineers, marketers), then approve the strategy, set budgets and monitor from a dashboard.

The README is direct about what it is not: "Not an agent framework. We don't tell you how to build agents. We tell you how to run a company made of them." Agents bring their own prompts, models and runtimes.

## How It Works

- **Tasks and goals.** Work is tracked as issues linked to a project, a parent and a company goal, so "agents see the 'why,' not just a title". A single assignee and execution locks ("atomic task checkout") stop two runs from claiming the same task.
- **Heartbeats.** Agents do not run continuously. A database-backed wakeup queue wakes an agent for assigned work, follow-up messages, or an optional timer, checks its budget, prepares its workspace and secrets, loads skills, and calls the adapter.
- **Routines.** Recurring tasks with cron, webhook and API triggers, plus concurrency and catch-up policies. Each run creates a tracked issue and wakes the assigned agent.
- **Governance.** Board approval workflows, review and approval stages on tasks, approval of new "hires", and pause, resume or terminate for any agent. Config changes are revisioned and can be rolled back.
- **Cost control.** Token and cost tracking by company, agent, project, goal, provider and model, with warning thresholds and hard stops. The README notes that enforcement uses recorded spend, so "usage reporting and in-flight work can delay a stop".
- **Connections and tools.** GitHub, Notion, Railway or your own MCP server, behind a tool gateway where each action is set to Allowed, Ask first, or Off.
- **Workspaces.** Project repositories with optional isolated git worktrees, plus sandbox providers for running agents off the host (the roadmap names e2b, Cloudflare, Daytona, Modal, Novita and self-hosted Kubernetes).
- **Multi-organization.** One deployment can host several companies, each with separate tasks, agents, permissions and history, and an organization can be exported and imported as a package.

## When To Pick It

- You have many agents running on recurring or long-lived work and are losing track of them. The README's own example is "20 simultaneous Claude Code terminals open".
- You want spend limits that pause an agent, not just a bill at the end of the month.
- You want humans in the loop at defined points (plan approval, task review, a risky tool call) rather than on every step.
- Your agents do more than code: support, reporting, research or social posts on a schedule, assigned to an owner with history you can inspect.
- You want to mix harnesses and models in one team and keep tasks, skills, permissions and history in one place regardless of which agent did the work.

## When Not To Pick It

- You want to watch a few coding agents work side by side in worktrees and review their diffs. That is a workbench, not a company: see [Orca](orca.md).
- You need a framework to build an agent's own loop. Paperclip says it is not one; see the [agent harness framework](../comparisons/agent-harness-frameworks.md) route.
- You want a single agent to get stronger on its own. Use the agent directly ([Claude Code](claude-code.md), [Codex](codex.md), [OpenClaw](openclaw.md)) or a layer built for it ([oh-my-claudecode](oh-my-claudecode.md)).
- You want long-term agent memory as a feature. "Memory / Knowledge" is still marked in progress on the roadmap; what exists today is persistent task context and session resume.
- You want a managed service today. Paperclip Cloud is a waitlist.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Work orchestration | Very strong | Goal-linked tickets, atomic checkout, blockers, delegation along the org chart |
| Governance and approval | Very strong | Approval stages, hire approval, Ask-first tool gateway, revisioned config with rollback |
| Scheduling | Very strong | Routines with cron, webhook and API triggers; timer heartbeats |
| Multi-agent | Very strong | Mixed human and agent org chart, multi-harness and multi-model teams |
| Cost control | Strong | Scoped budgets with warnings and hard stops, based on recorded spend |
| Execution | Medium | Worktrees and sandbox providers, but the actual work happens inside each adapter's agent |
| Delivery surfaces | Medium | Web UI usable on phones; Slack, Discord, Telegram and AgentMail connectors are experimental; no desktop app yet (on the roadmap) |
| Memory | Weak | Persistent task context and session resume; memory and knowledge are on the roadmap |

## Operating Cost

Medium. The local path is one command and an embedded Postgres, and it defaults to trusted loopback mode. Production means your own Postgres, authenticated mode, and a private-network bind (the README suggests Tailscale) or Docker. Node.js 24.11+ is required; subscription sign-in for Claude and Codex also needs Python 3 and the provider CLIs on the host. Releases are date-versioned and frequent, and recent ones open with breaking changes: `v2026.1012.0` required stopping every old process before upgrading, and `v2026.1023.0` widened what the Operator role can do. Read the release notes before every upgrade. Anonymous usage telemetry is **on by default**; `PAPERCLIP_TELEMETRY_DISABLED=1` or `DO_NOT_TRACK=1` turns it off.

## Bottom Line

Paperclip treats a fleet of agents as a management problem: who owns which task, why it matters, what it may spend, and who signs off. If you already have agents that work and your problem is coordination, cost and accountability, it gives you that as a self-hosted MIT server, without a vendor account. If your problem is making one agent better at coding, it is the wrong layer. Long-term memory is still on the roadmap, and the hosted version is still a waitlist.

## Sources

- [paperclipai/paperclip README](https://github.com/paperclipai/paperclip) · [LICENSE](https://github.com/paperclipai/paperclip/blob/master/LICENSE) · [Releases (v2026.1023.0, Oct 23 2026; v2026.1012.0)](https://github.com/paperclipai/paperclip/releases)
- [paperclip.ing](https://paperclip.ing) · [Cloud waitlist](https://paperclip.ing/waitlist/) · Docs: [Approvals](https://docs.paperclip.ing/guides/day-to-day/approvals/) · [Costs](https://docs.paperclip.ing/guides/day-to-day/costs/) · [Routines](https://docs.paperclip.ing/guides/projects-workflow/routines/) · [Deployment modes](https://docs.paperclip.ing/reference/deploy/deployment-modes/) · [Adapters](https://docs.paperclip.ing/reference/adapters/overview/)
