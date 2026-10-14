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

> **Last updated:** 2026-10-14 · **Snapshot window:** 2026-10-07 → 2026-10-14 (gain since last update, **7 days** against last window's 7, so the two columns compare directly for the first time since 09-17) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(=) | [mattpocock/skills](https://github.com/mattpocock/skills) | 290.4k | +11,878 | Watchlist (Skills Wave) | **Holds #1**, its 14th in 26 recorded windows, on a gain up **83%** — the largest it has posted in any 7-day window (previous best 11,147 on 06-24). Past **290k**, and 7,315 clear of #2 (last window: 1,626) |
| #2&nbsp;(=) | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 249.4k | +4,563 | In scope · [profile](agents/deepseek-harness.md) | Down 6%, a fourth straight slowdown since its 09-17 peak and the lowest of its six measured windows — but still the only project besides #1 above 4,000. Past **245k**. A `v0.2.1-alpha.2` pre-release (Oct 9) did not move the rate |
| #3&nbsp;(↑) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 106.4k | +4,172 | Watchlist (Skills Wave) | Up **78%**, its largest gain since 08-12 (+4,664) and a second straight acceleration. Past **105k**. Only a bug-fix release (0.6.13, Oct 13) in the window; no documented cause |
| #4&nbsp;(↑) | [Open Code Review](https://github.com/alibaba/open-code-review) | 47.1k | +2,966 | In scope · [profile](agents/open-code-review.md) | Up **93%**, its first acceleration since the 09-17 Trending peak, ending three straight slowdowns. Past **45k**; now ~8x its pre-Trending ~370/week. **v1.13.0** (Oct 13) added reviews on a ChatGPT plan and an ACP server, but landed on the window's last day |
| #5&nbsp;(↓) | [Superpowers](https://github.com/obra/superpowers) | 298.9k | +2,756 | In scope · [profile](agents/superpowers.md) | Down 13% after one acceleration. **1,126 short of 300k** |
| #6&nbsp;(↓) | [Pi](https://github.com/earendil-works/pi) | 115.1k | +1,992 | In scope · [profile](agents/pi.md) | Down 25% — the v1.0.0 release window gave back part of its 56% jump, but the rate is still above the ~1,710/week it ran before the release. Past **115k** |
| #7&nbsp;(↓) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 253.6k | +1,857 | In scope · [profile](agents/hermes-agent.md) | Up 8%, its first acceleration after five straight slowdowns since 09-06. **Present in all 26 recorded windows**, still the only project that has never missed one |
| #8&nbsp;(↑) | [OpenCode](https://github.com/anomalyco/opencode) | 213.4k | +1,289 | In scope · [profile](agents/opencode.md) | Up 9%, its first acceleration since it entered tracking (four straight slowdowns ended). **v1.19.0** (Oct 11) added `opencode upgrade --major` toward OpenCode 2 and turned auto-updates off |
| #9&nbsp;(new) | [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 51.9k | +1,200 | Watchlist (Skills Wave) | First seat since 09-06 — its 11th in 26 windows — on a second straight acceleration (+47%). The other research collection, K-Dense, accelerated too (+40%, 14th), ending six straight slowdowns |
| #10&nbsp;(new) | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 111.1k | +1,078 | Watchlist (finance vertical) | First seat since 09-17, its 14th in 26 windows, on a rate up 39%. It took the seat from Claude Code by **10 stars** (1,078 against 1,068) |

- Heat is useful for discovery, not for selection by itself.
- **This window is 7 days against last window's 7**, so for the first time since 09-17 the two gain columns compare directly; no weekly-rate conversion is applied below.
- **The board warmed: 38 of 55 measured repos accelerated, 17 slowed** — an exact inversion of last window's 17 and 38. Seven of the top ten sped up (last window six). The ten seats together gained 33,751 against 26,421, up 28%, while the bar for #10 barely moved (1,084 → 1,078).
- **[mattpocock/skills](https://github.com/mattpocock/skills) posted its largest 7-day gain on record, +11,878**, up 83%, and holds #1 for a second window — its 14th in 26. Only two of its windows ever beat this raw figure, and both were longer than seven days (the 15-day catch-up window of 08-27 and the 8-day 07-22); its fastest weekly *rate* remains the 5-day 09-06 window (~14,600/week). It out-gained the other three general collections combined (Superpowers +2,756, addyosmani +4,172, anthropics/skills +1,051 = 7,979) by **3,899** — last window the margin was 9 stars. One repository took 35% of the top ten's combined gain. **No trigger is documented**: no release in the window (the latest, v1.3.1 on Oct 4, listed the skills as a native Claude Code plugin in the official marketplace), an Oct 8 README rewrite around one-command installs, and no Hacker News story.
- **[DeepSeek Harness](agents/deepseek-harness.md) slowed for a fourth straight window** (−6%, the lowest of its six measured gains) and the gap to #1 widened from 1,626 to 7,315. It is still the only project other than #1 gaining more than 4,000 a week, and it crossed 245k. An `dsh-v0.2.1-alpha.2` pre-release landed on Oct 9 (thought-translation and Git-worktrees plugins, a `working_directory` tool); it shows up nowhere in the rate.
- **Two of last window's decliners reversed hard.** [Open Code Review](agents/open-code-review.md) nearly doubled (+93%) to #4, its first acceleration since the Trending spike of 09-17 ended three straight slowdowns; it crossed 45k and is now ~8x its pre-Trending ~370/week. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) rose 78% to #3 and crossed 105k. Neither has a documented cause: Open Code Review's v1.13.0 (reviews on a ChatGPT subscription, an Agent Client Protocol server) shipped on Oct 13, the window's last day; addyosmani's 0.6.13 is a bug-fix release.
- **The spike rule paid out again.** [OpenHuman](agents/openhuman.md), last window's ~12x jump with no documented cause, gave back **65%** (1,326 → 468) and fell from #8 to 23rd — its second spike to collapse within a window (the 09-01 one gave back 84%). [CodeGraph](agents/codegraph.md)'s +91% did not hold either (−30%, 18th), and [CLI-Anything](agents/cli-anything.md) fell a second straight window (−25%, 22nd), back near its pre-spike ~400/week.
- **[Claude Code](agents/claude-code.md) lost its seat by 10 stars** (1,068 against TradingAgents' 1,078, −1%) and sits 11th — but it **crossed 150k** (150,741; last window 327 short). Its window shipped `v2.1.293`–`v2.1.299`: Haiku 5.5 added as the API's default Haiku model (Oct 7), and `v2.1.296` (Oct 9) repriced Sonnet 5.5 cache reads in its cost accounting to **$0.10/M, "was $0.20"** — see the model-layer bullet below. Its own default models did not change.
- **The skills wave rose to 4 of 10** (#1, #3, #5, #9), from 3. The fourth seat is [academic-research-skills](https://github.com/Imbad0202/academic-research-skills), the first research collection on the board since 09-06; both research collections accelerated this window (K-Dense +40% after six straight slowdowns), so the split this board recorded on 10-07 closed. The other six seats are all agents; no infra project is on the board.
- **The model layer had its busiest week since September 22, and one price this map recorded has changed under it.** (1) Anthropic shipped **Claude Haiku 5.5** (`claude-haiku-5-5`) on **Oct 7**: $0.10 / $0.50 for prompts up to 100K tokens, $0.50 / $2.50 above that, cache reads $0.01 / $0.05, 1M context. (2) Google opened **Gemini 4 Argon** (`gemini-4-argon`) to the paid API on **Oct 13** — the gate recorded on 09-30 is lifted for the mitigated model; the no-guardrails build stays with the Fairwind Program — at **$2 / $10 through Nov 30, then $4 / $20**, cached input 95% off, not on the Free tier or the AI Pro plan. (3) Anthropic's pricing page now lists **Sonnet 5.5 cache reads at $0.10/M**, not the $0.20 this map recorded from the Sept 28 changelog; Claude Code `v2.1.296` corrected its own figure on Oct 9. That removes the one column that separated Sonnet 5.5 from GPT-6.1 Sol — both mid tiers are now $2 / $10 / $0.10. All three are in [cost & benchmarks](comparisons/cost-and-benchmarks.md) and [market-events](market-events.md). **No coding agent changed its default model for a second window**: [Codex CLI](agents/codex.md) `rust-v0.161.0` (Oct 7) carries the GPT-6.1 Sol default to the main release line, the same change `rust-v0.159.1` back-ported on Sept 29; [Gemini CLI](agents/gemini-cli.md) `v0.64.0` (Oct 13) and [OpenCode](agents/opencode.md) `v1.19.0` kept theirs.
- **Two tracked repositories moved, and both are re-keyed this refresh.** `trailhq/Graft` is now **`trailhq/Trail-Code`** — the README banner reads "Trail-code (previously graft)", and a Trail "learnings" layer (`.trail/learnings/`, `trail check`) sits in front of the unchanged `graft` CLI; the [profile](agents/graft.md) carries a dated note, and the repo is **11 stars short of 10k** (9,989, +340, up 42%). `Hmbown/CodeWhale` had already become **`codewhale-hq/Codewhale`** before the 10-07 fetch, which this map did not notice last window; its README now says "provider-neutral … not affiliated with any model provider" with 40+ provider routes, so the [CodeWhale](agents/codewhale.md) profile's "DeepSeek + MiMo native" framing is corrected in place. **[ZCode](agents/zcode.md)'s first measured week is +317** (7,804).
- Milestones, checked against the raw counts rather than the rounded column: mattpocock/skills crossed **290k**, DeepSeek Harness **245k**, addyosmani/agent-skills **105k**, [anthropics/skills](https://github.com/anthropics/skills) **180k** (181,024 — last window 27 short), Pi **115k**, Claude Code **150k**, [Cline](agents/cline.md) **70k** and Open Code Review **45k**. Three near misses: Superpowers is **1,126 short of 300k**, Trail Code 11 short of 10k, and [anthropics/financial-services](https://github.com/anthropics/financial-services) 216 short of 40k.
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 391.9k stars (+404, down 45%); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.

<details>
<summary>More window notes: skills-wave share, OpenClaw, and everything growing outside the top 10</summary>

- The `.claude/skills` wave **holds four of the top ten**, up from three: #1, #3, #5 and #9. Three are general collections; the fourth, [academic-research-skills](https://github.com/Imbad0202/academic-research-skills), is the first vertical collection on the board since financial-services on 09-30 and the first research one since 09-06. [mattpocock/skills](https://github.com/mattpocock/skills) at +11,878 out-gained the other general collections combined (+2,756 Superpowers, +4,172 addyosmani, +1,051 anthropics/skills = 7,979) by 3,899 — the second straight window the "one directory is the wave" read holds, and this time by a margin that is not a rounding error. Policy unchanged: curated collections are tracked as Skills Wave entries, the framework end is covered through [Superpowers](agents/superpowers.md).
- Just off the table: [Claude Code](agents/claude-code.md) 150.7k (+1,068) at 11th, ten stars behind #10; [anthropics/skills](https://github.com/anthropics/skills) 181.0k (+1,051) at 12th, up 7% and past 180k; [Codex CLI](agents/codex.md) 129.2k (+1,048) at 13th, up 14% and its first acceleration after four straight slowdowns; [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 48.8k (+978) at 14th; and [LiteLLM](agents/litellm.md) 61.2k (+956) at 15th, up **150%** from +383 — the largest percentage jump of any repo gaining more than 500 this window, with no cause checked. OpenClaw is excluded from the board, so these off-board positions are counted the same way.
- **[anthropics/financial-services](https://github.com/anthropics/financial-services) re-accelerated** (+896, up 36%, 16th) after two windows of fading, with zero commits since Sept 21 and no release; it runs at ~8.5x its old ~105/week baseline and is 216 short of 40k. Still no documented cause.
- **[AutoGPT](agents/autogpt.md) lost 116 stars**, the only negative week on the board and the first three-digit loss in the raw record (13 fetches since 07-16; the only earlier negative was Flowise's −6 last window). Possible reasons include GitHub removing accounts, but this map has no evidence either way.
- Continuing to grow but outside the top 10 by gain (raw 7-day figures): [Claude Code](agents/claude-code.md) 150.7k (+1,068), [anthropics/skills](https://github.com/anthropics/skills) 181.0k (+1,051), [Codex CLI](agents/codex.md) 129.2k (+1,048), [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 48.8k (+978), [LiteLLM](agents/litellm.md) 61.2k (+956), [anthropics/financial-services](https://github.com/anthropics/financial-services) 39.8k (+896), [OpenHands](agents/openhands.md) 90.9k (+718), [CodeGraph](agents/codegraph.md) 74.0k (+682), [Browser Use](agents/browser-use.md) 117.9k (+604), [Ruflo](agents/ruflo.md) 74.6k (+594), [n8n](agents/n8n.md) 207.3k (+546), [CLI-Anything](agents/cli-anything.md) 52.1k (+486), [OpenHuman](agents/openhuman.md) 42.0k (+468), [LangGraph](agents/langgraph.md) 43.2k (+442), [jcode](agents/jcode.md) 20.7k (+376), [Langfuse](agents/langfuse.md) 35.8k (+345), [Trail Code (Graft)](agents/graft.md) 10.0k (+340), [Cline](agents/cline.md) 70.3k (+334), [ZCode](agents/zcode.md) 7.8k (+317), [LangChain](agents/langchain.md) 147.8k (+313), [CrewAI](agents/crewai.md) 59.7k (+270), [Goose](agents/goose.md) 55.3k (+251), [mini-swe-agent](agents/mini-swe-agent.md) 8.5k (+249), [agentmemory](https://github.com/rohitg00/agentmemory) 29.4k (+211), [Omnigent](agents/omnigent.md) 10.8k (+168), [TrueForge](agents/trueforge.md) 6.2k (+152), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) 14.1k (+144), [Aider](agents/aider.md) 49.5k (+138), [Qwen Code](agents/qwen-code.md) 28.5k (+136), [Grok Build](agents/grok-build.md) 27.4k (+118), [Gemini CLI](agents/gemini-cli.md) 107.3k (+101), [12-factor-agents](https://github.com/humanlayer/12-factor-agents) 26.7k (+99), [Kimi Code](agents/kimi-code.md) 7.9k (+81), [eve](agents/eve.md) 5.6k (+80), [Continue](agents/continue.md) 36.2k (+76), [Letta (MemGPT)](agents/memgpt.md) 25.1k (+65), [OpenHarness](agents/openharness.md) 16.0k (+64), [LlamaIndex](agents/llamaindex.md) 52.5k (+62), [Open Interpreter](agents/open-interpreter.md) 68.6k (+54), [SWE-agent](agents/swe-agent.md) 20.5k (+53), [MiMoCode](agents/mimocode.md) 13.7k (+52), [QM](agents/qm.md) 15.4k (+51), [CodeWhale](agents/codewhale.md) 41.1k (+18), [Flowise](agents/flowise.md) 55.5k (+11), [CoStrict](agents/costrict.md) 4.4k (+3)

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

- **The `.claude/skills` wave is back to four seats, and one directory is most of it** (May 2026 → ongoing): curated skill collections and skills frameworks have held between two and six of the weekly heat top 10 for five months, and the count rotates rather than sitting still — 6/10, then 2/10, 3/10, 4/10, 5/10, 3/10, now **4 of 10** (2026-10-14). The fourth seat is a research collection, [academic-research-skills](https://github.com/Imbad0202/academic-research-skills), back for the first time since 09-06; the core remains [mattpocock/skills](https://github.com/mattpocock/skills), [Superpowers](agents/superpowers.md) and [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills). mattpocock posted its largest 7-day gain on record (+11,878) and out-gained the other three general collections combined by 3,899 — last window the margin was 9 stars — so the key-person risk this map has flagged since June is back in full. This map profiles the framework end through [Superpowers](agents/superpowers.md) and tracks collections on the [skill boards](rankings/skill-verticals.md).
- **The model layer became a budget decision — and the ladder now has every rung filled at both vendors**: [Claude Fable 5.1](agents/claude-fable-5.md) (Sept 1) and [GPT-6 Astra](agents/gpt-6-astra.md) (Sept 3) still both list at **$10 / $50**; below them sit **Opus 5.5** ($4 / $20, Sept 22), the two mid tiers **Sonnet 5.5** and **GPT-6.1 Sol** (both $2 / $10, Sept 28–29, both their vendor's coding-agent default), and now the floor: **GPT-6 Luna** ($0.10 / $0.50, Sept 22) and **Claude Haiku 5.5** (Oct 7, $0.10 / $0.50 for prompts up to 100K tokens, $0.50 / $2.50 above). Google joined the priced field on **Oct 13** when **Gemini 4 Argon** opened to the paid API at $2 / $10 through Nov 30, then $4 / $20. The column this map said separated the two mid tiers has closed: Anthropic's pricing page now lists Sonnet 5.5 cache reads at **$0.10/M**, not the $0.20 recorded from the Sept 28 changelog (Claude Code `v2.1.296` corrected its own figure on Oct 9), so Sonnet 5.5 and GPT-6.1 Sol are identical on sticker and on cache. What still separates them is long-context shape (OpenAI reprices the whole request past 272k input tokens; Anthropic does not; Haiku 5.5 prices by prompt length). See [cost & benchmarks](comparisons/cost-and-benchmarks.md).
- **Product boundaries are collapsing upward**: OpenAI merged Codex into the ChatGPT app (July 9), and at DevDay (Sept 29) moved it further off the laptop with reusable cloud environments usable from any device — on the OpenAI side, "which coding agent" keeps turning into "how you use ChatGPT." The bundled default model changed twice in a month: [GPT-6 Astra](agents/gpt-6-astra.md) from `rust-v0.153.4` (Sept 4), then **GPT-6.1 Sol** from `rust-v0.159.1` (Sept 29), carried to the main release line by `rust-v0.161.0` (Oct 7). Two windows have now passed with no tracked coding agent changing a default. If you run Codex on defaults, pin the model id anyway; the product will not hold it still for you. See [Codex](agents/codex.md).

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
| Runtime and tools | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [Trail Code (Graft)](agents/graft.md), [CLI-Anything](agents/cli-anything.md) | Teams that need workflow automation, code execution, LLM gateways, agent context infrastructure, agent-driven CLIs, or visual builders |
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
| [Trail Code (Graft)](agents/graft.md) | Runtime and tools | Code context written as linked markdown in your repo, wired into eight-plus agents with one command |
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