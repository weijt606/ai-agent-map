# DeerFlow

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/deer-flow.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](deer-flow.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: DeerFlow is ByteDance's open-source "super agent harness": a lead agent that plans, spawns sub-agents, keeps long-term memory and runs code in a sandbox, shipped as a self-hosted stack with a web workspace, a terminal UI, IM channels and an API. Version 2 is a ground-up rewrite of what began as a Deep Research framework, and it is batteries-included rather than a kit of parts.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | ByteDance (`bytedance/deer-flow`, deerflow.tech). The LICENSE names "Bytedance Ltd. and/or its affiliates" and "DeerFlow Authors" |
| Route | General-purpose autonomous agent (it calls itself a "super agent harness") |
| Repository | [`bytedance/deer-flow`](https://github.com/bytedance/deer-flow): MIT, Python backend with a Node.js frontend, 85,475 stars as of 2026-11-18 |
| Open source | Yes (MIT). The 1.x Deep Research framework is kept on the `main-1.x` branch |
| Built on | LangGraph and LangChain |
| Models | "Model-agnostic": any LLM with an OpenAI-compatible API. No model is preset; `make setup` writes `config.yaml` and `.env` |
| Best for | A team that wants one self-hosted agent that researches, writes code and produces files, with sub-agents, memory and a sandbox already wired together |
| Main cost | A full service stack (Gateway, frontend, nginx, sandbox containers) that the project says is built for a "local trusted environment"; every release so far has had breaking changes, and the last two opened with long lists of them |
| Start command | `git clone` then `make setup`, `make docker-init`, `make docker-start`; open `http://localhost:2026` |
| Docs | https://github.com/bytedance/deer-flow/tree/main/docs/guide |

## Why This Entry Exists

DeerFlow calls itself a harness, but this map files it with general-purpose autonomous agents such as [Agent Zero](agent-zero.md) and [AutoGPT](autogpt.md). The map's [harness route](../comparisons/agent-harness-frameworks.md) holds loops you fork and own ([Pi](pi.md), [jcode](jcode.md)), harnesses you compose ([DeepSeek Harness](deepseek-harness.md)) and meta-harnesses that drive other agents ([QM](qm.md), [Omnigent](omnigent.md)). DeerFlow uses the word for something closer to a finished product, a self-hosted application aimed at end-user tasks. Its README describes the change from v1: *"DeerFlow 2.0 is no longer a framework you wire together. It's a super agent harness — batteries included, fully extensible."* Out of the box it ships "a filesystem, memory, skills, sandbox-aware execution, and the ability to plan and spawn sub-agents for complex, multi-step tasks."

The project's own history explains the shape. It started as a Deep Research framework; users then built "data pipelines, generating slide decks, spinning up dashboards, automating content workflows" on it, and the team "rebuilt it from scratch." Version 2 "shares no code with v1."

## When To Pick It

- You want delegation as the default way of working. The lead agent "can spawn sub-agents on the fly — each with its own scoped context, tools, and termination conditions", then verifies and synthesizes what they report back.
- You want code to run somewhere other than your host. Sandbox modes are Local, Docker, and Docker with Kubernetes; optional providers include E2B, Tenki, OpenSandbox and BoxLite.
- You want the agent to reach people where they already are. IM channels cover Feishu/Lark, Slack, Telegram, Discord, DingTalk, WeChat, WeCom, QQ and Buzz, and the docs say "no public IP required for any of them." A separate GitHub channel works through webhooks.
- You want recurring work. A scheduled-task workspace supports `once`, `cron` and `interval` schedules, and 2.2 adds goal-driven tasks with per-owner limits. The scheduler is off until you set `scheduler.enabled: true`.
- You want long-term memory that is on unless you turn it off: `memory.enabled` defaults to `true` in both the code and the example config, with facts injected into the system prompt.

## When Not To Pick It

- **You plan to put it on a network without hardening it.** The security notice says DeerFlow "is designed by default to be deployed in a local trusted environment (accessible only via the 127.0.0.1 loopback interface)", and the README adds that a Gateway admin account "is equivalent to code execution on the host."
- You want approvals on by default. Per-tool human approval (`hitl_approval`) exists, but "the default is disabled for existing installations", and both the code default and the example config ship it as `enabled: false`.
- You need stable contracts between upgrades. v2.2.0 closed "1068 merged PRs" and opens with a breaking-changes list that touches binding, credential storage, the scheduler API and tool authorization.
- You want a single-file loop to read and fork. This is a multi-service application; see [Pi](pi.md) or [mini-swe-agent](mini-swe-agent.md).
- You want to avoid a vendor-run stack. The README promotes ByteDance Volcengine's Coding Plan and BytePlus InfoQuest, though neither is required.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Multi-agent | Very strong | The headline: a lead agent spawns scoped sub-agents; durable `batch_task` for large independent item sets |
| Code execution | Very strong | Local, Docker and Kubernetes sandbox modes plus optional cloud providers; host bash off by default |
| Delivery surfaces | Very strong | Web workspace, `deerflow` TUI, nine chat-app channels plus a GitHub webhook channel, personal access tokens and an embedded Python client |
| Memory | Strong | DeerMem long-term memory on by default; Mem0 is an opt-in alternative backend |
| Scheduling | Medium | `once` / `cron` / `interval` tasks, off by default; the docs still call it a "scheduled-task MVP" |
| Human approval | Medium | `ask` / `auto` / `full` modes with approval cards, but off unless the operator enables it, and `full` must be added to `allowed_modes` explicitly |
| Stability | Weak | Three releases since June 2026, each with breaking changes |

## How The Sandbox Defaults Work

The defaults are worth reading before anything else, because they decide what "runs code" means on your machine:

- The **default provider is `LocalSandboxProvider`**, and the configuration reference says it "is a host-side convenience mode, not a secure shell isolation boundary." For that reason `allow_host_bash` is `false` by default, and the docs recommend `AioSandboxProvider` (a Docker sandbox) when you need `bash`.
- **Docker sandbox containers** drop all Linux capabilities except a five-item allowlist and run with `no-new-privileges`, but the shipped image runs with `seccomp=unconfined` because its Chromium browser does not start under Docker's default profile.
- **Network exposure** is opt-in. The Docker stack publishes its entry port on `127.0.0.1` only. Since 2.2, `make dev` and `make start` also bind to loopback, and `BIND_HOST=0.0.0.0` in `.env` is required to expose the stack.

## Operating Cost

Medium to high. Setup is a wizard (about two minutes by the README's estimate) plus Docker, or Node.js 22+, pnpm, uv and nginx for local development. You bring the model credentials; `make doctor` flags placeholder keys. Going past localhost means following the security notice: IP allowlists, an authenticating reverse proxy, and network isolation. Multi-worker or multi-instance deployments need Postgres and the Redis stream bridge, and since 2.2 the ones that store credentials (IM channel connections or refresh-token OAuth) refuse to start without a shared `DEER_FLOW_CREDENTIALS_KEY`.

## Relationship To The Rest Of This Map

Against [DeepSeek Harness](deepseek-harness.md), the difference is how much is decided for you: `dsh` makes every part a replaceable plugin, while DeerFlow ships one opinionated lead-agent design and lets you "tear it apart" if you want. Against [OpenHands](openhands.md), both run sandboxed agents behind a web UI, but DeerFlow's centre is general research and content work rather than software tasks. Against [Hermes Agent](hermes-agent.md) and [OpenClaw](openclaw.md), DeerFlow overlaps on channels, memory and schedules, but it describes itself as a harness for long-horizon tasks, not a personal assistant.

## Bottom Line

DeerFlow is for teams that want sub-agents, memory, a sandbox and chat-app delivery already assembled, on hardware they run. MIT licensing and the LangGraph base keep it open to change. Two things count against it: the stack is designed for a trusted local network, and each release so far has come with breaking changes. Read the security notice before you expose it, and expect upgrades to need real work.

## Sources

- [bytedance/deer-flow README](https://github.com/bytedance/deer-flow) · [LICENSE](https://github.com/bytedance/deer-flow/blob/main/LICENSE) · [Releases (v2.2.0, Nov 4 2026)](https://github.com/bytedance/deer-flow/releases) · [Install.md](https://github.com/bytedance/deer-flow/blob/main/Install.md)
- Guides: [Security Notice](https://github.com/bytedance/deer-flow/blob/main/docs/guide/security.md) · [Sandbox](https://github.com/bytedance/deer-flow/blob/main/docs/guide/sandbox.md) · [Sub-Agents](https://github.com/bytedance/deer-flow/blob/main/docs/guide/subagents.md) · [Long-Term Memory](https://github.com/bytedance/deer-flow/blob/main/docs/guide/memory.md) · [Scheduled Tasks](https://github.com/bytedance/deer-flow/blob/main/docs/guide/scheduled-tasks.md) · [IM Channels](https://github.com/bytedance/deer-flow/blob/main/docs/guide/im-channels.md) · [Configuration](https://github.com/bytedance/deer-flow/blob/main/docs/guide/configuration.md) · [TUI](https://github.com/bytedance/deer-flow/blob/main/docs/guide/tui.md) · [Configuration Reference](https://github.com/bytedance/deer-flow/blob/main/backend/docs/CONFIGURATION.md) · [`config.example.yaml`](https://github.com/bytedance/deer-flow/blob/main/config.example.yaml)
