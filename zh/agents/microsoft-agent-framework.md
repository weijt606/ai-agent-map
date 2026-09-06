# Microsoft Agent Framework

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](microsoft-agent-framework.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/microsoft-agent-framework.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Microsoft Agent Framework 是 AutoGen 的继任者，也是本地图不收录 AutoGen 的原因——微软已把 AutoGen 置于**维护模式**，并把新用户指到这里。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 微软 |
| 路线 | 自建系统 |
| 仓库 | [`microsoft/agent-framework`](https://github.com/microsoft/agent-framework)——MIT，Python 与 .NET（Go SDK 在 [`agent-framework-go`](https://github.com/microsoft/agent-framework-go)） |
| 是否开源 | 是（MIT） |
| 最适合 | 要把多 agent 系统从原型带进生产的团队，尤其是 .NET 技术栈 |
| 主要代价 | 企业形态的框架；比"一口气读完的循环"重得多 |
| 前身 | **AutoGen**——6.08 万 star，现处维护模式，由社区管理 |
| 博客 | https://devblogs.microsoft.com/agent-framework/ |

## 为什么要收录

两个理由。

第一，本地图的[自建路线](../comparisons/agent-harness-frameworks.md)收了 LangChain、LangGraph、CrewAI、Semantic Kernel、DSPy、Pydantic AI 和 eve，却没有一条来自"上一代框架（AutoGen）在这个品类里被引用最多之一"的那家厂商。

第二，也更有用：**AutoGen 恰恰是读者会去找的那个条目，而今天推荐它是错的。** 它的 README 挂着维护模式声明——不再有新功能或增强，后续由社区管理——并把新用户指到这里，还给了迁移指南。本地图的贡献规则要求把"当前产品"与"已被取代的产品"分开写而不是混为一谈，所以 profile 给继任者，血统记在里面。

## 什么时候选它

- 你在**把 agent 带进生产**而不是做原型：项目自己的说法就是持久性、可重启、可观测、治理与 human-in-the-loop。
- 你需要**超出聊天循环的编排**——顺序、并发、交接（handoff）、群体协作这些基于图的模式。
- 你是 **.NET 团队**。这是本地图自建路线里最强的一等 .NET 选项，Python 与 Go 并列支持。
- 你要厂商灵活性，让架构熬得过一次换模型——Microsoft Foundry、Azure OpenAI、OpenAI、GitHub Copilot SDK 都是受支持路径。
- 你正在从 AutoGen 迁出，需要一个有稳定 API 与长期支持承诺的落点。

## 什么时候不选它

- 你想要小东西。这是企业级框架；想要一条能从头读到尾的循环，去看 [mini-swe-agent](mini-swe-agent.md) 或 [Pi](pi.md)。
- 你要的是成品 agent 而不是框架——看直接执行路线。
- 你的栈只有 Python 且已经压在 LangGraph 或 CrewAI 上；迁移成本是真的，而 MAF 的差异点（多语言、.NET 一等公民）可能对你不成立。
- 你要生态层面的厂商中立：许可是 MIT、支持多厂商，但周边平台故事是微软的。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 多语言覆盖 | **很强** | Python、.NET 与 Go——这条路线上无人能及 |
| 编排模式 | 很强 | 顺序、并发、交接、群体协作，皆为图模式 |
| 生产关切 | 很强 | 持久性、可重启、可观测、治理、human-in-the-loop |
| 厂商灵活性 | 强 | Microsoft Foundry、Azure OpenAI、OpenAI、GitHub Copilot SDK |
| 互操作 | 强 | 用 A2A 与 MCP 做跨运行时 |
| 体量 | 中 | 企业形态；不是一个轻依赖 |

## 关于 AutoGen 的说明

AutoGen（`microsoft/autogen`，6.08 万 star，CC-BY-4.0）仍然是被广泛引用的多 agent 框架，也是一大批既有代码的所在。按它自己的说法，当前状态是维护模式：不再有新功能，由社区管理，新用户被指向本框架，既有用户被指向迁移指南。本地图把它记在这里而不是单开一条，因为一个 profile 意味着一次当前推荐，而这个推荐并不成立。如果你在评估 agent 框架、而调研里冒出了 AutoGen，那份调研已经过期了——从这里开始。

## 结论

来读这一页的理由，往往是它上面那段关于 AutoGen 的说明。作为框架，MAF 是自建路线里"生产 + .NET"的那个答案；作为地图条目，它是对一条生态仍在靠惯性给出的推荐的纠正。
