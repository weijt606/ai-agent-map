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

> **Last updated:** 2026-09-01 · **Snapshot window:** 2026-08-27 → 2026-09-01 (gain since last update, **5 days** — the previous refresh was a late catch-up run on Aug 27, so this window closes short; approximate) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(new) | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 41.5k | +6,750 | Watchlist (Skills Wave · research vertical) | Enters at #1 straight from off the table on a **14× jump in weekly rate** (~9,450/week against ~670) — the largest re-acceleration this board has recorded, and the first #1 that is a *domain* collection rather than a general one |
| #2&nbsp;(↓) | [mattpocock/skills](https://github.com/mattpocock/skills) | 243.9k | +5,954 | Watchlist (Skills Wave) | **The nine-window #1 streak ends** (2026-06-24 → 2026-08-27; the previous edition said ten, which was one too many). It still out-gains every other general-purpose collection combined, but the rate is off 24% and it was plainly out-gained here, not edged out — past **243k** |
| #3&nbsp;(=) | [Pi](https://github.com/earendil-works/pi) | 100.5k | +2,707 | In scope · [profile](agents/pi.md) | **Crossed 100k**, which the last two windows had it closing on — held #3 on a rate 16% cooler (~3,790/week) |
| #4&nbsp;(=) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 239.5k | +2,595 | In scope · [profile](agents/hermes-agent.md) | Flat a second window running (+2% on the rate) — the in-scope absolute leader is now ~530 stars short of **240k** |
| #5&nbsp;(=) | [Superpowers](https://github.com/obra/superpowers) | 280.4k | +2,308 | In scope · [profile](agents/superpowers.md) | **Cleared 280k** on an essentially flat rate (−3%) — the steadiest line on this board, and the wave's framework anchor |
| #6&nbsp;(↓) | [Codex CLI](https://github.com/openai/codex) | 120.7k | +1,915 | In scope · [profile](agents/codex.md) | Gave back **57% of its weekly rate** (~6,216 → ~2,681) and fell four. Last window's price-cut surge was a spike, not a new baseline — cleared 120k |
| #7&nbsp;(↑) | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 102.2k | +1,455 | Out of scope (finance-research vertical) | Up one on a rate 45% hotter — a third consecutive window and an eleventh appearance overall, purely on gain, still not an in-scope agent surface |
| #8&nbsp;(↓) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 91.4k | +1,418 | Watchlist (Skills Wave) | Down two on rank but the rate is **up 17%** — the floor after August's spike is settling above where the spike began; cleared 91k |
| #9&nbsp;(↓) | [anthropics/skills](https://github.com/anthropics/skills) | 173.0k | +1,173 | Watchlist (Skills Wave canonical) | Flat a second window (+2%) — Anthropic's reference `.claude/skills` repo finished the window **ten stars short of 173k** (172,990) |
| #10&nbsp;(new) | [OpenHuman](https://github.com/tinyhumansai/openhuman) | 39.3k | +1,111 | In scope · [profile](agents/openhuman.md) | Takes the seat it missed by 259 stars last window, on a rate **70% hotter** — its first appearance on this table since being profiled |

