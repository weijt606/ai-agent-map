# AI Agent Map

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](zh/README.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](README.md)
[![License](https://img.shields.io/badge/LICENSE-MIT-16a34a?style=for-the-badge&labelColor=166534)](LICENSE)
[![Agent](https://img.shields.io/badge/AGENT-MAP-d97706?style=for-the-badge&labelColor=92400e)](agents/README.md)

<p align="center">
	<img src="assets/ai-agent-map-pixel-en.png" alt="Pixel-art style AI Agent Map banner showing four regions — daily coding agents, general autonomous agents, frameworks and platforms, and runtimes and tools — with agent icons placed on an illustrated treasure-map landscape" width="100%" />
</p>

AI Agent Map is a practical, visual-first guide for comparing mainstream AI agents, agent platforms, runtimes, and orchestration tools.

The goal is simple: help readers get to a sensible shortlist faster.

## What This Repo Is For

- The agent landscape is crowded.
- Many resources explain ideas, but not fit, anti-fit, or operating cost.
- People usually need a comparison layer, not another pile of links.

This repo stays focused on selection: what a system is good at, where it breaks down, and what kind of operator cost comes with it.

## Where To Start

| If your question is... | Start here |
| --- | --- |
| I need a shortlist first | [![Open agents](https://img.shields.io/badge/OPEN-AGENTS-d97706?style=for-the-badge&labelColor=92400e)](agents/README.md) |
| I need help choosing for coding automation | [![Read coding guide](https://img.shields.io/badge/READ-CODING%20GUIDE-2563eb?style=for-the-badge&labelColor=1d4ed8)](use-cases/coding-automation.md) |
| I already have candidates and want a side-by-side view | [![View mainstream matrix](https://img.shields.io/badge/VIEW-MAINSTREAM%20MATRIX-dc2626?style=for-the-badge&labelColor=991b1b)](comparisons/mainstream-agent-landscape.md) |
| I care about dimensions like approval, memory, scheduling, and deployment | [![Browse capabilities](https://img.shields.io/badge/BROWSE-CAPABILITIES-16a34a?style=for-the-badge&labelColor=166534)](capabilities/README.md) |

## Recent Heat Ranking

Popularity is not fit.

This table tracks projects that showed up as especially hot in the latest weekly GitHub snapshot. The rank follows the 7-day gain. The total star counts below were checked when this repo was updated.

> **Last updated:** 2026-05-19 · **Snapshot window:** 2026-05-12 → 2026-05-18 (7-day gain, approximate) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1 (new) | [DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI) | 32.3k | +13,500 | In scope · [profile](agents/deepseek-tui.md) (new) | DeepSeek-native terminal coding agent — the biggest single-week surge in this snapshot, fills a real gap as the first directory entry built around the DeepSeek model family |
| #2 (new) | [mattpocock/skills](https://github.com/mattpocock/skills) | 93.3k | +12,000 | Watchlist | A curated `.claude/skills` collection by Matt Pocock — not an agent itself, but a representative example of the skills wave (see Market Event below) |
| #3 (new) | [openhuman](https://github.com/tinyhumansai/openhuman) | 19.4k | +11,500 | Watchlist | Self-described "personal AI super intelligence" desktop agent — positioning still settling; revisit in 1-2 weeks once the boundary is clearer |
| #4 (new) | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 25.7k | +9,000 | Out of scope | Anthropic's vertical SDK for financial services — agent-adjacent, but a domain accelerator pack rather than a generic agent surface |
| #5 (new) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 43.6k | +7,500 | Watchlist | Production-grade engineering skills for AI coding agents from Addy Osmani — another data point in the same skills wave |
| #6 (new) | [Superpowers](https://github.com/obra/superpowers) | 197.7k | +6,500 | In scope · [profile](agents/superpowers.md) (new) | Jesse Vincent's agentic skills framework and methodology — composable skills + plugin marketplace integration with Claude Code, Codex, Cursor, GitHub Copilot, Gemini and more |
| #7 (new) | [Ruflo](https://github.com/ruvnet/ruflo) | 53.0k | +5,500 | In scope · [profile](agents/ruflo.md) (new) | Multi-agent orchestration platform for Claude Code (rebranded from Claude Flow) — federation across machines, 100+ specialized agents, neural memory |
| #8 (new) | [agentmemory](https://github.com/rohitg00/agentmemory) | 13.6k | +5,000 | Watchlist | Persistent memory layer for AI coding agents — overlaps with [MemGPT](agents/memgpt.md) territory; revisit if it sustains its second week of growth |
| #9 | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 157.3k | +4,500 | In scope · [profile](agents/hermes-agent.md) | Self-hosted multi-agent environment — fourth consecutive week of growth, now past 157k absolute |
| #10 | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 77.2k | +4,500 | Out of scope | Tauric Research's multi-agent finance framework — still hot but unchanged scope decision: domain-specific, research-only |

- Heat is useful for discovery, not for selection by itself.
- This week added three new in-scope profiles: [Superpowers](agents/superpowers.md), [DeepSeek-TUI](agents/deepseek-tui.md), and [Ruflo](agents/ruflo.md). Each one is the most-starred representative of a route not previously covered (skills framework / methodology, DeepSeek-native terminal agent, multi-machine federation orchestration).
- `mattpocock/skills` and `addyosmani/agent-skills` are intentionally on watchlist rather than profiled: a curated `.claude/skills` directory is a content asset, not an agent surface — the underlying skills pattern is captured through the [Superpowers](agents/superpowers.md) profile.
- `openhuman` and `agentmemory` are on watchlist for one more week; positioning needs to stabilize before a profile is worthwhile.
- `anthropics/financial-services` is intentionally out of scope: Anthropic is shipping vertical SDKs alongside the agent platform, but this map only tracks generic agent infrastructure. Note the trend ("agent vendors going vertical") even if the repo itself does not get a profile.
- Codex CLI (83.7k, ~+2.3k), Pi (51.5k, ~+3.0k), oh-my-claudecode (34.3k, ~+1.4k), GenericAgent (11.8k, ~+1.5k), ml-intern (9.6k, ~+0.7k) all continued to grow but dropped out of the top 10 this week as the skills wave and DeepSeek-TUI absorbed most of the trending oxygen.

## Market Event: The `.claude/skills` Wave (May 2026)

In the May 12 → 18 snapshot, three of the top six trending repositories were `.claude/skills` collections or frameworks built on top of Anthropic's skill pattern:

| Repo | Stars | Shape |
| --- | --- | --- |
| [Superpowers](agents/superpowers.md) | 197.7k | A complete skills framework + methodology, with plugin integrations into Claude Code, Codex, Cursor, GitHub Copilot, Gemini, OpenCode, and Factory Droid |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 93.3k | A curated personal `.claude/skills` directory from Matt Pocock — 18 skills across engineering, productivity, and miscellaneous |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 43.6k | A production-grade engineering skills set for AI coding agents from Addy Osmani |

What it means for selection:

- The `.claude/skills` directory pattern Anthropic introduced has crossed from curiosity into shared infrastructure — engineers are now publishing their personal skill libraries the way they used to publish dotfiles.
- For people choosing a coding agent, the underlying agent matters less than it did six months ago — the skill layer on top is doing more of the work.
- This map now treats the "agentic skills framework" as a route in its own right via the new [Superpowers](agents/superpowers.md) profile. Pure curated skill collections (`mattpocock/skills`, `addyosmani/agent-skills`) are tracked as watchlist entries rather than profiled, because they are content assets rather than agent surfaces.

## Market Event: GPT-5.5 Enters The Agent Landscape

On April 23 2026, OpenAI released [GPT-5.5](agents/gpt-5.5.md) — positioned as "a new class of intelligence for real work and powering agents." This is not a GitHub-trending project but a model release that reshapes the capability ceiling across multiple agent surfaces already tracked in this repo.

| What changed | Impact on this map |
| --- | --- |
| 82.7% on Terminal-Bench 2.0 | Highest agentic coding benchmark at launch — raises the bar for Codex and all OpenAI-API-based agents |
| 1M token context window | Long-context tasks that were impractical before become viable for API-based agent builders |
| 2x price vs GPT-5.4 | Cost-sensitive teams must re-benchmark per-task economics |
| SWE-Bench Pro at 58.6% | Still trails Claude Opus 4.7 (64.3%) — model choice depends on workload |

GPT-5.5 does not replace [Codex](agents/codex.md) as a product entry. It is the model layer underneath. See the [GPT-5.5 profile](agents/gpt-5.5.md) for the full breakdown.

### Codex Product Update (April 16 2026)

A week before the GPT-5.5 release, OpenAI shipped "Codex for (almost) everything," a major capability expansion on the [Codex](agents/codex.md) product surface itself.

| What changed | Why it matters |
| --- | --- |
| Background Computer Use | Codex can see, click, and type with its own cursor across any macOS app — even ones without an API |
| Parallel multi-agent execution | Multiple Codex agents can run on the same Mac in parallel without interfering with foreground work |
| 90+ new plugins | Atlassian Rovo, CircleCI, CodeRabbit, GitLab Issues, Microsoft Suite, and more |
| In-app browser + proactive suggestions | Direct iteration on frontend designs and proactive proposals from project context and memory |
| 3M weekly active developers | Reported in April 2026, nearly 2x early-March 2026 |

Combined with the GPT-5.5 backbone, this is the most consequential agent product update in the snapshot window.

## The First Cut Of The Map

| Route | Representative projects | Typical user |
| --- | --- | --- |
| Direct execution | [Claude Code](agents/claude-code.md), [Aider](agents/aider.md), [Codex](agents/codex.md), [Pi](agents/pi.md), [DeepSeek-TUI](agents/deepseek-tui.md), [Devin](agents/devin.md), [Jules](agents/jules.md), [OpenHands](agents/openhands.md) | Someone who wants to hand a concrete coding task to an agent |
| Frontier agentic model | [GPT-5.5](agents/gpt-5.5.md) | Someone choosing which model to wire into their own agent system or evaluating the capability ceiling of OpenAI-based surfaces |
| Agentic skills framework | [Superpowers](agents/superpowers.md) | Someone who wants a methodology + composable skills layer that plugs into Claude Code, Codex, Cursor, and similar agents |
| Workflow / orchestration layer | [oh-my-claudecode](agents/oh-my-claudecode.md), [oh-my-codex](agents/oh-my-codex.md), [Ruflo](agents/ruflo.md) | Someone who already likes Claude Code or Codex and wants stronger orchestration on top (Ruflo extends this to multi-machine federation and 100+ specialized agents) |
| Editor-centric AI workflow | [Cursor](agents/cursor.md), [Windsurf](agents/windsurf.md), [Continue](agents/continue.md) | Someone who wants the editor itself to stay central |
| Review-first automation | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md) | Someone who wants review and human control to stay central |
| Managed background path | [Claude Managed Agents](agents/claude-managed-agents.md) | Someone who needs scheduled, cloud, or detached Anthropic workflows |
| General-purpose autonomous agent | [AutoGPT](agents/autogpt.md), [Agent Zero](agents/agent-zero.md), [BabyAGI](agents/babyagi.md), [Julep](agents/julep.md), [GenericAgent](agents/generic-agent.md), [ml-intern](agents/ml-intern.md) | Someone who wants autonomous, general-purpose task execution (or, in ml-intern's case, autonomous ML engineering) |
| Build-your-own system | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md), [Haystack](agents/haystack.md), [Semantic Kernel](agents/semantic-kernel.md), [DSPy](agents/dspy.md), [Pydantic AI](agents/pydantic-ai.md) | Teams building their own agent platform instead of buying one |
| Runtime and tools | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md) | Teams that need workflow automation, code execution, LLM gateways, or visual builders |
| Self-hosted / local runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md) | Users who need on-device privacy, long-running agents, local control, channels, or devices |

## Repo Structure

| Directory | Purpose |
| --- | --- |
| [![Open agents](https://img.shields.io/badge/OPEN-AGENTS-d97706?style=for-the-badge&labelColor=92400e)](agents/README.md) | One page per agent with positioning, boundary, and trade-off. |
| [![Open use cases](https://img.shields.io/badge/OPEN-USE%20CASES-2563eb?style=for-the-badge&labelColor=1d4ed8)](use-cases/README.md) | Problem-first selection guides. |
| [![Open comparisons](https://img.shields.io/badge/OPEN-COMPARISONS-dc2626?style=for-the-badge&labelColor=991b1b)](comparisons/README.md) | Side-by-side comparisons for real decisions. |
| [![Open capabilities](https://img.shields.io/badge/OPEN-CAPABILITIES-16a34a?style=for-the-badge&labelColor=166534)](capabilities/README.md) | Shared vocabulary for capability differences. |

## Current Mainstream Coverage

| Project | Route | One-line positioning |
| --- | --- | --- |
| [Aider](agents/aider.md) | Direct execution | Terminal-first AI pair programmer close to git |
| [Claude Code](agents/claude-code.md) | Direct execution | Local and IDE-first coding agent |
| [Claude Managed Agents](agents/claude-managed-agents.md) | Managed background path | Anthropic managed / cloud execution mapping |
| [Codex](agents/codex.md) | Direct execution | Async coding delegation in isolated cloud environments |
| [oh-my-claudecode](agents/oh-my-claudecode.md) | Workflow layer | Teams-first orchestration layer on top of Claude Code |
| [oh-my-codex](agents/oh-my-codex.md) | Workflow layer | Stronger workflow, teams, and persistent state around Codex CLI |
| [Cursor](agents/cursor.md) | Editor-centric platform | AI editor spanning local coding, cloud agents, and integrations |
| [GitHub Copilot](agents/github-copilot.md) | Platform | Multi-surface agent platform across VS Code and GitHub |
| [Cline](agents/cline.md) | Review-first execution | Approval-first editor-native coding agent |
| [Windsurf](agents/windsurf.md) | AI-native IDE | Cascade-centered AI IDE |
| [OpenHands](agents/openhands.md) | Open-source execution | Open-source software engineering agent |
| [Devin](agents/devin.md) | Managed execution | End-to-end managed software engineering execution |
| [Jules](agents/jules.md) | Managed cloud execution | GitHub-connected coding delegation with PR handoff |
| [AI Edge Gallery](agents/ai-edge-gallery.md) | On-device local runtime | Mobile-first local assistant sandbox with agent skills |
| [Goose](agents/goose.md) | Open-source local platform | Extensible local agent across desktop, CLI, and API |
| [Hermes Agent](agents/hermes-agent.md) | Multi-agent / self-hosted | Long-lived self-hosted environment with memory and skills |
| [OpenClaw](agents/openclaw.md) | Runtime | Local-first multi-channel runtime layer |
| [LangChain](agents/langchain.md) | Platform | High-level framework for building custom agents quickly |
| [LangGraph](agents/langgraph.md) | Platform | Low-level framework for durable stateful workflows |
| [Continue](agents/continue.md) | Editor-centric | Open-source IDE extension with full model freedom |
| [GPT-5.5](agents/gpt-5.5.md) | Frontier agentic model | OpenAI's agentic model powering Codex, ChatGPT, and API agent builders |
| [AutoGPT](agents/autogpt.md) | Autonomous agent platform | Visual agent builder with workflows, marketplace, and multi-model support |
| [CrewAI](agents/crewai.md) | Multi-agent framework | Role-based agent collaboration with fast prototyping |
| [LlamaIndex](agents/llamaindex.md) | Data-first framework | RAG and agentic applications over documents and data |
| [n8n](agents/n8n.md) | Workflow automation | Visual workflow platform with native AI agent nodes and 400+ integrations |
| [MemGPT](agents/memgpt.md) | Stateful agent platform | Persistent memory agents that learn across sessions (now Letta) |
| [Agent Zero](agents/agent-zero.md) | Autonomous agent | Self-building autonomous agent with dynamic tool creation |
| [BabyAGI](agents/babyagi.md) | Experimental | Pioneering autonomous agent experiment — educational, not production |
| [Julep](agents/julep.md) | Workflow engine | Temporal-backed durable workflow engine for stateful AI agents |
| [Haystack](agents/haystack.md) | Framework | Production-oriented RAG and agent framework by deepset |
| [Semantic Kernel](agents/semantic-kernel.md) | Framework | Microsoft's AI orchestration SDK for .NET, Python, and Java |
| [DSPy](agents/dspy.md) | Framework | Programmatic prompt optimization — programming, not prompting, LMs |
| [Open Interpreter](agents/open-interpreter.md) | Runtime | Natural language to local code execution, no sandbox |
| [LiteLLM](agents/litellm.md) | Infrastructure | Unified API gateway for 100+ LLM providers |
| [Pydantic AI](agents/pydantic-ai.md) | Framework | Type-safe Python agent framework with structured outputs |
| [Flowise](agents/flowise.md) | Visual builder | Drag-and-drop LLM app and agent builder on top of LangChain |
| [Froge Code](agents/froge-code.md) | Review-first automation | Provisionally mapped to Automagik Genie |
| [Mercury Agent](agents/mercury-agent.md) | Self-hosted multi-channel | Permission-hardened agent for CLI and Telegram with token budgets |
| [Pi](agents/pi.md) | Direct execution | Minimal terminal coding-agent harness with multi-provider LLM support |
| [ml-intern](agents/ml-intern.md) | Domain-specific autonomous agent | Hugging Face's autonomous ML engineer — research, code, and ship ML using HF tooling |
| [GenericAgent](agents/generic-agent.md) | Self-evolving autonomous agent | Small-seed agent that grows a personal skill tree on every task |
| [Superpowers](agents/superpowers.md) | Agentic skills framework | Methodology and composable skills layer that plugs into Claude Code, Codex, Cursor, and other agents |
| [DeepSeek-TUI](agents/deepseek-tui.md) | Direct execution | DeepSeek-native terminal coding agent |
| [Ruflo](agents/ruflo.md) | Workflow / orchestration layer | Multi-agent orchestration platform for Claude with federation across machines, neural memory, and 100+ specialized agents |

## Example Reading Paths

If you are still deciding where to begin, use one of these quick routes and then branch out.

| If you sound like this... | Follow this path | What it helps you answer |
| --- | --- | --- |
| I want a day-to-day coding agent and need to choose terminal vs editor | [Aider](agents/aider.md) → [Claude Code](agents/claude-code.md) → [Cursor](agents/cursor.md) → [Cline](agents/cline.md) → [coding automation guide](use-cases/coding-automation.md) | Terminal-first local loop vs editor-led flow vs approval-first control |
| I already like Claude Code or Codex but want stronger orchestration | [Claude Code](agents/claude-code.md) → [oh-my-claudecode](agents/oh-my-claudecode.md) → [Codex](agents/codex.md) → [oh-my-codex](agents/oh-my-codex.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | When the base agent is enough and when a workflow layer actually adds value |
| I want to understand GPT-5.5's impact on the agent landscape | [GPT-5.5](agents/gpt-5.5.md) → [Codex](agents/codex.md) → [Claude Code](agents/claude-code.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | How a frontier model release shifts the capability ceiling and what it means for product choice |
| I want a dedicated AI IDE instead of stitching tools together | [Cursor](agents/cursor.md) → [Windsurf](agents/windsurf.md) → [GitHub Copilot](agents/github-copilot.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Dedicated AI editor vs ecosystem platform |
| I want to hand off tickets and check back later | [Codex](agents/codex.md) → [Jules](agents/jules.md) → [Devin](agents/devin.md) → [Claude Managed Agents](agents/claude-managed-agents.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Async cloud delegation vs managed background automation |
| I need something open-source or self-hosted | [Aider](agents/aider.md) → [OpenHands](agents/openhands.md) → [Goose](agents/goose.md) → [Hermes Agent](agents/hermes-agent.md) → [capabilities](capabilities/README.md) | Terminal control, open-source execution, and local runtime ownership |
| I am building an internal agent stack, not buying a product | [LangChain](agents/langchain.md) → [LangGraph](agents/langgraph.md) → [capabilities](capabilities/README.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Framework vs runtime vs product boundaries |

## Disclaimer

Star counts and 7-day gains are point-in-time GitHub snapshots taken when the repo is updated; numbers shift quickly between weekly refreshes and small rounding differences are expected. Project descriptions, vendors, and capability summaries reflect public information at the time of writing and may change as projects evolve, get acquired, or pivot. This map is selection guidance — not endorsement, financial advice, or a production-readiness guarantee. Verify against each project's own docs before committing to a choice.