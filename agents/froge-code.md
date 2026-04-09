# Froge Code

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/froge-code.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](froge-code.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: this page is currently written against an Automagik Genie mapping and fits review-first, multi-attempt, worktree-based coding automation.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Current mapping | Automagik Genie |
| Route | Review-first automation platform |
| Open source | Claimed yes, but the public product repo is not clearly exposed yet |
| Best for | Task boards, multiple attempts, human result selection |
| Main cost | Public naming is still evolving between Automagik and Genie, and the workflow is heavier |
| Official website | https://automagik.dev/ |

## When To Pick It

- You want coding automation to behave like a task board instead of a single agent session.
- You want to compare providers or agent behaviors on the same task class.
- You want isolated worktrees to reduce risk to the main workspace.

## When Not To Pick It

- You want one autonomous agent to go from issue to delivery with minimal workflow overhead.
- You do not want to manage provider, attempt, and review concepts.
- You need highly custom state-machine orchestration instead of task-board orchestration.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Task orchestration | Strong | The task board is the center |
| Code execution | Strong | Worktree isolation is useful for comparison |
| Multi-provider control | Strong | Good for side-by-side evaluation |
| Human oversight | Very strong | Human selection is part of the design |
| MCP | Strong | Works well as part of a broader automation flow |

## Operating Cost

Complexity is Medium. It keeps humans in control, but that also means you must actively maintain task structure, attempt strategy, and review rhythm.

## Bottom Line

The value here is workflow visibility, not magical autonomy from one agent.