# DeerFlow

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](deer-flow.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/deer-flow.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：DeerFlow 是字节跳动开源的"super agent harness"：一个会规划、会派生 sub-agent、带长期记忆、在沙箱里跑代码的主 agent，以自托管服务栈的形式交付，带 Web 工作台、终端 UI、IM 渠道和 API。2.0 版是对最初那个 Deep Research 框架的彻底重写，走的是"开箱即用"路线，而不是一套零件。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 字节跳动（`bytedance/deer-flow`，deerflow.tech）。LICENSE 里的版权方是"Bytedance Ltd. and/or its affiliates"和"DeerFlow Authors" |
| 路线 | 通用自主 agent（它自称"super agent harness"） |
| 仓库 | [`bytedance/deer-flow`](https://github.com/bytedance/deer-flow)：MIT，Python 后端 + Node.js 前端，截至 2026-11-18 共 85,475 star |
| 是否开源 | 是（MIT）。1.x 的 Deep Research 框架保留在 `main-1.x` 分支 |
| 底座 | LangGraph 与 LangChain |
| 模型 | "Model-agnostic"：任何兼容 OpenAI API 的 LLM 都能接。没有预设模型，`make setup` 会写出 `config.yaml` 和 `.env` |
| 最适合 | 想要一个自托管 agent 同时做调研、写代码、产出文件，并且 sub-agent、记忆、沙箱都已经接好的团队 |
| 主要代价 | 一整套服务栈（Gateway、前端、nginx、沙箱容器），项目自己说它是为"本地可信环境"设计的；到目前为止每次发版都有破坏性变更，最近两次开头就是一长串 |
| 启动命令 | `git clone` 后依次 `make setup`、`make docker-init`、`make docker-start`，打开 `http://localhost:2026` |
| 文档 | https://github.com/bytedance/deer-flow/tree/main/docs/guide |

## 为什么要收录

DeerFlow 自称 harness，但本地图把它和 [Agent Zero](agent-zero.md)、[AutoGPT](autogpt.md) 这类通用自主 agent 放在一起。本地图的 [harness 路线](../comparisons/agent-harness-frameworks.md)收的是你 fork 下来自己拥有的循环（[Pi](pi.md)、[jcode](jcode.md)）、你自己组合的 harness（[DeepSeek Harness](deepseek-harness.md)），以及驱动其他 agent 的 meta-harness（[QM](qm.md)、[Omnigent](omnigent.md)）。DeerFlow 用这个词指的东西更接近成品，是一个面向最终用户任务的自托管应用。README 这样描述它相对 v1 的变化：*"DeerFlow 2.0 is no longer a framework you wire together. It's a super agent harness — batteries included, fully extensible."* 开箱自带"a filesystem, memory, skills, sandbox-aware execution, and the ability to plan and spawn sub-agents for complex, multi-step tasks"。

项目自己的历史解释了这个形态：它起步于 Deep Research 框架，社区随后拿它做"data pipelines, generating slide decks, spinning up dashboards, automating content workflows"，于是团队"rebuilt it from scratch"。2.0 版"shares no code with v1"。

## 什么时候选它

- 你希望"派活"是默认工作方式。主 agent "can spawn sub-agents on the fly — each with its own scoped context, tools, and termination conditions"，再核对、汇总它们交回的结果。
- 你希望代码跑在宿主机以外的地方。沙箱模式有 Local、Docker、Docker + Kubernetes 三种，另有 E2B、Tenki、OpenSandbox、BoxLite 等可选 provider。
- 你希望 agent 出现在大家本来就在用的地方。IM 渠道覆盖飞书/Lark、Slack、Telegram、Discord、钉钉、微信、企业微信、QQ 和 Buzz，文档写明"no public IP required for any of them"。另有一个走 webhook 的 GitHub 渠道。
- 你有周期性任务。定时任务工作台支持 `once`、`cron`、`interval` 三种调度，2.2 又加了目标驱动的任务和按所有者的并发上限。调度器默认关闭，要设 `scheduler.enabled: true` 才会跑。
- 你想要默认开启的长期记忆：代码默认值和示例配置里 `memory.enabled` 都是 `true`，事实会注入 system prompt。

## 什么时候不选它

- **你打算不做加固就把它放上网络。** 安全说明写道，DeerFlow "is designed by default to be deployed in a local trusted environment (accessible only via the 127.0.0.1 loopback interface)"，README 还补充说 Gateway 管理员账号"is equivalent to code execution on the host"。
- 你希望审批默认开启。逐工具的人工审批（`hitl_approval`）是有的，但"the default is disabled for existing installations"，代码默认值和示例配置也都是 `enabled: false`。
- 你需要升级之间契约稳定。v2.2.0 合入了"1068 merged PRs"，开头就是一串破坏性变更，涉及监听地址、凭据存储、调度 API 和工具授权。
- 你想要一个能读完、能 fork 的单文件循环。这是一个多服务应用；去看 [Pi](pi.md) 或 [mini-swe-agent](mini-swe-agent.md)。
- 你想避开厂商主导的技术栈。README 推广了字节火山引擎的 Coding Plan 和 BytePlus 的 InfoQuest，不过两者都不是必需的。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 多 agent | 很强 | 招牌能力：主 agent 派生作用域受限的 sub-agent；大批独立条目可走持久化的 `batch_task` |
| 代码执行 | 很强 | Local、Docker、Kubernetes 三种沙箱模式加可选云端 provider；默认关闭宿主机 bash |
| 交付面 | 很强 | Web 工作台、`deerflow` TUI、九个聊天应用渠道外加一个 GitHub webhook 渠道、个人访问令牌和内嵌 Python 客户端 |
| 记忆 | 强 | DeerMem 长期记忆默认开启；Mem0 是需主动启用的可选后端 |
| 定时调度 | 中 | `once` / `cron` / `interval` 任务，默认关闭；文档仍称之为"scheduled-task MVP" |
| 人工审批 | 中 | 有 `ask` / `auto` / `full` 三种模式和审批卡片，但要运维方主动开启，且 `full` 必须显式加进 `allowed_modes` |
| 稳定性 | 弱 | 2026 年 6 月以来三次发版，每次都有破坏性变更 |

## 沙箱默认值怎么回事

这几个默认值值得最先读，因为它们决定了"能跑代码"在你机器上到底意味着什么：

- **默认 provider 是 `LocalSandboxProvider`**，配置参考说它"is a host-side convenience mode, not a secure shell isolation boundary"。所以 `allow_host_bash` 默认是 `false`，需要 `bash` 时文档建议改用 `AioSandboxProvider`（Docker 沙箱）。
- **Docker 沙箱容器**丢弃了所有 Linux capability，只保留一个五项的白名单，并开启 `no-new-privileges`；但随附镜像以 `seccomp=unconfined` 运行，因为其中的 Chromium 在 Docker 默认 seccomp 配置下起不来。
- **对外暴露**需要主动开启。Docker 栈的入口端口只发布在 `127.0.0.1` 上；从 2.2 起，`make dev` 和 `make start` 也只绑定回环地址，要暴露整个服务栈必须在 `.env` 里设置 `BIND_HOST=0.0.0.0`。

## 使用代价

中到高。安装是一个向导（README 估计约两分钟），再加 Docker；本地开发则需要 Node.js 22+、pnpm、uv 和 nginx。模型凭据自己提供，`make doctor` 会标出占位用的 key。要离开 localhost，就得照安全说明做：IP 白名单、带认证的反向代理、网络隔离。多 worker 或多实例部署需要 Postgres 和 Redis stream bridge；从 2.2 起，其中存储凭据的部署（IM 渠道连接或 refresh-token OAuth）没有共享的 `DEER_FLOW_CREDENTIALS_KEY` 就拒绝启动。

## 和本地图其他条目的关系

对 [DeepSeek Harness](deepseek-harness.md)，差别在于替你决定了多少：`dsh` 把每个部件都做成可替换插件，DeerFlow 交付的是一套有主见的主 agent 设计，想改的话可以"tear it apart"。对 [OpenHands](openhands.md)，两者都在 Web UI 后面跑沙箱里的 agent，但 DeerFlow 的重心是通用的调研与内容工作，而不是软件工程任务。对 [Hermes Agent](hermes-agent.md) 和 [OpenClaw](openclaw.md)，DeerFlow 在渠道、记忆、定时上有重叠，但它把自己定位成长周期任务的 harness，而不是个人助理。

## 结论

DeerFlow 适合想要 sub-agent、记忆、沙箱和聊天应用交付都已经拼好、并且跑在自己硬件上的团队。MIT 许可和 LangGraph 底座让它保持可改。不利的有两点：这套栈是为可信本地网络设计的，而且到目前为止每次发版都带破坏性变更。对外暴露前先读安全说明，升级时要预留真正的工作量。

## 来源

- [bytedance/deer-flow README](https://github.com/bytedance/deer-flow) · [LICENSE](https://github.com/bytedance/deer-flow/blob/main/LICENSE) · [Releases（v2.2.0，2026-11-04）](https://github.com/bytedance/deer-flow/releases) · [Install.md](https://github.com/bytedance/deer-flow/blob/main/Install.md)
- 指南：[Security Notice](https://github.com/bytedance/deer-flow/blob/main/docs/guide/security.md) · [Sandbox](https://github.com/bytedance/deer-flow/blob/main/docs/guide/sandbox.md) · [Sub-Agents](https://github.com/bytedance/deer-flow/blob/main/docs/guide/subagents.md) · [Long-Term Memory](https://github.com/bytedance/deer-flow/blob/main/docs/guide/memory.md) · [Scheduled Tasks](https://github.com/bytedance/deer-flow/blob/main/docs/guide/scheduled-tasks.md) · [IM Channels](https://github.com/bytedance/deer-flow/blob/main/docs/guide/im-channels.md) · [Configuration](https://github.com/bytedance/deer-flow/blob/main/docs/guide/configuration.md) · [TUI](https://github.com/bytedance/deer-flow/blob/main/docs/guide/tui.md) · [Configuration Reference](https://github.com/bytedance/deer-flow/blob/main/backend/docs/CONFIGURATION.md) · [`config.example.yaml`](https://github.com/bytedance/deer-flow/blob/main/config.example.yaml)
