# Doubao (豆包, ByteDance)

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/doubao.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](doubao.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Doubao is ByteDance's consumer assistant, now in two agent forms — a **work-task mode** in the app that runs Office deliverables and scheduled tasks, and the **Doubao Phone Assistant (豆包手机助手)**, a system-level service on partner phones that can operate other apps on the device — which makes it the only agent on this list built into a phone's operating system.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | ByteDance (App Store seller: Beijing Chuntian Zhiyun Technology) |
| Route | Consumer personal agent |
| Open source | No |
| Form factor | Doubao app (iOS, Android, PC, web); **Doubao Phone Assistant** as a system service on partner mobile devices |
| Status | Work-task mode and the "Ask Doubao before you buy" (买前问豆包) shopping assistant shipped in app v15.4.0 (**Oct 19 2026**). The phone assistant is listed in Doubao's own account terms as a system service on partner devices |
| Where it runs | App: ByteDance's service. Phone assistant: on the partner phone, operating its apps |
| Model | ByteDance's Doubao models; the listing names Seedance for video and no version for the agent |
| Price | Free basic use, with paid auto-renewing subscriptions (see the app's paid-service terms) |
| Regions | China |
| Official pages | https://apps.apple.com/cn/app/id6459478672 · https://o.doubao.com |

## The Two Forms

**Work-task mode (工作任务模式)** — per the App Store description, it "understands the request and executes automatically" with built-in Office and professional skills, and **supports scheduled tasks**, handing off complex work in one step.

**Doubao Phone Assistant (豆包手机助手)** — Doubao's account terms (updated Sept 10 2026) list "the Doubao Phone Assistant and other system services on partner mobile smart devices" as part of the Doubao account system. IT之家, citing ByteDance's press release, reports that the consumer version was released on **Sept 14 2026**, first on the nubia NaviX Ultra (on sale Sept 16); that "operate the phone" (操作手机) opens as a **Beta**; and that a **Screen Automation Operation Declaration Protocol (SAEP)** lets third-party apps declare whether they allow or refuse AI screen automation — with a 30-day public notice period — and that the assistant will not automate apps that refuse. This map has not found the protocol text itself on a first-party page.

## When To Pick It

- You are in China and want an agent that **operates the apps on your phone itself**, not a cloud copy of them — and you have, or will buy, a supported device.
- You want office deliverables and scheduled tasks from the app you may already use daily.

## When Not To Pick It

- You do not want an agent with **OS-level reach** into every app on your phone. That is the product, and the most sensitive permission surface on this list.
- You need the agent to work in apps that have declined screen automation under SAEP: it will not touch them.
- You are outside China.

## Bottom Line

The most deeply integrated agent here — inside the phone's system layer rather than inside an app — and therefore the one where "which apps may it touch" is a real policy question, now being settled app by app under SAEP. Read the app-level controls on your device before turning cross-app operation on.

## Sources

- [豆包 on the App Store (China), v15.4.0 release notes](https://apps.apple.com/cn/app/id6459478672)
- [Doubao account service terms (updated Sept 10 2026)](https://www.doubao.com/legal/doubao_account_service_terms) · [Doubao Phone Assistant site](https://o.doubao.com)
- Media (not first-party): [IT之家 on the Doubao Phone Assistant consumer release](https://www.ithome.com/1/001/971.htm)
