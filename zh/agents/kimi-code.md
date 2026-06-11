# Kimi Code

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](kimi-code.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/kimi-code.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：Kimi Code 是月之暗面（Moonshot AI）官方的终端 coding agent——和 Claude Code 一样的循环（读写代码、跑 shell、搜文件、抓网页），优先围绕 Kimi 模型调优，但也能配置成任意 OpenAI 兼容 provider。

> **传承关系：** Kimi Code（`MoonshotAI/kimi-code`，TypeScript）是初代 [`MoonshotAI/kimi-cli`](https://github.com/MoonshotAI/kimi-cli)（Python，8.9k star）的下一代继任者。团队正在逐步停掉 `kimi-cli`——安装 Kimi Code 会自动迁移旧的配置和会话。把 Kimi Code 当作面向未来的表面；过渡期内 `kimi-cli` 的文档和已有安装仍可用。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | Moonshot AI（Kimi 月之暗面） |
| 路线 | 直接执行——终端 coding agent |
| 开源 | 是 |
| 实现 | TypeScript（kimi-code）；Python（旧版 kimi-cli） |
| 许可 | MIT |
| 模型 | 开箱即用 Kimi（K2 系列）；任意 OpenAI 兼容 provider |
| 适合谁 | 想要厂商官方、Kimi 原生、且带一流 IDE/ACP 集成的 coding CLI 的开发者 |
| 主要代价 | 正处于迁移期——传承在 kimi-cli 退役过程中分散在两个仓库 |
| GitHub 仓库 | https://github.com/MoonshotAI/kimi-code |

## 什么时候选它

- 你想要做 Kimi 模型的那个团队出的第一方终端 coding agent，而不是第三方 harness 指向某个 Kimi 端点。
- 你想要零依赖安装（官方脚本不需要 Node.js），而且这个 CLI 还能作为 ACP agent server 接入 Zed、JetBrains 等 ACP 兼容编辑器。
- 你已经在用 Kimi 写代码，想让模型和 agent 循环一起调优，同时保留以后换成任意 OpenAI 兼容 provider 的余地。

## 什么时候不选

- 你今天就需要成熟稳定的表面——项目正从 `kimi-cli` 迁移到 `kimi-code`，会有动荡。
- 你把"广泛的多厂商中立"当作核心价值——provider 中立的 harness 如 [Pi](pi.md) 或 [Aider](aider.md) 是更稳的底座。
- 你需要云端委派、并行 agent 或脱机后台运行——那是 [Codex](codex.md) 或 [Devin](devin.md) 的领地。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 终端工作流 | 强 | 单进程循环；可切入 shell 命令模式 |
| Kimi 模型调优 | 非常强 | 第一方；agent 和模型出自同一团队 |
| IDE / ACP 集成 | 强 | ACP agent server（`kimi acp`）加 VS Code 插件 |
| 多 provider 支持 | 中 | 支持 OpenAI 兼容 provider，但 Kimi 是默认路径 |
| 后台执行 | 不是目标 | 前台、单开发者循环 |

## 使用成本

复杂度：低-中。安装是一行脚本，不需要 Node.js。眼下真正的成本是迁移：初代 `kimi-cli` 正在被 `kimi-code` 取代，所以在迁移落定前，文档、issue 和功能对齐分散在两个仓库。

## 底线

Kimi Code 是"我想要 Claude Code 风格的 CLI，但要 Kimi 原生"的官方答案。它是上手 Moonshot 模型最清晰的第一方路径，通过 ACP 和 VS Code 插件有真实的 IDE 触达。唯一的顾虑是时机——它正从 `kimi-cli` 重建中，表面还在收敛。如果你想要 provider 中立的底座，[Pi](pi.md) 或 [Aider](aider.md) 更合适；如果你就是想要官方 Kimi 循环，就是它。想要针对 DeepSeek + MiMo 的国产模型栈兄弟项目，看 [CodeWhale](codewhale.md)；想要小米自家的官方 CLI，看 [MiMoCode](mimocode.md)。
