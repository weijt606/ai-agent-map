# Grok Build

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](grok-build.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/grok-build.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话判断：Grok Build（`grok`）是 SpaceXAI 官方的终端 coding agent——Rust 写的全屏 TUI，能改代码、跑 shell、搜网页、管理长任务，同时还能在 CI 里 headless 运行、或通过 ACP 嵌进编辑器。

> **命名与边界：** 二进制叫 `grok`，产品叫 **Grok Build**，仓库是 [`xai-org/grok-build`](https://github.com/xai-org/grok-build)、域名 `x.ai`——但 README、logo 和文档把厂商标成 **SpaceXAI**。把 "xAI" 和 "SpaceXAI" 当作同一个厂商来看。构建产物名为 `xai-grok-pager`，官方安装包发出来时叫 `grok`。

> **源码可见，但不是社区共建。** Apache-2.0 许可是真的，但这个仓库是*从 SpaceXAI monorepo 周期性同步*出来的（根目录 `SOURCE_REV` 文件记录上游 commit），而且 `CONTRIBUTING.md` 明说**不接受外部贡献**。你可以读、可以 fork、可以自己构建；但你无法把改动合回上游。这和"fork 了就归你"的 harness 交易正好相反。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | SpaceXAI / xAI（`xai-org/grok-build`，x.ai/cli） |
| 路线 | 直接执行——厂商官方终端 coding agent |
| 开源 | Apache-2.0（源码可见；不接受外部贡献） |
| 实现 | Rust |
| 许可证 | Apache-2.0（一方代码）；vendored 三方代码沿用原许可证 |
| 模型 | Grok——首次启动时浏览器 OAuth 登录 SpaceXAI 账号 |
| 适合 | 已经在用 Grok 模型、想要一个快速的一方 TUI，并且要 headless CI 和编辑器（ACP）触达的开发者 |
| 主要代价 | 才两周大且绑定厂商；顶着 OSS 许可证但你无法向上游贡献 |
| GitHub 仓库 | https://github.com/xai-org/grok-build |

## 什么时候选它

- 你本来就在用 Grok/SpaceXAI 的模型，想要 agent 循环和模型出自同一个团队，而不是拿第三方 harness 去接 xAI 的 endpoint。
- 你想要一个二进制覆盖三种模式：交互式全屏 TUI（支持鼠标、可换主题）、脚本和 CI 用的 **headless** 执行、以及让 ACP 编辑器来驱动它的 **ACP** agent server——和 [Kimi Code](kimi-code.md) 在月之暗面那边给出的三面形态一样。
- 你想要这一代该有的扩展面——MCP server、skills、插件、hooks、slash 命令——而且沙箱和工作区 checkpoint 是做进运行时的，不是外挂的。
- 你想要 Rust 实现带来的启动速度和低占用，像 [jcode](jcode.md) 那样，但来自厂商而不是独立项目。

## 什么时候别选它

- 你想拥有并改造这个循环——许可证允许你 fork，但开发是封闭的、这棵树只是 monorepo 的导出，所以你的改动会永远活在下游。要 fork 就归你，那是 [Pi](pi.md)、[jcode](jcode.md) 或 [OpenHands](openhands.md)。
- 你把厂商中立当作核心价值。Grok Build 设计上就是登录 SpaceXAI 账号；如果你经常换模型，[Pi](pi.md)、[jcode](jcode.md) 或 [Aider](aider.md) 这种厂商无关的底座更稳。
- 你今天就需要成熟稳定的界面——这个仓库才两周大，还在快速变动。
- 你需要云端委派、定时后台运行或并行远端 agent——那是 [Codex](codex.md)、[Devin](devin.md) 或 [Claude Managed Agents](claude-managed-agents.md) 的地盘。

## 能力形态

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 终端工作流 | 很强 | 全屏、支持鼠标的 TUI，带 scrollback、弹窗、主题、slash 命令 |
| 代码执行 | 很强 | shell 执行、文件编辑、搜索都是一等工具；沙箱和工作区 checkpoint 内建在运行时里 |
| Grok 模型调优 | 很强 | 一方出品；agent 和模型出自同一厂商 |
| 交互面 | 强 | 一个二进制三种模式——交互 TUI、headless（脚本/CI）、以及给编辑器用的 ACP agent server |
| 扩展性 | 强 | MCP server、skills、插件、hooks——但扩展只能长在一棵你无法向上游提交的树旁边 |
| 厂商中立 | 非目标 | 浏览器 OAuth 登录 SpaceXAI 账号是默认且文档化的路径 |
| 社区共建 | 非目标 | 明确不接受贡献；仓库是 monorepo 的周期性同步 |

## 血缘说明

根据仓库自己的 `THIRD-PARTY-NOTICES` 以及 `xai-grok-tools` 里的 crate 级声明，Grok Build 带有 **[`openai/codex`](codex.md) 和 `sst/opencode` 工具实现的 in-tree 源码移植**，并附了 Apache §4(b) 的修改声明。在比较工具行为时这点值得知道：工具层不是净室设计，如果你用过 Codex，它的一些语义会让你觉得眼熟。

## 使用成本

*用*起来复杂度低到中，*依赖*它则更高。安装是一行脚本（`curl -fsSL https://x.ai/cli/install.sh | bash`，Windows 用 PowerShell），macOS/Linux/Windows 都有预编译二进制，首次启动在浏览器里完成鉴权。从源码构建比大多数项目重：需要固定版本的 Rust 工具链，外加 **DotSlash** 来跑 hermetic 工具（`protoc`），根 `Cargo.toml` 是生成的、只读，而且 Windows 源码构建属于尽力而为。真正的战略成本是治理形态——一棵两周大、厂商控制、你无法贡献的树，所以每一处本地改动都是永久的下游 diff。

## 结论

Grok Build 是"我想要 Claude-Code 那种终端 agent，但要 Grok 原生、而且是 Rust"这个需求的官方答案。它出场异常响亮——两周内 23k star、4.4k fork——而且内容是实的：打磨过的 TUI、headless CI 模式、ACP 编辑器触达、MCP/skills/插件/hooks，还有沙箱。但要仔细读它的治理：这里的 Apache-2.0 意味着*源码可见*，不是*社区共建*，而且模型路径指向 SpaceXAI。如果你想要同样的 Rust 级速度、但循环真正归你，看 [jcode](jcode.md) 或 [Pi](pi.md)；其他模型栈上的官方对应物，看 [Codex](codex.md)、[Claude Code](claude-code.md)、[Kimi Code](kimi-code.md) 和 [MiMoCode](mimocode.md)。路线级对比见 [coding CLI agent](../comparisons/coding-cli-agents.md)。
