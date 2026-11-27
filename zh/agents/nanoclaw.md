# NanoClaw

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](nanoclaw.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/nanoclaw.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：NanoClaw 是一个自托管、常驻在线的助手，由一个小型 Node 宿主进程构成，每个 agent 会话都跑在自己的 Docker 容器里。默认情况下 agent 通过 Anthropic 的 Claude Agent SDK 运行 Claude，你从聊天应用里找到它们。它的卖点是靠容器隔离而不是靠权限检查，靠让 coding agent 改你自己的 fork 来定制，而不是靠配置。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | GitHub 组织 `nanocoai`（官网 [nanoclaw.dev](https://nanoclaw.dev)）。LICENSE 写的是"Copyright (c) 2026 Gavriel" |
| 路线 | 自托管 / 本地 runtime |
| 仓库 | [`nanocoai/nanoclaw`](https://github.com/nanocoai/nanoclaw)：MIT，TypeScript，截至 2026-11-27 共 31,172 star（仓库创建于 2026-01-31） |
| 是否开源 | 是（MIT）。README 说基础代码只接受"Only bug fixes, security fixes, simplifications and code reductions"；新能力以 skill 的形式贡献 |
| 形态 | 一个 Node 宿主进程加上按会话起的 agent 容器（macOS、Linux 或通过 WSL2 的 Windows 上的 Docker），用 `bash nanoclaw.sh` 安装。主干自带一个终端渠道；聊天应用渠道用 `/add-<channel>` skill 加。用 `ncl` CLI 管理 |
| 模型与计费 | 自带凭据，凭据存在 credential gateway 里而不是容器里。Claude 是默认 runtime；Codex（ChatGPT 订阅或 API key）、Cursor（Cursor 账号或 API key）和 OpenCode（OpenRouter、Google、DeepSeek、本地兼容 OpenAI 的服务等）可作替代，可按 agent group 分别配置。可选的免费 NanoClaw 账号能解锁预构建的加固镜像和托管 Slack 应用 |
| 默认模型 | 通过 Claude Agent SDK 跑 Claude。源码写的是"Model and reasoning effort pass to the SDK verbatim; the SDK owns defaults"，所以没设模型的 group 用 SDK 的默认值。Codex 方面，2026.11.0 的发布说明写道"Groups with no model set start new threads on GPT-6.1 Sol with an API key and on GPT-6.2 Sol with a ChatGPT login" |
| 最适合 | 想在自己的电脑上跑一个助手、在聊天应用里回话、跑定时任务，并且让每个 agent 的文件、记忆和 shell 都待在各自容器里的个人，或彼此信任的一群人 |
| 主要代价 | 你要运行 Docker、一个 credential gateway，以及一个预期要靠 coding agent 去改的 fork。agent 在容器内运行时没有逐工具的确认提示，除非打开 egress lockdown，否则出站网络是放开的 |
| 文档 | [docs.nanoclaw.dev](https://docs.nanoclaw.dev) · [仓库 docs](https://github.com/nanocoai/nanoclaw/tree/main/docs)（仓库里的架构文档标注为"Draft — design intent, not a line-by-line spec"） |

## 它是什么

README 这样描述它：*"An AI assistant that runs agents securely in their own containers. Lightweight, built to be easily understood and completely customized for your needs."* 架构上，"A single Node host orchestrates per-session agent containers."聊天应用来的消息由宿主路由到某个 agent group 和会话，写进该会话的 `inbound.db`，再由容器里的 agent-runner 取走。回复写进 `outbound.db`，宿主通过渠道适配器发回去。README 把这称为"Two SQLite files per session, each with exactly one writer"。

围绕这个循环，它配了：

- **工具**：容器内的 Claude Code 工具、MCP server、网页搜索与抓取，以及 agent 镜像里固定版本的 `agent-browser` CLI。agent 可以申请安装软件包或添加 MCP server，两者都要经过管理员审批。
- **记忆**：每个 agent group 都有"persistent, file-based memory: plain Markdown files"。记忆文档写明"There is no database and no embedding store."每次开启新的上下文窗口时会注入两个文件（`index.md` 和 `system/definition.md`），每个上限 16k 字符。其余部分由 agent 顺着链接自己维护。
- **定时任务**：一次性或按 cron 循环的任务，用 `ncl tasks` 或在聊天里管理。可以加可选的 script gate：一段决定要不要唤醒 agent 的 Bash 脚本，于是"`wakeAgent: false` completes the run without calling the model."
- **多 agent**：agent 之间通过 `send_message` 发给 agent 类型的目标来互相发消息；从 2026.11.0 起"Agents can create other agents from templates."有 NanoClaw 账号的话，每个 Slack agent 都能有自己的 Slack 应用；README 说你可以"Spawn teammates from chat: every one gets its own bot identity, container, and memory"。
- **隔离级别**：按渠道选择，可以给一个聊天单独的 agent group，可以让一个 agent 跨多个独立会话共用，也可以把多个渠道并进一个共享会话（[隔离模型](https://github.com/nanocoai/nanoclaw/blob/main/docs/isolation-model.md)）。

## 什么时候选它

- 你希望 agent 的 shell 和文件访问被容器限制住，而不是被应用内检查限制。安全文档说 agent 以非特权用户运行，"only explicitly mounted directories are visible"，而且"The project root is **never mounted**"。
- 你希望 API key 不落到 agent 手里。"Real API credentials **never enter containers**"。由 credential gateway（默认是 OneCLI 的 Agent Vault，也可选 Iron Proxy）按请求注入凭据，而且"with none registered the host refuses to start"。
- 你想要一个跨很多聊天应用的助手。README 列出了 WhatsApp、WhatsApp Cloud API、Telegram、Discord、Slack、Microsoft Teams、Mattermost、Signal、iMessage、Matrix、Google Chat、Webex、Linear、GitHub、微信、Delta Chat、Dial（短信和语音通话）、Emacs，以及通过 Resend 的邮件，每个都按需安装。
- 你想把不同人的聊天隔开。独立的 agent group 意味着"Separate containers, separate session databases, separate everything."
- 你不怕改代码。README 的立场是"Customization = code changes"，你要"make your own fork and have your coding agent modify it"。
- 你想默认用 Claude Code 的 harness，同时保留把某个 group 换到 Codex、Cursor 或 OpenCode 的选项。

## 什么时候不选它

- **你希望每条高风险命令前都有确认提示。** Claude provider 以 `permissionMode: 'bypassPermissions'` 运行。源码注释写道"Claude runs unrestricted inside the container: NanoClaw's container isolation and the credential gateway's allow-list are the security boundary, not the SDK's own permission prompts."审批卡片是有的，但只针对特权操作，比如默认 scope 的 group 创建 agent、安装软件包、添加 MCP server、被拦下的 agent 间消息，以及 gateway 被配置为拦截的带凭据请求。文档还补充："If the gateway has no rule asking for approval, the host side never fires"。
- 你需要默认的网络隔离。"**Default: egress is open.**"屏蔽其他出站流量要用 `NANOCLAW_EGRESS_LOCKDOWN=true` 主动开启。每个容器的 CPU 和内存上限也是"opt-in and unset by default"。
- 你不想被 Docker 和大约 4 GB 内存占着。Docker 是必需的，原生 Windows 不支持（只支持 WSL2）。
- 你想要配置文件和设置界面。README 说"core ships no monitoring dashboard or debugging UI"（可选的 `/add-dashboard` skill 能加一个），排查问题则让你去找 coding agent。
- 你希望开箱就完全没有遥测、也不碰厂商账号。没有账号时，安装和卸载的诊断信息会发到 PostHog，除非设置 `NANOCLAW_NO_DIAGNOSTICS=1`。安装程序问要不要打开账号门户时默认答案是 yes，要在本地构建镜像得答 no。
- 你想把新功能合进上游。基础代码只收修复和精简，其他一律以 skill 的形式发布。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 代码执行 / 隔离 | 很强 | 按会话的 Docker 容器、非 root、项目外的挂载白名单、凭据由 gateway 注入；egress lockdown 需主动开启 |
| 交付面 | 很强 | 主干自带终端渠道，通过 `/add-<channel>` skill 接 19 个聊天和消息渠道，有账号时可用托管 Slack 应用 |
| 工具调用 | 强 | Claude Code 工具、MCP server、网页、`agent-browser`、agent 模板；安装软件包和 MCP 要审批 |
| 多 agent | 强 | agent 间消息、agent 用模板创建 agent、每个 agent 一个 Slack 应用；默认 scope 下要等管理员审批 |
| 定时调度 | 强 | 一次性和 cron 任务、可跳过模型调用的 script gate、在聊天或 `ncl tasks` 里管理 |
| 记忆 | 中 | 每个 agent group 一套纯 Markdown 文件，带常驻加载的索引；由 agent 自己维护，没有单独的整理任务 |
| 人工审批 | 中 | 特权操作和 gateway 拦下的请求有管理员审批卡片；容器内没有逐工具审批 |
| 治理 | 中 | MIT、issue 开放，但基础代码只收 bug 修复、安全修复、简化和代码精简 |

## 使用代价

中等。安装是三条命令（`git clone`、`cd nanoclaw`、`bash nanoclaw.sh`），脚本会安装或更新 Node 和 pnpm、缺 Docker 时装上、装一个 credential gateway、拉取或构建 agent 镜像，并配对你的第一个渠道。某一步失败时，它可以交给 Claude Code、Codex 或 OpenCode 诊断后接着跑。之后你维护的是一个 fork。渠道和 provider 由 skill 复制进去，版本通过 `/update-nanoclaw` 走 `stable` 渠道更新，2026.11.0 的发布说明列了八项"need action from some installs"的变更，其中包括 gateway 升级和新的渠道设置。"first user to pair becomes owner"，owner 和 admin 会在私信里收到审批卡片。陌生发送者按每个聊天的 `strict`、`request_approval` 或 `public` 策略处理；每个渠道适配器各自声明默认值。卸载用 `bash nanoclaw.sh --uninstall`，它会"asks for confirmation per group"。

## 和本地图其他条目的关系

NanoClaw 和 [OpenClaw](openclaw.md)、[nanobot](nanobot.md)、[Hermes Agent](hermes-agent.md)、[Mercury Agent](mercury-agent.md) 在同一条自托管赛道上：一个归你所有的 runtime、多个聊天入口、记忆和定时任务。它自己的 README 拿 OpenClaw 作对照，说 OpenClaw 的安全"is at the application level (allowlists, pairing codes) rather than true OS-level isolation"；这是 NanoClaw 自己的说法，不是本地图的结论。对 [nanobot](nanobot.md)，两者都主打小内核（NanoClaw："Small enough to understand"；nanobot："Small core"），但边界不同。nanobot 的默认是"workspace-restricted access, not an OS sandbox"，而 NanoClaw 把每个会话放进容器、把 key 留在 gateway 里。nanobot 用 Dream 自动整理记忆；NanoClaw 把记忆维护交给 agent 自己。两者都没有在每次工具调用前放一道确认，而这正是 [Mercury Agent](mercury-agent.md) 围绕的那一层。

## 结论

如果你想要一个常驻在聊天应用里的助手，而且最在意 agent 能碰到什么，NanoClaw 很合适。每个会话跑在自己的容器里，只看得到挂载进来的文件夹，也永远拿不到你的原始 key。代价是 Docker、一个 gateway，以及一个要通过 coding agent 来改的 fork。agent 在容器内运行时没有逐工具的确认提示，出站流量在你打开 egress lockdown 之前也一直是放开的。在接入有其他人的聊天之前，先打开 lockdown，并设好挂载白名单和发送者策略。

## 来源

- [nanocoai/nanoclaw README](https://github.com/nanocoai/nanoclaw) · [LICENSE](https://github.com/nanocoai/nanoclaw/blob/main/LICENSE) · [CONTRIBUTING](https://github.com/nanocoai/nanoclaw/blob/main/CONTRIBUTING.md) · [CLAUDE.md](https://github.com/nanocoai/nanoclaw/blob/main/CLAUDE.md) · [Releases（v2026.11.0，2026-11-20）](https://github.com/nanocoai/nanoclaw/releases/tag/v2026.11.0)
- 文档：[Security](https://github.com/nanocoai/nanoclaw/blob/main/docs/SECURITY.md) · [Isolation model](https://github.com/nanocoai/nanoclaw/blob/main/docs/isolation-model.md) · [Memory](https://github.com/nanocoai/nanoclaw/blob/main/docs/memory.md) · [Scheduled tasks](https://github.com/nanocoai/nanoclaw/blob/main/docs/scheduled-tasks.md) · [Architecture（草稿）](https://github.com/nanocoai/nanoclaw/blob/main/docs/architecture.md) · [API details](https://github.com/nanocoai/nanoclaw/blob/main/docs/api-details.md) · [docs.nanoclaw.dev](https://docs.nanoclaw.dev)
- 源码：[Claude provider policy](https://github.com/nanocoai/nanoclaw/blob/main/container/agent-runner/src/providers/claude-config.ts) · [agent-to-agent guard](https://github.com/nanocoai/nanoclaw/blob/main/src/modules/agent-to-agent/guard.ts) · [container CLI tools](https://github.com/nanocoai/nanoclaw/blob/main/container/cli-tools.json)
