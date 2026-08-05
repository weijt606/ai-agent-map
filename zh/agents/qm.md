# QM

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](qm.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/qm.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话判断：QM 是 Y Combinator 做的"多人协作 agent harness"——一个自托管的 agent，活在 Slack 和一个 web 应用里，给每个人*以及*每个房间各自独立的记忆、文件、keychain、权限、定时任务和常驻沙箱，而底下跑的 harness 由你选（Pi、OpenCode、Codex、Claude Code），不是它自带一个。

> **"多人"就是它的全部命题。** 大多数 agent 是按个人助理设计的，你可以硬撑着让它服务一整家公司。QM 反过来：基本单位是**作用域**（scope）——一个人、一个频道、一个群聊、一个项目——每个作用域自带状态和权限。这就是"一个 agent 装着所有人的上下文"和"一套部署、许多互相隔离的 agent"之间的区别。

> **贡献只收人写的文字，不收代码。** `CONTRIBUTING.md` 要求你把想改的东西用 `.txt` 或 `.md` 非正式地写进 `adrs/` 目录；如果维护者认可，*由他们*来实现。MIT 许可是真的，你可以自由 fork，但上游这棵树不是一个正常的 pull-request 项目。打算长期带补丁的话，先把这条读清楚。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | Y Combinator（`yc-software/qm`，qm.ycombinator.com） |
| 路线 | Agent harness 框架——多人 / 组织级作用域 |
| 开源 | MIT |
| 实现 | TypeScript 直接跑在 Node 上，HTTP 核心用 Fastify；Postgres 持久层；web UI 用 Vite + Lit；Slack 插件基于 Bolt |
| harness | 可插拔——Pi、OpenCode、Codex、Claude Code 驱动同一个 core |
| 表面 | Slack + web 应用，两边共享同一套身份和配置 |
| 适合 | 想要一套自托管 agent 部署服务全公司、同时保证按人隔离、并由管理员统一设定安全姿态的创业公司或团队 |
| 主要代价 | 才几天大；而且这是一套要运维的部署——Postgres、沙箱、连接器凭证，还得用你自己的云账号 |
| GitHub 仓库 | https://github.com/yc-software/qm |

## 什么时候选它

- 你要的是**给公司用的 agent，不是给一台笔记本用的**。每个员工拿到一个隔离的工作区，互不干扰；同一个 agent 也参与共享频道、群聊和项目。
- 你想让 agent 待在工作真正发生的地方。QM 把 Slack 和 web 应用都当一等表面，身份和配置在两边通用。
- 你想**不被单一厂商的循环绑死**。core 在设计上就是 harness 无关的——Pi、OpenCode、Codex、Claude Code 都是同一个接口背后的驱动，所以一套部署不会押注在"谁赢了 harness 之争"上。管理员还能决定哪些 harness 和模型可用。
- 你想要有作用域、可授权的 skill，而不是一个大家共用的 prompt 目录：skill 归属于作用域，可以按授权分享，要推广到全组织需要管理员批准，还能从 git 仓库导入 skill 包。
- 你想要后台工作是内建能力而不是外挂：cron 和 watch 按作用域在没人看着的时候跑。
- 你想自托管在自己的云账号里。`qm init --org <slug> --target <fly-or-aws>` 会脚手架出一个组织自有的部署仓库，依赖已发布的 `@yc-software/qm` 包，所以你根本不需要 checkout 源码就能跑起来。

## 什么时候不选它

- 你想要一个终端 coding agent。QM 不是那个东西，它是那个东西*上面*那一层。循环本身请看 [Claude Code](claude-code.md)、[Codex](codex.md)、[Grok Build](grok-build.md) 或 [jcode](jcode.md)——顺带一提，QM 可以驱动其中好几个。
- 你就一个人。多人那套机械——Postgres、作用域、keychain 视图、管理员姿态、按作用域的沙箱——在 n=1 时全是开销没有收益。[Pi](pi.md) 或 [OpenHands](openhands.md) 才是对的体量。
- 你需要经过验证的东西。这个仓库才几天大；在你自己跑通之前，把所有运维层面的说法都当作未经核实。
- 你需要把改动合回上游。见上面那条贡献说明——[OpenHands](openhands.md)、[Pi](pi.md)、[OpenHarness](openharness.md) 是收代码的。
- 你想要一个带支持合同的托管产品。每套 QM 部署都跑在运维方自己的云账号里，而且初始化过程刻意不生成部署 CI。

## 能力形态

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 多租户作用域 | 很强 | 人、频道、群聊、项目各自拥有记忆、文件、keychain 视图、权限、cron、web 应用和一个常驻沙箱 |
| harness 中立 | 很强 | Pi、OpenCode、Codex、Claude Code 在同一个接口背后；允许哪几个由管理员定 |
| 聊天表面触达 | 强 | Slack 插件（Bolt）由 core 在进程内启动并托管，加上一个共享身份与配置的 web 应用 |
| 审批与策略 | 强 | 三档组织级安全姿态，更小的作用域只能收紧不能放宽；另有预声明命令策略 |
| skill 与共享 | 强 | 作用域拥有 skill、按授权分享、组织级推广需管理员批准、可从 git 导入 skill 包 |
| 调度 | 强 | 按作用域的 cron 和 watch |
| 常驻环境 | 强 | 每个作用域的沙箱是一台持久的电脑——装过的工具会一直在 |
| 运维成熟度 | 未经验证 | 撰写时才几天大 |

## 值得知道的架构

每一轮对话都走一个**无头 core**，由它掌管身份、策略和调度；agent 循环是它背后一个可替换的驱动。Postgres 存会话、记忆和队列。agent 拿到的是一个小而固定的工具面，其中一个工具是 `execute`，在该作用域自己的沙箱里执行命令——那是它的常驻电脑。

web UI、管理面板和公开门户都是 core 的 HTTP API 之上的**可选插件**，Slack 则是一个可选的进程内插件，由 core 启动并监管。所有公司特有的东西——组织配置、自定义工具和 skill、沙箱镜像、基础设施——都住在一个独立的**部署目录**里而不是 core 里；而每一层基础设施（harness、会话存储、沙箱、记忆）都在接口背后，生产实现通过单个接线文件换进来。正是这种分离让"能升级"这件事显得可信：你的定制不是打在 core 上的 diff。

## 安全姿态

组织选定一档姿态，更小的作用域只能收紧：

- **Strict** — 每一次 harness 工具调用都暂停等人工批准，只有结束一轮的那两个无副作用调用除外。
- **Auto**（默认）— 一个分类器在带来源标记的外部数据和工具结果到达模型之前先做筛查；部署方可以把这一步指向自己的筛查代理。
- **Dangerous** — 不做内容筛查，工具调用之间也不暂停。

**预声明命令策略**——针对递归删除、破坏性 SQL 这类操作的批准规则和硬性拒绝——在每一档姿态下都生效，Dangerous 也不例外。QM 声明的模型和本地 coding agent 一样：agent 以它所服务的那个人的身份行事，用那个人的凭证和权限，做的每件事都留审计。威胁模型和已知限制写在 `SECURITY.md` 里；部署之前请读原文，不要只读上面这段摘要。

## 运维成本

中到高，而且是部署成本不是学习成本。你要在自己的 Fly 或 AWS 账号里跑一个 Postgres 支撑的服务、按作用域的沙箱、连接器凭证、Slack 应用配置和 web 登录。初始化流程会带着你走完这些并以一次线上验证收尾，部署仓库也确实全程不需要 checkout 源码——但这事怎么说都不是"一行装好"。如果你反而想把整个代码库放在一处，README 记录了一套**私有 fork** 做法（用裸克隆推到一个私有仓库，并且明确*不要*用 GitHub 的 Fork 按钮，因为公开仓库的 fork 没法改成私有，而且和原仓库共享同一个对象网络）。

## 结论

QM 是这张地图上第一个把"很多人、一套 agent 部署"当作设计问题本身、而不是事后补丁的项目，它给出的答案是作用域：按人和按房间隔离的状态与权限、一档由管理员设定的安全姿态、以及一个不关心循环由谁来跑的 core。它来得非常响——第一周大约 11.4k star、1.3k fork——但它才几天大，所以合理的读法是*架构有前途、运维未经验证*。想要一个自己拥有的单人循环，看 [Pi](pi.md)、[jcode](jcode.md) 或 [OpenHands](openhands.md)；这张地图上另一个元 harness——它优化的是"一个开发者在一个会话里混用多个 harness"而不是"一家公司共用一套部署"——见 [Omnigent](omnigent.md)。路线级的横向对比见 [agent harness 框架](../comparisons/agent-harness-frameworks.md)。
