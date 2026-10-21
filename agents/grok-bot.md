# Grok Bot

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/grok-bot.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](grok-bot.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Grok Bot is xAI's team of always-on agents — several named Bots share one cloud computer, sign into your tools, keep their own memory and rerun saved skills on a schedule — sold inside the X Subscription and run on Cursor's infrastructure.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | xAI (with Cursor running the compute) |
| Route | Consumer personal agent |
| Open source | No |
| Form factor | Desktop app (macOS, Windows, Linux), mobile app (iPhone, iPad, Android); tag `@bot` on X, not in every region yet |
| Status | Beta since **Aug 11 2026**; an enterprise offering followed on Sept 3 |
| Where it runs | **One cloud computer shared by all your Bots** (files, browser sessions, app logins), **in Cursor's cloud**, located **in the United States** |
| Model | Not chosen by you — "Cursor manages model selection", with no model picker |
| Price | Since Oct 12 2026, included in the X Subscription on **Premium ($30/month), Super ($100/month) and Ultra ($200/month)**, not on Plus ($8) |
| Official page | https://x.ai/news/introducing-grok-bot |

## Why This Entry Exists

It is built as "agents as teammates": several named Bots that share one computer, message each other, coordinate in group chats and pass ownership of a task. It also shows how far the vendor boundary has blurred — an xAI product whose computers and model routing belong to Cursor, which this map profiles separately as an [editor](cursor.md).

## When To Pick It

- You want **several standing agents with separate jobs** (outbound, campaigns, operations) rather than one assistant, and you want them to coordinate in shared chats.
- The work spans tools that have no API: a Bot uses connectors where they exist and the browser where they do not, and you can **walk it through a path once** and have it save that as a skill to rerun on a schedule.
- You already pay for SuperGrok, Cursor or X Premium and want the agent inside the same bill and usage pool.

## When Not To Pick It

- You need to know or choose the model. The serving mix is Cursor's and "can change over time".
- You need data outside the US, or a written residency commitment without talking to sales.
- You want every side effect reviewed. Its "Auto Review" model checks risky actions but, by xAI's own documentation, does not review every side effect.

## Permissions And Data

A Bot acts as the signed-in member, with no credentials of its own. Actions that need approval show the proposed operation and its inputs, with **Allow once**, **Always allow** (saves a matching rule) or **Deny**. Training: "with Privacy Mode enabled, customer data is not used for training" — the promise is tied to Privacy Mode, not unconditional.

## Bottom Line

A personal agent built as a staff — many Bots, a real shared computer, scheduled skills — that does not let you see or choose the model doing the work. Pick it for breadth of delegation; turn Privacy Mode on and scope approvals before you hand it live accounts.

## Sources

- [Introducing Grok Bot (Aug 11 2026)](https://x.ai/news/introducing-grok-bot) · [Grok Bot for Enterprise (Sept 3 2026)](https://x.ai/news/grok-bot-for-enterprise) · [Introducing The X Subscription (Oct 12 2026)](https://x.ai/news/x-subscription)
- [Grok Bot overview](https://docs.x.ai/grok-bot/overview) · [Approvals, security, and privacy](https://docs.x.ai/grok-bot/security) · [Grok Bot on The X Subscription](https://docs.x.ai/x-subscription/grok-bot)
