# Paseo

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/paseo.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](paseo.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Paseo is an open-source "agentic development environment" that runs the coding agents you already have (Claude Code, Codex, Copilot, OpenCode, Pi and more) from one daemon, each in its own worktree, with an editor, terminals, diffs and a browser around them. Desktop, mobile, web and CLI clients all connect to that daemon. Agents inside Paseo can also launch and talk to other agents, across providers. It does not ship a model or an agent of its own.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | An independent project (`getpaseo/paseo`, paseo.sh). The LICENSE names Mohamed Boudra as copyright holder; the README says it is "built by one person and funded by the people who use it" |
| Route | Workflow / orchestration layer, across many CLI agents rather than on top of one |
| Repository | [`getpaseo/paseo`](https://github.com/getpaseo/paseo): TypeScript, 25,917 stars as of 2026-11-27 (repo created 2025-10-13). GitHub reports the licence as `NOASSERTION`; the LICENSE file says Paseo is "licensed under the Apache License, Version 2.0" except third-party components, and the README footer says Apache-2.0 |
| Open source | Yes (Apache-2.0). The daemon, Expo mobile/web client, Electron desktop app, CLI and relay are all in the repo; the official relay server is a separate open-source repo, `getpaseo/paseo-relay` |
| Form factor | A local daemon (`packages/server`) plus clients: desktop app for macOS, Windows and Linux, a native iOS and Android app, a web UI, the `paseo` CLI (`npm install -g @getpaseo/cli`), a TypeScript SDK (`@getpaseo/client`) and a Docker image |
| Agents | Native integrations for Antigravity, Claude Code, Codex, fx, GitHub Copilot, Hoplite, Muse Code, Oh My Pi (off by default), OpenCode and Pi; any [Agent Client Protocol](https://agentclientprotocol.com) agent through a generic adapter, with an in-app catalog that lists Cursor, Gemini CLI, Hermes Agent, Kimi, Qwen Code, goose and others |
| Models and billing | Your own agent subscriptions or keys. "you install the underlying CLI. Paseo runs it." The provider pages say Paseo adds no charge for Claude Code or Codex; your plan's normal limits apply |
| Default model | None of its own. You pick a provider and model per agent (for example `paseo run --provider codex/gpt-5.5`), or save them in an agent profile |
| Default safety posture | Daemon listens on `127.0.0.1:6767` with no password; relay off on new installs; Paseo's agent tools off by default (`injectIntoAgents: false`). Agents start in a provider mode: Claude Code in `auto` ("Uses a model classifier to review permission prompts automatically"), or `default` ("Always Ask") under Bedrock or Vertex; Codex in `auto` (`on-request` approvals, `workspace-write` sandbox) |
| Best for | A developer who runs several coding agents, possibly from different vendors, and wants them in parallel worktrees on their own machines, reachable from a phone, and able to delegate to each other |
| Main cost | A daemon to keep running and secure once you leave localhost; no memory layer of its own; a release cadence of several per week (19 GitHub releases from Nov 1 to Nov 27, 2026, four of them pre-releases) |

## What It Is

The README describes Paseo as "an open source agentic development environment for desktop, mobile, web, and CLI." The architecture is client and server: "Paseo runs a local server called the daemon that manages your coding agents. Clients like the desktop app, mobile app, web app, and CLI connect to it." A provider is "the contract between Paseo and one external agent CLI", and the agent binary "runs as a normal subprocess" on the daemon host. On the desktop the daemon starts automatically.

Around those agents it puts:

- **Workspaces and worktrees**: "Run many agents at once, each in its own worktree, on one machine or several." Worktrees can branch off, check out a branch, or check out a PR, and live under `$PASEO_HOME/worktrees` by default.
- **A development workflow**: "Edit files, review diffs, open pull requests, and run terminals, in split panes you arrange how you want", plus a built-in browser in the desktop app.
- **Orchestration**: "Agents in Paseo can create worktrees, launch other agents, and talk to them, across providers." They do this through Paseo tools (delivered natively or over MCP) or by calling the `paseo` CLI from a shell.
- **Schedules and heartbeats**: a schedule "starts a new agent for you on a cron cadence"; a heartbeat "sends a recurring prompt back into one existing agent so it can reassess and continue the same conversation."
- **Voice**: dictation (on by default) and a voice mode (off until enabled). Speech runs locally by default, with OpenAI as an option.
- **Plugins**: they "run on the daemon and show up in every client you connect", and can add UI, hook into the agent lifecycle, answer permissions, or add a provider.
- **Hub** (optional): a separate service that "sits above your daemons so external events, schedules, and webhooks can start agents on those machines". Triggers come from GitHub, Linear, Slack, Discord, schedules and webhooks, and can live in `.paseo/triggers/*.yml`. Hub is open source and self-hostable; there is also a hosted Hub with a Free plan and a paid Pro plan.

## When To Pick It

- You run more than one coding agent, or several sessions of one, and want each in its own worktree with a diff, a terminal and a browser next to it.
- You want agents to delegate to each other across vendors. The docs' examples include implement-then-review and planning with one agent before handing off to another; the bundled skills `/paseo-handoff`, `/paseo-advisor` and `/paseo-committee` package these.
- You want the full app on your phone. The README says "The mobile app is the full app, native on iOS and Android", and pairing goes through an end-to-end encrypted relay or a direct connection (TCP, Tailscale or SSH).
- You want to run agents on a server or VM and drive them from anywhere: `npm install -g @getpaseo/cli`, `paseo`, then point clients or `paseo run --host` at it.
- You want to script agents. The CLI and the TypeScript SDK cover creating agents, waiting for results and following up.
- You care about telemetry. The README says "No telemetry, tracking, or forced login."

## When Not To Pick It

- You use one agent in one terminal and are happy. Run [Claude Code](claude-code.md), [Codex](codex.md) or [OpenCode](opencode.md) directly.
- You need a policy layer that enforces approvals and budgets across agents. Paseo surfaces each agent's own permission requests (in the app, `paseo permit`, or the `respond_to_permission` tool), but the rules come from each provider's mode, and provider modes such as Claude's `bypassPermissions` or Codex's `full-access` skip prompts. [Omnigent](omnigent.md) and [Paperclip](paperclip.md) put approval and budget policy above the agents.
- You want Paseo itself to sandbox agents. It does not: Hub security says Hub "does not sandbox the coding agent process on your machine", and for Docker the docs warn that "Agents can still access whatever code and credentials you mount into the container."
- You want a memory layer. Paseo leaves memory to each agent's own configuration and skills.
- You want to steer the product's direction through code contributions. CONTRIBUTING says "Product, design, architecture, and workflow decisions remain with the maintainer", and points specialized workflows to plugins.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Parallel execution | Very strong | One worktree per agent, on one machine or several (local, SSH, VPN, relay, Docker) |
| Agent breadth | Very strong | Ten native integrations plus any ACP agent; the in-app catalog lists over thirty more |
| Delivery surfaces | Very strong | Desktop on three OSes, native iOS/Android, self-hosted web UI, CLI, TypeScript SDK, voice |
| Coordinated multi-agent | Strong | Agents launch, message and collect results from other agents across providers; the tool route is off by default, the CLI route needs only shell access |
| Scheduling | Strong | Cron schedules and heartbeats in the app, CLI and MCP; event triggers through the optional Hub |
| Review | Strong | Diffs, an editor, pull requests and a desktop browser in the same workspace |
| Human approval | Medium | Pending permission requests can be answered from any client, CLI or MCP; the policy is each provider's mode, and defaults lean toward automatic review |
| Memory | Weak | No memory of its own; idle agents are released after an hour and the next prompt "resumes the same conversation" |
| Governance | Medium | Apache-2.0 and self-hostable end to end, with explicit daemon permissions such as `hub.execute`; decisions rest with a single maintainer |

## Operating Cost

Low to start: download the desktop app and "the daemon starts automatically", with at least one agent CLI installed and signed in. The cost grows when you leave localhost. By default "anyone who can reach the daemon's listening address can connect", so the docs say to set a password before binding to a network address and to "Never bind to 0.0.0.0 without a password". The pairing QR code or link is the trust anchor; the docs say to "Treat the link like a password". The official Docker image binds to `0.0.0.0:6767` inside the container, so set `PASEO_PASSWORD` before publishing the port and scope `/workspace` mounts tightly. Plugins run "unsandboxed with the daemon user's access on the daemon host". Connecting Hub is a separate decision: enrolling a daemon "does not allow Hub to run agents" until you grant `hub.execute`, and that grant lets Hub set "provider permission mode", which "can bypass interactive approval prompts".

## Relationship To The Rest Of This Map

Paseo sits in the same lane as [Orca](orca.md): a workbench that runs agents you already have, one worktree each, with desktop and phone clients. Orca's built-in coordinator/worker orchestration is labelled experimental and off by default; Paseo documents agent-to-agent delegation as a core feature, though its tool injection is also off by default. Orca leaves permissions to each agent's own settings; Paseo also relies on provider modes but routes pending permission requests to its clients, CLI and MCP tools. Against [Paperclip](paperclip.md), Paseo manages agents as workspaces and conversations, not as an organization with goals, budgets and an audit log.

## Bottom Line

Paseo is a good fit if you already run several coding agents and want one place to run them side by side, from your desk or your phone, with agents able to hand work to each other across vendors. It runs on machines you own, sends no telemetry, and is Apache-2.0. The safety model is the agents' own: Paseo forwards their permission prompts, but its defaults (Claude in classifier-reviewed `auto`, Codex in `on-request` with a workspace-write sandbox) and any mode you or Hub pick are what actually gate actions. Set a daemon password before you expose it to a network.

## Sources

- [getpaseo/paseo README](https://github.com/getpaseo/paseo) · [LICENSE](https://github.com/getpaseo/paseo/blob/main/LICENSE) · [CONTRIBUTING](https://github.com/getpaseo/paseo/blob/main/CONTRIBUTING.md) · [Releases (v0.18.0, Nov 27 2026)](https://github.com/getpaseo/paseo/releases)
- Docs: [Why Paseo?](https://github.com/getpaseo/paseo/blob/main/public-docs/why.md) · [Security](https://github.com/getpaseo/paseo/blob/main/public-docs/security.md) · [Configuration](https://github.com/getpaseo/paseo/blob/main/public-docs/configuration.md) · [Providers](https://github.com/getpaseo/paseo/blob/main/public-docs/providers.md) · [Supported providers](https://github.com/getpaseo/paseo/blob/main/public-docs/supported-providers/index.md) · [Claude Code](https://github.com/getpaseo/paseo/blob/main/public-docs/supported-providers/claude-code.md) · [Codex](https://github.com/getpaseo/paseo/blob/main/public-docs/supported-providers/codex.md) · [Orchestration](https://github.com/getpaseo/paseo/blob/main/public-docs/orchestration.md) · [MCP reference](https://github.com/getpaseo/paseo/blob/main/public-docs/mcp.md) · [Schedules](https://github.com/getpaseo/paseo/blob/main/public-docs/schedules.md) · [CLI](https://github.com/getpaseo/paseo/blob/main/public-docs/cli.md) · [Voice](https://github.com/getpaseo/paseo/blob/main/public-docs/voice.md) · [Hub](https://github.com/getpaseo/paseo/blob/main/public-docs/hub/index.md) · [Hosted Hub](https://github.com/getpaseo/paseo/blob/main/public-docs/hub/hosted.md) · [Hub security](https://github.com/getpaseo/paseo/blob/main/public-docs/hub/security.md) · [paseo.sh/docs](https://paseo.sh/docs)
- Source: [Claude provider modes](https://github.com/getpaseo/paseo/blob/main/packages/server/src/server/agent/providers/claude/agent.ts) · [Codex provider modes](https://github.com/getpaseo/paseo/blob/main/packages/server/src/server/agent/providers/codex-app-server-agent.ts)
