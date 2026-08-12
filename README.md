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
| I want every project scored on those dimensions, side by side | [Capability matrix](capabilities/matrix.md) |
| I want to know what it actually costs to run, and which model tier is worth it | [Cost & benchmarks](comparisons/cost-and-benchmarks.md) · [Memory approaches](comparisons/memory-approaches.md) |
| My agents already run — I need to know whether they still work | [Observability & evaluation](comparisons/observability-and-evals.md) |
| I want the stock rankings and the weekly trend chart | [![View rankings](https://img.shields.io/badge/VIEW-RANKINGS-7c3aed?style=for-the-badge&labelColor=5b21b6)](rankings/README.md) |
| I want problem-first guides or the full comparison list | [Use cases](use-cases/README.md) · [Comparisons](comparisons/README.md) |

## Recent Heat Ranking

Popularity is not fit.

This table tracks projects that showed up as especially hot in the latest weekly GitHub snapshot. The rank follows the 7-day gain. The total star counts below were checked when this repo was updated.

> **Last updated:** 2026-08-12 · **Snapshot window:** 2026-08-05 → 2026-08-12 (gain since last update, 7 days, approximate) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(=) | [mattpocock/skills](https://github.com/mattpocock/skills) | 214.3k | +10,291 | Watchlist (Skills Wave) | An eighth straight window at #1, past **214k** — the gain finally eased (−8%), and it still out-gains #2 by 2.2× |
| #2&nbsp;(new) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 86.4k | +4,664 | Watchlist (Skills Wave) | Off the table last week at +945, now #2 on a **4.9× jump** — the sharpest re-acceleration this board has recorded |
| #3&nbsp;(↓) | [Pi](https://github.com/earendil-works/pi) | 88.1k | +4,166 | In scope · [profile](agents/pi.md) | Slipped one on a flat gain (+4,263 → +4,166) — it was passed, not slowed; cleared 88k |
| #4&nbsp;(↓) | [Superpowers](https://github.com/obra/superpowers) | 270.9k | +4,083 | In scope · [profile](agents/superpowers.md) | Down one, also on a flat gain — cleared 270k as the wave's framework anchor |
| #5&nbsp;(↓) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 229.2k | +3,496 | In scope · [profile](agents/hermes-agent.md) | Down one as the gain cooled 10% — still the in-scope absolute leader, past 229k |
| #6&nbsp;(new) | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 97.7k | +2,050 | Out of scope (finance-research vertical) | Its biggest window on record (+785 → +2,050, 2.6×), closing on 100k — tracked, but still not an in-scope agent surface |
| #7&nbsp;(=) | [anthropics/skills](https://github.com/anthropics/skills) | 168.4k | +1,999 | Watchlist (Skills Wave canonical) | Held #7 with the gain up 28% — Anthropic's reference `.claude/skills` repo cleared 168k |
| #8&nbsp;(new) | [QM](https://github.com/yc-software/qm) | 13.2k | +1,756 | In scope · [profile](agents/qm.md) | First full window since being profiled: **+15% of its own size** (11.4k → 13.2k), straight onto the table |
| #9&nbsp;(↓) | [Codex CLI](https://github.com/openai/codex) | 105.4k | +1,382 | In scope · [profile](agents/codex.md) | Down three as the gain gave back last window's rebound (−28%) — cleared 105k |
| #10&nbsp;(↓) | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 66.0k | +1,337 | In scope · [profile](agents/codegraph.md) | Down two, gain off 14%, holding the last seat by 53 stars — the pre-indexed code knowledge graph cleared 66k |

- Heat is useful for discovery, not for selection by itself.
- **The curated-skills end re-accelerated violently, and it was one project doing it.** [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) went from +945 and off the table to **+4,664 and #2** — a 4.9× jump, the sharpest single-window re-acceleration this board has recorded. For the first time, the two largest curated `.claude/skills` directories hold the top two gain seats outright.
- **[mattpocock/skills](https://github.com/mattpocock/skills) takes an eighth straight #1** (214.3k, +10,291) — but this is its first deceleration in three windows (−8%). It still out-gains everything below #5 on this table combined, so read the dip as easing, not turning.
- **The frozen top six broke.** Last week #1–#6 were identical to the week before, a first for this board. This week four of those six moved: [Pi](agents/pi.md), [Superpowers](agents/superpowers.md) and [Hermes Agent](agents/hermes-agent.md) each slid a seat, and [Codex CLI](agents/codex.md) fell three. Note *why* — Pi and Superpowers posted essentially flat gains (both −2%). They were passed, not slowed.
- **[jcode](agents/jcode.md) reversed hard, and last week's read was too generous.** The "fastest riser by proportion" (+3,163) fell to **+1,284, a 59% drop**, and off the table entirely from #5. Two windows at 2–3k/week was the tail of a launch curve flattening, not a new baseline. The profile still stands; the trajectory call does not.
- **[TradingAgents](https://github.com/TauricResearch/TradingAgents) posts its biggest window ever and still is not in scope** (+2,050 to 97.7k, up 2.6× from +785). It enters at #6 because the table ranks gain, not fit — it remains a finance-research multi-agent framework, tracked but unprofiled. This is the clearest case yet for the line at the top of this section.
- **[QM](agents/qm.md)'s first full window backs the pickup**: +1,756 to 13.2k, roughly 15% of its own size, entering at #8 one week after being profiled. [Open Code Review](agents/open-code-review.md) (+1,246) and [Omnigent](agents/omnigent.md) (+507) post their first deltas just off the table.
- **[n8n](agents/n8n.md) crossed 200k and lost its seat in the same window** (200,311, +911, down from #10). Both facts are real: a milestone in absolute terms, and a gain that no longer clears a re-heated board.
- **New-inclusion decision: no new profile this window.** The scan surfaced nothing that clears the in-scope bar — the window's movement is all in projects already on the map. Joining the watchlist: [QwenLM/Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) (2.1k, Apache-2.0, opened 2026-07-29 — makes any agent harness multimodal-native, the freshest genuinely new angle) and [elder-plinius/T3MP3ST](https://github.com/elder-plinius/T3MP3ST) (5.5k, AGPL-3.0, a multi-agent offensive-security meta-harness — noted for the harness pattern, with the security vertical treated the same way as the finance one). Carried over and still growing: [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) (10.3k) and [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) (4.7k, +1.1k).

<details>
<summary>More window notes: skills-wave share, OpenClaw, and everything growing outside the top 10</summary>

- The `.claude/skills` wave **holds at four of the top ten** (`mattpocock/skills`, `addyosmani/agent-skills`, `Superpowers`, `anthropics/skills`), but the composition rotated again: [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) came back in, [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) dropped out. Two windows running, the count is stable while the members are not — the wave is rotating at its edge, not growing or shrinking. Policy unchanged: curated collections are tracked as Skills Wave entries, the framework end is covered through [Superpowers](agents/superpowers.md).
- Just off the table: [jcode](agents/jcode.md) 17.2k (+1,284), [Open Code Review](agents/open-code-review.md) 20.2k (+1,246) and [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 42.1k (+1,113) — the three of them inside 171 stars, all within reach of #10's +1,337.
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 386.0k stars (+0.8k); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.
- **First real deltas for last window's pickups**: [Open Code Review](agents/open-code-review.md) +1,246 (20.2k), [Omnigent](agents/omnigent.md) +507 (8.6k) and [Langfuse](agents/langfuse.md) +390 (32.9k) all now carry a comparable 7-day figure, alongside [QM](agents/qm.md) at #8. Four profiles added in two weeks, four of them growing — none needs a caveat next window.
- **[AutoGPT](agents/autogpt.md) woke up**: +724 to 186.5k, against +79 last window — a 9× jump off a very low base. One window is not a trend, but it is the largest proportional move outside the top ten and worth watching.
- **[Grok Build](agents/grok-build.md) keeps decelerating**: +552 to 24.7k, down 41% from its first comparable window (+940). Two windows of consistent decay past the launch spike, which is the expected shape.
- Continuing to grow but outside the top 10 by gain: [Claude Code](agents/claude-code.md) 141.1k (+0.8k), [AutoGPT](agents/autogpt.md) 186.5k (+0.7k), [Ruflo](agents/ruflo.md) 67.7k (+0.6k), [OpenHands](agents/openhands.md) 83.8k (+0.6k), [LangChain](agents/langchain.md) 144.1k (+0.6k), [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 33.3k (+0.6k), [LangGraph](agents/langgraph.md) 39.5k (+0.6k), [LiteLLM](agents/litellm.md) 56.2k (+0.6k), [Grok Build](agents/grok-build.md) 24.7k (+0.6k), [Omnigent](agents/omnigent.md) 8.6k (+0.5k), [Langfuse](agents/langfuse.md) 32.9k (+0.4k), [Goose](agents/goose.md) 52.7k (+0.4k), [Cline](agents/cline.md) 66.0k (+0.4k), [Open Interpreter](agents/open-interpreter.md) 68.0k (+0.4k), [Kimi Code](agents/kimi-code.md) 6.4k (+0.4k), [agentmemory](https://github.com/rohitg00/agentmemory) 26.9k (+0.3k), [CrewAI](agents/crewai.md) 57.0k (+0.3k), [CLI-Anything](agents/cli-anything.md) 46.9k (+0.3k), [MiMoCode](agents/mimocode.md) 12.7k (+67), [CoStrict](agents/costrict.md) 4.4k (+12, flat).

</details>

### Ranking Trend

How the weekly top 10 has shifted since tracking began — each line is one project, breaks mean it fell off the board that week:

<p align="center">
  <img src="assets/heat-trend-en.svg" alt="Weekly heat ranking trend (bump chart)" width="100%" />
</p>

And the same windows read as seats per layer — the quantitative version of the skills-wave story the bullets tell in prose:

<p align="center">
  <img src="assets/heat-composition-en.svg" alt="Weekly top-10 composition by layer (stacked bars)" width="100%" />
</p>

Full stock rankings by category — agents, agent infra, skills, and their verticals, sorted by total stars — live in [rankings/](rankings/README.md).

## Beyond The Rank

Popularity tells you what to look at. These four pages tell you what to pick:

- **[Capability matrix](capabilities/matrix.md)** — every project scored side by side (●/◐/○/—) across the nine shared [capability dimensions](capabilities/README.md), grouped by route. The answer to "for this capability, who treats it as a core strength."
- **[Cost & benchmarks](comparisons/cost-and-benchmarks.md)** — frontier-model capability vs per-token price, plus how each coding agent actually bills. Since the model layer went tiered and metered, "which tier for this task" is the selection decision.
- **[Memory approaches](comparisons/memory-approaches.md)** — six different things projects mean by "has memory," from self-editing stores to passive semantic recall, and which to pick for what you need to persist.
- **[Observability & evaluation](comparisons/observability-and-evals.md)** — the layer under everything above: once an agent runs unattended, failure stops looking like a crash and starts looking like silent quality drift. Compares [Langfuse](agents/langfuse.md), Opik, Phoenix, Helicone, LangSmith and others — and untangles the four different things "open source" means in that field.

## Market Pulse

The three structural stories shaping selection right now — full records with dates and sources live in [market-events.md](market-events.md):

- **The `.claude/skills` wave keeps compounding — and is now concentrating** (May 2026 → ongoing): curated skill collections and skills frameworks have held roughly half of the weekly heat top 10 for three months, but through August the count has stopped moving while the membership rotates, and the gain increasingly accrues to the two largest personal directories. For many tasks the skill layer now matters as much as the underlying agent; read the concentration as key-person risk, not a broadening ecosystem. This map profiles the framework end through [Superpowers](agents/superpowers.md) and tracks collections on the [skill boards](rankings/skill-verticals.md).
- **The model layer became a budget decision**: Anthropic's Mythos-class [Claude Fable 5](agents/claude-fable-5.md) (June 9) sits above Opus 4.8 on metered credits, while OpenAI's GPT-5.6 (July 9) ships in three price tiers — on both sides, "which tier of intelligence for this task" is now part of agent selection. Spring reference point: [GPT-5.5](agents/gpt-5.5.md).
- **Product boundaries are collapsing upward**: OpenAI merged Codex into the ChatGPT app (July 9) — on the OpenAI side, "which coding agent" is turning into "how you use ChatGPT." See [Codex](agents/codex.md).

## The First Cut Of The Map

<p align="center">
  <img src="assets/route-map-en.svg" alt="The AI Agent Map — 13 routes grouped into four decisions" width="100%" />
</p>

| Route | Representative projects | Typical user |
| --- | --- | --- |
| Direct execution | [Claude Code](agents/claude-code.md), [Aider](agents/aider.md), [Codex](agents/codex.md), [Kimi Code](agents/kimi-code.md), [MiMoCode](agents/mimocode.md), [CodeWhale](agents/codewhale.md), [Grok Build](agents/grok-build.md), [Devin](agents/devin.md), [Jules](agents/jules.md) | Someone who wants to hand a concrete coding task to an agent (see the [terminal coding CLI comparison](comparisons/coding-cli-agents.md)) |
| Agent harness framework | [Pi](agents/pi.md), [jcode](agents/jcode.md), [OpenHands](agents/openhands.md), [SWE-agent](agents/swe-agent.md), [mini-swe-agent](agents/mini-swe-agent.md), [OpenHarness](agents/openharness.md), [QM](agents/qm.md), [Omnigent](agents/omnigent.md) | Someone who wants to own the agent loop, tool surface, and permissions instead of inheriting a vendor's product — QM and Omnigent extend this to running *several* harnesses under one layer (see the [harness comparison](comparisons/agent-harness-frameworks.md)) |
| Frontier agentic model | [Claude Fable 5](agents/claude-fable-5.md), [GPT-5.5](agents/gpt-5.5.md) | Someone choosing which model to wire into their own agent system or evaluating the capability ceiling of Anthropic / OpenAI surfaces |
| Agentic skills framework | [Superpowers](agents/superpowers.md) | Someone who wants a methodology + composable skills layer that plugs into Claude Code, Codex, Cursor, and similar agents |
| Workflow / orchestration layer | [oh-my-claudecode](agents/oh-my-claudecode.md), [oh-my-codex](agents/oh-my-codex.md), [Ruflo](agents/ruflo.md) | Someone who already likes Claude Code or Codex and wants stronger orchestration on top (Ruflo extends this to multi-machine federation and 100+ specialized agents) |
| Editor-centric AI workflow | [Cursor](agents/cursor.md), [Windsurf](agents/windsurf.md), [Continue](agents/continue.md) | Someone who wants the editor itself to stay central |
| Review-first automation | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md), [CoStrict](agents/costrict.md), [Open Code Review](agents/open-code-review.md) | Someone who wants review and human control to stay central (CoStrict adds enterprise strict-workflow + private deployment; Open Code Review is review only, tuned for precision in CI) |
| Managed background path | [Claude Managed Agents](agents/claude-managed-agents.md) | Someone who needs scheduled, cloud, or detached Anthropic workflows |
| General-purpose autonomous agent | [AutoGPT](agents/autogpt.md), [Agent Zero](agents/agent-zero.md), [BabyAGI](agents/babyagi.md), [Julep](agents/julep.md), [GenericAgent](agents/generic-agent.md), [ml-intern](agents/ml-intern.md) | Someone who wants autonomous, general-purpose task execution (or, in ml-intern's case, autonomous ML engineering) |
| Build-your-own system | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md), [Haystack](agents/haystack.md), [Semantic Kernel](agents/semantic-kernel.md), [DSPy](agents/dspy.md), [Pydantic AI](agents/pydantic-ai.md) | Teams building their own agent platform instead of buying one |
| Runtime and tools | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [CLI-Anything](agents/cli-anything.md) | Teams that need workflow automation, code execution, LLM gateways, agent context infrastructure, agent-driven CLIs, or visual builders |
| Observability and evals | [Langfuse](agents/langfuse.md) | Someone whose agents already run in production and needs to know what they did, what they cost, and whether quality is drifting (see [observability & evaluation](comparisons/observability-and-evals.md)) |
| Self-hosted / local runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md), [OpenHuman](agents/openhuman.md) | Users who need on-device privacy, long-running agents, local control, channels, devices, or personal-data life integration |

## Current Mainstream Coverage

60 profiled projects, grouped by what they are. Expand a group, or browse the full route/coverage tables in [agents/](agents/README.md).

<details>
<summary><strong>Coding agents, editors, and orchestration</strong> (27 projects)</summary>

| Project | Route | One-line positioning |
| --- | --- | --- |
| [Aider](agents/aider.md) | Direct execution | Terminal-first AI pair programmer close to git |
| [Claude Code](agents/claude-code.md) | Direct execution | Local and IDE-first coding agent |
| [Claude Managed Agents](agents/claude-managed-agents.md) | Managed background path | Anthropic managed / cloud execution mapping |
| [Codex](agents/codex.md) | Direct execution | Coding agent inside the ChatGPT app, with async cloud delegation |
| [oh-my-claudecode](agents/oh-my-claudecode.md) | Workflow layer | Teams-first orchestration layer on top of Claude Code |
| [oh-my-codex](agents/oh-my-codex.md) | Workflow layer | Stronger workflow, teams, and persistent state around Codex CLI |
| [Cursor](agents/cursor.md) | Editor-centric platform | AI editor spanning local coding, cloud agents, and integrations |
| [GitHub Copilot](agents/github-copilot.md) | Platform | Multi-surface agent platform across VS Code and GitHub |
| [Cline](agents/cline.md) | Review-first execution | Approval-first editor-native coding agent |
| [Windsurf](agents/windsurf.md) | AI-native IDE | Cascade-centered AI IDE |
| [OpenHands](agents/openhands.md) | Open-source execution | Open-source software engineering agent |
| [Devin](agents/devin.md) | Managed execution | End-to-end managed software engineering execution |
| [Jules](agents/jules.md) | Managed cloud execution | GitHub-connected coding delegation with PR handoff |
| [Continue](agents/continue.md) | Editor-centric | Open-source IDE extension with full model freedom |
| [Froge Code](agents/froge-code.md) | Review-first automation | Provisionally mapped to Automagik Genie |
| [Pi](agents/pi.md) | Direct execution | Minimal terminal coding-agent harness with multi-provider LLM support |
| [jcode](agents/jcode.md) | Agent harness framework | Rust multi-session coding harness — fastest boot, provider-neutral OAuth, passive semantic memory |
| [CodeWhale](agents/codewhale.md) | Direct execution | DeepSeek + MiMo terminal coding agent (formerly DeepSeek-TUI) |
| [Kimi Code](agents/kimi-code.md) | Direct execution | Moonshot AI's official Kimi-native terminal coding CLI (successor to kimi-cli) |
| [MiMoCode](agents/mimocode.md) | Direct execution | Xiaomi's official MiMo terminal coding agent with built-in cross-session memory |
| [Grok Build](agents/grok-build.md) | Direct execution | SpaceXAI's official Rust terminal coding agent — full-screen TUI, headless CI mode, ACP editor server |
| [CoStrict](agents/costrict.md) | Review-first automation | Enterprise Cline-lineage coding agent with strict standardized workflow, AI code review, and private deployment |
| [SWE-agent](agents/swe-agent.md) | Agent harness framework | Princeton + Stanford's original SWE-bench harness with single-YAML configuration |
| [mini-swe-agent](agents/mini-swe-agent.md) | Agent harness framework | The ~100-line Python successor to SWE-agent that still scores >74% on SWE-bench Verified |
| [OpenHarness](agents/openharness.md) | Agent harness framework | HKUDS's 10-subsystem open agent harness with 43+ tools, anthropics/skills, and MCP |
| [Omnigent](agents/omnigent.md) | Agent harness framework | Meta-harness that mixes Claude Code, Codex, Cursor, OpenCode, Hermes, and Pi in one session, with policies and cloud sandboxes |
| [Open Code Review](agents/open-code-review.md) | Review-first automation | Alibaba's precision-first code-review CLI — deterministic pipeline around the model, plus CI and agent-plugin surfaces |

</details>

<details>
<summary><strong>Autonomous and self-hosted agents</strong> (14 projects)</summary>

| Project | Route | One-line positioning |
| --- | --- | --- |
| [AI Edge Gallery](agents/ai-edge-gallery.md) | On-device local runtime | Mobile-first local assistant sandbox with agent skills |
| [Goose](agents/goose.md) | Open-source local platform | Extensible local agent across desktop, CLI, and API |
| [Hermes Agent](agents/hermes-agent.md) | Multi-agent / self-hosted | Long-lived self-hosted environment with memory and skills |
| [OpenClaw](agents/openclaw.md) | Runtime | Local-first multi-channel runtime layer |
| [AutoGPT](agents/autogpt.md) | Autonomous agent platform | Visual agent builder with workflows, marketplace, and multi-model support |
| [Agent Zero](agents/agent-zero.md) | Autonomous agent | Self-building autonomous agent with dynamic tool creation |
| [BabyAGI](agents/babyagi.md) | Experimental | Pioneering autonomous agent experiment — educational, not production |
| [Open Interpreter](agents/open-interpreter.md) | Runtime | Natural language to local code execution, no sandbox |
| [Mercury Agent](agents/mercury-agent.md) | Self-hosted multi-channel | Permission-hardened agent for CLI and Telegram with token budgets |
| [ml-intern](agents/ml-intern.md) | Domain-specific autonomous agent | Hugging Face's autonomous ML engineer — research, code, and ship ML using HF tooling |
| [GenericAgent](agents/generic-agent.md) | Self-evolving autonomous agent | Small-seed agent that grows a personal skill tree on every task |
| [OpenHuman](agents/openhuman.md) | Self-hosted / local runtime | Desktop life-integration agent with 118+ connectors, local Memory Tree, and Ollama support |
| [Julep](agents/julep.md) | Workflow engine | Temporal-backed durable workflow engine for stateful AI agents |
| [QM](agents/qm.md) | Agent harness framework | Y Combinator's multiplayer agent for Slack and web — per-person and per-room scopes, self-hosted, harness-agnostic |

</details>

<details>
<summary><strong>Frameworks and infrastructure</strong> (16 projects)</summary>

| Project | Route | One-line positioning |
| --- | --- | --- |
| [LangChain](agents/langchain.md) | Platform | High-level framework for building custom agents quickly |
| [LangGraph](agents/langgraph.md) | Platform | Low-level framework for durable stateful workflows |
| [CrewAI](agents/crewai.md) | Multi-agent framework | Role-based agent collaboration with fast prototyping |
| [LlamaIndex](agents/llamaindex.md) | Data-first framework | RAG and agentic applications over documents and data |
| [n8n](agents/n8n.md) | Workflow automation | Visual workflow platform with native AI agent nodes and 400+ integrations |
| [MemGPT](agents/memgpt.md) | Stateful agent platform | Persistent memory agents that learn across sessions (now Letta) |
| [Haystack](agents/haystack.md) | Framework | Production-oriented RAG and agent framework by deepset |
| [Semantic Kernel](agents/semantic-kernel.md) | Framework | Microsoft's AI orchestration SDK for .NET, Python, and Java |
| [DSPy](agents/dspy.md) | Framework | Programmatic prompt optimization — programming, not prompting, LMs |
| [LiteLLM](agents/litellm.md) | Infrastructure | Unified API gateway for 100+ LLM providers |
| [Langfuse](agents/langfuse.md) | Infrastructure | Open-source agent observability, evals, and prompt management (watches agents, does not run them) |
| [Pydantic AI](agents/pydantic-ai.md) | Framework | Type-safe Python agent framework with structured outputs |
| [Flowise](agents/flowise.md) | Visual builder | Drag-and-drop LLM app and agent builder on top of LangChain |
| [Ruflo](agents/ruflo.md) | Workflow / orchestration layer | Multi-agent orchestration platform for Claude with federation across machines, neural memory, and 100+ specialized agents |
| [CodeGraph](agents/codegraph.md) | Runtime and tools | Pre-indexed code knowledge graph + MCP server for Claude Code, Cursor, Codex CLI, opencode, and Hermes Agent |
| [CLI-Anything](agents/cli-anything.md) | Runtime and tools | Auto-generates Click-based CLIs for arbitrary software so agents can drive non-API apps |

</details>

<details>
<summary><strong>Models and skills</strong> (3 entries)</summary>

| Project | Route | One-line positioning |
| --- | --- | --- |
| [Claude Fable 5](agents/claude-fable-5.md) | Frontier agentic model | Anthropic's Mythos-class frontier model — the capability ceiling above Opus for Claude-based agents |
| [GPT-5.5](agents/gpt-5.5.md) | Frontier agentic model | OpenAI's spring 2026 agentic model (succeeded by GPT-5.6 in July) |
| [Superpowers](agents/superpowers.md) | Agentic skills framework | Methodology and composable skills layer that plugs into Claude Code, Codex, Cursor, and other agents |

</details>

## Example Reading Paths

If you are still deciding where to begin, use one of these quick routes and then branch out.

| If you sound like this... | Follow this path | What it helps you answer |
| --- | --- | --- |
| I want a day-to-day coding agent and need to choose terminal vs editor | [Aider](agents/aider.md) → [Claude Code](agents/claude-code.md) → [terminal coding CLI comparison](comparisons/coding-cli-agents.md) → [Cursor](agents/cursor.md) → [Cline](agents/cline.md) → [coding automation guide](use-cases/coding-automation.md) | Which vendor CLI fits your model, terminal-first local loop vs editor-led flow vs approval-first control |
| I already like Claude Code or Codex but want stronger orchestration | [Claude Code](agents/claude-code.md) → [oh-my-claudecode](agents/oh-my-claudecode.md) → [Codex](agents/codex.md) → [oh-my-codex](agents/oh-my-codex.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | When the base agent is enough and when a workflow layer actually adds value |
| I want to understand how the 2026 model race changes agent choice | [Claude Fable 5](agents/claude-fable-5.md) → [GPT-5.5](agents/gpt-5.5.md) → [Codex](agents/codex.md) → [Claude Code](agents/claude-code.md) → [market events](market-events.md) | How frontier model tiers (Mythos, GPT-5.6) shift the capability ceiling and what it means for product choice |
| I want a dedicated AI IDE instead of stitching tools together | [Cursor](agents/cursor.md) → [Windsurf](agents/windsurf.md) → [GitHub Copilot](agents/github-copilot.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Dedicated AI editor vs ecosystem platform |
| I want to hand off tickets and check back later | [Codex](agents/codex.md) → [Jules](agents/jules.md) → [Devin](agents/devin.md) → [Claude Managed Agents](agents/claude-managed-agents.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Async cloud delegation vs managed background automation |
| I need something open-source or self-hosted | [Aider](agents/aider.md) → [OpenHands](agents/openhands.md) → [Goose](agents/goose.md) → [Hermes Agent](agents/hermes-agent.md) → [capabilities](capabilities/README.md) | Terminal control, open-source execution, and local runtime ownership |
| I am building an internal agent stack, not buying a product | [LangChain](agents/langchain.md) → [LangGraph](agents/langgraph.md) → [capabilities](capabilities/README.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Framework vs runtime vs product boundaries |

## Disclaimer

Star counts and 7-day gains are point-in-time GitHub snapshots taken when the repo is updated; numbers shift quickly between weekly refreshes and small rounding differences are expected. Project descriptions, vendors, and capability summaries reflect public information at the time of writing and may change as projects evolve, get acquired, or pivot. This map is selection guidance — not endorsement, financial advice, or a production-readiness guarantee. Verify against each project's own docs before committing to a choice.