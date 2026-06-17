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

> **Last updated:** 2026-06-17 · **Snapshot window:** 2026-06-11 → 2026-06-17 (gain since last update, ~6 days, approximate) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1 (↑) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 62.2k | +8,800 | Watchlist (Skills Wave) | Took the gain lead — Addy Osmani's curated agent-skills collection accelerated past 62k |
| #2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 133.3k | +8,200 | Watchlist (Skills Wave) | Still compounding — Matt Pocock's curated `.claude/skills` directory cleared 133k |
| #3 (↑) | [Superpowers](https://github.com/obra/superpowers) | 230.9k | +6,600 | In scope · [profile](agents/superpowers.md) | The agentic skills framework crossed 230k — the wave's framework anchor keeps compounding |
| #4 (new) | [MiMoCode](https://github.com/XiaomiMiMo/MiMo-Code) | 9.6k | +6,500 | In scope · [profile](agents/mimocode.md) | Breakout — Xiaomi's first-party MiMo CLI roughly tripled (3.1k → 9.6k) in its first full window after being profiled, vaulting into the gain top 10 |
| #5 (↓) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 196.1k | +5,600 | In scope · [profile](agents/hermes-agent.md) | Cooled from the gain lead but kept climbing — the in-scope absolute leader cleared 196k |
| #6 (↓) | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 51.0k | +3,800 | In scope · [profile](agents/codegraph.md) | Slower than its breakout window but still climbing — the pre-indexed code knowledge graph cleared 51k |
| #7 | [anthropics/skills](https://github.com/anthropics/skills) | 152.1k | +2,800 | Watchlist (Skills Wave canonical) | Anthropic's own reference `.claude/skills` repo — the upstream source; steady growth past 152k |
| #8 (↓) | [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 32.4k | +2,300 | Watchlist (Skills Wave) | Still a fast-growing curated skills collection — academic research pipeline for Claude Code crossed 32k |
| #9 | [Pi](https://github.com/earendil-works/pi) | 63.6k | +1,900 | In scope · [profile](agents/pi.md) | Steady climb — the Earendil-owned harness crossed 63k |
| #10 (↓) | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 86.9k | +1,800 | Out of scope | Vertical finance-research multi-agent system — high total, steady gain, but out of scope as a domain vertical |

