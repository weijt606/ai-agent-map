# Pi

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/pi.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](pi.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Pi is a minimal, opinionated coding-agent harness — the agent loop, tools, and providers, with everything else left to extensions.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | earendil-works (acquired April 8 2026 from Mario Zechner / badlogic) |
| Route | Self-hostable terminal coding agent + agent toolkit |
| Open source | Yes (MIT, TypeScript) |
| Best for | Developers who want to keep the harness small and own the orchestration choices themselves |
| Main cost | You bring your own API keys, your own skills, and your own opinions about how to extend the agent |
| Official website | https://lefos.ai/ |
| GitHub repo | https://github.com/earendil-works/pi |

## When To Pick It

- You want a coding agent CLI that ships only the core loop (read, write, edit, bash) and lets you grow it with skills and extensions.
- You want broad LLM provider support — OpenAI, Anthropic, Google, vLLM pods — without lock-in to one vendor's surface.
- You want to publish your work sessions back to Hugging Face as open training data, which the project actively encourages.

## When Not To Pick It

- You want a turnkey product with bundled teams, dashboards, and managed background runs out of the box.
- You don't want to think about which extensions and skills to wire in.
- You need a polished editor surface; Pi is terminal-first.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Terminal workflow | Very strong | The CLI is the primary surface |
| Provider coverage | Very strong | Unified LLM API across OpenAI, Anthropic, Google, vLLM |
| Tool harness | Strong | Read, write, edit, bash by default; extend via skills, prompt templates, packages |
| Orchestration out of the box | Light by design | The point is to leave orchestration to the caller |
| Channels (Slack, web UI) | Available as toolkit packages | TUI, web UI, and Slack bot ship as separate packages |

## Operating Cost

Complexity is Medium. Installation is straightforward, but Pi assumes you will pick the model, wire in the skills, and decide how the agent extends itself. The "harness rebellion" framing is intentional: less bundled, more your call.

## Bottom Line

Pi sits in the same category as Aider and Claude Code — terminal-first coding agent — but stays smaller on purpose. The April 8 2026 acquisition by Earendil (now also building the Lefos cloud agent platform) put real funding behind a previously solo project, and weekly star growth jumped after that. Worth a look if you want to own the harness instead of renting it.
