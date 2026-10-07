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

> **Last updated:** 2026-10-07 · **Snapshot window:** 2026-09-30 → 2026-10-07 (gain since last update, **7 days** against last window's 6, so the two columns are not directly comparable; every claim below is stated on the **weekly rate**) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(↑) | [mattpocock/skills](https://github.com/mattpocock/skills) | 278.5k | +6,506 | Watchlist (Skills Wave) | **Back at #1**, its 13th in 25 recorded windows, on a rate up **57%** — its first acceleration after four straight slowdowns since 09-06. Past **275k**, and 1,626 clear of #2 |
| #2&nbsp;(↓) | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 244.8k | +4,880 | In scope · [profile](agents/deepseek-harness.md) | Its #1 lasted one window. Rate down **26%**, the lowest of its five measured windows and its third straight slowdown. Past **240k** |
| #3&nbsp;(↑) | [Superpowers](https://github.com/obra/superpowers) | 296.1k | +3,175 | In scope · [profile](agents/superpowers.md) | Rate up 20%, its first acceleration since 09-17. Past **295k** |
| #4&nbsp;(↑) | [Pi](https://github.com/earendil-works/pi) | 113.1k | +2,672 | In scope · [profile](agents/pi.md) | Rate up **56%** in the window it shipped **v1.0.0** (Oct 1), more than reversing last window's 30% drop and ending four consecutive windows at #6. Back at #4 for the first time since 09-06 |
| #5&nbsp;(↑) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 102.3k | +2,343 | Watchlist (Skills Wave) | **Crossed 100k** (102,252), on a rate up 68% |
| #6&nbsp;(↓) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 251.8k | +1,719 | In scope · [profile](agents/hermes-agent.md) | Rate down 11%, a fifth straight slowdown since its 09-06 peak. **Present in all 25 recorded windows**, still the only project that has never missed one |
| #7&nbsp;(↓) | [Open Code Review](https://github.com/alibaba/open-code-review) | 44.1k | +1,533 | In scope · [profile](agents/open-code-review.md) | Rate down **45%**, a third straight slowdown. It did not level off near last window's ~2,800/week; it is now ~4x its pre-Trending ~370/week |
| #8&nbsp;(new) | [OpenHuman](https://github.com/tinyhumansai/openhuman) | 41.5k | +1,326 | In scope · [profile](agents/openhuman.md) | Back on the board for the first time since 09-01 — its fourth seat in 25 windows — on a rate **~12x** last window's ~112/week, its fastest since 09-01. **No documented cause**: a release (v0.64.10) landed on Sept 30 and the repo now describes itself as an "agent harness", but neither explains a 12x week. Its last spike (08-27 → 09-01) was gone a window later |
| #9&nbsp;(↓) | [OpenCode](https://github.com/anomalyco/opencode) | 212.1k | +1,183 | In scope · [profile](agents/opencode.md) | Rate down 18%, its fourth straight slowdown since its first measured window |
| #10&nbsp;(new) | [Claude Code](https://github.com/anthropics/claude-code) | 149.7k | +1,084 | In scope · [profile](agents/claude-code.md) | Its second top-ten seat, after 09-24. Rate up 19% to ~1,084/week, just above the 610–1,030 range of its pre-Opus-5.5 windows — it gets the seat mostly because the bar for #10 dropped to meet it. 327 short of 150k |

- Heat is useful for discovery, not for selection by itself.
- **This window is 7 days against last window's 6.** The raw gains in the two columns are not directly comparable, so every claim here is on the **weekly rate** (this window: the gain as printed; last window: gain ÷ 6 × 7).
- **The board warmed slightly: 17 of 55 measured repos accelerated, 38 slowed** (last window 13 and 42). Six of the top ten sped up, against one last window. The entry bar for #10 fell anyway, from 1,166 to 1,084 — 6 days' gain against 7 days', so on the weekly rate it fell from ~1,360 to ~1,084.
- **[mattpocock/skills](https://github.com/mattpocock/skills) took #1 back after one window**, on its fastest rate since 09-06. It is its 13th #1 in 25 recorded windows. It also out-gained the other general collections combined for the first time in four windows — by **9 stars** (+6,506 against Superpowers +3,175, addyosmani +2,343 and anthropics/skills +979 = 6,497), which is a tie in all but name.
- **[DeepSeek Harness](agents/deepseek-harness.md)'s #1 did not survive a second window.** Last window this board said the seat came to it rather than being taken; that is how it left, too — its rate fell 26% to ~4,880/week, the lowest of its five measured windows and a third straight slowdown since its 09-17 peak of ~8,800. It is still #2, and still ~4,900 a week.
- **Last window's open questions all resolved the same way: down.** [anthropics/financial-services](https://github.com/anthropics/financial-services) fell **56%** to ~661/week and off the board to 17th — still ~6x its old ~105/week baseline, so the spike is fading rather than gone. [CLI-Anything](agents/cli-anything.md)'s tripled rate gave back **49%** (~1,265 → ~651/week, 18th), so it was a spike, as this board's one-window rule assumed. [Open Code Review](agents/open-code-review.md) did not level off near ~2,800/week as last window suggested; it fell another 45% to #7.
- **[OpenHuman](agents/openhuman.md) is this window's spike.** It went from ~112 to 1,326 a week — roughly 12x — and returned at #8 after five windows off. Nothing documented explains it: there is a Sept 30 release and a new self-description as an "agent harness", no Hacker News post, and issue/PR activity actually fell week over week. Forks jumped on Oct 6 and were spread across the whole day, which looks like a listing rather than a single post — an inference, not a finding. The board's one-window rule applies in full, and OpenHuman has form: its 08-27 → 09-01 spike gave back 84% the next window.
- **[Claude Code](agents/claude-code.md) is back at #10**, its second seat. Unlike its first (09-24, the Opus 5.5 release window), there is no matching release spike this time: the rate rose 19%, to just above its pre-Opus-5.5 range. Read it as the bar for #10 dropping to meet it, not a new baseline.
- The skills wave fell to **3 of 10** (#1, #3, #5), from 5 — both `anthropics/*` collections left the table, anthropics/skills slowing 28% to a tie for 11th and financial-services fading as described above. The three that remain are the three general collections that have carried the wave since June: [mattpocock](https://github.com/mattpocock/skills), [Superpowers](agents/superpowers.md) and [addyosmani](https://github.com/addyosmani/agent-skills).
- **A quiet week for default models, a release week for [Pi](agents/pi.md).** No coding agent tracked here changed its default model this window (checked: [Claude Code](agents/claude-code.md) `2.1.285`–`2.1.292`, [Codex CLI](agents/codex.md) `rust-v0.160.0`/`.1`, [Gemini CLI](agents/gemini-cli.md) `v0.63.0`, [OpenCode](agents/opencode.md) `v1.18.35`), ending September's run of four. Haiku 5.5 has still not shipped. Google announced **Gemini 4 Argon** on Sept 30 at **$2 / $10** introductory ($4 / $20 after), but it is gated to Google's cyber-defender program for now, so it stays in [market-events](market-events.md) rather than the cost table until it can be bought. Pi shipped **v1.0.0 on Oct 1** — fullscreen TUI by default and, per its release notes, about 40% fewer prompt tokens in codemode — in the same window its rate rose 56%.
- **Pending pickup: [ZCode](agents/zcode.md) entered tracking** at **7,487** stars (`zai-org/ZCode`, open-sourced on September 20). Its first measured gain lands next window. **[Graft](agents/graft.md)'s first measured week is +240** (9.6k).
- Milestones, checked against the raw counts rather than the rounded column: mattpocock/skills crossed **275k**, DeepSeek Harness **240k**, Superpowers **295k**, addyosmani/agent-skills **100k**, [TradingAgents](https://github.com/TauricResearch/TradingAgents) **110k**, [LiteLLM](agents/litellm.md) **60k**, [Goose](agents/goose.md) **55k** and [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) **50k**. Two near misses: [anthropics/skills](https://github.com/anthropics/skills) shows as 180.0k but is **27 short** (179,973), and Claude Code is 327 short of 150k.
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 391.5k stars (+738, rate up 41%); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.

<details>
<summary>More window notes: skills-wave share, OpenClaw, and everything growing outside the top 10</summary>

- The `.claude/skills` wave **holds three of the top ten**, down from five: #1, #3 and #5. All three are general collections; no vendor or vertical collection is on the board this window. [mattpocock/skills](https://github.com/mattpocock/skills) at +6,506 edges the other general collections combined (+3,175 Superpowers, +2,343 addyosmani, +979 anthropics/skills = 6,497) by 9 stars — the first window since 09-09 that the old "one directory is the wave" read is even arithmetically true, and too close to call a reversal. Policy unchanged: curated collections are tracked as Skills Wave entries, the framework end is covered through [Superpowers](agents/superpowers.md).
- Just off the table: [CodeGraph](agents/codegraph.md) 73.4k (+979) and [anthropics/skills](https://github.com/anthropics/skills) 180.0k (+979) **tied for 11th**, CodeGraph on a rate up 91%; [Codex CLI](agents/codex.md) 128.1k (+923) at 13th, a fourth straight slowdown; [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 50.7k (+814) at 14th; and [TradingAgents](https://github.com/TauricResearch/TradingAgents) 110.0k (+777) at 15th. OpenClaw is excluded from the board, so these off-board positions are counted the same way.
- **The two research collections split.** [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) accelerated 16%, ending a run of four slowdowns since its 09-06 peak. [K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills) (−24%, 47.8k) slowed for a **sixth consecutive window** since its 09-01 peak and now runs at well under a tenth of it.
- **[eve](agents/eve.md) and [TrueForge](agents/trueforge.md) both slowed** (eve +65, −24%; TrueForge +58, −36%). At these sizes a few dozen stars is noise. [Flowise](agents/flowise.md) lost 6 stars, the only tracked repo with a negative week.
- Continuing to grow but outside the top 10 by gain (raw 7-day figures): [CodeGraph](agents/codegraph.md) 73.4k (+979), [anthropics/skills](https://github.com/anthropics/skills) 180.0k (+979), [Codex CLI](agents/codex.md) 128.1k (+923), [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 50.7k (+814), [TradingAgents](https://github.com/TauricResearch/TradingAgents) 110.0k (+777), [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 47.8k (+699), [anthropics/financial-services](https://github.com/anthropics/financial-services) 38.9k (+661), [CLI-Anything](agents/cli-anything.md) 51.7k (+651), [OpenHands](agents/openhands.md) 90.1k (+604), [Browser Use](agents/browser-use.md) 117.3k (+581), [Ruflo](agents/ruflo.md) 74.0k (+508), [n8n](agents/n8n.md) 206.8k (+486), [Cline](agents/cline.md) 70.0k (+390), [LiteLLM](agents/litellm.md) 60.3k (+383), [LangGraph](agents/langgraph.md) 42.8k (+330), [Omnigent](agents/omnigent.md) 10.6k (+287), [Langfuse](agents/langfuse.md) 35.5k (+256), [Goose](agents/goose.md) 55.0k (+244), [LangChain](agents/langchain.md) 147.5k (+244), [Graft](agents/graft.md) 9.6k (+240), [CrewAI](agents/crewai.md) 59.4k (+214), [agentmemory](https://github.com/rohitg00/agentmemory) 29.2k (+169), [mini-swe-agent](agents/mini-swe-agent.md) 8.3k (+164), [Aider](agents/aider.md) 49.4k (+123), [12-factor-agents](https://github.com/humanlayer/12-factor-agents) 26.6k (+115), [Qwen Code](agents/qwen-code.md) 28.3k (+115), [jcode](agents/jcode.md) 20.3k (+113), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) 14.0k (+113), [Grok Build](agents/grok-build.md) 27.2k (+96), [Letta (MemGPT)](agents/memgpt.md) 25.1k (+91), [Continue](agents/continue.md) 36.1k (+78), [QM](agents/qm.md) 15.4k (+72), [LlamaIndex](agents/llamaindex.md) 52.4k (+65), [eve](agents/eve.md) 5.5k (+65), [AutoGPT](agents/autogpt.md) 187.7k (+64), [TrueForge](agents/trueforge.md) 6.1k (+58), [SWE-agent](agents/swe-agent.md) 20.5k (+49), [Kimi Code](agents/kimi-code.md) 7.8k (+48), [MiMoCode](agents/mimocode.md) 13.6k (+45), [Gemini CLI](agents/gemini-cli.md) 107.2k (+45), [Open Interpreter](agents/open-interpreter.md) 68.5k (+44), [OpenHarness](agents/openharness.md) 15.9k (+33), [CodeWhale](agents/codewhale.md) 41.1k (+28), [CoStrict](agents/costrict.md) 4.4k (+8)

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

- **The `.claude/skills` wave still holds a large share of the board, but it is down to its three core general collections** (May 2026 → ongoing): curated skill collections and skills frameworks have held between two and six of the weekly heat top 10 for four and a half months, and the count rotates rather than sitting still — 6/10, then 2/10, 3/10, 4/10, 5/10, now **3 of 10** (2026-10-07). The two `anthropics/*` collections that lifted it to five last window both left the table; what remains is [mattpocock/skills](https://github.com/mattpocock/skills) (back at #1), [Superpowers](agents/superpowers.md) and [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), which crossed 100k. mattpocock out-gained the other general collections combined this window for the first time since 09-09 — but by 9 stars (+6,506 against +6,497), so read the key-person risk as unresolved rather than returning. This map profiles the framework end through [Superpowers](agents/superpowers.md) and tracks collections on the [skill boards](rankings/skill-verticals.md).
- **The model layer became a budget decision — and in September both vendors moved their coding agents down the ladder**: [Claude Fable 5.1](agents/claude-fable-5.md) (Sept 1) and [GPT-6 Astra](agents/gpt-6-astra.md) (Sept 3) still both list at **$10 / $50**, but on September 22 Anthropic shipped **Claude Opus 5.5** at **$4 / $20** and OpenAI **GPT-6 Sol** at **$2 / $10** and **GPT-6 Luna** at **$0.10 / $0.50**. A week later both mid tiers turned over again: **Claude Sonnet 5.5** (Sept 28) and **GPT-6.1 Sol** (Sept 29), both at **$2 / $10**, and each became its vendor's coding-agent default — [Claude Code](agents/claude-code.md) `2.1.284` and [Codex CLI](agents/codex.md) `rust-v0.159.1`. That is four default-model changes inside a patch release in one month. With the mid-tier stickers identical, **cache read is the column that separates them again** — $0.10/M for GPT-6.1 Sol against $0.20/M for Sonnet 5.5, one week after the two vendors had converged on $0.20 — along with long-context shape (OpenAI reprices the whole request past 272k input tokens; Anthropic does not). See [cost & benchmarks](comparisons/cost-and-benchmarks.md).
- **Product boundaries are collapsing upward**: OpenAI merged Codex into the ChatGPT app (July 9), and at DevDay (Sept 29) moved it further off the laptop with reusable cloud environments usable from any device — on the OpenAI side, "which coding agent" keeps turning into "how you use ChatGPT." The bundled default model changed twice in a month: [GPT-6 Astra](agents/gpt-6-astra.md) from `rust-v0.153.4` (Sept 4), then **GPT-6.1 Sol** from `rust-v0.159.1` (Sept 29). If you run Codex on defaults, pin the model id; the product will not hold it still for you. See [Codex](agents/codex.md).

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