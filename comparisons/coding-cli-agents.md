# Terminal Coding CLI Agents

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/coding-cli-agents.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](coding-cli-agents.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

This page compares the projects that all solve the same shape of problem: a **terminal-native coding agent** — a single-process loop you run in your shell that reads and edits code, runs commands, and iterates on feedback.

This category exploded in 2026. Every major model vendor now ships its own CLI in the Claude Code mold, plus open-source and Chinese-stack entrants. They look almost identical on the surface; the real differences are which models they are tuned for, who maintains them, and what one thing each does better than the rest.

## What Counts As A Coding CLI Here

In scope: foreground, single-developer terminal loops whose primary job is writing code. Out of scope and covered elsewhere:

- **Editor-centric surfaces** — [Cursor](../agents/cursor.md), [Windsurf](../agents/windsurf.md), [Continue](../agents/continue.md), [TRAE](../agents/trae.md) (the editor is the agent, not the terminal; TRAE CLI 2.0 exists only on the China enterprise flagship plan).
- **Cloud delegation / managed execution** — [Devin](../agents/devin.md), [Jules](../agents/jules.md), [Claude Managed Agents](../agents/claude-managed-agents.md) (you hand off and check back, not a foreground loop).
- **Desktop task surfaces** — [ZCode](../agents/zcode.md) (direct execution, but a GUI, not a terminal loop).
- **Harness frameworks you fork and own** — [Pi](../agents/pi.md), [jcode](../agents/jcode.md), [OpenHands](../agents/openhands.md), [SWE-agent](../agents/swe-agent.md), [mini-swe-agent](../agents/mini-swe-agent.md), [OpenHarness](../agents/openharness.md), [DeepSeek Harness](../agents/deepseek-harness.md) (compared in [agent harness frameworks](agent-harness-frameworks.md)). Pi and jcode are terminal-first and coding-capable, but their value is owning the loop, not adopting a vendor product.

## One-Page Comparison

| Project | Vendor | Models (default) | Lang / License | One thing it does best |
| --- | --- | --- | --- | --- |
| [Claude Code](../agents/claude-code.md) | Anthropic | Claude (Opus / Sonnet) | Proprietary | The reference implementation — deepest IDE/desktop/web reach and the richest skills + plugin ecosystem |
| [Codex](../agents/codex.md) | OpenAI | GPT-6.1 Sol (bundled default since `rust-v0.159.1`) | Open source CLI | Pairs a terminal loop with isolated cloud delegation and parallel agents on the same product surface |
| [OpenCode](../agents/opencode.md) | Anomaly Co (community) | Bring your own | TypeScript / MIT | The largest vendor-neutral loop — 222k stars (2026-10-28), and the one other harnesses build on |
| [Gemini CLI](../agents/gemini-cli.md) | Google | Gemini 3 | TypeScript / Apache-2.0 | Open-source loop with Google Search grounding built in; since 2026-06-18 it serves Code Assist Standard/Enterprise licences and paid API keys, not free or Google AI Pro/Ultra users |
| [Antigravity CLI](../agents/antigravity.md) (`agy`) | Google | Gemini (Claude on paid plans) | Go / closed (the CLI repo holds docs only) | Where Google moved consumer Gemini CLI users on 2026-06-18: a free weekly quota, Gemini-only from 2026-11-02, shared with the Antigravity app; the terms forbid driving it from third-party agents |
| [Qwen Code](../agents/qwen-code.md) | Alibaba / Qwen | Qwen (switchable at runtime) | TypeScript / Apache-2.0 | Open client *and* open weights, speaking OpenAI/Anthropic/Gemini/local protocols |
| [Aider](../agents/aider.md) | Open source | Bring your own | Python / Apache-2.0 | Git-centered loop with explicit diffs and total model freedom |
| [Kimi Code](../agents/kimi-code.md) | Moonshot AI | Kimi | TypeScript / MIT | First-party Kimi loop with strong IDE reach via ACP + a VS Code extension |
| [CodeBuddy Code](../agents/codebuddy.md) | Tencent Cloud | Multi-vendor built-in catalog (Hunyuan/Hy3 and DeepSeek named), or any OpenAI-format endpoint | Closed (an MIT text ships with a minified bundle) | One CLI across international, China, dedicated-cloud and self-hosted editions, sharing an account with a plugin and an IDE |
| [MiMoCode](../agents/mimocode.md) | Xiaomi | MiMo (MiMo Auto) | TypeScript / MIT | Persistent cross-session memory built in — keeps project understanding across runs |
| [CodeWhale](../agents/codewhale.md) | codewhale-hq (community) | Any — 40+ provider routes, DeepSeek default | Rust / open source | Claude-Code shape, provider-neutral since its Hmbown → codewhale-hq move; began DeepSeek-only |
| [Grok Build](../agents/grok-build.md) | SpaceXAI / xAI | Grok | Rust / Apache-2.0 (source-available) | One binary covering three modes — full-screen TUI, headless CI, and an ACP server editors can drive |

> Vendor-official CLIs (Claude Code, Codex, Gemini CLI, Antigravity CLI, Qwen Code, Kimi Code, MiMoCode, Grok Build) tune the model and the loop together. Third-party/community CLIs (OpenCode, Aider, CodeWhale) trade that for portability or a specific cost/model target.
>
> **Open source is not one thing here.** Aider (Apache-2.0), Kimi Code and MiMoCode (MIT) take outside contributions. [Grok Build](../agents/grok-build.md) ships Apache-2.0 source but is a periodic export from SpaceXAI's monorepo and **explicitly does not accept external contributions** — read it, fork it, but you cannot upstream to it.

## How To Choose

1. **Start from the model you want to run.** If you are committed to a vendor's models, its first-party CLI is usually the best-tuned path: Claude → [Claude Code](../agents/claude-code.md), GPT → [Codex](../agents/codex.md), Gemini → [Antigravity CLI](../agents/antigravity.md) on a personal Google account or [Gemini CLI](../agents/gemini-cli.md) on a Code Assist Standard/Enterprise licence or paid API key, Kimi → [Kimi Code](../agents/kimi-code.md), Qwen → [Qwen Code](../agents/qwen-code.md), MiMo → [MiMoCode](../agents/mimocode.md), Grok → [Grok Build](../agents/grok-build.md), DeepSeek/MiMo on a budget → [CodeWhale](../agents/codewhale.md). If you are *not* committed, [OpenCode](../agents/opencode.md) is the vendor-neutral default. Gemini CLI's free tier is no longer the consumer path: Google moved those users to [Antigravity CLI](../agents/antigravity.md), whose free tier is a weekly quota with no published numbers, Gemini-only from 2026-11-02.
2. **If model freedom matters more than tuning,** pick a provider-neutral base: [Aider](../agents/aider.md) for a finished CLI, or step up to the [Pi](../agents/pi.md) harness if you want to own the loop.
3. **If long-horizon memory on one repo is the pain point,** [MiMoCode](../agents/mimocode.md)'s built-in cross-session memory is the clearest differentiator; otherwise pair any CLI with [CodeGraph](../agents/codegraph.md) or [Graft](../agents/graft.md) for code-context indexing.
4. **If you need cloud delegation or background runs,** none of these foreground loops fit — go to [Codex](../agents/codex.md) (cloud side), [Jules](../agents/jules.md), or [Devin](../agents/devin.md).

## Four Things Not To Mix Up

- **A vendor CLI is not just a model endpoint.** Claude Code, Kimi Code, and MiMoCode tune the agent loop, tools, and prompts around their own model — that is the value over pointing a generic harness at the same API.
- **MiMoCode is not [CodeWhale](../agents/codewhale.md).** MiMoCode is Xiaomi's first-party CLI; CodeWhale is a community, provider-neutral Rust TUI (DeepSeek default) that began as a DeepSeek + MiMo wrapper. They share a model family, not a codebase.
- **Apache-2.0 does not mean community-built.** [Grok Build](../agents/grok-build.md) carries a real OSS license on a tree that is closed to contributions and synced from a private monorepo. If your reason for choosing open source is influence over the roadmap rather than the right to read and fork, check the contribution policy, not just the LICENSE file.
- **A coding CLI is not a harness.** If you want to fork, audit, and own the loop end-to-end, that is [Pi](../agents/pi.md) / [OpenHands](../agents/openhands.md) territory, not a vendor product you adopt as-is.

For the broader, all-routes view, see the [mainstream agent selection matrix](mainstream-agent-landscape.md). For a problem-first walkthrough, see the [coding automation guide](../use-cases/coding-automation.md).
