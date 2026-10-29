# Claude Managed Agents

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/claude-managed-agents.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](claude-managed-agents.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Claude Managed Agents is a named Anthropic API product (in beta): a pre-built, configurable agent harness that runs in managed infrastructure, for long-running and asynchronous work.

> **Correction (2026-10-30):** this profile called "Claude Managed Agents" a repository label for several Anthropic execution paths rather than a product name. Anthropic's docs now describe it as a product in its own right: "Pre-built, configurable agent harness that runs in managed infrastructure", built around agents, environments (an Anthropic-managed cloud sandbox or a self-hosted sandbox), sessions and events, behind the `managed-agents-2026-04-01` beta header and enabled by default for API accounts. It is not eligible for Zero Data Retention or HIPAA BAA coverage. Source: [Claude Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview).

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anthropic |
| Route | Managed and cloud execution workflow |
| Open source | No |
| Best for | Scheduled, background, and programmatic Claude execution |
| Main cost | Beta (`managed-agents-2026-04-01` header); sessions are stateful and stored server-side, so it is not eligible for Zero Data Retention or HIPAA BAA |
| Official website | https://platform.claude.com/docs/en/managed-agents/overview |

## When To Pick It

- You want Claude working in the background rather than staying in a tight local loop.
- You care about agent SDK access, scheduling, or programmatic embedding.
- You want Anthropic's agent loop inside a larger internal workflow or application.

## When Not To Pick It

- You need Zero Data Retention or HIPAA BAA coverage; Managed Agents is not eligible for either.
- You want highly interactive local coding collaboration.
- You need an open-source path. Self-hosted sandboxes exist, but the harness and the model stay Anthropic's.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Managed execution | Strong | Better fit for cloud and background paths |
| Scheduling | Strong | Suitable for recurring or detached work |
| Programmability | Strong | The agent SDK is a major entry point |
| Subagents | Strong | Useful for specialization and isolation |
| Local interaction | Medium | Not the main reason to look here |

## Operating Cost

Complexity is Medium. The difficult part is not capability but the data and lifecycle model: sessions, environments and their stored history are server-side resources you create, steer and delete through the API.

## Bottom Line

If your real need is “Claude should keep working in the background,” this page is usually closer to that need than Claude Code alone.