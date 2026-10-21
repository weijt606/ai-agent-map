# Muse（Meta）

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](meta-muse.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/meta-muse.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：Muse 是 Meta 的消费级个人 agent——你在它自己的应用或 WhatsApp 里给它发消息，它在一台带浏览器的专属云端虚拟机上把事办完，付款走一次性卡号——公开了一份详细的安全设计，而它的隐私模式只是宣布、还没上线。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | Meta |
| 路线 | 消费级个人 agent |
| 开源 | 否 |
| 形态 | iOS 与 Android 应用、muse.ai 网页、WhatsApp；AI 眼镜"即将推出" |
| 状态 | **2026-09-08** 发布，"正在美国推出"；Meta 帮助中心称 Muse 及其订阅"正在小范围测试" |
| 在哪里跑 | **Muse Secure VM**——每人一台带独立浏览器的专属云端电脑 |
| 模型 | **Muse Spark**；Meta 称 [Muse Wonder](../market-events.md) 将"很快为 Muse 提供能力"，订阅用户优先 |
| 价格 | 免费（有用量限制）；**Power $20/月**（每周 5 亿 Muse token）、**Maximum $100/月**（每周 30 亿） |
| 官方页面 | https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ |

别和 Meta 的 Muse *模型*（Muse Spark、Muse Wonder）混淆——本地图在[成本与 benchmark](../comparisons/cost-and-benchmarks.md) 里跟踪它们——也别和 Meta 的编码 agent Muse Code 混淆。

## 什么时候选它

- 你想要一个办**生活杂事**的 agent——填表、预订、账单、购物——并且更愿意像跟人聊天一样给它发消息，包括在 WhatsApp 里。
- 你希望购物时不交出自己的卡：结账走 **Link by Stripe**，生成一次性卡号；Meta 称 Muse 是第一个享受 Link 购物保障的 agent。
- 你希望厂商公开了 agent 是怎么被约束的，而不只是它能做什么。

## 什么时候不选它

- 你不在美国，或不在小范围测试名单里。
- 你需要厂商本身也看不到你的数据。目前的架构"不阻止 Meta 在支持、保护或运营服务所必需时访问数据"；用只有你持有的密钥加密的 **Muse Confidential VM** 宣布在"今年晚些时候"推出，尚未上线。
- 你需要用现有的登录信息。1Password 支持和 Shop Pay 都还是"即将推出"。

## 权限与数据

宿主侧的 **Sentinel**（agent 无法覆盖）是"连接器动作与网络出口的唯一权限决定方"；agent 永远看不到真实凭证。授权可以是一次性、会话级、任务级、限时或永久。Muse 会记住你说过的事并主动给建议；你可以让它"忘掉"特定内容。Meta 设有最高 30 万美元的漏洞奖励，包括成功的提示词注入。本地图读到的帮助中心页面写了价格与用量，但没有说对话是否用于训练模型。

## 结论

一个公开了约束设计的跑腿 agent——但在 Confidential VM 上线之前，运营方仍能接触你的数据。把它当作一个很强的美国限定预览版，而不是一个已经讲完的隐私故事。

## 来源

- [Introducing Muse（Meta，2026-09-08，09-30 更新）](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)
- [Security and safety for AI agents: our approach with Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)
- [Muse 订阅（Meta 帮助中心）](https://www.meta.com/help/subscriptions/1021145227643680/) · [Muse Wonder](https://research.meta.ai/blog/muse-wonder)
