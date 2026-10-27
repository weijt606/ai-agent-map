# Paperclip

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](paperclip.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/paperclip.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：Paperclip 是一个开源、自托管的控制平面，用公司管员工的方式管一支 AI agent 团队。agent 有职位、汇报关系和预算；工作以挂在目标下的工单形式下发；周期性工作按计划自动跑；审批、花费上限和审计日志压在最上面。它不负责造 agent。你把 Claude Code、Codex、OpenClaw、Hermes 或任何"can receive a heartbeat"的 agent 带进来，Paperclip 管的是它们所在的那个组织。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | Paperclip Labs, Inc.（`paperclipai/paperclip`，paperclip.ing） |
| 路线 | 工作流 / orchestration layer，围绕工单和组织架构组织，而不是围绕单个 agent 的会话 |
| 仓库 | [`paperclipai/paperclip`](https://github.com/paperclipai/paperclip)：MIT，TypeScript，截至 2026-10-28 共 107.9k star |
| 开源 | 是（MIT）。"Open source. Self-hosted. No Paperclip account required." |
| 形态 | Node.js 服务端 + React 网页界面 + 内嵌 PostgreSQL；用 `npx paperclipai@latest onboard --yes` 或 Docker 安装 |
| 支持的 agent | 有 OpenClaw、Claude Code、Codex、Cursor（及 Cursor Cloud）、Gemini CLI、OpenCode、Pi、Hermes（及 Hermes Gateway）、Grok Build、Kimi Code 的适配器，另外支持自定义进程、HTTP 端点和适配器插件 |
| 模型 | 每个 agent 单独选；从 `v2026.1023.0` 起，agent 也可以走你自己的网关（OpenRouter、Amazon Bedrock、Google Gemini，或任何 OpenAI Responses、Anthropic Messages、Chat Completions 端点） |
| 托管版 | README 链了一个"Paperclip Cloud"候补名单；官网没有写价格，README 路线图把"Cloud deployments"标为进行中 |
| 适合谁 | 有很多 agent 在跑持续性工作（写代码，也包括调研、运营、内容）、需要搞清楚谁在做什么、花了多少、哪些要人签字的人 |
| 主要代价 | 要运维一个服务端和一个数据库，要学一套新概念（公司、心跳、routine、治理），而且新版本经常带破坏性变更 |

## 它是什么

README 的描述是"a Node.js server and React UI that orchestrates a team of AI agents to run a business"，接着说："It looks like a task manager. Under the hood: org charts, budgets, governance, goal alignment, and agent coordination." 它宣传的流程是三步：定一个目标，按职位"招聘"一组 agent（CEO、CTO、工程师、市场），然后审批策略、设定预算，在仪表盘上盯着。

README 对自己不是什么也说得很直白："Not an agent framework. We don't tell you how to build agents. We tell you how to run a company made of them." agent 自带 prompt、模型和运行时。

## 它怎么运作

- **任务与目标**：工作以 issue 跟踪，挂在项目、父任务和公司目标之下，这样"agents see the 'why,' not just a title"。单一负责人加执行锁（"atomic task checkout"）防止两次运行抢同一个任务。
- **心跳**：agent 不是一直在跑。一个基于数据库的唤醒队列会在有指派的工作、后续消息或可选定时器到来时叫醒 agent，检查预算、准备工作区和密钥、加载 skill，再调用适配器。
- **Routine**：周期任务，支持 cron、webhook 和 API 触发，以及并发和补跑策略。每次运行都会生成一个可追踪的 issue 并叫醒被指派的 agent。
- **治理**：董事会式审批流程、任务上的评审和审批阶段、新"员工"入职审批，以及对任何 agent 的暂停、恢复或终止。配置变更有版本记录，可以回滚。
- **成本控制**：按公司、agent、项目、目标、供应商和模型统计 token 和花费，可设预警阈值和硬性上限。README 也写明，执行依据的是已记录的花费，所以"usage reporting and in-flight work can delay a stop"。
- **连接与工具**：GitHub、Notion、Railway 或你自己的 MCP 服务器，都挂在一个工具网关后面，每个动作可设为 Allowed、Ask first 或 Off。
- **工作区**：项目仓库，可选隔离的 git worktree，以及把 agent 跑到本机之外的沙箱供应商（路线图点名了 e2b、Cloudflare、Daytona、Modal、Novita 和自托管 Kubernetes）。
- **多组织**：一个部署可以承载多家公司，各自的任务、agent、权限和历史互相隔离；一个组织可以打包导出、再导入。

## 什么时候选它

- 你有很多 agent 在跑周期性或长期的工作，已经理不清了。README 自己举的例子是"20 simultaneous Claude Code terminals open"。
- 你想要能让 agent 停下来的花费上限，而不是月底才看到账单。
- 你希望人只在定好的节点介入（计划审批、任务评审、有风险的工具调用），而不是每一步都盯着。
- 你的 agent 不只写代码：客服、报表、调研或社媒发帖按计划跑，有负责人、有可查的历史。
- 你想在一个团队里混用不同 harness 和模型，同时不管是哪个 agent 干的活，任务、skill、权限和历史都放在同一处。

## 什么时候不选它

- 你只想看几个 coding agent 在 worktree 里并排干活、评审它们的 diff。那是工作台，不是公司：看 [Orca](orca.md)。
- 你需要一个框架来写 agent 自己的循环。Paperclip 说了自己不是；看 [agent harness 框架](../comparisons/agent-harness-frameworks.md)这条路线。
- 你想让单个 agent 自己变强。直接用 agent（[Claude Code](claude-code.md)、[Codex](codex.md)、[OpenClaw](openclaw.md)），或者给它配专门的增强层（[oh-my-claudecode](oh-my-claudecode.md)）。
- 你要的是作为功能的长期 agent 记忆。路线图上"Memory / Knowledge"还标着进行中；现在有的是持久化的任务上下文和会话恢复。
- 你今天就要托管服务。Paperclip Cloud 还在候补名单阶段。

## 能力形态

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 工作编排 | 非常强 | 挂在目标下的工单、原子领取、阻塞依赖、沿组织架构委派 |
| 治理与审批 | 非常强 | 审批阶段、入职审批、Ask first 工具网关、带版本可回滚的配置 |
| 调度 | 非常强 | 支持 cron、webhook、API 触发的 routine；定时心跳 |
| 多 agent | 非常强 | 人和 agent 混编的组织架构，多 harness、多模型团队 |
| 成本控制 | 强 | 分范围的预算，带预警和硬上限，依据已记录的花费 |
| 执行 | 中 | 有 worktree 和沙箱供应商，但实际干活发生在各适配器背后的 agent 里 |
| 交付界面 | 中 | 网页界面可在手机上用；Slack、Discord、Telegram、AgentMail 连接器还是 experimental；暂无桌面应用（在路线图上） |
| 记忆 | 弱 | 持久化任务上下文和会话恢复；记忆与知识在路线图上 |

## 使用成本

中。本地起步只要一条命令加一个内嵌 Postgres，默认是受信任的本机回环模式。生产环境意味着自己的 Postgres、认证模式，再加私有网络绑定（README 建议 Tailscale）或 Docker。需要 Node.js 24.11+；用 Claude 和 Codex 订阅登录，还需要主机上有 Python 3 和对应供应商的 CLI。版本按日期命名、发得很勤，最近几版开头都是破坏性变更：`v2026.1012.0` 要求升级前停掉所有旧进程，`v2026.1023.0` 扩大了 Operator 角色的权限。每次升级前都要读发布说明。匿名使用遥测**默认开启**；设 `PAPERCLIP_TELEMETRY_DISABLED=1` 或 `DO_NOT_TRACK=1` 可以关掉。

## 结论

Paperclip 把一群 agent 当成管理问题来处理：谁负责哪个任务、为什么要做、能花多少、谁来签字。如果你手上的 agent 已经能干活，卡住你的是协调、成本和问责，它给你的是一个自托管的 MIT 服务端，不需要厂商账号。如果你的问题是让一个 agent 写代码更强，它就是放错了层。长期记忆还在路线图上，托管版也还在候补名单阶段。

## 来源

- [paperclipai/paperclip README](https://github.com/paperclipai/paperclip) · [LICENSE](https://github.com/paperclipai/paperclip/blob/master/LICENSE) · [Releases（v2026.1023.0，2026-10-23；v2026.1012.0）](https://github.com/paperclipai/paperclip/releases)
- [paperclip.ing](https://paperclip.ing) · [Cloud 候补名单](https://paperclip.ing/waitlist/) · 文档：[Approvals](https://docs.paperclip.ing/guides/day-to-day/approvals/) · [Costs](https://docs.paperclip.ing/guides/day-to-day/costs/) · [Routines](https://docs.paperclip.ing/guides/projects-workflow/routines/) · [Deployment modes](https://docs.paperclip.ing/reference/deploy/deployment-modes/) · [Adapters](https://docs.paperclip.ing/reference/adapters/overview/)
