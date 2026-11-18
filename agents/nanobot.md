# nanobot

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/nanobot.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](nanobot.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: nanobot is a self-hosted personal agent from HKU's Data Intelligence Lab that runs as one local gateway and meets you in a browser, a terminal or a chat app. It remembers preferences, runs scheduled automations and delegates to subagents. Its pitch is a "small core" you can read and own, not a platform.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | HKUDS (Data Intelligence Lab@HKU). The LICENSE names "Xubin Ren and the nanobot contributors" |
| Route | Self-hosted / local runtime |
| Repository | [`HKUDS/nanobot`](https://github.com/HKUDS/nanobot): MIT, Python, 50,167 stars as of 2026-11-18 (repo created 2026-02-01) |
| Open source | Yes (MIT). Issues are open to everyone; "pull requests are currently limited to repository collaborators" |
| Form factor | A Python gateway with a bundled WebUI, a native TUI, chat-app channels and a Python SDK; PyPI package `nanobot-ai` |
| Models and billing | Bring your own provider or local server: "nanobot does not supply a model account." OpenAI-compatible APIs, Ollama, vLLM, and OAuth sign-in for some providers |
| Default model | Nothing usable until you add a provider credential; the docs say to save a preset in **Settings → Models**. The config schema's built-in default is `anthropic/claude-opus-4-5` with provider `auto` |
| Best for | One person, or a small trusted group, who wants a personal agent on their own machine or server, reachable from chat apps, with memory and schedules |
| Main cost | The default file boundary is application-level, not an OS sandbox, and there is no per-action approval step; you set up the shell sandbox and channel allowlists yourself |
| Docs | [nanobot.wiki](https://nanobot.wiki) (released version) · [repo docs](https://github.com/HKUDS/nanobot/tree/main/docs) (current source; the README says it "describes current source", so some features below may be newer than v0.4.1) |

## What It Is

The README opens with: *"nanobot is an ultra-lightweight, open-source, self-hosted personal AI agent framework written in Python. Use it in a browser, terminal, or chat app to work with files, remember preferences, and schedule tasks."* Architecturally it is one gateway. "The Python gateway owns agent execution, sessions, tools, memory, and security policy for the WebUI, TUI, and chat apps", and every client shares that runtime.

Around that loop it puts:

- **Tools**: file read/write/edit, shell, web search and fetch with SSRF checks, MCP servers, cron, image generation, and subagents. Apps, Skills and Agent Plugins add more.
- **Memory** in two layers. Conversations are summarized as they grow; **Dream** then consolidates long-term memory into files such as `USER.md` and `memory/MEMORY.md`. Dream is enabled by default and runs every 2 hours (`intervalH: 2`) while the gateway runs.
- **Automations**: reminders and scheduled tasks on a cron service, local triggers that let a script start a saved task, and a built-in `heartbeat` job (on by default) that works through `HEARTBEAT.md`.
- **Subagents**: delegated tasks that stay attached to the conversation that started them, four at a time by default (`maxConcurrentSubagents: 4`).
- **Long-horizon goals**: `/goal` keeps the agent working "beyond the ordinary iteration limit until it records completion, cancellation, or a blocked state."

## When To Pick It

- You want one agent you can message from many places. The channel docs cover 18 platforms (the source tree has 18 channel packages besides the WebUI's WebSocket), including Telegram, Discord, Slack, WhatsApp, WeChat, Feishu, DingTalk, QQ, Matrix, Mattermost, Signal, Email, Microsoft Teams and Linear.
- You want memory that consolidates on its own and that you can inspect. Dream writes to files in the workspace, and `/dream-log` shows what changed.
- You want background work: the README lists "long-horizon goals" and "scheduled automations", and `nanobot gateway --background` keeps channels and automations running after clients close.
- You want to embed the same agent in your own code through the Python SDK.
- You want to choose the model freely, including a local one.

## When Not To Pick It

- **You need an approval step before risky actions.** Access is set per topic (Restricted or Full Access) and per channel sender (pairing and `allowFrom`), but the docs describe no per-action approval card. `/stop` interrupts work, and "cancellation does not undo file changes or other actions already taken."
- You expect isolation by default. The WebUI's **Default Permission** is "workspace-restricted access, not an OS sandbox"; in the config, `tools.restrictToWorkspace` defaults to `false` and `tools.exec.sandbox` to `""`. The docs tell production deployments to set both, and note that Windows "runs commands without OS sandboxing" and "Neither backend restricts network access."
- You need separate memory per client or user inside one instance. Topics and projects do not create separate long-term memory; the docs say to run separate instances.
- You want to contribute code without being a collaborator.
- You want a team platform with roles and audit. WebUI access "grants administration of the same agent instance".

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Delivery surfaces | Very strong | WebUI (desktop and mobile), native TUI, 18 chat channels, Python SDK |
| Scheduling | Strong | Cron reminders, scheduled automations, local triggers, heartbeat on by default; missed times are not replayed after a restart |
| Memory | Strong | Session summaries plus Dream consolidation, on by default and editable as files |
| Tool use | Strong | Files, shell, web, MCP, image generation, Apps, Skills and Agent Plugins |
| Multi-agent | Medium | Subagents per conversation, four concurrent by default; interrupted tasks are not resumed automatically |
| Human approval | Weak | Channel pairing and access modes, no per-action approval |
| Governance | Medium | MIT and open issues, but PRs limited to collaborators |

## Operating Cost

Low to start: one installer command (`curl … install.sh | sh`) or `uv tool install nanobot-ai`, then `nanobot webui` and a model preset. The first-run WebUI binds to localhost and uses a login link the README says to "keep this credential private". The cost grows when you keep it online. Background mode does not restart after a reboot or crash, so the docs point to an OS-managed service (Docker Compose, Linux services, macOS LaunchAgent). Exposing it to chat apps means setting allowlists per platform. Slack and Mattermost DMs "are open by default", and `allowFrom: ["*"]` "allows anyone who can reach that channel to talk to the bot." A one-click Render Blueprint exists; it asks for `ANTHROPIC_API_KEY` and a `NANOBOT_WEB_TOKEN`.

## Relationship To The Rest Of This Map

nanobot sits in the same self-hosted lane as [Hermes Agent](hermes-agent.md), [OpenClaw](openclaw.md) and [Mercury Agent](mercury-agent.md): one runtime you own, many chat surfaces, memory and schedules. Within that lane its distinguishing claim is size and readability ("Small core"), and its weak spot is the approval layer, which [Mercury Agent](mercury-agent.md) puts at the centre. Against [DeerFlow](deer-flow.md), nanobot is a personal agent for one owner; DeerFlow is a multi-user harness with sub-agent batches, sandbox containers and an optional approval policy.

## Bottom Line

nanobot is a good fit if you want a personal agent that lives on your machine or server, answers in the chat apps you already use, and keeps its memory in files you can read. The defaults are built for a single trusted owner: an application-level workspace boundary, no per-action approvals, and a WebUI that is an admin console. Turn on the shell sandbox and channel allowlists before you let anyone else talk to it.

## Sources

- [HKUDS/nanobot README](https://github.com/HKUDS/nanobot) · [LICENSE](https://github.com/HKUDS/nanobot/blob/main/LICENSE) · [Releases (v0.4.1, Nov 6 2026)](https://github.com/HKUDS/nanobot/releases) · [config schema](https://github.com/HKUDS/nanobot/blob/main/nanobot/config/schema.py)
- Docs: [Concepts](https://github.com/HKUDS/nanobot/blob/main/docs/concepts.md) · [Architecture](https://github.com/HKUDS/nanobot/blob/main/docs/architecture.md) · [Configuration](https://github.com/HKUDS/nanobot/blob/main/docs/configuration.md) · [Memory](https://github.com/HKUDS/nanobot/blob/main/docs/memory.md) · [Automations](https://github.com/HKUDS/nanobot/blob/main/docs/automations.md) · [Chat Apps](https://github.com/HKUDS/nanobot/blob/main/docs/chat-apps.md) · [WebUI](https://github.com/HKUDS/nanobot/blob/main/docs/webui.md) · [Providers](https://github.com/HKUDS/nanobot/blob/main/docs/providers.md) · [Deployment](https://github.com/HKUDS/nanobot/blob/main/docs/deployment.md) · [nanobot.wiki](https://nanobot.wiki)
