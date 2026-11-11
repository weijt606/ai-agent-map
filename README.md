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
| I want to know how capable each model tier is and how agents bill | [![View benchmarks and billing](https://img.shields.io/badge/VIEW-BENCHMARKS%20%26%20BILLING-0891b2?style=for-the-badge&labelColor=0e7490)](comparisons/benchmarks-and-billing.md) [![View memory approaches](https://img.shields.io/badge/VIEW-MEMORY%20APPROACHES-0d9488?style=for-the-badge&labelColor=0f766e)](comparisons/memory-approaches.md) |
| My agents already run — I need to know whether they still work | [![View observability and evaluation](https://img.shields.io/badge/VIEW-OBSERVABILITY%20%26%20EVALS-4f46e5?style=for-the-badge&labelColor=3730a3)](comparisons/observability-and-evals.md) |
| I want the stock rankings and the weekly trend chart | [![View rankings](https://img.shields.io/badge/VIEW-RANKINGS-7c3aed?style=for-the-badge&labelColor=5b21b6)](rankings/README.md) |
| I want problem-first guides or the full comparison list | [![Browse use cases](https://img.shields.io/badge/BROWSE-USE%20CASES-ea580c?style=for-the-badge&labelColor=9a3412)](use-cases/README.md) [![Browse comparisons](https://img.shields.io/badge/BROWSE-COMPARISONS-475569?style=for-the-badge&labelColor=334155)](comparisons/README.md) |

## Recent Heat Ranking

Popularity is not fit.

This table tracks projects that showed up as especially hot in the latest weekly GitHub snapshot. The rank follows the 7-day gain. The total star counts below were checked when this repo was updated.

> **Last updated:** 2026-11-11 · **Snapshot window:** 2026-11-04 → 2026-11-11 (gain since last update: **7 calendar days**, about 7.17 by fetch time against about 7.45 last window, so comparisons below use elapsed time) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(↑) | [mattpocock/skills](https://github.com/mattpocock/skills) | 321.2k | +9,640 | Watchlist (Skills Wave) | **Back to #1** after two windows at #2: up **45%** on elapsed time to about 9,412 a week, its largest 7-day gain since 10-14 and its 16th #1 in 30 windows. **Passed [Superpowers](agents/superpowers.md)** (321,245 against 315,888), so it is now the largest collection this map tracks and the second-largest tracked repo after OpenClaw. **Past 320k**. No release and no commit since Oct 31 |
| #2&nbsp;(↓) | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 278.5k | +7,164 | In scope · [profile](agents/deepseek-harness.md) | Down 4% on elapsed time (about 6,995 a week), flat by this board's rule, but #1 changed hands after two windows. **Past 275k** (278,465). One pre-release, `dsh-v0.2.2-rc.1` |
| #3&nbsp;(new) | [Orca](https://github.com/stablyai/orca) | 121.7k | +7,099 | In scope · [profile](agents/orca.md) | **First measured window**: tracked since 11-03, so there is no earlier rate to compare and this is not a breakout call. Infra (orchestration). **Past 120k** (121,747). Eight releases, `v1.4.249`–`v1.4.256`, including chat forking and Plan mode |
| #4&nbsp;(↑) | [anthropics/skills](https://github.com/anthropics/skills) | 192.6k | +5,472 | Watchlist (Skills Wave) | Up **91%** on elapsed time to about 5,343 a week, a second straight rise: its largest window gain since the 9-day 06-01 window and its fastest weekly rate since 05-22. **Past 190k** (192,624). One commit: the Office skills (`docx`, `pdf`, `pptx`, `xlsx`) moved to Apache-2.0 on Nov 6. Nothing links that to the stars |
| #5&nbsp;(new) | [ECC](https://github.com/affaan-m/ECC) | 300.9k | +4,333 | In scope · [profile](agents/ecc.md) | **First measured window.** **Past 300k** (300,941), the third collection past it after mattpocock/skills and Superpowers. No release since `v2.2.3` (Oct 1); two CI commits |
| #6&nbsp;(↓) | [Superpowers](https://github.com/obra/superpowers) | 315.9k | +3,959 | In scope · [profile](agents/superpowers.md) | Down **29%** on elapsed time to about 3,865 a week, back to its 10-21 pace: last window's 46% jump did not repeat, so it stays a one-window spike. Now **5,357 behind** mattpocock/skills. **Past 315k**. No release and no commit since Nov 3 |
| #7&nbsp;(new) | [claude-mem](https://github.com/thedotmack/claude-mem) | 115.9k | +3,900 | In scope · [profile](agents/claude-mem.md) | **First measured window.** Infra (memory and context). **Past 115k** (115,944). Fourteen releases, `v15.10.0`–`v15.17.0` |
| #8&nbsp;(new) | [Graphify](https://github.com/Graphify-Labs/graphify) | 145.8k | +3,884 | In scope · [profile](agents/graphify.md) | **First measured window.** Infra (memory and context). **Past 145k** (145,792). Four releases, `v0.9.103`–`v0.9.106` |
| #9&nbsp;(↓) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 115.4k | +2,315 | Watchlist (Skills Wave) | Up 18% on elapsed time, ending three straight slowdowns; down a place only because new entrants landed above it. **Past 115k** (115,385). No release and no commit since Nov 1 |
| #10&nbsp;(↓) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 262.5k | +2,248 | In scope · [profile](agents/hermes-agent.md) | Down 11% on elapsed time and four places, holding the last seat by 92 over [Paperclip](agents/paperclip.md). **Present in all 30 recorded windows**. `v0.23.0` "The Hearth Release" (Nov 5) and `v0.23.1` |

- Heat is useful for discovery, not for selection by itself.
- **Window length.** Fetches were about **7.17 days** apart (Nov 4 11:16 → Nov 11 15:20, Beijing time) against about **7.45** last window. That 4% gap is under the 5% at which this board must switch basis, but last window was read on elapsed time, so this one is too. The table shows raw gains; single-digit changes count as flat.
- **Four of the top ten are first measurements, not breakouts.** [Orca](agents/orca.md) (#3), [ECC](agents/ecc.md) (#5), [claude-mem](agents/claude-mem.md) (#7) and [Graphify](agents/graphify.md) (#8) entered tracking on 11-03, and this is the first window in which they could rank. All four were already large and growing before this map polled them, so read their seats the way the board read the 09-09 pickups: the coverage gap closing, not four simultaneous jumps. The fifth, [Paperclip](agents/paperclip.md), is 11th (+2,156). Their next window is the first that can say whether any of them is speeding up.
- **Like for like, the board barely moved.** Of the 57 repos measured in both windows, **20 accelerated and 37 slowed** on elapsed time (17 and 40 on raw gains). The ten seats ran about 48,831 a week against about 34,710 (+41%), and the bar for #10 rose about 43% (about 1,536 → about 2,195 a week), but nearly all of that is the new entrants: the ten fastest of the repos measured last window ran about 36,260 a week (+4%), and their #10 ([Pi](agents/pi.md), about 1,424) was 7% below last window's bar. Of the six seat-holders with an earlier rate, three sped up (mattpocock/skills, anthropics/skills, addyosmani/agent-skills), one was flat (DeepSeek Harness) and two slowed (Superpowers, Hermes Agent).
- **[mattpocock/skills](https://github.com/mattpocock/skills) retook #1 and passed Superpowers.** Last edition put the gap at 324 and noted that this map's previous forecast of a crossing (10-21) was wrong. This time it happened, because mattpocock sped up 45% while Superpowers fell 29%; it now leads by **5,357**. That is its 16th #1 in 30 windows, against three for [DeepSeek Harness](agents/deepseek-harness.md), whose two-window hold ended on a flat gain. It is now the largest collection this map tracks, but in gains it still trailed the other four general collections combined by 6,439 (9,640 against 5,472 + 4,333 + 3,959 + 2,315 = 16,079), so concentration in the wave did not return.
- **The spike rule paid out twice more.** [Superpowers](agents/superpowers.md)' 46% jump gave back 29%, with no release or commit in the window. [TradingAgents](https://github.com/TauricResearch/TradingAgents) slowed a second straight window (−51%) and left the board for 14th; a README commit on Nov 4 announcing the Trading-R1 launch did not lift it.
- **The board's mix is the most unusual on record.** Skills hold **five seats** (#1, #4, #5, #6, #9), all of them general collections, the first time five general collections have sat in the top ten (the earlier peak was four; ECC is counted for the first time). Infra holds **three** (Orca, claude-mem, Graphify), the most in any of 30 windows; the previous high was two. Agents hold **two** (#2, #10), tying the fewest, last seen on 05-22. [OpenCode](agents/opencode.md)'s nine-window run ended at 13th (−23%), and [Codex CLI](agents/codex.md) (12th, flat) and Pi (15th, −7%) left after one window back. Hermes Agent (30 of 30), Superpowers and mattpocock/skills (25 each) are the long runs still going; DeepSeek Harness is next at 10.
- **The model layer moved on several fronts.** (1) **Anthropic released Claude Fable 5.2 and Mythos 5.2** (Nov 9): Anthropic's table puts Fable 5.2 above Opus 5.5, GPT-6 Astra and Gemini 4 Carbon on FrontierSWE v2 (69.9%) and FrontierCode 2.0 (49.1%), vendor-reported; Anthropic still recommends starting most coding on Opus 5.5. [Claude Code](agents/claude-code.md) `2.1.321` made it the default *Fable* model the same day, and GitHub Copilot added it. (2) **Google's Gemini 4 Carbon**, announced Oct 28 behind its Fairwind Program and missed by this map until now, reached the Gemini API on Nov 10 and is rolling out to AI Ultra in Antigravity and the Gemini app. (3) **Kimi K3.1 Pro's weights are public** on Hugging Face (by Nov 5) under a custom licence, and it now sits in the open-weights table. (4) OpenAI released GPT-6-Cyber (Nov 5), a vulnerability-research model behind its Daybreak setup, not a coding default. (5) Google will also route `gemini-2.5-flash` to `gemini-3.5-flash-lite` on Dec 1, alongside `gemini-2.5-pro` → `gemini-3.8-flash`; [Gemini CLI](agents/gemini-cli.md)'s source default is still `gemini-2.5-pro` at `v0.68.0`. **The no-change run on defaults ended after five windows**, inside model families rather than at the top level: Claude Code moved its Fable default to 5.2, and [Pi](agents/pi.md) `v1.5.1` (Nov 9) moved its `anthropic` provider default from Opus 4.8 to Opus 5.5 and moved several other providers to newer models. [Codex CLI](agents/codex.md) `rust-v0.167.0` changed only the models used for memory extraction; [OpenCode](agents/opencode.md) `v2.2.7` changed none. Details in [market-events](market-events.md).
- **Personal agents and skills pages refreshed.** Gemini 4 Carbon reached Gemini Task on AI Ultra, [ChatGPT dots](agents/chatgpt-dots.md) added GPT-6.1 Terra and opens by default to eligible Enterprise workspaces from Nov 18, [Muse](agents/meta-muse.md) added voice and an Apple Watch app, and [Grok Bot](agents/grok-bot.md)'s docs now say Grok Bot, not Cursor, picks the model; see [recent changes](comparisons/personal-agents.md#recent-changes). On the [Agent Skills](comparisons/agent-skills.md) page, anthropics/skills' Office skills are now Apache-2.0, and two Claude rows are corrected (claude.ai skills have synced to Claude Code since v2.1.273; Team and Enterprise can provision skills organization-wide).
- **Corrections.** The [Pi](agents/pi.md) profile's website was `lefos.ai`, which redirects elsewhere; it is pi.dev. **No new profile this window.** Candidates found by the scan: [DeerFlow](https://github.com/bytedance/deer-flow) (85.2k, MIT, a sub-agent harness) and [nanobot](https://github.com/HKUDS/nanobot) (50.0k, MIT, a self-hosted personal agent); [magpie](https://github.com/yetone/magpie) (34.2k) grew fastest on the watchlist but is a gateway, not an agent.
- Milestones, checked against the raw counts rather than the rounded column: **mattpocock/skills 320k**, **ECC 300k**, DeepSeek Harness **275k**, OpenCode **225k**, [n8n](agents/n8n.md) **210k**, anthropics/skills **190k**, Claude Code **155k**, Graphify **145k**, Orca, Pi and [Browser Use](agents/browser-use.md) **120k**, claude-mem and addyosmani/agent-skills **115k**, both research collections **56k**, [Aider](agents/aider.md) **50k**, [Langfuse](agents/langfuse.md) **37k**, [Qwen Code](agents/qwen-code.md) **29k** and [mini-swe-agent](agents/mini-swe-agent.md) **9.5k**. Near misses: [Codex CLI](agents/codex.md) is **178 short of 135k**, [Open Code Review](agents/open-code-review.md) 184 short of 50k.
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 394.3k stars (+445, down 31% on elapsed time); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.

<details>
<summary>More window notes: skills-wave share, OpenClaw, and everything growing outside the top 10</summary>

- The `.claude/skills` wave **holds five of the top ten**: #1, #4, #5, #6 and #9, all general collections, five for the first time since 09-30 and the first time all five are general collections. Policy unchanged: curated collections are tracked as Skills Wave entries and compared on the [Agent Skills](comparisons/agent-skills.md) page; the framework end is profiled through [Superpowers](agents/superpowers.md) and [ECC](agents/ecc.md).
- Just off the table, on elapsed time: [Paperclip](agents/paperclip.md) 113.0k (+2,156) at 11th, first measured, with `v2026.1106.0` making Paperclip Runner the default for new Claude, Codex, OpenCode and Pi agents and removing Pipelines; [Codex CLI](agents/codex.md) 134.8k (+1,777) at 12th, flat; [OpenCode](agents/opencode.md) 226.0k (+1,577) at 13th, down 23%, on `v2.2.6` and `v2.2.7`; TradingAgents 121.9k (+1,527) at 14th, down 51%; [Pi](agents/pi.md) 121.3k (+1,459) at 15th, down 7%, past 120k; academic-research-skills 56.4k (+1,163) at 16th, up 12%; [CodeGraph](agents/codegraph.md) 77.4k (+922) at 17th, up 14%; [Claude Code](agents/claude-code.md) 155.2k (+787) at 18th, down 6%, on three releases (`v2.1.319`, `v2.1.321`, `v2.1.322`); scientific-agent-skills 56.8k (+778) at 19th, down 24%; and [Browser Use](agents/browser-use.md) 120.7k (+686) at 20th, flat, with its 1.0 rewrite shipping on Nov 10, a day before this fetch. OpenClaw is excluded from the board, so these off-board positions are counted the same way.
- **The research collections diverged.** academic-research-skills sped up 12% while scientific-agent-skills slowed 24%; K-Dense stays the larger, 56,768 against 56,399, but the gap fell from 754 to 369. [mini-swe-agent](agents/mini-swe-agent.md) more than doubled its pace (+462, 24th). [Gemini CLI](agents/gemini-cli.md) slowed again (+59, down 56%, 53rd). [anthropics/financial-services](https://github.com/anthropics/financial-services) was flat (+188, 36th).
- Continuing to grow but outside the top 10 by gain (raw figures, 7 calendar days): [Paperclip](agents/paperclip.md) 113.0k (+2,156), [Codex CLI](agents/codex.md) 134.8k (+1,777), [OpenCode](agents/opencode.md) 226.0k (+1,577), [TradingAgents](https://github.com/TauricResearch/TradingAgents) 121.9k (+1,527), [Pi](agents/pi.md) 121.3k (+1,459), [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 56.4k (+1,163), [CodeGraph](agents/codegraph.md) 77.4k (+922), [Claude Code](agents/claude-code.md) 155.2k (+787), [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 56.8k (+778), [Browser Use](agents/browser-use.md) 120.7k (+686), [Ruflo](agents/ruflo.md) 81.5k (+645), [n8n](agents/n8n.md) 210.1k (+586), [OpenHands](agents/openhands.md) 93.2k (+580), [mini-swe-agent](agents/mini-swe-agent.md) 9.5k (+462), [Open Code Review](agents/open-code-review.md) 49.8k (+441), [LiteLLM](agents/litellm.md) 63.1k (+428), [CLI-Anything](agents/cli-anything.md) 58.6k (+382), [LangChain](agents/langchain.md) 149.3k (+361), [LangGraph](agents/langgraph.md) 44.8k (+360), [Qwen Code](agents/qwen-code.md) 29.3k (+312), [Langfuse](agents/langfuse.md) 37.3k (+310), [CrewAI](agents/crewai.md) 60.8k (+287), [Goose](agents/goose.md) 56.4k (+250), [jcode](agents/jcode.md) 21.7k (+242), [Cline](agents/cline.md) 71.5k (+241), [anthropics/financial-services](https://github.com/anthropics/financial-services) 41.2k (+188), [agentmemory](https://github.com/rohitg00/agentmemory) 30.3k (+158), [ZCode](agents/zcode.md) 8.6k (+143), [Omnigent](agents/omnigent.md) 11.3k (+137), [Aider](agents/aider.md) 50.1k (+129), [12-factor-agents](https://github.com/humanlayer/12-factor-agents) 27.1k (+124), [Trail Code (Graft)](agents/graft.md) 11.2k (+120), [OpenHuman](agents/openhuman.md) 42.6k (+114), [AutoGPT](agents/autogpt.md) 188.0k (+101), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) 14.6k (+100), [LlamaIndex](agents/llamaindex.md) 52.9k (+74), [Kimi Code](agents/kimi-code.md) 8.2k (+72), [Letta (MemGPT)](agents/memgpt.md) 25.4k (+70), [Open Interpreter](agents/open-interpreter.md) 68.9k (+68), [SWE-agent](agents/swe-agent.md) 20.8k (+64), [Grok Build](agents/grok-build.md) 27.7k (+63), [eve](agents/eve.md) 5.8k (+61), [Gemini CLI](agents/gemini-cli.md) 108.8k (+59), [Continue](agents/continue.md) 36.5k (+51), [QM](agents/qm.md) 15.7k (+50), [MiMoCode](agents/mimocode.md) 13.8k (+35), [OpenHarness](agents/openharness.md) 16.2k (+31), [TrueForge](agents/trueforge.md) 6.5k (+31), [Flowise](agents/flowise.md) 55.6k (+21), [CodeWhale](agents/codewhale.md) 41.2k (+13), [CoStrict](agents/costrict.md) 4.5k (+5)

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

Popularity tells you what to look at. These six pages tell you what to pick:

- **[Capability matrix](capabilities/matrix.md)** — every project scored side by side (●/◐/○/—) across the nine shared [capability dimensions](capabilities/README.md), grouped by route. The answer to "for this capability, who treats it as a core strength."
- **[Benchmarks & billing](comparisons/benchmarks-and-billing.md)** — frontier-model capability, plus how each coding agent bills. Since the model layer went tiered and metered, "which tier for this task" is the selection decision. This map does not list or compare prices.
- **[Memory approaches](comparisons/memory-approaches.md)** — seven different things projects mean by "has memory," from self-editing stores to passive semantic recall, and which to pick for what you need to persist.
- **[Consumer personal agents](comparisons/personal-agents.md)** — the agents you hand your day to — ChatGPT dots, Gemini Task, Claude, Muse, Grok Bot, Cue, Doubao, Qwen, AutoGLM, Yuanbao, Today — compared on facts and control rather than popularity, because closed products have no public number to rank by.
- **[Agent Skills](comparisons/agent-skills.md)** — what a skill is, which agents load one, and the five largest collections and frameworks (Superpowers, mattpocock/skills, ECC, anthropics/skills, addyosmani/agent-skills) compared on kind, footprint, maintainer and license, plus what to check before installing someone else's. Collections are compared here rather than profiled.
- **[Observability & evaluation](comparisons/observability-and-evals.md)** — the layer under everything above: once an agent runs unattended, failure stops looking like a crash and starts looking like silent quality drift. Compares [Langfuse](agents/langfuse.md), Opik, Phoenix, Helicone, LangSmith and others — and untangles the four different things "open source" means in that field.

## Market Pulse

The three structural stories shaping selection right now — full records with dates and sources live in [market-events.md](market-events.md):

- **The `.claude/skills` wave takes five seats, and mattpocock/skills passes Superpowers** (May 2026 → ongoing): curated skill collections and skills frameworks have held between two and six of the weekly heat top 10 for five months, and the count rotates rather than sitting still: 6/10, then 2/10, 3/10, 4/10, 5/10, 3/10, 4/10 for four windows, and now **5 of 10** (2026-11-11), the first time all five are general collections: [mattpocock/skills](https://github.com/mattpocock/skills), [anthropics/skills](https://github.com/anthropics/skills), [ECC](agents/ecc.md), [Superpowers](agents/superpowers.md) and [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills). ECC counts for the first time, on its first measured gain. mattpocock (321,245) now leads Superpowers (315,888) by 5,357, so the largest collection this map tracks is a personal directory, the key-person risk this map has flagged since June; in gains it still trailed the other four combined by 6,439. ECC (300,941) is third. This map profiles the framework end through Superpowers and ECC, and compares collections on the [Agent Skills](comparisons/agent-skills.md) page.
- **The model ladder now has every rung filled at both vendors, and Google has a new top**: [Claude Fable 5.2](agents/claude-fable-5.md) (Nov 9), [GPT-6 Astra](agents/gpt-6-astra.md) (Sept 3) and Google's **Gemini 4 Carbon** (announced Oct 28, on the Gemini API Nov 10) sit at the top; below them are **Opus 5.5** (Sept 22), the two mid tiers **Sonnet 5.5** and **GPT-6.1 Sol** (Sept 28–29, both their vendor's coding-agent default), and the lowest tiers, **GPT-6 Luna** (Sept 22) and **Claude Haiku 5.5** (Oct 7). On **Oct 26** OpenAI added **GPT-6.1 Terra**, selectable in Codex but not made a default. Google's **Gemini 4 Argon** opened to the paid API on **Oct 13**, and Meta released **Muse Wonder** on Oct 12. On the open side, **Kimi K3.1 Pro**'s weights went public by Nov 5. See [benchmarks & billing](comparisons/benchmarks-and-billing.md).
- **Product boundaries are collapsing upward**: OpenAI merged Codex into the ChatGPT app (July 9), and at DevDay (Sept 29) moved it further off the laptop with reusable cloud environments usable from any device — on the OpenAI side, "which coding agent" keeps turning into "how you use ChatGPT." The bundled default model changed twice in a month: [GPT-6 Astra](agents/gpt-6-astra.md) from `rust-v0.153.4` (Sept 4), then **GPT-6.1 Sol** from `rust-v0.159.1` (Sept 29), carried to the main release line by `rust-v0.161.0` (Oct 7). Since `0.162.0` (Oct 8) the TUI also follows the server's model default, so the effective default can change without a release, and on **Oct 14** OpenAI retired GPT-5.5 from Codex and ChatGPT for ChatGPT sign-in. The run of windows with no tracked coding agent changing a default in a release ended at five on Nov 9, though not at Codex: [Claude Code](agents/claude-code.md) moved its Fable default to 5.2 and [Pi](agents/pi.md) its `anthropic` provider default to Opus 5.5, while Codex's main default has been GPT-6.1 Sol since Sept 29. If you run Codex on defaults, pin the model id anyway — and know that a pinned model can be retired under you; the product will not hold either still for you. See [Codex](agents/codex.md).

## The First Cut Of The Map

<p align="center">
  <img src="assets/route-map-en.svg" alt="The AI Agent Map — 16 routes grouped into five decisions" width="100%" />
</p>

| Route | Representative projects | Typical user |
| --- | --- | --- |
| Direct execution | [Claude Code](agents/claude-code.md), [Aider](agents/aider.md), [Codex](agents/codex.md), [Kimi Code](agents/kimi-code.md), [MiMoCode](agents/mimocode.md), [CodeWhale](agents/codewhale.md), [ZCode](agents/zcode.md), [CodeBuddy](agents/codebuddy.md), [OpenCode](agents/opencode.md), [Gemini CLI](agents/gemini-cli.md), [Qwen Code](agents/qwen-code.md), [Grok Build](agents/grok-build.md), [Devin](agents/devin.md), [Jules](agents/jules.md) | Someone who wants to hand a concrete coding task to an agent (see the [terminal coding CLI comparison](comparisons/coding-cli-agents.md)) |
| Agent harness framework | [DeepSeek Harness](agents/deepseek-harness.md), [Pi](agents/pi.md), [jcode](agents/jcode.md), [OpenHands](agents/openhands.md), [SWE-agent](agents/swe-agent.md), [mini-swe-agent](agents/mini-swe-agent.md), [OpenHarness](agents/openharness.md), [QM](agents/qm.md), [Omnigent](agents/omnigent.md), [TrueForge](agents/trueforge.md) | Someone who wants to own the agent loop, tool surface, and permissions instead of inheriting a vendor's product — QM and Omnigent extend this to running *several* harnesses under one layer (see the [harness comparison](comparisons/agent-harness-frameworks.md)) |
| Frontier agentic model | [Claude Fable 5.2](agents/claude-fable-5.md), [Claude Opus 5](agents/claude-opus-5.md), [GPT-6 Astra](agents/gpt-6-astra.md), [GPT-5.5](agents/gpt-5.5.md) | Someone choosing which model to wire into their own agent system or evaluating the capability ceiling of Anthropic / OpenAI surfaces — the ceilings (Fable 5.2, Astra) and the tier you actually run under them are separate decisions (Opus 5 was Claude Code's default Opus until Opus 5.5 replaced it on Sept 22, and Sonnet 5.5 became the default Sonnet on Sept 28) |
| Open-weights agentic model | [Kimi K3](agents/kimi-k3.md), [GLM-5.3](agents/glm-5.md), [DeepSeek V4](agents/deepseek-v4.md), [Qwen3-Coder](agents/qwen3-coder.md) | Someone who wants frontier-class capability on weights they host and licence themselves — a different decision from picking between the closed ceilings |
| Agentic skills framework | [Superpowers](agents/superpowers.md), [ECC](agents/ecc.md) | Someone who wants a methodology + composable skills layer that plugs into Claude Code, Codex, Cursor, and similar agents |
| Workflow / orchestration layer | [oh-my-claudecode](agents/oh-my-claudecode.md), [oh-my-codex](agents/oh-my-codex.md), [Ruflo](agents/ruflo.md), [Orca](agents/orca.md), [Paperclip](agents/paperclip.md) | Someone who already likes Claude Code or Codex and wants stronger orchestration on top (Ruflo extends this to multi-machine federation and 100+ specialized agents); Orca and Paperclip coordinate many different agents at once |
| Editor-centric AI workflow | [Cursor](agents/cursor.md), [Windsurf](agents/windsurf.md), [Google Antigravity](agents/antigravity.md), [TRAE](agents/trae.md), [Continue](agents/continue.md) | Someone who wants the editor itself to stay central |
| Review-first automation | [Cline](agents/cline.md), [GitHub Copilot](agents/github-copilot.md), [Froge Code](agents/froge-code.md), [CoStrict](agents/costrict.md), [Open Code Review](agents/open-code-review.md) | Someone who wants review and human control to stay central (CoStrict adds enterprise strict-workflow + private deployment; Open Code Review is review only, tuned for precision in CI) |
| Managed background path | [Claude Managed Agents](agents/claude-managed-agents.md) | Someone who needs scheduled, cloud, or detached Anthropic workflows |
| Consumer personal agent | [ChatGPT dots](agents/chatgpt-dots.md), [Gemini Task](agents/gemini-task.md), [Claude (Cowork)](agents/claude-cowork.md), [Claude Duet](agents/claude-duet.md), [Muse (Meta)](agents/meta-muse.md), [Grok Bot](agents/grok-bot.md), [Cue (Manus)](agents/manus-cue.md), [Doubao](agents/doubao.md), [Qwen app](agents/qwen-app.md), [AutoGLM](agents/autoglm.md), [Yuanbao](agents/yuanbao.md), [Today](agents/today-ai.md) | Someone who wants to hand errands, inboxes, bookings or their phone to an agent sold as a product rather than run as software (see the [personal agents comparison](comparisons/personal-agents.md)) |
| General-purpose autonomous agent | [AutoGPT](agents/autogpt.md), [Agent Zero](agents/agent-zero.md), [BabyAGI](agents/babyagi.md), [Julep](agents/julep.md), [GenericAgent](agents/generic-agent.md), [ml-intern](agents/ml-intern.md), [WorkBuddy](agents/workbuddy.md), [Kimi Work](agents/kimi-work.md) | Someone who wants autonomous, general-purpose task execution — ml-intern is the ML-specialized variant, while WorkBuddy and Kimi Work aim the same loop at desktop knowledge work rather than repositories |
| Build-your-own system | [LangChain](agents/langchain.md), [LangGraph](agents/langgraph.md), [CrewAI](agents/crewai.md), [LlamaIndex](agents/llamaindex.md), [Haystack](agents/haystack.md), [Semantic Kernel](agents/semantic-kernel.md), [DSPy](agents/dspy.md), [Pydantic AI](agents/pydantic-ai.md), [eve](agents/eve.md), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) | Teams building their own agent platform instead of buying one |
| Runtime and tools | [n8n](agents/n8n.md), [MemGPT](agents/memgpt.md), [Open Interpreter](agents/open-interpreter.md), [LiteLLM](agents/litellm.md), [Flowise](agents/flowise.md), [CodeGraph](agents/codegraph.md), [Trail Code (Graft)](agents/graft.md), [CLI-Anything](agents/cli-anything.md), [claude-mem](agents/claude-mem.md), [Graphify](agents/graphify.md) | Teams that need workflow automation, code execution, LLM gateways, agent context infrastructure, agent-driven CLIs, or visual builders |
| Observability and evals | [Langfuse](agents/langfuse.md) | Someone whose agents already run in production and needs to know what they did, what they cost, and whether quality is drifting (see [observability & evaluation](comparisons/observability-and-evals.md)) |
| Browser agent | [Browser Use](agents/browser-use.md) | Someone whose task lives on a website with no API — a different question from how an agent edits files, because it decides what an agent may do as you on the open web |
| Self-hosted / local runtime | [AI Edge Gallery](agents/ai-edge-gallery.md), [Goose](agents/goose.md), [Hermes Agent](agents/hermes-agent.md), [OpenClaw](agents/openclaw.md), [Mercury Agent](agents/mercury-agent.md), [OpenHuman](agents/openhuman.md) | Users who need on-device privacy, long-running agents, local control, channels, devices, or personal-data life integration |

## Current Mainstream Coverage

98 profiled projects, grouped by what they are. Expand a group, or browse the full route/coverage tables in [agents/](agents/README.md).

<details>
<summary><strong>Coding agents, editors, and orchestration</strong> (36 projects)</summary>

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
| [Google Antigravity](agents/antigravity.md) | Editor-centric AI workflow | Google's agent-first platform: desktop agent app, `agy` CLI, standalone IDE and editor extensions on one Gemini-tuned harness; free weekly tier, closed source |
| [TRAE](agents/trae.md) | Editor-centric AI workflow | ByteDance's AI IDE: VS Code-style IDE with an AI-led SOLO mode, plus an Agent window for parallel, cloud and scheduled tasks; separate international and China editions; chats may train models unless Privacy Mode is on |
| [OpenHands](agents/openhands.md) | Open-source execution | Open-source software engineering agent |
| [Devin](agents/devin.md) | Managed execution | End-to-end managed software engineering execution |
| [Jules](agents/jules.md) | Managed cloud execution | GitHub-connected coding delegation with PR handoff |
| [Continue](agents/continue.md) | Editor-centric | Open-source IDE extension with full model freedom |
| [Froge Code](agents/froge-code.md) | Review-first automation | Provisionally mapped to Automagik Genie |
| [Pi](agents/pi.md) | Agent harness framework | Minimal terminal coding-agent harness with multi-provider LLM support |
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
| [OpenCode](agents/opencode.md) | Direct execution | The largest vendor-neutral open-source coding agent — 222k stars (2026-10-28), MIT |
| [Gemini CLI](agents/gemini-cli.md) | Direct execution | Google's open-source terminal agent with Search grounding built in; since 2026-06-18 it serves Code Assist Standard/Enterprise and paid API keys, while consumer users were moved to Antigravity CLI |
| [Qwen Code](agents/qwen-code.md) | Direct execution | Open client and open weights, switchable across OpenAI/Anthropic/Gemini/local at runtime |
| [DeepSeek Harness](agents/deepseek-harness.md) | Agent harness framework | Everything-is-a-plugin harness — even the agent loop is swappable from config |
| [ZCode](agents/zcode.md) | Direct execution | Zhipu's desktop agentic dev environment: long-horizon "Goal" tasks, steerable from WeChat/Feishu/Telegram |
| [CodeBuddy](agents/codebuddy.md) | Direct execution | Tencent Cloud's coding line (editor plugin, CodeBuddy IDE, CodeBuddy Code CLI): a Claude-Code-shaped loop with a multi-vendor model catalog and private-cloud editions |
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
| [Claude Fable 5.2](agents/claude-fable-5.md) | Frontier agentic model | Anthropic's Mythos-class ceiling — the model you spend credits on, refreshed Nov 9 2026 |
| [Claude Opus 5](agents/claude-opus-5.md) | Frontier agentic model | The Opus tier below Fable; Claude Code's default Opus until Opus 5.5 replaced it on Sept 22 (Sonnet 5.5 became the default Sonnet on Sept 28) |
| [GPT-6 Astra](agents/gpt-6-astra.md) | Frontier agentic model | OpenAI's current ceiling (Sept 3 2026), shipped to the public in a restricted version |
| [GPT-5.5](agents/gpt-5.5.md) | Frontier agentic model | OpenAI's spring 2026 model, kept as the lineage reference through GPT-5.6 to Astra |
| [Kimi K3](agents/kimi-k3.md) | Open-weights agentic model | First open 3T-class model — 2.8T params, native vision, 1M context, custom licence |
| [GLM-5.3](agents/glm-5.md) | Open-weights agentic model | Strongest open-weights coding model on vendor numbers, Apache-2.0 — and ungated cyber capability |
| [DeepSeek V4](agents/deepseek-v4.md) | Open-weights agentic model | MIT at 1.6T params; SWE-bench Verified 80.6, reproducible because the weights are open |
| [Qwen3-Coder](agents/qwen3-coder.md) | Open-weights agentic model | The one that fits — ~3B activated of 80B, 256K→1M context, runs where you are |
| [Superpowers](agents/superpowers.md) | Agentic skills framework | Methodology and composable skills layer that plugs into Claude Code, Codex, Cursor, and other agents |
| [ECC](agents/ecc.md) | Agentic skills framework | Cross-harness plugin bundling 314 skills, 71 subagents, enforcement hooks, a memory vault and the AgentShield config scanner; Claude Code first |

</details>
<details>
<summary><strong>Consumer personal agents</strong> (12 products)</summary>

| Project | Route | One-line positioning |
| --- | --- | --- |
| [ChatGPT dots](agents/chatgpt-dots.md) | Consumer personal agent | OpenAI's always-on agent in ChatGPT — GPT-6 Astra, its own cloud computer, reachable in Slack, Teams and by call; Pro only, not in Europe |
| [Gemini Task](agents/gemini-task.md) | Consumer personal agent | The Gemini app's agent mode (formerly Spark) — scheduled work across Google Workspace and Chrome, with a published confirmation list |
| [Claude (Cowork)](agents/claude-cowork.md) | Consumer personal agent | Cowork merged into the Claude app — tasks that schedule and keep running in an isolated cloud session, three named approval modes |
| [Claude Duet](agents/claude-duet.md) | Consumer personal agent | Anthropic's separate proactive-agent app: morning brief, checks your accounts every few hours, own VM, approval before it sends, pays, signs or deletes; US waitlist |
| [Muse (Meta)](agents/meta-muse.md) | Consumer personal agent | Meta's errand agent in its own app and WhatsApp — a dedicated cloud VM, one-time card payments, US limited testing, open in Singapore |
| [Grok Bot](agents/grok-bot.md) | Consumer personal agent | xAI's team of always-on Bots sharing one cloud computer in Cursor's cloud, with saved skills on a schedule |
| [Cue (Manus)](agents/manus-cue.md) | Consumer personal agent | Manus's personal-agent app where each agent has its own email, phone number, wallet and computer; invite-only early access |
| [Doubao](agents/doubao.md) | Consumer personal agent | ByteDance's assistant with a work-task mode and a phone-OS assistant that operates other apps on partner phones (Beta) |
| [Qwen app](agents/qwen-app.md) | Consumer personal agent | Alibaba's consumer app turned errand agent — deliverables, scheduled tasks, food, hotels and government services |
| [AutoGLM](agents/autoglm.md) | Consumer personal agent | Zhipu's phone-use agent: a free app on cloud phones, plus the Apache-2.0 Open-AutoGLM framework for your own phone |
| [Yuanbao](agents/yuanbao.md) | Consumer personal agent | Tencent's free assistant with a Hy3 Agent feature that delivers office files — the consumer end of WorkBuddy's model family |
| [Today](agents/today-ai.md) | Consumer personal agent | A personal AI assistant built on memory and proactive help: morning and evening briefings, scheduled tasks, cloud computers and a Chrome extension; China-edition data kept in mainland China in principle, plus an international edition |

</details>

## Example Reading Paths

If you are still deciding where to begin, use one of these quick routes and then branch out.

| If you sound like this... | Follow this path | What it helps you answer |
| --- | --- | --- |
| I want a day-to-day coding agent and need to choose terminal vs editor | [Aider](agents/aider.md) → [Claude Code](agents/claude-code.md) → [terminal coding CLI comparison](comparisons/coding-cli-agents.md) → [Cursor](agents/cursor.md) → [Cline](agents/cline.md) → [coding automation guide](use-cases/coding-automation.md) | Which vendor CLI fits your model, terminal-first local loop vs editor-led flow vs approval-first control |
| I already like Claude Code or Codex but want stronger orchestration | [Claude Code](agents/claude-code.md) → [oh-my-claudecode](agents/oh-my-claudecode.md) → [Codex](agents/codex.md) → [oh-my-codex](agents/oh-my-codex.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | When the base agent is enough and when a workflow layer actually adds value |
| I want to understand how the 2026 model race changes agent choice | [Claude Fable 5.2](agents/claude-fable-5.md) → [Claude Opus 5](agents/claude-opus-5.md) → [GPT-6 Astra](agents/gpt-6-astra.md) → [Codex](agents/codex.md) → [Claude Code](agents/claude-code.md) → [market events](market-events.md) | How the frontier tiers and the default tier under them shift the capability ceiling, and what it means for product choice |
| I want a dedicated AI IDE instead of stitching tools together | [Cursor](agents/cursor.md) → [Windsurf](agents/windsurf.md) → [GitHub Copilot](agents/github-copilot.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Dedicated AI editor vs ecosystem platform |
| I want to hand off tickets and check back later | [Codex](agents/codex.md) → [Jules](agents/jules.md) → [Devin](agents/devin.md) → [Claude Managed Agents](agents/claude-managed-agents.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Async cloud delegation vs managed background automation |
| I need something open-source or self-hosted | [Aider](agents/aider.md) → [OpenHands](agents/openhands.md) → [Goose](agents/goose.md) → [Hermes Agent](agents/hermes-agent.md) → [capabilities](capabilities/README.md) | Terminal control, open-source execution, and local runtime ownership |
| I am building an internal agent stack, not buying a product | [LangChain](agents/langchain.md) → [LangGraph](agents/langgraph.md) → [capabilities](capabilities/README.md) → [mainstream matrix](comparisons/mainstream-agent-landscape.md) | Framework vs runtime vs product boundaries |

## Disclaimer

Star counts and 7-day gains are point-in-time GitHub snapshots taken when the repo is updated; numbers shift quickly between weekly refreshes and small rounding differences are expected. Project descriptions, vendors, and capability summaries reflect public information at the time of writing and may change as projects evolve, get acquired, or pivot. This map is selection guidance — not endorsement, financial advice, or a production-readiness guarantee. Verify against each project's own docs before committing to a choice.