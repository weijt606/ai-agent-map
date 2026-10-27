# Claude Duet

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](claude-duet.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/claude-duet.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：Anthropic 的第二个消费级 agent，也是会先来找你的那个。它是一个独立应用，围绕 Opus 5.5 设计：每天早上给你简报，每隔几小时查一次你关联的账号，在你的设备关着时也在自己的虚拟机上干活；发消息、付款、签字或删除任何东西之前都等你点头。它面向专业人士和小企业主，不是用来跑个人杂事的。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | Anthropic |
| 路线 | 消费级个人 agent |
| 开源 | 否 |
| 形态 | iOS 与 Android 上的**独立应用**，以及 claude.ai；"目前"与主 Claude 应用分开 |
| 状态 | **2026-10-21 起以候补名单方式开放研究预览**，先面向美国 Pro 与 Max 订阅用户；iOS 应用 10 月 26 日上架 |
| 在哪里干活 | "一台带自己浏览器的虚拟机"，所以"不需要你的电脑或手机开着" |
| 模型 | 围绕 **Claude Opus 5.5** 设计（[成本与基准](../comparisons/cost-and-benchmarks.md)） |
| 价格 | 预览期间含在 **Pro** 与 **Max** 里，和套餐共用用量额度；它的后台检查也计入额度 |
| 地区 | 先开放美国 |
| 官方页面 | https://claude.com/resources/articles/claude-duet |

## 和 Claude（Cowork）有什么不同

[Claude（Cowork）](claude-cowork.md)是 Claude 应用接你交给它的任务。Duet 是一个独立应用，**由它先开口**：早上就你邮件和日历里需要拍板的事给一份简短简报，之后"每隔几小时"查一次你关联的账号，只在有事需要你时才发消息。你可以告诉它想听什么、多久一次。它会沿用你 Claude 账号里的记忆、skills 和已关联应用，所有事放在一条持续的对话里，也可以按工作领域（财务、招聘）分频道。Anthropic 说，从早期用户那里学到的东西"会决定两者以后怎么配合"。

## 什么时候选它

- 你经营小企业或忙碌的业务，想要一个**盯着**收件箱、日历和业务工具、把要紧的事推给你的东西，而不是等你提问。
- 你的工作都在它能通过 Claude Marketplace 接上的工具里：Gmail、Slack、QuickBooks、Stripe、Gusto、Docusign、HubSpot、Canva、Shopify。
- 你已经是美国的 Pro 或 Max 用户，并且能从候补名单里排上。

## 什么时候不选它

- 你想要一个跑腿的。Anthropic 说个人杂事（"比如订票"）它不太擅长，而且它"还不能把它的浏览器给你看"。
- 你需要实时提醒。它每隔几小时查一次，"紧急的事可能在两次检查之间到来"。
- 你不在美国，或者没有付费套餐。

## 权限与数据

Duet"会自己阅读、起草、准备工作"，但在发消息、付款、签文件或删除任何东西之前，会把它要做的事原样给你看并等你批准。**交易证券和在账户之间转钱即使批准也不允许。**操作要过 Anthropic 的 auto mode 分类器。凭证处理沿用 Claude Managed Agents 的设计，所以 Duet"从不直接看到你的密码或登录令牌"。一个专门的分类器会拒绝分享最高敏感级别的信息，比如银行卡号和政府证件；健康与财务信息只有在你明确指示时才会发出。购物走 Stripe 的 Link：由你批准花费，用虚拟卡支付；在线商店可以用 Shop Pay；用 1Password 登录"即将推出"。本地图读到的页面没有写明 Duet 专门的训练条款。

## 结论

一个被设计成有选择地打扰你的 agent，并且写明了哪些操作即使你批准也不做。它还在预览期：要排候补、只开放美国、何时打扰你的判断还在调。如果你是美国的小企业主、已经在付 Claude 的钱，值得去排候补。其他人等它和主应用合并或正式毕业再说。

## 来源

- [Introducing Claude Duet（2026-10-21，10-23 更新）](https://claude.com/resources/articles/claude-duet) · [Claude 发布说明](https://support.claude.com/en/articles/12138966-release-notes) · [Claude Duet 的 App Store 页面](https://apps.apple.com/us/app/id6803276000)
