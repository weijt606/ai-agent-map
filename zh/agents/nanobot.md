# nanobot

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](nanobot.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/nanobot.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：nanobot 是港大数据智能实验室（HKUDS）出的自托管个人 agent，以一个本地 gateway 的形式运行，你可以在浏览器、终端或聊天应用里找到它。它会记住偏好、跑定时自动化、把任务派给 subagent。它的卖点是一个你读得懂、归你所有的"small core"，而不是一个平台。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | HKUDS（Data Intelligence Lab@HKU）。LICENSE 里的版权方是"Xubin Ren and the nanobot contributors" |
| 路线 | 自托管 / 本地 runtime |
| 仓库 | [`HKUDS/nanobot`](https://github.com/HKUDS/nanobot)：MIT，Python，截至 2026-11-18 共 50,167 star（仓库创建于 2026-02-01） |
| 是否开源 | 是（MIT）。issue 对所有人开放；"pull requests are currently limited to repository collaborators" |
| 形态 | 一个 Python gateway，自带 WebUI、原生 TUI、聊天应用渠道和 Python SDK；PyPI 包名 `nanobot-ai` |
| 模型与计费 | 自带 provider 或本地模型服务："nanobot does not supply a model account."支持兼容 OpenAI 的 API、Ollama、vLLM，部分 provider 支持 OAuth 登录 |
| 默认模型 | 加上 provider 凭据之前没有可用的模型；文档要求在 **Settings → Models** 里保存预设。配置 schema 的内置默认值是 `anthropic/claude-opus-4-5`，provider 为 `auto` |
| 最适合 | 想在自己的电脑或服务器上跑一个个人 agent、能从聊天应用里找到它、带记忆和定时任务的个人或小范围可信团队 |
| 主要代价 | 默认的文件边界是应用层的，不是操作系统沙箱，也没有逐操作审批；shell 沙箱和渠道白名单要自己配 |
| 文档 | [nanobot.wiki](https://nanobot.wiki)（已发布版本）· [仓库 docs](https://github.com/HKUDS/nanobot/tree/main/docs)（当前源码；README 自称"describes current source"，所以下文部分功能可能比 v0.4.1 新） |

## 它是什么

README 开头这样写：*"nanobot is an ultra-lightweight, open-source, self-hosted personal AI agent framework written in Python. Use it in a browser, terminal, or chat app to work with files, remember preferences, and schedule tasks."* 架构上它是一个 gateway："The Python gateway owns agent execution, sessions, tools, memory, and security policy for the WebUI, TUI, and chat apps"，所有客户端共用这个 runtime。

围绕这个循环，它配了：

- **工具**：文件读写与编辑、shell、带 SSRF 检查的网页搜索与抓取、MCP server、cron、图像生成和 subagent。Apps、Skills、Agent Plugins 还能再加。
- **两层记忆**。对话变长时会被摘要；**Dream** 再把长期记忆整理进 `USER.md`、`memory/MEMORY.md` 等文件。Dream 默认开启，gateway 运行期间每 2 小时跑一次（`intervalH: 2`）。
- **自动化**：基于 cron 服务的提醒和定时任务、让脚本触发已保存任务的本地 trigger，以及一个内置的 `heartbeat` 任务（默认开启），它会处理 `HEARTBEAT.md` 里的事项。
- **Subagent**：派出去的任务挂在发起它的那段对话上，默认最多同时跑四个（`maxConcurrentSubagents: 4`）。
- **长周期目标**：`/goal` 让 agent 超出普通的迭代上限继续工作，"until it records completion, cancellation, or a blocked state"。

## 什么时候选它

- 你想要一个能从很多地方发消息找到的 agent。渠道文档覆盖 18 个平台（源码里除 WebUI 用的 WebSocket 外有 18 个渠道包），包括 Telegram、Discord、Slack、WhatsApp、微信、飞书、钉钉、QQ、Matrix、Mattermost、Signal、Email、Microsoft Teams 和 Linear。
- 你想要能自己整理、也能被你检查的记忆。Dream 写进工作区里的文件，`/dream-log` 能看到改了什么。
- 你有后台工作：README 列出了"long-horizon goals"和"scheduled automations"，`nanobot gateway --background` 能让渠道和自动化在客户端关闭后继续运行。
- 你想通过 Python SDK 把同一个 agent 嵌进自己的代码。
- 你想自由选模型，包括本地模型。

## 什么时候不选它

- **你需要在高风险操作前有一道审批。** 访问控制是按话题（Restricted 或 Full Access）和按渠道发送者（配对和 `allowFrom`）来设的，但文档里没有逐操作的审批卡片。`/stop` 能中断工作，但"cancellation does not undo file changes or other actions already taken"。
- 你期望默认就有隔离。WebUI 的 **Default Permission** 是"workspace-restricted access, not an OS sandbox"；配置里 `tools.restrictToWorkspace` 默认 `false`，`tools.exec.sandbox` 默认 `""`。文档要求生产部署两个都设上，并说明 Windows 上命令在没有操作系统沙箱的情况下运行（"runs commands without OS sandboxing"），两种沙箱后端也都不限制网络访问（"Neither backend restricts network access"）。
- 你需要在同一个实例里给不同客户或用户分开记忆。话题和项目不会产生独立的长期记忆，文档的建议是跑多个实例。
- 你不是协作者，但想贡献代码。
- 你要的是带角色和审计的团队平台。WebUI 访问权"grants administration of the same agent instance"。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 交付面 | 很强 | WebUI（桌面与手机）、原生 TUI、18 个聊天渠道、Python SDK |
| 定时调度 | 强 | cron 提醒、定时自动化、本地 trigger、默认开启的 heartbeat；重启后错过的时间点不会补跑 |
| 记忆 | 强 | 会话摘要 + Dream 整理，默认开启，以文件形式可编辑 |
| 工具调用 | 强 | 文件、shell、网页、MCP、图像生成、Apps、Skills 和 Agent Plugins |
| 多 agent | 中 | 每段对话可派 subagent，默认并发四个；被中断的任务不会自动恢复 |
| 人工审批 | 弱 | 有渠道配对和访问模式，没有逐操作审批 |
| 治理 | 中 | MIT、issue 开放，但 PR 只限协作者 |

## 使用代价

起步低：一条安装命令（`curl … install.sh | sh`）或 `uv tool install nanobot-ai`，然后 `nanobot webui` 并保存一个模型预设。首次启动的 WebUI 绑定在 localhost，用一条登录链接进入，README 要求这条链接保密（"keep this credential private"）。要让它长期在线，成本就上来了。后台模式不会在重启或崩溃后自动拉起，文档指向操作系统托管的服务（Docker Compose、Linux service、macOS LaunchAgent）。接聊天应用意味着要逐个平台设白名单：Slack 和 Mattermost 的私信"are open by default"，而 `allowFrom: ["*"]` 会让任何能触达该渠道的人都能和机器人对话（"allows anyone who can reach that channel to talk to the bot"）。另有一键部署的 Render Blueprint，会要求填写 `ANTHROPIC_API_KEY` 和 `NANOBOT_WEB_TOKEN`。

## 和本地图其他条目的关系

nanobot 和 [Hermes Agent](hermes-agent.md)、[OpenClaw](openclaw.md)、[Mercury Agent](mercury-agent.md) 在同一条自托管赛道上：一个归你所有的 runtime、多个聊天入口、记忆和定时任务。在这条赛道里，它的差异化主张是体量小、读得懂（"Small core"），短板是审批层，而 [Mercury Agent](mercury-agent.md) 恰恰把审批放在中心。对 [DeerFlow](deer-flow.md)，nanobot 是给单个主人用的个人 agent；DeerFlow 是多用户的 harness，带 sub-agent 批处理、沙箱容器和可选的审批策略。

## 结论

如果你想要一个住在自己电脑或服务器上、在你常用的聊天应用里回话、把记忆存成你看得懂的文件的个人 agent，nanobot 很合适。它的默认值是为单个可信主人设计的：应用层的工作区边界、没有逐操作审批、WebUI 就是管理后台。在让任何其他人跟它说话之前，先打开 shell 沙箱和渠道白名单。

## 来源

- [HKUDS/nanobot README](https://github.com/HKUDS/nanobot) · [LICENSE](https://github.com/HKUDS/nanobot/blob/main/LICENSE) · [Releases（v0.4.1，2026-11-06）](https://github.com/HKUDS/nanobot/releases) · [config schema](https://github.com/HKUDS/nanobot/blob/main/nanobot/config/schema.py)
- 文档：[Concepts](https://github.com/HKUDS/nanobot/blob/main/docs/concepts.md) · [Architecture](https://github.com/HKUDS/nanobot/blob/main/docs/architecture.md) · [Configuration](https://github.com/HKUDS/nanobot/blob/main/docs/configuration.md) · [Memory](https://github.com/HKUDS/nanobot/blob/main/docs/memory.md) · [Automations](https://github.com/HKUDS/nanobot/blob/main/docs/automations.md) · [Chat Apps](https://github.com/HKUDS/nanobot/blob/main/docs/chat-apps.md) · [WebUI](https://github.com/HKUDS/nanobot/blob/main/docs/webui.md) · [Providers](https://github.com/HKUDS/nanobot/blob/main/docs/providers.md) · [Deployment](https://github.com/HKUDS/nanobot/blob/main/docs/deployment.md) · [nanobot.wiki](https://nanobot.wiki)
