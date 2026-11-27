# QwenPaw

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](qwenpaw.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/qwenpaw.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：QwenPaw 是 AgentScope 团队出的自托管个人助手：一个 Python 应用同时提供网页 Console、TUI 和桌面应用，并能在从钉钉、飞书到 Telegram、Slack 的聊天应用里回话。它的主打功能是基于 ReMe 的三层记忆、一个实例里跑多个 agent，以及五层安全机制。不过它的内核级沙箱要你自己打开。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | AgentScope 团队（`agentscope-ai`，也做了 AgentScope、AgentScope Runtime 和 ReMe）。SECURITY.md 把漏洞报告指向阿里巴巴安全响应中心（ASRC） |
| 路线 | 自托管 / 本地 runtime |
| 仓库 | [`agentscope-ai/QwenPaw`](https://github.com/agentscope-ai/QwenPaw)：Apache-2.0，Python，截至 2026-11-27 共 38,256 star（仓库创建于 2026-02-24） |
| 是否开源 | 是（Apache License 2.0）。CONTRIBUTING 欢迎通过 pull request 贡献新渠道、模型 provider、skill 和 MCP |
| 形态 | 一个 Python 包（`pip install qwenpaw`），在 `127.0.0.1:8088` 上跑本地网页 Console，另有全屏 TUI、桌面应用（Beta，Windows 和 macOS）、REST API、Docker 镜像，以及可自托管的多用户 Hub |
| 模型与计费 | 自带 provider 密钥，或在本地跑模型。README 在"14+ cloud providers"里列出了 DashScope / Qwen、OpenAI、Anthropic、Google Gemini、DeepSeek、Kimi 和 OpenRouter，另有内置的 QwenPaw Local runtime（llama.cpp）、Ollama 和 LM Studio |
| 默认模型 | 没有。没有 provider 时，`qwenpaw init --defaults` 会输出"No LLM provider configured"；对云端模型，"QwenPaw will not work until a valid key is set."聊天模型要在 **Settings → Models** 里选。项目还为 agent 任务训练了自家的 QwenPaw-Flash 模型（2B / 4B / 9B / 35B-A3B / 27B） |
| 最适合 | 想在自己电脑上跑一个个人助手、能从国内外聊天应用里找到它、记忆会随时间积累的个人，或者用 Hub 的小范围可信团队 |
| 主要代价 | 只有被守卫规则标记的调用才弹审批（默认 `AUTO`），内核沙箱默认关闭（`sandbox_enabled: false`），Console 登录也默认关闭。功能面大、迭代快：v2.3.0 于 2026-11-11 发布，2026-11-23 又出了 v2.3.1 beta |
| 文档 | [qwenpaw.agentscope.io/docs](https://qwenpaw.agentscope.io/docs) · [仓库内文档源码](https://github.com/agentscope-ai/QwenPaw/tree/main/website/public/docs) |

## 它是什么

README 的概括是 *"Your personal AI assistant — deploy locally or in the cloud, extend with Skills & Plugins, connect across every channel."* 名字"stands for Qwen Personal Agent Workstation"。一个进程服务所有客户端：TUI "drives the _same_ agent as the Console and the IM Channels — same memory, skills, MCP tools, and sessions"。

围绕这个 agent，它配了：

- **工具**：shell、带预览和 diff 的统一文件工作区、处理 PDF、Word、Excel 和 PowerPoint 的文档 skill、Browser-use 和 Computer-use（v2.1.0 加入）、MCP 客户端，以及带插件市场的插件系统。Codex 和 Qoder 后端是可选插件。
- **三层记忆**："live working context, full verbatim history, and a self-evolving personal knowledge base powered by ReMe"。**Auto-Memory** 默认"after every five user turns"运行一次，写成 Markdown 笔记；**Auto-Dream** 再把它们整理进 `digest/` 知识库。它的 cron 任务默认开启，每天 23:00 运行（`dream_cron: "0 23 * * *"`）。文档说"Markdown files are the source of truth"。
- **定时调度**：cron 任务"support **multiple jobs in parallel**"，每个任务有自己的时间、内容和投递目标；另有 **heartbeat** 定时问候，它的 `enabled` 字段"**Default false**"。
- **多 agent**：一个实例里跑多个独立 agent，各有自己的人设、记忆、skill 和渠道；一个需手动开启的 **Multi-Agent Collaboration** skill 让它们互相调用；项目内的一次性 subagent（`spawn_subagent`）；以及跑"**master → worker → verifier** pipeline"的 Mission Mode。
- **双向 ACP**：QwenPaw 可以通过 `delegate_external_agent` 把任务交给外部 runner（内置示例有 `opencode`、`qwen_code`、`claude_code` 和 `codex`），也可以作为 ACP server 供其他客户端接入。文档把 ACP 展开为 Agent Client Protocol；README 的功能表写的是 Agent Communication Protocol。

## 什么时候选它

- 你想要一个既能进国内工作聊天、也能进国际应用的助手。渠道指南有 18 节，包括钉钉（"recommended"）、飞书（Lark）、企业微信、个人微信、QQ、元宝、iMessage（仅 macOS）、Discord、Telegram、Slack、Matrix、Mattermost、Azure Bot、MQTT、Voice 和 SIP。
- 你想要会不断积累、又能以 Markdown 文件形式阅读和编辑的长期记忆。
- 你想完全本地运行。README 说本地后端不需要 API key，QwenPaw Local 下载 QwenPaw-Flash 模型时会给出"hardware-aware recommendations"。
- 你想在一次安装里放几个分工不同的 agent（文档举的例子是工作与生活分开、按平台分 agent），或者想让 QwenPaw 通过 ACP 把活交给 Codex、Claude Code、OpenCode 或 Qwen Code。
- 你需要在一台服务器上给小范围可信团队用：Hub 让每个成员拿到"their own QwenPaw with separate workspaces, settings, credentials, and conversations."

## 什么时候不选它

- **你期望默认每个操作都要审批。** 默认的 `approval_level` 是 `AUTO`："Only tool calls flagged by guard rules require approval"。shell 规避检查默认全部关闭（"**All checks default to `false` (disabled).**"），而且"In non-interactive contexts without a session, findings are logged and execution may still proceed"。想让每次调用都审批，可以用 `STRICT`。
- **你以为内核沙箱默认开着。** README 把 Seatbelt、Bubblewrap / Landlock 和 AppContainer 隔离列为核心一层，但配置字段 `security.sandbox_enabled` 默认是 `False`：没有匹配规则的 shell 调用会"run directly without the sandbox"。即便打开，文档也列了限制：`network_allow` 默认 `["*"]`，"Bubblewrap does not isolate the network at all"，默认的 `allow_read_all: true` 让整个文件系统可读。
- 你打算不配登录就把 Console 暴露到 localhost 之外。网页认证"**disabled by default**"，要用 `QWENPAW_AUTH_ENABLED` 打开；来自 localhost 的请求总是跳过认证。
- 你需要一个公开的多租户服务。Hub 文档说当前版本"intended only for internal teams whose members trust one another"，并提醒不要把它当作"as a public multi-tenant service for unknown users."来运营。
- 你希望默认不收遥测。`qwenpaw init --defaults` 会自动同意匿名使用数据收集（版本、安装方式、操作系统、Python 版本、CPU 架构、是否有 GPU），而且 agent 运行时（包括定时任务）每天还会发送这些字段、一个持久的随机 runtime UUID 和 UTC 日期；交互式 `init` 会询问，设置 `QWENPAW_TELEMETRY_DISABLED` 可两者都关掉。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 交付面 | 很强 | 网页 Console、TUI、桌面应用（Beta）、18 节渠道、REST API、ACP server |
| 记忆 | 很强 | 基于 ReMe 的三层记忆；Auto-Memory 和每日 Auto-Dream 默认开启；Markdown 是唯一事实来源 |
| 工具调用 | 很强 | shell、文件、文档、Browser-use、Computer-use、MCP、skill 和插件市场 |
| 多 agent | 强 | 每个实例多个独立 agent、需手动开启的协作 skill、一次性 subagent、Mission Mode、ACP 委派 |
| 定时调度 | 强 | 可并行、带投递目标的 cron 任务；heartbeat 默认关闭 |
| 人工审批 | 中 | 默认对守卫标记的调用审批，`STRICT` 对每次调用审批，MCP 工具可设 ask 规则；非交互运行可能直接执行 |
| 执行隔离 | 中 | 有 macOS、Linux 和 Windows 的内核沙箱后端，但默认关闭，且默认网络全开 |
| 治理 | 强 | Apache-2.0、开放 pull request、有成文的私下漏洞报告流程 |

## 使用代价

起步低：`pip install qwenpaw`（Python 3.11 到 3.14 以下）或一行安装脚本，然后 `qwenpaw init --defaults` 和 `qwenpaw app`，再在 Console 里选模型。init 命令会显示一段安全提示，把默认配置称为"a single-operator boundary: one trusted user."Console 默认绑定 `127.0.0.1`，README 里的 Docker 命令把端口映射到 `127.0.0.1:8088`，并把密钥放在单独的 `qwenpaw-secrets` 卷里。在放宽访问之前，这些活要你自己做：设置 `QWENPAW_AUTH_ENABLED`、打开 `sandbox_enabled`、考虑改用 `SMART` 或 `STRICT` 审批、给渠道用户设白名单。项目迭代也快。它的 roadmap 正在把非核心组件拆成插件，v2.3.0 把渠道改成了插件，所以渠道卡片在你安装插件前可能显示"**Plugin not installed**"。托管选项有阿里云 ECS 一键部署、AgentScope Platform 和 ModelScope Studio；README 要求 Studio 用户设为"**non-public** so others cannot control your QwenPaw"。

## 和本地图其他条目的关系

QwenPaw 和 [nanobot](nanobot.md)、[OpenClaw](openclaw.md)、[Hermes Agent](hermes-agent.md) 在同一条自托管赛道上：一个归你所有的 runtime、多个聊天入口、记忆和定时任务。本地图对 nanobot 的判断是没有逐操作审批、文件边界是应用层的；相比之下，QwenPaw 默认带基于规则的审批提示，还有一个可以打开的操作系统级沙箱。它的渠道指南把国内平台放在前面（钉钉是"recommended"的渠道，接着是飞书，后面还有企业微信、微信、QQ 和元宝），Hub 还多了一个可信团队模式。它也伸进了编码赛道：借助 ACP 委派，它能把 [Codex](codex.md) 或 [Claude Code](claude-code.md) 当作协作者来驱动。

## 结论

如果你想要一个住在自己电脑上、从钉钉或飞书找到它和从 Telegram 一样方便、记忆会长成一个可读知识库、本地或云端模型任选的个人助手，QwenPaw 很合适。把它的安全清单当作一组开关来看。默认你有守卫标记审批、File Guard 和 warn 模式的 skill 扫描器，但没有内核沙箱，也没有 Console 登录。在任何其他人能触达它之前，先把这些打开。

## 来源

- [agentscope-ai/QwenPaw README](https://github.com/agentscope-ai/QwenPaw) · [LICENSE](https://github.com/agentscope-ai/QwenPaw/blob/main/LICENSE) · [SECURITY.md](https://github.com/agentscope-ai/QwenPaw/blob/main/SECURITY.md) · [CONTRIBUTING](https://github.com/agentscope-ai/QwenPaw/blob/main/CONTRIBUTING.md) · [Releases（v2.3.0.post1，2026-11-18；v2.3.1-beta.1，2026-11-23）](https://github.com/agentscope-ai/QwenPaw/releases) · [config schema](https://github.com/agentscope-ai/QwenPaw/blob/main/src/qwenpaw/config/config.py) · [init 命令](https://github.com/agentscope-ai/QwenPaw/blob/main/src/qwenpaw/cli/init_cmd.py)
- 文档：[Security](https://qwenpaw.agentscope.io/docs/security) · [Models](https://qwenpaw.agentscope.io/docs/models) · [Channels](https://qwenpaw.agentscope.io/docs/channels) · [Memory](https://qwenpaw.agentscope.io/docs/memory) · [Cron](https://qwenpaw.agentscope.io/docs/cron) · [Heartbeat](https://qwenpaw.agentscope.io/docs/heartbeat) · [Multi-Agent](https://qwenpaw.agentscope.io/docs/multi-agent) · [ACP Integration](https://qwenpaw.agentscope.io/docs/acp-integration) · [Hub](https://qwenpaw.agentscope.io/docs/hub) · [TUI](https://qwenpaw.agentscope.io/docs/tui) · [Release notes](https://qwenpaw.agentscope.io/release-notes)
