# herdr

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](herdr.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/herdr.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：herdr 是给 coding agent 用的终端工作区管理器，一个 Rust 单文件程序，用起来像 tmux，但它知道哪个 pane 里跑着 agent，也知道这个 agent 是在工作、被卡住还是空闲。你在里面跑 Claude Code、Codex、OpenCode、Pi 等；herdr 把它们的终端保活在后台 server 里，可以跨 SSH 机器，并给脚本和其他 agent 一套 CLI 和 socket API 来启动、发 prompt、等待它们。它自己不带 agent，也不带模型。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | GitHub 组织 `herdrdev`（herdr.dev）。LICENSE 是标准的 Apache 2.0 文本，没有写版权方；提交最多的贡献者是 `ogulcancelik` |
| 路线 | 工作流 / 编排层，落在终端这一层，横跨多个 CLI agent |
| 仓库 | [`herdrdev/herdr`](https://github.com/herdrdev/herdr)：Apache-2.0，Rust，截至 2026-11-27 共 53,195 star（仓库创建于 2026-03-27） |
| 是否开源 | 是（Apache-2.0）。README 留了企业 / 合作联系方式；没有描述任何托管服务 |
| 形态 | "one rust binary, no electron"：一个后台 server 加终端客户端，支持 Linux、macOS 和 Windows，另有 `herdr` CLI、本地 socket API、插件和一个 agent skill 文件 |
| Agent | [Agents](https://herdr.dev/docs/agents/) 页列出 herdr 支持的 23 个 agent（Claude Code、Codex、GitHub Copilot CLI、Cursor Agent CLI、OpenCode、Pi、Hermes Agent、Grok CLI、Gemini CLI、Cline 等），另有五个 agent 自己向 herdr 上报状态。"Other agents still run normally in Herdr panes. They just show up as plain terminals." |
| 模型与计费 | 没有自己的。每个 agent 保留自己的模型、登录和计费；herdr "doesn't wrap or replace them; it owns their terminals." |
| 默认安全姿态 | 自己没有沙箱，也没有审批层：每个 agent 保留自己的权限模式。herdr 看到审批或提问界面时把 pane 标为 `blocked`，`agent prompt` 拒绝往被卡住的 agent 里输入。向 herdr.dev 的后台版本检查和检测 manifest 检查默认开启 |
| 最适合 | 已经同时跑好几个终端 agent、经常走 SSH，想把它们放进持久 pane、配一个状态侧栏和可脚本化控制面的开发者 |
| 主要代价 | 要学一个新的终端复用器并长期待在里面；server 或机器重启后原来的进程不会保留；最新稳定版是 v0.9.5（2026-10-14） |

## 它是什么

README 的标语是"the runtime your coding agents live on."文档说得更直白："Herdr is a terminal workspace manager. It keeps real terminal processes running and adds structure around them."它的基本单元是工作区（每个仓库或任务一个）、tab 和 pane，而"A pane is a real terminal."pane 归 server 所有；客户端可以连上、断开，`ctrl+b q` 断开时什么都不会停。

在终端复用器之上，它加了对 agent 有用的几块：

- **Agent 状态。** herdr 识别每个 pane 里的 agent，把它归为 `blocked`、`working`、`done`、`idle` 或 `unknown`，做法是拿屏幕最底部的实时内容去匹配检测 manifest，或者采用 integration 的上报。状态会汇总到侧栏里的 tab 和工作区，agent 完成或需要输入时可以弹通知（弹窗默认 `off`）。
- **自动化。** "agents drive herdr through the cli and socket api: they can spawn panes, prompt each other, and wait until another agent is genuinely blocked."核心动词是 `herdr agent start reviewer --kind codex`、`agent prompt … --wait` 和 `agent wait --until blocked`；`pane run` 和 `pane wait-output` 用来管测试、服务这类普通进程。
- **一个 agent skill。** `skills/herdr/SKILL.md` 教 coding agent 在 pane 里使用 herdr CLI，并要求它在没有设置 `HERDR_ENV=1` 时停下。
- **会话恢复。** server 重启后，herdr 恢复保存的布局；装了 integration 的话，它会把支持的 agent 重新拉起到各自原来的对话里（例如 `claude --resume <id>`、`codex resume <id>`）。原生 agent 会话恢复默认开启。
- **多台机器。** 保存过的 SSH 机器出现在同一个窗口里，"with a combined agent list and independent reconnects"；每台机器各自运行自己的 herdr server。
- **Git worktree 和插件。** 工作区行上可以创建、打开、删除 Git worktree checkout；插件通过 manifest 增加动作、事件钩子和 pane。

## 什么时候选它

- 你同时跑好几个终端 agent，总是搞不清哪个在等你。状态侧栏和 blocked 检测就是它的主工作流："start several agents, let them work in parallel, and use the sidebar to see which project needs a decision"。
- 你通过 SSH 在远程机器上干活，希望连接断了 agent 还在跑。herdr "keeps terminals running in a background server when you close the client or lose your SSH connection."
- 你想在手机上看 agent，又不想装 app。"Herdr works on your phone without a mobile app or web dashboard"：SSH 进去运行 `herdr`，TUI 会适配窄屏。
- 你想让一个 agent 把活交给另一个，或者用脚本驱动 agent，又不想引入一个框架。CLI 封装返回 JSON，`agent prompt --wait` 会阻塞到目标稳定下来。
- 你本来就熟悉 tmux 或 zellij。文档写道"The prefix is `ctrl+b`, panes persist, detach and reattach work the way you expect"，鼠标支持也默认开启。

## 什么时候不选它

- **你需要 herdr 来强制审批或隔离。** herdr 不加沙箱，权限交给每个 agent 自己。它自己的文档提醒：少见的提示界面"may initially show as `idle` instead of `blocked`"，信任这个状态的自动化"can type into an approval dialog"，而且"idle status is not authorization to approve an action."想在 agent 前面加一层策略，看 [Omnigent](omnigent.md)。
- 你想要带 diff 审阅和内置浏览器的桌面应用。herdr 跑在"whatever terminal you already use"里；这条赛道上的桌面工作台是 [Orca](orca.md)。
- 你想要任务图、目标或预算。herdr 有 pane、agent 和等待，没有工单，也没有协调者协议；[Paperclip](paperclip.md) 把 agent 组织成一家公司，带工单、预算和审批。
- 你需要运行中的进程熬过重启。server 重启后布局会回来，支持的 agent 对话也会回来，但"Snapshot restore does not preserve running shells, servers, tests, or arbitrary processes."更新时的 live handoff 是"experimental and opt-in"。
- 你不想要后台联网。`update.version_check` 和 `update.manifest_check` 默认都是 `true`，herdr 会"applies valid per-agent rule updates automatically"；在意的话把它们设成 `false`。
- 你只在一个终端里用一个 agent。直接跑 [Claude Code](claude-code.md)、[Codex](codex.md) 或 [OpenCode](opencode.md)。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| Agent 状态感知 | 很强 | 每个 pane 分 `blocked` / `working` / `done` / `idle` / `unknown`，汇总到 tab 和工作区；integration 可以直接上报状态 |
| Agent 覆盖面 | 很强 | 支持 23 个 agent，另有五个 agent 自己支持 herdr；其他 agent 当作普通终端运行 |
| 可脚本控制 | 很强 | 输出 JSON 的 CLI、带公开 schema 和事件订阅的 socket API、一个 agent skill 文件 |
| 持久性 | 强 | 断开客户端或 SSH 掉线时进程照跑；重启后布局回来、支持的 agent 恢复对话，但进程不会回来 |
| 多机器 | 强 | 保存的 SSH 机器在同一个窗口，各自独立重连；`--machine` 把 CLI 命令路由到远程 server |
| 交付面 | 中 | 你自己终端里的 TUI（包括手机 SSH 客户端）、CLI 和 socket；没有 GUI、网页或手机 app |
| 人工审批 | 弱 | 检测被卡住的 agent 并通知；审批本身仍在各 agent 自己的界面里完成 |
| 记忆 | 弱 | 自己没有；会话恢复依赖每个 agent 的原生会话 |
| 定时调度 | 弱 | 没有调度器；等待和插件只对事件做出反应 |

## 使用代价

起步低：`curl -fsSL https://herdr.dev/install.sh | sh`、`brew install herdr`、`mise use -g herdr`，Windows 上用 PowerShell 安装脚本，然后在工作所在的目录运行 `herdr`。你已经装好的 agent 一启动就会被识别。代价在于周边要装的东西。会话恢复需要每个 agent 装一个 integration（`herdr integration install claude` 等），它会把钩子或扩展写进该 agent 自己的配置。插件"run as your user, inherit your environment, and can call the full Herdr CLI"，而 herdr "does not review or sandbox plugin code"。pane 屏幕历史默认关闭，"because pane output can include secrets, tokens, prompts, and command output"；如果打开，要像对待终端历史一样对待会话目录。远程设置用你平常的 OpenSSH 认证，在远程主机上安装 herdr 或停掉那里正在运行的 server 之前会先问你；停 server 时默认答案是 No。

## 和本地图其他条目的关系

herdr 和 [Orca](orca.md) 在同一条赛道上：两者都不自带 agent，都把你已有的 CLI agent 并排跑起来并追踪哪个需要你。Orca 的做法是一个围绕 git worktree 搭建的桌面应用，带 diff 审阅、浏览器和手机伴侣 app；herdr 的做法是一个终端复用器，带持久 pane、SSH 机器和可以让 agent 来驱动的 CLI/socket API。[Paperclip](paperclip.md) 在更高一层，给 agent 角色、工单、预算、例行任务和审批。[Ruflo](ruflo.md) 在 Claude Code 之上做 swarm 和记忆；herdr 既不加记忆也不加 swarm 模型，保持与 agent 无关。

## 结论

如果你的 agent 本来就住在终端里，而问题是让它们保持存活、找到卡住的那一个、再让脚本或其他 agent 给它们派活，herdr 很合适。它开源，完全运行在你控制的机器上，把模型、计费和权限都留给每个 agent。最后这一点有两面：herdr 会告诉你某个 agent 卡住了，但它不做决定、也不强制任何东西，所以每个 agent 自己的审批设置要保持在你想要的位置。

## 来源

- [herdrdev/herdr README](https://github.com/herdrdev/herdr) · [LICENSE](https://github.com/herdrdev/herdr/blob/master/LICENSE) · [Releases（v0.9.5，2026-10-14）](https://github.com/herdrdev/herdr/releases) · [SKILL.md](https://github.com/herdrdev/herdr/blob/master/skills/herdr/SKILL.md) · [v0.9.5 文档源码](https://github.com/herdrdev/herdr/tree/master/docs/versions/0.9.5/website/src/content/docs)
- 文档：[Concepts](https://herdr.dev/docs/concepts/) · [Agents](https://herdr.dev/docs/agents/) · [Agent automation](https://herdr.dev/docs/agent-automation/) · [Agent skill](https://herdr.dev/docs/agent-skill/) · [Session state](https://herdr.dev/docs/session-state/) · [Connecting machines](https://herdr.dev/docs/connecting-machines/) · [How to work](https://herdr.dev/docs/how-to-work/) · [Integrations](https://herdr.dev/docs/integrations/) · [Plugins](https://herdr.dev/docs/plugins/) · [Configuration](https://herdr.dev/docs/configuration/) · [Config reference](https://herdr.dev/docs/config-reference/) · [Socket API](https://herdr.dev/docs/socket-api/) · [Install](https://herdr.dev/docs/install/)
