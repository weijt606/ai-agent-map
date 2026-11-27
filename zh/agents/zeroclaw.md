# ZeroClaw

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](zeroclaw.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/zeroclaw.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：ZeroClaw 是一个自托管的 agent runtime，以单个 Rust 二进制发布，用一个 TOML 文件配置。一个 agent 可以同时在聊天应用、邮件、语音、webhook、Web 管理面板和终端客户端里回话，并通过 shell、浏览器、HTTP、MCP 和硬件工具干活。它最有辨识度的选择是默认安全姿态：autonomy 为 `supervised`，中风险操作会在发起对话的那个渠道里等你批准。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | ZeroClaw Labs。README 写明原作者为 @theonlyhennygod、项目负责人为 @JordanTheJet，并称项目"Built and maintained by the community" |
| 路线 | 自托管 / 本地 runtime |
| 仓库 | [`zeroclaw-labs/zeroclaw`](https://github.com/zeroclaw-labs/zeroclaw)：Rust，截至 2026-11-27 共 33,639 star（仓库创建于 2026-02-13）。GitHub 显示的许可证是 Apache-2.0；仓库同时带 `LICENSE-MIT` 和 `LICENSE-APACHE`，README 写的是"Dual-licensed: MIT OR Apache 2.0. You may choose either." |
| 是否开源 | 是。较大的改动走 RFC 流程，贡献者要签 CLA，并且"AI-assisted PRs are welcome"。ZeroClaw 的名称和 logo 是 ZeroClaw Labs 的商标 |
| 形态 | 一个二进制（`zeroclaw`），包含 daemon、HTTP/WebSocket gateway 与 Web 管理面板（`http://127.0.0.1:42617`）、`zerocode` 终端界面、聊天渠道，以及面向编辑器的 ACP；`zeroclaw service install` 会把它注册为 systemd、launchctl 或 Windows Service |
| 模型与计费 | 自带 provider：Anthropic、OpenAI、Ollama，"or any OpenAI-compatible endpoint"，支持 fallback 链和路由。文档写了 OpenAI Codex（读取 Codex CLI 的 `auth.json`）和 Claude Max（`claude setup-token`）的订阅登录方式。文档自称"Not a SaaS. There's no hosted version, no account system, no billing." |
| 默认模型 | 你选之前没有：`zeroclaw quickstart` 里的 **Model provider** 一步是必填的，负责设定 provider、它的 key 或 endpoint，以及模型。文档自己的示例用的是 `gpt-5.4` 和 `claude-sonnet-4-5` |
| 默认安全 | autonomy 为 `Supervised`，workspace-only 为 `true`，操作系统沙箱自动探测，OTP 关闭；gateway 绑定在 `127.0.0.1`，客户端必须先配对（默认 `require_pairing = true`） |
| 最适合 | 想在自己的笔记本、服务器或单板机上跑一个常驻个人 agent、能从很多渠道找到它、并且默认就开着审批关卡的人 |
| 主要代价 | 配置面很大（provider、agent、risk profile、runtime profile、渠道都是 `<type>.<alias>` 形式的表）。`zeroclaw estop`"is not a safety control today"，命令执行不做审计，Windows 上没有操作系统级沙箱后端 |
| 文档 | [docs.zeroclaw.com](https://docs.zeroclaw.com/master/en/introduction.html) · [仓库 docs](https://github.com/zeroclaw-labs/zeroclaw/tree/master/docs/book/src) · [zeroclaw.com](https://www.zeroclaw.com/) |

## 它是什么

README 这样描述它："an agent runtime — a single Rust binary you configure and run. It talks to LLM providers (Anthropic, OpenAI, Ollama, and ~20 others), reaches the world through 30+ channels (Discord, Telegram, Matrix, email, voice, webhooks, your own CLI), and acts through tools (shell, browser, HTTP, hardware, custom MCP servers). Everything runs on your machine, with your keys, in your workspace." 文档还说明了它不是什么："Not a framework. You don't build apps on top of ZeroClaw. You configure it and connect channels."

围绕这个 runtime，它配了：

- **渠道**：每个配置好的渠道都投递到同一个 agent 循环。文档列出了聊天平台（Matrix、Telegram、Discord、Slack、Mattermost、LINE、Signal、WhatsApp、企业微信 WeCom、微信、钉钉、Lark、QQ 等）、社交信息流、Git 托管平台、邮件和语音。渠道是编译期 feature；默认构建带 ACP、webhook、email、Telegram、Discord 和 filesystem，标准发布产物再加上 Git、Matrix、Lark 和 WhatsApp Web。
- **工具**：shell、文件、网页抓取与搜索、浏览器、HTTP、MCP server、cron 管理（`cron_add`、`cron_list`、`cron_run` 等）、skill、构建中包含时的 WASM 插件，以及硬件访问（Raspberry Pi、STM32、Arduino、ESP32 上的 GPIO / I2C / SPI / USB）。
- **记忆**：按 agent 选择的可插拔后端（`sqlite`、`markdown`、`postgres`、`qdrant`、`lucid` 或 `none`）。新 agent 默认用 SQLite，agent 写过数据后后端就会锁定。agent 之间共享记忆需要显式开启。
- **SOP 引擎**："deterministic procedures"，带"explicit trigger matching, approval gates, and auditable run state."webhook、MQTT、filesystem 和 AMQP 是已接通的事件源，cron 触发器由 daemon 分发；文档说 peripheral 和 calendar 触发器"are defined and matched but not yet routed to a live event source."
- **多 agent**：`spawn_subagent` 让同一个 agent 去跑一个子任务（subagent 不能再派自己的 subagent），`delegate` 把工作交给另一个已配置的 agent，peer group 让同一渠道上的 agent 互相对话。

## 什么时候选它

- 你想在高风险操作前有审批，又不想自己搭。默认的 `supervised` 级别下，低风险工具直接跑，中风险工具要询问，高风险工具被拦下。审批提示出现在发起对话的那个渠道里：Telegram 用内联按钮，Slack 用 Block Kit 按钮，Discord、Signal、Matrix 和 WhatsApp 回复 `<token> approve|deny|always`，CLI 里是行内提示。无人应答的请求默认 120 秒后过期，并且"Timeouts are treated as denials."
- 你想把审批发到别处。`approval_route` 能把一个 risk profile 的审批发到单独的审批渠道，默认失败即拒绝（`on_no_approver = "deny"`）。
- 你想让一个 agent 出现在很多入口上，包括邮件、语音、Git 托管平台和通过 ACP 接入的编辑器。
- 你想在小型或特殊硬件上跑它，或者让 agent 驱动传感器和引脚。
- 你想自选或混用 provider，包括本地 Ollama，并在某个 provider 出问题时自动 fallback。
- 你想让不止一个人使用管理面板。v0.9.0（2026-11-12）新增了可选的、通过你自己的 OpenID Connect provider 登录，账号会被限制在"inside what their permission profile allows"。

## 什么时候不选它

- **你需要产品内一个真正生效的急停开关。** 安全文档说 `zeroclaw estop`"is not a safety control today"；"To halt the agent now, stop the ZeroClaw process itself."
- **你需要 agent 执行过什么的审计记录。** 默认审计日志只覆盖"certificate issuance and renewal only (command execution is not audited)"。Tool receipt 是回填进对话的 HMAC 证据，"not a chained or durable audit log today."
- 你在 Windows 上运行并想要操作系统隔离：沙箱表格里 Windows 一栏写的是"No OS-level backend"。在 Linux 上，Landlock 和 Firejail 都不限制出站网络。
- 你想要一个能手工读改的小配置。一个可用的配置至少要有 provider、agent 和 risk profile，各自是 `<type>.<alias>` 形式的表，而且 v0.9.0 把配置升到了 schema version 4，带破坏性变更。
- 你想要一个用来搭自己应用的库；项目明确说自己不是框架。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 交付面 | 很强 | 30+ 渠道、Web 管理面板、`zerocode` 终端界面、REST/WebSocket gateway、面向编辑器的 ACP；具体渠道取决于构建 |
| 人工审批 | 很强 | 默认 `supervised`，按渠道的审批按钮或 token、`always_ask`、失败即拒绝的跨渠道审批路由，可选的逐操作 OTP |
| 工具调用 | 强 | shell、文件、网页、浏览器、HTTP、MCP、cron 工具、skill、WASM 插件、硬件外设 |
| 代码执行 | 强 | shell 受命令白名单和校验器约束，有工作区边界和操作系统沙箱后端（Landlock、Firejail、Bubblewrap、Seatbelt、Docker）；Windows 上没有 |
| 记忆 | 中 | 六种可插拔后端，默认 SQLite，跨 agent 共享需显式开启；文档没有写自动整理 |
| 定时调度 | 中 | agent 可自行管理的 cron 任务、SOP 的 cron 触发器、daemon 里的 heartbeat 监控；cron 运行"are never pre-approved" |
| 多 agent | 中 | 只有一层的 subagent、向其他 agent 委派（每个 risk profile 默认禁止）、共享渠道上的 peer group |
| 治理 | 强 | MIT 或 Apache-2.0，PR 开放，有 RFC 流程和 CLA |

## 使用代价

起步低：一条安装命令（`curl -fsSL … install.sh | sh`，Windows 上有预编译的 PowerShell 路径），然后 `zeroclaw quickstart` 依次带你配好 provider、risk profile、记忆、可选的渠道和 agent；CLI 渠道马上就能用。`zeroclaw service install` 和 `zeroclaw service start` 让它常驻运行。暴露面越大，成本越高。把 gateway 开到局域网需要 `host = "0.0.0.0"` 再加 `allow_public_bind = true`（"Without it, the daemon refuses"），或者用 Tailscale 之类的隧道。每个渠道都有自己的白名单（`allowed_users`、`allowed_chats`、webhook 的 IP 白名单）。生产环境下文档要求"enable OTP and restricted tools"，并用"an external supervisor or logging wrapper"来记录执行过的命令。YOLO 模式会关掉所有关卡，只适用于"dev boxes, home labs, and throwaway VMs"；文档警告，挂在公开 Telegram 机器人后面的 YOLO agent"is a Telegram-accessible root shell"。

## 和本地图其他条目的关系

ZeroClaw 和 [OpenClaw](openclaw.md)、[nanobot](nanobot.md)、[Hermes Agent](hermes-agent.md)、[Mercury Agent](mercury-agent.md) 在同一条自托管赛道上：一个归你所有的 runtime、多个聊天入口、工具和定时任务。对 [nanobot](nanobot.md)，最明显的差别在审批：nanobot 有访问配对但没有逐操作审批，而 ZeroClaw 出厂就开着 `supervised` 审批，工作区边界也设为 `true`。这让它更接近同样以审批为中心的 [Mercury Agent](mercury-agent.md)。对 [OpenClaw](openclaw.md)，两者都是覆盖面很广、要做很多路由、权限和运维决策的控制平面；ZeroClaw 自己的特色是单个 Rust 二进制、硬件外设和 SOP 引擎。

## 结论

如果你想在自己的硬件上跑一个常驻个人 agent、能从很多渠道找到它，并且希望审批提示是默认开启而不是额外加装的，ZeroClaw 很合适。要留出时间理解它的配置模型，并仔细读安全文档：急停开关不生效，命令不做审计，隔离效果取决于你的操作系统。在让任何其他人能触达它之前，保持 gateway 只在 localhost 上并开着配对，设好渠道白名单，再打开 OTP。

## 来源

- [zeroclaw-labs/zeroclaw README](https://github.com/zeroclaw-labs/zeroclaw) · [LICENSE-MIT](https://github.com/zeroclaw-labs/zeroclaw/blob/master/LICENSE-MIT) · [LICENSE-APACHE](https://github.com/zeroclaw-labs/zeroclaw/blob/master/LICENSE-APACHE) · [Releases（v0.9.0，2026-11-12）](https://github.com/zeroclaw-labs/zeroclaw/releases)
- 文档：[Quickstart](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/getting-started/quickstart.md) · [Security model](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/security/model.md) · [Autonomy levels](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/security/autonomy.md) · [Sandboxing](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/security/sandboxing.md) · [YOLO mode](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/getting-started/yolo.md) · [Channels](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/channels/overview.md) · [Provider catalog](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/providers/catalog.md) · [Tools](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/tools/overview.md) · [Delegation](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/agents/delegation.md) · [Agent filesystem and memory](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/agents/filesystem.md) · [SOP](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/sop/index.md) · [Network deployment](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/ops/network-deployment.md) · [What this isn't](https://github.com/zeroclaw-labs/zeroclaw/blob/master/docs/book/src/philosophy/what-this-isnt.md) · [docs.zeroclaw.com](https://docs.zeroclaw.com/master/en/introduction.html)
