# Paseo

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](paseo.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/paseo.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Paseo 是一个开源的"agentic development environment"，用一个 daemon 运行你已有的编程 agent（Claude Code、Codex、Copilot、OpenCode、Pi 等），每个 agent 一个独立 worktree，周围配上编辑器、终端、diff 和浏览器。桌面、手机、网页和 CLI 客户端都连到这个 daemon。Paseo 里的 agent 还能跨 provider 启动其他 agent 并和它们对话。它不自带模型，也不自带 agent。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 独立项目（`getpaseo/paseo`，paseo.sh）。LICENSE 里的版权方是 Mohamed Boudra；README 说它"built by one person and funded by the people who use it" |
| 路线 | 工作流 / 编排层，横跨多个 CLI agent，而不是叠在某一个之上 |
| 仓库 | [`getpaseo/paseo`](https://github.com/getpaseo/paseo)：TypeScript，截至 2026-11-27 共 25,917 star（仓库创建于 2025-10-13）。GitHub 显示的许可证是 `NOASSERTION`；LICENSE 文件写明除第三方组件外 Paseo "licensed under the Apache License, Version 2.0"，README 末尾也写 Apache-2.0 |
| 是否开源 | 是（Apache-2.0）。daemon、Expo 手机/网页客户端、Electron 桌面应用、CLI 和 relay 都在仓库里；官方 relay 服务端是另一个开源仓库 `getpaseo/paseo-relay` |
| 形态 | 一个本地 daemon（`packages/server`）加多个客户端：macOS、Windows、Linux 桌面应用，原生 iOS 和 Android 应用，网页 UI，`paseo` CLI（`npm install -g @getpaseo/cli`），TypeScript SDK（`@getpaseo/client`），以及 Docker 镜像 |
| Agent | 原生集成 Antigravity、Claude Code、Codex、fx、GitHub Copilot、Hoplite、Muse Code、Oh My Pi（默认关闭）、OpenCode 和 Pi；任何支持 [Agent Client Protocol](https://agentclientprotocol.com) 的 agent 都能通过通用适配器接入，应用内目录列出了 Cursor、Gemini CLI、Hermes Agent、Kimi、Qwen Code、goose 等 |
| 模型与计费 | 用你自己的 agent 订阅或 key。"you install the underlying CLI. Paseo runs it."provider 文档说 Paseo 不会为 Claude Code 或 Codex 额外收费，你套餐的正常额度照常适用 |
| 默认模型 | 自己没有。每个 agent 由你选 provider 和模型（例如 `paseo run --provider codex/gpt-5.5`），也可以存进 agent profile |
| 默认安全姿态 | daemon 监听 `127.0.0.1:6767`，没有密码；新安装默认关闭 relay；Paseo 的 agent 工具默认不注入（`injectIntoAgents: false`）。agent 以 provider 的模式启动：Claude Code 默认 `auto`（"Uses a model classifier to review permission prompts automatically"），走 Bedrock 或 Vertex 时为 `default`（"Always Ask"）；Codex 默认 `auto`（`on-request` 审批、`workspace-write` 沙箱） |
| 最适合 | 同时跑多个编程 agent（可能来自不同厂商）、想让它们在自己机器上的并行 worktree 里运行、能从手机上管、还能互相委派任务的开发者 |
| 主要代价 | 离开 localhost 后要维护并保护一个 daemon；自己没有记忆层；每周发好几个版本（2026 年 11 月 1 日到 27 日 GitHub 上发布了 19 个版本，其中 4 个是预发布） |

## 它是什么

README 把 Paseo 描述为"an open source agentic development environment for desktop, mobile, web, and CLI."架构是客户端/服务端："Paseo runs a local server called the daemon that manages your coding agents. Clients like the desktop app, mobile app, web app, and CLI connect to it."provider 是"the contract between Paseo and one external agent CLI"，agent 二进制在 daemon 所在的机器上"runs as a normal subprocess"。桌面端会自动启动 daemon。

围绕这些 agent，它配了：

- **工作区和 worktree**："Run many agents at once, each in its own worktree, on one machine or several."worktree 可以新开分支、检出已有分支或检出一个 PR，默认放在 `$PASEO_HOME/worktrees` 下。
- **开发工作流**："Edit files, review diffs, open pull requests, and run terminals, in split panes you arrange how you want"，桌面应用里还有内置浏览器。
- **编排**："Agents in Paseo can create worktrees, launch other agents, and talk to them, across providers."途径是 Paseo 工具（原生下发或走 MCP），或者在 shell 里调用 `paseo` CLI。
- **定时任务和 heartbeat**：schedule"starts a new agent for you on a cron cadence"；heartbeat"sends a recurring prompt back into one existing agent so it can reassess and continue the same conversation."
- **语音**：听写（默认开启）和语音模式（开启前默认关闭）。语音默认在本地运行，也可以选 OpenAI。
- **插件**：插件"run on the daemon and show up in every client you connect"，可以加界面、挂到 agent 生命周期上、回应权限请求，或新增一个 provider。
- **Hub**（可选）：一个独立服务，"sits above your daemons so external events, schedules, and webhooks can start agents on those machines"。触发来源包括 GitHub、Linear、Slack、Discord、定时任务和 webhook，触发器可以放在 `.paseo/triggers/*.yml` 里。Hub 开源、可自托管；另有托管版 Hub，提供免费的 Free 套餐和付费的 Pro 套餐。

## 什么时候选它

- 你在用不止一个编程 agent，或者同一个 agent 开多个会话，想让每个都有自己的 worktree，旁边配好 diff、终端和浏览器。
- 你想让 agent 跨厂商互相委派。文档的示例包括"先实现再审查"，以及用一个 agent 做规划再交给另一个；内置的 skill `/paseo-handoff`、`/paseo-advisor` 和 `/paseo-committee` 把这些打包好了。
- 你想在手机上用完整的应用。README 说"The mobile app is the full app, native on iOS and Android"，配对可以走端到端加密的 relay，也可以直连（TCP、Tailscale 或 SSH）。
- 你想在服务器或虚拟机上跑 agent，再从任何地方操作：`npm install -g @getpaseo/cli`、`paseo`，然后把客户端或 `paseo run --host` 指过去。
- 你想用脚本驱动 agent。CLI 和 TypeScript SDK 覆盖创建 agent、等待结果和追加指令。
- 你在意遥测。README 说"No telemetry, tracking, or forced login."

## 什么时候不选它

- 你只用一个 agent、一个终端，而且很满意。直接用 [Claude Code](claude-code.md)、[Codex](codex.md) 或 [OpenCode](opencode.md)。
- 你需要一个跨 agent 强制执行审批和预算的策略层。Paseo 会把每个 agent 自己的权限请求展示出来（在应用里、`paseo permit`，或 `respond_to_permission` 工具），但规则来自各 provider 的模式，而 Claude 的 `bypassPermissions`、Codex 的 `full-access` 这类模式会跳过提示。[Omnigent](omnigent.md) 和 [Paperclip](paperclip.md) 把审批和预算策略放在 agent 之上。
- 你希望 Paseo 本身给 agent 加沙箱。它不做：Hub 安全文档说 Hub"does not sandbox the coding agent process on your machine"，Docker 部分也提醒"Agents can still access whatever code and credentials you mount into the container."
- 你想要记忆层。Paseo 把记忆留给每个 agent 自己的配置和 skill。
- 你想通过贡献代码来影响产品方向。CONTRIBUTING 写明"Product, design, architecture, and workflow decisions remain with the maintainer"，并把专门的工作流引向插件。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 并行执行 | 很强 | 每个 agent 一个 worktree，可以在一台或多台机器上（本地、SSH、VPN、relay、Docker） |
| agent 覆盖面 | 很强 | 十个原生集成，外加任何 ACP agent；应用内目录另列了三十多个 |
| 交付面 | 很强 | 三个系统的桌面端、原生 iOS/Android、自托管网页 UI、CLI、TypeScript SDK、语音 |
| 协同多 agent | 强 | agent 能跨 provider 启动其他 agent、给它们发消息并收集结果；工具途径默认关闭，CLI 途径只需要 shell 权限 |
| 定时调度 | 强 | 应用、CLI 和 MCP 里都有 cron 定时任务和 heartbeat；可选的 Hub 提供事件触发 |
| 审查 | 强 | diff、编辑器、PR 和桌面浏览器在同一个工作区里 |
| 人工审批 | 中 | 待处理的权限请求可以在任何客户端、CLI 或 MCP 里回应；策略取决于各 provider 的模式，默认值偏向自动审查 |
| 记忆 | 弱 | 自己没有记忆；空闲 agent 一小时后被释放，下一条 prompt"resumes the same conversation" |
| 治理 | 中 | Apache-2.0，可以端到端自托管，有 `hub.execute` 这类明确的 daemon 权限；决策权在单一维护者手里 |

## 使用代价

起步低：下载桌面应用后"the daemon starts automatically"，前提是至少装好并登录一个 agent CLI。离开 localhost 后成本就上来了。默认情况下"anyone who can reach the daemon's listening address can connect"，所以文档要求绑定到网络地址之前先设密码，并且"Never bind to 0.0.0.0 without a password"。配对二维码或链接是信任锚点，文档要求"Treat the link like a password"。官方 Docker 镜像在容器内绑定 `0.0.0.0:6767`，所以发布端口前要设 `PASEO_PASSWORD`，并把 `/workspace` 挂载范围收紧。插件"unsandboxed with the daemon user's access on the daemon host"运行。接入 Hub 是另一个决定：登记 daemon"does not allow Hub to run agents"，要等你授予 `hub.execute`；而这项授权允许 Hub 设置"provider permission mode"，这些模式"can bypass interactive approval prompts"。

## 和本地图其他条目的关系

Paseo 和 [Orca](orca.md) 在同一条赛道上：一个运行你已有 agent 的工作台，每个 agent 一个 worktree，带桌面和手机客户端。Orca 内置的协调者/工作者编排标注为实验性、默认关闭；Paseo 把 agent 之间的委派写成核心功能，不过它的工具注入同样默认关闭。Orca 把权限交给每个 agent 自己的设置；Paseo 也依赖 provider 的模式，但会把待处理的权限请求转到它的客户端、CLI 和 MCP 工具上。对 [Paperclip](paperclip.md)，Paseo 是以工作区和对话来管理 agent，而不是一个带目标、预算和审计日志的组织。

## 结论

如果你已经在跑好几个编程 agent，想在一个地方让它们并排运行，在桌前或手机上都能管，还能让 agent 跨厂商互相交接工作，Paseo 很合适。它跑在你自己的机器上，不发遥测，采用 Apache-2.0。安全模型用的是 agent 自己的：Paseo 会转发它们的权限提示，但真正把关操作的是它的默认值（Claude 用分类器审查的 `auto`，Codex 用 `on-request` 加 workspace-write 沙箱）以及你或 Hub 选择的模式。在把它暴露到网络之前，先设好 daemon 密码。

## 来源

- [getpaseo/paseo README](https://github.com/getpaseo/paseo) · [LICENSE](https://github.com/getpaseo/paseo/blob/main/LICENSE) · [CONTRIBUTING](https://github.com/getpaseo/paseo/blob/main/CONTRIBUTING.md) · [Releases（v0.18.0，2026-11-27）](https://github.com/getpaseo/paseo/releases)
- 文档：[Why Paseo?](https://github.com/getpaseo/paseo/blob/main/public-docs/why.md) · [Security](https://github.com/getpaseo/paseo/blob/main/public-docs/security.md) · [Configuration](https://github.com/getpaseo/paseo/blob/main/public-docs/configuration.md) · [Providers](https://github.com/getpaseo/paseo/blob/main/public-docs/providers.md) · [Supported providers](https://github.com/getpaseo/paseo/blob/main/public-docs/supported-providers/index.md) · [Claude Code](https://github.com/getpaseo/paseo/blob/main/public-docs/supported-providers/claude-code.md) · [Codex](https://github.com/getpaseo/paseo/blob/main/public-docs/supported-providers/codex.md) · [Orchestration](https://github.com/getpaseo/paseo/blob/main/public-docs/orchestration.md) · [MCP reference](https://github.com/getpaseo/paseo/blob/main/public-docs/mcp.md) · [Schedules](https://github.com/getpaseo/paseo/blob/main/public-docs/schedules.md) · [CLI](https://github.com/getpaseo/paseo/blob/main/public-docs/cli.md) · [Voice](https://github.com/getpaseo/paseo/blob/main/public-docs/voice.md) · [Hub](https://github.com/getpaseo/paseo/blob/main/public-docs/hub/index.md) · [Hosted Hub](https://github.com/getpaseo/paseo/blob/main/public-docs/hub/hosted.md) · [Hub security](https://github.com/getpaseo/paseo/blob/main/public-docs/hub/security.md) · [paseo.sh/docs](https://paseo.sh/docs)
- 源码：[Claude provider 模式](https://github.com/getpaseo/paseo/blob/main/packages/server/src/server/agent/providers/claude/agent.ts) · [Codex provider 模式](https://github.com/getpaseo/paseo/blob/main/packages/server/src/server/agent/providers/codex-app-server-agent.ts)
