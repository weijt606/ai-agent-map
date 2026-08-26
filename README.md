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

> **Last updated:** 2026-08-27 · **Snapshot window:** 2026-08-12 → 2026-08-27 (gain since last update, **15 days** — two scheduled Wednesday refreshes were missed, so this is a catch-up window; approximate) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(=) | [mattpocock/skills](https://github.com/mattpocock/skills) | 237.9k | +23,585 | Watchlist (Skills Wave) | A tenth straight window at #1, past **237k** — at ~11.0k/week it is still accelerating (+7% on the weekly rate) and out-gains #2 by 1.8× |
| #2&nbsp;(↑) | [Codex CLI](https://github.com/openai/codex) | 118.8k | +13,321 | In scope · [profile](agents/codex.md) | Up seven on a **4.5× jump in weekly rate** — the largest re-acceleration this board has recorded, against OpenAI's Aug 21 Sol price cut and a 20M-user announcement; cleared 118k |
| #3&nbsp;(=) | [Pi](https://github.com/earendil-works/pi) | 97.8k | +9,677 | In scope · [profile](agents/pi.md) | Held #3 with the weekly rate up 8% (~4.5k/week) — closing on **100k** without a single loud week |
| #4&nbsp;(↑) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 236.9k | +7,632 | In scope · [profile](agents/hermes-agent.md) | Up one on a flat weekly rate (+2%) — still the in-scope absolute leader, past 236k |
| #5&nbsp;(↓) | [Superpowers](https://github.com/obra/superpowers) | 278.1k | +7,140 | In scope · [profile](agents/superpowers.md) | Down one as the weekly rate cooled 18% — cleared 278k, still the wave's framework anchor |
| #6&nbsp;(↓) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 90.0k | +3,638 | Watchlist (Skills Wave) | Last window's 4.9× spike gave back **64% of its weekly rate** — cleared 90k, but the #2 seat lasted exactly one window |
| #7&nbsp;(=) | [anthropics/skills](https://github.com/anthropics/skills) | 171.8k | +3,449 | Watchlist (Skills Wave canonical) | Held #7 with the weekly rate off 19% — Anthropic's reference `.claude/skills` repo cleared 171k |
| #8&nbsp;(↓) | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 100.7k | +3,018 | Out of scope (finance-research vertical) | **Crossed 100k** and slipped two as the rate cooled 31% — tracked, still not an in-scope agent surface |
| #9&nbsp;(↑) | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 68.3k | +2,247 | In scope · [profile](agents/codegraph.md) | Up one despite a 22% cooler rate — the pre-indexed code knowledge graph cleared 68k |
| #10&nbsp;(new) | [n8n](https://github.com/n8n-io/n8n) | 202.5k | +2,214 | In scope · [profile](agents/n8n.md) | Back on the table one window after losing its seat, weekly rate up 13% — past 202k |

- Heat is useful for discovery, not for selection by itself.
- **Two refreshes were missed, so read every number here as 15 days, not 7.** The Wednesday updates for 2026-08-19 and 2026-08-26 did not run; this window spans 2026-08-12 → 2026-08-27. Raw gains are therefore roughly 2.1× a normal window and are **not** comparable to last week's column. Every "up"/"cooled" claim below is stated on the **weekly rate** (gain ÷ 15 × 7), which is comparable; the table's own numbers are the raw 15-day gains.
- **[Codex CLI](agents/codex.md) is the story, and it is a vendor story.** It went from #9 to **#2** on +13,321 — a weekly rate of ~6.2k against ~1.4k last window, a **4.5× re-acceleration** and the largest this board has recorded. It sits on two dated events inside the window: OpenAI **cut GPT-5.6 Sol from $5/$30 to $4/$20 per M tokens on Aug 21** for three months, applying to Codex credits as well as the API, and reported **20M active Codex users** the same day. This is the first time the heat board's top mover is explained by a price change rather than a launch.
- **[mattpocock/skills](https://github.com/mattpocock/skills) takes a tenth straight #1 and re-accelerates** (237.9k, +23,585, ~11.0k/week against 10,291). The single deceleration flagged last window did not continue. It still out-gains everything below #4 on this table combined.
- **Last window's read on [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) was a spike, not a re-acceleration.** The "sharpest single-window re-acceleration this board has recorded" gave back **64% of its weekly rate** (4,664 → ~1,698/week) and fell from #2 to #6. Two windows running, this board has now over-read a one-window jump — [jcode](agents/jcode.md) in August, addyosmani here. The pattern is worth stating as a rule: a single 4–5× window is a spike until a second window confirms it.
- **[TradingAgents](https://github.com/TauricResearch/TradingAgents) crossed 100k and is still not in scope** (100,735). It has now been on this table four windows running purely on gain. The line at the top of this section does the work: this table ranks heat, not fit.
- **The middle of the board is one broad cool-down.** Six of the top ten posted a lower weekly rate than last window, and outside the top ten the pattern is sharper: [QM](agents/qm.md) gave back 71% of its rate (1,756 → ~501/week, off the table from #8), [Open Code Review](agents/open-code-review.md) 53%, [jcode](agents/jcode.md) another 50%, [AutoGPT](agents/autogpt.md) 77% — last window's "9× wake-up" was noise. Against that, [Pi](agents/pi.md), [n8n](agents/n8n.md), [Claude Code](agents/claude-code.md) and [Grok Build](agents/grok-build.md) all improved.
- **[n8n](agents/n8n.md) is back one window after losing its seat**, and [OpenHuman](agents/openhuman.md) (+1,955, 38.2k) missed the table by 259 stars — its best showing since being profiled.
- **New-inclusion decision: one profile added — [eve](agents/eve.md)** (`vercel/eve`, Apache-2.0, 4.8k). A backfill rather than a breakout: Vercel shipped it at Ship London on **June 17 2026** as part of its Agent Stack, and this map missed it. It belongs on the build-your-own route and it changes that route's shape — an agent is a *directory of files*, and durable execution, per-agent sandboxes, `needsApproval` gates, subagents, evals, and eight-plus channel adapters ship inside the framework. It is the first entry on that route with real delivery surfaces, and the only one whose documented production path runs through one vendor's platform. Also scanned and held on the watchlist: [truefoundry/trueforge](https://github.com/truefoundry/trueforge) (4.6k, MIT, "the runtime layer that turns an LLM into a working agent"), [trailhq/Graft](https://github.com/trailhq/Graft) (4.9k, MIT, a shared code-graph context layer under Claude Code / Cursor / Codex / Gemini) and [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi) (2.1k in three weeks, but no clear license — `NOASSERTION`, which is a hard blocker for a profile here). Carried over and still growing: [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) (6.4k), [QwenLM/Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) (2.8k).

<details>
<summary>More window notes: skills-wave share, OpenClaw, and everything growing outside the top 10</summary>

- The `.claude/skills` wave **holds at four of the top ten** for a third straight window (`mattpocock/skills`, `addyosmani/agent-skills`, `Superpowers`, `anthropics/skills`) — and this time the membership did not rotate either. What moved is the internal split: [mattpocock/skills](https://github.com/mattpocock/skills) now accounts for **more than the other three combined**, where a month ago it was roughly level with them. The wave is not broadening; it is concentrating into one directory. Policy unchanged: curated collections are tracked as Skills Wave entries, the framework end is covered through [Superpowers](agents/superpowers.md).
- Just off the table: [OpenHuman](agents/openhuman.md) 38.2k (+1,955, its best window since being profiled, missing #10 by 259 stars), [Claude Code](agents/claude-code.md) 143.1k (+1,952) and [Ruflo](agents/ruflo.md) 69.5k (+1,788).
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 387.7k stars (+1.7k); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.
- **Last window's four pickups have now all posted a second delta, and three of the four decelerated hard**: [QM](agents/qm.md) −71% on the weekly rate (14.2k), [Open Code Review](agents/open-code-review.md) −53% (21.5k), [Omnigent](agents/omnigent.md) −39% (9.3k). Only [Langfuse](agents/langfuse.md) held flat (−1%, 33.8k). None of the four is shrinking, but the "four profiles added, four of them growing" framing from last window overstated a launch bump — the honest read is that a first full window after a pickup is almost always the peak.
- **[AutoGPT](agents/autogpt.md)'s wake-up was noise.** Last window's 9× jump (+724) fell to a weekly rate of ~167 (+357 over 15 days, −77%) — back to the low base it came from. Flagged here because the map called it "worth watching" and it was not.
- **[Grok Build](agents/grok-build.md) stopped decelerating**: +1,372 to 26.1k, a weekly rate of ~640 against 552 — the first uptick after two windows of post-launch decay.
- Continuing to grow but outside the top 10 by gain (15-day figures): [Claude Code](agents/claude-code.md) 143.1k (+2.0k), [OpenHuman](agents/openhuman.md) 38.2k (+2.0k), [Ruflo](agents/ruflo.md) 69.5k (+1.8k), [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 43.8k (+1.8k), [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 34.7k (+1.4k), [OpenHands](agents/openhands.md) 85.2k (+1.4k), [jcode](agents/jcode.md) 18.6k (+1.4k), [CLI-Anything](agents/cli-anything.md) 48.3k (+1.4k), [Grok Build](agents/grok-build.md) 26.1k (+1.4k), [Open Code Review](agents/open-code-review.md) 21.5k (+1.3k), [LiteLLM](agents/litellm.md) 57.3k (+1.2k), [QM](agents/qm.md) 14.2k (+1.1k), [LangChain](agents/langchain.md) 145.1k (+1.0k), [LangGraph](agents/langgraph.md) 40.5k (+1.0k), [Cline](agents/cline.md) 66.9k (+0.9k), [Langfuse](agents/langfuse.md) 33.8k (+0.8k), [Goose](agents/goose.md) 53.5k (+0.8k), [Kimi Code](agents/kimi-code.md) 7.1k (+0.7k), [CrewAI](agents/crewai.md) 57.6k (+0.7k), [Omnigent](agents/omnigent.md) 9.3k (+0.7k), [agentmemory](https://github.com/rohitg00/agentmemory) 27.5k (+0.6k), [mini-swe-agent](agents/mini-swe-agent.md) 6.8k (+0.4k), [Aider](agents/aider.md) 48.5k (+0.4k), [AutoGPT](agents/autogpt.md) 186.9k (+0.4k), [LlamaIndex](agents/llamaindex.md) 51.9k (+0.3k), [Letta (MemGPT)](agents/memgpt.md) 24.5k (+0.2k), [OpenHarness](agents/openharness.md) 15.5k (+0.2k), [Continue](agents/continue.md) 35.6k (+0.2k), [Open Interpreter](agents/open-interpreter.md) 68.2k (+0.2k), [CodeWhale](agents/codewhale.md) 40.9k (+0.2k), [MiMoCode](agents/mimocode.md) 12.9k (+0.2k), [SWE-agent](agents/swe-agent.md) 20.1k (+100), [Flowise](agents/flowise.md) 55.4k (+58), [CoStrict](agents/costrict.md) 4.4k (+30, near-flat).

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

- **The `.claude/skills` wave keeps compounding — and is now concentrating into one directory** (May 2026 → ongoing): curated skill collections and skills frameworks have held roughly half of the weekly heat top 10 for three months, and through August the count stopped moving entirely — four of ten, three windows running, with no rotation in the last one. What is still moving is the split inside the wave: [mattpocock/skills](https://github.com/mattpocock/skills) now out-gains the other three combined, where a month ago it was level with them. For many tasks the skill layer now matters as much as the underlying agent; read the concentration as key-person risk, not a broadening ecosystem. This map profiles the framework end through [Superpowers](agents/superpowers.md) and tracks collections on the [skill boards](rankings/skill-verticals.md).
- **The model layer became a budget decision, and the budget now moves**: Anthropic's Mythos-class [Claude Fable 5](agents/claude-fable-5.md) (June 9) sits above Opus 4.8 on metered credits, while OpenAI's GPT-5.6 (July 9) ships in three price tiers. As of **August 21** the top tier is also *promotional* — Sol cut to $4 / $20 for three months, covering Codex credits — which put the index leader below Opus 4.8 on output price and made [cost & benchmarks](comparisons/cost-and-benchmarks.md) a document with a review date on it. Spring reference point: [GPT-5.5](agents/gpt-5.5.md).
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

61 profiled projects, grouped by what they are. Expand a group, or browse the full route/coverage tables in [agents/](agents/README.md).

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
<summary><strong>Frameworks and infrastructure</strong> (17 projects)</summary>

| Project | Route | One-line positioning |
| --- | --- | --- |
| [eve](agents/eve.md) | Build-your-own platform | Vercel's filesystem-first agent framework — durable execution, sandboxes, approvals, channels, evals |
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