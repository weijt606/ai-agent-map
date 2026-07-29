# Grok Build

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/grok-build.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](grok-build.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Grok Build (`grok`) is SpaceXAI's official terminal coding agent — a Rust, full-screen TUI that edits code, runs shell commands, searches the web, and manages long-running tasks, and that also runs headless in CI or embeds in editors over ACP.

> **Naming and boundary:** the binary is `grok`, the product is **Grok Build**, and the repo is [`xai-org/grok-build`](https://github.com/xai-org/grok-build) under the `x.ai` domain — but the README, logo, and docs brand the vendor as **SpaceXAI**. Treat "xAI" and "SpaceXAI" as the same vendor surface. The built artifact is named `xai-grok-pager`; official installs ship it as `grok`.

> **Source-available, not community-developed.** The Apache-2.0 license is real, but the repo is *synced periodically from the SpaceXAI monorepo* (a `SOURCE_REV` file records the upstream commit), and `CONTRIBUTING.md` states plainly that **external contributions are not accepted**. You can read, fork, and build it; you cannot upstream to it. This is the opposite of the fork-and-own harness bargain.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | SpaceXAI / xAI (`xai-org/grok-build`, x.ai/cli) |
| Route | Direct execution — vendor-official terminal coding agent |
| Open source | Apache-2.0 (source-available; external contributions not accepted) |
| Implementation | Rust |
| License | Apache-2.0 (first-party code); vendored third-party under original licenses |
| Models | Grok — browser OAuth to a SpaceXAI account on first launch |
| Best for | Developers on Grok models who want a fast, first-party TUI with headless CI and editor (ACP) reach |
| Main cost | Two weeks old and vendor-bound; you cannot contribute upstream despite the OSS license |
| GitHub repo | https://github.com/xai-org/grok-build |

## When To Pick It

- You are already on Grok/SpaceXAI models and want the agent loop and the model shipped by the same team, rather than a third-party harness pointed at an xAI endpoint.
- You want one binary that covers three modes: an interactive full-screen TUI (mouse-interactive, themeable), **headless** execution for scripting and CI, and an **ACP** agent server so ACP-compatible editors can drive it — the same three-surface shape [Kimi Code](kimi-code.md) offers on the Moonshot side.
- You want the extension surface the current generation expects — MCP servers, skills, plugins, hooks, slash commands — with sandboxing and workspace checkpoints built into the runtime rather than bolted on.
- You want a Rust implementation for boot speed and footprint, like [jcode](jcode.md), but from a vendor rather than an independent project.

## When Not To Pick It

- You want to own and extend the loop — the license lets you fork, but development is closed and the tree is a monorepo export, so your changes live downstream forever. [Pi](pi.md), [jcode](jcode.md), or [OpenHands](openhands.md) are the fork-and-own picks.
- You want provider neutrality as the core value. Grok Build authenticates to a SpaceXAI account by design; a provider-agnostic base like [Pi](pi.md), [jcode](jcode.md), or [Aider](aider.md) is safer if you switch models often.
- You need a mature, stable surface today — the repo is roughly two weeks old and moving fast.
- You need cloud delegation, scheduled background runs, or parallel remote agents — that is [Codex](codex.md), [Devin](devin.md), or [Claude Managed Agents](claude-managed-agents.md) territory.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Terminal workflow | Very strong | Full-screen, mouse-interactive TUI with scrollback, modals, theming, slash commands |
| Code execution | Very strong | Shell execution, file edits, and search as first-class tools; sandboxing and workspace checkpoints in the runtime |
| Grok model tuning | Very strong | First-party; agent and model ship from the same vendor |
| Delivery surfaces | Strong | One binary in three modes — interactive TUI, headless (scripting/CI), and ACP agent server for editors |
| Extensibility | Strong | MCP servers, skills, plugins, hooks — though extensions live beside a tree you cannot upstream to |
| Provider neutrality | Not the goal | Browser OAuth to a SpaceXAI account is the default and documented path |
| Community development | Not the goal | Contributions explicitly not accepted; repo is a periodic monorepo sync |

## Lineage Note

Per the repo's own `THIRD-PARTY-NOTICES` and the crate-local notice in `xai-grok-tools`, Grok Build carries **in-tree source ports of [`openai/codex`](codex.md) and `sst/opencode` tool implementations**, with the Apache §4(b) change notice attached. That is worth knowing when comparing tool behavior: the tool layer is not a clean-room design, and some of its semantics will feel familiar if you have used Codex.

## Operating Cost

Complexity is Low–Medium to *use*, higher to *depend on*. Install is a one-line script (`curl -fsSL https://x.ai/cli/install.sh | bash`, or PowerShell on Windows) with prebuilt macOS/Linux/Windows binaries, and first launch handles auth in the browser. Building from source is heavier than most: it needs a pinned Rust toolchain plus **DotSlash** for hermetic tooling (`protoc`), the root `Cargo.toml` is generated and read-only, and Windows source builds are best-effort. The strategic cost is the governance shape — a two-week-old, vendor-controlled tree you cannot contribute to, so every local change is a permanent downstream diff.

## Bottom Line

Grok Build is the vendor-official answer to "I want a Claude-Code-style terminal agent, but Grok-native and in Rust." It arrived unusually loud — 23k stars and 4.4k forks inside two weeks — and the substance is real: a polished TUI, headless CI mode, ACP editor reach, MCP/skills/plugins/hooks, and sandboxing. Read the governance carefully, though: Apache-2.0 here means *source-available*, not *community-built*, and the model path points at SpaceXAI. If you want the same Rust-grade speed with a loop you actually own, see [jcode](jcode.md) or [Pi](pi.md); for the vendor-official equivalents on other model stacks, see [Codex](codex.md), [Claude Code](claude-code.md), [Kimi Code](kimi-code.md), and [MiMoCode](mimocode.md). For the route-level comparison, see [coding CLI agents](../comparisons/coding-cli-agents.md).
