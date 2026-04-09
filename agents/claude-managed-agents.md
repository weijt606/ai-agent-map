# Claude Managed Agents

[![中文](https://img.shields.io/badge/中文-查看中文版-9ca3af?style=flat-square)](../zh/agents/claude-managed-agents.md)
[![English](https://img.shields.io/badge/English-Current%20Page-1f6feb?style=flat-square)](claude-managed-agents.md)

One-line take: this is the repository label for Anthropic's managed and cloud-style Claude execution paths, not a single sharply bounded product name.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Anthropic |
| Route | Managed and cloud execution workflow |
| Open source | No |
| Best for | Scheduled, background, and programmatic Claude execution |
| Main cost | The public product boundary is spread across multiple concepts |
| Official entry | https://code.claude.com/docs/en/agent-sdk/overview |

## When To Pick It

- You want Claude working in the background rather than staying in a tight local loop.
- You care about agent SDK access, scheduling, or programmatic embedding.
- You want Anthropic's agent loop inside a larger internal workflow or application.

## When Not To Pick It

- You want one clearly named product with one obvious operator surface.
- You want highly interactive local coding collaboration.
- You need an open-source or self-hosted path.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Managed execution | Strong | Better fit for cloud and background paths |
| Scheduling | Strong | Suitable for recurring or detached work |
| Programmability | Strong | The agent SDK is a major entry point |
| Subagents | Strong | Useful for specialization and isolation |
| Local interaction | Medium | Not the main reason to look here |

## Operating Cost

Complexity is Medium. The difficult part is not capability, but naming and mental model: this is better understood as a family of Anthropic execution modes than as one button-like product.

## Bottom Line

If your real need is “Claude should keep working in the background,” this page is usually closer to that need than Claude Code alone.