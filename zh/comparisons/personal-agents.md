# 消费级个人 agent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](personal-agents.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/personal-agents.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

这一页收的是你把日常交出去的那类 agent——跑腿、收件箱、预订、文档、你的手机——它们以消费级产品的形式出售，而不是你自己运行的软件。它们都不开源（其中一个有开源的兄弟项目）。本页做收录，按事实和控制力而不是热度来比较，并记录它们的变化。

> **最近复核：** 2026-10-28 · 下面每条事实都来自厂商自己的页面、帮助中心或应用商店页面，标注 *媒体* 的除外。格子里写 **?** 表示厂商没有一手文档说明——不代表产品没有这个能力。

## 为什么这里没有热度排名

本地图的其他部分用 GitHub star 给开源项目排名，这是任何人都能核对的公开数字。闭源消费级产品没有对应的东西：下载量、月活和应用商店排名要么是二手转述，要么口径不一，要么根本不公布。用它们拼出来的排名看着精确，实际上是编的。所以本页只做**收录和比较**，变化体现在页面底部的"最近变化"记录里。

你自己运行的自托管个人 agent——[Hermes Agent](../agents/hermes-agent.md)、[OpenClaw](../agents/openclaw.md)、[OpenHuman](../agents/openhuman.md)、[Goose](../agents/goose.md)——以及桌面知识工作 agent [Kimi Work](../agents/kimi-work.md) 和 [WorkBuddy](../agents/workbuddy.md)，见[能力矩阵](../capabilities/matrix.md)和热度榜。

## 全景一览

| Agent | 厂商 | 形态 | 状态（日期） | 在哪里干活 | 模型 | 入门价格 | 地区 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ChatGPT dots](../agents/chatgpt-dots.md) | OpenAI | ChatGPT 应用；Slack、Teams、电话 | 逐步推出（2026-09-29） | 自己的云端电脑和浏览器；一台已连接的个人电脑 | GPT-6 Astra | Pro，$100/月 | 不含欧洲经济区、英国、瑞士 |
| [Gemini Task](../agents/gemini-task.md) | Google | Gemini 应用里的 Chat/Task 切换 | 已上线，原名 Spark（2026-05-19） | 远程浏览器/电脑；你的 Chrome | Gemini 3.5 + Antigravity harness | AI Pro，$19.99/月（美国） | 不含欧洲经济区、英国、瑞士、尼日利亚 |
| [Claude（Cowork）](../agents/claude-cowork.md) | Anthropic | Claude 应用；Claude in Chrome | 已并入 Claude（2026-09-16） | 隔离的云端会话；你的电脑；Chrome | Anthropic 当前模型 | Pro，$20/月 | ? |
| [Claude Duet](../agents/claude-duet.md) | Anthropic | 独立应用（iOS、Android）与 claude.ai | 研究预览，候补名单（2026-10-21） | 自己的虚拟机，带浏览器 | Claude Opus 5.5 | Pro，$20/月 | 先开放美国 |
| [Muse](../agents/meta-muse.md) | Meta | 应用、网页、WhatsApp | 美国小范围测试（2026-09-08） | 带浏览器的专属云端虚拟机 | Muse Spark | 免费；Power $20/月 | 美国 |
| [Grok Bot](../agents/grok-bot.md) | xAI | 桌面 + 移动应用；X 上 `@bot` | Beta（2026-08-11） | Cursor 云上一台共享云电脑，位于美国 | 由 Cursor 选择 | X Premium，$30/月 | 算力在美国 |
| [Cue](../agents/manus-cue.md) | Manus | 网页、桌面、移动应用 | 抢先体验，仅限邀请 | 每个 agent 一台电脑 | ? | 抢先体验期免费（含 Plus） | ? |
| [豆包](../agents/doubao.md) | 字节跳动 | 应用；合作手机上的系统服务 | 已上线；手机操作为 Beta（2026-09-14，*媒体*） | 字节跳动服务；**你手机的系统层** | 豆包模型 | 免费；付费档每月 68 元起 | 中国 |
| [千问 App](../agents/qwen-app.md) | 阿里巴巴 | 应用 | 已上线 | 阿里服务及合作服务 | 千问 | 免费 + 订阅 | 中国 |
| [AutoGLM](../agents/autoglm.md) | 智谱 | 应用；开源框架 | 应用最近更新 2026-07-09 | 云手机 + 云电脑；或经 ADB/HDC 操作你的手机 | AutoGLM-Phone-9B | 免费 | 中国（应用） |
| [元宝](../agents/yuanbao.md) | 腾讯 | 应用 | Agent 功能自 2026-07-06 | 腾讯服务 | Hy3 | 免费 | 中国 |
| [Today](../agents/today-ai.md) | 汇翮（上海）智能科技（中国版）；Today AI PTE. LTD.（国际版） | 桌面（Mac、Windows、Linux）、iOS、Android、网页；Chrome 插件 | 已上线；中国区 App Store 首发 2026-10-04 | 自己的云端电脑；经插件用你的 Chrome | 中国版经阿里云百炼、腾讯云 TokenHub、金山云调用 DeepSeek 等模型 | 中国版基础版免费；国际版 Pro $20/月 | 中国 + 国际版 |

