# Browser Use

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](browser-use.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/browser-use.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Browser Use 把一个真浏览器交给 agent——像人一样打开页面、点击、输入、填表单——11.3 万 star、MIT，它是本地图此前完全没有路线覆盖的那项能力的默认答案。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Browser Use（开源项目，另有托管云） |
| 路线 | **浏览器 agent**——一条新路线上的第一个条目 |
| 仓库 | [`browser-use/browser-use`](https://github.com/browser-use/browser-use)——MIT，Python，**11.3 万 star** |
| 是否开源 | 是（MIT）；另有托管的 Browser Use Cloud |
| 最适合 | 活在网站上而不是代码仓库里的任务 |
| 主要代价 | 一个驱动真浏览器的 agent 是实打实的安全面——要刻意划范围 |
| 环境要求 | Python 3.11+ |
| 文档 | https://docs.browser-use.com |

## 为什么要收录

本地图覆盖了改代码的 agent、跑终端的 agent、调度别的 agent 的 agent，以及写文档的 agent。它**没有一条路线**覆盖大多数非工程自动化真正需要的那项能力：驱动一个没有 API 的网站。

当本地图记录到 [Kimi Work](kimi-work.md) 把浏览器自动化作为头条功能、以及 [Claude in Chrome](../market-events.md) 在取消逐动作审批后正式开放时，这个缺口就撑不住了。Browser Use 是这个品类里开放、可自托管的那一个，也是别人被拿来对比的那一个。

## 什么时候选它

- **任务在网站上，而且没有 API。** 填申请、从页面抽结构化数据、跨表单的多步流程——都是项目自己的例子。
- 你想把它装进**你已经在跑的 agent**里：它以 skill 形式注册（`browser-use skill install`），README 里给了 Claude Code、Codex、Cursor、[Hermes Agent](hermes-agent.md)、[OpenClaw](openclaw.md) 的接法——其中三个本地图已经收录。
- 你想在自己的代码里用**任意 LLM**：这个 Python 库按设计与模型无关。
- 你希望以后有换到托管路径的选项而不用换工具——Browser Use Cloud 与库并存。
- 你要 MIT，而不是 copyleft 或 source-available：在浏览器 agent 里，Skyvern 是 AGPL-3.0，而这个差别会决定部署。

## 什么时候不选它

- **你还没想清楚那个浏览器登录着什么。** 这是这个品类的核心风险，不是脚注：一个握着你活跃会话的自主循环，能以你的身份行动。第一次运行之前，先把浏览器配置、凭据和审批闸划清楚。
- 你要的是确定性自动化。如果流程稳定、可脚本化，Playwright 比让模型决定点哪里更便宜、更快、更可预测。
- 你要的是编码 agent——这是给 agent 的一项能力，不是 agent 的替代品。
- 你需要 Node 原生 SDK 而不是 Python——Stagehand（MIT，TypeScript）是可比的邻居，它在本地图的候补名单上而不是已收录。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 网页任务完成 | 很强 | 定义这个品类的实现：打开、点击、输入、填写、抽取 |
| harness 集成 | 很强 | 以 skill 形式提供；文档覆盖 Claude Code、Codex、Cursor、Hermes、OpenClaw |
| 模型自由度 | 很强 | 在你自己的代码里可配任意 LLM |
| 部署选项 | 强 | 自托管库或托管云 |
| 许可 | 强 | MIT，而最接近的替代品是 AGPL-3.0 |
| 安全面 | **谨慎处理** | 被自动化的对象就是一个活的浏览器会话 |

## 它打开的这条路线

"浏览器 agent"在本地图上是一条独立路线，而不是一条功能项，因为选型问题真的不同：你不是在选 agent 怎么改文件，而是在选**允许一个 agent 以你的身份、在开放互联网上做什么**。这条路线补齐之前，值得知道的邻居：**Stagehand**（`browserbase/stagehand`，MIT，TypeScript，2.4 万）是 SDK 形态的那个，**Skyvern**（`Skyvern-AI/skyvern`，AGPL-3.0，2.3 万）是工作流形态的那个。两者都在候补名单上。

## 结论

如果一个 agent 必须像人一样使用网页，就从这里开始：体量最大、MIT、与模型无关，而且已经接进本地图覆盖的 harness 里。把省下的时间花在审批设计上——让它有用的那项能力，和让它危险的是同一项。
