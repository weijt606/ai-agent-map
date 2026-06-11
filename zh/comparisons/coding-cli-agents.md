# 终端编码 CLI Agent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](coding-cli-agents.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/coding-cli-agents.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

这一页对比的是一类解决同样形态问题的项目：**终端原生 coding agent**——你在 shell 里跑的单进程循环，读写代码、执行命令、根据反馈迭代。

这个品类在 2026 年爆发。每个主流模型厂商现在都出了自己 Claude Code 形态的 CLI，再加上开源和国产栈的入局者。它们表面几乎一样；真正的差异是为哪些模型调优、谁来维护，以及各自有哪一件事做得比别人好。

## 这里算「coding CLI」的标准

收录范围：前台、单开发者、主要工作是写代码的终端循环。不在此范围、在别处覆盖的：

- **编辑器中心表面** —— [Cursor](../agents/cursor.md)、[Windsurf](../agents/windsurf.md)、[Continue](../agents/continue.md)（编辑器本身是 agent，而不是终端）。
- **云端委派 / 托管执行** —— [Devin](../agents/devin.md)、[Jules](../agents/jules.md)、[Claude Managed Agents](../agents/claude-managed-agents.md)（你交出去再回来查，不是前台循环）。
- **可 fork 自有的 harness 框架** —— [Pi](../agents/pi.md)、[OpenHands](../agents/openhands.md)、[SWE-agent](../agents/swe-agent.md)（见 [harness 框架一览](../README.md#agent-harness-框架一览)）。Pi 是终端优先、能写代码，但它的价值是拥有循环，而不是采用一个厂商产品。

## 一页对比

| 项目 | 厂商 | 模型（默认） | 语言 / 许可 | 最擅长的一件事 |
| --- | --- | --- | --- | --- |
| [Claude Code](../agents/claude-code.md) | Anthropic | Claude（Opus / Sonnet） | 闭源 | 参考实现——最深的 IDE/桌面/web 触达，最丰富的 skills + 插件生态 |
| [Codex](../agents/codex.md) | OpenAI | GPT-5.x | CLI 开源 | 在同一产品表面把终端循环和隔离云端委派、并行 agent 结合 |
| [Aider](../agents/aider.md) | 开源 | 自带模型 | Python / Apache-2.0 | 以 git 为中心、显式 diff、完全的模型自由 |
| [Kimi Code](../agents/kimi-code.md) | Moonshot AI | Kimi（K2） | TypeScript / MIT | 第一方 Kimi 循环，通过 ACP + VS Code 插件有强 IDE 触达 |
| [MiMoCode](../agents/mimocode.md) | 小米 | MiMo（MiMo Auto） | TypeScript / MIT | 内置持久跨会话记忆——跨多次运行保留项目理解 |
| [CodeWhale](../agents/codewhale.md) | Hmbown（社区） | DeepSeek + MiMo | Rust / 开源 | Claude Code 形态重新围绕低成本国产模型搭建，国产模型当一等公民 |

> 厂商官方 CLI（Claude Code、Codex、Kimi Code、MiMoCode）把模型和循环一起调优。第三方/社区 CLI（Aider、CodeWhale）用这点换取可移植性或特定的成本/模型目标。

## 怎么选

1. **从你想跑的模型出发。** 如果你绑定某厂商的模型，它的第一方 CLI 通常是调得最好的路径：Claude → [Claude Code](../agents/claude-code.md)，GPT-5.x → [Codex](../agents/codex.md)，Kimi → [Kimi Code](../agents/kimi-code.md)，MiMo → [MiMoCode](../agents/mimocode.md)，想省钱跑 DeepSeek/MiMo → [CodeWhale](../agents/codewhale.md)。
2. **如果模型自由比调优更重要，** 选 provider 中立的底座：要成品 CLI 就用 [Aider](../agents/aider.md)，想拥有循环就上 [Pi](../agents/pi.md) harness。
3. **如果单仓库长程记忆是痛点，** [MiMoCode](../agents/mimocode.md) 内置的跨会话记忆是最清晰的差异点；否则给任意 CLI 配上 [CodeGraph](../agents/codegraph.md) 做代码上下文索引。
4. **如果你需要云端委派或后台运行，** 这些前台循环都不合适——去 [Codex](../agents/codex.md)（云端那侧）、[Jules](../agents/jules.md) 或 [Devin](../agents/devin.md)。

## 三个别搞混的点

- **厂商 CLI 不只是一个模型端点。** Claude Code、Kimi Code、MiMoCode 把 agent 循环、工具和 prompt 围绕自家模型调优——这就是它相对于"拿通用 harness 指向同一个 API"的价值。
- **MiMoCode 不是 [CodeWhale](../agents/codewhale.md)。** MiMoCode 是小米第一方 CLI；CodeWhale 是包装 DeepSeek + MiMo 的社区 Rust TUI。它们共享一个模型家族，不共享代码库。
- **coding CLI 不是 harness。** 如果你想端到端 fork、审计、拥有循环，那是 [Pi](../agents/pi.md) / [OpenHands](../agents/openhands.md) 的领地，而不是一个照单全收的厂商产品。

想要更全、覆盖所有路线的视角，看[主流 agent 选型矩阵](mainstream-agent-landscape.md)。想要问题优先的走查，看[编码自动化指南](../use-cases/coding-automation.md)。
