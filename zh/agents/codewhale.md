# CodeWhale

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](codewhale.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/codewhale.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：CodeWhale（原 DeepSeek-TUI）是一个用 Rust 写的开源终端 coding agent——形态和 Claude Code 或 Codex CLI 一样——起步时只支持 DeepSeek，现在自称 provider 中立：40 多条内置 provider 路线、任意 OpenAI 兼容端点，以及通过 Ollama、vLLM、SGLang 跑本地模型。DeepSeek 仍是默认 provider，但已经不是它的卖点。

> **更名（2026 年 5 月底）：** 项目从 `Hmbown/DeepSeek-TUI` 改名为 `Hmbown/CodeWhale`，并从只支持 DeepSeek 扩展到 **DeepSeek + MiMo**（小米开源模型），同时上线了产品官网 [codewhale.net](https://codewhale.net/)。旧的 `DeepSeek-TUI` 链接会自动重定向。

> **搬家并重新定位（2026 年 10 月，2026-10-14 更正）：** 仓库现在在 [`codewhale-hq/Codewhale`](https://github.com/codewhale-hq/Codewhale)（搬家发生在 2026-10-07 那次抓取之前，本地图晚了一个窗口才注意到），自己的写法变成了"Codewhale"，README 写明它"provider 中立、独立维护，不隶属于任何模型厂商"。本 profile 此前把它描述为 DeepSeek/MiMo 原生、主要代价是绑定较窄模型集的 agent；下面已就地改正。引擎现在和终端客户端分开（"agent engine and terminal client"），`codewhale login` 账号可以集中保管 provider key，v0.10.1 于 10 月 8 日发布。旧的 `Hmbown/*` 链接会重定向。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | codewhale-hq（开源社区，"独立维护"；此前挂在 Hmbown 下） |
| 路线 | 直接执行——终端 coding agent |
| 开源 | 是——MIT |
| 实现 | Rust（引擎 + 终端客户端）；可从 npm 与 crates.io 安装 |
| 模型 | 任意——40 多条 provider 路线（Anthropic、DeepSeek、Google、Mistral、Moonshot、OpenAI、OpenRouter、xAI……）、OpenAI 兼容端点、本地运行时。**DeepSeek 仍是默认 provider** |
| 适合谁 | 想要 Claude Code 风格的循环、又想指向当下最便宜或自己能用的模型——包括国产栈和本地模型——而不想用某家厂商自己 CLI 的开发者 |
| 主要代价 | 社区项目，表面变化快，还有一层可选的账号；provider 越宽，循环的质量越取决于你接进去的模型 |
| GitHub 仓库 | https://github.com/codewhale-hq/Codewhale |

## 什么时候选它

- 你想要一个不绑定某家模型线的终端 coding agent，而且切换 provider（或跑本地模型）频繁到会话内的 `/provider` 与 `/model` 真有用。
- 你想在 Claude Code 形态的循环里一等公民地用 DeepSeek、Moonshot 或 MiMo，但又想保留不换工具就切到 Anthropic 或 OpenAI 路线的选项。
- 你倾向于极简终端表面，而不是桌面或 IDE 体验，并且想要明确的模式（Plan 只看不改，Work 与 Operate 才改）、审批姿态、`/undo` 与 `/restore`，以及每次会话的收据。

## 什么时候不选

- 你想要厂商自己维护、带稳定承诺的客户端——[Claude Code](claude-code.md)、[Codex](codex.md)、[Gemini CLI](gemini-cli.md) 都由模型厂商自己维护。
- 你想要一个可以往上搭的 harness，而不是一个成品 agent——[Pi](pi.md) 或 [Aider](aider.md) 把循环暴露得更多。
- 你需要云端委派、并行 agent 或后台运行——那是 [Codex](codex.md) 或 [Devin](devin.md) 的领地。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 终端工作流 | 强 | TUI 原生循环；Plan / Work / Operate 模式；每个文件、命令、审批都有收据 |
| 多 provider 支持 | 强 | 40 多条路线，外加 OpenAI 兼容与本地；本 profile 在 2026-10-14 之前写的是"弱"，已经过时 |
| DeepSeek / MiMo 调优 | 强 | 项目的起点；DeepSeek 仍是默认 provider，并且仍读 `deepseek-tui` 的配置和会话 |
| 后台执行 | 不是目标 | 前台、单开发者循环 |

## 使用成本

复杂度：低-中。安装很简单（npm 或 crates.io）；模型账单就是你路由到的那个 provider 的价格，没有加价。可选的 Codewhale 账号替你在已登录设备间保管 provider key；不登录也能本地用。价格风险跟着你选的 provider，不跟着 agent。

## 底线

CodeWhale 当初以 DeepSeek-TUI 之名、作为一个 DeepSeek 原生终端 agent 出现在本仓库的热门快照里。现在它押的是相反的一注：一个 provider 中立的 Claude Code 形态循环，默认仍是 DeepSeek，但把每一条路线——包括本地运行时——都当一等公民。如果你想用一个终端 agent 横跨几家模型厂商，或者想用国产模型又不放弃其他家的选项，这是最直接的路径。如果你要的是厂商自己的客户端，就选厂商自己的客户端。
