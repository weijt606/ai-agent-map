# Qwen Code

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/qwen-code.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](qwen-code.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Qwen Code is the rare vendor CLI that is open at both ends — the client is Apache-2.0 and [the models are open-weights too](qwen3-coder.md) — and it will happily run on Anthropic, OpenAI, or a local Ollama endpoint instead.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Alibaba / Qwen |
| Route | Direct execution |
| Repository | [`QwenLM/qwen-code`](https://github.com/QwenLM/qwen-code) — Apache-2.0, TypeScript, **27.7k stars** |
| Open source | Yes (Apache-2.0), and so are the models |
| Best for | Teams that want a vendor CLI without the vendor lock-in that usually comes with one |
| Main cost | Smaller than the leading CLIs; the self-iterating development model is unusual and worth understanding |
| Surfaces | Terminal, IDE plugins, desktop app, daemon mode, SDKs, IM bots |
| Blog | https://qwenlm.github.io/blog/ |

## Why This Entry Exists

This map's direct-execution route documents one vendor CLI per model family, and Alibaba's was missing. It also completes a pair: this map now profiles [Qwen3-Coder](qwen3-coder.md), the open-weights model, and this is the loop its vendor ships to run it.

The interesting property is the combination. Every other first-party CLI here pairs an open or closed client with **closed** weights. Qwen Code is open on both sides, which makes "no vendor lock-in" a checkable claim rather than a slogan.

## When To Pick It

- **You want to switch models at runtime.** It speaks OpenAI, Anthropic, Gemini, and Qwen APIs, plus any third-party provider or a local model through Ollama or vLLM — switchable at runtime rather than at install time.
- You want **agentic features without configuration**: Auto-Memory, Auto-Skills, SubAgents, Agent Teams, and MCP are described as working out of the box.
- You need it **outside the terminal**: IDE plugins, a desktop app, daemon mode, SDKs, and IM bots for Telegram, DingTalk, WeChat, and Feishu — the same messaging-surface pattern this map recorded for [WorkBuddy](workbuddy.md) and [ZCode](zcode.md).
- You want the whole stack open — Apache-2.0 client, open-weights models — for audit or air-gapped deployment.

## When Not To Pick It

- You want the largest ecosystem. At 27.7k stars it is an order of magnitude below [OpenCode](opencode.md) and [Gemini CLI](gemini-cli.md); fewer third-party integrations target it.
- **The self-iterating development model matters to you.** The project states it uses its own agent and models to file issues, submit PRs, review code, and run tests. That is an interesting claim about agent maturity and a governance question about review depth — decide which reading you hold before adopting it.
- You want a vendor-neutral project rather than a vendor's open project — that is [OpenCode](opencode.md).
- Your model commitment is Claude or GPT and you want their tuned defaults.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Model freedom | **Very strong** | Multi-protocol with runtime switching, including local models |
| Openness | Very strong | Apache-2.0 client and open-weights models — unusual as a pair |
| Delivery surfaces | Very strong | Terminal, IDE, desktop, daemon, SDKs, four IM platforms |
| Agentic features | Strong | Auto-Memory, Auto-Skills, SubAgents, Agent Teams, MCP |
| Ecosystem size | Medium | Well behind the leading CLIs on adoption |
| Development governance | Medium | Self-iterating: its own agent files issues, PRs, and reviews |

## Relationship To Qwen3-Coder

[Qwen3-Coder](qwen3-coder.md) is the model, this is the loop. They are released and evolve together, which is the argument for using them as a pair — but the multi-protocol support means you can take the loop without the models, or the models without the loop. On this map that combination is rare enough to be the reason to look at either one.

## Bottom Line

Qwen Code is the answer to "can I have a vendor's CLI without the vendor's gravity". Smaller ecosystem than the leaders, unusual development process, but genuinely open at both layers and portable across providers by design.
