# oh-my-pi

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](oh-my-pi.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/oh-my-pi.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：oh-my-pi（`omp`）是 Stencil Labs 出的终端编码 agent，从 [Pi](pi.md) fork 而来，把 Pi 留给扩展去做的部分直接补齐了：LSP 和调试器工具、subagent、可选的审查模型、实时会话共享，以及需要手动开启的记忆。它默认不弹任何审批（`yolo`），所以在让它碰你在乎的东西之前，先把审批模式设好。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Stencil Labs。README 写着"Built by Stencil Labs"；LICENSE 的版权方是 Mario Zechner（2025）、Can Bölük（2025-2026）和 Stencil Labs, Inc.（2026） |
| 路线 | 直接执行（终端编码 agent） |
| 仓库 | [`can1357/oh-my-pi`](https://github.com/can1357/oh-my-pi)：MIT，TypeScript 加 Rust 原生内核，截至 2026-11-27 共 40,027 star（仓库创建于 2025-12-31） |
| 与 Pi 的关系 | 是 fork。README 写着"Fork of Pi by @mariozechner"，链接到 `badlogic/pi-mono`，这个地址现在跳转到 `earendil-works/pi`，也就是本地图 [Pi](pi.md) 条目对应的仓库。GitHub 没有把它标成 fork，它是一个独立仓库 |
| 是否开源 | 是（MIT）。PR 目前作为试行"temporarily open to everyone"，README 也提醒"the vouch system may return" |
| 形态 | CLI 和 TUI（`omp`）、一次性模式（`omp -p`）、Node SDK、基于 stdio 的 RPC 模式，以及给编辑器用的 ACP server；npm 包名 `@oh-my-pi/pi-coding-agent` |
| 模型与计费 | 自带 provider。README 列出了 API key 类 provider、`oauth`（"signs in with your provider account"）、`plan`（"routes through a coding-plan subscription"），以及 key 可选的 `local` 本地服务 |
| 默认模型 | 没有固定默认值。启动时依次取 `--model`、已保存的默认值，再在你有凭据的 provider 里取"known provider defaults"。`e95d0dd` 提交里的模型目录给 `anthropic` 设的是 `claude-opus-5-5`，`openai` 和 `openai-codex` 是 `gpt-5.5`，`google` 是 `gemini-3.1-pro-preview`。`omp setup` 里有一步专门选默认模型 |
| 最适合 | 想要一个基于 Pi、已经自带语言服务器、调试器、subagent 和大量 provider 的终端 agent 的开发者 |
| 主要代价 | 默认审批模式是 `yolo`，设置表对它的描述是"auto-approve all tiers"，也没有操作系统沙箱。打开一个仓库时还会"by design"加载它的扩展、hook 和 MCP 配置 |
| 文档 | [omp.sh/docs](https://omp.sh/docs) · [仓库 docs](https://github.com/can1357/oh-my-pi/tree/main/docs) |

## 它是什么

README 称它为"A coding agent with the IDE wired in."，还把项目描述为"a fork of Pi by Mario Zechner, rewritten as a coding-first surface"，以及"extended with a batteries-included coding workflow."。README 给出的数字是"60+"个 provider、"31"个内置工具。对几个入口，它自己的说法是"Same engine, four wrappers"：TUI、`omp -p`、Node SDK，以及 `omp --mode rpc` / `omp acp`。

围绕 agent 循环，它配了：

- **代码智能**：`lsp` 工具负责诊断、跳转、重命名和 code action；`debug` 工具驱动 DAP 会话（断点、单步、线程、变量）。
- **执行**：`bash` 工具背后是它自己的 bash 5.3 引擎，coreutils 在进程内运行；`eval` 工具提供"persistent Python and JavaScript cells"，并能回调 agent 自己的工具。
- **Subagent**：`task` 工具把工作分给 subagent。`task.maxConcurrency`"defaults to `32`"。有隔离工作区，但 `task.isolation.enabled` 默认是 `false`，没写 `isolated: true` 的任务"share the parent checkout"。**Agent Hub**（`Alt+A`）显示每个 subagent 的活动，可以给它发引导消息或直接结束它。
- **Advisor**：放在 `advisor` 角色上的第二个模型"reads every turn the main agent takes"，并插入批注。`advisor.enabled` 默认 `false`，文档也说明 advisor"does not approve actions"。
- **Collab**：`/collab` 通过中继共享一个实时会话。"Guests can prompt and interrupt the agent; the host machine runs the agent and all tools." 默认中继是 `wss://my.omp.sh`，文档说生产中继"is not currently distributed for self-hosting"。
- **记忆**：五种模式（`off`、`local`、`hindsight`、`mnemopi`、`sharpshooter`）。"Memory is disabled by default."
- **桌面与网页**：`browser` 工具、默认关闭的宿主桌面 `computer` API，以及覆盖 25 个已列出后端的 `web_search`。

## 什么时候选它

- 你想让 agent 用上语言服务器和真正的调试器。`lsp` 和 `debug` 是内置的，不是扩展。
- 你想要开箱即有的 subagent，带一个能观察和引导它们的 hub，每个任务还可以选用隔离工作区。
- 你想自由切换 provider。README 列出了前沿 API、编码套餐订阅和本地服务（Ollama、LM Studio、llama.cpp、vLLM），还能在 `~/.omp/agent/models.yml` 里自定义兼容 OpenAI 的 provider，并支持按角色分配模型和 fallback 链。
- 你想终端和编辑器共用一个 agent。`omp acp` 讲 Agent Client Protocol，README 点名了 Zed。
- 你的仓库里已经有 `AGENTS.md`、`CLAUDE.md`、`.claude/`、`.codex/` 或 `opencode.json`。README 说 omp 会读这些项目文件，但"never reads another tool's `~/` config"。
- 你是从 [Pi](pi.md) 起步的，想要它的底座外加这些已经装好的部件。

## 什么时候不选它

- **你期望默认就在高风险操作前弹审批。** `tools.approvalMode` 默认是 `yolo`。可以改成 `always-ask`、`always-ask-cached` 或 `write`，`tools.restrictedFolders` 则会"whatever the approval mode (`yolo` and `--auto-approve` included)"强制弹出审批。在 `yolo` 下，`bash` 里单独的高危命令 override"is ignored"。
- **你需要隔离。** 文档说 bash 的模式规则"not process or filesystem containment"，"Extensions are not sandboxed"，`computer.run` 的只读标志"is not a sandbox"。不打开隔离的话，subagent 和父会话共用同一个 checkout。
- **你会打开不信任的仓库。** "Opening a repository loads its project inputs by design: settings, extensions, hooks, tools, commands, skills, rules, and project MCP configuration." `--no-extensions` 之类的参数能收窄范围，但 README 说它们这样做"without changing the repository-trust model."
- 你需要定时或后台运行。文档里没有描述 cron 或调度器，SDK、RPC 和 print 会话在所有者主动开启之前也不会启动空闲任务。
- 你希望第一次会话就有记忆。得先选一个后端。
- 你想要一个能从头读到尾的小 harness。那是 [Pi](pi.md) 的卖点；omp 加了一个 README 估算为"~80k"行的 Rust 内核。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 工具调用 | 很强 | LSP、DAP 调试器、AST 编辑与搜索、浏览器、覆盖 25 个后端的网页搜索、MCP、扩展、skill |
| 代码执行 | 很强 | 内置 bash 引擎和进程内工具集，持久化的 Python 与 JavaScript `eval` cell，能回调工具 |
| 多 agent | 强 | `task` 分发（默认并发 32 个）、Agent Hub、`orchestrate` 和 `workflowz` 关键词；隔离需手动开启 |
| 交付面 | 强 | TUI、一次性模式、Node SDK、RPC、面向编辑器的 ACP、通过 `/collab` 的浏览器访客 |
| 人工审批 | 中 | 四种审批模式、按工具的策略和受限目录，但默认是 `yolo` |
| 记忆 | 中 | 四种后端（外加 `off`），带 retain、recall、learn 工具，默认全部关闭 |
| 定时调度 | 弱 | 文档里没有描述调度器 |
| 治理 | 中 | MIT，PR 作为可能撤回的试行对所有人开放 |

## 使用代价

起步低：`curl -fsSL https://omp.sh/install | sh`、`brew install can1357/tap/omp`、`bun install -g @oh-my-pi/pi-coding-agent`、Nix、PowerShell 或 mise 都行。README 写的是"macOS · Linux · Windows · bun ≥ 1.4.4"。然后加一个 provider key，或用 `/login` 登录。状态存在 `~/.omp`。成本在配置上：要审批就得改审批模式，要每个 subagent 有独立 checkout 就得开隔离，要记忆就得选后端。发版很频繁：`v19.2.0` 和 `v19.2.1` 都在 2026-11-25 发布。Collab 会话走 `my.omp.sh` 上的托管中继，目前不能自托管；README 说"Frames are sealed client-side; the relay never sees your keys."

## 和本地图其他条目的关系

omp 和 [Claude Code](claude-code.md)、[OpenCode](opencode.md) 同在直接执行路线上：一个跑在你自己机器上的终端编码 agent。它的底座是 [Pi](pi.md)，而本地图把 Pi 归在"自己掌控循环"的 harness 里。这条分界线来自两边各自的 README。Pi 的条目描述的核心是 read、write、edit、bash，并写着"The point is to leave orchestration to the caller"；omp 则说它补上了"everything you're missing"，把 subagent、LSP、调试器和记忆都做成内置。omp 仍然保留了 Pi 式的积木（SDK、RPC、扩展），所以想自己掌控循环就从 Pi 开始；想要这些部件已经接好，就从这里开始。它还会读 OpenCode 的 `opencode.json` 和 Claude Code 的 `.claude/` 项目文件，在现有仓库里试用的成本因此更低。

## 结论

如果你想要一个基于 Pi、把 IDE 那部分能力装在里面的编码 agent——语言服务器、调试器、subagent、审查模型和大量 provider——oh-my-pi 很合适。它的默认值信任你，也信任仓库：不弹审批、没有操作系统沙箱、subagent 共用同一个 checkout、打开仓库就加载项目扩展。在用它处理重要代码之前，先设好 `tools.approvalMode` 和 `tools.restrictedFolders`。

## 来源

- [can1357/oh-my-pi README](https://github.com/can1357/oh-my-pi) · [LICENSE](https://github.com/can1357/oh-my-pi/blob/main/LICENSE) · [Releases（v19.2.1，2026-11-25）](https://github.com/can1357/oh-my-pi/releases) · [CHANGELOG](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/CHANGELOG.md) · [provider 目录默认值](https://github.com/can1357/oh-my-pi/tree/main/packages/catalog/src/compat/rules/providers) · [task 设置](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/src/task/settings.ts)
- 文档：[Approval mode](https://github.com/can1357/oh-my-pi/blob/main/docs/approval-mode.md) · [Settings](https://github.com/can1357/oh-my-pi/blob/main/docs/settings.md) · [Models](https://github.com/can1357/oh-my-pi/blob/main/docs/models.md) · [Memory](https://github.com/can1357/oh-my-pi/blob/main/docs/memory.md) · [Task tool](https://github.com/can1357/oh-my-pi/blob/main/docs/tools/task.md) · [Advisor](https://github.com/can1357/oh-my-pi/blob/main/docs/advisor-watchdog.md) · [Collab](https://github.com/can1357/oh-my-pi/blob/main/docs/collab.md) · [Extension loading](https://github.com/can1357/oh-my-pi/blob/main/docs/extension-loading.md) · [Computer use](https://github.com/can1357/oh-my-pi/blob/main/docs/computer-use.md) · [SDK](https://github.com/can1357/oh-my-pi/blob/main/docs/sdk.md) · [omp.sh](https://omp.sh)
