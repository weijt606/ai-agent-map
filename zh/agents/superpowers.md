# Superpowers

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](superpowers.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/superpowers.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：Superpowers 是一套可组合的 agentic skills 框架，外加一套开发方法论——它叠在已有 coding agent 之上，把临时性 prompt 工作变成结构化工作流。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | Jesse Vincent 和 Prime Radiant 团队 |
| 路线 | Agentic skills 框架 / 方法论层 |
| 开源 | 是（MIT，Shell + plugin pack） |
| 适合谁 | 想要在 Claude Code、Codex、Cursor、Copilot、Gemini 等之间共享一致 skills 层的工程师 |
| 主要代价 | 你要接受一套方法论——它对 brainstorm → design → plan → implement → review → complete 有明确意见 |
| GitHub 仓库 | https://github.com/obra/superpowers |

## 什么时候选它

- 你已经用 Claude Code、Codex、Cursor、GitHub Copilot、Gemini、OpenCode 或 Factory Droid，想跨多个 agent 共享一套 skills 层。
- 你想要一种方法论强制 TDD、基于证据的验证和复杂度控制，而不仅是几个 skill 文件。
- 你不想手工维护自己的 `.claude/skills` 目录，更愿意接入插件 marketplace。

## 什么时候不选

- 你想要一个端到端 agent 产品；Superpowers 本身不跑 agent，它只塑造已有 agent 上 skills 怎么组合。
- 你不认同它强加的开发周期（brainstorm → design → plan → implement → review → complete），更想自己定义工作流。
- 你想要轻量、极简的 skill 集——Superpowers 故意做得全面，不是极简。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| Skill 组合 | 非常强 | 可组合 skills 根据开发阶段自动激活 |
| 跨 agent 覆盖 | 非常强 | 已有 Claude Code、Codex、Cursor、GitHub Copilot、Gemini、OpenCode、Factory Droid 的 plugin |
| 方法论强制度 | 强 | TDD 和基于证据的验证是一等公民 |
| 独立运行时 | 不是目标 | Superpowers 不跑 agent——它只塑造已有 agent 怎么工作 |
| 插件 marketplace 集成 | 强 | Anthropic 官方 marketplace 有正式 plugin |

## 使用成本

复杂度：中。安装本身简单，但你引入的是方法论而不是单一工具——价值取决于你的团队是否愿意按它强制的阶段化工作流执行。

## 底线

Superpowers 是 2026 年 5 月 GitHub trending 上 `.claude/skills` 浪潮里 star 数最高的项目。和一份 curated skills 目录不同，它是一套有框架支撑、对接几乎所有主流 coding agent 的方法论。在"纯 Claude Code"和"Claude Code + Superpowers"之间选时，问题其实是：你愿不愿意接受 Jesse Vincent 对 TDD 和验证的意见，还是要自己长出来。两种都是合理选择；写入这条 profile 的原因是，skills 浪潮里"有意见的框架"这一端已经成熟到可以横向对比了。
