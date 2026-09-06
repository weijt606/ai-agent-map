# Kimi Work

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/kimi-work.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](kimi-work.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Kimi Work is Moonshot's desktop agent for knowledge work — [Kimi Code](kimi-code.md)'s loop pointed at your mounted folders, a browser extension that clicks for you, and a built-in cron engine, with an agent swarm behind it.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Moonshot AI |
| Route | General-purpose autonomous agent (local-first desktop) |
| Open source | No |
| Best for | Recurring knowledge work on local files: research into decks and spreadsheets, scheduled reporting |
| Main cost | Proprietary desktop client; it mounts your folders and drives your logged-in browser |
| Platforms | macOS (Apple Silicon), Windows |
| Public beta | Announced June 3–4 2026 |
| Official page | https://www.kimi.ai/products/kimi-work |

## Why This Entry Exists

This map already profiles [Kimi Code](kimi-code.md), Moonshot's terminal coding agent. Kimi Work is the same vendor taking that loop off the repository and onto the desktop, and the vendor says so directly: **Kimi Code is the core Kimi Work runs on.** That makes it the cleanest example in this directory of a coding-agent loop being re-aimed at general work, which is a selection question — the strengths and the failure modes travel with it.

It also lands in the same window as Tencent's [WorkBuddy](workbuddy.md), which is why this map now records desktop knowledge-work agents as a category rather than as one-offs.

## When To Pick It

- Your work is **local files plus the web**, and you want one agent that can do both: mount folders with your authorization, then navigate, click, scroll, and extract through the Kimi Browser Extension using the sessions you are already logged into.
- You want **things to happen on a schedule**. A built-in cron engine runs tasks around the clock, including LLM agent calls and Python scripts — closer to a standing automation than a chat session.
- Your outputs are **deliverables**: it converts research into PowerPoint and Excel directly.
- The work is **big enough to parallelize** — the agent swarm coordinates specialized sub-agents, reported at up to 300 for complex tasks.
- You work in Chinese-market finance or research: A-share, Hong Kong, and US market data are pre-integrated, and the online Kimi Agent's skills and professional databases (finance, science, law) carry over.

## When Not To Pick It

- **It drives the browser you are already logged into.** That is the feature and the risk in one sentence. Anything you would not want an autonomous loop doing with your live sessions is a reason to scope its access carefully, or not to run it.
- You want to audit the loop. Closed source, with filesystem and browser reach — the opposite governance position from the open harnesses on this map.
- You want a coding agent — that is [Kimi Code](kimi-code.md), and it is the better tool for repositories.
- You need Linux, or a fully non-Moonshot model stack.
- You need a stability guarantee: this is a young product, opened to public beta in June 2026.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Local file work | Very strong | Mounts folders and works inside them with authorization |
| Browser automation | Very strong | Kimi Browser Extension navigates, clicks, scrolls, extracts |
| Scheduling | Very strong | Built-in cron engine; LLM calls and Python scripts as scheduled work |
| Multi-agent | Strong | Agent swarm of specialized sub-agents (reported up to 300) |
| Office artefacts | Strong | Research to slides and spreadsheets |
| Domain data | Strong | Pre-integrated A-share / HK / US equities; inherited finance, science, and law databases |
| Open source / auditability | None | Proprietary |

## Relationship To Kimi Code

Same vendor, same underlying loop, different unit of work. [Kimi Code](kimi-code.md) is a terminal agent whose object is a repository, is tracked on this map's heat boards, and fits the [coding CLI comparison](../comparisons/coding-cli-agents.md). Kimi Work's object is your desktop. If you want one Moonshot agent for engineering, take Kimi Code; the case for Kimi Work is recurring non-code work that has to touch real files and real websites.

## Bottom Line

Kimi Work is the most explicit statement so far that vendors intend the coding-agent loop to be the general work loop. The cron engine and the browser extension are what make it more than a chat window — and they are also exactly what you should scope before letting it run unattended.
