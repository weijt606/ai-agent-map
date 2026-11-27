# QwenPaw

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/qwenpaw.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](qwenpaw.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: QwenPaw is the AgentScope team's self-hosted personal assistant: one Python app that serves a web Console, a TUI and a desktop app, and answers in chat apps from DingTalk and Feishu to Telegram and Slack. Its headline features are a three-layer memory built on ReMe, several agents per instance, and a five-layer security stack. Its kernel sandbox, though, is off until you switch it on.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | The AgentScope team (`agentscope-ai`, makers of AgentScope, AgentScope Runtime and ReMe). SECURITY.md sends vulnerability reports to the Alibaba Security Response Center |
| Route | Self-hosted / local runtime |
| Repository | [`agentscope-ai/QwenPaw`](https://github.com/agentscope-ai/QwenPaw): Apache-2.0, Python, 38,256 stars as of 2026-11-27 (repo created 2026-02-24) |
| Open source | Yes (Apache License 2.0). CONTRIBUTING invites new channels, model providers, skills and MCPs through pull requests |
| Form factor | A Python package (`pip install qwenpaw`) that runs a local web Console on `127.0.0.1:8088`, plus a full-screen TUI, a desktop app (Beta, Windows and macOS), a REST API, a Docker image and a self-hosted multi-user Hub |
| Models and billing | Bring your own provider key, or run a model locally. The README lists DashScope / Qwen, OpenAI, Anthropic, Google Gemini, DeepSeek, Kimi and OpenRouter among "14+ cloud providers", plus a built-in QwenPaw Local runtime (llama.cpp), Ollama and LM Studio |
| Default model | None. `qwenpaw init --defaults` with no provider prints "No LLM provider configured", and for cloud models "QwenPaw will not work until a valid key is set." You pick a chat model in **Settings → Models**. The project also trains its own QwenPaw-Flash models (2B / 4B / 9B / 35B-A3B / 27B) for agent tasks |
| Best for | One person, or a small trusted team on Hub, who wants a personal assistant on their own machine, reachable from Chinese and international chat apps, with memory that builds up over time |
| Main cost | Approval prompts appear only for calls the guard rules flag (default `AUTO`), the kernel sandbox is off by default (`sandbox_enabled: false`), and Console login is off by default. A large, fast-moving surface: v2.3.0 shipped on 2026-11-11 and a v2.3.1 beta followed on 2026-11-23 |
| Docs | [qwenpaw.agentscope.io/docs](https://qwenpaw.agentscope.io/docs) · [repo docs source](https://github.com/agentscope-ai/QwenPaw/tree/main/website/public/docs) |

## What It Is

The README sums it up as *"Your personal AI assistant — deploy locally or in the cloud, extend with Skills & Plugins, connect across every channel."* The name "stands for Qwen Personal Agent Workstation". One process serves every client: the TUI "drives the _same_ agent as the Console and the IM Channels — same memory, skills, MCP tools, and sessions".

Around that agent it puts:

- **Tools**: shell, a unified file workspace with previews and diffs, document skills for PDF, Word, Excel and PowerPoint, Browser-use and Computer-use (added in v2.1.0), MCP clients, and a plugin system with a marketplace. Codex and Qoder backends are optional plugins.
- **Memory** in three layers: "live working context, full verbatim history, and a self-evolving personal knowledge base powered by ReMe". **Auto-Memory** runs "after every five user turns" by default and writes Markdown notes; **Auto-Dream** consolidates them into a `digest/` knowledge base. Its cron job is enabled by default and runs daily at 23:00 (`dream_cron: "0 23 * * *"`). The docs say "Markdown files are the source of truth".
- **Scheduling**: cron jobs that "support **multiple jobs in parallel**", each with its own timing, content and delivery target, and a **heartbeat** check-in whose `enabled` field is "**Default false**".
- **Multiple agents**: several independent agents in one instance, each with its own persona, memory, skills and channels; an opt-in **Multi-Agent Collaboration** skill so they can call each other; ephemeral in-project subagents (`spawn_subagent`); and a Mission Mode that runs a "**master → worker → verifier** pipeline".
- **ACP** both ways: QwenPaw can delegate to external runners through `delegate_external_agent` (built-in examples are `opencode`, `qwen_code`, `claude_code` and `codex`), or act as an ACP server for other clients. The docs expand ACP as Agent Client Protocol; the README's feature table calls it Agent Communication Protocol.

## When To Pick It

- You want an assistant in Chinese work chat as well as international apps. The channel guide has 18 sections, including DingTalk ("recommended"), Feishu (Lark), WeCom, personal WeChat, QQ, Yuanbao, iMessage (macOS only), Discord, Telegram, Slack, Matrix, Mattermost, Azure Bot, MQTT, Voice and SIP.
- You want long-term memory that accumulates and that you can read and edit as Markdown files.
- You want to run fully local. The README says local backends need no API key, and QwenPaw Local downloads QwenPaw-Flash models "with hardware-aware recommendations".
- You want several specialised agents in one install (the docs give work/life separation and per-platform agents as examples), or want QwenPaw to hand work to Codex, Claude Code, OpenCode or Qwen Code over ACP.
- You need a small trusted team on one server: Hub gives each member "their own QwenPaw with separate workspaces, settings, credentials, and conversations."

## When Not To Pick It

- **You expect every action to be approved by default.** The default `approval_level` is `AUTO`: "Only tool calls flagged by guard rules require approval". The shell-evasion checks are all off by default ("**All checks default to `false` (disabled).**"), and "In non-interactive contexts without a session, findings are logged and execution may still proceed". `STRICT` exists if you want every call approved.
- **You expect the kernel sandbox to be on.** The README presents Seatbelt, Bubblewrap / Landlock and AppContainer isolation as a core layer, but the config field `security.sandbox_enabled` defaults to `False`: shell calls with no matching rule "run directly without the sandbox". Even when on, the docs list limits: `network_allow` defaults to `["*"]`, "Bubblewrap does not isolate the network at all", and the default `allow_read_all: true` leaves the whole filesystem readable.
- You plan to expose the Console beyond localhost without setting up login. Web authentication is "**disabled by default**" and is turned on with `QWENPAW_AUTH_ENABLED`; requests from localhost always skip it.
- You need a public multi-tenant service. The Hub docs say the current release is "intended only for internal teams whose members trust one another" and warn not to run it "as a public multi-tenant service for unknown users."
- You want no telemetry by default. `qwenpaw init --defaults` accepts anonymous usage collection automatically (version, install method, OS, Python version, CPU architecture, GPU availability), and while agents run, including scheduled tasks, a daily ping sends those fields with a persistent random runtime UUID and the UTC date; the interactive `init` asks, and `QWENPAW_TELEMETRY_DISABLED` turns both off.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Delivery surfaces | Very strong | Web Console, TUI, desktop app (Beta), 18 channel sections, REST API, ACP server |
| Memory | Very strong | Three layers on ReMe; Auto-Memory and a daily Auto-Dream job on by default; Markdown is the source of truth |
| Tool use | Very strong | Shell, files, documents, Browser-use, Computer-use, MCP, skills and a plugin marketplace |
| Multi-agent | Strong | Independent agents per instance, opt-in collaboration skill, ephemeral subagents, Mission Mode, ACP delegation |
| Scheduling | Strong | Parallel cron jobs with delivery targets; heartbeat off by default |
| Human approval | Medium | Approval for guard-flagged calls by default, `STRICT` for every call, ask rules for MCP tools; non-interactive runs may proceed |
| Execution isolation | Medium | Kernel sandbox backends for macOS, Linux and Windows, but off by default and with open network by default |
| Governance | Strong | Apache-2.0, open pull requests, a documented private security-report process |

## Operating Cost

Low to start: `pip install qwenpaw` (Python 3.11 to below 3.14) or a one-line install script, then `qwenpaw init --defaults` and `qwenpaw app`, and choose a model in the Console. The init command shows a security notice that calls the default setup "a single-operator boundary: one trusted user." The Console binds to `127.0.0.1` by default, and the README's Docker command maps the port to `127.0.0.1:8088`, keeping secrets in a separate `qwenpaw-secrets` volume. Before you widen access, the work is yours: set `QWENPAW_AUTH_ENABLED`, turn on `sandbox_enabled`, consider `SMART` or `STRICT` approval, and allowlist channel users. The project also moves fast. Its roadmap is splitting non-core components into plugins, and v2.3.0 moved channels to plugins, so a channel card can show "**Plugin not installed**" until you install it. Hosted options include an Alibaba Cloud ECS one-click deploy, the AgentScope Platform and ModelScope Studio; the README tells Studio users to set it "**non-public** so others cannot control your QwenPaw".

## Relationship To The Rest Of This Map

QwenPaw sits in the same self-hosted lane as [nanobot](nanobot.md), [OpenClaw](openclaw.md) and [Hermes Agent](hermes-agent.md): one runtime you own, many chat surfaces, memory and schedules. Against nanobot, which this map scores with no per-action approval and an application-level workspace boundary, QwenPaw ships rule-based approval prompts on by default and an OS-level sandbox you can turn on. Its channel guide puts Chinese platforms first (DingTalk is the "recommended" channel, followed by Feishu, with WeCom, WeChat, QQ and Yuanbao further down), and its Hub adds a trusted-team mode. It also reaches into the coding lane: ACP delegation lets it drive [Codex](codex.md) or [Claude Code](claude-code.md) as collaborators.

## Bottom Line

QwenPaw is a good fit if you want a personal assistant on your own machine that you can reach from DingTalk or Feishu as easily as from Telegram, with memory that grows into a readable knowledge base, and a choice of local or cloud models. Treat its security list as a set of switches. By default you get guard-flagged approvals, File Guard and a warn-mode skill scanner, but no kernel sandbox and no Console login. Turn those on before anyone else can reach it.

## Sources

- [agentscope-ai/QwenPaw README](https://github.com/agentscope-ai/QwenPaw) · [LICENSE](https://github.com/agentscope-ai/QwenPaw/blob/main/LICENSE) · [SECURITY.md](https://github.com/agentscope-ai/QwenPaw/blob/main/SECURITY.md) · [CONTRIBUTING](https://github.com/agentscope-ai/QwenPaw/blob/main/CONTRIBUTING.md) · [Releases (v2.3.0.post1, Nov 18 2026; v2.3.1-beta.1, Nov 23 2026)](https://github.com/agentscope-ai/QwenPaw/releases) · [config schema](https://github.com/agentscope-ai/QwenPaw/blob/main/src/qwenpaw/config/config.py) · [init command](https://github.com/agentscope-ai/QwenPaw/blob/main/src/qwenpaw/cli/init_cmd.py)
- Docs: [Security](https://github.com/agentscope-ai/QwenPaw/blob/main/website/public/docs/security.en.md) · [Models](https://github.com/agentscope-ai/QwenPaw/blob/main/website/public/docs/models.en.md) · [Channels](https://qwenpaw.agentscope.io/docs/channels) · [Memory](https://qwenpaw.agentscope.io/docs/memory) · [Cron](https://github.com/agentscope-ai/QwenPaw/blob/main/website/public/docs/cron.en.md) · [Heartbeat](https://qwenpaw.agentscope.io/docs/heartbeat) · [Multi-Agent](https://github.com/agentscope-ai/QwenPaw/blob/main/website/public/docs/multi-agent.en.md) · [ACP Integration](https://github.com/agentscope-ai/QwenPaw/blob/main/website/public/docs/acp-integration.en.md) · [Hub](https://github.com/agentscope-ai/QwenPaw/blob/main/website/public/docs/hub.en.md) · [TUI](https://github.com/agentscope-ai/QwenPaw/blob/main/website/public/docs/tui.en.md) · [Release notes](https://github.com/agentscope-ai/QwenPaw/releases)
