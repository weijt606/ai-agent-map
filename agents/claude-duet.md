# Claude Duet

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/claude-duet.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](claude-duet.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Anthropic's second consumer agent, and the one that comes to you first. A separate app built around Opus 5.5 that briefs you each morning, checks your connected accounts every few hours, works on its own virtual machine while your devices are off, and waits for your okay before it sends, pays, signs or deletes anything. It is aimed at professionals and small business owners, not personal errands.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anthropic |
| Route | Consumer personal agent |
| Open source | No |
| Form factor | A **standalone app** on iOS and Android, and on claude.ai; "for now" separate from the main Claude app |
| Status | **Research preview by waitlist since Oct 21 2026**, starting with US Pro and Max subscribers; iOS app listed Oct 26 |
| Where it runs | "A virtual machine with its own browser", so it "doesn't require your laptop or phone to be on" |
| Model | Designed around **Claude Opus 5.5** ([cost & benchmarks](../comparisons/cost-and-benchmarks.md)) |
| Price | Included in **Pro** and **Max** during the preview, sharing the plan's usage limits; its background checks count against them |
| Regions | US first |
| Official page | https://claude.com/resources/articles/claude-duet |

## How It Differs From Claude (Cowork)

[Claude (Cowork)](claude-cowork.md) is the Claude app taking a task you hand it. Duet is a separate app that **starts the conversation**: a short morning brief on what needs a decision across your email and calendar, then a check of your connected accounts "every few hours" with a message only when something needs you. You can say what you want to hear about and how often. It carries over your Claude memory, skills and connected apps, and it keeps everything in one ongoing thread, with optional channels per area of work (finance, hiring). Anthropic says what it learns from early users "will shape how the two work together".

## When To Pick It

- You run a small business or a busy practice and want something that **watches** your inbox, calendar and business tools and raises what matters, rather than waiting for a prompt.
- Your work lives in tools it can reach through the Claude Marketplace: Gmail, Slack, QuickBooks, Stripe, Gusto, Docusign, HubSpot, Canva, Shopify.
- You are already on Pro or Max in the US and can get through the waitlist.

## When Not To Pick It

- You want an errand runner. Anthropic says personal errands "such as booking tickets" are weaker, and it "can't yet show you its browser".
- You need real-time alerts. Because it checks every few hours, "something urgent can arrive between checks".
- You are outside the US, or not on a paid plan.

## Permissions And Data

Duet "reads, drafts, and prepares work on its own", but before it sends a message, makes a payment, signs a document or deletes anything, it shows you exactly what it will do and waits for approval. **Trading securities and moving money between accounts are off-limits even with approval.** Actions pass Anthropic's auto mode classifier. Credentials follow the Claude Managed Agents design, so Duet "never directly sees your passwords or sign-in tokens". A dedicated classifier rejects requests to share the strictest tier of information, such as card numbers and government IDs; health and finance details go out only on explicit instruction. Purchases go through Stripe's Link, which asks you to approve the spend and pays with a virtual card; Shop Pay works at online stores, and 1Password sign-in is "coming soon". The pages this map read do not state training terms specific to Duet.

## Bottom Line

An agent designed to interrupt you selectively, with a written list of actions it will not take even when you approve them. It is a preview: waitlisted, US only, and still tuning its judgment about when to interrupt you. For a US small-business owner already paying for Claude, it is worth joining the waitlist. Everyone else should wait for it to merge with, or graduate from, the main app.

## Sources

- [Introducing Claude Duet (Oct 21 2026, updated Oct 23)](https://claude.com/resources/articles/claude-duet) · [Claude release notes](https://support.claude.com/en/articles/12138966-release-notes) · [Claude Duet on the App Store](https://apps.apple.com/us/app/id6803276000)
