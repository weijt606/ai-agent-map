# How To Choose An Agent For Coding Automation

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-9ca3af?style=for-the-badge)](../zh/use-cases/coding-automation.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-1f6feb?style=for-the-badge)](coding-automation.md)
[![Home](https://img.shields.io/badge/HOME-README-24292f?style=for-the-badge)](../README.md)

This page does not answer whether agents can write code.

That question is no longer the useful one. The better question is: which operating model fits your coding workflow?

## Quick Start

| If your real need is... | Start with |
| --- | --- |
| Tight local collaboration in the terminal or IDE | [Claude Code](../agents/claude-code.md) |
| Async delegation into cloud execution | [Codex](../agents/codex.md) |
| Anthropic background / scheduled / managed path | [Claude Managed Agents](../agents/claude-managed-agents.md) |
| Strong approval and strong control inside the editor | [Cline](../agents/cline.md) |
| One flow across VS Code, GitHub, local, and cloud | [GitHub Copilot](../agents/github-copilot.md) |
| Open-source software engineering agent close to the Devin route | [OpenHands](../agents/openhands.md) |
| Direct issue-to-execution handoff | [Devin](../agents/devin.md) |
| Review-first task board with multiple attempts | [Froge Code](../agents/froge-code.md) |
| Long-lived self-hosted environment with memory and messaging | [Hermes Agent](../agents/hermes-agent.md) |
| Runtime, channels, devices, and deeper control plane | [OpenClaw](../agents/openclaw.md) |
| Build your own agent fast instead of buying one | [LangChain](../agents/langchain.md) |
| Build a durable stateful workflow platform | [LangGraph](../agents/langgraph.md) |

## Three-Step Decision Path

1. Decide whether you want to use an agent directly or build a system.
2. Decide whether you care more about low-ops managed service or high-control self-hosting.
3. Decide whether you want autonomy-first execution or review-first human control.

## The Four Most Common Routes

| Route | Representative projects | What it feels like |
| --- | --- | --- |
| Local collaboration | [Claude Code](../agents/claude-code.md), [Cline](../agents/cline.md) | High interaction, fast iteration, strong operator feel |
| Cloud delegation | [Codex](../agents/codex.md), [Devin](../agents/devin.md) | Assign work, come back later, review the result |
| Review-first automation | [GitHub Copilot](../agents/github-copilot.md), [Froge Code](../agents/froge-code.md) | Keep humans central while still using powerful agent workflows |
| Build / self-host | [OpenHands](../agents/openhands.md), [Hermes Agent](../agents/hermes-agent.md), [LangChain](../agents/langchain.md), [LangGraph](../agents/langgraph.md) | More flexibility, more environment and operations cost |

## Key Trade-Offs

| Project | Biggest upside | Cost you must accept |
| --- | --- | --- |
| Claude Code | Smooth local loop with MCP, instructions, and subagents | You still own permissions and local environment control |
| Claude Managed Agents | Better fit for scheduled and background Anthropic workflows | Product boundary is not represented by one simple public page |
| Codex | Strong isolation and review evidence | Less immediate than editor-native pair programming |
| GitHub Copilot | Local, CLI, and cloud workflows can live together | Best fit depends heavily on VS Code and GitHub |
| Cline | Powerful editor-native workflow with explicit approvals | Approval friction is real |
| OpenHands | Real open-source runnable system with multiple operating modes | Docker and runtime setup are heavier |
| Devin | Very direct managed execution path | Less control over system boundaries |
| Froge Code | Strong task visibility, multiple attempts, isolated worktrees | The workflow is heavier and provider-dependent |
| Hermes Agent | Long-lived self-hosted environment with memory and delegation | Needs ongoing curation |
| OpenClaw | Strong runtime, channels, and device control | Usually too heavy for pure coding-only work |
| LangChain | Fastest path to custom agent assembly | Complex workflows often still push you down into LangGraph |
| LangGraph | Strong durable state, approval, and recovery model | Highest engineering and ops burden |

## Common Failure Modes

- Choosing a framework when what you really need is a ready-to-run agent.
- Choosing an autonomy-first executor when your real need is review-first control.
- Choosing a broad runtime platform when you only need coding automation.
- Ignoring permissions, secrets, code exposure, and validation responsibility.

## One Rule That Usually Works

Pick the smallest agent surface that solves your current problem.

Do not adopt a full runtime, platform, and orchestration stack on day one just because you might want those capabilities later.