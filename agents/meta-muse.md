# Muse (Meta)

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/meta-muse.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](meta-muse.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Muse is Meta's consumer personal agent — you message it in its own app or in WhatsApp, and it does the errand on a dedicated cloud VM with its own browser, paying through a one-time card number — with a detailed published security design and a privacy mode that has been announced but not shipped.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Meta |
| Route | Consumer personal agent |
| Open source | No |
| Form factor | iOS and Android apps, the muse.ai web app, and WhatsApp; AI glasses "coming soon" |
| Status | Announced **Sept 8 2026**, "rolling out in the US"; Meta's help center says Muse and its subscriptions are "in limited testing" |
| Where it runs | **Muse Secure VM** — a dedicated cloud computer per person, with its own browser |
| Model | **Muse Spark**; Meta says [Muse Wonder](../market-events.md) will "soon power experiences in Muse", subscribers first |
| Price | Free with a usage limit; **Power $20/month** (500M Muse tokens a week), **Maximum $100/month** (3B a week) |
| Official page | https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ |

Not to be confused with Meta's Muse *models* (Muse Spark, Muse Wonder), which this map tracks in [cost & benchmarks](../comparisons/cost-and-benchmarks.md), or with Muse Code, Meta's coding agent.

## When To Pick It

- You want an agent for **life errands** — forms, bookings, bills, purchases — and you would rather message it like a person, including from WhatsApp.
- You want purchases handled without handing over your card: checkout runs through **Link by Stripe**, which issues a one-time card number, and Meta says Muse is the first agent covered by Link's purchase protections.
- You want a vendor that has published how the agent is contained, not only what it can do.

## When Not To Pick It

- You are outside the US, or not in the limited test.
- You need the vendor to be unable to see your data. Today's architecture "does not prevent Meta from accessing data when necessary to support, secure or operate the service"; **Muse Confidential VM**, encrypted with a key only you hold, is announced for "later this year" and has not shipped.
- You need your existing logins. 1Password support and Shop Pay are both "coming soon".

## Permissions And Data

A host-side **Sentinel**, which the agent cannot override, is "the sole permission authority for connector actions and network egress"; the agent never sees real credentials. Grants can be one-time, session-, task- or time-bounded, or perpetual. Muse remembers what you tell it and makes unprompted suggestions; you can tell it to "forget" specific things. Meta runs a bug bounty of up to $300,000, including for successful prompt injections. The help center page this map read states prices and limits but says nothing about whether conversations train models.

## Bottom Line

An errand agent with a published containment design — and, until Confidential VM ships, one whose operator can still reach your data. Read it as a strong US-only preview, not a finished privacy story.

## Sources

- [Introducing Muse (Meta, Sept 8 2026, updated Sept 30)](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)
- [Security and safety for AI agents: our approach with Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)
- [Muse subscriptions (Meta help center)](https://www.meta.com/help/subscriptions/1021145227643680/) · [Muse Wonder](https://research.meta.ai/blog/muse-wonder)
