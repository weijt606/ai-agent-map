# Today

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/today-ai.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](today-ai.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: a personal AI assistant built around "remembers you and helps before you ask", shipped as a China edition (todayai.cn) and an international edition (today.ai). Memory, morning and evening briefings and scheduled tasks sit at the center. Tasks run on the vendor's cloud computers, and with a Chrome extension it can also click and fill forms in your own signed-in browser. Key steps such as submitting a form, placing an order or paying are left for you to confirm or take over. Both editions state that identifiable user content is not used to train public foundation models.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | China edition: **汇翮（上海）智能科技有限公司 (Huihe Intelligent Technology, Shanghai)**, the operator named in its privacy policy and user agreement; international edition: **Today AI PTE. LTD.**, the App Store seller, with terms governed by Singapore law. Founder Qi Junyuan (*media*) |
| Route | Consumer personal agent |
| Open source | No |
| Form factor | Desktop: Mac (Apple silicon / Intel, macOS 14+), Windows (x64 / ARM64), Linux (x64 / ARM64, AppImage); iOS; Android (APK direct from the China site, Google Play internationally); web; a Chrome extension per edition |
| Status | Live. First release dates recorded by the App Store: international 2026-08-27, China 2026-10-04; China iOS is on 1.24.0 (2026-10-30). Media report the China launch on Sept 24–25 (*media*) |
| Where it runs | Its own "stable computers in the cloud" that "can open browsers, work with files, run code", labelled "24 Hours Available"; with the extension installed, also **your Chrome**, where it reads pages, clicks and fills forms |
| Model | China edition: inference through **Alibaba Cloud Bailian, Tencent Cloud TokenHub and Kingsoft Cloud**, which serve "DeepSeek and other models"; speech through Alibaba Cloud DashScope. International: AI providers "may include" AWS, Anthropic and OpenAI. Neither names the model in use |
| Price | China edition: the **basic plan is free "permanently"**, and new users get "300 million tokens and 3 months of Pro" (todayai.cn, read 2026-10-31); the China Pro price is not listed. International App Store in-app purchases: **Pro $20/mo, Ultra $200/mo**; eligible accounts may get a 7-day Pro trial, Ultra has none |
| Regions | Mainland China (China edition, mainland phone-number accounts) plus an international edition |
| Official page | https://todayai.cn · https://today.ai/?international=1 |

## What It Is

Today calls itself a personal assistant "that actually knows you — and acts before you ask". Three threads:

- **Memory**: "a living memory system that keeps your days, your people, your preferences, and the goals you keep coming back to in context, with you in control". The China App Store description says you can view, edit or delete what it remembers.
- **Proactive**: morning and evening briefings built from what you share and authorize, follow-ups on unfinished items, and reminders or suggested next steps "at the right time". The site shows recurring jobs such as "Email triage, every 2h" and "Weekdays at 9:00"; the App Store descriptions say scheduled tasks can run when you need them.
- **Execution**: it can "plan the work, use tools, check progress, and report back", with several tasks running in the background while you do something else. Connectors cover "calendar, mail, notes, and files to messaging, project tools" (site); the China App Store lists email, calendar, documents, reading, office platforms and fitness services. Community Skills run inside Today. Besides the app, you can reach it "through supported messaging channels".

The mobile tab bar is Chat, Today, Memories, Tasks, plus a fifth tab called Spark in the China edition and Capabilities internationally.

## When To Pick It

- You want an assistant centered on **memory and proactive nudges**, not a chat app that waits for you, and you want health data (HealthKit / Health Connect), calendar and mail folded into the same briefing.
- You move between many devices: it ships three desktop apps (Mac, Windows, Linux), two phone apps (iOS, Android) and the web.
- You want it to work in **sites you are already signed in to**: with the Chrome extension it reads your open tabs, clicks, types and fills forms, and can search your history and bookmarks.

## When Not To Pick It

- You need written approval rules. It says only that "key steps" such as submitting forms, ordering and paying are yours to confirm or take over, and that sending or modifying things externally is confirmed "per feature"; there is no published per-action rule set or off-limits list.
- You want to know what China-edition Pro costs first. Neither the site nor the China App Store page lists it.
- You are choosing by specific connector. The site lists categories only, with no public connector list; media lists disagree with each other.

## Permissions And Data

**Training.** China privacy policy (updated and effective 2026-10-25): "unless we clearly state otherwise and obtain your consent as required by law, we will not use user content that can identify you to train public-facing foundation models"; anonymized data may be used for security, reliability and quality analysis. International privacy policy (updated 2026-08-31): AI providers are not permitted to use your identifiable chat content, attachments or health data to train their public foundation models.

**Where data lives.** China edition: personal information is "in principle stored within mainland China"; real-time voice conversation "may use Alibaba Cloud's real-time voice model service located in Singapore", which needs your separate consent first. Before anything is sent to a third-party AI provider, the app shows what is sent, to whom and why, and asks for explicit consent; decline and the AI features that depend on it stop working. Internationally, data may be processed outside your country.

**Retention.** China edition: user content is kept "until you delete it, close your account, or the purpose is fulfilled". International: AI content is kept as account history you can view and delete; deleting the account in the app removes chat history, memories, tasks and data synced from connected apps.

**Device permissions.** On Android, the China edition can, with your item-by-item consent, read SMS, read and write contacts and calendars, read and clear other apps' notifications, read app usage time and access all files. The Chrome extension sends page content, screenshots, URLs and relevant history or bookmark results to Today for processing; disconnecting it "does not automatically delete data already sent".

**Approvals.** China App Store description: "You can watch the process and take over or stop at any time. For key steps such as submitting forms, placing orders or paying, you confirm or finish them yourself." The extension listing suggests stating boundaries in the task, e.g. "fill in this sign-up form, but don't submit it yet".

## Bottom Line

A personal assistant with memory, briefings and scheduled tasks at its center, usable on desktop, phone and web, and specific about training and storage: no training of public foundation models on identifiable content, and China-edition data kept in mainland China in principle. The weak side is the control surface: approvals are written only as "you confirm key steps", connectors have no public list, and the China Pro price is not stated. Worth trying on the free plan plus the new-user allowance if you want a proactive assistant with data kept in mainland China; before you let it pay or send on your behalf, check in the app exactly where it stops to ask.

## Sources

- [todayai.cn](https://todayai.cn/) · [International today.ai](https://today.ai/?international=1) · [China downloads](https://todayai.cn/downloads) · [International downloads](https://today.ai/downloads)
- [China privacy policy (2026-10-25)](https://todayai.cn/privacy) · [China user agreement](https://todayai.cn/terms) · [International Privacy Policy (2026-08-31)](https://today.ai/privacy) · [International Terms of Service (effective 2026-09-07)](https://today.ai/terms)
- [Today on the China App Store](https://apps.apple.com/cn/app/id6775764827) · [Today on the US App Store (in-app prices)](https://apps.apple.com/us/app/id6760608312) · [Google Play](https://play.google.com/store/apps/details?id=ai.today.android.app) · [Chrome extension "Today AI 中国版"](https://chromewebstore.google.com/detail/edkhmdfegifiidpkfifcoiafjgbopggj) · [Chrome extension "Today AI"](https://chromewebstore.google.com/detail/today-ai/adhckffghihcelhbpgbkbepmlhcmofjc)
- *Media*: [QbitAI, 2026-09-24](https://finance.sina.cn/2026-09-24/detail-inisxnuz4997238.d.html) (founder, launch) · [The Capital via 36Kr, 2026-10-22](https://eu.36kr.com/zh/p/4036453319660681) (cumulative financing above $200M per 5Y Capital; it gave the new-user offer as 100 million tokens plus one month of Pro, which differs from the 300 million tokens plus 3 months of Pro the site states now — this page follows the site)
