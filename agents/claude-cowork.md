# Claude (Cowork)

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/claude-cowork.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](claude-cowork.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Anthropic's personal agent is no longer a separate product — **Cowork merged into the Claude app on Sept 16 2026**, so the same Claude that chats now takes a task, schedules it, keeps working in an isolated cloud session after you close your laptop, and drives Chrome through Claude in Chrome — with three named approval modes you pick per task.

> **Update, Oct 28 2026:** Cowork is no longer Anthropic's *only* consumer agent. On Oct 21 Anthropic opened a waitlisted research preview of **[Claude Duet](claude-duet.md)**, a separate app (US Pro and Max first) in which Claude works as a proactive agent on its own virtual machine with a browser, built around Opus 5.5, asking approval before it sends, pays, signs or deletes. Anthropic says it lives apart from the main Claude app "for now". See the [personal agents](../comparisons/personal-agents.md#recent-changes) log.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anthropic |
| Route | Consumer personal agent |
| Open source | No |
| Form factor | The Claude app on desktop (macOS, Windows), web and mobile; **Claude in Chrome** extension for browser actions |
| Status | Cowork GA on desktop **Apr 9 2026**; web and mobile with remote sessions (beta) **July 7**; Claude in Chrome GA on every paid plan **Aug 26**; Cowork and chat merged **Sept 16**, rolling out to Pro and Max first, Team and Free later |
| Where it runs | Cloud tasks run "in an isolated, temporary environment on Anthropic's servers", created for that session; computer use on your own machine is also available |
| Model | Anthropic's current models (see [Opus 5](claude-opus-5.md), [cost & benchmarks](../comparisons/cost-and-benchmarks.md)) |
| Price | **Pro $20/month** ($17/month billed annually); **Max from $100/month** |
| Official page | https://claude.com/resources/articles/cowork-is-now-claude |

The map profiles Anthropic's coding agent ([Claude Code](claude-code.md)) and its developer-hosted agents ([Claude Managed Agents](claude-managed-agents.md)) separately. Claude Tag (Claude in Slack) is a Team and Enterprise product, so it is not covered here.

## When To Pick It

- You want **one app** for asking and delegating: no switch between a chat product and an agent product.
- You want work to **continue after you close the laptop**, and to recur on a schedule.
- You want to choose how much the agent may do on its own, per task.

## When Not To Pick It

- You are on Team or Free and need it now: the merged experience reaches Pro and Max first.
- You want the agent to be contained when it uses your own computer. Anthropic says plainly that computer use "has no sandbox between Claude and what's on your screen".
- You want it to run in other Chromium browsers or on mobile browsers: Claude in Chrome does not.

## Permissions And Data

Three approval modes: **Manually approve**, **Automatically approve** (Claude still reviews each action for safety before it runs) and **Skip all approvals** (nothing checks its actions). In every mode it asks before permanently deleting files. Anthropic recommends manual approval for sensitive files, new tools and anything hard to undo, such as sending messages or making purchases. In Chrome, a safety classifier validates each action before it runs. Memory works across chat and Cowork (since Aug 25 2026), is listed item by item under Settings → Memory where you can edit or delete it, keeps topics such as health or beliefs out unless you turn on sensitive topics, and is on by default for Free, Pro and Max. Training on consumer plans is your choice: if you allow it, data is retained for five years; if not, the 30-day retention period continues.

## Bottom Line

An agent folded into the default app rather than sold as a separate product, with three explicit modes for the axis that matters most: how much it may do without asking. Pick a mode deliberately; "Skip all approvals" means exactly that.

## Sources

- [Claude Cowork and chat merge into one Claude (Sept 16 2026)](https://claude.com/resources/articles/cowork-is-now-claude) · [Claude in Chrome is generally available (Aug 26 2026)](https://claude.com/resources/articles/claude-in-chrome-generally-available)
- [Claude release notes](https://support.claude.com/en/articles/12138966-release-notes) · [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Claude pricing](https://claude.com/pricing) · [Updates to consumer terms](https://www.anthropic.com/news/updates-to-our-consumer-terms)
