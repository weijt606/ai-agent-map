# 主流 Agent 选型矩阵

[![ZH](https://img.shields.io/badge/ZH-CURRENT-1f6feb?style=for-the-badge)](mainstream-agent-landscape.md)
[![EN](https://img.shields.io/badge/EN-English-9ca3af?style=for-the-badge)](../../comparisons/mainstream-agent-landscape.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-24292f?style=for-the-badge)](../README.md)

这不是排行榜，而是一张能快速缩小候选集的横向表。

每一行只回答一件事：它更适合拿来解决什么问题。

## 一页式横向对比

| 项目 | 路线 | 运行位置 | 操作节奏 | 最适合 | 主要代价 |
| --- | --- | --- | --- | --- | --- |
| [Claude Code](../agents/claude-code.md) | 本地协作型 coding agent | 终端、IDE、桌面、Web | 高频交互 | 想边做边和 agent 配合写代码 | 不适合完全脱离人的后台执行 |
| [Claude Managed Agents](../agents/claude-managed-agents.md) | 管理式自动化路径 | Anthropic 管理式 / 云端执行 | 后台、定时、程序化 | 想把 Claude 跑成后台工作流 | 官方公开边界分散在多个概念里 |
| [Codex](../agents/codex.md) | 云端委派型 coding agent | 云端隔离环境 + CLI / IDE | 异步委派 | 想丢任务、等结果、看日志和测试证据 | 本地即时协作感弱一些 |
| [GitHub Copilot](../agents/github-copilot.md) | agent 平台 | VS Code、本地 CLI、cloud、GitHub | 本地到云端切换 | 已经工作在 VS Code / GitHub 生态里 | 最佳体验更依赖生态绑定 |
| [Cline](../agents/cline.md) | approval-first coding agent | 编辑器、本地终端 | 强审批、强控制 | 想让 agent 很强，但每一步都可把关 | 审批频率会带来摩擦 |
| [OpenHands](../agents/openhands.md) | 开源 SWE agent | 自托管、cloud、enterprise | 灵活切换 | 想要开源但又不只要一个 demo | 安装和运行成本更高 |
| [Devin](../agents/devin.md) | 托管执行器 | 托管云产品 | 委派后 review | 想直接把 issue 交给 agent 跑 | 自定义和自托管空间更小 |
| [Hermes Agent](../agents/hermes-agent.md) | 自托管多 agent 环境 | CLI + gateway | 长期经营型 | 想要 memory、skills、delegation 和消息渠道 | 需要持续整理权限与环境 |
| [OpenClaw](../agents/openclaw.md) | runtime / gateway | 本地优先 self-hosted | 常驻运行型 | 需要渠道、设备、工具和 runtime 控制面 | 对纯 coding 工作偏重 |
| [LangChain](../agents/langchain.md) | 高层框架 | 开源库 | 快速搭建型 | 想快速做自定义 agent 原型 | 精细状态控制不如更底层框架 |
| [LangGraph](../agents/langgraph.md) | 底层 orchestration 框架 | 开源库 | 平台建设型 | 需要持久化、有状态、可恢复 workflow | 设计和运维成本最高 |
| [Froge Code](../agents/froge-code.md) | review-first 自动化平台 | 自托管平台 | 多尝试 + 人工挑选 | 想把 coding automation 做成任务板流程 | 名称仍待进一步确认 |

## 怎么读这张表

1. 先看“路线”，确定你是本地协作、云端委派、review-first 还是自建平台。
2. 再看“运行位置”，排掉明显不符合你环境边界的项目。
3. 最后看“主要代价”，这往往比功能表更能决定是否适合你。

## 读表时别混淆三件事

- framework 不等于成品 agent。
- 支持某个能力，不等于在那个能力上最强。
- 操作成本也是产品的一部分。