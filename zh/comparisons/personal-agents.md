# 消费级个人 agent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](personal-agents.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/personal-agents.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

这一页收的是你把日常交出去的那类 agent——跑腿、收件箱、预订、文档、你的手机——它们以消费级产品的形式出售，而不是你自己运行的软件。它们都不开源（其中一个有开源的兄弟项目）。本页做收录，按事实和控制力而不是热度来比较，并记录它们的变化。

> **最近复核：** 2026-10-21 · 下面每条事实都来自厂商自己的页面、帮助中心或应用商店页面，标注 *媒体* 的除外。格子里写 **?** 表示厂商没有一手文档说明——不代表产品没有这个能力。

## 为什么这里没有热度排名

本地图的其他部分用 GitHub star 给开源项目排名，这是任何人都能核对的公开数字。闭源消费级产品没有对应的东西：下载量、月活和应用商店排名要么是二手转述，要么口径不一，要么根本不公布。用它们拼出来的排名看着精确，实际上是编的。所以本页只做**收录和比较**，变化体现在页面底部的"最近变化"记录里。

你自己运行的自托管个人 agent——[Hermes Agent](../agents/hermes-agent.md)、[OpenClaw](../agents/openclaw.md)、[OpenHuman](../agents/openhuman.md)、[Goose](../agents/goose.md)——以及桌面知识工作 agent [Kimi Work](../agents/kimi-work.md) 和 [WorkBuddy](../agents/workbuddy.md)，见[能力矩阵](../capabilities/matrix.md)和热度榜。

## 全景一览

| Agent | 厂商 | 形态 | 状态（日期） | 在哪里干活 | 模型 | 入门价格 | 地区 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ChatGPT dots](../agents/chatgpt-dots.md) | OpenAI | ChatGPT 应用；Slack、Teams、电话 | 逐步推出（2026-09-29） | 自己的云端电脑和浏览器；一台已连接的个人电脑 | GPT-6 Astra | Pro，$100/月 | 不含欧洲经济区、英国、瑞士 |
| [Gemini Task](../agents/gemini-task.md) | Google | Gemini 应用里的 Chat/Task 切换 | 已上线，原名 Spark（2026-05-19） | 远程浏览器/电脑；你的 Chrome | Gemini 3.5 + Antigravity harness | AI Pro，$19.99/月（美国） | 不含欧洲经济区、英国、瑞士、尼日利亚 |
| [Claude（Cowork）](../agents/claude-cowork.md) | Anthropic | Claude 应用；Claude in Chrome | 已并入 Claude（2026-09-16） | 隔离的云端会话；你的电脑；Chrome | Anthropic 当前模型 | Pro，$20/月 | ? |
| [Muse](../agents/meta-muse.md) | Meta | 应用、网页、WhatsApp | 美国小范围测试（2026-09-08） | 带浏览器的专属云端虚拟机 | Muse Spark | 免费；Power $20/月 | 美国 |
| [Grok Bot](../agents/grok-bot.md) | xAI | 桌面 + 移动应用；X 上 `@bot` | Beta（2026-08-11） | Cursor 云上一台共享云电脑，位于美国 | 由 Cursor 选择 | X Premium，$30/月 | 算力在美国 |
| [Cue](../agents/manus-cue.md) | Manus | 网页、桌面、移动应用 | 抢先体验，仅限邀请 | 每个 agent 一台电脑 | ? | 抢先体验期免费 | ? |
| [豆包](../agents/doubao.md) | 字节跳动 | 应用；合作手机上的系统服务 | 已上线；手机操作为 Beta（2026-09-14，*媒体*） | 字节跳动服务；**你手机的系统层** | 豆包模型 | 免费 + 订阅 | 中国 |
| [千问 App](../agents/qwen-app.md) | 阿里巴巴 | 应用 | 已上线 | 阿里服务及合作服务 | 千问 | 免费 + 订阅 | 中国 |
| [AutoGLM](../agents/autoglm.md) | 智谱 | 应用；开源框架 | 应用最近更新 2026-07-09 | 云手机 + 云电脑；或经 ADB/HDC 操作你的手机 | AutoGLM-Phone-9B | 免费 | 中国（应用） |
| [元宝](../agents/yuanbao.md) | 腾讯 | 应用 | Agent 功能自 2026-07-06 | 腾讯服务 | Hy3 | 免费 | 中国 |

