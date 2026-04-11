# oh-my-codex

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](oh-my-codex.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/oh-my-codex.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：oh-my-codex 是 Codex CLI 之上的更强 operating layer，不是一个新的执行引擎。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Yeachan Heo 与贡献者社区 |
| 路线 | 面向 Codex CLI 的工作流 / orchestration layer |
| 是否开源 | 是 |
| 最适合 | 已经在用 Codex，希望补上可复用 skills、team execution、hooks 和持久运行状态 |
| 主要代价 | 它不是在“简化 Codex”，而是在 Codex 之上再加一层更厚的工作流与 runtime 概念 |
| 官网 | https://yeachan-heo.github.io/oh-my-codex-website/ |
| GitHub 仓库 | https://github.com/Yeachan-Heo/oh-my-codex |

## 什么时候选它

- 你已经在用 Codex CLI，但想让日常工作流更成体系。
- 你想用 `$deep-interview`、`$ralplan`、`$team`、`$ralph` 组成更稳定的 clarify-plan-execute loop。
- 你想把项目状态、计划、日志和 memory 持久化到 `.omx/`，而不是只靠薄薄一层 CLI。

## 什么时候别选

- 你就想用原生 Codex，不想多一层工作流表面。
- 你不想碰 tmux、hooks、skills 或额外 runtime。
- 你想要的是云端托管委派，而不是本地 operator 风格的 Codex 栈。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Workflow standardization | 很强 | 统一 clarify-plan-execute loop 是核心价值 |
| Multi-agent execution | 强 | 任务足够大时，team mode 很有价值 |
| Persistent state | 强 | `.omx/` 对计划、日志和 mode tracking 很关键 |
| Native Codex integration | 强 | hooks 和 Codex 感知工作流是主轴 |
| Low-ceremony usage | 中等 | 上手不算难，但它不是保留 Codex 轻量感的路线 |

## 使用代价

复杂度是 Medium。安装和初始化可控，但 OMX 最舒服的路径仍然是熟悉 Codex CLI、Node，以及 macOS / Linux 上的 tmux。它真正的代价是：你要用更厚的一层 operating layer 来换更强 orchestration。

## 最后一句

如果 Codex CLI 已经是你认可的执行引擎，而你又想把流程做得更稳、更可复用，oh-my-codex 值得认真看。