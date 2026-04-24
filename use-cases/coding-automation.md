# How To Choose An Agent For Coding Automation

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/use-cases/coding-automation.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](coding-automation.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

This page does not answer whether agents can write code.

That question is no longer the useful one. The better question is: which operating model fits your coding workflow?

## Quick Start

| If your real need is... | Start with |
| --- | --- |
| Tight local collaboration in the terminal or IDE | [Claude Code](../agents/claude-code.md) |
| Terminal-first local coding with a strong git loop | [Aider](../agents/aider.md) |
| Async delegation into cloud execution | [Codex](../agents/codex.md) |
| Strongest OpenAI model for agentic coding with 1M context | [GPT-5.5](../agents/gpt-5.5.md) |
| I already use Claude Code and want teams, skills, and stronger orchestration | [oh-my-claudecode](../agents/oh-my-claudecode.md) |
| I already use Codex CLI and want teams, hooks, and persistent workflow state | [oh-my-codex](../agents/oh-my-codex.md) |
| Google-managed GitHub-connected cloud delegation | [Jules](../agents/jules.md) |
| Anthropic background / scheduled / managed path | [Claude Managed Agents](../agents/claude-managed-agents.md) |
| AI editor that spans local coding, background agents, and integrations | [Cursor](../agents/cursor.md) |
| Dedicated AI IDE centered on the editor flow | [Windsurf](../agents/windsurf.md) |
| Open-source editor extension with full model freedom | [Continue](../agents/continue.md) |
| Strong approval and strong control inside the editor | [Cline](../agents/cline.md) |
| One flow across VS Code, GitHub, local, and cloud | [GitHub Copilot](../agents/github-copilot.md) |
| Open-source software engineering agent close to the Devin route | [OpenHands](../agents/openhands.md) |
| Direct issue-to-execution handoff | [Devin](../agents/devin.md) |
| Review-first task board with multiple attempts | [Froge Code](../agents/froge-code.md) |
| Open-source local agent with desktop, CLI, and extensions | [Goose](../agents/goose.md) |
| Long-lived self-hosted environment with memory and messaging | [Hermes Agent](../agents/hermes-agent.md) |
| Runtime, channels, devices, and deeper control plane | [OpenClaw](../agents/openclaw.md) |
| Build your own agent fast instead of buying one | [LangChain](../agents/langchain.md) |
| Build a durable stateful workflow platform | [LangGraph](../agents/langgraph.md) |

## Three-Step Decision Path

1. Decide whether you want to use an agent directly or build a system.
2. Decide whether you care more about low-ops managed service or high-control self-hosting.
3. Decide whether you want autonomy-first execution or review-first human control.

## The Most Common Routes

| Route | Representative projects | What it feels like |
| --- | --- | --- |
| Local collaboration | [Claude Code](../agents/claude-code.md), [Aider](../agents/aider.md) | High interaction, fast iteration, strong operator feel |
| Workflow layer on top of a base agent | [oh-my-claudecode](../agents/oh-my-claudecode.md), [oh-my-codex](../agents/oh-my-codex.md) | Keep Claude Code or Codex as the execution engine and add reusable orchestration on top |
| Editor-centric AI workflow | [Cursor](../agents/cursor.md), [Windsurf](../agents/windsurf.md) | Keep the editor central and make the IDE itself part of the agent choice |
| Cloud delegation | [Codex](../agents/codex.md), [Devin](../agents/devin.md), [Jules](../agents/jules.md) | Assign work, come back later, review the result |
| Managed background path | [Claude Managed Agents](../agents/claude-managed-agents.md) | Scheduled or detached Anthropic workflows |
| Review-first automation | [Cline](../agents/cline.md), [GitHub Copilot](../agents/github-copilot.md), [Froge Code](../agents/froge-code.md) | Keep humans central while still using powerful agent workflows |
| Build / self-host | [OpenHands](../agents/openhands.md), [Goose](../agents/goose.md), [Hermes Agent](../agents/hermes-agent.md), [LangChain](../agents/langchain.md), [LangGraph](../agents/langgraph.md) | More flexibility, more environment and operations cost |

## Key Trade-Offs

| Project | Biggest upside | Cost you must accept |
| --- | --- | --- |
| Claude Code | Smooth local loop with MCP, instructions, and subagents | You still own permissions and local environment control |
| Aider | Terminal-first pair programming stays close to git | You still own model setup and terminal ergonomics |
| Claude Managed Agents | Better fit for scheduled and background Anthropic workflows | Product boundary is not represented by one simple public page |
| Codex | Strong isolation and review evidence | Less immediate than editor-native pair programming |
| GPT-5.5 | Highest agentic coding benchmarks and 1M context window | 2x API cost, fully proprietary, trails Claude on SWE-Bench Pro |
| oh-my-claudecode | Claude Code gains teams, reusable skills, and richer runtime control | You add another workflow layer and still depend on Claude Code |
| oh-my-codex | Codex gets a clearer clarify-plan-execute operating model | More setup, more ceremony, and the best path usually involves tmux |
| Cursor | One polished surface for editor, delegation, and integrations | Broad product surface and a clearly closed-source boundary |
| GitHub Copilot | Local, CLI, and cloud workflows can live together | Best fit depends heavily on VS Code and GitHub |
| Cline | Powerful editor-native workflow with explicit approvals | Approval friction is real |
| Windsurf | Dedicated AI IDE with strong in-flow editing | Narrower extension story and a more opinionated workflow |
| Continue | Open-source, full model freedom, team config sharing | You own model setup — more configuration than turnkey alternatives |
| OpenHands | Real open-source runnable system with multiple operating modes | Docker and runtime setup are heavier |
| Devin | Very direct managed execution path | Less control over system boundaries |
| Jules | Managed GitHub-connected cloud execution with PR flow | Cloud-first delivery and an API surface that is still evolving |
| Goose | Open-source local agent with extensions, MCP, and shared config | Product boundary is broader than coding-only work |
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