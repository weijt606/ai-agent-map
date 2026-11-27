# ZeroClaw

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/zeroclaw.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](zeroclaw.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: ZeroClaw is a self-hosted agent runtime shipped as a single Rust binary that you configure with one TOML file. One agent answers across chat apps, email, voice, webhooks, a web dashboard and a terminal client, and acts through shell, browser, HTTP, MCP and hardware tools. Its defining choice is the default safety posture: `supervised` autonomy, where medium-risk actions wait for your approval in the channel that asked.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | ZeroClaw Labs. The README credits original creator @theonlyhennygod and project lead @JordanTheJet, and calls it "Built and maintained by the community" |
| Route | Self-hosted / local runtime |
| Repository | [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw): Rust, 33,639 stars as of 2026-11-27 (repo created 2026-02-13). GitHub reports the license as Apache-2.0; the repo ships both `LICENSE-MIT` and `LICENSE-APACHE` and the README says "Dual-licensed: MIT OR Apache 2.0. You may choose either." |
| Open source | Yes. Larger changes go through an RFC process, contributors sign a CLA, and "AI-assisted PRs are welcome". The ZeroClaw name and logo are trademarks of ZeroClaw Labs |
| Form factor | One binary (`zeroclaw`) with a daemon, an HTTP/WebSocket gateway and web dashboard (`http://127.0.0.1:42617`), the `zerocode` terminal interface, chat channels and ACP for editors; `zeroclaw service install` registers it with systemd, launchctl or Windows Service |
| Models and billing | Bring your own provider: Anthropic, OpenAI, Ollama, "or any OpenAI-compatible endpoint", with fallback chains and routing. Subscription sign-in is documented for OpenAI Codex (the Codex CLI's `auth.json`) and Claude Max (`claude setup-token`). The docs say it is "Not a SaaS. There's no hosted version, no account system, no billing." |
| Default model | None until you choose one: the **Model provider** step in `zeroclaw quickstart` is required and sets the provider, its key or endpoint, and the model. The docs' own examples use `gpt-5.4` and `claude-sonnet-4-5` |
| Default safety | Autonomy `Supervised`, workspace-only `true`, OS sandbox auto-detected, OTP off; the gateway binds to `127.0.0.1` and clients must pair first (`require_pairing = true` is the default) |
| Best for | Someone who wants an always-on personal agent on their own laptop, server or single-board computer, reachable from many channels, with approval gates on by default |
| Main cost | A large config surface (providers, agents, risk profiles, runtime profiles, channels as `<type>.<alias>` tables). `zeroclaw estop` is "not a safety control today", command execution is not audited, and Windows has no OS-level sandbox backend |
| Docs | [docs.zeroclaw.com](https://docs.zeroclaw.com/master/en/introduction.html) · [repo docs](https://github.com/zeroclaw-labs/zeroclaw/tree/master/docs/book/src) · [zeroclaw.com](https://www.zeroclaw.com/) |

## What It Is

The README describes it as "an agent runtime — a single Rust binary you configure and run. It talks to LLM providers (Anthropic, OpenAI, Ollama, and ~20 others), reaches the world through 30+ channels (Discord, Telegram, Matrix, email, voice, webhooks, your own CLI), and acts through tools (shell, browser, HTTP, hardware, custom MCP servers). Everything runs on your machine, with your keys, in your workspace." The docs add what it is not: "Not a framework. You don't build apps on top of ZeroClaw. You configure it and connect channels."

Around that runtime it puts:

- **Channels**: every configured channel delivers to the same agent loop. The docs list chat platforms (Matrix, Telegram, Discord, Slack, Mattermost, LINE, Signal, WhatsApp, WeCom, WeChat, DingTalk, Lark, QQ and more), social feeds, Git forges, email and voice. Channels are compile-time features; the default build carries ACP, webhook, email, Telegram, Discord and filesystem, and standard release artifacts add Git, Matrix, Lark and WhatsApp Web.
- **Tools**: shell, files, web fetch and search, browser, HTTP, MCP servers, cron management (`cron_add`, `cron_list`, `cron_run` and others), skills, WASM plugins in builds that include them, and hardware access (GPIO / I2C / SPI / USB on Raspberry Pi, STM32, Arduino and ESP32).
- **Memory**: a pluggable backend chosen per agent (`sqlite`, `markdown`, `postgres`, `qdrant`, `lucid` or `none`). SQLite is the default for a new agent, and the backend is locked once the agent has written data. Sharing memory between agents is opt-in.
- **SOP engine**: "deterministic procedures" with "explicit trigger matching, approval gates, and auditable run state." Webhooks, MQTT, filesystem and AMQP are wired event sources and cron triggers are dispatched by the daemon; the docs say peripheral and calendar triggers "are defined and matched but not yet routed to a live event source."
- **Multiple agents**: `spawn_subagent` runs the same agent on a subtask (subagents cannot spawn their own), `delegate` hands work to a different configured agent, and peer groups let agents on a shared channel address each other.

## When To Pick It

- You want approvals before risky actions without building them yourself. Under the default `supervised` level, low-risk tools run, medium-risk tools ask, high-risk tools are blocked. The prompt arrives in the channel that started the conversation: Telegram inline buttons, Slack Block Kit buttons, a `<token> approve|deny|always` reply on Discord, Signal, Matrix and WhatsApp, or an inline CLI prompt. Unanswered requests time out after 120 seconds by default and "Timeouts are treated as denials."
- You want approvals routed somewhere else. `approval_route` sends a risk profile's approvals to a separate approver channel, and it fails closed by default (`on_no_approver = "deny"`).
- You want one agent on many surfaces, including email, voice, Git forges and an editor over ACP.
- You want to run it on small or unusual hardware, or drive sensors and pins from the agent.
- You want to pick or mix providers, including local Ollama, with fallback when one fails.
- You want more than one person on the dashboard. v0.9.0 (Nov 12 2026) added opt-in sign-in through your own OpenID Connect provider, with accounts kept "inside what their permission profile allows".

## When Not To Pick It

- **You need a working kill switch inside the product.** The security docs say `zeroclaw estop` "is not a safety control today"; "To halt the agent now, stop the ZeroClaw process itself."
- **You need an audit trail of what the agent ran.** The default audit log covers "certificate issuance and renewal only (command execution is not audited)". Tool receipts are HMAC evidence fed back into the conversation, "not a chained or durable audit log today."
- You run on Windows and want OS isolation: the sandbox table lists "No OS-level backend" for Windows. On Linux, Landlock and Firejail leave network egress unchanged.
- You want a small config to read and edit by hand. A working config needs at least a provider, an agent and a risk profile, each as a `<type>.<alias>` table, and v0.9.0 moved the config to schema version 4 with breaking changes.
- You want a library to build your own app on; the project says it is not a framework.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Delivery surfaces | Very strong | 30+ channels, web dashboard, `zerocode` terminal interface, REST/WebSocket gateway, ACP for editors; channel set depends on the build |
| Human approval | Very strong | `supervised` by default, per-channel approval buttons or tokens, `always_ask`, cross-channel approval routing that fails closed, optional OTP per action |
| Tool use | Strong | Shell, files, web, browser, HTTP, MCP, cron tools, skills, WASM plugins, hardware peripherals |
| Code execution | Strong | Shell under command allowlist and validator, workspace boundary, OS sandbox backends (Landlock, Firejail, Bubblewrap, Seatbelt, Docker); none on Windows |
| Memory | Medium | Six pluggable backends, SQLite by default, opt-in cross-agent sharing; no automatic consolidation is documented |
| Scheduling | Medium | Cron jobs the agent can manage, SOP cron triggers, a heartbeat monitor in the daemon; cron runs "are never pre-approved" |
| Multi-agent | Medium | Depth-1 subagents, delegation to other agents (forbidden by default per risk profile), peer groups on shared channels |
| Governance | Strong | MIT or Apache-2.0, open PRs with an RFC process and a CLA |

## Operating Cost

Low to start: one installer command (`curl -fsSL … install.sh | sh`, or a prebuilt PowerShell path on Windows), then `zeroclaw quickstart` walks through provider, risk profile, memory, optional channels and the agent; the CLI channel works immediately. `zeroclaw service install` and `zeroclaw service start` keep it running. The cost grows with exposure. Opening the gateway to the LAN needs `host = "0.0.0.0"` plus `allow_public_bind = true` ("Without it, the daemon refuses"), or a tunnel such as Tailscale. Each channel has its own allowlist (`allowed_users`, `allowed_chats`, webhook IP allowlists). For production the docs say to "enable OTP and restricted tools" and to use "an external supervisor or logging wrapper" for a record of commands. YOLO mode removes every gate and is meant for "dev boxes, home labs, and throwaway VMs"; the docs warn that a YOLO agent behind a public Telegram bot "is a Telegram-accessible root shell".

## Relationship To The Rest Of This Map

ZeroClaw sits in the same self-hosted lane as [OpenClaw](openclaw.md), [nanobot](nanobot.md), [Hermes Agent](hermes-agent.md) and [Mercury Agent](mercury-agent.md): one runtime you own, many chat surfaces, tools and schedules. Against [nanobot](nanobot.md), the clearest difference is approval: nanobot has access pairing but no per-action approval, while ZeroClaw ships with `supervised` approval on and the workspace boundary set to `true`. That puts it closer to [Mercury Agent](mercury-agent.md), which also centres on approval. Against [OpenClaw](openclaw.md), both are broad control planes that carry many routing, permission and ops decisions; ZeroClaw's own angles are the single Rust binary, hardware peripherals and the SOP engine.

## Bottom Line

ZeroClaw fits if you want an always-on personal agent on hardware you own, reachable from many channels, and you want approval prompts on by default rather than as an add-on. Budget time for the config model and read the security docs closely: the emergency stop is not enforced, commands are not audited, and isolation depends on your OS. Keep the gateway on localhost with pairing, set channel allowlists, and turn on OTP before anyone else can reach it.

## Sources

- [zeroclaw-labs/zeroclaw README](https://github.com/zeroclaw-labs/zeroclaw) · [LICENSE-MIT](https://github.com/zeroclaw-labs/zeroclaw/blob/master/LICENSE-MIT) · [LICENSE-APACHE](https://github.com/zeroclaw-labs/zeroclaw/blob/master/LICENSE-APACHE) · [Releases (v0.9.0, Nov 12 2026)](https://github.com/zeroclaw-labs/zeroclaw/releases)
- Docs: [Quickstart](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/getting-started/quickstart.md) · [Security model](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/security/model.md) · [Autonomy levels](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/security/autonomy.md) · [Sandboxing](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/security/sandboxing.md) · [YOLO mode](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/getting-started/yolo.md) · [Channels](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/channels/overview.md) · [Provider catalog](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/providers/catalog.md) · [Tools](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/tools/overview.md) · [Delegation](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/agents/delegation.md) · [Agent filesystem and memory](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/agents/filesystem.md) · [SOP](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/sop/index.md) · [Network deployment](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/ops/network-deployment.md) · [What this isn't](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/philosophy/what-this-isnt.md) · [docs.zeroclaw.com](https://docs.zeroclaw.com/master/en/introduction.html)
