# Consumer Personal Agents

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/comparisons/personal-agents.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](personal-agents.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

Agents you hand your day to — errands, inboxes, bookings, documents, your phone — sold as consumer products rather than run as software. None of them is open source (one has an open-source sibling). This page collects them, compares them on facts and control rather than popularity, and logs what changes.

> **Last reviewed:** 2026-10-28 · Every fact below comes from the vendor's own page, help center or app-store listing unless it is marked *media*. A cell reading **?** means the vendor does not document it first-hand — not that the product lacks it.

## Why There Is No Popularity Ranking Here

The rest of this map ranks open-source projects by GitHub stars, a public number anyone can check. Closed consumer products have no equivalent: downloads, monthly users and app-store ranks are reported second-hand, on different definitions, if at all. A ranked list built on them would look precise and be made up. So this page **lists and compares** instead, and the "Recent changes" log at the bottom is where movement shows up.

For self-hosted personal agents you run yourself — [Hermes Agent](../agents/hermes-agent.md), [OpenClaw](../agents/openclaw.md), [OpenHuman](../agents/openhuman.md), [Goose](../agents/goose.md) — and the desktop knowledge-work agents [Kimi Work](../agents/kimi-work.md) and [WorkBuddy](../agents/workbuddy.md), see the [capability matrix](../capabilities/matrix.md) and the heat ranking.

## The Field At A Glance

| Agent | Vendor | Form | Status (date) | Where it works | Model | Entry price | Regions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ChatGPT dots](../agents/chatgpt-dots.md) | OpenAI | ChatGPT apps; Slack, Teams, calls | Rolling out (Sept 29 2026) | Own cloud computer + browser; one connected PC | GPT-6 Astra | Pro, $100/mo | Not EEA, UK, CH |
| [Gemini Task](../agents/gemini-task.md) | Google | Chat/Task toggle in the Gemini app | Shipping, ex-"Spark" (May 19 2026) | Remote browser/computer; your Chrome | Gemini 3.5 + Antigravity harness | AI Pro, $19.99/mo (US) | Not EEA, UK, CH, Nigeria |
| [Claude (Cowork)](../agents/claude-cowork.md) | Anthropic | The Claude app; Claude in Chrome | Merged into Claude (Sept 16 2026) | Isolated cloud session; your computer; Chrome | Anthropic's current models | Pro, $20/mo | ? |
| [Muse](../agents/meta-muse.md) | Meta | App, web, WhatsApp | Limited testing, US (Sept 8 2026) | Dedicated cloud VM with browser | Muse Spark | Free; Power $20/mo | US |
| [Grok Bot](../agents/grok-bot.md) | xAI | Desktop + mobile apps; `@bot` on X | Beta (Aug 11 2026) | One shared cloud computer in Cursor's cloud, US | Chosen by Cursor | X Premium, $30/mo | Compute in US |
| [Cue](../agents/manus-cue.md) | Manus | Web, desktop, mobile app | Early access, invite only | Own computer per agent | ? | Free in early access (Plus included) | ? |
| [Doubao](../agents/doubao.md) | ByteDance | App; system service on partner phones | Shipping; phone control Beta (Sept 14 2026, *media*) | ByteDance service; **your phone's OS** | Doubao models | Free; paid tiers from ¥68/mo | China |
| [Qwen app](../agents/qwen-app.md) | Alibaba | App | Shipping | Alibaba service and partner services | Qwen | Free + subscriptions | China |
| [AutoGLM](../agents/autoglm.md) | Zhipu | App; open-source framework | App last updated July 9 2026 | Cloud phone + cloud PC; or your phone via ADB/HDC | AutoGLM-Phone-9B | Free | China (app) |
| [Yuanbao](../agents/yuanbao.md) | Tencent | App | Agent feature since July 6 2026 | Tencent service | Hy3 | Free | China |

## Capability Grid

Same legend as the [capability matrix](../capabilities/matrix.md): ● core strength · ◐ solid support · ○ limited · — not a goal · **?** not documented first-hand.