## 能力格

图例与[能力矩阵](../capabilities/matrix.md)一致：● 核心强项 · ◐ 扎实支持 · ○ 有限 · — 不是目标 · **?** 无一手文档。

| Agent | 网上跑腿 | 交付成品 | 定时 | 你的设备 | 记忆 | 多 agent | 审批控制 | 能自己跑 |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [ChatGPT dots](../agents/chatgpt-dots.md) | ● | ● | ● | ◐ | ● | ● | ● | — |
| [Gemini Task](../agents/gemini-task.md) | ● | ◐ | ● | ◐ | ◐ | ○ | ● | — |
| [Claude（Cowork）](../agents/claude-cowork.md) | ◐ | ● | ● | ◐ | ● | ? | ● | — |
| [Claude Duet](../agents/claude-duet.md) | ◐ | ● | ● | ○ | ● | ? | ● | — |
| [Muse](../agents/meta-muse.md) | ● | ? | ? | ○ | ● | ? | ● | — |
| [Grok Bot](../agents/grok-bot.md) | ● | ◐ | ● | ○ | ● | ● | ◐ | — |
| [Cue](../agents/manus-cue.md) | ● | ? | ◐ | ○ | ◐ | ● | ◐ | — |
| [豆包](../agents/doubao.md) | ◐ | ● | ● | ● | ? | ? | ◐ | — |
| [千问 App](../agents/qwen-app.md) | ● | ● | ● | ○ | ? | ? | ? | — |
| [AutoGLM](../agents/autoglm.md) | ● | ○ | ? | ● | ? | ? | ? | ● |
| [元宝](../agents/yuanbao.md) | ○ | ● | ? | — | ? | ? | ? | — |
| [Today](../agents/today-ai.md) | ◐ | ◐ | ● | ◐ | ● | ? | ◐ | — |

几个难打的格子是怎么打的：**你的设备**只有在 agent 操作你手里那部手机上的应用时才给 ●（豆包的系统服务；AutoGLM 的开源框架），能用你的电脑或浏览器给 ◐，只在厂商机器上干活给 ○。**审批控制**在厂商写明了逐动作确认规则或分级授权时给 ●（dots 的自动审查与自定义规则、Gemini 的确认清单、Claude 的三种模式、Duet 对发送/付款/签字/删除的审批和禁止清单、Muse 的 Sentinel），有控制但不完整或较粗时给 ◐（Grok Bot 的 Auto Review 不覆盖所有副作用；Cue 的预算与逐笔付款确认；豆包靠应用级 SAEP 声明；Today 只写了提交表单、下单、付款等"关键步骤"由你确认或接手，可随时接管或停止）。

## 决定大多数选择的三个问题

1. **它用谁的身份办事？** 这里几乎每个 agent 都以你的身份登录。[Cue](../agents/manus-cue.md) 给每个 agent 自己的邮箱、电话号码和钱包——对你的账号暴露更少，对它联系的人暴露更多。
2. **它在谁的机器上干活？** 厂商的云电脑（dots、Duet、Muse、Grok Bot、Cue、AutoGLM 应用、Today），你的浏览器或电脑（Gemini、Claude、dots 连接的电脑、Today 的 Chrome 插件），还是你手机的操作系统（豆包）。离你的设备越近，你交出去的权限越大。
3. **厂商看不看得到、拿不拿去训练？** 在宣布的 Confidential VM 上线之前，Muse 的运营方仍能接触你的数据；Claude 是否训练由你选，保留期是 5 年对 30 天；Grok Bot 只在 Privacy Mode 下不训练；Gemini Task 要求开启保留活动记录；Today 两个版本都写明不用可识别的用户内容训练面向公众的基础模型，中国版数据原则上存在中国大陆，实时语音可能在新加坡处理、需另行同意。好几个产品根本没写这一点——把"没写"也当成一个答案。

