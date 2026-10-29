# Gemini CLI

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/gemini-cli.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](gemini-cli.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Gemini CLI is Google's open-source terminal agent, and it is **no longer Google's free path for individuals**: since June 18 2026 free users and Google AI Pro and Ultra subscribers are served by [Google Antigravity](antigravity.md)'s CLI instead. It remains the Apache-2.0 client for Gemini Code Assist Standard and Enterprise organisations and paid Gemini API keys.

> **Correction (2026-10-30):** this profile led with a consumer free tier that stopped applying on 2026-06-18. Google's quota page now opens with the banner "Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026." Google's developer blog (May 19 2026) says that from that date Gemini CLI stops serving Google AI Pro and Ultra subscribers, free users of Gemini Code Assist for individuals and the Code Assist IDE extensions, while Code Assist Standard and Enterprise organisations and paid Gemini and Gemini Enterprise Agent Platform API keys keep working; Antigravity CLI "is available to everyone". The "60 requests/min" figure is withdrawn too: Google's page gives no per-minute number. Corrected in place below. Sources: [Gemini CLI quota and pricing](https://geminicli.com/docs/resources/quota-and-pricing), [Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/).

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Google |
| Route | Direct execution |
| Repository | [`google-gemini/gemini-cli`](https://github.com/google-gemini/gemini-cli) — Apache-2.0, TypeScript, **109k stars (2026-10-28)** |
| Open source | Yes (Apache-2.0) |
| Best for | Terminal work on Gemini for Code Assist Standard / Enterprise organisations and paid Gemini API key users |
| Main cost | No consumer free path since 2026-06-18; access needs a Code Assist Standard / Enterprise licence or a paid API key, with per-minute and per-day request limits |
| Free tier | **Not for consumers since 2026-06-18.** Google's quota page still lists 1,000 requests/day for Gemini Code Assist for individuals, but those users were moved to Antigravity CLI on 2026-06-18; no per-minute number is published |
| Docs | https://geminicli.com/docs/ |

## Why This Entry Exists

The map had a factual hole. Its own market-events timeline records Meta's Muse Code as "closing the first-party coding-CLI field" in August 2026 — while the field was missing Google's entry the whole time. This map profiles [Claude Code](claude-code.md), [Codex](codex.md), [Grok Build](grok-build.md), [Kimi Code](kimi-code.md), [MiMoCode](mimocode.md) and [Qwen Code](qwen-code.md), records Meta's Muse Code in its timeline, and had no page for the vendor CLI with 109k stars (2026-10-28).

It is also referenced as an integration target inside [CodeGraph](codegraph.md), [Superpowers](superpowers.md), and [oh-my-claudecode](oh-my-claudecode.md) — the same pattern that hid [OpenCode](opencode.md).

## When To Pick It

- **Your organisation already pays for Gemini Code Assist Standard or Enterprise, or you run on a paid Gemini API key.** Those are the access paths Google kept on 2026-06-18. If you are an individual and budget is the constraint, look at [Google Antigravity](antigravity.md) instead.
- You want **Google Search grounding inside the loop** — a built-in tool, not an MCP server you have to wire up. For research-shaped tasks that is a genuine differentiator against every other CLI here.
- You want **Gemini 3 with a 1M-token context** in your terminal, with the vendor's own tuning.
- You want a permissive licence on the client: Apache-2.0, unlike the proprietary first-party CLIs on this route.
- You want MCP support and a terminal-first design without adopting a whole IDE.

## When Not To Pick It

- Your model commitment is elsewhere. The tool exists to run Gemini; if you are on Claude or GPT, their own CLIs are better tuned — see the [coding CLI comparison](../comparisons/coding-cli-agents.md).
- **You need predictable throughput.** Per-minute and per-day request caps are a rate limit in the middle of your agent loop; budget for the paid path before you depend on it.
- You want a vendor-neutral loop — that is [OpenCode](opencode.md).
- You need on-premises or offline operation.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Cost of entry | Weak for individuals | Free and Google One users were moved to Antigravity CLI on 2026-06-18; access now needs a Code Assist Standard / Enterprise licence or a paid API key |
| Search grounding | Very strong | Google Search is a built-in tool, not an add-on |
| Long context | Very strong | Gemini 3, 1M-token context window |
| Extensibility | Strong | MCP support for custom integrations |
| Licence | Strong | Apache-2.0 on the client |
| Throughput predictability | Medium | Requests are limited per minute and per day |
| Model freedom | Weak | It is Google's CLI for Google's models |

## Relationship To Google's Other Agent Surfaces

Google appears in this map at three points that are easy to confuse. [Jules](jules.md) is the managed background agent; [Google Antigravity](antigravity.md) is Google's agent-first platform (app, IDE, editor extensions and the `agy` CLI), and since 2026-06-18 the place Google sends free and Google One users who used to run Gemini CLI; Gemini CLI is the terminal loop you drive yourself. If you want a task queue, take Jules. If you want to sit in the loop, take this.

## Bottom Line

The free tier was the headline until 2026-06-18, when Google moved free individual users and Google AI Pro and Ultra subscribers to [Google Antigravity](antigravity.md)'s CLI; if that is you, start there. Gemini CLI remains the Apache-2.0 terminal agent for Code Assist Standard and Enterprise organisations and paid Gemini API keys. Weigh the rate limits before you build automation on it, and treat the model lock-in as the price of the tuning.
