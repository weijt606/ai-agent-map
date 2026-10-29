# Claude Managed Agents

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](claude-managed-agents.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/claude-managed-agents.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Claude Managed Agents 是 Anthropic 一个有正式名称的 API 产品（beta）：跑在托管基础设施上、预置且可配置的 agent harness，面向长时间运行和异步的工作。

> **更正（2026-10-30）：** 本 profile 原先把"Claude Managed Agents"说成本仓库对 Anthropic 几种执行路径的统称，而不是产品名。Anthropic 的文档现在把它作为独立产品来写："Pre-built, configurable agent harness that runs in managed infrastructure"，围绕 agent、environment（Anthropic 托管的云端沙箱，或你自己基础设施上的自托管沙箱）、session 和 event 四个概念，需要 `managed-agents-2026-04-01` beta header，API 账号默认开通。它不符合零数据保留（ZDR）和 HIPAA BAA 的适用条件。来源：[Claude Managed Agents 概览](https://platform.claude.com/docs/en/managed-agents/overview)。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Anthropic |
| 路线 | 管理式 / 云端执行工作流 |
| 是否开源 | 否 |
| 最适合 | 后台、定时、程序化的 Claude 执行 |
| 主要代价 | 处于 beta（`managed-agents-2026-04-01` header）；session 有状态并存在服务端，因此不适用零数据保留和 HIPAA BAA |
| 官网 | https://platform.claude.com/docs/en/managed-agents/overview |

## 什么时候选它

- 你要的是 Claude 在后台持续跑，而不是本地强交互。
- 你需要 Agent SDK、cloud scheduling、程序化接入这类能力。
- 你想把 Anthropic 的 agent loop 嵌进自己的系统或流程里。

## 什么时候别选

- 你需要零数据保留或 HIPAA BAA；Managed Agents 两者都不适用。
- 你想要高度互动的本地 coding 体验。
- 你需要开源方案。自托管沙箱是有的，但 harness 和模型仍是 Anthropic 的。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Managed execution | 强 | 更适合后台和云端路径 |
| Scheduling | 强 | 适合定时、轮询、持续任务 |
| Programmability | 强 | Agent SDK 是重要入口 |
| Subagents | 强 | 适合做专门分工 |
| Local interaction | 中 | 不如 Claude Code 那样强调本地协作 |

## 使用代价

复杂度是 Medium。难点不在技术能力，而在数据和生命周期模型上：session、environment 和它们保存的历史都是服务端资源，要通过 API 创建、引导和删除。

## 最后一句

如果你的真实需求是“让 Claude 在后台干活”，这个条目比单看 Claude Code 更接近答案。