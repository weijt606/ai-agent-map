---
name: "OpenClaw"
vendor: "openclaw"
category: "platform"
open_source: true
complexity: "high"
verification: "verified-public-project"
last_reviewed: "2026-04-09"
description: "Local-first agent runtime and gateway for multi-channel assistants, tools, routing, and device integrations."
description_zh: "本地优先的 agent runtime / gateway，支持多渠道助手、工具接入、路由和设备集成。"
homepage: "https://openclaw.ai"
repo: "https://github.com/openclaw/openclaw"
---

# OpenClaw

中文：
OpenClaw 更像一个 agent runtime 和 control plane，而不是单一的 coding agent。它适合想要把 agent 接到消息渠道、浏览器、设备节点和本地工具上的开发者或高级用户。

English:
OpenClaw is better understood as an agent runtime and control plane than as a single coding agent. It fits builders or advanced users who want an agent connected to messaging channels, browser automation, device nodes, and local tools.

## 基本信息 | Snapshot

| Field | Value |
| --- | --- |
| Name | OpenClaw |
| Vendor / Owner | openclaw |
| Category | platform |
| Open Source | Yes |
| Complexity | High |
| Delivery Model | Local-first self-hosted runtime and gateway |
| Homepage | https://openclaw.ai |
| Repo | https://github.com/openclaw/openclaw |

## 能力画像 | Capability Profile

| Capability | Assessment | Notes |
| --- | --- | --- |
| Tool use | Very strong | Public docs describe browser control, canvas, nodes, cron, sessions, and channel-specific actions. |
| Code execution | Strong | The runtime can execute commands on the host or in Docker sandboxes depending on session and security policy. |
| Multi-agent routing | Strong | Public docs describe isolated agents, per-agent sessions, and agent-to-agent session tools. |
| Messaging / delivery | Very strong | Designed around WhatsApp, Telegram, Slack, Discord, Signal, iMessage, WeChat, WebChat, and other channels. |
| Device integrations | Strong | macOS, iOS, and Android nodes expose local actions such as notifications, camera, screen recording, and system commands. |
| Memory / context | Medium | Session management, pruning, workspace instructions, and skills exist, but the public emphasis is runtime and control plane design rather than deep memory as the primary differentiator. |

## 最适合的使用场景 | Best Use Cases

- 想要一个本地优先、常驻运行、可接多种消息渠道的个人或团队助手。 Good for local-first assistants that live across multiple communication channels.
- 需要把 agent 接到浏览器、设备节点、消息平台和定时任务上的 runtime。 Good when you need a runtime that joins tools, devices, channels, and scheduled jobs.
- 希望保留较强的部署控制、安全策略和 workspace 定制能力。 Useful when you want stronger control over deployment, security policy, and workspace behavior.

## 不适合的场景 | Not Suitable For

- 只想要一个最小化的 coding agent，不想管理 gateway、渠道和权限。 Not a fit if you only want a minimal coding agent and do not want to manage a gateway, channels, and permissions.
- 希望开箱即用、完全托管、几乎零运维。 Weak fit for users who want a fully managed and low-ops product.
- 只关心 issue-to-PR 执行，不关心消息集成和 runtime 控制。 Overkill if your only goal is issue-to-PR execution.

## 复杂度判断 | Complexity

中文：
复杂度为 High。OpenClaw 的能力面很大，但这也意味着更多的路由、安全、权限和运维决策。它更像一套 agent operating layer，而不是一个单点工具。

English:
Complexity is High. OpenClaw has a broad capability surface, which also means more routing, security, permission, and operational decisions. It behaves more like an agent operating layer than a single-purpose tool.

## 实战备注 | Real-World Usage Notes

- 如果你真的需要“多渠道 + 多设备 + 工具执行 + 自托管”，OpenClaw 很有吸引力。 If you truly need multi-channel, multi-device, tool-executing, self-hosted behavior, OpenClaw is compelling.
- 对外部消息入口要谨慎，尤其是 DM、群组和工具执行权限。 Be careful with external messaging surfaces, especially DM, group, and tool execution permissions.
- 对纯代码自动化而言，它往往不是最轻的选项。 For pure coding automation, it is often not the lightest option.