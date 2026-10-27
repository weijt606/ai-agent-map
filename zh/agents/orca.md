# Orca

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](orca.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/orca.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：Orca 是一个开源桌面应用，用来同时跑好几个 coding agent。CLI agent 和订阅都用你已经在付费的那些（Claude Code、Codex、OpenCode、Pi，以及任何其它 CLI agent），Orca 给每个 agent 分配独立的 git worktree、终端和浏览器，再把它们放在同一个窗口和一个手机配套应用里统一追踪。它自己不带 agent，是 agent 干活的工作台。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | Stably AI（`stablyai/orca`，onorca.dev；官网写"Backed by Y Combinator"）。LICENSE 文件里的版权方是 Lovecast Inc. |
| 路线 | 工作流 / orchestration layer，横跨多个 CLI agent，而不是架在某一个之上 |
| 仓库 | [`stablyai/orca`](https://github.com/stablyai/orca)：MIT，TypeScript，截至 2026-10-28 共 107.8k star |
| 开源 | 是（MIT）。桌面应用、手机应用，以及把两者配对起来的中继服务都在仓库里 |
| 形态 | macOS、Windows、Linux 桌面应用；iOS 和 Android 配套应用（beta）；无界面的 `orca serve` 运行时；`orca` CLI |
| 支持的 agent | "Works with any CLI agent"：README 列了三十多个，包括 Claude Code、Codex、Grok、Cursor、GitHub Copilot、Antigravity、OpenCode、Pi、Hermes Agent、Goose、Kimi、Qwen Code 和 DeepSeek Harness |
| 模型与计费 | 用你自己的 agent 订阅或 key："Plug in the subscriptions you already have and run them side by side." 内置账号切换和 Claude / Codex 用量追踪 |
| 价格 | 官网写"Free and open source"。Enterprise 页面提供落地支持，价格要联系销售；没有描述托管方案，文档明确说 Orca "does **not** sell managed VPS hosting" |
| 适合谁 | 已经在跑两个以上 coding agent、想把它们放进并行 worktree，并在一个地方完成评审、浏览器调试和手机提醒的开发者 |
| 主要代价 | 你和 agent 之间又多一个应用，而且几乎每天发版；编排、Cloud VM 和远程服务器都标着 experimental 或 beta |

## 它是什么

Orca 的 README 把自己叫作"The AI Orchestrator for 100x builders"，官网叫它"The agent development environment"。实际上它是一个长得像编辑器的桌面应用，基本单位是 git worktree：把同一个 prompt "fan … across five agents, each in its own isolated git worktree"，比较结果，合并最好的那个。围绕这一点，它把平时散在别的窗口里的东西收了进来：

- **终端**：WebGL 渲染、可任意分屏、重启后滚动记录还在。
- **评审**：diff 视图里可以"drop comments on any diff line and ship them back to the agent"，应用内还能看 GitHub PR 和 issue，以及 Linear、Jira 的条目。
- **每个 worktree 一个 Chromium 浏览器**，带 Design Mode：点中页面元素，就把它的 HTML、CSS 和一张裁剪截图送进 agent 的 prompt。
- **Monaco 编辑器**，自动保存；文件和图片可以直接拖进 prompt。
- **通知**：能区分 agent 是做完了，还是在等你。

## 它怎么跑 agent

每个 worktree 都要在某台机器上跑，[Ways to run Orca](https://www.onorca.dev/docs/ways-to-run) 页面列了四种：

| 模式 | agent 跑在哪 |
| --- | --- |
| 本地 | 你的桌面电脑 |
| SSH 目标 | 一台通过 SSH 连的主机；编辑器和界面留在笔记本上 |
| Remote Orca Server（beta） | 一台你自己控制、运行 Orca 桌面版或 `orca serve` 的机器；笔记本、网页和手机客户端都配对到它，笔记本睡眠后 agent 照样在跑 |
| Cloud VM（experimental） | 每个 worktree 一个一次性沙箱、虚拟机或 Docker 容器，由仓库里的 `orca.yaml` recipe 在你自己的云账号上启动（文档点名了 Vercel Sandbox、Fly、Modal、SSH 主机和本地 Docker） |

有两项功能让它从窗口管理器变成了编排层：

- **Orchestration**（experimental，默认关闭，要在 Settings → Experimental 打开）：一个协调者 agent 开一个持久的"Run"，定义带依赖关系的任务，把任务派给各自 worktree 里的 worker agent，再通过收件箱接收 `worker_done`、心跳和提问消息。"Decision gate"会把任务卡住，直到有人做出决定。
- **定时自动化**：用 `orca` CLI 创建自动化，触发方式可以是预设（`hourly`、`daily`、`weekdays`、`weekly`）、cron 表达式或 RRULE 字符串，在指定的仓库或 worktree 里运行，存放在本机或已连接的 Orca 主机上。

**手机配套应用**是遥控器，不是编辑器：能看所有已连接主机上的每个 worktree 和 agent 状态，回复正在等你的 agent、附上文件、在源码管理里提交、切换 agent 账号，并在 agent 做完时收到推送。手机通过中继连到桌面；中继的源码在仓库的 `cloud/` 目录里，而它的部署"is owned by the private `stablyai/orca-cloud` repository"。

## 什么时候选它

- 你已经在用不止一个 CLI agent，或者同一个 agent 开好几个会话，正在手工倒腾终端和分支。并行 worktree 加统一状态视图就是这个产品的核心。
- 你想让几个 agent 在同一个任务上赛跑，留下最好的结果。文档把这做成了现成的 recipe（"Race three agents on the same task"）。
- 你想把 agent 放在家里的服务器或 VPS 上一直跑，用手机看进度。Remote Orca Server 加手机配套应用就能做到，不用自己搭，而且跑在你自己的硬件上。
- 你付的是 Claude 或 Codex 订阅而不是 API key，想原样用起来。Orca 启动的是厂商自己的 CLI，并追踪它们的用量和限额重置时间。

## 什么时候不选它

- 你只在一个终端里用一个 agent，而且很满意。直接用 [Claude Code](claude-code.md)、[Codex](codex.md) 或 [OpenCode](opencode.md)。
- 你需要一层策略，在所有 agent 前面统一执行审批和花费上限。Orca 把权限交给每个 agent 自己的设置；[Omnigent](omnigent.md) 才是在每个 harness 前面加审批和花费策略的那种。
- 你想按团队来管 agent，有目标、预算和组织架构，而不是按 worktree 管。那是 [Paperclip](paperclip.md)。
- 你需要稳定的接口。它几乎每天发版（`v1.4.239` 到 `v1.4.242` 在 2026 年 10 月 24 日到 27 日之间发布），多 agent 编排、Cloud VM 和 Remote Orca Server 都标着 experimental 或 beta。
- 你想留在现有的编辑器里。Orca 是独立的桌面应用；想在常用编辑器里直接用 agent，看 [Cursor](cursor.md) 或 [Cline](cline.md)。

## 能力形态

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 并行执行 | 非常强 | 每个 agent 一个 worktree、终端和浏览器；可跑在本地、SSH、远程服务器或每个 worktree 一台 Cloud VM |
| agent 覆盖面 | 非常强 | 任何 CLI agent；README 点名了三十多个 |
| 交付界面 | 非常强 | 三大系统的桌面版、iOS / Android 配套应用、连远程服务器的网页客户端，以及 CLI |
| 评审 | 强 | diff 批注发回给 agent，应用内看 GitHub / Linear / Jira |
| 多 agent 协同 | 中 | 有协调者 / worker 协议，但还是 experimental，默认关闭 |
| 调度 | 中 | CLI 里的 cron / RRULE 自动化 |
| 记忆 | 弱 | `CLAUDE.md` 和 `AGENTS.md` 交给 agent 自己管；它提供的是会话恢复和历史，不是记忆 |
| 治理 | 弱 | 没有跨 agent 的审批或预算策略；每个 agent 沿用自己的权限模式 |

## 使用成本

起步成本低：下载桌面安装包，或者 `brew install --cask stablyai/orca/orca`（README 提醒裸写 `orca` 会装到另一个不相干的 cask），然后指向你已经装好的 agent。远程模式的成本会往上走：Remote Orca Server 要求每个 agent CLI 都在服务器上装好并登录，文档建议机器之间用 Tailscale，而配对链接"grants access to this Orca runtime"，要"like a password"一样对待。Orca 会收集匿名使用遥测，退出方法写在它的[隐私与遥测页面](https://www.onorca.dev/docs/telemetry)。

## 结论

Orca 是给你已有 agent 用的驾驶舱，不是又一个 agent。同时跑好几个 agent 之后会冒出来的那堆活，它都接住了：隔离的 worktree、状态面板、评审、浏览器，还有一部会告诉你哪个跑完了的手机。全部是 MIT，所有远程模式都跑在你自己的机器上。它的多 agent 协同比较新，还标着 experimental，所以选 Orca 是为了今天把 agent 并排跑起来，而不是为了一支受监督的 agent 团队。同样是"多个 harness、一层统一"但带策略引擎的，看 [Omnigent](omnigent.md)；想按组织来管 agent、有目标和预算的，看 [Paperclip](paperclip.md)。

## 来源

- [stablyai/orca README](https://github.com/stablyai/orca) · [LICENSE](https://github.com/stablyai/orca/blob/main/LICENSE) · [Releases（v1.4.242，2026-10-27）](https://github.com/stablyai/orca/releases) · [中继 README（`cloud/`）](https://github.com/stablyai/orca/blob/main/cloud/README.md)
- [onorca.dev](https://www.onorca.dev) · [Enterprise](https://www.onorca.dev/enterprise) · 文档：[Ways to run Orca](https://www.onorca.dev/docs/ways-to-run) · [Remote Orca Servers](https://www.onorca.dev/docs/remote-servers) · [Orchestration](https://www.onorca.dev/docs/cli/orchestration) · [Scheduled automations](https://www.onorca.dev/docs/cli/automations) · [Mobile companion](https://www.onorca.dev/docs/mobile) · [Agent hooks & memory](https://www.onorca.dev/docs/agents/hooks-memory)