- Heat is useful for discovery, not for selection by itself.
- **This window is 5 days, not 7.** The previous refresh was a late catch-up run on 2026-08-27, so this one spans 2026-08-27 → 2026-09-01. Raw gains here are therefore ~0.71× a normal window and are **not** comparable to last window's 15-day column. Every "up"/"cooled"/"×" claim below is stated on the **weekly rate** (gain ÷ 5 × 7) against last window's weekly rate (gain ÷ 15 × 7); the table shows the raw 5-day gains.
- **The science vertical is the story, at both ends of the stack.** [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) — 165 validated skills and 100+ scientific databases across biology, chemistry, medicine, and drug discovery — went from off the table to **#1** on ~9,450/week against ~670, a **14×** jump. It did not move alone: [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) is **#11** on a rate up 67%. Inside the same window, Anthropic previewed the **[Model Hardware Standard](market-events.md)** (Aug 27), an open interface for agents driving microscopes, liquid handlers, robotic arms, and lasers — built with HHMI, with QuEra using it for laser coordination on a quantum computer. The map is stating the coincidence, not a cause: neither repo cites MHS, and K-Dense also shipped its own free desktop co-scientist (**K-Dense BYOK**, MIT) in the days before the window. What is not in doubt is where the heat went.
- **Apply this map's own rule to its own #1: one window is a spike until a second confirms it.** The board wrote that rule last window after over-reading [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) and [jcode](agents/jcode.md). A 14× window is the largest test it has faced. It is reported at #1 because that is where the gain puts it, and it is **not** yet read as a trend.
- **The rule immediately paid out on [Codex CLI](agents/codex.md).** Last window's "largest re-acceleration this board has recorded" — 4.5×, #9 to #2, on OpenAI's Aug 21 Sol price cut — gave back **57% of its weekly rate** and fell to #6. A price cut moved one window's stars; it did not move the baseline. That is now three spikes in three windows (jcode, addyosmani, Codex) that did not survive the next one.
- **[mattpocock/skills](https://github.com/mattpocock/skills)'s run at #1 is over after nine consecutive windows** (2026-06-24 → 2026-08-27; 243.9k, +5,954, ~8,336/week against 11,006). Correction to the previous edition, which called 2026-08-27 a *tenth* straight window — the recorded count is nine, and the 15-day catch-up window appears to have been counted twice. It was out-gained by a clear margin rather than edged out, and its own rate fell 24% — both halves matter, because the concentration story this map has been telling depends on the second one continuing.
- **[Pi](agents/pi.md) crossed 100k** (100,474), the milestone the last two windows had it approaching, without a single loud week in the run-up. [Superpowers](agents/superpowers.md) cleared **280k** and [Codex CLI](agents/codex.md) **120k** in the same window.
- **The `.claude/skills` wave went from 4 of the top ten to 5 — the first time it has held five since 2026-07-14.** For the previous two windows it held four seats, all general-purpose collections, with no rotation. Be precise about what is new here, because the obvious reading is wrong: a **research-vertical** collection is not new on this board — [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) held a top-ten seat in nine earlier windows, most recently 2026-08-05, and [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) itself sat at #8 back in May. What has never happened before is a domain collection at **#1**, with a second one directly behind it at #11. The wave did not just discover verticals; a vertical took the lead.
- **The board re-accelerated broadly**, reversing last window's cool-down: **27 of 47** tracked repos posted a higher weekly rate. Biggest movers up outside the top ten: [agentmemory](https://github.com/rohitg00/agentmemory) +81% (27.9k), [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) +67% (44.8k), [12-factor-agents](https://github.com/humanlayer/12-factor-agents) +49% (25.6k), [OpenHands](agents/openhands.md) +44% (85.9k), [OpenClaw](agents/openclaw.md) +40%, [CrewAI](agents/crewai.md) +39%. Down hardest: [Flowise](agents/flowise.md) −74%, [CodeWhale](agents/codewhale.md) −60%, [Grok Build](agents/grok-build.md) −49%, [Kimi Code](agents/kimi-code.md) −49%, [QM](agents/qm.md) −47% for a second straight window.
- **New-inclusion decision: one profile added — [TrueForge](agents/trueforge.md)** (`truefoundry/trueforge`, MIT, TypeScript, 5.0k, 348 forks). It has now grown steadily across two windows on the watchlist, which is the bar this map said it would apply. It is a third shape on the [harness route](comparisons/agent-harness-frameworks.md): not a loop you fork and not a meta-harness that drives other loops, but **a harness you deploy and call over HTTP** — model calls, MCP tools, `SKILL.md` packs, sandboxing, approvals, subagents, and session state run inside a server that exposes a chat UI, a REST API with a TypeScript SDK, and an embeddable UI SDK. Still on the watchlist: [trailhq/Graft](https://github.com/trailhq/Graft) (5.4k, MIT, a shared code-graph context layer — overlaps [CodeGraph](agents/codegraph.md), held for that reason), [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) (7.0k), [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi) (3.2k, still `NOASSERTION` — a hard blocker), [QwenLM/Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) (2.8k), and new this window [Nanako0129/sepia](https://github.com/Nanako0129/sepia) (1.4k in four days, MIT).
- Off the board, the vendor layer moved twice: **[Meta took Muse Code out of beta on Aug 31](market-events.md)** with three subscription plans and a contributor tier that trades your prompts and completions for a ~21× cheaper output rate, and **a ransomware crew was documented driving Cursor Agent through hands-on intrusion in ten organizations** ([Gambit Security, Aug 27](market-events.md)). Details in [market-events](market-events.md).

<details>
<summary>More window notes: skills-wave share, OpenClaw, and everything growing outside the top 10</summary>

- The `.claude/skills` wave **holds five of the top ten**, its first five-seat window since 2026-07-14 — and the new seat is [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills), a science collection, with [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) just behind at #11. The concentration the map flagged last window is still real — [mattpocock/skills](https://github.com/mattpocock/skills) still out-gains the other general collections combined (5,954 against 4,899). What is genuinely new is not that a vertical collection is on the board (that has been true on and off since May) but that one is **leading** it. Policy unchanged: curated collections are tracked as Skills Wave entries, the framework end is covered through [Superpowers](agents/superpowers.md).
- Just off the table: [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 44.8k (+975, rate up 67%), [CodeGraph](agents/codegraph.md) 69.1k (+814, rate up 9%, down from #9) and [OpenClaw](agents/openclaw.md) (+792). [n8n](agents/n8n.md) lost its seat again, finishing 16th by gain among the ranked projects on a rate 29% cooler (203.1k, +527) — it has now held a seat in two of the last four windows.
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 388.5k stars (+792, rate up 40%); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.
- **The "first window after a pickup is the peak" read from last window half held.** [QM](agents/qm.md) decelerated a second time (−47%, 14.4k) and [Open Code Review](agents/open-code-review.md) a second time (−25%, 21.8k), but [Omnigent](agents/omnigent.md) reversed up (+25%, 9.6k) and [Langfuse](agents/langfuse.md) held flat again (+4%, 34.1k). Two of four kept falling, which is weaker than the rule the map stated — worth recording as a partial miss rather than a confirmation.
- **[eve](agents/eve.md) posts its first stamped count at 4,902** (`vercel/eve`), tracked from this window forward; it carries no gain yet because it was untracked when the window opened. [TrueForge](agents/trueforge.md) (5,038) is profiled but not yet polled — per house rule a new profile carries `tracked: false` for one window, so it enters the boards next refresh.
- **[Grok Build](agents/grok-build.md) resumed decelerating**: +235 to 26.3k, a weekly rate of ~329 against 640 — last window's uptick did not hold, and the post-launch decay is back on.
- Continuing to grow but outside the top 10 by gain (raw 5-day figures): [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 44.8k (+975), [CodeGraph](agents/codegraph.md) 69.1k (+814), [OpenHands](agents/openhands.md) 85.9k (+681), [Ruflo](agents/ruflo.md) 70.1k (+646), [Claude Code](agents/claude-code.md) 143.7k (+593), [n8n](agents/n8n.md) 203.1k (+527), [CLI-Anything](agents/cli-anything.md) 48.8k (+502), [LiteLLM](agents/litellm.md) 57.8k (+430), [Cline](agents/cline.md) 67.3k (+381), [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) 27.9k (+378), [LangChain](agents/langchain.md) 145.4k (+373), [LangGraph](agents/langgraph.md) 40.9k (+368), [jcode](agents/jcode.md) 19.0k (+322), [Open Code Review](agents/open-code-review.md) 21.8k (+315), [CrewAI](agents/crewai.md) 58.0k (+312), [Langfuse](agents/langfuse.md) 34.1k (+285), [Goose](agents/goose.md) 53.8k (+275), [Omnigent](agents/omnigent.md) 9.6k (+275), [Grok Build](agents/grok-build.md) 26.3k (+235), [QM](agents/qm.md) 14.4k (+188), [AutoGPT](agents/autogpt.md) 187.1k (+162), [Aider](agents/aider.md) 48.7k (+139), [humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) 25.6k (+129), [mini-swe-agent](agents/mini-swe-agent.md) 6.9k (+123), [Kimi Code](agents/kimi-code.md) 7.2k (+115), [anthropics/financial-services](https://github.com/anthropics/financial-services) 34.6k (+93), [LlamaIndex](agents/llamaindex.md) 52.0k (+87), [Letta (MemGPT)](agents/memgpt.md) 24.5k (+86), [Continue](agents/continue.md) 35.7k (+81), [OpenHarness](agents/openharness.md) 15.6k (+65), [Open Interpreter](agents/open-interpreter.md) 68.2k (+60), [MiMoCode](agents/mimocode.md) 12.9k (+42), [SWE-agent](agents/swe-agent.md) 20.2k (+41), [CodeWhale](agents/codewhale.md) 40.9k (+24), [CoStrict](agents/costrict.md) 4.4k (+7), [Flowise](agents/flowise.md) 55.4k (+5)

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
| Agent harness framework | [Pi](agents/pi.md), [jcode](agents/jcode.md), [OpenHands](agents/openhands.md), [SWE-agent](agents/swe-agent.md), [mini-swe-agent](agents/mini-swe-agent.md), [OpenHarness](agents/openharness.md), [QM](agents/qm.md), [Omnigent](agents/omnigent.md), [TrueForge](agents/trueforge.md) | Someone who wants to own the agent loop, tool surface, and permissions instead of inheriting a vendor's product — QM and Omnigent extend this to running *several* harnesses under one layer (see the [harness comparison](comparisons/agent-harness-frameworks.md)) |
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

62 profiled projects, grouped by what they are. Expand a group, or browse the full route/coverage tables in [agents/](agents/README.md).

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
<summary><strong>Autonomous and self-hosted agents</strong> (15 projects)</summary>

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
| [TrueForge](agents/trueforge.md) | Agent harness framework | Harness-as-a-server — one loop behind an HTTP API, with a chat UI, a TypeScript SDK, and an embeddable UI |

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