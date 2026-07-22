# jcode

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/jcode.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](jcode.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: jcode is a Rust terminal coding-agent harness built for multi-session workflows and raw performance — a provider-neutral loop you own end to end, with a passive semantic-memory graph as its signature feature rather than a vendor product you adopt as-is.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Independent (`1jehuang/jcode`, jcode.sh) |
| Route | Agent harness framework — terminal-first coding harness |
| Open source | Yes |
| Implementation | Rust |
| License | MIT |
| Models | Provider-neutral — OAuth to Claude, OpenAI/ChatGPT/Codex, Gemini, Copilot, Azure; plus any OpenAI-compatible endpoint (OpenRouter, DeepSeek, Kimi/Moonshot, Ollama, LM Studio, …) |
| Best for | Developers who want a fast, low-footprint harness they can customize deeply, run many sessions of, and point at whatever model they already pay for |
| Main cost | Younger project moving fast; the harness surface and config are still settling |
| GitHub repo | https://github.com/1jehuang/jcode |

## When To Pick It

- You want to own the loop, tool surface, and configuration — like [Pi](pi.md) — but with an emphasis on speed and scale: jcode's Rust core boots in ~14 ms to first frame and holds the lowest RAM in its class, which matters when you run many parallel sessions.
- You want one harness that talks to whatever model you already subscribe to — it logs in over OAuth to Claude, OpenAI, Gemini, and Copilot, and speaks the shared OpenAI-compatible API for almost everything else.
- You want memory that works without babysitting: jcode embeds each turn as a semantic vector and auto-recalls relevant history through a memory graph (with an optional verifier side-agent), instead of making the model call memory tools by hand — while still exposing explicit memory + session-search tools when you want them.

## When Not To Pick It

- You want a vendor-tuned product where the model and loop ship from the same team — that is [Claude Code](claude-code.md), [Codex](codex.md), or [Kimi Code](kimi-code.md), not a fork-and-own harness.
- You need a mature, stable surface today — jcode is younger and iterating quickly, so expect churn in config and features.
- You want to publish SWE-bench numbers or read the entire loop in one sitting — [SWE-agent](swe-agent.md) and [mini-swe-agent](mini-swe-agent.md) are the research-reference and minimal picks respectively.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Performance / footprint | Very strong | Rust core; fastest boot and lowest RAM among mainstream coding CLIs by its own benchmarks |
| Multi-session workflows | Strong | Designed to scale to many concurrent sessions cheaply |
| Passive memory | Very strong | Semantic-vector memory graph with auto-recall + optional verifier side-agent; explicit memory and session-search tools also available |
| Provider neutrality | Very strong | OAuth to the major vendors plus a shared OpenAI-compatible provider for the long tail |
| Extensibility | Strong | MCP config, "infinite customizability" is the stated design goal |
| Vendor-official model tuning | Not the goal | Provider-neutral by design; no first-party model |

## Operating Cost

Complexity is Low–Medium. Install is a one-line script (`curl -fsSL https://jcode.sh/install | bash`, or PowerShell on Windows), and the Rust binary is light on resources. The real cost is maturity: jcode is a younger, fast-moving project, so config formats and features are still moving. The passive memory system is powerful but is one more subsystem to understand if you want to tune what gets recalled.

## Bottom Line

jcode is the harness pick for "I want to own the loop like [Pi](pi.md), but faster, leaner, and provider-agnostic — and I want memory that just works." Its distinguishing bets are Rust-grade performance for many-session workflows and a passive semantic-memory graph, on top of broad multi-provider OAuth. If you want a vendor-tuned product instead, [Claude Code](claude-code.md), [Codex](codex.md), or [Kimi Code](kimi-code.md) fit; if you want the smallest readable base or SWE-bench reproducibility, see [mini-swe-agent](mini-swe-agent.md) and [SWE-agent](swe-agent.md). For the full harness comparison, see [agent harness frameworks](../comparisons/agent-harness-frameworks.md).
