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

> **Last updated:** 2026-10-28 · **Snapshot window:** 2026-10-21 → 2026-10-28 (gain since last update, **7 days** against last window's 7, so the two columns compare directly for a third straight week) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(↑) | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 263.5k | +7,011 | In scope · [profile](agents/deepseek-harness.md) | **Takes #1** for the second time (first: 09-30), on a gain down just 1%: the steadiest large grower on the board, promoted because mattpocock/skills slowed. Its third 7-day gain above 7,000. Past **260k**, and now 5,868 ahead of Hermes Agent in total stars. One pre-release in the window (`dsh-v0.2.1-rc.3`, Oct 23) |
| #2&nbsp;(↓) | [mattpocock/skills](https://github.com/mattpocock/skills) | 304.7k | +5,483 | Watchlist (Skills Wave) | Down **38%** and off #1 after three windows. **Crossed 300k** (304,687), but at 1,457 behind [Superpowers](agents/superpowers.md) it did *not* pass it, as last window's pace suggested it would. For the first time since 09-30 it gained less than the other three general collections combined. No release |
| #3&nbsp;(new) | [TradingAgents](https://github.com/TauricResearch/TradingAgents) | 117.1k | +4,677 | Watchlist (finance vertical) | Up **250%**, from 14th to #3: its best seat and largest gain since its #1 on 05-08, and its 15th seat in 28 windows. Past **115k**. One release, `v0.7.1` (Oct 27), a bug-fix release; nothing documented ties it to the gain, so it is treated as a spike |
| #4&nbsp;(↑) | [Superpowers](https://github.com/obra/superpowers) | 306.1k | +3,310 | In scope · [profile](agents/superpowers.md) | Down 16%, still at #4. Past **305k** (306,144), 1,457 ahead of mattpocock/skills. One release, `v7.0.1` (Oct 21) |
| #5&nbsp;(↓) | [OpenCode](https://github.com/anomalyco/opencode) | 222.3k | +2,841 | In scope · [profile](agents/opencode.md) | Down **53%** after last window's 2.0 breakout, but kept a seat. Past **220k**. `v2.2.0` shipped Oct 27 |
| #6&nbsp;(↑) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 257.7k | +1,918 | In scope · [profile](agents/hermes-agent.md) | Down 9%, up three places because others fell further. **Present in all 28 recorded windows**. Three releases (`v0.22.3`–`v0.22.5`) |
| #7&nbsp;(↑) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 111.0k | +1,906 | Watchlist (Skills Wave) | Down 30%, a second straight slowdown. Past **110k** (111,034). No commit in the window |
| #8&nbsp;(↓) | [Ruflo](https://github.com/ruvnet/ruflo) | 79.7k | +1,653 | In scope · [profile](agents/ruflo.md) | Down **52%** from last window's record, but kept a seat a second window. 20 releases in the window. **285 short of 80k** |
| #9&nbsp;(↓) | [CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 57.4k | +1,597 | In scope · [profile](agents/cli-anything.md) | Down **56%**, kept a seat a second window for the first time; still no commit since Sept 22 and no documented cause |
| #10&nbsp;(new) | [anthropics/skills](https://github.com/anthropics/skills) | 184.2k | +1,556 | Watchlist (Skills Wave) | Up from 12th on a gain down 2%: its first seat since 09-30 and its 17th in 28 windows. **827 short of 185k** |

- Heat is useful for discovery, not for selection by itself.
- **This window is 7 days against last window's 7**, so raw gains compare directly for a third straight week; no weekly-rate conversion is applied below.
- **The board cooled sharply.** Only **15 of 57 measured repos accelerated and 42 slowed** (last window 31 and 24). The ten seats together gained **31,952** against 44,336 (−28%), and the bar for #10 fell **19%** (1,920 → 1,556). Nine of the ten seat-holders slowed; only [TradingAgents](https://github.com/TauricResearch/TradingAgents) sped up.
- **[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) takes #1 for the second time, by holding still.** +7,011 is down just 1% on last window, while [mattpocock/skills](https://github.com/mattpocock/skills) fell 38% to +5,483 and ended a three-window run at #1 (its 15 #1s in 28 windows still lead the board; DeepSeek Harness now has 2). It is the same pattern as its first #1 on 09-30, which also came on a gain that did not rise — and that one lasted a single window. Past 260k; one pre-release (`dsh-v0.2.1-rc.3`, Oct 23).
- **mattpocock/skills crossed 300k but did not catch [Superpowers](agents/superpowers.md).** At 304,687 against 306,144 it is **1,457 behind**, down from 3,630; last window's note that the gap would close "inside a week" at that pace was wrong, because the pace fell. And for the first time since 09-30 it gained **less than the other three general collections combined** (5,483 against 3,310 + 1,906 + 1,556 = 6,772) — so the "one directory is the wave" read that held for three windows does not hold this one.
- **The spike rule paid out on all three of last window's unexplained jumps.** [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) gave back **68%** and left the board (11th, 78 short of 55k); [CLI-Anything](agents/cli-anything.md) gave back **56%** and [Ruflo](agents/ruflo.md) **52%**, though both kept a seat (#9, #8) because the bar fell too. The one documented breakout, [OpenCode](agents/opencode.md), also gave back **53%** (+2,841, #5) and kept its seat; `v2.2.0` shipped Oct 27.
- **This window's own spike is [TradingAgents](https://github.com/TauricResearch/TradingAgents): +4,677, up 250%**, from 14th to #3 — its best seat and largest gain since it held #1 on 05-08, the board's first window. The window's only release, `v0.7.1` (Oct 27), is a bug-fix release (filing dates, settlement across market holidays, SEC statement periods), and nothing first-hand ties it to the gain. By the board's rule it is a spike until a second window confirms it.
- **The skills wave holds 4 of 10** (#2, #4, #7, #10) for a third straight window, with a different fourth seat again: [anthropics/skills](https://github.com/anthropics/skills) returned at #10 (first seat since 09-30) as K-Dense left. The other six seats are four agents (#1, #3, #5, #6) and two infra projects (#8, #9). Hermes Agent (28 of 28 windows), Superpowers and mattpocock/skills (23 each) are the long runs still going; DeepSeek Harness and OpenCode are next at 8.
- **The model layer moved on a new OpenAI tier, a Kimi point release and Anthropic's corporate news, not on defaults.** (1) **OpenAI's GPT-6.1 Terra** (Oct 26) lists at **$1 / $5 with $0.05 cached input** and a 1.05M context, repricing the whole request past 272k input tokens; it reached Codex and ChatGPT Work on Plus and above the same day as a selectable model, not a default. (2) **Moonshot's Kimi K3.1 Pro** (Oct 24 on Moonshot's own index) is on its API at **$2 / $10 with $0.20 cache reads** (a Highspeed variant at $4 / $20); Moonshot says the weights follow by Nov 4, and its quickstart still shows unfilled `[xx.x%]` benchmark placeholders, so no score is recorded here. K2-series models close to new users on Oct 31 and retire by the end of December. (3) **Anthropic donated Agent Skills to the Agentic AI Foundation** (Oct 22), saying more than 70 agent platforms have integrated the standard, and **filed an S-1** for a Nasdaq listing as "ANT" (Oct 26). (4) Anthropic also opened a waitlisted preview of **[Claude Duet](agents/claude-duet.md)** (Oct 21), a separate personal-agent app, profiled this refresh — see [personal agents](comparisons/personal-agents.md#recent-changes). **No tracked coding agent changed its default model for a fourth straight window**: [Claude Code](agents/claude-code.md) `v2.1.307`–`v2.1.311`, [Codex CLI](agents/codex.md) `rust-v0.164.0` (still bundles GPT-6.1 Sol first), [OpenCode](agents/opencode.md) `v2.2.0`, [Qwen Code](agents/qwen-code.md) and [Kimi Code](agents/kimi-code.md); [Gemini CLI](agents/gemini-cli.md) shipped no stable release. **OpenCode's Oct 17 incident now has a vendor statement on record:** its X post says a breach "related to a large scale distillation attack" affected **1.4% of OpenCode Console users**, the subset with external providers linked, all notified by email. Last window this map could not read it; the dated line in the [timeline](agents/README.md) is updated in place. The [cost table](comparisons/cost-and-benchmarks.md) adds GPT-6.1 Terra; every other row was re-checked against the Anthropic, OpenAI, Google and Meta pricing pages and is unchanged, and both promotions (GPT-5.6 Sol to Nov 21, Gemini 4 Argon to Nov 30) are still live. Details in [market-events](market-events.md).
- Milestones, checked against the raw counts rather than the rounded column: **mattpocock/skills 300k**, Superpowers **305k**, DeepSeek Harness **260k**, OpenCode **220k**, TradingAgents **115k**, addyosmani/agent-skills **110k**, [CodeGraph](agents/codegraph.md) **75k**, [CrewAI](agents/crewai.md) **60k**, [Omnigent](agents/omnigent.md) **11k** and [Kimi Code](agents/kimi-code.md) **8k**. Near misses: [agentmemory](https://github.com/rohitg00/agentmemory) is **58 short of 30k**, scientific-agent-skills 78 short of 55k, [Aider](agents/aider.md) 228 short of 50k, Ruflo 285 short of 80k, mattpocock/skills 313 short of 305k.
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 393.2k stars (+557, down 21%); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.

<details>
<summary>More window notes: skills-wave share, OpenClaw, and everything growing outside the top 10</summary>

- The `.claude/skills` wave **holds four of the top ten for a third straight window**: #2, #4, #7 and #10 — and for the first time since 08-27 all four are general collections, as [anthropics/skills](https://github.com/anthropics/skills) took the seat [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) gave up. [mattpocock/skills](https://github.com/mattpocock/skills) at +5,483 gained **1,289 less** than the other three combined (+3,310 Superpowers, +1,906 addyosmani, +1,556 anthropics/skills = 6,772), ending a three-window run in which it out-gained them. Policy unchanged: curated collections are tracked as Skills Wave entries, the framework end is covered through [Superpowers](agents/superpowers.md).
- Just off the table: scientific-agent-skills 54.9k (+1,488) at 11th, down 68% (see above); [Pi](agents/pi.md) 118.2k (+1,379) at 12th, down 24%, a second window off; [Gemini CLI](agents/gemini-cli.md) 108.6k (+1,086) at 13th, **up 665%**, its largest gain since tracking began on 09-09 — with no stable release in the window (nightlies only), no default-model change and no documented cause; [CodeGraph](agents/codegraph.md) 75.6k (+1,013) at 14th, up 89% and past 75k; [Codex CLI](agents/codex.md) 131.3k (+1,007) at 15th, down 8%; and [Claude Code](agents/claude-code.md) 153.6k (+908) at 16th, down 53% after last window's seat, on five releases (`v2.1.307`–`v2.1.311`). OpenClaw is excluded from the board, so these off-board positions are counted the same way.
- **The research collections both cooled.** [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) slowed 34% (+889, 17th), and K-Dense, at 54,922 against 54,158, stays the larger of the two. [Open Code Review](agents/open-code-review.md) held level (+723, up 1%, 18th) after last window's 76% drop, about 2x its pre-Trending ~370/week. [anthropics/financial-services](https://github.com/anthropics/financial-services) gave back 69% (+253, 27th).
- Continuing to grow but outside the top 10 by gain (raw 7-day figures): [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 54.9k (+1,488), [Pi](agents/pi.md) 118.2k (+1,379), [Gemini CLI](agents/gemini-cli.md) 108.6k (+1,086), [CodeGraph](agents/codegraph.md) 75.6k (+1,013), [Codex CLI](agents/codex.md) 131.3k (+1,007), [Claude Code](agents/claude-code.md) 153.6k (+908), [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 54.2k (+889), [Open Code Review](agents/open-code-review.md) 48.5k (+723), [n8n](agents/n8n.md) 208.8k (+574), [Browser Use](agents/browser-use.md) 119.3k (+561), [OpenHands](agents/openhands.md) 92.0k (+544), [Langfuse](agents/langfuse.md) 36.6k (+475), [LiteLLM](agents/litellm.md) 62.2k (+453), [LangChain](agents/langchain.md) 148.6k (+368), [LangGraph](agents/langgraph.md) 44.0k (+354), [Goose](agents/goose.md) 55.8k (+338), [anthropics/financial-services](https://github.com/anthropics/financial-services) 40.9k (+253), [Trail Code (Graft)](agents/graft.md) 10.8k (+253), [ZCode](agents/zcode.md) 8.3k (+242), [CrewAI](agents/crewai.md) 60.2k (+225), [Cline](agents/cline.md) 70.9k (+221), [agentmemory](https://github.com/rohitg00/agentmemory) 29.9k (+205), [mini-swe-agent](agents/mini-swe-agent.md) 8.9k (+185), [OpenHuman](agents/openhuman.md) 42.4k (+170), [jcode](agents/jcode.md) 21.2k (+161), [Omnigent](agents/omnigent.md) 11.1k (+134), [Qwen Code](agents/qwen-code.md) 28.8k (+132), [AutoGPT](agents/autogpt.md) 187.8k (+100), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) 14.3k (+97), [LlamaIndex](agents/llamaindex.md) 52.7k (+96), [Aider](agents/aider.md) 49.8k (+91), [OpenHarness](agents/openharness.md) 16.1k (+91), [Kimi Code](agents/kimi-code.md) 8.0k (+89), [Grok Build](agents/grok-build.md) 27.6k (+89), [12-factor-agents](https://github.com/humanlayer/12-factor-agents) 26.9k (+78), [QM](agents/qm.md) 15.5k (+73), [Open Interpreter](agents/open-interpreter.md) 68.7k (+69), [TrueForge](agents/trueforge.md) 6.4k (+68), [eve](agents/eve.md) 5.7k (+67), [Continue](agents/continue.md) 36.3k (+66), [Letta (MemGPT)](agents/memgpt.md) 25.3k (+53), [SWE-agent](agents/swe-agent.md) 20.7k (+48), [MiMoCode](agents/mimocode.md) 13.7k (+38), [CodeWhale](agents/codewhale.md) 41.1k (+30), [Flowise](agents/flowise.md) 55.5k (+18), [CoStrict](agents/costrict.md) 4.5k (+5)

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

Popularity tells you what to look at. These five pages tell you what to pick:

- **[Capability matrix](capabilities/matrix.md)** — every project scored side by side (●/◐/○/—) across the nine shared [capability dimensions](capabilities/README.md), grouped by route. The answer to "for this capability, who treats it as a core strength."
- **[Cost & benchmarks](comparisons/cost-and-benchmarks.md)** — frontier-model capability vs per-token price, plus how each coding agent actually bills. Since the model layer went tiered and metered, "which tier for this task" is the selection decision.
- **[Memory approaches](comparisons/memory-approaches.md)** — seven different things projects mean by "has memory," from self-editing stores to passive semantic recall, and which to pick for what you need to persist.
- **[Consumer personal agents](comparisons/personal-agents.md)** — the agents you hand your day to — ChatGPT dots, Gemini Task, Claude, Muse, Grok Bot, Cue, Doubao, Qwen, AutoGLM, Yuanbao — compared on facts and control rather than popularity, because closed products have no public number to rank by.
- **[Observability & evaluation](comparisons/observability-and-evals.md)** — the layer under everything above: once an agent runs unattended, failure stops looking like a crash and starts looking like silent quality drift. Compares [Langfuse](agents/langfuse.md), Opik, Phoenix, Helicone, LangSmith and others — and untangles the four different things "open source" means in that field.

## Market Pulse

The three structural stories shaping selection right now — full records with dates and sources live in [market-events.md](market-events.md):

- **The `.claude/skills` wave holds four seats, and one directory is most of it** (May 2026 → ongoing): curated skill collections and skills frameworks have held between two and six of the weekly heat top 10 for five months, and the count rotates rather than sitting still — 6/10, then 2/10, 3/10, 4/10, 5/10, 3/10, 4/10, and **4 of 10** again (2026-10-21). The fourth seat is a research collection again, but a different one: [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) (K-Dense) replaced academic-research-skills on an unexplained +373%. The core remains [mattpocock/skills](https://github.com/mattpocock/skills), [Superpowers](agents/superpowers.md) and [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills); Superpowers crossed **300k** and mattpocock is 796 short of it. mattpocock held #1 a third straight window and still out-gained the other three general collections combined, but by 530 stars, down from 3,899 — the key-person risk this map has flagged since June is still there, just less lopsided than last window. This map profiles the framework end through [Superpowers](agents/superpowers.md) and tracks collections on the [skill boards](rankings/skill-verticals.md).
- **The model layer became a budget decision — and the ladder now has every rung filled at both vendors**: [Claude Fable 5.1](agents/claude-fable-5.md) (Sept 1) and [GPT-6 Astra](agents/gpt-6-astra.md) (Sept 3) still both list at **$10 / $50**; below them sit **Opus 5.5** ($4 / $20, Sept 22), the two mid tiers **Sonnet 5.5** and **GPT-6.1 Sol** (both $2 / $10, Sept 28–29, both their vendor's coding-agent default), and now the floor: **GPT-6 Luna** ($0.10 / $0.50, Sept 22) and **Claude Haiku 5.5** (Oct 7, $0.10 / $0.50 for prompts up to 100K tokens, $0.50 / $2.50 above). Google joined the priced field on **Oct 13** when **Gemini 4 Argon** opened to the paid API at $2 / $10 through Nov 30, then $4 / $20, and Meta's **Muse Wonder** (Oct 12) lands on **$4 / $20 with $0.20 cache reads** — Opus 5.5's numbers exactly, which makes $4 / $20 a three-vendor price point. The column this map said separated the two mid tiers has closed: Anthropic's pricing page now lists Sonnet 5.5 cache reads at **$0.10/M**, not the $0.20 recorded from the Sept 28 changelog (Claude Code `v2.1.296` corrected its own figure on Oct 9), so Sonnet 5.5 and GPT-6.1 Sol are identical on sticker and on cache. What still separates them is long-context shape (OpenAI reprices the whole request past 272k input tokens; Anthropic does not; Haiku 5.5 prices by prompt length). See [cost & benchmarks](comparisons/cost-and-benchmarks.md).
- **Product boundaries are collapsing upward**: OpenAI merged Codex into the ChatGPT app (July 9), and at DevDay (Sept 29) moved it further off the laptop with reusable cloud environments usable from any device — on the OpenAI side, "which coding agent" keeps turning into "how you use ChatGPT." The bundled default model changed twice in a month: [GPT-6 Astra](agents/gpt-6-astra.md) from `rust-v0.153.4` (Sept 4), then **GPT-6.1 Sol** from `rust-v0.159.1` (Sept 29), carried to the main release line by `rust-v0.161.0` (Oct 7). Since `0.162.0` (Oct 8) the TUI also follows the server's model default, so the effective default can change without a release, and on **Oct 14** OpenAI retired GPT-5.5 from Codex and ChatGPT for ChatGPT sign-in. Three windows have now passed with no tracked coding agent changing a default in a release. If you run Codex on defaults, pin the model id anyway — and know that a pinned model can be retired under you; the product will not hold either still for you. See [Codex](agents/codex.md).

## The First Cut Of The Map

<p align="center">
  <img src="assets/route-map-en.svg" alt="The AI Agent Map — 16 routes grouped into five decisions" width="100%" />
</p>

| Route | Representative projects | Typical user |
| --- | --- | --- |
| Direct execution | [Claude Code](agents/claude-code.md), [Aider](agents/aider.md), [Codex](agents/codex.md), [Kimi Code](agents/kimi-code.md), [MiMoCode](agents/mimocode.md), [CodeWhale](agents/codewhale.md), [ZCode](agents/zcode.md), [OpenCode](agents/opencode.md), [Gemini CLI](agents/gemini-cli.md), [Qwen Code](agents/qwen-code.md), [Grok Build](agents/grok-build.md), [Devin](agents/devin.md), [Jules](agents/jules.md) | Someone who wants to hand a concrete coding task to an agent (see the [terminal coding CLI comparison](comparisons/coding-cli-agents.md)) |
| Agent harness framework | [DeepSeek Harness](agents/deepseek-harness.md), [Pi](agents/pi.md), [jcode](agents/jcode.md), [OpenHands](agents/openhands.md), [SWE-agent](agents/swe-agent.md), [mini-swe-agent](agents/mini-swe-agent.md), [OpenHarness](agents/openharness.md), [QM](agents/qm.md), [Omnigent](agents/omnigent.md), [TrueForge](agents/trueforge.md) | Someone who wants to own the agent loop, tool surface, and permissions instead of inheriting a vendor's product — QM and Omnigent extend this to running *several* harnesses under one layer (see the [harness comparison](comparisons/agent-harness-frameworks.md)) |
| Frontier agentic model | [Claude Fable 5.1](agents/claude-fable-5.md), [Claude Opus 5](agents/claude-opus-5.md), [GPT-6 Astra](agents/gpt-6-astra.md), [GPT-5.5](agents/gpt-5.5.md) | Someone choosing which model to wire into their own agent system or evaluating the capability ceiling of Anthropic / OpenAI surfaces — the ceilings (Fable 5.1, Astra) and the default you actually run (Opus 5) are separate decisions |
| Open-weights agentic model | [Kimi K3](agents/kimi-k3.md), [GLM-5.3](agents/glm-5.md), [DeepSeek V4](agents/deepseek-v4.md), [Qwen3-Coder](agents/qwen3-coder.md) | Someone who wants frontier-class capability on weights they host and licence themselves — a different decision from picking between the closed ceilings |
| Agentic skills framework | [Superpowers](agents/superpowers.md), [ECC](agents/ecc.md) | Someone who wants a methodology + composable skills layer that plugs into Claude Code, Codex, Cursor, and similar agents |
| Workflow / orchestration layer | [oh-my-claudecode](agents/oh-my-claudecode.md), [oh-my-codex](agents/oh-my-codex.md), [Ruflo](agents/ruflo.md), [Orca](agents/orca.md), [Paperclip](agents/paperclip.md) | Someone who already likes Claude Code or Codex and wants stronger orchestration on top (Ruflo extends this to multi-machine federation and 100+ specialized agents) |
| Editor-centric AI workflow | [Cursor](agents/cursor.md), [Windsurf](agents/windsurf.md), [Continue](agents/continue.md) | Someone who wants the editor itself to stay central |
| Review-first automation | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md), [CoStrict](agents/costrict.md), [Open Code Review](agents/open-code-review.md) | Someone who wants review and human control to stay central (CoStrict adds enterprise strict-workflow + private deployment; Open Code Review is review only, tuned for precision in CI) |
| Managed background path | [Claude Managed Agents](agents/claude-managed-agents.md) | Someone who needs scheduled, cloud, or detached Anthropic workflows |
| Consumer personal agent | [ChatGPT dots](agents/chatgpt-dots.md), [Gemini Task](agents/gemini-task.md), [Claude (Cowork)](agents/claude-cowork.md), [Claude Duet](agents/claude-duet.md), [Muse (Meta)](agents/meta-muse.md), [Grok Bot](agents/grok-bot.md), [Cue (Manus)](agents/manus-cue.md), [Doubao](agents/doubao.md), [Qwen app](agents/qwen-app.md), [AutoGLM](agents/autoglm.md), [Yuanbao](agents/yuanbao.md) | Someone who wants to hand errands, inboxes, bookings or their phone to an agent sold as a product rather than run as software (see the [personal agents comparison](comparisons/personal-agents.md)) |
| General-purpose autonomous agent | [AutoGPT](agents/autogpt.md), [Agent Zero](agents/agent-zero.md), [BabyAGI](agents/babyagi.md), [Julep](agents/julep.md), [GenericAgent](agents/generic-agent.md), [ml-intern](agents/ml-intern.md), [WorkBuddy](agents/workbuddy.md), [Kimi Work](agents/kimi-work.md) | Someone who wants autonomous, general-purpose task execution — ml-intern is the ML-specialized variant, while WorkBuddy and Kimi Work aim the same loop at desktop knowledge work rather than repositories |
| Build-your-own system | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md), [Haystack](agents/haystack.md), [Semantic Kernel](agents/semantic-kernel.md), [DSPy](agents/dspy.md), [Pydantic AI](agents/pydantic-ai.md), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) | Teams building their own agent platform instead of buying one |
| Runtime and tools | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [Trail Code (Graft)](agents/graft.md), [CLI-Anything](agents/cli-anything.md), [claude-mem](agents/claude-mem.md), [Graphify](agents/graphify.md) | Teams that need workflow automation, code execution, LLM gateways, agent context infrastructure, agent-driven CLIs, or visual builders |
| Observability and evals | [Langfuse](agents/langfuse.md) | Someone whose agents already run in production and needs to know what they did, what they cost, and whether quality is drifting (see [observability & evaluation](comparisons/observability-and-evals.md)) |
| Browser agent | [Browser Use](agents/browser-use.md) | Someone whose task lives on a website with no API — a different question from how an agent edits files, because it decides what an agent may do as you on the open web |
| Self-hosted / local runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md), [OpenHuman](agents/openhuman.md) | Users who need on-device privacy, long-running agents, local control, channels, devices, or personal-data life integration |

## Current Mainstream Coverage

94 profiled projects, grouped by what they are. Expand a group, or browse the full route/coverage tables in [agents/](agents/README.md).

<details>
<summary><strong>Coding agents, editors, and orchestration</strong> (33 projects)</summary>

| Project | Route | One-line positioning |
| --- | --- | --- |
| [Aider](agents/aider.md) | Direct execution | Terminal-first AI pair programmer close to git |
| [Claude Code](agents/claude-code.md) | Direct execution | Local and IDE-first coding agent |
| [Claude Managed Agents](agents/claude-managed-agents.md) | Managed background path | Anthropic managed / cloud execution mapping |
| [Codex](agents/codex.md) | Direct execution | Coding agent inside the ChatGPT app, with async cloud delegation |
| [oh-my-claudecode](agents/oh-my-claudecode.md) | Workflow layer | Teams-first orchestration layer on top of Claude Code |
| [oh-my-codex](agents/oh-my-codex.md) | Workflow layer | Stronger workflow, teams, and persistent state around Codex CLI |
| [Orca](agents/orca.md) | Workflow / orchestration layer | Open-source desktop app that runs any CLI coding agent side by side, each in its own git worktree, with review, browser, remote servers and a phone companion |
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
| [CodeWhale](agents/codewhale.md) | Direct execution | Provider-neutral Rust terminal coding agent, 40+ provider routes, DeepSeek still the default (formerly DeepSeek-TUI) |
| [Kimi Code](agents/kimi-code.md) | Direct execution | Moonshot AI's official Kimi-native terminal coding CLI (successor to kimi-cli) |
| [MiMoCode](agents/mimocode.md) | Direct execution | Xiaomi's official MiMo terminal coding agent with built-in cross-session memory |
| [Grok Build](agents/grok-build.md) | Direct execution | SpaceXAI's official Rust terminal coding agent — full-screen TUI, headless CI mode, ACP editor server |
| [CoStrict](agents/costrict.md) | Review-first automation | Enterprise Cline-lineage coding agent with strict standardized workflow, AI code review, and private deployment |
| [SWE-agent](agents/swe-agent.md) | Agent harness framework | Princeton + Stanford's original SWE-bench harness with single-YAML configuration |
| [mini-swe-agent](agents/mini-swe-agent.md) | Agent harness framework | The ~100-line Python successor to SWE-agent that still scores >74% on SWE-bench Verified |
| [OpenHarness](agents/openharness.md) | Agent harness framework | HKUDS's 10-subsystem open agent harness with 43+ tools, anthropics/skills, and MCP |
| [Omnigent](agents/omnigent.md) | Agent harness framework | Meta-harness that mixes Claude Code, Codex, Cursor, OpenCode, Hermes, and Pi in one session, with policies and cloud sandboxes |
| [OpenCode](agents/opencode.md) | Direct execution | The largest vendor-neutral open-source coding agent — 219k stars, MIT |
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
<summary><strong>Frameworks and infrastructure</strong> (23 projects)</summary>

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
| [Paperclip](agents/paperclip.md) | Workflow / orchestration layer | Self-hosted control plane that runs a team of agents like a company: goal-linked tickets, org chart, budgets, approvals and scheduled routines |
| [CodeGraph](agents/codegraph.md) | Runtime and tools | Pre-indexed code knowledge graph + MCP server for Claude Code, Cursor, Codex CLI, opencode, and Hermes Agent |
| [Trail Code (Graft)](agents/graft.md) | Runtime and tools | Code context written as linked markdown in your repo, wired into eight-plus agents with one command |
| [claude-mem](agents/claude-mem.md) | Runtime and tools | Bolt-on cross-session memory: hooks capture agent activity, a model compresses it, relevant context is injected next session; paid hosted observer optional |
| [Graphify](agents/graphify.md) | Runtime and tools | Turns a codebase plus its docs, PDFs and media into a provenance-tagged knowledge graph that agents query through a skill, CLI or local MCP server |
| [Browser Use](agents/browser-use.md) | Browser agent | Gives an agent a real browser — opens pages, clicks, types, fills forms |
| [Microsoft Agent Framework](agents/microsoft-agent-framework.md) | Build-your-own system | AutoGen's successor; production multi-agent workflows across Python, .NET, and Go |
| [CLI-Anything](agents/cli-anything.md) | Runtime and tools | Auto-generates Click-based CLIs for arbitrary software so agents can drive non-API apps |

</details>

<details>
<summary><strong>Models and skills</strong> (10 entries)</summary>

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
| [ECC](agents/ecc.md) | Agentic skills framework | Cross-harness plugin bundling 311 skills, 71 subagents, enforcement hooks, a memory vault and the AgentShield config scanner; Claude Code first |

</details>
<details>
<summary><strong>Consumer personal agents</strong> (11 products)</summary>

| Project | Route | One-line positioning |
| --- | --- | --- |
| [ChatGPT dots](agents/chatgpt-dots.md) | Consumer personal agent | OpenAI's always-on agent in ChatGPT — GPT-6 Astra, its own cloud computer, reachable in Slack, Teams and by call; Pro only, not in Europe |
| [Gemini Task](agents/gemini-task.md) | Consumer personal agent | The Gemini app's agent mode (formerly Spark) — scheduled work across Google Workspace and Chrome, with a published confirmation list |
| [Claude (Cowork)](agents/claude-cowork.md) | Consumer personal agent | Cowork merged into the Claude app — tasks that schedule and keep running in an isolated cloud session, three named approval modes |
| [Claude Duet](agents/claude-duet.md) | Consumer personal agent | Anthropic's separate proactive-agent app: morning brief, checks your accounts every few hours, own VM, approval before it sends, pays, signs or deletes; US waitlist |
| [Muse (Meta)](agents/meta-muse.md) | Consumer personal agent | Meta's errand agent in its own app and WhatsApp — a dedicated cloud VM, one-time card payments, US limited testing |
| [Grok Bot](agents/grok-bot.md) | Consumer personal agent | xAI's team of always-on Bots sharing one cloud computer in Cursor's cloud, with saved skills on a schedule |
| [Cue (Manus)](agents/manus-cue.md) | Consumer personal agent | Manus's personal-agent app where each agent has its own email, phone number, wallet and computer; invite-only early access |
| [Doubao](agents/doubao.md) | Consumer personal agent | ByteDance's assistant with a work-task mode and a phone-OS assistant that operates other apps on partner phones (Beta) |
| [Qwen app](agents/qwen-app.md) | Consumer personal agent | Alibaba's consumer app turned errand agent — deliverables, scheduled tasks, food, hotels and government services |
| [AutoGLM](agents/autoglm.md) | Consumer personal agent | Zhipu's phone-use agent: a free app on cloud phones, plus the Apache-2.0 Open-AutoGLM framework for your own phone |
| [Yuanbao](agents/yuanbao.md) | Consumer personal agent | Tencent's free assistant with a Hy3 Agent feature that delivers office files — the consumer end of WorkBuddy's model family |

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