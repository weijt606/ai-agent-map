# T3 Code

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](t3-code.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/t3-code.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：T3 Code 是一个开源的控制面，管的是你已经装好的那些编码 agent。你机器上的一个 server 驱动 Claude Code、Codex 和另外八个点了名的 agent（外加任何 ACP agent），桌面、网页和手机客户端看到的是同一批 thread。它自己不带 agent；FAQ 里直说 T3 Code 不是 harness。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | T3 Tools, Inc.（GitHub 组织 `pingdotgg`；官网 [t3.codes](https://t3.codes)）。LICENSE 里的版权方是"T3 Tools Inc." |
| 路线 | 工作流 / 编排层，横跨多个编码 agent，而不是叠在某一个之上 |
| 仓库 | [`pingdotgg/t3code`](https://github.com/pingdotgg/t3code)：MIT，TypeScript，截至 2026-11-27 共 81,794 star（仓库创建于 2026-02-08） |
| 是否开源 | 是（MIT），但 README 说许可证"applies **only to the source code**"；fork 必须换成自己的品牌。贡献方面："Small, focused fixes are the most likely to be merged. Features need an approved discussion first." |
| 形态 | macOS、Windows、Linux 桌面应用；一个 `t3` CLI，启动 server 并打开网页版；托管网页客户端 `app.t3.codes`；iOS 和 Android 应用 |
| Agent | Claude Code、Codex、Cursor、OpenCode、Grok Build、Antigravity、Kiro、Pi、Muse Code、fx，"and any [ACP](https://github.com/pingdotgg/t3code/blob/main/docs/user/providers-acp.md) agent"（GitHub Copilot 通过 ACP Registry 添加） |
| 模型与计费 | 用你自己的订阅或 key："T3 Code does not resell tokens." FAQ 对"How much does T3 Code cost?"的回答是"Nothing. You pay your own model/agent providers." 额外的 provider 实例可以用 API key 或 OpenRouter |
| 默认模型 | T3 Code 会自己设定 Codex 的默认：`DEFAULT_MODEL = "gpt-6-astra"`，并把默认挪到账号里能用的 `gpt-6-astra`、`gpt-5.6-sol`、`gpt-5.6-terra` 中的第一个，三个都没有时才用 Codex 自己的默认。Claude 兜底用 `claude-opus-5-5`；其他 provider 沿用各自会话或账号的模型。源码里默认启用的 provider 实例是 Codex 和 Claude，其余八个 driver 默认关闭；之后新 thread 沿用"your last provider, model, and options"。后台文字任务（标题、commit、PR 文案）默认用 Codex 实例的 `gpt-6-luna`，推理强度 low |
| 默认安全姿态 | 新 thread 默认 **Full access**（"Runs commands and edits without approval prompts"；源码里 `DEFAULT_RUNTIME_MODE = "full-access"`）。SECURITY.md：environment "is not a sandbox"，全权限会话"equals a shell as the server's OS user"，并且"is the default grant"。新装的后台服务"bind to localhost only" |
| 最适合 | 已经在用 Claude Code 或 Codex（或两个都用）、想在自己的机器上用一个界面管并行 worktree thread、跨 agent 委派和手机审批的开发者 |
| 主要代价 | 开箱模式就是不弹审批，审批得你自己打开；主机必须保持唤醒；版本还在 1.0 之前且发得很勤，好几项功能（workflows、linked environments、guest links）放在 Labs 里 |
| 文档 | [User guide](https://github.com/pingdotgg/t3code/blob/main/docs/user/README.md) · [全部文档](https://github.com/pingdotgg/t3code/blob/main/docs/README.md)（在仓库里） |

## 它是什么

README 开头这样写：*"The open-source control plane for coding agents."* 以及 *"T3 Code runs the coding agents on your machine and gives them one fast interface. Start a thread at your desk, then approve the next step from your phone."* 用户指南把它分成主机和客户端："A T3 Code **server** runs on the machine that holds your code and provider CLIs (your laptop, desktop, workstation, or VPS). Your desktop app, browser, and phone are **clients** connected to one or more environments."

FAQ 划清了它和 harness 的界线："A harness turns an LLM into an agent (tools, execution loop, and results)—like Claude Code's Agent SDK or Codex App Server. T3 Code drives those harnesses through one fast interface; it does not work without at least one installed agent."

围绕这一层，它配了：

- **Thread 与 worktree**：每个任务一个 thread；**New worktree** 给它"an isolated Git branch and working directory so multiple agents can work in parallel"。在新 thread 里 `Shift`-点选多个模型，会"starts a separate thread and worktree for each model."
- **跨 agent 协作**："Change models in the middle of a thread. Let Claude hand a task to Codex." agent 可以调用 `delegate_task`，在另一个 provider 或模型上、在隔离的 worktree 里、或在 linked machine 上开一个 subagent。
- **审查与源码管理**：按 turn、未提交、分支和 commit 看 diff；行内审查评论可以一条消息发回给 agent；一键 commit、push 和开 pull request。源码管理指南列出了 GitHub、GitLab、Forgejo/Gitea、Bitbucket、Azure DevOps、GitCafe、Cursor Origin，以及 Linear 和 Jira 的 issue。
- **工作区工具**：集成终端、带元素拾取器的内置浏览器、Devices 面板里的 iOS 模拟器和 Android 模拟器，以及语音输入。
- **自动化**：定时任务和 webhook 触发的任务，外加 **Workflows**（Labs），文档的描述是"durable TypeScript scripts that chain agents, code steps, schedules, webhooks, issue/PR triggers, and human approvals into multi-stage runs that survive server restarts."
- **给外部 agent 的 MCP 端点**：Claude Code、Codex、ChatGPT 或"any OAuth-capable MCP client"可以读取项目和 thread，授权到 Supervised 及以上时还能启动、发消息和停止 thread。

## 什么时候选它

- 你已经按订阅在用 Claude Code 或 Codex（或两个都用），想把它们放在一处。README 原话："It drives the agents you are already signed in to."
- 你想用手机指挥 agent。FAQ 列出了"Approve steps, review PRs, and steer threads from iOS and Android"，远程访问可以走 T3 Connect、局域网、Tailscale 或桌面端托管的 SSH。
- 你想让一个 agent 把活交给另一个。`delegate_task` 可以指定另一个 provider 或模型，而且"A delegated subagent can never exceed its parent thread's permission mode."
- 你在家用服务器或 VPS 上跑 agent。`t3 service install` 能在 Linux、macOS 或 Windows 上把它装成后台用户服务，负载均衡可以把新 thread 分到已连接的多台机器上。
- 你需要管理员来设上限。managed policy 可以为一台机器上的所有用户"set defaults, lock settings, and restrict capabilities (such as maximum permission mode, allowed providers, or remote access)"。

## 什么时候不选它

- **你期望它默认先问再动手。** 新 thread 默认是 **Full access**。你可以切到 **Supervised**、**Auto-accept edits** 或 **Auto**，但每种模式怎么执行取决于 provider："Providers enforce permissions differently, and some read-only actions proceed even in **Supervised**"。Muse Code 和 Kiro 只提供 Supervised 和 Full access。
- 你想要一道隔离边界。SECURITY.md 说 environment "is not a sandbox: it intentionally runs agents and terminals with that user's privileges."
- 你想用本地模型。FAQ："Does T3 Code support local models? No. T3 Code focuses on frontier coding agents." 本地兼容 OpenAI 的端点只用于 thread 标题这类轻量文字生成。
- 你的主机会休眠。"If the host machine sleeps or shuts down, agents pause until it wakes"，workflow run 也"only advance while the server that started them is online."
- 你需要记忆层。T3 Code 保存 thread、导入近期的 Claude Code、Codex 和 Pi 对话，并在切换 provider 时带上上下文，但记忆留在各个 agent 自己那里；rewind "cannot undo external actions or separate provider memory."
- 你需要稳定的接口。从 v0.1.8（2026-11-09）到 v0.1.13（2026-11-26）发了六个稳定版，中间还夹着 nightly；单是 v0.1.13 就写着"401 changes from 52 contributors"。
- 你只想在一个终端里用一个 agent。直接用 [Claude Code](claude-code.md)、[Codex](codex.md) 或 [OpenCode](opencode.md)。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 并行执行 | 很强 | 每个任务一个 thread，每个 thread 可选独立 worktree，一个 prompt 同时跑多个模型，本地、SSH 或 linked 主机 |
| Agent 覆盖面 | 强 | 十个点名的 provider 加 ACP Registry；每个都要在主机上单独安装和登录 |
| 交付面 | 很强 | 三个系统的桌面端、带网页版的 `t3` CLI、`app.t3.codes`、iOS 和 Android，以及一个 MCP 端点 |
| 协同多 agent | 强 | `delegate_task` 可跨 provider、worktree 和 linked machine；持久的多阶段 workflow 在 Labs 里 |
| 审查 | 强 | 按 turn 和分支看 diff、行内审查评论发回 agent、一键 PR、支持多家源码托管 |
| 定时调度 | 中 | Settings 里的定时任务和 webhook 任务；workflow 的定时和 issue/PR 触发（Labs）；主机必须在线 |
| 人工审批 | 中 | 四种权限模式、手机端审批、低于 Full access 时的 push hook 确认、workflow 的 `ask`；但默认是 Full access，执行方式因 provider 而异 |
| 记忆 | 弱 | thread、会话导入和上下文交接；没有自己的记忆层 |
| 治理 | 中 | MIT、managed policy、限定 scope 的 token 和设备审批；fork 受商标限制，贡献政策收得很窄 |

## 使用代价

起步低：下载桌面应用、`brew install --cask t3-code`，或者 `curl -fsSL https://t3.codes/install.sh | sh` 后运行 `t3`。另一个前提是在同一台机器上有一个"installed and signed in"的 agent，比如 `claude auth login` 或 `codex login`。远程用起来成本就上来了。新装的后台服务只监听 localhost；`t3 up --lan` 会开放局域网和 Tailscale 地址，此时"Anyone on that network can reach the port (gated by pairing)"。用 T3 Connect 时，"By default, any device signed into your T3 Connect account can connect"，直到你打开 **Require approval for new devices**；文档要求"Treat pairing URLs and codes as passwords"。免费的 T3 Connect 账号最多关联 3 台主机，关联付费的 T3 Chat 账号可以提高这个上限。代码和 prompt"go directly from your machine to your chosen provider"；T3 Connect 的流量走 Cloudflare 隧道，T3 的 relay "coordinates the link without proxying your HTTP/WebSocket sessions"。产品使用事件（provider、模型、token 总量，不含 prompt 和文件内容）默认发送，设 `T3CODE_TELEMETRY_ENABLED=false` 或 `DO_NOT_TRACK=1` 才关闭。

## 和本地图其他条目的关系

T3 Code 和 [Orca](orca.md) 在同一条赛道上：MIT 的桌面应用加手机伴侣，在并行 worktree 里跑你已经付费的 CLI agent，自己不带 agent。Orca 的条目把它描述成一个编辑器形态的工作台，其 coordinator/worker 编排是实验性的、默认关闭；T3 Code 是 client/server 结构的控制面，agent 之间的委派在文档里是常规功能，持久的 workflow 引擎才是 Labs 那一块。在审批上两者路子不同：Orca 把权限交给每个 agent 自己的设置，T3 Code 则按 thread 设一个权限模式并映射到各个 provider，默认是 Full access。想把 agent 当成一个有目标、预算和审计日志的组织来管，看 [Paperclip](paperclip.md)；想在每个 harness 前面加审批和花费策略，看 [Omnigent](omnigent.md)。

## 结论

如果你已经在跑 Claude Code 或 Codex，想在自己的硬件上用一个快速的界面管并行 thread、跨 agent 交接、审查和手机审批，T3 Code 很合适。它不是 agent，不是沙箱，也不是记忆层。默认值偏向速度：新 thread 跑在 Full access 下，全权限客户端就等于主机上的一个 shell。在让它碰任何重要的东西之前，先改默认权限模式、打开新设备审批，并考虑上一份 managed policy。

## 来源

- [pingdotgg/t3code README](https://github.com/pingdotgg/t3code) · [LICENSE](https://github.com/pingdotgg/t3code/blob/main/LICENSE) · [SECURITY.md](https://github.com/pingdotgg/t3code/blob/main/SECURITY.md) · [Releases（v0.1.13，2026-11-26）](https://github.com/pingdotgg/t3code/releases) · [t3.codes](https://t3.codes)
- 源码默认值：[`providerPolicy.ts`](https://github.com/pingdotgg/t3code/blob/main/packages/contracts/src/providerPolicy.ts) · [`settings.ts`](https://github.com/pingdotgg/t3code/blob/main/packages/contracts/src/settings.ts) · [`model.ts`](https://github.com/pingdotgg/t3code/blob/main/packages/contracts/src/model.ts)
- 文档：[User guide](https://github.com/pingdotgg/t3code/blob/main/docs/user/README.md) · [FAQ](https://github.com/pingdotgg/t3code/blob/main/docs/user/faq.md) · [Install](https://github.com/pingdotgg/t3code/blob/main/docs/user/install.md) · [Permission modes](https://github.com/pingdotgg/t3code/blob/main/docs/user/permission-modes.md) · [Remote access](https://github.com/pingdotgg/t3code/blob/main/docs/user/remote-access.md) · [Subagents](https://github.com/pingdotgg/t3code/blob/main/docs/user/subagents.md) · [Workflows](https://github.com/pingdotgg/t3code/blob/main/docs/user/workflows.md) · [Project settings](https://github.com/pingdotgg/t3code/blob/main/docs/user/project-settings.md) · [Outside agents](https://github.com/pingdotgg/t3code/blob/main/docs/user/outside-agents.md) · [Managed policy](https://github.com/pingdotgg/t3code/blob/main/docs/user/managed-policy.md) · [Background service](https://github.com/pingdotgg/t3code/blob/main/docs/user/background-service.md) · [Composer](https://github.com/pingdotgg/t3code/blob/main/docs/user/composer.md) · [Diffs](https://github.com/pingdotgg/t3code/blob/main/docs/user/diffs.md) · [Telemetry](https://github.com/pingdotgg/t3code/blob/main/docs/user/telemetry.md)