| Agent | Web errands | Deliverables | Scheduling | Your device | Memory | Multi-agent | Approval controls | Run it yourself |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [ChatGPT dots](../agents/chatgpt-dots.md) | ● | ● | ● | ◐ | ● | ● | ● | — |
| [Gemini Task](../agents/gemini-task.md) | ● | ◐ | ● | ◐ | ◐ | ○ | ● | — |
| [Claude (Cowork)](../agents/claude-cowork.md) | ◐ | ● | ● | ◐ | ● | ? | ● | — |
| [Muse](../agents/meta-muse.md) | ● | ? | ? | ○ | ● | ? | ● | — |
| [Grok Bot](../agents/grok-bot.md) | ● | ◐ | ● | ○ | ● | ● | ◐ | — |
| [Cue](../agents/manus-cue.md) | ● | ? | ◐ | ○ | ◐ | ● | ◐ | — |
| [Doubao](../agents/doubao.md) | ◐ | ● | ● | ● | ? | ? | ◐ | — |
| [Qwen app](../agents/qwen-app.md) | ● | ● | ● | ○ | ? | ? | ? | — |
| [AutoGLM](../agents/autoglm.md) | ● | ○ | ? | ● | ? | ? | ? | ● |
| [Yuanbao](../agents/yuanbao.md) | ○ | ● | ? | — | ? | ? | ? | — |

How the hard cells were scored: **Your device** is ● only where the agent operates apps on a phone you hold (Doubao's system service; AutoGLM's open framework), ◐ where it can use your computer or browser, ○ where it works only on a vendor machine. **Approval controls** is ● where the vendor documents per-action confirmation rules or scoped grants (dots' automatic review and custom rules, Gemini's confirmation list, Claude's three modes, Muse's Sentinel), ◐ where control exists but is partial or coarse (Grok Bot's Auto Review does not cover every side effect; Cue's budget; Doubao's app-level SAEP declarations).

## Three Questions That Decide Most Choices

1. **Whose identity does it act under?** Almost every agent here signs in as you. [Cue](../agents/manus-cue.md) gives each agent its own email, phone number and wallet — less exposure for your accounts, more for the people it contacts.
2. **Whose machine does it work on?** A vendor cloud computer (dots, Muse, Grok Bot, Cue, AutoGLM's app), your browser or computer (Gemini, Claude, dots' connected PC), or your phone's operating system (Doubao). The closer to your device, the larger the permission you are granting.
3. **Can the vendor see it, and does it train on it?** Muse's operator can still reach your data until its announced Confidential VM ships; Claude's training is an opt-in choice with 5-year vs 30-day retention; Grok Bot excludes training only under Privacy Mode; Gemini Task requires Keep Activity on. Several products do not state this at all — treat that as an answer.

## Recent Changes

Newest first. This log is refreshed with the weekly update; dated entries are not rewritten.

- **2026-10-28** — **Anthropic released Claude Duet on Oct 21**, a separate app in which Claude "works as a proactive agent": research preview by waitlist, starting with US Pro and Max subscribers, built around Claude Opus 5.5, running on "a virtual machine with its own browser" so your laptop or phone need not be on, and waiting for approval before it sends a message, pays, signs a document or deletes anything; trading securities and moving money are off-limits even with approval. Anthropic says "for now" it lives apart from the main Claude app, which qualifies the [Claude (Cowork)](../agents/claude-cowork.md) row: Anthropic now has two consumer agent surfaces. It reached the US App Store on Oct 26 and is a profile candidate (see Watchlist). **Cue**'s App Store description now documents scheduled and event-triggered automations, a memory feature ("Memory and Dream"), payments you confirm, and Plus membership included at no charge during access; the Scheduling and Memory cells move from **?** to ◐. **Doubao**'s App Store listing states its tiers (free basic; ¥68, ¥200 and ¥500 a month); v15.5.0 (Oct 26) repeats v15.4.0's notes. **Muse** v13.1 (Oct 24) made shopping in chat easier. No first-hand change for dots, Gemini Task, Grok Bot, AutoGLM or Yuanbao, and Qwen Go! is still media-only.
- **2026-10-21** — Page created with ten agents. Recorded along the way: Grok Bot moved into the X Subscription on Oct 12 (Premium $30, Super $100, Ultra $200); Qwen Go! was reported by media on Oct 13 as a waitlist feature inside the Qwen app (not yet first-party confirmed); Muse Wonder (Oct 12) is announced to power Muse "soon", subscribers first; Doubao app v15.4.0 (Oct 19) added work-task mode and a shopping assistant.

## Watchlist

Candidates not yet profiled: the **Kimi app**'s agent swarm (the consumer front end of [Kimi Work](../agents/kimi-work.md)); **Baidu Wenxin**'s task-hosting mode; **StepFun**'s Step Agent; **MiniMax Agent** (a new "M Plan" subscription in its v4.22.2 app, Oct 22); **Claude Duet** (Anthropic, Oct 21, see above); Ant Group's **Lingguang** (v1.3.80, Oct 26, "灵光2.0", pitched as a personal assistant that "manages things"). Phone-maker system agents (Honor, vivo, Huawei) have so far surfaced only in media round-ups.
