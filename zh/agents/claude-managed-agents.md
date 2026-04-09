# Claude Managed Agents

[![ZH](https://img.shields.io/badge/ZH-CURRENT-1f6feb?style=for-the-badge)](claude-managed-agents.md)
[![EN](https://img.shields.io/badge/EN-English-9ca3af?style=for-the-badge)](../../agents/claude-managed-agents.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-24292f?style=for-the-badge)](../README.md)

一句话：这是仓库里对 Anthropic 管理式、云端式 Claude 执行路径的统一叫法，不是一个边界非常清晰的单独产品名。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Anthropic |
| 路线 | 管理式 / 云端执行工作流 |
| 是否开源 | 否 |
| 最适合 | 后台、定时、程序化的 Claude 执行 |
| 主要代价 | 官方边界分散在多个文档概念里 |
| 官方入口 | https://code.claude.com/docs/en/agent-sdk/overview |

## 什么时候选它

- 你要的是 Claude 在后台持续跑，而不是本地强交互。
- 你需要 Agent SDK、cloud scheduling、程序化接入这类能力。
- 你想把 Anthropic 的 agent loop 嵌进自己的系统或流程里。

## 什么时候别选

- 你需要一个名称、边界、控制台都非常明确的单一产品。
- 你想要高度互动的本地 coding 体验。
- 你需要开源或自托管方案。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Managed execution | 强 | 更适合后台和云端路径 |
| Scheduling | 强 | 适合定时、轮询、持续任务 |
| Programmability | 强 | Agent SDK 是重要入口 |
| Subagents | 强 | 适合做专门分工 |
| Local interaction | 中 | 不如 Claude Code 那样强调本地协作 |

## 使用代价

复杂度是 Medium。难点不在技术能力，而在认知模型上: 你需要把它理解成 Anthropic 几种执行模式的组合，而不是一个“点一下就懂”的独立产品。

## 最后一句

如果你的真实需求是“让 Claude 在后台干活”，这个条目比单看 Claude Code 更接近答案。