## 能力格

图例与[能力矩阵](../capabilities/matrix.md)一致：● 核心强项 · ◐ 扎实支持 · ○ 有限 · — 不是目标 · **?** 无一手文档。

| Agent | 网上跑腿 | 交付成品 | 定时 | 你的设备 | 记忆 | 多 agent | 审批控制 | 能自己跑 |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [ChatGPT dots](../agents/chatgpt-dots.md) | ● | ● | ● | ◐ | ● | ● | ● | — |
| [Gemini Task](../agents/gemini-task.md) | ● | ◐ | ● | ◐ | ◐ | ○ | ● | — |
| [Claude（Cowork）](../agents/claude-cowork.md) | ◐ | ● | ● | ◐ | ● | ? | ● | — |
| [Muse](../agents/meta-muse.md) | ● | ? | ? | ○ | ● | ? | ● | — |
| [Grok Bot](../agents/grok-bot.md) | ● | ◐ | ● | ○ | ● | ● | ◐ | — |
| [Cue](../agents/manus-cue.md) | ● | ? | ? | ○ | ? | ● | ◐ | — |
| [豆包](../agents/doubao.md) | ◐ | ● | ● | ● | ? | ? | ◐ | — |
| [千问 App](../agents/qwen-app.md) | ● | ● | ● | ○ | ? | ? | ? | — |
| [AutoGLM](../agents/autoglm.md) | ● | ○ | ? | ● | ? | ? | ? | ● |
| [元宝](../agents/yuanbao.md) | ○ | ● | ? | — | ? | ? | ? | — |

几个难打的格子是怎么打的：**你的设备**只有在 agent 操作你手里那部手机上的应用时才给 ●（豆包的系统服务；AutoGLM 的开源框架），能用你的电脑或浏览器给 ◐，只在厂商机器上干活给 ○。**审批控制**在厂商写明了逐动作确认规则或分级授权时给 ●（dots 的自动审查与自定义规则、Gemini 的确认清单、Claude 的三种模式、Muse 的 Sentinel），有控制但不完整或较粗时给 ◐（Grok Bot 的 Auto Review 不覆盖所有副作用；Cue 的预算；豆包靠应用级 SAEP 声明）。

## 决定大多数选择的三个问题

1. **它用谁的身份办事？** 这里几乎每个 agent 都以你的身份登录。[Cue](../agents/manus-cue.md) 给每个 agent 自己的邮箱、电话号码和钱包——对你的账号暴露更少，对它联系的人暴露更多。
2. **它在谁的机器上干活？** 厂商的云电脑（dots、Muse、Grok Bot、Cue、AutoGLM 应用），你的浏览器或电脑（Gemini、Claude、dots 连接的电脑），还是你手机的操作系统（豆包）。离你的设备越近，你交出去的权限越大。
3. **厂商看不看得到、拿不拿去训练？** 在宣布的 Confidential VM 上线之前，Muse 的运营方仍能接触你的数据；Claude 是否训练由你选，保留期是 5 年对 30 天；Grok Bot 只在 Privacy Mode 下不训练；Gemini Task 要求开启保留活动记录。好几个产品根本没写这一点——把"没写"也当成一个答案。

## 最近变化

新的在前。本记录随每周更新刷新；已注明日期的条目不改写。

- **2026-10-21** —— 建页，收录十个 agent。顺带记下：Grok Bot 于 10 月 12 日并入 X Subscription（Premium $30、Super $100、Ultra $200）；千问Go! 于 10 月 13 日被媒体报道为千问应用内的预约排队功能（尚无一手确认）；Muse Wonder（10 月 12 日）宣布将"很快"为 Muse 提供能力，订阅用户优先；豆包 v15.4.0（10 月 19 日）上线工作任务模式和购物助手。

## 候补

尚未收录的候选：**Kimi 应用**的 Agent 集群（[Kimi Work](../agents/kimi-work.md) 的消费级前端）；**百度文心**的任务托管模式；**阶跃星辰**的 Step Agent；**MiniMax Agent**。手机厂商的系统级 agent（荣耀、vivo、华为）目前只出现在媒体盘点里。
