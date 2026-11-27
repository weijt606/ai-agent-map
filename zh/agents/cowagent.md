# CowAgent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](cowagent.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/cowagent.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：CowAgent 是一个自托管的个人 agent，前身是 `chatgpt-on-wechat`，跑在你的电脑或服务器上，在 Web 控制台、桌面客户端、手机 App 和十一个 IM 渠道里回话，其中包括微信、飞书、钉钉、企业微信和 QQ。它在工具循环之上叠了基于文件的记忆、知识库、每晚一次的"Deep Dream"和后台的"Self-Evolution"，还能组建一支 agent 团队。源码或 Docker 安装的默认权限模式是 `full-access`。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | zhayujie（LICENSE 写的是"Copyright (c) 2022 zhayujie"）。README 通过 LinkAI 提供企业托管 |
| 路线 | 自托管 / 本地 runtime |
| 仓库 | [`zhayujie/CowAgent`](https://github.com/zhayujie/CowAgent)：MIT，Python，截至 2026-11-27 共 48,111 star（仓库创建于 2022-08-07；项目"was previously named `chatgpt-on-wechat`"） |
| 是否开源 | 是（MIT）。CONTRIBUTING 要求 fork、从 `master` 拉分支再提 PR；issue 和 PR 请用英文 |
| 形态 | 一个 Python 服务，带 9899 端口的 Web 控制台和 `cow` CLI；内置后端的 macOS / Windows 桌面客户端；iOS / Android / HarmonyOS App（公测）；CowAgent Cloud 实例 |
| 模型与计费 | 自带 key：模型表列了十一家厂商、CowAgent 和 LinkAI 两个服务，以及一个"Custom"条目，用于"Local models / third-party proxy"。可选的官方路线：CowAgent 模型服务（"a single API key"）、用 ChatGPT 登录走"Codex subscription"，以及内置模型的 CowAgent Cloud 套餐 |
| 默认模型 | `config-template.json` 和 `config.py` 里是 `deepseek-flash`，所有 API key 都为空。安装脚本有一步"Guided configuration for AI model and channel"，Web 控制台里也能切换 provider |
| 最适合 | 想要一个常驻在中外 IM 应用里的个人 agent、记忆和知识库能自己长、可能还要几个分工 agent 的人 |
| 主要代价 | 源码和 Docker 安装默认 `full-access`，而权限模式是"argument-level checks, not an OS sandbox"。不设 `web_password` 的话 Web 控制台没有密码 |
| 文档 | [docs.cowagent.ai](https://docs.cowagent.ai/intro/index) · [仓库 docs](https://github.com/zhayujie/CowAgent/tree/master/docs) · [cowagent.ai](https://cowagent.ai) |

## 它是什么

README 开头这样写：*"**CowAgent** is your own open-source personal AI agent. It plans tasks proactively, uses tools, skills and MCP, and gets to know you over time through long-term memory, a knowledge base and self-evolution. It's also an open, extensible Agent Harness."* 架构上是一条管线："messages flow in through **Channels**; the **Agent Core** plans and reasons over memory, knowledge, and the available tools and skills; **Models** generate the response, which is sent back through the originating channel."

围绕这个循环，它配了：

- **工具**：`read` / `write` / `edit` / `ls`、`bash`、`send`、`memory`、`env_config`、`web_fetch`、`scheduler`、`web_search`、`vision` 和 `browser`（用 `cow install-browser` 安装），以及在一个 `mcp.json` 里配置的 MCP server。
- **Skill**：来自 Skill Hub、GitHub、ClawHub 或某个 URL，也可以在对话里用 `skill-creator` 写出来。
- **三层记忆**：对话上下文、`memory/YYYY-MM-DD.md` 里的每日文件，以及 `MEMORY.md`，后者"is injected into the system prompt for every conversation."每天 23:55 跑一次每日摘要，随后 **Deep Dream** 把它提炼进 `MEMORY.md`（`deep_dream_enabled` 默认 `true`）。检索混合了 FTS5 关键词检索和向量检索。
- **个人知识库**（默认 `knowledge: true`）：把主题整理成 Markdown wiki，并提供知识图谱视图。
- **Self-Evolution**：对话空闲（默认 10 分钟）且轮数足够（默认 6 轮）后，一个只有"a restricted toolset"的独立任务会保存记忆、修复或新建 skill、跟进没做完的任务。每次复盘前都会做备份，可以撤销。`config.py` 和模板把 `self_evolution_enabled` 设为 `true`；文档表格写的是 `false`，并注明"(on by default for new installs)"。
- **多 agent**：常驻的团队成员各有"its own memory, capabilities, knowledge, and workspace"，由一个主 agent 把任务委派给它们；还有共用主 agent 工作区的临时 sub-agent（每次调用 `max_concurrent: 3`，`max_depth: 1`）。
- **定时任务**：一次性、固定间隔或 cron 计划，触发时发送固定消息或执行一个 agent 任务，结果写回用户的会话。

## 什么时候选它

- 你的用户在中文 IM 应用里。渠道表覆盖微信、飞书 / Lark、钉钉、企业微信机器人、企业微信应用、微信客服、微信公众号和 QQ，以及 Telegram、Slack 和 Discord。一个实例"can serve multiple channels in parallel."
- 你想要几个分工明确的 agent。每个团队成员可以有自己的模型、skill、知识库和工作区，渠道实例也可以分别绑定到不同的 agent 或团队。
- 你想要能自我维护、又读得懂的记忆。记忆、梦境日记和进化记录都是工作区（默认 `~/cow`）里的 Markdown 文件，可以在 Web 控制台里浏览。
- 你想要宽的模型选择，包括国内厂商（DeepSeek、Qwen、GLM、Kimi、MiniMax、豆包、文心、MiMo）和本地模型，而且对话、视觉、图像生成、语音和 embedding 可以各自走不同的厂商。
- 你想在手机上用同一个 agent。手机 App 可以在手机上直接跑 agent，也可以和电脑、服务器或 CowAgent Cloud 上的实例配对。

## 什么时候不选它

- **你需要在电脑或服务器上的高风险操作前有一道审批。** 三种权限模式（`read-only`、`workspace-write`、`full-access`）只决定放行或拒绝一次调用；文档没有描述桌面端或服务器上的逐操作审批。逐操作的询问只存在于手机 App 的手机能力上："It asks before each action"。
- 你期望默认就有约束。`agent_permission_mode` 默认 `full-access`；只有全新安装的桌面端和手机端会被设为 `workspace-write`，而"docker/source stay at full-access."SECURITY.md 说这些模式"are argument-level checks, not an OS sandbox"，权限策略代码也写明由 `bash` 启动的程序"can still write wherever the OS lets it."文档的建议是"for strong isolation, run inside a container."
- 你打算不加固就对外暴露。`web_password` 默认为空（"empty means no authentication required"）。`web_host` 留空时，没有密码的控制台监听 `127.0.0.1`，设了密码后改为监听 `0.0.0.0`。README 的免责声明写着"only deploy it in trusted environments."
- 你需要开源版自带角色、工作区和审计日志。README 把"role-based access, audit logs"列在 LinkAI 的企业功能下，而不是开源项目里。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 交付面 | 很强 | Web 控制台、桌面客户端、手机 App（公测）、十一个 IM 渠道，以及默认关闭的 OpenAI 兼容对话 API |
| 记忆 | 很强 | 三层记忆、每晚 Deep Dream、知识库和 Self-Evolution，全部是工作区文件 |
| 工具调用 | 强 | 文件、shell、浏览器、网页、视觉、scheduler、MCP 和 skill 市场 |
| 多 agent | 强 | 各有独立工作区的常驻 agent 团队、委派、并行 sub-agent |
| 定时调度 | 中 | 通过 scheduler 工具做 cron、间隔和一次性任务，外加每晚的记忆任务 |
| 人工审批 | 弱 | 会话级权限模式；逐操作询问只用于手机能力 |
| 治理 | 中 | MIT、fork 即可提 PR；团队角色和审计通过 LinkAI 提供，不在仓库里 |

## 使用代价

起步低：一条安装命令（`bash <(curl -fsSL https://cdn.link-ai.tech/code/cow/run.sh)`，Windows 上是 `irm … run.ps1 | iex`）或 `docker compose up -d`，然后打开 `http://localhost:9899`。安装脚本会克隆到 `~/CowAgent`，需要 Python 3.7–3.13（"3.9 recommended"）。桌面客户端内置后端，CowAgent Cloud 不需要服务器。要对外暴露控制台就得多做几步：设置 `web_host` 和 `web_password`、开放 9899 端口，TLS 方面文档推荐用 nginx 反向代理。Docker compose 文件保留了 `AGENT_PERMISSION_MODE: 'full-access'`，注释是"Container is already an isolation boundary"。README 还提醒 Agent 模式"consumes substantially more tokens than regular chat"。2026-09-14（v2.1.9）到 2026-11-26（v2.3.0）之间发了五个版本，`cow update` 会拉取最新代码并重启。

## 和本地图其他条目的关系

CowAgent 和 [nanobot](nanobot.md)、[OpenClaw](openclaw.md)、[Hermes Agent](hermes-agent.md) 在同一条自托管赛道上：一个归你所有的 runtime、多个聊天入口、记忆和定时任务。对 [nanobot](nanobot.md)，它有类似的基于文件的记忆和梦境式整理，也同样没有逐操作审批，但多了有名字的权限模式，以及成员各自保留独立工作区和记忆的 agent 团队；nanobot 的文档则要求跑多个实例来分开记忆。它的渠道列表更偏向国内企业应用和微信系应用，除了自家的 Skill Hub，也能从 ClawHub 安装 skill。

## 结论

如果你想要一个住在自己电脑或服务器上、在微信、飞书、钉钉、QQ、Telegram 或 Slack 里回话的个人 agent 或小型 agent 团队，而且记忆和知识库会自己整理成你读得懂的文件，CowAgent 很合适。它的默认值假定主人可信：源码和 Docker 安装是 `full-access`、控制台没有密码、没有逐操作审批。在把它接给你不完全信任的人之前，先把会话切到 `workspace-write`、设好密码，并放进容器里跑。

## 来源

- [zhayujie/CowAgent README](https://github.com/zhayujie/CowAgent) · [LICENSE](https://github.com/zhayujie/CowAgent/blob/master/LICENSE) · [SECURITY.md](https://github.com/zhayujie/CowAgent/blob/master/SECURITY.md) · [CONTRIBUTING.md](https://github.com/zhayujie/CowAgent/blob/master/CONTRIBUTING.md) · [Releases（v2.3.0，2026-11-26）](https://github.com/zhayujie/CowAgent/releases) · [config-template.json](https://github.com/zhayujie/CowAgent/blob/master/config-template.json) · [config.py](https://github.com/zhayujie/CowAgent/blob/master/config.py) · [权限策略](https://github.com/zhayujie/CowAgent/blob/master/agent/permission/policy.py) · [docker-compose.yml](https://github.com/zhayujie/CowAgent/blob/master/docker/docker-compose.yml)
- 文档：[Architecture](https://docs.cowagent.ai/intro/architecture) · [Choose How to Use](https://docs.cowagent.ai/guide) · [Quick Start](https://docs.cowagent.ai/guide/quick-start) · [Mobile App](https://docs.cowagent.ai/guide/mobile) · [CowAgent Cloud](https://docs.cowagent.ai/guide/cloud) · [Web Console](https://docs.cowagent.ai/channels/web) · [Channels](https://docs.cowagent.ai/channels/index) · [Models](https://docs.cowagent.ai/models/index) · [Long-term Memory](https://docs.cowagent.ai/memory/index) · [Deep Dream](https://docs.cowagent.ai/memory/deep-dream) · [Self-Evolution](https://docs.cowagent.ai/memory/self-evolution) · [Agent Teams](https://docs.cowagent.ai/multi-agent/team) · [Sub-Agent](https://docs.cowagent.ai/multi-agent/subagent) · [Scheduler](https://docs.cowagent.ai/tools/scheduler)
