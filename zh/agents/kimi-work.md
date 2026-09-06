# Kimi Work

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](kimi-work.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/kimi-work.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Kimi Work 是月之暗面面向知识工作的桌面 agent——把 [Kimi Code](kimi-code.md) 的循环指向你挂载的文件夹，配一个会替你点击的浏览器扩展和一个内置 cron 引擎，后面还站着一群子 agent。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 月之暗面（Moonshot AI） |
| 路线 | 通用自主 agent（本地优先的桌面端） |
| 是否开源 | 否 |
| 最适合 | 落在本地文件上的重复性知识工作：调研转幻灯片与表格、定时产出报告 |
| 主要代价 | 闭源桌面客户端；它会挂载你的文件夹，并驱动你已登录的浏览器 |
| 平台 | macOS（Apple Silicon）、Windows |
| 公测 | 2026-06-03 → 06-04 宣布 |
| 官方页面 | https://www.kimi.ai/products/kimi-work |

## 为什么要收录

本地图已经收了月之暗面的终端编码 agent [Kimi Code](kimi-code.md)。Kimi Work 是同一家厂商把那套循环搬下代码仓库、搬上桌面，而且厂商说得很直接：**Kimi Work 的内核就是 Kimi Code。** 这让它成为本目录里最干净的一个例子——一条编码 agent 的循环被重新瞄准到通用工作上。这是一个选型问题，因为它的长处和它的失效模式会一起被带过去。

它还和腾讯 [WorkBuddy](workbuddy.md) 落在同一个时间窗内，这也是本地图现在把"桌面知识工作 agent"作为一个类别、而不是当成个别现象记录的原因。

## 什么时候选它

- 你的活是**本地文件加网页**，而且你想要一个 agent 两头都能干：在你授权下挂载文件夹，然后用 Kimi 浏览器扩展、借你已经登录的会话去导航、点击、滚动、抽取。
- 你想让事情**按时发生**。内置 cron 引擎全天候跑任务，包括 LLM agent 调用和 Python 脚本——这更接近一条常驻自动化，而不是一次聊天。
- 你要的产出是**交付物**：它直接把调研转成 PowerPoint 和 Excel。
- 活**大到值得并行**——agent 集群会调度专职子 agent，据报复杂任务下最多可到 300 个。
- 你在中国市场做金融或研究：A 股、港股、美股行情数据已预集成，线上 Kimi Agent 的 skills 与金融、科学、法律专业数据库也一并继承。

## 什么时候不选它

- **它驱动的是你已经登录的浏览器。** 这一句话里同时是它的卖点和它的风险。凡是你不希望一个自主循环拿你的活跃会话去做的事，都是把它的权限收紧、甚至干脆不跑它的理由。
- 你想审计这条循环。闭源，却同时够得到文件系统和浏览器——和本地图上那些开源 harness 是相反的治理位置。
- 你要的是编码 agent——那是 [Kimi Code](kimi-code.md)，面向仓库它是更合适的工具。
- 你需要 Linux，或者一套完全不依赖月之暗面的模型栈。
- 你需要稳定性承诺：这是 2026 年 6 月才开放公测的年轻产品。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 本地文件工作 | 很强 | 在授权下挂载文件夹并在其中工作 |
| 浏览器自动化 | 很强 | Kimi 浏览器扩展负责导航、点击、滚动、抽取 |
| 定时调度 | 很强 | 内置 cron 引擎；LLM 调用与 Python 脚本都能作为定时任务 |
| 多 agent | 强 | 由专职子 agent 组成的 agent 集群（据报最多 300 个） |
| 办公成品 | 强 | 调研直接转幻灯片与表格 |
| 领域数据 | 强 | 预集成 A 股 / 港股 / 美股；继承金融、科学、法律数据库 |
| 开源 / 可审计性 | 无 | 闭源 |

## 和 Kimi Code 的关系

同一家厂商、同一套底层循环，工作单位不同。[Kimi Code](kimi-code.md) 是终端 agent，对象是代码仓库，被本地图的热度榜跟踪，也归入[编码 CLI 对比](../comparisons/coding-cli-agents.md)。Kimi Work 的对象是你的桌面。如果你只想要月之暗面的一个 agent 来做工程，拿 Kimi Code；Kimi Work 的理由是那些必须碰真实文件与真实网站的、重复发生的非代码工作。

## 结论

Kimi Work 是迄今最明确的一个信号：厂商是打算让编码 agent 的循环成为通用工作的循环。cron 引擎和浏览器扩展是它区别于一个聊天窗口的地方——也正是你在让它无人值守运行之前，应该先把权限划清楚的地方。
