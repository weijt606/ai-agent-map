---
name: "Claude Code"
vendor: "Anthropic"
category: "execution"
open_source: false
complexity: "medium"
verification: "verified-public-positioning"
last_reviewed: "2026-04-09"
description: "Anthropic's agentic coding tool for terminal, IDE, desktop, and browser workflows."
description_zh: "Anthropic 推出的 agentic coding 工具，覆盖终端、IDE、桌面和浏览器工作流。"
homepage: "https://code.claude.com/docs/en/overview"
repo: ""
---

# Claude Code

中文：
Claude Code 是典型的本地和 IDE 优先 coding agent。它的强项不是“全托管替你做完”，而是把 instructions、MCP、subagents、scheduled tasks 和多表面工作流合成一条连续的开发回路。

English:
Claude Code is a local-first and IDE-first coding agent. Its strength is not fully managed execution, but a unified development loop that combines instructions, MCP, subagents, scheduled tasks, and multiple working surfaces.

## 基本信息 | Snapshot

| Field | Value |
| --- | --- |
| Name | Claude Code |
| Vendor | Anthropic |
| Category | execution |
| Open Source | No |
| Complexity | Medium |
| Delivery Model | Terminal, IDE, desktop, and web surfaces |
| Homepage | https://code.claude.com/docs/en/overview |
| Repo | None |

## 能力画像 | Capability Profile

| Capability | Assessment | Notes |
| --- | --- | --- |
| Tool use | Strong | Public docs position Claude Code as reading code, editing files, running commands, and integrating with development tools. |
| Code execution | Strong | The terminal-first workflow and built-in agent loop are core to the product. |
| MCP integration | Strong | Public docs explicitly call out MCP connectors and custom tool extension. |
| Subagents | Strong | Anthropic documents built-in and custom subagents with isolated context and tool restrictions. |
| Scheduling | Medium | Scheduled tasks are supported across local and cloud-oriented paths. |
| Human collaboration | Strong | It is designed for iterative interaction across terminal, IDE, desktop, and browser surfaces. |

## 最适合的使用场景 | Best Use Cases

- 想在本地仓库里高频和 agent 协作写代码、修 bug、跑命令。 Best for interactive local coding, debugging, and command execution.
- 需要 instructions、skills、MCP 和 subagents 共同工作。 Good when you want instructions, skills, MCP, and subagents in one workflow.
- 需要一个从终端到 IDE 再到 web 都相对统一的开发体验。 Good when you want a unified workflow across terminal, IDE, and web surfaces.

## 不适合的场景 | Not Suitable For

- 只想把任务扔出去后台跑完，自己回头看 PR。 Not the best fit if you only want detached background execution with minimal interaction.
- 对权限、工具和本地环境完全不想操心。 Weak fit if you do not want to manage permissions, tools, and local environment behavior.
- 需要开源可自托管的整套 coding agent。 Not a fit for teams that require a fully open-source self-hosted agent.

## 复杂度判断 | Complexity

中文：
复杂度为 Medium。入门并不难，但要把 subagents、MCP、scheduled tasks 和项目级 instructions 用好，需要一定 workflow 设计能力。

English:
Complexity is Medium. Getting started is straightforward, but effective use of subagents, MCP, scheduled tasks, and project instructions still requires workflow design discipline.

## 实战备注 | Real-World Usage Notes

- Claude Code 更像一个“可持续使用的开发环境增强层”，不是一次性的任务执行器。 Claude Code behaves more like a durable augmentation layer for development than a one-shot executor.
- 如果团队已经有较清晰的本地开发习惯，它的融入成本通常低于全新平台。 It usually fits more naturally than an entirely new platform when the team already has strong local development habits.
- 真正的价值往往来自 CLAUDE.md、subagents 和 MCP 这些结构化能力，而不只是单次提示词。 The real value often comes from structured capabilities such as CLAUDE.md, subagents, and MCP, not just better prompts.