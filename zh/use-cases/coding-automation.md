# 如何选择用于代码自动化的 Agent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](coding-automation.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../use-cases/coding-automation.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

这个页面不回答“agent 能不能写代码”。

现在这个问题已经不重要了。真正重要的是：你的代码工作流更适合哪一种 operating model。

## 先看结论

| 你的真实需求 | 先看哪个 |
| --- | --- |
| 我要在本地终端或 IDE 里高频协作 | [Claude Code](../agents/claude-code.md) |
| 我要终端优先、本地写代码，还想保留强 git 节奏 | [Aider](../agents/aider.md) |
| 我要把明确任务异步丢到云端跑 | [Codex](../agents/codex.md) |
| 我已经在用 Claude Code，只是想补强 teams、skills 和 orchestration | [oh-my-claudecode](../agents/oh-my-claudecode.md) |
| 我已经在用 Codex CLI，只是想补上 teams、hooks 和持久 workflow state | [oh-my-codex](../agents/oh-my-codex.md) |
| 我要 Google 托管、GitHub 连接的云端委派 | [Jules](../agents/jules.md) |
| 我要 Anthropic 的后台 / 定时 / 管理式路径 | [Claude Managed Agents](../agents/claude-managed-agents.md) |
| 我要一个覆盖本地编码、后台 agent 和集成的 AI 编辑器 | [Cursor](../agents/cursor.md) |
| 我要以编辑器流为中心的专用 AI IDE | [Windsurf](../agents/windsurf.md) |
| 我要编辑器内强审批、强控制 | [Cline](../agents/cline.md) |
| 我要 VS Code + GitHub 里本地和云端切换 | [GitHub Copilot](../agents/github-copilot.md) |
| 我要一个开源、接近 Devin 路线的软件工程 agent | [OpenHands](../agents/openhands.md) |
| 我要把明确 issue 直接交给 agent 执行 | [Devin](../agents/devin.md) |
| 我要 review-first、任务板式、多次尝试对比 | [Froge Code](../agents/froge-code.md) |
| 我要一个开源本地 agent，带 desktop、CLI 和扩展能力 | [Goose](../agents/goose.md) |
| 我要长期自托管，还需要 memory、skills、messaging | [Hermes Agent](../agents/hermes-agent.md) |
| 我要 runtime、渠道、设备和更强控制面 | [OpenClaw](../agents/openclaw.md) |
| 我要快速搭自己的 agent，而不是买现成产品 | [LangChain](../agents/langchain.md) |
| 我要长期运行、有状态、可恢复 workflow | [LangGraph](../agents/langgraph.md) |

## 三步判断

1. 先决定你是要“直接用 agent”，还是“自己搭系统”。
2. 再决定你更在意“低运维托管”，还是“高控制自托管”。
3. 最后决定你要“agent 自主推进”，还是“人始终主导 review”。

## 最常见的路线

| 路线 | 代表项目 | 核心感觉 |
| --- | --- | --- |
| 本地协作型 | [Claude Code](../agents/claude-code.md), [Aider](../agents/aider.md) | 边聊边做，节奏快，操作感强 |
| 底层 agent 之上的工作流层 | [oh-my-claudecode](../agents/oh-my-claudecode.md), [oh-my-codex](../agents/oh-my-codex.md) | 保留 Claude Code 或 Codex 作为执行引擎，再往上叠可复用 orchestration |
| 编辑器中心工作流 | [Cursor](../agents/cursor.md), [Windsurf](../agents/windsurf.md) | 编辑器本身就是选型的一部分 |
| 云端委派型 | [Codex](../agents/codex.md), [Devin](../agents/devin.md), [Jules](../agents/jules.md) | 先交任务，再回来 review |
| 管理式后台路径 | [Claude Managed Agents](../agents/claude-managed-agents.md) | 更偏定时、后台、程序化 Anthropic 工作流 |
| review-first 自动化 | [Cline](../agents/cline.md), [GitHub Copilot](../agents/github-copilot.md), [Froge Code](../agents/froge-code.md) | 让 agent 很强，但把合并和节奏留给人 |
| 自建 / 自托管 | [OpenHands](../agents/openhands.md), [Goose](../agents/goose.md), [Hermes Agent](../agents/hermes-agent.md), [LangChain](../agents/langchain.md), [LangGraph](../agents/langgraph.md) | 灵活，但要自己承担环境和运维 |

## 关键取舍

| 项目 | 最值得看的优点 | 最需要接受的代价 |
| --- | --- | --- |
| Claude Code | 本地 loop 很顺，MCP、instructions、subagents 组合完整 | 权限、环境和节奏还是你自己管 |
| Aider | 终端里的 AI 结对编程依然贴着 git 走 | 模型配置和终端 ergonomics 还是要自己扛 |
| Claude Managed Agents | 更适合后台、定时和程序化运行 | 官方公开边界不是单一产品页 |
| Codex | 云端隔离、日志和测试证据很清楚 | 更偏异步，不如编辑器内 agent 即时 |
| oh-my-claudecode | 给 Claude Code 补上 teams、可复用 skills 和更强运行控制 | 你会多背一层工作流，而且仍然依赖 Claude Code |
| oh-my-codex | 给 Codex 带来更清晰的 clarify-plan-execute operating model | 配置更多、流程更重，而且最佳路径通常离不开 tmux |
| Cursor | 一个打磨完整的表面把编辑、委派、集成都串起来 | 产品边界更宽，而且闭源属性很明确 |
| GitHub Copilot | 本地、CLI、cloud 都能串起来 | 最佳体验更依赖 VS Code / GitHub |
| Cline | 编辑器内强能力 + 强审批 | 高频审批会带来摩擦 |
| Windsurf | AI 原生 IDE 的 in-flow 编辑体验很强 | 扩展生态更收敛，工作流也更有主张 |
| OpenHands | 开源路线完整，CLI / GUI / cloud 都能走 | 安装、Docker、模型配置成本更高 |
| Devin | 托管式执行很直接 | 自定义和控制边界更少 |
| Jules | GitHub 连接、托管云端执行、PR 回收路径清楚 | cloud-first，而且 API 边界还在演进 |
| Goose | 开源本地 agent，加 extensions、MCP 和共享配置 | 产品边界比纯 coding 更宽 |
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