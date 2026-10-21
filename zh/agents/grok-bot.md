# Grok Bot

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](grok-bot.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/grok-bot.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：Grok Bot 是 xAI 的一组常驻 agent——好几个有名字的 Bot 共用一台云端电脑，登录你的工具，各自保留记忆，并按计划重跑保存下来的技能——包含在 X Subscription 里，算力由 Cursor 提供。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | xAI（算力由 Cursor 运行） |
| 路线 | 消费级个人 agent |
| 开源 | 否 |
| 形态 | 桌面应用（macOS、Windows、Linux）、移动应用（iPhone、iPad、Android）；也可在 X 上 `@bot`，但尚未覆盖所有地区 |
| 状态 | **2026-08-11** 起 beta；9 月 3 日推出企业版 |
| 在哪里跑 | **你所有的 Bot 共用一台云端电脑**（文件、浏览器会话、应用登录都共享），**在 Cursor 的云上**，位于**美国** |
| 模型 | 不由你选——"Cursor 负责模型选择"，没有模型选择器 |
| 价格 | 2026-10-12 起包含在 X Subscription 的 **Premium（$30/月）、Super（$100/月）、Ultra（$200/月）**，Plus（$8）不含 |
| 官方页面 | https://x.ai/news/introducing-grok-bot |

## 为什么收录

它是按"把 agent 当同事"来设计的：多个有名字的 Bot 共用一台电脑，互相发消息，在群聊里协作，并能把任务的负责权交给彼此。它也说明厂商边界已经模糊到什么程度——一个 xAI 产品，电脑和模型路由都是 Cursor 的；本地图另有 Cursor 的[编辑器 profile](cursor.md)。

## 什么时候选它

- 你想要**几个各管一摊的常驻 agent**（外联、营销活动、运营），而不是一个助手，并希望它们在共享聊天里协作。
- 工作跨越没有 API 的工具：有连接器就用连接器，没有就用浏览器；你可以**带它走一遍流程**，它会存成技能并按计划重跑。
- 你已经在付 SuperGrok、Cursor 或 X Premium，希望 agent 跟它们共用一张账单、一个用量池。

## 什么时候不选它

- 你需要知道或选择模型。模型组合由 Cursor 决定，并且"会随时间变化"。
- 你需要数据在美国以外，或者不经销售就拿到书面的数据驻留承诺。
- 你希望每一个副作用都被审查。按 xAI 自己的文档，它的"Auto Review"模型会检查有风险的动作，但不会审查每一个副作用。

## 权限与数据

Bot 以登录成员的身份行事，没有自己的凭证。需要审批的动作会展示拟执行的操作及其输入，你可以选 **Allow once**（允许一次）、**Always allow**（保存为匹配规则）或 **Deny**（拒绝）。训练方面："开启 Privacy Mode 时，客户数据不会用于训练"——这个承诺绑定在 Privacy Mode 上，不是无条件的。

## 结论

一个按"团队"搭起来的个人 agent——好几个 Bot、一台真实的共享电脑、定时技能——但你看不到也选不了干活的是哪个模型。看中委派的广度就选它；把真实账号交给它之前，先打开 Privacy Mode、收紧审批。

## 来源

- [Introducing Grok Bot（2026-08-11）](https://x.ai/news/introducing-grok-bot) · [Grok Bot for Enterprise（2026-09-03）](https://x.ai/news/grok-bot-for-enterprise) · [Introducing The X Subscription（2026-10-12）](https://x.ai/news/x-subscription)
- [Grok Bot 概览](https://docs.x.ai/grok-bot/overview) · [审批、安全与隐私](https://docs.x.ai/grok-bot/security) · [X Subscription 里的 Grok Bot](https://docs.x.ai/x-subscription/grok-bot)