- Heat is useful for discovery, not for selection by itself.
- The headline this window is [MiMoCode](agents/mimocode.md): Xiaomi's first-party MiMo CLI, profiled here only last week, roughly tripled from ~3.1k to ~9.6k stars and entered the gain top 10 at #4 in its first full window.
- The `.claude/skills` wave retook the gain lead: [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) jumped from #5 to the #1 gain spot, and five of the top ten are again skills collections or frameworks (`addyosmani/agent-skills`, `mattpocock/skills`, `Superpowers`, `anthropics/skills`, `academic-research-skills`). Policy unchanged: curated collections are tracked as Skills Wave entries, the framework end is covered through [Superpowers](agents/superpowers.md).
- [Hermes Agent](agents/hermes-agent.md) cooled from the gain lead (#1 → #5) but kept climbing past 196k; [Superpowers](agents/superpowers.md) crossed 230k.
- **New-inclusion scan** turned up two fresh candidates added to the watchlist — [rmux](https://github.com/Helvesec/rmux) (Helvesec, Rust, 1.8k, a universal typed-SDK multiplexer that drives any CLI, adjacent to [CLI-Anything](agents/cli-anything.md)) and [microsoft/intelligent-terminal](https://github.com/microsoft/intelligent-terminal) (1.1k, a Windows Terminal fork with native agent integration) — but neither clears the in-scope bar yet.
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 379.2k stars (+1.1k); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.
- Continuing to grow but outside the top 10 by gain: [Codex CLI](https://github.com/openai/codex) 91.7k (+1.3k), [Ruflo](agents/ruflo.md) 60.0k (+1.1k), [openhuman](agents/openhuman.md) 32.5k (+1.0k), [agentmemory](https://github.com/rohitg00/agentmemory) 23.3k (+0.9k), [financial-services](https://github.com/anthropics/financial-services) 31.5k (+0.7k), [CLI-Anything](agents/cli-anything.md) 43.3k (+0.6k), [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 28.5k (+0.6k), [CodeWhale](agents/codewhale.md) 38.6k (+0.6k), [Kimi Code](agents/kimi-code.md) 2.5k (+0.3k), [12-factor-agents](https://github.com/humanlayer/12-factor-agents) 23.4k (+0.2k), [jcode](https://github.com/1jehuang/jcode) 7.1k (+0.1k), [CoStrict](agents/costrict.md) 4.2k (flat).

## Market Event: The `.claude/skills` Wave (May 2026, expanding)

The wave that broke into trending in mid-May has intensified. Across the May 12 → 22 snapshots, six of the top ten trending repositories are now skills frameworks, curated skills collections, or methodology docs built on Anthropic's skill pattern:

| Repo | Stars | Shape |
| --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | 145.5k | Anthropic's own canonical Agent Skills reference repository — the upstream source of the pattern |
| [Superpowers](agents/superpowers.md) | 215.5k | A complete skills framework + methodology, with plugin integrations into Claude Code, Codex, Cursor, GitHub Copilot, Gemini, OpenCode, and Factory Droid |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 114.7k | A curated personal `.claude/skills` directory from Matt Pocock — now past 114k stars |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 47.7k | A production-grade engineering skills set for AI coding agents from Addy Osmani |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 26.9k | Ready-to-use Agent Skills for research / science / engineering / analysis / finance / writing |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 26.0k | Curated academic research pipeline (research → write → review → revise → finalize) for Claude Code |

What it means for selection:

- The `.claude/skills` directory pattern Anthropic introduced has crossed from curiosity into shared infrastructure — engineers are now publishing their personal skill libraries the way they used to publish dotfiles, and Anthropic's own reference repo is the canonical anchor.
- For people choosing a coding agent, the underlying agent matters less than it did six months ago — the skill layer on top is doing more of the work, and the breadth of available skill collections is now domain-spanning (engineering, science, academic research, finance, productivity).
- This map treats the "agentic skills framework" as a route in its own right via the [Superpowers](agents/superpowers.md) profile. Curated skill collections (`anthropics/skills`, `mattpocock/skills`, `addyosmani/agent-skills`, `scientific-agent-skills`, `academic-research-skills`) are tracked as Skills Wave watchlist entries rather than profiled, because they are content assets rather than agent surfaces.

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

## Agent Harness Frameworks At A Glance

A "harness" is the minimal scaffolding around an LLM that turns it into an agent — the loop, the tool surface, the permission model, the skills hook. These are projects you can fork, audit, and own end-to-end, rather than vendor products you adopt as-is.

| Project | Stars | License | Sweet spot | Footprint |
| --- | --- | --- | --- | --- |
| [Pi](agents/pi.md) | 58.8k | MIT (TS) | Terminal-first coding harness with broad LLM provider coverage | Small core + opt-in skills/extensions |
| [OpenHands](agents/openhands.md) | 75.7k | Open source | Full open-source SWE agent (CLI + GUI + cloud option) | Heaviest — closer to a product |
| [SWE-agent](agents/swe-agent.md) | 19.4k | MIT (Py) | Research reference behind SWE-bench, single-YAML config | Medium; upstream moving focus to mini-swe-agent |
| [mini-swe-agent](agents/mini-swe-agent.md) | 4.8k | MIT (Py) | ~100-line successor; SWE-bench Verified >74% | Tiny — readable in one sitting |
| [OpenHarness](agents/openharness.md) | 13.4k | MIT (Py) | 10-subsystem open harness with anthropics/skills + MCP + 43 tools | Medium; production-shaped, sibling to [CLI-Anything](agents/cli-anything.md) |

How to read this row:

- Pick by footprint, not by stars. The right harness is the one whose surface area you are willing to maintain.
- If you want the smallest credible base to fork: [mini-swe-agent](agents/mini-swe-agent.md).
- If you want a production-shaped open runtime to self-host: [OpenHarness](agents/openharness.md).
- If you want to publish SWE-bench numbers: [SWE-agent](agents/swe-agent.md) is the canonical reference; mini-swe-agent is the working successor.
- If you want a terminal-first day-to-day coding harness: [Pi](agents/pi.md).
- If you want a more complete SWE agent product that is still open source: [OpenHands](agents/openhands.md).

## The First Cut Of The Map

| Route | Representative projects | Typical user |
| --- | --- | --- |
| Direct execution | [Claude Code](agents/claude-code.md), [Aider](agents/aider.md), [Codex](agents/codex.md), [Kimi Code](agents/kimi-code.md), [MiMoCode](agents/mimocode.md), [CodeWhale](agents/codewhale.md), [Devin](agents/devin.md), [Jules](agents/jules.md) | Someone who wants to hand a concrete coding task to an agent (see the [terminal coding CLI comparison](comparisons/coding-cli-agents.md)) |
| Agent harness framework | [Pi](agents/pi.md), [OpenHands](agents/openhands.md), [SWE-agent](agents/swe-agent.md), [mini-swe-agent](agents/mini-swe-agent.md), [OpenHarness](agents/openharness.md) | Someone who wants to own the agent loop, tool surface, and permissions instead of inheriting a vendor's product |
| Frontier agentic model | [GPT-5.5](agents/gpt-5.5.md) | Someone choosing which model to wire into their own agent system or evaluating the capability ceiling of OpenAI-based surfaces |
| Agentic skills framework | [Superpowers](agents/superpowers.md) | Someone who wants a methodology + composable skills layer that plugs into Claude Code, Codex, Cursor, and similar agents |
| Workflow / orchestration layer | [oh-my-claudecode](agents/oh-my-claudecode.md), [oh-my-codex](agents/oh-my-codex.md), [Ruflo](agents/ruflo.md) | Someone who already likes Claude Code or Codex and wants stronger orchestration on top (Ruflo extends this to multi-machine federation and 100+ specialized agents) |
| Editor-centric AI workflow | [Cursor](agents/cursor.md), [Windsurf](agents/windsurf.md), [Continue](agents/continue.md) | Someone who wants the editor itself to stay central |
| Review-first automation | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md), [CoStrict](agents/costrict.md) | Someone who wants review and human control to stay central (CoStrict adds enterprise strict-workflow + private deployment) |
| Managed background path | [Claude Managed Agents](agents/claude-managed-agents.md) | Someone who needs scheduled, cloud, or detached Anthropic workflows |
| General-purpose autonomous agent | [AutoGPT](agents/autogpt.md), [Agent Zero](agents/agent-zero.md), [BabyAGI](agents/babyagi.md), [Julep](agents/julep.md), [GenericAgent](agents/generic-agent.md), [ml-intern](agents/ml-intern.md) | Someone who wants autonomous, general-purpose task execution (or, in ml-intern's case, autonomous ML engineering) |
| Build-your-own system | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md), [Haystack](agents/haystack.md), [Semantic Kernel](agents/semantic-kernel.md), [DSPy](agents/dspy.md), [Pydantic AI](agents/pydantic-ai.md) | Teams building their own agent platform instead of buying one |
| Runtime and tools | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [CLI-Anything](agents/cli-anything.md) | Teams that need workflow automation, code execution, LLM gateways, agent context infrastructure, agent-driven CLIs, or visual builders |
| Self-hosted / local runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md), [OpenHuman](agents/openhuman.md) | Users who need on-device privacy, long-running agents, local control, channels, devices, or personal-data life integration |

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
| [CodeWhale](agents/codewhale.md) | Direct execution | DeepSeek + MiMo terminal coding agent (formerly DeepSeek-TUI) |
| [Kimi Code](agents/kimi-code.md) | Direct execution | Moonshot AI's official Kimi-native terminal coding CLI (successor to kimi-cli) |
| [MiMoCode](agents/mimocode.md) | Direct execution | Xiaomi's official MiMo terminal coding agent with built-in cross-session memory |
| [CoStrict](agents/costrict.md) | Review-first automation | Enterprise Cline-lineage coding agent with strict standardized workflow, AI code review, and private deployment |
| [Ruflo](agents/ruflo.md) | Workflow / orchestration layer | Multi-agent orchestration platform for Claude with federation across machines, neural memory, and 100+ specialized agents |
| [OpenHuman](agents/openhuman.md) | Self-hosted / local runtime | Desktop life-integration agent with 118+ connectors, local Memory Tree, and Ollama support |
| [CodeGraph](agents/codegraph.md) | Runtime and tools | Pre-indexed code knowledge graph + MCP server for Claude Code, Cursor, Codex CLI, opencode, and Hermes Agent |
| [CLI-Anything](agents/cli-anything.md) | Runtime and tools | Auto-generates Click-based CLIs for arbitrary software so agents can drive non-API apps |
| [SWE-agent](agents/swe-agent.md) | Agent harness framework | Princeton + Stanford's original SWE-bench harness with single-YAML configuration |
| [mini-swe-agent](agents/mini-swe-agent.md) | Agent harness framework | The ~100-line Python successor to SWE-agent that still scores >74% on SWE-bench Verified |
| [OpenHarness](agents/openharness.md) | Agent harness framework | HKUDS's 10-subsystem open agent harness with 43+ tools, anthropics/skills, and MCP |

## Example Reading Paths

If you are still deciding where to begin, use one of these quick routes and then branch out.

| If you sound like this... | Follow this path | What it helps you answer |
| --- | --- | --- |
| I want a day-to-day coding agent and need to choose terminal vs editor | [Aider](agents/aider.md) → [Claude Code](agents/claude-code.md) → [terminal coding CLI comparison](comparisons/coding-cli-agents.md) → [Cursor](agents/cursor.md) → [Cline](agents/cline.md) → [coding automation guide](use-cases/coding-automation.md) | Which vendor CLI fits your model, terminal-first local loop vs editor-led flow vs approval-first control |
| I already like Claude Code or Codex but want stronger orchestration | [Claude Code](agents/claude-code.md) → [oh-my-claudecode](agents/oh-my-claudecode.md) → [Codex](agents/codex.md) → [oh-my-codex](agents/oh-my-codex.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | When the base agent is enough and when a workflow layer actually adds value |
| I want to understand GPT-5.5's impact on the agent landscape | [GPT-5.5](agents/gpt-5.5.md) → [Codex](agents/codex.md) → [Claude Code](agents/claude-code.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | How a frontier model release shifts the capability ceiling and what it means for product choice |
| I want a dedicated AI IDE instead of stitching tools together | [Cursor](agents/cursor.md) → [Windsurf](agents/windsurf.md) → [GitHub Copilot](agents/github-copilot.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Dedicated AI editor vs ecosystem platform |
| I want to hand off tickets and check back later | [Codex](agents/codex.md) → [Jules](agents/jules.md) → [Devin](agents/devin.md) → [Claude Managed Agents](agents/claude-managed-agents.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Async cloud delegation vs managed background automation |
| I need something open-source or self-hosted | [Aider](agents/aider.md) → [OpenHands](agents/openhands.md) → [Goose](agents/goose.md) → [Hermes Agent](agents/hermes-agent.md) → [capabilities](capabilities/README.md) | Terminal control, open-source execution, and local runtime ownership |
| I am building an internal agent stack, not buying a product | [LangChain](agents/langchain.md) → [LangGraph](agents/langgraph.md) → [capabilities](capabilities/README.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Framework vs runtime vs product boundaries |

## Disclaimer

Star counts and 7-day gains are point-in-time GitHub snapshots taken when the repo is updated; numbers shift quickly between weekly refreshes and small rounding differences are expected. Project descriptions, vendors, and capability summaries reflect public information at the time of writing and may change as projects evolve, get acquired, or pivot. This map is selection guidance — not endorsement, financial advice, or a production-readiness guarantee. Verify against each project's own docs before committing to a choice.