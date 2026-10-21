# Claude（Cowork）

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](claude-cowork.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/claude-cowork.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：Anthropic 的个人 agent 已经不是一个单独的产品——**Cowork 在 2026-09-16 并入了 Claude 应用**，所以同一个会聊天的 Claude 现在也能接任务、定时执行、在你合上电脑后继续在隔离的云端会话里干活，并通过 Claude in Chrome 操作浏览器——它有三种命名清楚的审批模式，按任务选择。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | Anthropic |
| 路线 | 消费级个人 agent |
| 开源 | 否 |
| 形态 | 桌面（macOS、Windows）、网页和移动端的 Claude 应用；浏览器操作用 **Claude in Chrome** 扩展 |
| 状态 | Cowork 桌面版 **2026-04-09** GA；**07-07** 上线网页与移动端并支持远程会话（beta）；Claude in Chrome **08-26** 在所有付费套餐 GA；**09-16** Cowork 与聊天合并，先向 Pro 与 Max 推出，Team 与 Free 随后 |
| 在哪里跑 | 云端任务跑在"Anthropic 服务器上一个隔离的临时环境"里，按会话创建；也可以在你自己的电脑上使用 computer use |
| 模型 | Anthropic 当前的模型（见 [Opus 5](claude-opus-5.md)、[成本与 benchmark](../comparisons/cost-and-benchmarks.md)） |
| 价格 | **Pro $20/月**（按年付 $17/月）；**Max $100/月起** |
| 官方页面 | https://claude.com/resources/articles/cowork-is-now-claude |

本地图另外收录了 Anthropic 的编码 agent（[Claude Code](claude-code.md)）和面向开发者的托管 agent（[Claude Managed Agents](claude-managed-agents.md)）。Claude Tag（Slack 里的 Claude）是 Team 与 Enterprise 产品，所以不在这里。

## 什么时候选它

- 你想要**一个应用**同时提问和委派：不用在聊天产品和 agent 产品之间切换。
- 你希望合上电脑之后**活儿还在继续**，并且能定期重复。
- 你想按任务决定 agent 可以自己做多少。

## 什么时候不选它

- 你是 Team 或 Free 用户，而且现在就要用：合并后的体验先到 Pro 与 Max。
- 你希望 agent 在你自己的电脑上操作时也被隔离。Anthropic 直说 computer use"在 Claude 和你屏幕上的内容之间没有沙箱"。
- 你想在其他 Chromium 浏览器或手机浏览器里用：Claude in Chrome 不支持。

## 权限与数据

三种审批模式：**手动批准**、**自动批准**（Claude 仍会在每个动作执行前做安全检查）和**跳过所有审批**（没有任何东西检查它的动作）。无论哪种模式，永久删除文件前都会先问你。Anthropic 建议在涉及敏感文件、新工具，以及发消息、购物这类难以撤销的操作时用手动批准。在 Chrome 里，每个动作执行前都有安全分类器校验。记忆在聊天和 Cowork 之间共享（2026-08-25 起），在"设置 → 记忆"里逐条列出、可编辑可删除；健康、信仰之类的话题默认不进记忆，除非你打开敏感话题选项；Free、Pro、Max 默认开启。消费者套餐是否用于训练由你选择：允许的话数据保留五年，不允许则维持 30 天的保留期。

## 结论

把 agent 并进默认应用、而不是单独卖的做法，并且在最要紧的那根轴上——不问你能做多少——给了三种明确的模式。认真选一个模式；"跳过所有审批"就是字面意思。

## 来源

- [Claude Cowork 与聊天合并为一个 Claude（2026-09-16）](https://claude.com/resources/articles/cowork-is-now-claude) · [Claude in Chrome 正式可用（2026-08-26）](https://claude.com/resources/articles/claude-in-chrome-generally-available)
- [Claude 发布说明](https://support.claude.com/en/articles/12138966-release-notes) · [安全使用 Claude Cowork](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Claude 价格](https://claude.com/pricing) · [消费者条款更新](https://www.anthropic.com/news/updates-to-our-consumer-terms)
