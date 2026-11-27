# NanoClaw

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/nanoclaw.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](nanoclaw.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: NanoClaw is a self-hosted, always-on assistant built as one small Node host process that runs every agent session in its own Docker container. By default the agents run Claude through Anthropic's Claude Agent SDK, and you reach them from chat apps. Its pitch is isolation by container instead of by permission checks, and customization by editing your own fork with a coding agent instead of by configuration.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | The `nanocoai` GitHub organization (site [nanoclaw.dev](https://nanoclaw.dev)). The LICENSE reads "Copyright (c) 2026 Gavriel" |
| Route | Self-hosted / local runtime |
| Repository | [`nanocoai/nanoclaw`](https://github.com/nanocoai/nanoclaw): MIT, TypeScript, 31,172 stars as of 2026-11-27 (repo created 2026-01-31) |
| Open source | Yes (MIT). The README says the base will accept "Only bug fixes, security fixes, simplifications and code reductions"; new capabilities are contributed as skills |
| Form factor | A Node host process plus per-session agent containers (Docker on macOS, Linux or Windows via WSL2), installed with `bash nanoclaw.sh`. Trunk ships a terminal channel; chat-app channels are added with `/add-<channel>` skills. Managed with the `ncl` CLI |
| Models and billing | Bring your own credential, kept in a credential gateway rather than in the container. Claude is the default runtime; Codex (ChatGPT subscription or API key), Cursor (Cursor account or API key) and OpenCode (OpenRouter, Google, DeepSeek, local OpenAI-compatible servers and more) are alternatives, configurable per agent group. An optional free NanoClaw account unlocks a prebuilt hardened image and a managed Slack app |
| Default model | Claude through the Claude Agent SDK. The source says "Model and reasoning effort pass to the SDK verbatim; the SDK owns defaults", so a group with no model set gets the SDK's default. For Codex, the 2026.11.0 notes say "Groups with no model set start new threads on GPT-6.1 Sol with an API key and on GPT-6.2 Sol with a ChatGPT login" |
| Best for | One person, or people who trust each other, who want an assistant on their own machine that answers in chat apps, runs scheduled jobs, and keeps each agent's files, memory and shell inside its own container |
| Main cost | You run Docker, a credential gateway and a fork you are expected to change with a coding agent. Inside its container the agent runs without per-tool prompts, and outbound network traffic is open unless you turn on egress lockdown |
| Docs | [docs.nanoclaw.dev](https://docs.nanoclaw.dev) · [repo docs](https://github.com/nanocoai/nanoclaw/tree/main/docs) (the in-repo architecture doc is labelled "Draft — design intent, not a line-by-line spec") |

## What It Is

The README describes it as *"An AI assistant that runs agents securely in their own containers. Lightweight, built to be easily understood and completely customized for your needs."* Architecturally, "A single Node host orchestrates per-session agent containers." A message from a chat app is routed by the host to an agent group and a session, written to that session's `inbound.db`, and picked up by the agent-runner inside the container. The reply goes into `outbound.db`, and the host delivers it back through the channel adapter. The README calls this "Two SQLite files per session, each with exactly one writer".

Around that loop it puts:

- **Tools**: Claude Code's tools inside the container, MCP servers, web search and fetch, and a pinned `agent-browser` CLI in the agent image. An agent can ask to install packages or add an MCP server; both go through an admin approval.
- **Memory**: every agent group has "persistent, file-based memory: plain Markdown files". The memory doc says "There is no database and no embedding store." Two files (`index.md` and `system/definition.md`) are injected whenever a fresh context window starts, each capped at 16k characters. The agent maintains the rest by following links.
- **Scheduled tasks**: one-off or cron-recurring jobs, managed with `ncl tasks` or from chat. They can have optional script gates: a Bash script that decides whether to wake the agent, so "`wakeAgent: false` completes the run without calling the model."
- **Multiple agents**: agents message each other through `send_message` to an agent destination, and since 2026.11.0 "Agents can create other agents from templates." With a NanoClaw account, each Slack agent can get its own Slack app; the README says you can "Spawn teammates from chat: every one gets its own bot identity, container, and memory".
- **Isolation levels**: per channel, you can give a chat its own agent group, share one agent across separate sessions, or fold several channels into one shared session ([isolation model](https://github.com/nanocoai/nanoclaw/blob/main/docs/isolation-model.md)).

## When To Pick It

- You want the agent's shell and file access confined by a container, not by in-app checks. The security doc says agents run as an unprivileged user, "only explicitly mounted directories are visible", and "The project root is **never mounted**".
- You want API keys kept out of the agent's reach. "Real API credentials **never enter containers**". A credential gateway (OneCLI's Agent Vault by default, or Iron Proxy) injects them per request, and "with none registered the host refuses to start".
- You want one assistant across many chat apps. The README lists WhatsApp, WhatsApp Cloud API, Telegram, Discord, Slack, Microsoft Teams, Mattermost, Signal, iMessage, Matrix, Google Chat, Webex, Linear, GitHub, WeChat, Delta Chat, Dial (SMS and voice calls), Emacs and email via Resend, each installed on demand.
- You want different people's chats kept apart. Separate agent groups get "Separate containers, separate session databases, separate everything."
- You are comfortable changing code. The README's stance is "Customization = code changes", and you "make your own fork and have your coding agent modify it".
- You want Claude Code's harness as the default, with the option to move a group to Codex, Cursor or OpenCode.

## When Not To Pick It

- **You want a prompt before every risky command.** The Claude provider runs with `permissionMode: 'bypassPermissions'`. The source comment says "Claude runs unrestricted inside the container: NanoClaw's container isolation and the credential gateway's allow-list are the security boundary, not the SDK's own permission prompts." Approval cards exist, but only for privileged actions such as creating an agent from a default-scope group, installing packages, adding an MCP server, held agent-to-agent messages, and credentialed requests the gateway is configured to hold. The docs add: "If the gateway has no rule asking for approval, the host side never fires".
- You need network isolation by default. "**Default: egress is open.**" Blocking other outbound traffic is opt-in with `NANOCLAW_EGRESS_LOCKDOWN=true`. Per-container CPU and memory caps are "opt-in and unset by default".
- You don't want Docker or about 4 GB of RAM taken up. Docker is required, and native Windows is not supported (WSL2 only).
- You want configuration files and a settings UI. The README says "core ships no monitoring dashboard or debugging UI" (an optional `/add-dashboard` skill adds one) and points you to your coding agent for debugging.
- You want no telemetry and no vendor account at all, out of the box. Without an account, setup and uninstall diagnostics go to PostHog unless you set `NANOCLAW_NO_DIAGNOSTICS=1`. Setup's default answer to opening the account portal is yes, and you have to answer no to build the image locally.
- You want new features merged upstream. The base only takes fixes and reductions; everything else ships as a skill.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Code execution / isolation | Very strong | Per-session Docker containers, non-root, mount allowlist outside the project, credentials injected by a gateway; egress lockdown is opt-in |
| Delivery surfaces | Very strong | Terminal channel in trunk, 19 chat and messaging channels via `/add-<channel>` skills, managed Slack apps with an account |
| Tool use | Strong | Claude Code's tools, MCP servers, web, `agent-browser`, agent templates; package and MCP installs need approval |
| Multi-agent | Strong | Agent-to-agent messaging, agents creating agents from templates, one Slack app per agent; held for admin approval at default scope |
| Scheduling | Strong | One-off and cron tasks, script gates that skip the model call, management from chat or `ncl tasks` |
| Memory | Medium | Plain Markdown files per agent group with an always-loaded index; maintained by the agent, with no separate consolidation job |
| Human approval | Medium | Admin approval cards for privileged actions and gateway-held requests; no per-tool approval inside the container |
| Governance | Medium | MIT and open issues, but the base takes only fixes, security fixes, simplifications and code reductions |

## Operating Cost

Moderate. Setup is three commands (`git clone`, `cd nanoclaw`, `bash nanoclaw.sh`), and the script installs or updates Node and pnpm, installs Docker if missing, installs a credential gateway, fetches or builds the agent image and pairs your first channel. If a step fails, it can hand off to Claude Code, Codex or OpenCode to diagnose and resume. After that, you maintain a fork. Channels and providers are copied into it by skills, releases come on a `stable` channel through `/update-nanoclaw`, and the 2026.11.0 notes list eight changes that "need action from some installs", among them gateway upgrades and new channel settings. The "first user to pair becomes owner", and owners and admins receive approval cards in their DMs. Unknown senders are handled per chat with a `strict`, `request_approval` or `public` policy; each channel adapter declares its own defaults. Uninstalling is `bash nanoclaw.sh --uninstall`, which "asks for confirmation per group".

## Relationship To The Rest Of This Map

NanoClaw sits in the same self-hosted lane as [OpenClaw](openclaw.md), [nanobot](nanobot.md), [Hermes Agent](hermes-agent.md) and [Mercury Agent](mercury-agent.md): one runtime you own, many chat surfaces, memory and schedules. Its own README positions it against OpenClaw, saying OpenClaw's security "is at the application level (allowlists, pairing codes) rather than true OS-level isolation"; that is NanoClaw's claim, not a finding of this map. Against [nanobot](nanobot.md), the two share the "small and readable" pitch but differ on the boundary. nanobot's default is "workspace-restricted access, not an OS sandbox", while NanoClaw puts every session in a container and keeps keys in a gateway. nanobot consolidates memory automatically with Dream; NanoClaw leaves memory upkeep to the agent. Neither puts a prompt in front of every tool call, which is the layer [Mercury Agent](mercury-agent.md) is built around.

## Bottom Line

NanoClaw fits if you want an always-on assistant in your chat apps and you care most about what the agent can reach. Each session runs in its own container, sees only mounted folders, and never holds your raw keys. The trade-offs are Docker, a gateway, and a fork you change through a coding agent. Inside the container the agent runs without per-tool prompts, and outbound traffic stays open until you turn on egress lockdown. Before you connect chats with other people, turn on lockdown and set mount allowlists and sender policies.

## Sources

- [nanocoai/nanoclaw README](https://github.com/nanocoai/nanoclaw) · [LICENSE](https://github.com/nanocoai/nanoclaw/blob/main/LICENSE) · [CONTRIBUTING](https://github.com/nanocoai/nanoclaw/blob/main/CONTRIBUTING.md) · [CLAUDE.md](https://github.com/nanocoai/nanoclaw/blob/main/CLAUDE.md) · [Releases (v2026.11.0, Nov 20 2026)](https://github.com/nanocoai/nanoclaw/releases/tag/v2026.11.0)
- Docs: [Security](https://github.com/nanocoai/nanoclaw/blob/main/docs/SECURITY.md) · [Isolation model](https://github.com/nanocoai/nanoclaw/blob/main/docs/isolation-model.md) · [Memory](https://github.com/nanocoai/nanoclaw/blob/main/docs/memory.md) · [Scheduled tasks](https://github.com/nanocoai/nanoclaw/blob/main/docs/scheduled-tasks.md) · [Architecture (draft)](https://github.com/nanocoai/nanoclaw/blob/main/docs/architecture.md) · [API details](https://github.com/nanocoai/nanoclaw/blob/main/docs/api-details.md) · [docs.nanoclaw.dev](https://docs.nanoclaw.dev)
- Source: [Claude provider policy](https://github.com/nanocoai/nanoclaw/blob/main/container/agent-runner/src/providers/claude-config.ts) · [agent-to-agent guard](https://github.com/nanocoai/nanoclaw/blob/main/src/modules/agent-to-agent/guard.ts) · [container CLI tools](https://github.com/nanocoai/nanoclaw/blob/main/container/cli-tools.json)