## 最近变化

新的在前。本记录随每周更新刷新；已注明日期的条目不改写。

- **2026-10-31** —— **收录 [Today](../agents/today-ai.md)**，本页第十二个 agent：一个主打记忆和主动帮助的个人 AI 助理，中国版（todayai.cn）由汇翮（上海）智能科技有限公司运营，国际版（today.ai）的 App Store 卖家是 Today AI PTE. LTD.。它自己的页面写明了：在厂商的云端电脑上打开浏览器、处理文件、运行代码；早间与晚间简报；定时任务；可查看、修改、删除的记忆；一个能在你已登录的 Chrome 里点击和填表的插件；提交表单、下单、付款等关键步骤由你确认或接手。中国版"基础版永久免费"，新用户"注册即领 3亿 Tokens，畅享 3 个月 Pro 权益"；媒体 10 月 22 日写的是 1亿 Token 加一个月 Pro（*媒体*），本页以官网为准。国际版 App Store 内购为 Pro $20/月、Ultra $200/月；中国版 Pro 价格没有公开。中国版隐私政策（10 月 25 日）说不用可识别的用户内容训练面向公众的基础模型，模型推理经阿里云百炼、腾讯云 TokenHub、金山云。据五源资本披露，公司累计融资超过 2 亿美元（*媒体*，10 月 21–22 日）。其余十一个 agent 本期没有复核。
- **2026-10-28** —— **Anthropic 于 10 月 21 日发布 Claude Duet**，一个独立应用，Claude 在里面"作为主动型 agent 工作"：研究预览，凭候补名单开放，先面向美国的 Pro 与 Max 订阅用户；围绕 Claude Opus 5.5 设计；运行在"一台带自己浏览器的虚拟机"上，不需要你的电脑或手机开着；在发消息、付款、签文件或删除任何东西之前会等你批准，交易证券和在账户间转钱即使批准也不允许。Anthropic 说它"目前"与主 Claude 应用分开，这修正了 [Claude（Cowork）](../agents/claude-cowork.md) 那一行的说法：Anthropic 现在有两个消费级 agent 入口。它 10 月 26 日上了美区 App Store，现已收录：[Claude Duet](../agents/claude-duet.md)，本页第十一个 agent。**Cue** 的 App Store 介绍现在写明了定时与事件触发的自动化、记忆功能（"Memory and Dream"）、由你确认的付款，以及获得资格期间免费附带 Plus 会员；调度与记忆两格由 **?** 改为 ◐。**豆包**的 App Store 页面写明了档位（基础版免费；每月 68、200、500 元）；v15.5.0（10 月 26 日）的更新说明与 v15.4.0 相同。**Muse** v13.1（10 月 24 日）让聊天内购物更方便。dots、Gemini Task、Grok Bot、AutoGLM、元宝没有一手变化，千问Go! 仍只有媒体报道。
- **2026-10-21** —— 建页，收录十个 agent。顺带记下：Grok Bot 于 10 月 12 日并入 X Subscription（Premium $30、Super $100、Ultra $200）；千问Go! 于 10 月 13 日被媒体报道为千问应用内的预约排队功能（尚无一手确认）；Muse Wonder（10 月 12 日）宣布将"很快"为 Muse 提供能力，订阅用户优先；豆包 v15.4.0（10 月 19 日）上线工作任务模式和购物助手。

## 候补

尚未收录的候选：**Kimi 应用**的 Agent 集群（[Kimi Work](../agents/kimi-work.md) 的消费级前端）；**百度文心**的任务托管模式；**阶跃星辰**的 Step Agent；**MiniMax Agent**（v4.22.2 应用于 10 月 22 日推出新的"M Plan"订阅）；蚂蚁集团的**灵光**（v1.3.80，10 月 26 日，"灵光2.0"，定位"能管事的个人助理"）。手机厂商的系统级 agent（荣耀、vivo、华为）目前只出现在媒体盘点里。
