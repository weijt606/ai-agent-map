# jcode

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](jcode.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/jcode.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：jcode 是一个用 Rust 写的终端 coding-agent harness，专为多会话工作流和极致性能打造——一个你能端到端拥有、provider 中立的循环，招牌功能是被动语义记忆图谱，而不是一个拿来即用的厂商产品。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | 独立开发（`1jehuang/jcode`，jcode.sh） |
| 路线 | Agent harness 框架——终端优先的 coding harness |
| 开源 | 是 |
| 实现 | Rust |
| 许可 | MIT |
| 模型 | provider 中立——OAuth 登录 Claude、OpenAI/ChatGPT/Codex、Gemini、Copilot、Azure；外加任意 OpenAI 兼容端点（OpenRouter、DeepSeek、Kimi/月之暗面、Ollama、LM Studio……） |
| 适合谁 | 想要一个快、占用小、可深度定制、能跑很多会话、并指向自己已付费模型的 harness 的开发者 |
| 主要代价 | 项目较年轻、迭代快，harness 表面和配置仍在收敛 |
| GitHub 仓库 | https://github.com/1jehuang/jcode |

## 什么时候选它

- 你想像 [Pi](pi.md) 一样拥有循环、工具面和配置，但更看重速度和规模：jcode 的 Rust 内核首帧启动约 14ms，同类里 RAM 占用最低——当你并行跑很多会话时这很关键。
- 你想要一个 harness 接通你已经订阅的任何模型——它用 OAuth 登录 Claude、OpenAI、Gemini、Copilot，其余几乎全部走共享的 OpenAI 兼容 API。
- 你想要不用盯着的记忆：jcode 把每一轮对话嵌入成语义向量，通过记忆图谱自动召回相关历史（可选一个校验 side-agent），而不是让模型手动调记忆工具——同时在你需要时也暴露显式的记忆和会话检索工具。

## 什么时候不选

- 你想要模型和循环出自同一团队的厂商调优产品——那是 [Claude Code](claude-code.md)、[Codex](codex.md) 或 [Kimi Code](kimi-code.md)，不是一个 fork-and-own 的 harness。
- 你今天就需要成熟稳定的表面——jcode 较年轻、迭代快，配置和功能会有动荡。
- 你想发布 SWE-bench 成绩，或想一口气读完整个循环——那分别是 [SWE-agent](swe-agent.md)（研究参照）和 [mini-swe-agent](mini-swe-agent.md)（极简）的领地。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 性能 / 占用 | 非常强 | Rust 内核；据其自测在主流 coding CLI 中启动最快、RAM 最低 |
| 多会话工作流 | 强 | 面向廉价地扩展到很多并发会话设计 |
| 被动记忆 | 非常强 | 语义向量记忆图谱 + 自动召回 + 可选校验 side-agent；也提供显式记忆和会话检索工具 |
| provider 中立 | 非常强 | OAuth 登录主流厂商，长尾走共享 OpenAI 兼容 provider |
| 可扩展性 | 强 | 支持 MCP 配置，"无限可定制"是其标称设计目标 |
| 厂商官方模型调优 | 不是目标 | 设计上 provider 中立；没有第一方模型 |

## 使用成本

复杂度：低-中。安装是一行脚本（`curl -fsSL https://jcode.sh/install | bash`，Windows 用 PowerShell），Rust 二进制占用很轻。真正的成本是成熟度：jcode 是个较年轻、快速演进的项目，配置格式和功能仍在移动。被动记忆系统很强，但如果你想调"召回什么"，它就是多一个要理解的子系统。

## 底线

jcode 是这样一个 harness 选择："我想像 [Pi](pi.md) 一样拥有循环，但要更快、更精简、provider 无关——而且我想要开箱即用的记忆。"它的差异化押注是面向多会话工作流的 Rust 级性能，加一套被动语义记忆图谱，再叠上广泛的多 provider OAuth。如果你想要厂商调优的产品，[Claude Code](claude-code.md)、[Codex](codex.md) 或 [Kimi Code](kimi-code.md) 更合适；如果你想要最小可读底座或 SWE-bench 可复现性，看 [mini-swe-agent](mini-swe-agent.md) 和 [SWE-agent](swe-agent.md)。完整的 harness 横评见[agent harness 框架](../comparisons/agent-harness-frameworks.md)。
