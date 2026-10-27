# ECC

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/ecc.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](ecc.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: ECC is a plugin you install into an existing coding agent that brings a whole engineering system with it — 71 subagents, 311 skills, hooks, rules, a local memory vault, and the AgentShield config scanner — organised around a plan → test → implement → review → verify → remember → improve loop.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Affaan Mustafa (single maintainer, per the README) and contributors |
| Route | Agentic skills framework — a skills, hooks, and memory layer that runs inside a host agent |
| Repository | [`affaan-m/ECC`](https://github.com/affaan-m/ECC) — MIT, JavaScript; 290.6k stars as of 2026-10-28 |
| Open source | Yes (MIT). A hosted **ECC Pro** GitHub App is paid: free for public repos, $19/seat/month for private repos, Enterprise on request |
| Works with | [Claude Code](claude-code.md) (stable, primary); [Codex](codex.md) and Qoder (native plugins); [Cursor](cursor.md), [OpenCode](opencode.md), GitHub Copilot CLI (beta); Gemini, Zed, Antigravity, Qwen, [Hermes](hermes-agent.md), [OpenClaw](openclaw.md), Kimi and others (experimental adapters); [GitHub Copilot](github-copilot.md) Chat (instructions only) |
| Best for | Claude Code users who want planning, TDD, fresh-context review, hook-enforced checks, and agent-config security scanning in one install |
| Main cost | A large surface to install and keep in context; the README itself warns against stacking install methods and recommends a minimal profile when context footprint matters |
| Current release | 2.2.3 (2026-10-01); install with `npx ecc-universal@2.2.3 setup` |
| Website | https://ecc.tools |

## How It Works

ECC splits its work across five kinds of component, each with a different context cost. **Skills** (311) are workflows such as TDD, security review, or deep research, loaded only when a task needs them. **Agents** (71) are scoped subagents with their own context and tool permissions, used to keep planning, implementation, and review apart. **Rules** are always-loaded standards that you install per language. **Hooks** run outside the model on harness events: session summaries, continuous learning, and GateGuard, which gates destructive shell commands such as `rm` or a forced `git checkout` before they run. **Instincts** are patterns learned from past sessions, stored with confidence scores and recalled when relevant.

Two pieces sit beside that core. The **Memory Vault** (`ecc memory`, added in the 2.2 line) stores durable context and cross-harness handoffs as local Markdown under `.ecc/memory/`; the README states that memory is unreviewed context, not executable policy. **AgentShield**, also shipped as the `ecc-agentshield` npm package, scans `CLAUDE.md`, settings, MCP configs, hooks, agent definitions, and skills for secrets, permission problems, hook injection, and risky MCP servers.

**How it differs from [Superpowers](superpowers.md).** Both sit inside a host agent and ship a stage-based development cycle. Superpowers' loop is brainstorm → design → plan → implement → review → complete, and its README uses hooks only to bootstrap the skills at session start. ECC adds runtime pieces that Superpowers' README does not describe: hooks used for enforcement, the Memory Vault and instincts for memory, a security scanner, and a paid hosted GitHub App. The trade is coverage against footprint. ECC's own install docs spend a section on keeping it from crowding the context window.

## When To Pick It

- You work mainly in [Claude Code](claude-code.md), which the README marks as the stable primary harness, and want a ready-made system rather than assembling skills yourself.
- You want checks enforced by hooks outside the prompt (GateGuard, session summaries) rather than reminders the model may forget.
- You want to audit your own agent setup (hooks, MCP servers, permissions, secrets) with AgentShield.
- You switch between harnesses and want one local, inspectable Markdown format for handoffs between them.

## When Not To Pick It

- You want a standalone agent. ECC does not run a loop of its own; it changes how an installed harness behaves.
- You rely on Cursor, OpenCode, Gemini, or the other non-Claude adapters for parity. The README labels those beta, experimental, or instruction-only and says full Claude feature parity is not claimed.
- You want a small skill set. The default install is large; use `--profile minimal` or a selective install if context footprint matters.
- You are on native Windows and need continuous learning or Memory Vault writes. The README lists open native-Windows defects for both and recommends WSL.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Skill and agent catalog | Very strong | 71 agents, 311 skills, 97 command shims; skills load on demand |
| Enforcement via hooks | Strong | GateGuard gates destructive shell commands; hooks run outside the model context |
| Memory | Solid | Memory Vault (local Markdown, optional MCP server) plus learned instincts; recall is treated as unreviewed context |
| Agent-config security | Strong | AgentShield scans prompts, hooks, MCP config, permissions, secrets, and agent files |
| Cross-harness parity | Uneven | Stable on Claude Code, native on Codex and Qoder, beta or experimental elsewhere |
| Standalone runtime | Not the goal | Runs inside a host agent |

## Operating Cost

Complexity is Medium to High. Setup is one guided command, but you are adopting a large catalog plus runtime hooks, and the README spends whole sections on not installing twice, trimming rules, and disabling unused MCP servers to keep context under control. The OSS layer is MIT; private-repo analysis through the hosted GitHub App is $19 per seat per month.

## Bottom Line

ECC packs a methodology plus subagents, hooks, memory, and a security scanner into one plugin. Pick it if you live in Claude Code and want the system ready-made. Pick [Superpowers](superpowers.md) if you want the methodology without the runtime layer. Either way, the host agent's capabilities still set the ceiling.

## Sources

- [ECC README](https://github.com/affaan-m/ECC#readme) · [Releases](https://github.com/affaan-m/ECC/releases) · [2.0.0 release notes](https://github.com/affaan-m/ECC/blob/main/docs/releases/2.0.0/release-notes.md) · [LICENSE (MIT)](https://github.com/affaan-m/ECC/blob/main/LICENSE) · [ECC Tools pricing](https://ecc.tools/pricing) · [Superpowers README](https://github.com/obra/superpowers#readme)
