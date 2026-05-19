# Agents

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/README.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](README.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

This is not a wall of names.

Think of it as a shortlist directory: understand the route first, then decide which profile is worth opening.

## Browse By Route

| Route | Representative projects | Best for |
| --- | --- | --- |
| Direct execution | [Claude Code](claude-code.md), [Aider](aider.md), [Codex](codex.md), [Pi](pi.md), [DeepSeek-TUI](deepseek-tui.md), [Devin](devin.md), [Jules](jules.md), [OpenHands](openhands.md) | People who want to hand a coding task directly to an agent |
| Frontier agentic model | [GPT-5.5](gpt-5.5.md) | People choosing which model to wire into their agent system, or evaluating the capability ceiling of OpenAI surfaces |
| Agentic skills framework | [Superpowers](superpowers.md) | Users who want a methodology + composable skills layer that plugs into Claude Code, Codex, Cursor, and other agents |
| Workflow / orchestration layer | [oh-my-claudecode](oh-my-claudecode.md), [oh-my-codex](oh-my-codex.md), [Ruflo](ruflo.md) | Users who already like Claude Code or Codex and want stronger teams, skills, and persistent workflow (Ruflo extends this to multi-machine federation) |
| Editor-centric AI workflow | [Cursor](cursor.md), [Windsurf](windsurf.md), [Continue](continue.md) | Users who want the editor itself to be the main agent surface |
| Review-first automation | [Cline](cline.md), [GitHub Copilot](github-copilot.md), [Froge Code](froge-code.md) | People who want review and human pacing to stay central |
| General-purpose autonomous agent | [AutoGPT](autogpt.md), [Agent Zero](agent-zero.md), [BabyAGI](babyagi.md), [Julep](julep.md), [GenericAgent](generic-agent.md), [ml-intern](ml-intern.md) | People who want autonomous general-purpose task execution (ml-intern is the ML-specialized variant) |
| Build-your-own platform | [LangChain](langchain.md), [LangGraph](langgraph.md), [CrewAI](crewai.md), [LlamaIndex](llamaindex.md), [Haystack](haystack.md), [Semantic Kernel](semantic-kernel.md), [DSPy](dspy.md), [Pydantic AI](pydantic-ai.md) | Teams building their own agent system |
| Runtime and tools | [n8n](n8n.md), [MemGPT](memgpt.md), [Open Interpreter](open-interpreter.md), [LiteLLM](litellm.md), [Flowise](flowise.md) | Teams needing workflow automation, code execution, LLM gateways, or visual builders |
| Self-hosted / local runtime | [AI Edge Gallery](ai-edge-gallery.md), [Goose](goose.md), [Hermes Agent](hermes-agent.md), [OpenClaw](openclaw.md), [Mercury Agent](mercury-agent.md) | Users who need local control, on-device privacy, extensions, channels, or deeper runtime ownership |
| Managed background path | [Claude Managed Agents](claude-managed-agents.md) | Users who need scheduled, cloud, or detached execution |

## Recent Heat Snapshot

This is not a ranking of quality.

It is a quick view of projects that appeared especially hot in the latest weekly GitHub snapshot. The order follows the 7-day gain, while the star totals below reflect the current counts checked during this repo update.

> **Last updated:** 2026-05-19 · **Snapshot window:** 2026-05-12 → 2026-05-18 (7-day gain, approximate) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When a profile exists in this directory, it is linked separately in the "Directory status" column.

| Rank | Project | Current stars | Snapshot gain | Directory status | Note |
| --- | --- | --- | --- | --- | --- |
| #1 (new) | [DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | 32.3k | +13,500 | [Profile](deepseek-tui.md) (added this week) | DeepSeek-native terminal coding agent — biggest single-week surge in this snapshot |
| #2 (new) | [mattpocock/skills](https://github.com/mattpocock/skills) | 93.3k | +12,000 | Watchlist | Matt Pocock's curated `.claude/skills` directory — not an agent itself; representative example of the skills wave |
| #3 (new) | [openhuman](https://github.com/tinyhumansai/openhuman) | 19.4k | +11,500 | Watchlist | Self-described "personal AI super intelligence" desktop agent — positioning still settling |
| #4 (new) | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 25.7k | +9,000 | Not included | Anthropic's vertical SDK for financial services — agent-adjacent, not generic agent infrastructure |
| #5 (new) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 43.6k | +7,500 | Watchlist | Production-grade engineering skills for AI coding agents — another data point in the same skills wave |
| #6 (new) | [Superpowers](https://github.com/obra/superpowers) | 197.7k | +6,500 | [Profile](superpowers.md) (added this week) | Jesse Vincent's agentic skills framework — composable skills + plugin marketplace with Claude Code, Codex, Cursor, GitHub Copilot, Gemini, and more |
| #7 (new) | [Ruflo](https://github.com/ruvnet/ruflo) | 53.0k | +5,500 | [Profile](ruflo.md) (added this week) | Multi-agent orchestration platform for Claude Code (rebranded from Claude Flow) — multi-machine federation, neural memory, 100+ specialized agents |
| #8 (new) | [agentmemory](https://github.com/rohitg00/agentmemory) | 13.6k | +5,000 | Watchlist | Persistent memory layer for AI coding agents — overlaps with [MemGPT](memgpt.md) territory |
| #9 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 157.3k | +4,500 | [Profile](hermes-agent.md) | Fourth consecutive week of growth — still the in-scope absolute leader |
| #10 | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 77.2k | +4,500 | Not included | Tauric Research's multi-agent finance framework — still hot, scope unchanged (research-only, domain-specific) |

**Market events:**
- **May 2026 (this snapshot)** — The `.claude/skills` wave: three of the top six trending repos are skills frameworks or curated skills collections (Superpowers, mattpocock/skills, agent-skills). The new [Superpowers](superpowers.md) profile captures the framework end of this trend.
- **April 8 2026** — Earendil (Armin Ronacher's company) acquired the [Pi](pi.md) project from Mario Zechner; the repo moved from `badlogic/pi-mono` to `earendil-works/pi`, and Earendil also began building Lefos, a cloud agent platform on top of it.
- **April 16 2026** — OpenAI shipped "Codex for (almost) everything," adding Background Computer Use, parallel multi-agent execution, an in-app browser, and 90+ plugins on the [Codex](codex.md) product surface. Reported 3M weekly active developers, ~2x early-March 2026.
- **April 23 2026** — OpenAI released [GPT-5.5](gpt-5.5.md), the model layer powering Codex, ChatGPT, and every OpenAI-API-based agent.

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
| [Agent Zero](agent-zero.md) | autonomous | Yes | Self-building autonomous agent with dynamic tool creation | Verified |
| [BabyAGI](babyagi.md) | experimental | Yes | Pioneering autonomous agent experiment — educational | Verified |
| [Julep](julep.md) | workflow engine | Yes | Temporal-backed durable workflow engine for stateful agents | Verified |
| [Haystack](haystack.md) | platform | Yes | Production-oriented RAG and agent framework by deepset | Verified |
| [Semantic Kernel](semantic-kernel.md) | platform | Yes | Microsoft AI orchestration SDK for .NET, Python, Java | Verified |
| [DSPy](dspy.md) | platform | Yes | Programmatic prompt optimization framework | Verified |
| [Open Interpreter](open-interpreter.md) | runtime / tools | Yes | Natural language to local code execution | Verified |
| [LiteLLM](litellm.md) | infrastructure | Yes | Unified API gateway for 100+ LLM providers | Verified |
| [Pydantic AI](pydantic-ai.md) | platform | Yes | Type-safe Python agent framework with structured outputs | Verified |
| [Flowise](flowise.md) | runtime / tools | Yes | Visual drag-and-drop LLM app and agent builder | Verified |
| [Froge Code](froge-code.md) | automation | Yes | Currently mapped to Automagik Genie | Public naming is still evolving |
| [Mercury Agent](mercury-agent.md) | multi-channel runtime | Yes | Permission-hardened self-hosted agent for CLI and Telegram with token budgets | Verified against current repo |
| [Pi](pi.md) | execution / toolkit | Yes | Minimal terminal coding-agent harness with multi-provider LLM support | Verified after April 2026 acquisition by Earendil |
| [ml-intern](ml-intern.md) | autonomous (domain-specific) | Yes | Autonomous ML engineering agent built on the Hugging Face ecosystem | Verified |
| [GenericAgent](generic-agent.md) | autonomous (self-evolving) | Yes | Small-seed agent that grows a personal skill tree on every task | Verified after week-2 of watchlist tracking |
| [Superpowers](superpowers.md) | skills framework / methodology | Yes | Composable agentic skills framework with Claude Code, Codex, Cursor, Copilot, Gemini plugins | Verified at v5.1 (May 2026) |
| [DeepSeek-TUI](deepseek-tui.md) | execution (DeepSeek-native) | Yes | DeepSeek-native terminal coding agent | Verified during May 2026 surge |
| [Ruflo](ruflo.md) | multi-agent orchestration | Yes | Multi-machine federated Claude orchestration platform (formerly Claude Flow) | Verified after rebrand |

## Writing Standard

See [evaluation framework](evaluation-framework.md).

## Naming Notes

If a project name or public boundary is ambiguous, this directory keeps the ambiguity visible instead of pretending verification is complete.