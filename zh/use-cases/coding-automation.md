# 如何选择用于代码自动化的 Agent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-1f6feb?style=for-the-badge)](coding-automation.md)
[![EN](https://img.shields.io/badge/EN-English-9ca3af?style=for-the-badge)](../../use-cases/coding-automation.md)
[![Home](https://img.shields.io/badge/HOME-README-24292f?style=for-the-badge)](../README.md)

这个页面不回答“agent 能不能写代码”。

现在这个问题已经不重要了。真正重要的是：你的代码工作流更适合哪一种 operating model。

## 先看结论

| 你的真实需求 | 先看哪个 |
| --- | --- |
| 我要在本地终端或 IDE 里高频协作 | [Claude Code](../agents/claude-code.md) |
| 我要把明确任务异步丢到云端跑 | [Codex](../agents/codex.md) |
| 我要 Anthropic 的后台 / 定时 / 管理式路径 | [Claude Managed Agents](../agents/claude-managed-agents.md) |
| 我要编辑器内强审批、强控制 | [Cline](../agents/cline.md) |
| 我要 VS Code + GitHub 里本地和云端切换 | [GitHub Copilot](../agents/github-copilot.md) |
| 我要一个开源、接近 Devin 路线的软件工程 agent | [OpenHands](../agents/openhands.md) |
| 我要把明确 issue 直接交给 agent 执行 | [Devin](../agents/devin.md) |
| 我要 review-first、任务板式、多次尝试对比 | [Froge Code](../agents/froge-code.md) |
| 我要长期自托管，还需要 memory、skills、messaging | [Hermes Agent](../agents/hermes-agent.md) |
| 我要 runtime、渠道、设备和更强控制面 | [OpenClaw](../agents/openclaw.md) |
| 我要快速搭自己的 agent，而不是买现成产品 | [LangChain](../agents/langchain.md) |
| 我要长期运行、有状态、可恢复 workflow | [LangGraph](../agents/langgraph.md) |

## 三步判断

1. 先决定你是要“直接用 agent”，还是“自己搭系统”。
2. 再决定你更在意“低运维托管”，还是“高控制自托管”。
3. 最后决定你要“agent 自主推进”，还是“人始终主导 review”。

## 最常见的四条路线

| 路线 | 代表项目 | 核心感觉 |
| --- | --- | --- |
| 本地协作型 | [Claude Code](../agents/claude-code.md), [Cline](../agents/cline.md) | 边聊边做，节奏快，控制感强 |
| 云端委派型 | [Codex](../agents/codex.md), [Devin](../agents/devin.md) | 先交任务，再回来 review |
| review-first 自动化 | [GitHub Copilot](../agents/github-copilot.md), [Froge Code](../agents/froge-code.md) | 让 agent 很强，但把合并和节奏留给人 |
| 自建 / 自托管 | [OpenHands](../agents/openhands.md), [Hermes Agent](../agents/hermes-agent.md), [LangChain](../agents/langchain.md), [LangGraph](../agents/langgraph.md) | 灵活，但要自己承担环境和运维 |

## 关键取舍

| 项目 | 最值得看的优点 | 最需要接受的代价 |
| --- | --- | --- |
| Claude Code | 本地 loop 很顺，MCP、instructions、subagents 组合完整 | 权限、环境和节奏还是你自己管 |
| Claude Managed Agents | 更适合后台、定时和程序化运行 | 官方公开边界不是单一产品页 |
| Codex | 云端隔离、日志和测试证据很清楚 | 更偏异步，不如编辑器内 agent 即时 |
| GitHub Copilot | 本地、CLI、cloud 都能串起来 | 最佳体验更依赖 VS Code / GitHub |
| Cline | 编辑器内强能力 + 强审批 | 高频审批会带来摩擦 |
| OpenHands | 开源路线完整，CLI / GUI / cloud 都能走 | 安装、Docker、模型配置成本更高 |
| Devin | 托管式执行很直接 | 自定义和控制边界更少 |
| Froge Code | 多尝试、worktree 隔离、人工挑选很清楚 | 流程更重，依赖接入的 provider |
| Hermes Agent | 长期使用的自托管工作环境很完整 | 需要长期整理权限、memory 和 skills |
| OpenClaw | 渠道、设备、runtime 控制面很强 | 对纯 coding 任务往往偏重 |
| LangChain | 自定义 agent 起步快 | 复杂 workflow 最终常常还是要下沉到 LangGraph |
| LangGraph | 持久化、有状态、审批流和恢复能力强 | 工程和运维成本最高 |

## 最容易选错的地方

- 你其实想要现成 agent，却先选了 framework。
- 你其实想要 review-first，却先选了 autonomy-first 执行器。
- 你只是想做代码自动化，却把消息渠道、设备接入、runtime 全一起背上了。
- 你没有先想清楚权限、密钥、代码暴露和测试责任。

## 一个够用的原则

先选能解决当前问题的最小 agent surface。

不要为了“以后可能会用到”，第一天就把 runtime、平台和 orchestration 一次性全装上。