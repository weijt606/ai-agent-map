# Agents

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/README.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](README.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

This is not a wall of names.

Think of it as a shortlist directory: understand the route first, then decide which profile is worth opening.

## Browse By Route

| Route | Representative projects | Best for |
| --- | --- | --- |
| Direct execution | [Claude Code](claude-code.md), [Aider](aider.md), [Codex](codex.md), [Devin](devin.md), [Jules](jules.md), [OpenHands](openhands.md) | People who want to hand a coding task directly to an agent |
| Frontier agentic model | [GPT-5.5](gpt-5.5.md) | People choosing which model to wire into their agent system, or evaluating the capability ceiling of OpenAI surfaces |
| Workflow / orchestration layer | [oh-my-claudecode](oh-my-claudecode.md), [oh-my-codex](oh-my-codex.md) | Users who already like Claude Code or Codex and want stronger teams, skills, and persistent workflow |
| Editor-centric AI workflow | [Cursor](cursor.md), [Windsurf](windsurf.md), [Continue](continue.md) | Users who want the editor itself to be the main agent surface |
| Review-first automation | [Cline](cline.md), [GitHub Copilot](github-copilot.md), [Froge Code](froge-code.md) | People who want review and human pacing to stay central |
| General-purpose autonomous agent | [AutoGPT](autogpt.md) | People who want a visual agent-builder for autonomous general-purpose tasks |
| Build-your-own platform | [LangChain](langchain.md), [LangGraph](langgraph.md), [CrewAI](crewai.md), [LlamaIndex](llamaindex.md) | Teams building their own agent system |
| Runtime and tools | [n8n](n8n.md), [MemGPT](memgpt.md) | Teams needing workflow automation with AI agents, or persistent memory for stateful agents |
| Self-hosted / local runtime | [AI Edge Gallery](ai-edge-gallery.md), [Goose](goose.md), [Hermes Agent](hermes-agent.md), [OpenClaw](openclaw.md) | Users who need local control, on-device privacy, extensions, channels, or deeper runtime ownership |
| Managed background path | [Claude Managed Agents](claude-managed-agents.md) | Users who need scheduled, cloud, or detached execution |

## Recent Heat Snapshot

This is not a ranking of quality.

It is a quick view of projects that appeared especially hot in the late-April 2026 GitHub snapshot. The order follows that snapshot, while the star totals below reflect the current counts checked during this repo update.

| Rank | Project | Current stars | Snapshot gain | Directory status | Note |
| --- | --- | --- | --- | --- | --- |
| #1 | [Hermes Agent](hermes-agent.md) | 113.0k | +57,100 | Profile included | Clear in-scope self-hosted multi-agent environment with explosive growth |
| #2 | [OpenScreen](https://github.com/siddharthvaddem/openscreen) | 32.4k | +4,500 | Not included | Still hot, but it is a screen-demo tool rather than an agent |
| #3 | [oh-my-codex](oh-my-codex.md) | 25.3k | +4,400 | Profile included | A fast-rising Codex workflow and orchestration layer |
| #4 | [oh-my-claudecode](oh-my-claudecode.md) | 31.0k | +3,400 | Profile included | A hot workflow and orchestration layer around Claude Code |
| #5 | [AI Edge Gallery](ai-edge-gallery.md) | 21.9k | +1,600 | Profile included with caveat | Better read as an on-device assistant sandbox than a coding-first agent |

**Market event (April 23 2026):** OpenAI released [GPT-5.5](gpt-5.5.md) — not a GitHub-trending project, but a model that reshapes the capability ceiling for Codex, ChatGPT, and every OpenAI-API-based agent. See the [GPT-5.5 profile](gpt-5.5.md) for positioning and trade-offs.

## Current Coverage

| Project | Category | Open source | One-line fit | Status |
| --- | --- | --- | --- | --- |
| [Aider](aider.md) | execution | Yes | Terminal-first AI pair programming with a strong git loop | Verified |
| [Claude Code](claude-code.md) | execution | No | Local and IDE-first coding agent | Verified |
| [Claude Managed Agents](claude-managed-agents.md) | automation | No | Anthropic managed / cloud execution mapping | Mapping documented |
| [Codex](codex.md) | execution | No | Cloud software engineering agent inside ChatGPT | Verified against current product boundary |
| [oh-my-claudecode](oh-my-claudecode.md) | multi-agent | Yes | Workflow and orchestration layer for Claude Code | Verified with package naming note |
| [oh-my-codex](oh-my-codex.md) | multi-agent | Yes | Workflow and orchestration layer for Codex CLI | Verified |
| [Cursor](cursor.md) | platform | No | AI editor spanning local coding, integrations, and background agents | Verified |
| [GitHub Copilot](github-copilot.md) | platform | No | Multi-surface agent platform across VS Code and GitHub | Verified |
| [Cline](cline.md) | execution | Yes | Approval-first editor-native coding agent | Verified |
| [Windsurf](windsurf.md) | platform | No | AI-native IDE centered on Cascade | Verified |
| [OpenHands](openhands.md) | execution | Yes | Open-source software engineering agent | Verified |
| [Devin](devin.md) | execution | No | Managed end-to-end software engineering execution | Verified |
| [Jules](jules.md) | automation | No | Google managed cloud coding agent with GitHub and PR flow | Verified against current docs |
| [AI Edge Gallery](ai-edge-gallery.md) | platform | Yes | On-device local assistant sandbox with agent skills and mobile actions | Verified with scope caveat |
| [Goose](goose.md) | platform | Yes | Extensible local agent across desktop, CLI, and API | Verified |
| [Hermes Agent](hermes-agent.md) | multi-agent | Yes | Self-hosted environment with memory, skills, and subagents | Verified |
| [OpenClaw](openclaw.md) | platform | Yes | Local-first runtime across channels and devices | Verified |
| [LangChain](langchain.md) | platform | Yes | High-level framework for custom agents | Verified |
| [LangGraph](langgraph.md) | platform | Yes | Low-level framework for durable workflows | Verified |
| [Continue](continue.md) | platform | Yes | Open-source IDE extension with full model freedom | Verified |
| [GPT-5.5](gpt-5.5.md) | model / agentic | No | Frontier agentic model powering Codex, ChatGPT, and API surfaces | Verified against launch materials |
| [AutoGPT](autogpt.md) | autonomous | Yes | Visual agent-builder platform with workflows and marketplace | Verified |
| [CrewAI](crewai.md) | multi-agent | Yes | Role-based multi-agent orchestration framework | Verified |
| [LlamaIndex](llamaindex.md) | platform | Yes | Data-first RAG and agent framework | Verified |
| [n8n](n8n.md) | runtime / tools | Fair-code | Visual workflow automation with native AI agent nodes | Verified |
| [MemGPT](memgpt.md) | runtime / tools | Yes | Stateful agents with persistent memory (now Letta) | Verified |
| [Froge Code](froge-code.md) | automation | Yes | Currently mapped to Automagik Genie | Public naming is still evolving |

## Writing Standard

See [evaluation framework](evaluation-framework.md).

## Naming Notes

If a project name or public boundary is ambiguous, this directory keeps the ambiguity visible instead of pretending verification is complete.