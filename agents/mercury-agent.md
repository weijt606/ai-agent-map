# Mercury Agent

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/mercury-agent.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](mercury-agent.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Mercury Agent is a permission-hardened self-hosted assistant designed to run 24/7 across CLI and Telegram, not a one-shot coding tool.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | cosmicstack-labs |
| Route | Self-hosted multi-channel agent with permission guardrails |
| Open source | Yes (MIT, TypeScript) |
| Best for | Always-on personal or team agent that needs approvals, token budgets, and persistent memory |
| Main cost | You own the daemon, the permission policy, and the channel surface |
| Official website | https://mercury.cosmicstack.org |
| GitHub repo | https://github.com/cosmicstack-labs/mercury-agent |

## When To Pick It

- You want a long-running assistant reachable from both terminal and Telegram, with a single persistent state.
- You want explicit approval workflows, shell blocklists, and folder-level scoping rather than implicit autonomy.
- You want a daily token budget with auto-concise mode so spend cannot drift unbounded.
- You want a transparent personality layer (`soul.md`, `persona.md`) you can edit and version yourself.

## When Not To Pick It

- You only want a one-off coding agent that finishes a task and exits.
- You do not want to run a daemon, manage a SQLite store, or curate permissions over time.
- You need a polished managed product with vendor SLAs.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Tool use | Strong | 31 built-in tools across filesystem, shell, git, web, scheduler, and messaging |
| Permissions | Very strong | Shell blocklist, folder scoping, and approval workflows are first-class |
| Memory | Strong | SQLite-backed "Second Brain" with 10 memory types and full-text search |
| Scheduling | Strong | Persistent scheduler plus daemon mode with auto-restart |
| Multi-channel access | Strong | CLI streaming and Telegram with admin/member roles |
| Provider freedom | Strong | DeepSeek, OpenAI, Anthropic, Grok, Ollama Cloud, and local Ollama with fallback |

## Operating Cost

Complexity is Medium. Installation is straightforward, but Mercury is a daemon you keep alive — permission policies, memory hygiene, and channel access need ongoing attention. The token-budget feature limits financial blast radius but does not remove the operational surface.

## How It Compares Inside The Self-Hosted Lane

- Versus [Hermes Agent](hermes-agent.md): Hermes leans into memory, skills, and subagent delegation as the operating model. Mercury leans into permission hardening, token budgets, and Telegram-as-channel.
- Versus [OpenClaw](openclaw.md): OpenClaw is a broader runtime and gateway across many channels and devices. Mercury is narrower — CLI plus Telegram, with stricter approval discipline.
- Versus [Goose](goose.md): Goose is desktop / CLI / API with extensions. Mercury foregrounds approval and budget guardrails over extension breadth.

## Bottom Line

If you want a self-hosted always-on assistant with strict permissions, a real token budget, and a Telegram surface, Mercury is worth a serious look. If you want pure coding execution or a managed product, look elsewhere first.
