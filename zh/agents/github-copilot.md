# GitHub Copilot

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](github-copilot.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/github-copilot.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：现在的 GitHub Copilot 更像一个 agent 平台，而不是单纯补全工具。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | GitHub / Microsoft |
| 路线 | VS Code + GitHub 生态里的多表面 agent 平台 |
| 是否开源 | 否 |
| 最适合 | 本地、CLI、cloud workflow 需要串起来的团队 |
| 主要代价 | 最佳体验强依赖 VS Code / GitHub 生态 |
| 官网 | https://code.visualstudio.com/docs/copilot/agents/overview |

## 什么时候选它

- 你的团队主要工作在 VS Code 和 GitHub 上。
- 你希望 Ask、Plan、Agent、CLI、cloud path 放在同一个入口里。
- 你希望 issue、PR、review 和编辑器执行能顺着一条工作流走。

## 什么时候别选

- 你不在 VS Code / GitHub 生态里工作。
- 你需要完全开源或强自托管。
- 你只想要一个极简、单表面的 agent。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Local execution | 强 | 编辑器内体验已经不是附属功能 |
| Cloud delegation | 强 | 适合把任务接到 GitHub 工作流里 |
| Workflow handoff | 强 | 本地到云端切换是亮点 |
| Permission control | 强 | 控制粒度比较清楚 |
| Custom agents | 中 | 适合做角色化和专用入口 |

## 2026 年年中动态

2026 年 6–7 月的更新把 Copilot 进一步推向 agent 平台，而不是补全工具：

- **Agent finder（6 月 17 日）**：Copilot 自己为任务找到合适的能力，不再需要手工配置 MCP / skills / agents。
- **JetBrains AI Assistant（6 月 30 日）**：Copilot Agent 成为 JetBrains agent 选择器里的一等选项——它开始进入其他厂商的表面里竞争。
- **VS Code（6 月）**：agentic 浏览器工具 GA（在编辑器内导航、检查、截图、验证 web 应用）、agent 会话分组管理与成本可见性、兼容 Anthropic / OpenAI 模型的 1M token 上下文。
- **Code review（6 月 18 日）**：Copilot code review 支持仓库级 AGENTS.md。
- **Copilot CLI（7 月）**：plan mode 硬拦截会改动工作区的工具调用，另有语音模式持久化、canvas 支持、更细的 subagent 控制；/security-review 命令进入公测。

选型要点：平台优势还在复利——Copilot 越来越像整条 GitHub 工作流的 agent 层，而不是单个助手。

## 使用代价

复杂度是 Medium。基础使用很轻，但一旦你开始混用本地 agent、CLI、cloud path 和权限模式，工作流会明显变复杂。

## 最后一句

GitHub Copilot 的优势不是某一个 agent 特别强，而是它把主流开发动作塞进了同一条链路里。