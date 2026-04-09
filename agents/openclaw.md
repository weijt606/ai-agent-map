# OpenClaw

[![中文](https://img.shields.io/badge/中文-查看中文版-9ca3af?style=flat-square)](../zh/agents/openclaw.md)
[![English](https://img.shields.io/badge/English-Current%20Page-1f6feb?style=flat-square)](openclaw.md)

One-line take: OpenClaw is better understood as a local-first runtime and control plane than as a lightweight coding tool.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | openclaw |
| Route | Self-hosted runtime / gateway |
| Open source | Yes |
| Best for | Channels, devices, tools, and long-running assistants |
| Main cost | Many routing, permission, security, and ops decisions |
| Official entry | https://openclaw.ai |

## When To Pick It

- You need the agent connected to browsers, devices, messaging platforms, and scheduled jobs.
- You want a local-first self-hosted runtime with a strong control plane.
- You are building an operating layer, not just adding a coding assistant.

## When Not To Pick It

- You only want a minimal coding agent.
- You want a fully managed low-ops product.
- Your only goal is issue-to-PR execution.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Tool use | Very strong | The capability surface is wide |
| Code execution | Strong | Can bridge host and container-like environments |
| Multi-agent routing | Strong | Good for more complex routing stories |
| Messaging / delivery | Very strong | A major reason to look at it |
| Device integrations | Strong | Useful when real device control matters |

## Operating Cost

Complexity is High. OpenClaw has a large surface area, and that inevitably comes with more security, routing, permission, and operations work.

## Bottom Line

If you need an agent operating layer, OpenClaw is compelling. If you only need coding automation, it is often too heavy.