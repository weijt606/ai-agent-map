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
| I want every project scored on those dimensions, side by side | [![View capability matrix](https://img.shields.io/badge/VIEW-CAPABILITY%20MATRIX-059669?style=for-the-badge&labelColor=047857)](capabilities/matrix.md) |
| I want to know what it actually costs to run, and which model tier is worth it | [![View cost and benchmarks](https://img.shields.io/badge/VIEW-COST%20%26%20BENCHMARKS-0891b2?style=for-the-badge&labelColor=0e7490)](comparisons/cost-and-benchmarks.md) [![View memory approaches](https://img.shields.io/badge/VIEW-MEMORY%20APPROACHES-0d9488?style=for-the-badge&labelColor=0f766e)](comparisons/memory-approaches.md) |
| My agents already run — I need to know whether they still work | [![View observability and evaluation](https://img.shields.io/badge/VIEW-OBSERVABILITY%20%26%20EVALS-4f46e5?style=for-the-badge&labelColor=3730a3)](comparisons/observability-and-evals.md) |
| I want the stock rankings and the weekly trend chart | [![View rankings](https://img.shields.io/badge/VIEW-RANKINGS-7c3aed?style=for-the-badge&labelColor=5b21b6)](rankings/README.md) |
| I want problem-first guides or the full comparison list | [![Browse use cases](https://img.shields.io/badge/BROWSE-USE%20CASES-ea580c?style=for-the-badge&labelColor=9a3412)](use-cases/README.md) [![Browse comparisons](https://img.shields.io/badge/BROWSE-COMPARISONS-475569?style=for-the-badge&labelColor=334155)](comparisons/README.md) |

## Recent Heat Ranking

Popularity is not fit.

This table tracks projects that showed up as especially hot in the latest weekly GitHub snapshot. The rank follows the 7-day gain. The total star counts below were checked when this repo was updated.

> **Last updated:** 2026-09-09 · **Snapshot window:** 2026-09-06 → 2026-09-09 (gain since last update, **3 days** — the regular Wednesday cadence resumes after Sunday's off-cycle refresh, so this window is short and noisy; raw gains here are ~0.43x a normal window and every comparison below is stated on the **weekly rate**) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(=) | [mattpocock/skills](https://github.com/mattpocock/skills) | 257.6k | +3,237 | Watchlist (Skills Wave) | Holds #1 **by 11 stars** while its own rate falls 48% (~14,600/week → ~7,550). Past **257k**, but this is the narrowest lead the board has recorded |
| #2&nbsp;(new) | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 217.2k | +3,226 | In scope · [profile](agents/deepseek-harness.md) | **First measured gain, and it lands at #2** on ~7,530/week, within 1% of the leader. Tracked from last window; this is the first window it could rank at all |
| #3&nbsp;(=) | [Superpowers](https://github.com/obra/superpowers) | 283.8k | +1,414 | In scope · [profile](agents/superpowers.md) | Up 19% on the rate and the only skills entry that accelerated this window. Holds #3 for a second window |
| #4&nbsp;(↓) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 243.7k | +1,232 | In scope · [profile](agents/hermes-agent.md) | Down 32% and two seats the window after crossing 240k. Still present in all 20 recorded windows |
| #5&nbsp;(new) | [Browser Use](https://github.com/browser-use/browser-use) | 113.9k | +1,228 | In scope · [profile](agents/browser-use.md) | **First measured gain**, straight to #5 on ~2,870/week. The browser-agent route's only entry, profiled three days ago |
| #6&nbsp;(↓) | [Pi](https://github.com/earendil-works/pi) | 103.4k | +1,028 | In scope · [profile](agents/pi.md) | Cooled another 10% and crossed **103k**. Two consecutive windows of gentle decline after the 100k milestone |
| #7&nbsp;(new) | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 103.6k | +924 | Out of scope (finance-research vertical) | Rate up **189%** and back on the table after one window off; crossed **103k**. One short window, so the board is not reading it as a trend |
| #8&nbsp;(new) | [OpenCode](https://github.com/anomalyco/opencode) | 206.1k | +916 | In scope · [profile](agents/opencode.md) | **First measured gain** at ~2,140/week, past **206k**. The third of last window's new pickups to take a top-ten seat immediately |
| #9&nbsp;(↑) | [Ruflo](https://github.com/ruvnet/ruflo) | 71.8k | +824 | In scope · [profile](agents/ruflo.md) | Rate up **71%** in its second window on the board, confirming last window's first-ever appearance rather than reversing it |
| #10&nbsp;(↓) | [Codex CLI](https://github.com/openai/codex) | 122.8k | +814 | In scope · [profile](agents/codex.md) | Up 7% on the rate but down two seats, which is what happens when three new repos enter above you |

- Heat is useful for discovery, not for selection by itself.
- **This window is 3 days.** Sunday's refresh was off-cycle, and the regular Wednesday cadence resumes here, so the span is short and the raw gains are roughly 0.43x a normal week. Every claim below is stated on the **weekly rate** (gain ÷ 3 × 7) against last window's rate (gain ÷ 5 × 7). A three-day window is the noisiest this board has published; read the direction, not the decimals.
- **Three repositories that entered tracking last window took top-ten seats on their first measured gain.** [DeepSeek Harness](agents/deepseek-harness.md) at #2, [Browser Use](agents/browser-use.md) at #5, [OpenCode](agents/opencode.md) at #8. None of them could rank before this window, because they were untracked when the previous one opened. That is a scanning failure showing up as a result: all three were large and active for weeks while this board had no line for them.
- **The #1 seat was decided by 11 stars.** [mattpocock/skills](https://github.com/mattpocock/skills) took +3,237 against DeepSeek Harness's +3,226. The leader's own rate fell 48% from last window's record, so it held the seat by decelerating slightly less than the field, not by pulling away.
- **The skills wave fell to 2 of 10, its lowest share since the wave began.** It was 6 of 10 last window, which matched the board record. The drop has two causes and both are real: three non-skills repos entered above them, and the collections genuinely cooled — [anthropics/skills](https://github.com/anthropics/skills) −52% on the rate, [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) −37%, [K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills) −27%, [addyosmani](https://github.com/addyosmani/agent-skills) −12%. [Superpowers](agents/superpowers.md) is the sole exception, up 19%. Since 2026-05-23 the wave's floor had been 3 of 10, set once on 2026-07-29.
- **[Ruflo](agents/ruflo.md) is the one entry that confirmed rather than reversed.** Its first-ever appearance last window could have been a spike; the rate is up 71% in the second window instead. By this board's own rule that is the first breakout in five windows to survive its follow-up.
- **Two accelerations that this board is explicitly not calling trends yet**: [TradingAgents](https://github.com/TauricResearch/TradingAgents) up 189% and back on the table, and [OpenHands](agents/openhands.md) up 129% at #12. One short window is a spike until a second confirms it, and four of the last five failed that test.
- Milestones this window: [OpenCode](agents/opencode.md) crossed **206k**, [DeepSeek Harness](agents/deepseek-harness.md) **217k**, [Pi](agents/pi.md) and [TradingAgents](https://github.com/TauricResearch/TradingAgents) both **103k**, mattpocock/skills **257k**.
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 389.3k stars (+241); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.

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
- **The model layer became a budget decision — and in the first week of September both ceilings moved to the same price**: [Claude Fable 5.1](agents/claude-fable-5.md) (Sept 1) and [GPT-6 Astra](agents/gpt-6-astra.md) (Sept 3) both list at **$10 / $50**, so the frontier comparison is no longer about the sticker. It is about **cache reads** ($0.25 vs $1) and **long-context shape** — Anthropic bills its 1M window at flat rates, OpenAI doubles input past 272k tokens. Underneath, the tier ladders are what most work should run on: [Opus 5](agents/claude-opus-5.md) ($5/$25, the Claude Code default since July 24) and Sonnet 5 ($2/$10) on one side, GPT-5.6 Sol/Terra/Luna on the other, with Sol's promotional $4/$20 running to at least Nov 21. Full table in [cost & benchmarks](comparisons/cost-and-benchmarks.md); lineage in [GPT-5.5](agents/gpt-5.5.md).
- **Product boundaries are collapsing upward**: OpenAI merged Codex into the ChatGPT app (July 9) — on the OpenAI side, "which coding agent" is turning into "how you use ChatGPT." Since Codex CLI `rust-v0.153.4` (Sept 4) the bundled default model there is [GPT-6 Astra](agents/gpt-6-astra.md), which means the product's default now inherits Astra's restricted cybersecurity behaviour. See [Codex](agents/codex.md).

## The First Cut Of The Map

<p align="center">
  <img src="assets/route-map-en.svg" alt="The AI Agent Map — 15 routes grouped into four decisions" width="100%" />
</p>

| Route | Representative projects | Typical user |
| --- | --- | --- |
| Direct execution | [Claude Code](agents/claude-code.md), [Aider](agents/aider.md), [Codex](agents/codex.md), [Kimi Code](agents/kimi-code.md), [MiMoCode](agents/mimocode.md), [CodeWhale](agents/codewhale.md), [ZCode](agents/zcode.md), [OpenCode](agents/opencode.md), [Gemini CLI](agents/gemini-cli.md), [Qwen Code](agents/qwen-code.md), [Grok Build](agents/grok-build.md), [Devin](agents/devin.md), [Jules](agents/jules.md) | Someone who wants to hand a concrete coding task to an agent (see the [terminal coding CLI comparison](comparisons/coding-cli-agents.md)) |
| Agent harness framework | [DeepSeek Harness](agents/deepseek-harness.md), [Pi](agents/pi.md), [jcode](agents/jcode.md), [OpenHands](agents/openhands.md), [SWE-agent](agents/swe-agent.md), [mini-swe-agent](agents/mini-swe-agent.md), [OpenHarness](agents/openharness.md), [QM](agents/qm.md), [Omnigent](agents/omnigent.md), [TrueForge](agents/trueforge.md) | Someone who wants to own the agent loop, tool surface, and permissions instead of inheriting a vendor's product — QM and Omnigent extend this to running *several* harnesses under one layer (see the [harness comparison](comparisons/agent-harness-frameworks.md)) |
| Frontier agentic model | [Claude Fable 5.1](agents/claude-fable-5.md), [Claude Opus 5](agents/claude-opus-5.md), [GPT-6 Astra](agents/gpt-6-astra.md), [GPT-5.5](agents/gpt-5.5.md) | Someone choosing which model to wire into their own agent system or evaluating the capability ceiling of Anthropic / OpenAI surfaces — the ceilings (Fable 5.1, Astra) and the default you actually run (Opus 5) are separate decisions |
| Open-weights agentic model | [Kimi K3](agents/kimi-k3.md), [GLM-5.3](agents/glm-5.md), [DeepSeek V4](agents/deepseek-v4.md), [Qwen3-Coder](agents/qwen3-coder.md) | Someone who wants frontier-class capability on weights they host and licence themselves — a different decision from picking between the closed ceilings |
| Agentic skills framework | [Superpowers](agents/superpowers.md) | Someone who wants a methodology + composable skills layer that plugs into Claude Code, Codex, Cursor, and similar agents |
| Workflow / orchestration layer | [oh-my-claudecode](agents/oh-my-claudecode.md), [oh-my-codex](agents/oh-my-codex.md), [Ruflo](agents/ruflo.md) | Someone who already likes Claude Code or Codex and wants stronger orchestration on top (Ruflo extends this to multi-machine federation and 100+ specialized agents) |
| Editor-centric AI workflow | [Cursor](agents/cursor.md), [Windsurf](agents/windsurf.md), [Continue](agents/continue.md) | Someone who wants the editor itself to stay central |
| Review-first automation | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md), [CoStrict](agents/costrict.md), [Open Code Review](agents/open-code-review.md) | Someone who wants review and human control to stay central (CoStrict adds enterprise strict-workflow + private deployment; Open Code Review is review only, tuned for precision in CI) |
| Managed background path | [Claude Managed Agents](agents/claude-managed-agents.md) | Someone who needs scheduled, cloud, or detached Anthropic workflows |
| General-purpose autonomous agent | [AutoGPT](agents/autogpt.md), [Agent Zero](agents/agent-zero.md), [BabyAGI](agents/babyagi.md), [Julep](agents/julep.md), [GenericAgent](agents/generic-agent.md), [ml-intern](agents/ml-intern.md), [WorkBuddy](agents/workbuddy.md), [Kimi Work](agents/kimi-work.md) | Someone who wants autonomous, general-purpose task execution — ml-intern is the ML-specialized variant, while WorkBuddy and Kimi Work aim the same loop at desktop knowledge work rather than repositories |
| Build-your-own system | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md), [Haystack](agents/haystack.md), [Semantic Kernel](agents/semantic-kernel.md), [DSPy](agents/dspy.md), [Pydantic AI](agents/pydantic-ai.md), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) | Teams building their own agent platform instead of buying one |
| Runtime and tools | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [CLI-Anything](agents/cli-anything.md) | Teams that need workflow automation, code execution, LLM gateways, agent context infrastructure, agent-driven CLIs, or visual builders |
| Observability and evals | [Langfuse](agents/langfuse.md) | Someone whose agents already run in production and needs to know what they did, what they cost, and whether quality is drifting (see [observability & evaluation](comparisons/observability-and-evals.md)) |
| Browser agent | [Browser Use](agents/browser-use.md) | Someone whose task lives on a website with no API — a different question from how an agent edits files, because it decides what an agent may do as you on the open web |
| Self-hosted / local runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md), [OpenHuman](agents/openhuman.md) | Users who need on-device privacy, long-running agents, local control, channels, devices, or personal-data life integration |

## Current Mainstream Coverage

77 profiled projects, grouped by what they are. Expand a group, or browse the full route/coverage tables in [agents/](agents/README.md).

<details>
<summary><strong>Coding agents, editors, and orchestration</strong> (32 projects)</summary>

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
| [OpenCode](agents/opencode.md) | Direct execution | The largest vendor-neutral open-source coding agent — 205k stars, MIT |
| [Gemini CLI](agents/gemini-cli.md) | Direct execution | Google's terminal agent; 1,000 free requests a day and Search grounding built in |
| [Qwen Code](agents/qwen-code.md) | Direct execution | Open client and open weights, switchable across OpenAI/Anthropic/Gemini/local at runtime |
| [DeepSeek Harness](agents/deepseek-harness.md) | Agent harness framework | Everything-is-a-plugin harness — even the agent loop is swappable from config |
| [ZCode](agents/zcode.md) | Direct execution | Zhipu's desktop agentic dev environment: long-horizon "Goal" tasks, steerable from WeChat/Feishu/Telegram |
| [Open Code Review](agents/open-code-review.md) | Review-first automation | Alibaba's precision-first code-review CLI — deterministic pipeline around the model, plus CI and agent-plugin surfaces |

</details>

<details>
<summary><strong>Autonomous and self-hosted agents</strong> (17 projects)</summary>

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
| [WorkBuddy](agents/workbuddy.md) | General-purpose autonomous agent | Tencent's desktop office agent — the same loop, aimed at documents, decks, and spreadsheets |
| [Kimi Work](agents/kimi-work.md) | General-purpose autonomous agent | Moonshot's desktop knowledge-work agent: mounted folders, browser automation, built-in cron |
| [TrueForge](agents/trueforge.md) | Agent harness framework | Harness-as-a-server — one loop behind an HTTP API, with a chat UI, a TypeScript SDK, and an embeddable UI |

</details>

<details>
<summary><strong>Frameworks and infrastructure</strong> (19 projects)</summary>

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
| [Browser Use](agents/browser-use.md) | Browser agent | Gives an agent a real browser — opens pages, clicks, types, fills forms |
| [Microsoft Agent Framework](agents/microsoft-agent-framework.md) | Build-your-own system | AutoGen's successor; production multi-agent workflows across Python, .NET, and Go |
| [CLI-Anything](agents/cli-anything.md) | Runtime and tools | Auto-generates Click-based CLIs for arbitrary software so agents can drive non-API apps |

</details>

<details>
<summary><strong>Models and skills</strong> (9 entries)</summary>

| Project | Route | One-line positioning |
| --- | --- | --- |
| [Claude Fable 5.1](agents/claude-fable-5.md) | Frontier agentic model | Anthropic's Mythos-class ceiling — the model you spend credits on, refreshed Sept 1 2026 |
| [Claude Opus 5](agents/claude-opus-5.md) | Frontier agentic model | The Opus tier at half the ceiling's price — the Claude model most agents actually run on |
| [GPT-6 Astra](agents/gpt-6-astra.md) | Frontier agentic model | OpenAI's current ceiling (Sept 3 2026), shipped to the public in a restricted version |
| [GPT-5.5](agents/gpt-5.5.md) | Frontier agentic model | OpenAI's spring 2026 model, kept as the lineage reference through GPT-5.6 to Astra |
| [Kimi K3](agents/kimi-k3.md) | Open-weights agentic model | First open 3T-class model — 2.8T params, native vision, 1M context, custom licence |
| [GLM-5.3](agents/glm-5.md) | Open-weights agentic model | Strongest open-weights coding model on vendor numbers, Apache-2.0 — and ungated cyber capability |
| [DeepSeek V4](agents/deepseek-v4.md) | Open-weights agentic model | MIT at 1.6T params; SWE-bench Verified 80.6, reproducible because the weights are open |
| [Qwen3-Coder](agents/qwen3-coder.md) | Open-weights agentic model | The one that fits — ~3B activated of 80B, 256K→1M context, runs where you are |
| [Superpowers](agents/superpowers.md) | Agentic skills framework | Methodology and composable skills layer that plugs into Claude Code, Codex, Cursor, and other agents |

</details>

## Example Reading Paths

If you are still deciding where to begin, use one of these quick routes and then branch out.

| If you sound like this... | Follow this path | What it helps you answer |
| --- | --- | --- |
| I want a day-to-day coding agent and need to choose terminal vs editor | [Aider](agents/aider.md) → [Claude Code](agents/claude-code.md) → [terminal coding CLI comparison](comparisons/coding-cli-agents.md) → [Cursor](agents/cursor.md) → [Cline](agents/cline.md) → [coding automation guide](use-cases/coding-automation.md) | Which vendor CLI fits your model, terminal-first local loop vs editor-led flow vs approval-first control |
| I already like Claude Code or Codex but want stronger orchestration | [Claude Code](agents/claude-code.md) → [oh-my-claudecode](agents/oh-my-claudecode.md) → [Codex](agents/codex.md) → [oh-my-codex](agents/oh-my-codex.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | When the base agent is enough and when a workflow layer actually adds value |
| I want to understand how the 2026 model race changes agent choice | [Claude Fable 5.1](agents/claude-fable-5.md) → [Claude Opus 5](agents/claude-opus-5.md) → [GPT-6 Astra](agents/gpt-6-astra.md) → [Codex](agents/codex.md) → [Claude Code](agents/claude-code.md) → [market events](market-events.md) | How the frontier tiers and the default tier under them shift the capability ceiling, and what it means for product choice |
| I want a dedicated AI IDE instead of stitching tools together | [Cursor](agents/cursor.md) → [Windsurf](agents/windsurf.md) → [GitHub Copilot](agents/github-copilot.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Dedicated AI editor vs ecosystem platform |
| I want to hand off tickets and check back later | [Codex](agents/codex.md) → [Jules](agents/jules.md) → [Devin](agents/devin.md) → [Claude Managed Agents](agents/claude-managed-agents.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Async cloud delegation vs managed background automation |
| I need something open-source or self-hosted | [Aider](agents/aider.md) → [OpenHands](agents/openhands.md) → [Goose](agents/goose.md) → [Hermes Agent](agents/hermes-agent.md) → [capabilities](capabilities/README.md) | Terminal control, open-source execution, and local runtime ownership |
| I am building an internal agent stack, not buying a product | [LangChain](agents/langchain.md) → [LangGraph](agents/langgraph.md) → [capabilities](capabilities/README.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Framework vs runtime vs product boundaries |

## Disclaimer

Star counts and 7-day gains are point-in-time GitHub snapshots taken when the repo is updated; numbers shift quickly between weekly refreshes and small rounding differences are expected. Project descriptions, vendors, and capability summaries reflect public information at the time of writing and may change as projects evolve, get acquired, or pivot. This map is selection guidance — not endorsement, financial advice, or a production-readiness guarantee. Verify against each project's own docs before committing to a choice.