# OpenClaw

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/openclaw.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](openclaw.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: OpenClaw is better understood as a local-first runtime and control plane than as a lightweight coding tool.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | openclaw |
| Route | Self-hosted runtime / gateway |
| Open source | Yes |
| Best for | Channels, devices, tools, and long-running assistants |
| Main cost | Many routing, permission, security, and ops decisions |
| Official website | https://openclaw.ai |
| GitHub repo | https://github.com/openclaw/openclaw |

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