# CodeWhale

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/codewhale.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](codewhale.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: CodeWhale (formerly DeepSeek-TUI) is an open-source Rust terminal coding agent — the same shape as Claude Code or Codex CLI — that began as a DeepSeek-only client and now describes itself as provider-neutral, with 40+ built-in provider routes, any OpenAI-compatible endpoint, and local models through Ollama, vLLM or SGLang. DeepSeek is still the default provider; it is no longer the point.

> **Rebrand (late May 2026):** The project renamed from `Hmbown/DeepSeek-TUI` to `Hmbown/CodeWhale` and broadened from DeepSeek-only to **DeepSeek + MiMo** (Xiaomi's open model). It ships a product site at [codewhale.net](https://codewhale.net/). Older links to `DeepSeek-TUI` redirect.

> **Moved and repositioned (October 2026, corrected 2026-10-14):** the repository now lives at [`codewhale-hq/Codewhale`](https://github.com/codewhale-hq/Codewhale) (the move pre-dates the 2026-10-07 fetch; this map noticed it one window late), spells itself "Codewhale", and its README states it is "provider-neutral and independently maintained, and is not affiliated with any model provider". This profile had described it as a DeepSeek/MiMo-native agent whose main cost was a narrow model set; that framing is corrected in place below. The engine is now split from the terminal client ("agent engine and terminal client"), a `codewhale login` account can hold provider keys centrally, and v0.10.1 shipped on October 8. Old `Hmbown/*` links redirect.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | codewhale-hq (open source community, "independently maintained"; formerly under Hmbown) |
| Route | Direct execution — terminal coding agent |
| Open source | Yes — MIT |
| Implementation | Rust (engine + terminal client); npm and crates.io installs |
| Models | Any — 40+ provider routes (Anthropic, DeepSeek, Google, Mistral, Moonshot, OpenAI, OpenRouter, xAI …), OpenAI-compatible endpoints, local runtimes. **DeepSeek remains the default provider** |
| Best for | Developers who want a Claude-Code-style loop they can point at whichever model is cheapest or available to them — including Chinese-stack and local models — without a vendor's own CLI |
| Main cost | A community project with a fast-moving surface and an optional account layer; provider breadth means the quality of the loop varies with the model you plug in |
| GitHub repo | https://github.com/codewhale-hq/Codewhale |

## When To Pick It

- You want a terminal coding agent that is not tied to one vendor's model line, and you switch providers (or run local models) often enough that `/provider` and `/model` inside the session matter.
- You want DeepSeek, Moonshot or MiMo models in a Claude-Code-shaped loop with first-class support, but want the option to swap to Anthropic or OpenAI routes without changing tools.
- You prefer a minimal terminal surface over a desktop or IDE-based experience, with explicit modes (Plan explores, Work and Operate change things), approval postures, `/undo` and `/restore`, and per-session receipts.

## When Not To Pick It

- You want a vendor-maintained client with a stability promise — [Claude Code](claude-code.md), [Codex](codex.md) or [Gemini CLI](gemini-cli.md) are maintained by the model's own vendor.
- You want a harness to build on rather than a finished agent — [Pi](pi.md) or [Aider](aider.md) expose more of the loop.
- You need cloud delegation, parallel agents, or background runs — that is [Codex](codex.md) or [Devin](devin.md) territory.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Terminal workflow | Strong | TUI-native loop; Plan / Work / Operate modes; receipts for every file, command and approval |
| Multi-provider support | Strong | 40+ routes plus OpenAI-compatible and local; was "light" in this profile until 2026-10-14, which was out of date |
| DeepSeek / MiMo tuning | Strong | Where the project started; DeepSeek is still the default provider and reads `deepseek-tui` configuration and sessions |
| Background execution | Not the goal | Foreground, single-developer loop |

## Operating Cost

Complexity is Low–Medium. Installing it is straightforward (npm or crates.io); the model bill is whatever provider you route to, with no markup. The optional Codewhale account stores provider keys for your signed-in devices; local use works without it. Pricing exposure follows the provider you choose, not the agent.

## Bottom Line

CodeWhale first appeared in this map's heat snapshot as DeepSeek-TUI, a DeepSeek-native terminal agent. It is now the opposite bet: a provider-neutral Claude-Code-shaped loop that keeps DeepSeek as its default but treats every route — including local runtimes — as first-class. If you want one terminal agent across several model vendors, or want Chinese-stack models without giving up the option of the others, it is the most direct path. If you want the vendor's own client, pick the vendor's own client.
