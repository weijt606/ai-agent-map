# Terminal Coding CLI Agents

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/coding-cli-agents.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](coding-cli-agents.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

This page compares the projects that all solve the same shape of problem: a **terminal-native coding agent** — a single-process loop you run in your shell that reads and edits code, runs commands, and iterates on feedback.

This category exploded in 2026. Every major model vendor now ships its own CLI in the Claude Code mold, plus open-source and Chinese-stack entrants. They look almost identical on the surface; the real differences are which models they are tuned for, who maintains them, and what one thing each does better than the rest.

## What Counts As A Coding CLI Here

In scope: foreground, single-developer terminal loops whose primary job is writing code. Out of scope and covered elsewhere:

- **Editor-centric surfaces** — [Cursor](../agents/cursor.md), [Windsurf](../agents/windsurf.md), [Continue](../agents/continue.md) (the editor is the agent, not the terminal).
- **Cloud delegation / managed execution** — [Devin](../agents/devin.md), [Jules](../agents/jules.md), [Claude Managed Agents](../agents/claude-managed-agents.md) (you hand off and check back, not a foreground loop).
- **Harness frameworks you fork and own** — [Pi](../agents/pi.md), [jcode](../agents/jcode.md), [OpenHands](../agents/openhands.md), [SWE-agent](../agents/swe-agent.md) (compared in [agent harness frameworks](agent-harness-frameworks.md)). Pi and jcode are terminal-first and coding-capable, but their value is owning the loop, not adopting a vendor product.

## One-Page Comparison

| Project | Vendor | Models (default) | Lang / License | One thing it does best |
| --- | --- | --- | --- | --- |
| [Claude Code](../agents/claude-code.md) | Anthropic | Claude (Opus / Sonnet) | Proprietary | The reference implementation — deepest IDE/desktop/web reach and the richest skills + plugin ecosystem |
| [Codex](../agents/codex.md) | OpenAI | GPT-5.x | Open source CLI | Pairs a terminal loop with isolated cloud delegation and parallel agents on the same product surface |
| [Aider](../agents/aider.md) | Open source | Bring your own | Python / Apache-2.0 | Git-centered loop with explicit diffs and total model freedom |
| [Kimi Code](../agents/kimi-code.md) | Moonshot AI | Kimi (K2) | TypeScript / MIT | First-party Kimi loop with strong IDE reach via ACP + a VS Code extension |
| [MiMoCode](../agents/mimocode.md) | Xiaomi | MiMo (MiMo Auto) | TypeScript / MIT | Persistent cross-session memory built in — keeps project understanding across runs |
| [CodeWhale](../agents/codewhale.md) | Hmbown (community) | DeepSeek + MiMo | Rust / open source | Claude-Code shape refit around low-cost Chinese-stack models as first-class citizens |

> Vendor-official CLIs (Claude Code, Codex, Kimi Code, MiMoCode) tune the model and the loop together. Third-party/community CLIs (Aider, CodeWhale) trade that for portability or a specific cost/model target.

## How To Choose

1. **Start from the model you want to run.** If you are committed to a vendor's models, its first-party CLI is usually the best-tuned path: Claude → [Claude Code](../agents/claude-code.md), GPT-5.x → [Codex](../agents/codex.md), Kimi → [Kimi Code](../agents/kimi-code.md), MiMo → [MiMoCode](../agents/mimocode.md), DeepSeek/MiMo on a budget → [CodeWhale](../agents/codewhale.md).
2. **If model freedom matters more than tuning,** pick a provider-neutral base: [Aider](../agents/aider.md) for a finished CLI, or step up to the [Pi](../agents/pi.md) harness if you want to own the loop.
3. **If long-horizon memory on one repo is the pain point,** [MiMoCode](../agents/mimocode.md)'s built-in cross-session memory is the clearest differentiator; otherwise pair any CLI with [CodeGraph](../agents/codegraph.md) for code-context indexing.
4. **If you need cloud delegation or background runs,** none of these foreground loops fit — go to [Codex](../agents/codex.md) (cloud side), [Jules](../agents/jules.md), or [Devin](../agents/devin.md).

## Three Things Not To Mix Up

- **A vendor CLI is not just a model endpoint.** Claude Code, Kimi Code, and MiMoCode tune the agent loop, tools, and prompts around their own model — that is the value over pointing a generic harness at the same API.
- **MiMoCode is not [CodeWhale](../agents/codewhale.md).** MiMoCode is Xiaomi's first-party CLI; CodeWhale is a community Rust TUI that wraps DeepSeek + MiMo. They share a model family, not a codebase.
- **A coding CLI is not a harness.** If you want to fork, audit, and own the loop end-to-end, that is [Pi](../agents/pi.md) / [OpenHands](../agents/openhands.md) territory, not a vendor product you adopt as-is.

For the broader, all-routes view, see the [mainstream agent selection matrix](mainstream-agent-landscape.md). For a problem-first walkthrough, see the [coding automation guide](../use-cases/coding-automation.md).
