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

> **Last updated:** 2026-09-24 · **Snapshot window:** 2026-09-17 → 2026-09-24 (gain since last update, **7 days** against last window's 8, so the two columns are close but not identical; every claim below is stated on the **weekly rate**) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(=) | [Open Code Review](https://github.com/alibaba/open-code-review) | 40.2k | +7,112 | In scope · [profile](agents/open-code-review.md) | **Held #1 after the Trending placement ended.** The rate fell 26%, which is a spike giving part of itself back — but it is still the largest gain on the board, and it cleared **35k** and **40k** in one window. Two windows is this board's own bar for a trend, and it cleared it |
| #2&nbsp;(=) | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 234.3k | +7,096 | In scope · [profile](agents/deepseek-harness.md) | Third consecutive window at #2, rate down 19%, past **230k**. It finished **16 stars** behind #1 — the second-narrowest gap at the top this board has recorded, after the 11 stars of 2026-09-09 |
| #3&nbsp;(=) | [mattpocock/skills](https://github.com/mattpocock/skills) | 268.5k | +4,613 | Watchlist (Skills Wave) | Rate down 17%. **A second window running outside the top two** — the first time that has happened in its 18 windows on this board. Past **265k** |
| #4&nbsp;(↑) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 98.7k | +3,033 | Watchlist (Skills Wave) | Rate up **37%**, a second consecutive acceleration and its best seat since 2026-08-12. It is **1,288 stars short of 100k** — not there yet |
| #5&nbsp;(↓) | [Superpowers](https://github.com/obra/superpowers) | 290.7k | +2,882 | In scope · [profile](agents/superpowers.md) | Rate down 18% and one seat, but it cleared **290k** — the second-largest total on this board |
| #6&nbsp;(=) | [Pi](https://github.com/earendil-works/pi) | 108.9k | +2,439 | In scope · [profile](agents/pi.md) | Rate down 9%, a third window in the same seat. Steady rather than cooling |
| #7&nbsp;(new) | [Claude Code](https://github.com/anthropics/claude-code) | 147.8k | +2,108 | In scope · [profile](agents/claude-code.md) | **Its first top-ten seat** — it appears in none of the board's previous 22 windows. Rate up **105%**, and the window contains `v2.1.280` (Sept 22) making **Opus 5.5** the default Opus model |
| #8&nbsp;(↓) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 248.4k | +2,081 | In scope · [profile](agents/hermes-agent.md) | Rate down 9% and one seat. **Present in all 23 recorded windows** — still the only project that has never missed one |
| #9&nbsp;(new) | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 36.9k | +2,048 | Out of scope (finance vertical) | **A 19x jump in weekly rate** (~105 → 2,048), the second-largest this board has computed, behind Open Code Review's 26x last window. No cause is documented, so the spike rule applies in full. Crossed **35k** |
| #10&nbsp;(=) | [OpenCode](https://github.com/anomalyco/opencode) | 209.7k | +1,667 | In scope · [profile](agents/opencode.md) | Rate essentially flat (−1%) for a third consecutive window — the steadiest line on the board this week |

- Heat is useful for discovery, not for selection by itself.
- **This window is 7 days against last window's 8.** The two columns are close but not identical, so every claim here is on the **weekly rate** (this window: the gain as printed; last window: gain ÷ 8 × 7).
- **The board cooled broadly: 19 of 55 tracked repos accelerated, 36 slowed.** The top two both gave back a quarter of their rate and still finished 2,500 clear of #3. Read this as one very hot window unwinding, not as a new leader emerging.
- **[Open Code Review](agents/open-code-review.md) confirmed.** Last window this board called its 26x jump a spike because the cause — **#1 on GitHub Trending on September 16** — is the most transient one there is. It then held #1 through a window with no Trending placement in it, at 74% of the previous rate, and cleared **35k** and **40k**. By the board's own two-window rule that is a trend.
- **[Claude Code](agents/claude-code.md) takes a top-ten seat for the first time.** It is in none of the previous 22 windows, and this is not a small repo arriving — it is the tenth-largest repo this board tracks by total stars, doubling a rate that had been flat for two months. The window contains `v2.1.280` (Sept 22), which made **[Opus 5.5](comparisons/cost-and-benchmarks.md)** the default Opus model on the same day Anthropic announced it.
- **Two `anthropics/*` repos hold seats in the same window for the first time**, and neither is [anthropics/skills](https://github.com/anthropics/skills), which is now three windows off the board. [anthropics/financial-services](https://github.com/anthropics/financial-services) went from ~105/week to 2,048 — a 19x jump, second only to Open Code Review's 26x. Unlike that one it has **no documented cause**: no release, no Trending placement this board can point at, and the two commits in the window are a deletion and a security fix. It is a spike until a second window says otherwise.
- **A correction to last window's read on [TradingAgents](https://github.com/TauricResearch/TradingAgents).** This board wrote that its second consecutive acceleration was "the confirmation this board said it was waiting for" and recorded it as a confirmed trend. It then fell **63%** and left the table. That is the second time in two windows a confirmation call has failed (Ruflo was the first), which is worth stating plainly: **two windows of growth is a weaker signal than this board has been treating it as**, especially when either window is short.
- **[Codex CLI](agents/codex.md) falls off after 13 consecutive windows** (2026-06-24 → 2026-09-17). Four longer streaks were running when it ended — Hermes Agent 22, Superpowers 17, mattpocock/skills 17, Pi 16 — so this is the shortest of the board's five long runs, but it is the only one of the five to break. It did not collapse — the rate fell 28% and it finished 11th — but a streak that long ending is the more durable fact.
- The skills wave recovered to **4 of 10** from 3, and holds seats #3, #4 and #5 as a contiguous block. Inside the wave the split is the story again: [addyosmani](https://github.com/addyosmani/agent-skills) up 37%, [mattpocock](https://github.com/mattpocock/skills) down 17%, [Superpowers](agents/superpowers.md) down 18%, and the new seat is a **vendor** collection rather than a community one.
- Milestones, checked against the raw counts rather than the rounded column: Open Code Review crossed **35k** and **40k**, DeepSeek Harness **230k**, mattpocock/skills **265k**, Superpowers **290k**, financial-services **35k**, [Browser Use](agents/browser-use.md) **115k**, [n8n](agents/n8n.md) **205k**, and [OpenClaw](agents/openclaw.md) **390k**.
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 390.3k stars (+416, rate down 27%); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.

<details>
<summary>More window notes: skills-wave share, OpenClaw, and everything growing outside the top 10</summary>

- **Housekeeping first: this block was stale for two refreshes.** The notes here were last rewritten on 2026-09-01 and still carried that window's 5-day figures through the 09-09 and 09-17 refreshes, including a "five of the top ten" skills-wave count that the main bullets above had already contradicted. It is regenerated from this window's fetch below, and the off-board list is now produced from the snapshot rather than typed by hand.
- The `.claude/skills` wave **holds four of the top ten**, up from three, and they sit together at #3, #4 and #5 plus the newcomer at #9. The concentration read still holds but has softened: [mattpocock/skills](https://github.com/mattpocock/skills) at +4,613 no longer out-gains the other general collections combined (+3,033 addyosmani, +2,882 Superpowers, +1,051 anthropics/skills = 6,966). That comparison flipped last window and has now flipped further, so treat "one directory is the wave" as a 2026 H1 fact rather than a current one. Policy unchanged: curated collections are tracked as Skills Wave entries, the framework end is covered through [Superpowers](agents/superpowers.md).
- Just off the table: [Codex CLI](agents/codex.md) 126.2k (+1,316) at 11th, [Browser Use](agents/browser-use.md) 116.1k (+1,207) at 12th on a rate up 40%, [TradingAgents](https://github.com/TauricResearch/TradingAgents) 108.3k (+1,134) at 13th, and [n8n](agents/n8n.md) 205.8k (+1,073) at 14th on a rate up 36%. OpenClaw is excluded from the board, so these off-board positions are counted the same way.
- **The research collections kept cooling.** [K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills) (−6%, 46.3k) has now slowed for a **fourth consecutive window** since its 09-01 peak, and [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (−16%, 49.3k) for a **third** since its own peak on 09-06. The science vertical that led the board three weeks ago holds no seat at all.
- **[Browser Use](agents/browser-use.md) reversed up 40%** after falling 70% last window, and crossed **115k**. One window up after one window down is not a trend either way; it is recorded here so the next window has a baseline.
- **[eve](agents/eve.md) has nearly stopped**: +18 to 5.3k, a weekly rate of 18 against 265 — a 93% fall, the steepest on the board. [TrueForge](agents/trueforge.md) (+220, 5.9k) slowed 36% in its first fully measured window. Both are young enough that this is noise, but both are now moving slower than every other profiled harness.
- **[Graft](agents/graft.md) is this window's new profile** (`trailhq/Graft`, 9.1k). It carries `tracked: false` for one window per house rule, so it takes no seat on any board until the next refresh.
- Continuing to grow but outside the top 10 by gain (raw 7-day figures): [Codex CLI](agents/codex.md) 126.2k (+1,316), [Browser Use](agents/browser-use.md) 116.1k (+1,207), [TradingAgents](https://github.com/TauricResearch/TradingAgents) 108.3k (+1,134), [n8n](agents/n8n.md) 205.8k (+1,073), [anthropics/skills](https://github.com/anthropics/skills) 177.8k (+1,051), [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 46.3k (+1,032), [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 49.3k (+883), [OpenHands](agents/openhands.md) 89.0k (+761), [CodeGraph](agents/codegraph.md) 71.9k (+712), [Cline](agents/cline.md) 69.2k (+685), [LiteLLM](agents/litellm.md) 59.5k (+539), [Ruflo](agents/ruflo.md) 73.2k (+490), [12-factor-agents](https://github.com/humanlayer/12-factor-agents) 26.4k (+469), [LangChain](agents/langchain.md) 146.9k (+444), [CLI-Anything](agents/cli-anything.md) 49.9k (+407), [LangGraph](agents/langgraph.md) 42.2k (+394), [MiMoCode](agents/mimocode.md) 13.4k (+287), [CrewAI](agents/crewai.md) 59.0k (+278), [Langfuse](agents/langfuse.md) 35.0k (+269), [jcode](agents/jcode.md) 20.1k (+267), [agentmemory](https://github.com/rohitg00/agentmemory) 28.8k (+251), [OpenHuman](agents/openhuman.md) 40.1k (+249), [Grok Build](agents/grok-build.md) 27.1k (+241), [mini-swe-agent](agents/mini-swe-agent.md) 7.9k (+223), [Goose](agents/goose.md) 54.6k (+222), [TrueForge](agents/trueforge.md) 5.9k (+220), [Kimi Code](agents/kimi-code.md) 7.6k (+214), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) 13.8k (+203), [Qwen Code](agents/qwen-code.md) 28.1k (+188), [Omnigent](agents/omnigent.md) 10.2k (+163), [Aider](agents/aider.md) 49.1k (+123), [AutoGPT](agents/autogpt.md) 187.5k (+116), [Gemini CLI](agents/gemini-cli.md) 107.1k (+111), [LlamaIndex](agents/llamaindex.md) 52.3k (+110), [QM](agents/qm.md) 15.2k (+101), [Letta (MemGPT)](agents/memgpt.md) 24.9k (+91), [OpenHarness](agents/openharness.md) 15.8k (+74), [Continue](agents/continue.md) 36.0k (+68), [Open Interpreter](agents/open-interpreter.md) 68.4k (+61), [SWE-agent](agents/swe-agent.md) 20.4k (+47), [CodeWhale](agents/codewhale.md) 41.0k (+43), [eve](agents/eve.md) 5.3k (+18), [Flowise](agents/flowise.md) 55.5k (+10), [CoStrict](agents/costrict.md) 4.4k (+8)

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
- **[Memory approaches](comparisons/memory-approaches.md)** — seven different things projects mean by "has memory," from self-editing stores to passive semantic recall, and which to pick for what you need to persist.
- **[Observability & evaluation](comparisons/observability-and-evals.md)** — the layer under everything above: once an agent runs unattended, failure stops looking like a crash and starts looking like silent quality drift. Compares [Langfuse](agents/langfuse.md), Opik, Phoenix, Helicone, LangSmith and others — and untangles the four different things "open source" means in that field.

## Market Pulse

The three structural stories shaping selection right now — full records with dates and sources live in [market-events.md](market-events.md):

- **The `.claude/skills` wave is still half the board, but the concentration read has flipped** (May 2026 → ongoing): curated skill collections and skills frameworks have held roughly half of the weekly heat top 10 for four months, and the count has been rotating rather than sitting still — 6/10, then 2/10, then 3/10, now **4 of 10** (2026-09-24). What changed is the split inside the wave. Through August [mattpocock/skills](https://github.com/mattpocock/skills) out-gained the other general collections combined; as of this window it does not (+4,613 against +6,966), and the newest seat belongs to a **vendor** collection, [anthropics/financial-services](https://github.com/anthropics/financial-services), rather than a community one. Read the key-person risk as easing, not as resolved. This map profiles the framework end through [Superpowers](agents/superpowers.md) and tracks collections on the [skill boards](rankings/skill-verticals.md).
- **The model layer became a budget decision — and on September 22 both vendors cut below their own ceiling on the same day**: [Claude Fable 5.1](agents/claude-fable-5.md) (Sept 1) and [GPT-6 Astra](agents/gpt-6-astra.md) (Sept 3) still both list at **$10 / $50**, but three weeks later Anthropic shipped **Claude Opus 5.5** at **$4 / $20** claiming Fable-5.1-level work at 40% less to run, and OpenAI shipped **GPT-6 Sol** at **$2 / $10** and **GPT-6 Luna** at **$0.10 / $0.50**. Both vendors now price cache reads at **$0.20/M**, so the column this map spent the quarter pointing at no longer separates them; **long-context shape** does — Anthropic bills its 1M window at standard rates, OpenAI reprices the whole request past 272k input tokens. [Claude Code](agents/claude-code.md) `v2.1.280` made Opus 5.5 the default Opus model the same day, the second default-model change inside a patch release this map has recorded in a month. See [cost & benchmarks](comparisons/cost-and-benchmarks.md).
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
| Runtime and tools | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [Graft](agents/graft.md), [CLI-Anything](agents/cli-anything.md) | Teams that need workflow automation, code execution, LLM gateways, agent context infrastructure, agent-driven CLIs, or visual builders |
| Observability and evals | [Langfuse](agents/langfuse.md) | Someone whose agents already run in production and needs to know what they did, what they cost, and whether quality is drifting (see [observability & evaluation](comparisons/observability-and-evals.md)) |
| Browser agent | [Browser Use](agents/browser-use.md) | Someone whose task lives on a website with no API — a different question from how an agent edits files, because it decides what an agent may do as you on the open web |
| Self-hosted / local runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md), [OpenHuman](agents/openhuman.md) | Users who need on-device privacy, long-running agents, local control, channels, devices, or personal-data life integration |

## Current Mainstream Coverage

78 profiled projects, grouped by what they are. Expand a group, or browse the full route/coverage tables in [agents/](agents/README.md).

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
<summary><strong>Frameworks and infrastructure</strong> (20 projects)</summary>

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
| [Graft](agents/graft.md) | Runtime and tools | Code context written as linked markdown in your repo, wired into eight-plus agents with one command |
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