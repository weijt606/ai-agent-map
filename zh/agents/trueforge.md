# TrueForge

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](trueforge.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/trueforge.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话判断：TrueForge 是一个你**部署起来、然后用 HTTP 调用**的 agent harness，而不是一个你 fork 下来自己拥有的循环——模型调用、MCP 工具、`SKILL.md` 技能包、沙箱、审批、subagent、会话状态全部跑在一个 server 里，对外暴露聊天 UI、带 TypeScript SDK 的 REST API，以及一个可嵌入的 UI SDK。

> **这条路线上的第三种形态。** 单循环 harness（[Pi](pi.md)、[mini-swe-agent](mini-swe-agent.md)）**就是**那个循环，你靠 fork 来拥有它。元 harness（[QM](qm.md)、[Omnigent](omnigent.md)）在一套策略下驱动好几个别的循环。TrueForge 两者都不是：它只跑**一个**循环，但把这个循环当成一个前面挂着 API 的服务来跑。它优化的单位既不是一个仓库也不是一个人，而是**你产品的后端**。

> **它公开了可复现的成本数字，这条路线上几乎没人这么干。** TrueForge 用 DevRev Enterprise-Bench 里 14 个跨系统任务，在同模型、同 MCP server 的条件下把自己和 [Claude Managed Agents](claude-managed-agents.md) 以及 deepagents 做了对比，并把复现用的脚手架放在 `benchmark/` 里。这些数字要当作厂商自测来读——但值得读，因为把竞品的成本曲线摆到台面上，比它本该有的频率要罕见得多。

## 快速判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | TrueFoundry（`truefoundry/trueforge`，trueforge.dev）——2026 年 7 月底公开 |
| 路线 | Agent harness 框架——harness 即服务端 |
| 开源 | MIT；npm 包 `@truefoundry/trueforge` 及 `-core`、`-sdk`、`-ui`；带 Helm chart |
| 实现 | Node ≥ 22.14 上的 TypeScript |
| 核心思路 | harness 是一个可部署的 server，有三扇前门：聊天 UI、HTTP API + SDK、可嵌入 UI |
| 模型 | OpenAI、Anthropic、Google Gemini、目录里的其他 provider，或任意 OpenAI 兼容端点 |
| 工具 | 远程 MCP server，支持 header auth 或 OAuth（含在聊天里完成授权）；git 托管的 `SKILL.md` 技能包按需加载 |
| 隔离 | 沙箱即工具（目前是 Daytona，官方称计划接更多 provider），按需开；密钥留在 harness 里 |
| 部署 | 本地模式（单进程 + SQLite，`npx` 起）或托管模式（Postgres + Redis；Docker Compose、Helm 或 Railway），可选 OIDC |
| 适合 | 要把 agent 放进自家产品背后的团队——循环、沙箱、审批都当成自己运维的基础设施 |
| 主要代价 | 公开六周，版本还停在 0.x 的 release candidate；贡献者几乎全来自一家公司 |
| GitHub 仓库 | https://github.com/truefoundry/trueforge |

## 什么时候选它

- 你要**把 agent 嵌进一个产品**，而不是在终端里跑一个。主要接口是 HTTP API 和可嵌入的 `@truefoundry/trueforge-ui`；自带的聊天 UI 是顺手给的，不是重点。
- 你希望 **harness 是你自己运维的基础设施**。Postgres 和 Redis、一个 Helm chart、可选的 OIDC——这些都在说同一件事：它被设计成你集群里一个带登录的服务，不是笔记本上一个二进制。
- 你想要**用目录而不是代码来配置**。模型、MCP server、skill、沙箱都是一次性接好的，来自你可以覆写的 YAML 目录；agent 再从已接好的东西里挑。这和"每个 agent 各自声明自己的 provider"的常规框架假设有实打实的运维差别。
- 你希望**密钥不进沙箱**。代码与文件执行是作为一个**工具**隔离出去的，按需开，凭据握在 harness 手里，不交给模型的执行环境。
- 你希望**人工卡点是产品特性**而不是调试提示：工具审批、向用户提问、Generative UI 都渲染在你的用户看得到的那个聊天界面里。
- 你在意**上下文成本**，而且想看到推导过程。公开的对比里，TrueForge 跑 Opus 4.8 解出 10.7/14，**每次运行 $8.6 对 Claude Managed Agents 的 $11.8**，准确率相同；跑 GLM-5.2 解出 11.7/14，每次 **$3.0**——同模型下每次 370 万 token 对 deepagents 的 1650 万，官方把这归因于更少的工具调用（19 对 32–40）、延迟加载工具、以及用压缩而不是重放来管上下文。

## 什么时候不要选它

- **你想要一个编码 agent。** TrueForge 是用来**跑** agent 的，它不待在你的仓库里改文件。那种需求请看 [Claude Code](claude-code.md)、[Codex](codex.md) 或 [Pi](pi.md)。
- **你想要能读完的最小那个东西。** 它在这条路线上和 [mini-swe-agent](mini-swe-agent.md) 是两个极端。如果目标是一口气读懂一个完整循环，从那边开始。
- **你需要生产成熟度。** 2026 年 7 月底才公开，版本号是 `0.x`，当前 tag 还是 release candidate。README 自己就写明：本地模式默认没有登录，只该跑在 localhost 上。
- **你需要厂商中立的治理。** MIT、可 fork，但提交历史压倒性地来自 TrueFoundry 员工，而且 fork 过来的 PR 被要求只改源码，因为 SDK 由维护者在合并后重新生成。这是一家公司公开发布的项目，不是一个社区项目——这和 [eve](eve.md) 的风险不是同一种（那边是许可证开放但**部署**是锁定点），值得分开说。
- **你的隔离要求指名了 provider。** 沙箱目前跑在 Daytona 上；更多 provider 是"计划中"，不是已交付。
- **你要定时自治或多渠道交付。** 这里没有 cron 原语，也没有 Slack/Discord/Telegram 那套适配器——本地图上把这些当成框架职责的是 [eve](eve.md) 和 [QM](qm.md)。

## 能力形态

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 工具使用 | 很强 | 远程 MCP，支持 header auth 或 OAuth 与聊天内授权；目录化配置；延迟加载工具与 Code Mode，把工具面挡在上下文之外 |
| 代码执行 | 强 | 沙箱即工具，按需开；密钥握在 harness 手里而不是沙箱里 |
| 记忆 | 弱 | 会话状态与压缩属于持久性和上下文工程，不是记忆系统——这里没有任何东西会跨会话学习 |
| 编排 | 很强 | subagent、延迟加载工具、大结果外置、压缩、持久化会话 |
| 多 agent | 中等 | 一个 harness 内部的 subagent；它不像元 harness 那样驱动别的 harness |
| 人工审批 | 很强 | 工具审批与向用户提问都是一等公民，而且渲染在终端用户看到的界面里 |
| 定时调度 | 无 | 没有 cron 原语 |
| 交付面 | 中等 | 聊天 UI、HTTP API + TypeScript SDK、可嵌入 UI SDK——都是真交付面，但没有渠道适配器 |
| 部署控制 | 很强 | MIT，设计上就是自托管；本地 SQLite，或经 Docker Compose、Helm、Railway 上 Postgres + Redis，可选 OIDC |

## 值得知道的架构点

推导出其他一切的那个设计决定，是**把循环放到一条 API 边界后面**。一旦 harness 变成 server，会话状态就必须持久化而不能留在进程里，工具就必须集中声明而不能每次调用传进来，审批就必须能渲染给正拿着客户端的那个人看——这也是为什么审批是以 Generative UI 而不是终端提示的形式出现的。可大可小的两种模式也是同一个选择的副产品：本地模式就是同一个 server，只是把 Postgres 换成 SQLite、把登录去掉。

第二个值得抽出来的想法是**把目录当作配置单位**。模型、MCP server、skill、沙箱都是一次性接好的，来自你可以覆写的 YAML，agent 从可用的里面选。这把"agent 定义自带 provider 配置"的常规框架假设反了过来，也正是它让一个共享部署可治理的原因：任何 agent 够得着的东西集合，是运维的决定，不是开发者的决定。

第三，对一个这么年轻的项目来说，它的上下文工程写得异常明确——**延迟加载工具、Code Mode、大结果外置、以及用压缩而非重放**都是被点名的特性，而 benchmark 把大部分成本差距归因于的正是这几条。不管那些公开数字在你的负载上是否站得住，把成本故事讲成一套机制而不是一句主张，才是有用的那部分。

## 运维成本

中等，而且它对此很诚实。`npx @truefoundry/trueforge@latest` 不需要任何基础设施就能跑起来，但那条路被明确说了不是部署方式——只要不止一个人用，你就要跑 Postgres、Redis 和一个 OIDC provider，外加一个沙箱 provider 的账号。相对地，持续的模型开销正是这个项目拿来竞争的那个数字，而且它公开了可复现的脚手架供你自己核。要给运维留预算，而不是给循环留：循环正是 TrueForge 替你接过去的那部分。

## 结论

TrueForge 回答了 harness 路线此前只是顺带回答过的一个问题：**如果你想拥有循环，但不想把它托管在自己的终端里，怎么办？** 单循环 harness 给你一个可以 fork 的东西；元 harness 给你一层管住好几个循环的策略；TrueForge 给你一个跑着的服务，带 API、带登录、带你的用户看得见的审批界面。这让它成为"agent 是你产品的一个功能"而不是"agent 是你机器上的一个工具"时的自然选择——也是这条路线上唯一一个用可复现的成本对比而不是功能清单来立论的条目。掂量它的时候要掂量年龄和单一公司的贡献者结构，而不是许可证：MIT 不等于社区治理。路线级视角见 [agent harness 框架](../comparisons/agent-harness-frameworks.md)与[能力矩阵里的 harness 行](../capabilities/matrix.md#自己掌控循环的-harness-框架)。想要框架而不是服务端，看 [eve](eve.md)；想把状态图握在自己手里，看 [LangGraph](langgraph.md)。
