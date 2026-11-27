# CowAgent

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/cowagent.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](cowagent.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: CowAgent is a self-hosted personal agent, formerly `chatgpt-on-wechat`, that runs on your computer or server and answers in a web console, a desktop client, a phone app and eleven IM channels, with WeChat, Feishu, DingTalk, WeCom and QQ among them. It layers file-based memory, a knowledge base, a nightly "Deep Dream" and background "Self-Evolution" over a tool loop, and it lets you build a team of agents. The default permission mode on a source or Docker install is `full-access`.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | zhayujie (the LICENSE reads "Copyright (c) 2022 zhayujie"). The README offers enterprise hosting through LinkAI |
| Route | Self-hosted / local runtime |
| Repository | [`zhayujie/CowAgent`](https://github.com/zhayujie/CowAgent): MIT, Python, 48,111 stars as of 2026-11-27 (repo created 2022-08-07; the project "was previously named `chatgpt-on-wechat`") |
| Open source | Yes (MIT). CONTRIBUTING asks you to fork, branch from `master` and open a PR; issues and PRs should be in English |
| Form factor | A Python service with a Web console on port 9899 and a `cow` CLI; a macOS / Windows desktop client with the backend bundled; an iOS / Android / HarmonyOS app (public beta); CowAgent Cloud instances |
| Models and billing | Bring your own key: the model table lists eleven vendors, the CowAgent and LinkAI services, and a "Custom" entry for "Local models / third-party proxy". Optional first-party routes: the CowAgent model service ("a single API key"), ChatGPT sign-in for "Codex subscription" access, and CowAgent Cloud plans with built-in models |
| Default model | `deepseek-flash` in `config-template.json` and `config.py`, with every API key empty. The installer has a "Guided configuration for AI model and channel" step, and the Web console switches providers |
| Best for | Someone who wants an always-on personal agent in Chinese and global IM apps, with memory and a knowledge base that grow on their own, and possibly several specialised agents |
| Main cost | Source and Docker installs default to `full-access`, and the permission modes are "argument-level checks, not an OS sandbox". The Web console has no password unless you set `web_password` |
| Docs | [docs.cowagent.ai](https://docs.cowagent.ai/intro/index) · [repo docs](https://github.com/zhayujie/CowAgent/tree/master/docs) · [cowagent.ai](https://cowagent.ai) |

## What It Is

The README opens with: *"**CowAgent** is your own open-source personal AI agent. It plans tasks proactively, uses tools, skills and MCP, and gets to know you over time through long-term memory, a knowledge base and self-evolution. It's also an open, extensible Agent Harness."* The architecture is one pipeline: "messages flow in through **Channels**; the **Agent Core** plans and reasons over memory, knowledge, and the available tools and skills; **Models** generate the response, which is sent back through the originating channel."

Around that loop it puts:

- **Tools**: `read` / `write` / `edit` / `ls`, `bash`, `send`, `memory`, `env_config`, `web_fetch`, `scheduler`, `web_search`, `vision` and `browser` (installed with `cow install-browser`), plus MCP servers configured in one `mcp.json`.
- **Skills** from the Skill Hub, GitHub, ClawHub or a URL, or written in conversation with `skill-creator`.
- **Memory** in three tiers: conversation context, daily files in `memory/YYYY-MM-DD.md`, and `MEMORY.md`, which "is injected into the system prompt for every conversation." A daily summary runs at 23:55, and **Deep Dream** then distills it into `MEMORY.md` (`deep_dream_enabled` defaults to `true`). Retrieval mixes FTS5 keyword search and vector search.
- **A personal knowledge base** (`knowledge: true` by default) that curates topics into a Markdown wiki with a knowledge-graph view.
- **Self-Evolution**: after a conversation goes idle (10 minutes by default) and has enough turns (6 by default), a separate task with "a restricted toolset" saves memory, fixes or creates skills and follows up on unfinished tasks. Each review takes a backup and can be undone. `config.py` and the template set `self_evolution_enabled` to `true`; the docs table lists `false` and adds "(on by default for new installs)".
- **Multi-agent**: persistent team members with "its own memory, capabilities, knowledge, and workspace", a lead agent that delegates to them, and short-lived sub-agents that share the lead's workspace (`max_concurrent: 3` per call, `max_depth: 1`).
- **Scheduled tasks**: one-time, fixed-interval or cron schedules that send a fixed message or run an agent task, with the result written back into the user's session.

## When To Pick It

- Your users live in Chinese IM apps. The channel table covers WeChat, Feishu / Lark, DingTalk, WeCom Bot, WeCom App, WeChat Customer Service, WeChat Official Account and QQ, as well as Telegram, Slack and Discord. One instance "can serve multiple channels in parallel."
- You want several specialised agents. Each team member can have its own model, skills, knowledge base and workspace, and channel instances can be bound to different agents or teams.
- You want memory that maintains itself and stays readable. Memory, dream diaries and evolution records are Markdown files in the workspace (`~/cow` by default), browsable in the Web console.
- You want a wide model choice, including Chinese providers (DeepSeek, Qwen, GLM, Kimi, MiniMax, Doubao, ERNIE, MiMo) and local models, with chat, vision, image generation, speech and embeddings each routable to a different vendor.
- You want the same agent on a phone. The mobile app can run the agent on the phone or pair with an instance on a computer, server or CowAgent Cloud.

## When Not To Pick It

- **You need an approval step before risky actions on a computer or server.** The three permission modes (`read-only`, `workspace-write`, `full-access`) allow or refuse a call; the docs describe no per-action approval on the desktop or server. Per-action prompts exist only for phone capabilities in the mobile app: "It asks before each action".
- You expect confinement by default. `agent_permission_mode` defaults to `full-access`; only fresh desktop and mobile installs are set to `workspace-write`, and "docker/source stay at full-access." SECURITY.md says the modes "are argument-level checks, not an OS sandbox", and the policy code says a program started by `bash` "can still write wherever the OS lets it." The docs advise "for strong isolation, run inside a container."
- You plan to expose it without hardening. `web_password` is empty by default ("empty means no authentication required"). With `web_host` left empty, the console listens on `127.0.0.1` without a password and on `0.0.0.0` once a password is set. The README's disclaimer says "only deploy it in trusted environments."
- You need roles, workspaces and audit logs in the open-source build. The README lists "role-based access, audit logs" under LinkAI's enterprise features, not the open-source project.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Delivery surfaces | Very strong | Web console, desktop client, mobile app (beta), eleven IM channels, an off-by-default OpenAI-compatible chat API |
| Memory | Very strong | Three tiers, nightly Deep Dream, knowledge base and Self-Evolution, all as workspace files |
| Tool use | Strong | Files, shell, browser, web, vision, scheduler, MCP and a skill marketplace |
| Multi-agent | Strong | Persistent agent teams with their own workspaces, delegation, parallel sub-agents |
| Scheduling | Medium | Cron, interval and one-time tasks through the scheduler tool, plus the nightly memory jobs |
| Human approval | Weak | Session permission modes; per-action prompts only for phone capabilities |
| Governance | Medium | MIT, PRs open to forks; team roles and audit are offered through LinkAI, not in the repo |

## Operating Cost

Low to start: one installer command (`bash <(curl -fsSL https://cdn.link-ai.tech/code/cow/run.sh)`, or `irm … run.ps1 | iex` on Windows) or `docker compose up -d`, then open `http://localhost:9899`. The installer clones to `~/CowAgent` and needs Python 3.7–3.13 ("3.9 recommended"). The desktop client bundles the backend, and CowAgent Cloud needs no server. Exposing the console takes more work: set `web_host` and `web_password`, open port 9899, and for TLS the docs recommend an nginx reverse proxy. The Docker compose file keeps `AGENT_PERMISSION_MODE: 'full-access'` with the comment "Container is already an isolation boundary". Agent mode also "consumes substantially more tokens than regular chat", the README warns. Five releases shipped between 2026-09-14 (v2.1.9) and 2026-11-26 (v2.3.0), and `cow update` pulls the latest code and restarts.

## Relationship To The Rest Of This Map

CowAgent shares the self-hosted lane with [nanobot](nanobot.md), [OpenClaw](openclaw.md) and [Hermes Agent](hermes-agent.md): one runtime you own, many chat surfaces, memory and schedules. Against [nanobot](nanobot.md), it has a similar file-based memory with a dream-style consolidation and a similar lack of per-action approval, but it adds named permission modes and agent teams whose members keep separate workspaces and memory; nanobot's docs say to run separate instances for separate memory. Its channel list leans harder on Chinese enterprise and WeChat-family apps, and it can install skills from ClawHub alongside its own Skill Hub.

## Bottom Line

CowAgent fits if you want a personal agent, or a small team of agents, that lives on your machine or server and answers in WeChat, Feishu, DingTalk, QQ, Telegram or Slack, with memory and a knowledge base that curate themselves into files you can read. The defaults assume a trusted owner: `full-access` on source and Docker installs, no console password, and no per-action approval. Switch sessions to `workspace-write`, set a password, and run it in a container before you connect it to people you do not fully trust.

## Sources

- [zhayujie/CowAgent README](https://github.com/zhayujie/CowAgent) · [LICENSE](https://github.com/zhayujie/CowAgent/blob/master/LICENSE) · [SECURITY.md](https://github.com/zhayujie/CowAgent/blob/master/SECURITY.md) · [CONTRIBUTING.md](https://github.com/zhayujie/CowAgent/blob/master/CONTRIBUTING.md) · [Releases (v2.3.0, Nov 26 2026)](https://github.com/zhayujie/CowAgent/releases) · [config-template.json](https://github.com/zhayujie/CowAgent/blob/master/config-template.json) · [config.py](https://github.com/zhayujie/CowAgent/blob/master/config.py) · [permission policy](https://github.com/zhayujie/CowAgent/blob/master/agent/permission/policy.py) · [docker-compose.yml](https://github.com/zhayujie/CowAgent/blob/master/docker/docker-compose.yml)
- Docs: [Architecture](https://docs.cowagent.ai/intro/architecture) · [Choose How to Use](https://docs.cowagent.ai/guide) · [Quick Start](https://docs.cowagent.ai/guide/quick-start) · [Mobile App](https://docs.cowagent.ai/guide/mobile) · [CowAgent Cloud](https://docs.cowagent.ai/guide/cloud) · [Web Console](https://docs.cowagent.ai/channels/web) · [Channels](https://docs.cowagent.ai/channels/index) · [Models](https://docs.cowagent.ai/models/index) · [Long-term Memory](https://docs.cowagent.ai/memory/index) · [Deep Dream](https://docs.cowagent.ai/memory/deep-dream) · [Self-Evolution](https://docs.cowagent.ai/memory/self-evolution) · [Agent Teams](https://docs.cowagent.ai/multi-agent/team) · [Sub-Agent](https://docs.cowagent.ai/multi-agent/subagent) · [Scheduler](https://docs.cowagent.ai/tools/scheduler)
