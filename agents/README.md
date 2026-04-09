# Agents

[![中文](https://img.shields.io/badge/中文-查看中文版-9ca3af?style=flat-square)](../zh/agents/README.md)
[![English](https://img.shields.io/badge/English-Current%20Page-1f6feb?style=flat-square)](README.md)

This is not a wall of names.

Think of it as a shortlist directory: understand the route first, then decide which profile is worth opening.

## Browse By Route

| Route | Representative projects | Best for |
| --- | --- | --- |
| Direct execution | [Claude Code](claude-code.md), [Codex](codex.md), [Devin](devin.md), [OpenHands](openhands.md) | People who want to hand a coding task directly to an agent |
| Strong approval / strong control | [Cline](cline.md), [GitHub Copilot](github-copilot.md), [Froge Code](froge-code.md) | People who want review and human pacing to stay central |
| Build-your-own platform | [LangChain](langchain.md), [LangGraph](langgraph.md) | Teams building their own agent system |
| Self-hosted runtime | [Hermes Agent](hermes-agent.md), [OpenClaw](openclaw.md) | Users who need long-lived agents, channels, devices, or deeper control |
| Managed background path | [Claude Managed Agents](claude-managed-agents.md) | Users who need scheduled, cloud, or detached execution |

## Current Coverage

| Project | Category | Open source | One-line fit | Status |
| --- | --- | --- | --- | --- |
| [Claude Code](claude-code.md) | execution | No | Local and IDE-first coding agent | Verified |
| [Claude Managed Agents](claude-managed-agents.md) | automation | No | Anthropic managed / cloud execution mapping | Mapping documented |
| [Codex](codex.md) | execution | No | Cloud software engineering agent inside ChatGPT | Verified against current product boundary |
| [GitHub Copilot](github-copilot.md) | platform | No | Multi-surface agent platform across VS Code and GitHub | Verified |
| [Cline](cline.md) | execution | Yes | Approval-first editor-native coding agent | Verified |
| [OpenHands](openhands.md) | execution | Yes | Open-source software engineering agent | Verified |
| [Devin](devin.md) | execution | No | Managed end-to-end software engineering execution | Verified |
| [Hermes Agent](hermes-agent.md) | multi-agent | Yes | Self-hosted environment with memory, skills, and subagents | Verified |
| [OpenClaw](openclaw.md) | platform | Yes | Local-first runtime across channels and devices | Verified |
| [LangChain](langchain.md) | platform | Yes | High-level framework for custom agents | Verified |
| [LangGraph](langgraph.md) | platform | Yes | Low-level framework for durable workflows | Verified |
| [Froge Code](froge-code.md) | automation | Yes | Provisionally mapped to Automagik Forge | Name still needs confirmation |

## Writing Standard

See [evaluation framework](evaluation-framework.md).

## Naming Notes

If a project name or public boundary is ambiguous, this directory keeps the ambiguity visible instead of pretending verification is complete.