# Gemini CLI

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/gemini-cli.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](gemini-cli.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Gemini CLI is Google's open-source terminal agent, and the only first-party coding CLI on this map with a **free tier you can do real work on** — 1,000 requests a day on a personal Google account.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Google |
| Route | Direct execution |
| Repository | [`google-gemini/gemini-cli`](https://github.com/google-gemini/gemini-cli) — Apache-2.0, TypeScript, **107k stars** |
| Open source | Yes (Apache-2.0) |
| Best for | Terminal work on Gemini, and anyone who needs a capable agent at zero cost |
| Main cost | Free tier has rate limits; heavier use moves you onto paid Google plans |
| Free tier | **60 requests/min, 1,000 requests/day** with a personal Google account |
| Docs | https://geminicli.com/docs/ |

## Why This Entry Exists

The map had a factual hole. Its own market-events timeline records Meta's Muse Code as "closing the first-party coding-CLI field" in August 2026 — while the field was missing Google's entry the whole time. This map profiles [Claude Code](claude-code.md), [Codex](codex.md), [Grok Build](grok-build.md), [Kimi Code](kimi-code.md), [MiMoCode](mimocode.md), and [CodeWhale](codewhale.md), and had no page for the vendor CLI with 107k stars.

It is also referenced as an integration target inside [CodeGraph](codegraph.md), [Superpowers](superpowers.md), and [oh-my-claudecode](oh-my-claudecode.md) — the same pattern that hid [OpenCode](opencode.md).

## When To Pick It

- **Budget is the constraint.** 1,000 requests/day free with a personal account is not a trial; it is enough for daily work, and nothing else in this route offers it.
- You want **Google Search grounding inside the loop** — a built-in tool, not an MCP server you have to wire up. For research-shaped tasks that is a genuine differentiator against every other CLI here.
- You want **Gemini 3 with a 1M-token context** in your terminal, with the vendor's own tuning.
- You want a permissive licence on the client: Apache-2.0, unlike the proprietary first-party CLIs on this route.
- You want MCP support and a terminal-first design without adopting a whole IDE.

## When Not To Pick It

- Your model commitment is elsewhere. The tool exists to run Gemini; if you are on Claude or GPT, their own CLIs are better tuned — see the [coding CLI comparison](../comparisons/coding-cli-agents.md).
- **You need predictable throughput.** A free tier with per-minute and per-day caps is a rate limit in the middle of your agent loop; budget for the paid path before you depend on it.
- You want a vendor-neutral loop — that is [OpenCode](opencode.md).
- You need on-premises or offline operation.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Cost of entry | **Very strong** | The most generous free tier in this route by a distance |
| Search grounding | Very strong | Google Search is a built-in tool, not an add-on |
| Long context | Very strong | Gemini 3, 1M-token context window |
| Extensibility | Strong | MCP support for custom integrations |
| Licence | Strong | Apache-2.0 on the client |
| Throughput predictability | Medium | Free tier is rate-limited by minute and by day |
| Model freedom | Weak | It is Google's CLI for Google's models |

## Relationship To Google's Other Agent Surfaces

Google appears in this map at three points that are easy to confuse. [Jules](jules.md) is the managed background agent; **Antigravity** is Google's agent-first IDE, referenced by [CodeGraph](codegraph.md) and [Omnigent](omnigent.md) as an integration target but not yet profiled here; Gemini CLI is the terminal loop you drive yourself. If you want a task queue, take Jules. If you want to sit in the loop, take this.

## Bottom Line

The free tier is the headline and it is not a gimmick — for individual developers and for anyone evaluating agents without a budget line, this is the lowest-friction serious agent on the map. Weigh the rate limits before you build automation on it, and treat the model lock-in as the price of the tuning.
