---
name: "Hermes Agent"
vendor: "Nous Research"
category: "multi-agent"
open_source: true
complexity: "medium"
verification: "verified-public-project"
last_reviewed: "2026-04-09"
description: "Self-hosted agent with CLI, messaging gateway, memory, skills, MCP, scheduling, and subagent delegation."
description_zh: "自托管 agent，提供 CLI、消息网关、memory、skills、MCP、调度和 subagent delegation。"
homepage: "https://hermes-agent.nousresearch.com/docs/"
repo: "https://github.com/NousResearch/hermes-agent"
---

# Hermes Agent

中文：
Hermes Agent 是一个面向高级用户和开发者的自托管 agent，强调 CLI 体验、消息网关、记忆系统、skills 和 subagents。它更适合想长期经营一个 agent 工作环境的人，而不是只想偶尔跑一次任务的人。

English:
Hermes Agent is a self-hosted agent for advanced users and builders. It emphasizes the CLI experience, messaging gateway, memory, skills, and subagents. It is better suited to people who want a long-lived agent environment, not just a one-off task runner.

## 基本信息 | Snapshot

| Field | Value |
| --- | --- |
| Name | Hermes Agent |
| Vendor | Nous Research |
| Category | multi-agent |
| Open Source | Yes |
| Complexity | Medium |
| Delivery Model | Self-hosted CLI and gateway-based agent |
| Homepage | https://hermes-agent.nousresearch.com/docs/ |
| Repo | https://github.com/NousResearch/hermes-agent |

## 能力画像 | Capability Profile

| Capability | Assessment | Notes |
| --- | --- | --- |
| Tool use | Strong | Public docs describe 40+ tools and configurable toolsets. |
| Code execution | Strong | Supports multiple terminal backends including local, Docker, SSH, and other remote runtimes. |
| Memory | Strong | Public docs emphasize persistent memory, session search, user profiles, and a skills system. |
| Scheduling | Strong | Built-in cron scheduling is documented as a first-class feature. |
| Multi-agent delegation | Strong | Public docs describe spawning isolated subagents and parallel workstreams. |
| Messaging | Strong | CLI plus messaging gateways for Telegram, Discord, Slack, WhatsApp, Signal, and related workflows. |

## 最适合的使用场景 | Best Use Cases

- 想要一个可以长期陪伴工作的自托管 agent，而不只是一次性执行器。 Good for a long-lived self-hosted agent, not just a one-shot executor.
- 希望在 CLI、消息渠道、MCP、skills 和 memory 之间形成统一工作流。 Good when you want a unified workflow across CLI, messaging, MCP, skills, and memory.
- 需要 subagent delegation、长期上下文和定时自动化。 Useful when you need delegation, persistent context, and scheduled automation.

## 不适合的场景 | Not Suitable For

- 只想点击几下就把单个 coding task 丢给 agent。 Not a fit if you only want a minimal point-and-click tool for one coding task.
- 没有意愿管理模型、权限、skills、toolsets 和运行后端。 Weak fit if you do not want to manage models, permissions, skills, toolsets, and runtime backends.
- 追求成熟的企业 UI，而不是 CLI 主导的操作体验。 Less suitable if you want a polished enterprise UI instead of a CLI-centered workflow.

## 复杂度判断 | Complexity

中文：
复杂度为 Medium。Hermes 的安装路径相对直接，但一旦你开始使用 gateway、skills、memory 和 subagents，操作模型就会明显变重。

English:
Complexity is Medium. The installation path is relatively direct, but the operating model becomes noticeably heavier once you start using gateway integrations, skills, memory, and subagents.

## 实战备注 | Real-World Usage Notes

- Hermes 的价值来自“长期积累的工作环境”，不是单次回复质量。 Hermes becomes valuable as a long-lived working environment, not just through single-response quality.
- 技能、记忆和工具权限需要持续整理，否则系统会逐渐变复杂。 Skills, memory, and tool permissions need ongoing curation or the system becomes harder to operate.
- 如果你想要的是自托管、可扩展、可持续经营的 agent，Hermes 很值得评估。 If you want a self-hosted, extensible, long-lived agent environment, Hermes is worth evaluating.