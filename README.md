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

> **Last updated:** 2026-10-21 · **Snapshot window:** 2026-10-14 → 2026-10-21 (gain since last update, **7 days** against last window's 7, so the two columns compare directly for a second straight week) · **Star counts:** checked at update time

Project names link to the upstream GitHub repo. When this map has a written profile, it is linked separately in the "Map status" column.

| Rank | Project | Current stars | Snapshot gain | Map status | How to read it |
| --- | --- | --- | --- | --- | --- |
| #1&nbsp;(=) | [mattpocock/skills](https://github.com/mattpocock/skills) | 299.2k | +8,787 | Watchlist (Skills Wave) | **Holds #1** for a third straight window, its 15th in 27, on a gain down 26% from last window's 7-day record. **796 short of 300k**; 1,673 clear of #2 (last window: 7,315). No release in the window |
| #2&nbsp;(=) | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 256.5k | +7,114 | In scope · [profile](agents/deepseek-harness.md) | Up **56%**, ending four straight slowdowns, and its largest 7-day gain on record. Past **250k** and **255k**, and now **ahead of Hermes Agent in total stars** (256,509 against 255,734). Five pre-releases in the window, ending at `rc.2` (Oct 17) with support for DeepSeek's new V4.1-Flash-1017 |
| #3&nbsp;(↑) | [OpenCode](https://github.com/anomalyco/opencode) | 219.4k | +6,043 | In scope · [profile](agents/opencode.md) | Up **369%**, more than three times its previous best (1,920 on 09-17), and its first podium seat. **OpenCode 2.0** was announced Oct 12 and its Hacker News launch thread (887 points) ran on Oct 14; 2.x ships from a separate branch, not as a GitHub Release. Past **215k** |
| #4&nbsp;(new) | [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 53.4k | +4,627 | Watchlist (Skills Wave) | Up **373%**, its first seat since 09-06 and its 4th in 27 windows. Past **50k**, and now larger than academic-research-skills. No release and no documented cause: treated as a spike |
| #5&nbsp;(=) | [Superpowers](https://github.com/obra/superpowers) | 302.8k | +3,960 | In scope · [profile](agents/superpowers.md) | Up 44%. **Crossed 300k** (302,834), the second repository this map tracks past 300k after OpenClaw |
| #6&nbsp;(new) | [CLI-Anything](https://github.com/HKUDS/CLI-Anything) | 55.8k | +3,631 | In scope · [profile](agents/cli-anything.md) | Up **647%**, the largest jump in the window, with no commit since Sept 22 and no release since June: **no documented cause**. First seat since 05-23, its only previous one. Past **55k** |
| #7&nbsp;(new) | [Ruflo](https://github.com/ruvnet/ruflo) | 78.1k | +3,445 | In scope · [profile](agents/ruflo.md) | Up **480%**, its largest gain in this map's raw record (since 07-16), and its first seat since 09-09. A vendor press release went out Oct 13, the day before the window opened, and 13 releases shipped inside it. Past **75k** |
| #8&nbsp;(↓) | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 109.1k | +2,704 | Watchlist (Skills Wave) | Down 35% after two accelerations. **872 short of 110k** |
| #9&nbsp;(↓) | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 255.7k | +2,105 | In scope · [profile](agents/hermes-agent.md) | Up 13%, a second straight acceleration. **Present in all 27 recorded windows**; past **255k**, but passed by DeepSeek Harness in total stars |
| #10&nbsp;(new) | [Claude Code](https://github.com/anthropics/claude-code) | 152.7k | +1,920 | In scope · [profile](agents/claude-code.md) | Up **80%**: its third seat (after 09-24 and 10-07) and its second-largest 7-day gain on record, after 09-24's 2,108. Eight releases (`v2.1.299`–`v2.1.306`), no default-model change |

- Heat is useful for discovery, not for selection by itself.
- **This window is 7 days against last window's 7**, so raw gains compare directly for a second straight week; no weekly-rate conversion is applied below.
- **Fewer repos sped up than last window, but the top heated hard.** 31 of 57 measured repos accelerated, 24 slowed and two were flat (last window 38 of 55 accelerated). The ten seats together gained **44,336** against 33,751 (+31%), and the bar for #10 rose **78%** (1,078 → 1,920). Four repos gained 4.7 to 7.5 times what they did last window — [OpenCode](agents/opencode.md), [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills), [CLI-Anything](agents/cli-anything.md) and [Ruflo](agents/ruflo.md) — and only OpenCode's has a documented trigger.
- **[mattpocock/skills](https://github.com/mattpocock/skills) holds #1 for a third straight window**, its 15th in 27, on +8,787 — down 26% from last window's 7-day record but still the largest gain on the board. Its lead over #2 shrank from 7,315 to **1,673**, and its margin over the other three general collections combined from 3,899 to **530**. It is **796 stars short of 300k** and 3,630 behind [Superpowers](agents/superpowers.md) (last window 8,457); at this window's pace that gap closes inside a week. No release in the window; the only commit was a PR merged on Oct 19.
- **[DeepSeek Harness](agents/deepseek-harness.md) re-accelerated and passed [Hermes Agent](agents/hermes-agent.md) in total stars.** +7,114 (up 56%) ends four straight slowdowns and is its largest 7-day gain on record (its rate peak is still the 8-day 09-17 window, ~8,800/week). At 256,509 against 255,734 it is now the largest agent this map tracks after OpenClaw; last window Hermes led 253,629 to 249,395. The window carried five pre-releases ending at `dsh-v0.2.1-rc.2` (Oct 17), which added DeepSeek-V4.1-Flash-1017 on the day DeepSeek released it — and DeepSeek's release note names the harness as the client to use. Both repos gained; Hermes simply gained less (+2,105, still up 13%).
- **[OpenCode](agents/opencode.md) had the one documented breakout: +6,043, up 369%**, from #8 to #3, more than three times its previous best. **OpenCode 2.0** was announced on Oct 12 and its Hacker News launch thread (887 points) ran on Oct 14, the window's first day; existing installs move with `opencode upgrade --major` (added in v1.19.0), and 2.x ships from its own branch rather than as a GitHub Release. Separately, on **Oct 17** a post on OpenCode's X account reporting a credential leak was submitted to Hacker News as "OpenCode Hacked: User credentials leaked" (973 points), and a repository issue the next day refers to "the Console breach". This map could not read the vendor's statement directly and does not repeat scope figures from second-hand posts — if you use OpenCode's hosted Console, check the vendor's notice and rotate keys.
- **Three spikes with no documented cause, and two of them are infra.** [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) (+373%, #4) had no release; [CLI-Anything](agents/cli-anything.md) (+647%, #6) has had no commit since Sept 22; [Ruflo](agents/ruflo.md) (+480%, #7) had a vendor press release the day before the window and 13 releases inside it, but nothing ties either to the gain. CLI-Anything and Ruflo give the infra layer **two seats for the first time since 08-27** and its first seat of any kind since 09-09. By this board's rule each is a spike until a second window confirms it — and CLI-Anything's last jump, on 09-30, gave back 49% the next window.
- **[Pi](agents/pi.md)'s 20-window run ended — the longest run on the board ever to end.** It fell from #6 to 11th on a gain down only 9% (+1,810), squeezed out by the higher bar rather than by a collapse. The previous longest run to end was [anthropics/skills](https://github.com/anthropics/skills)' 15 (ended 09-09). Three long runs remain: Hermes Agent 27 (every recorded window), Superpowers 22, mattpocock/skills 22; DeepSeek Harness and OpenCode are next at 7.
- **The skills wave holds 4 of 10** (#1, #4, #5, #8) with a different fourth seat: K-Dense replaced academic-research-skills and passed it in total stars. The other six seats split four agents (#2, #3, #9, #10) and two infra projects (#6, #7).
- **The model layer moved on price and on retirement, not on defaults.** (1) **Meta's Muse Wonder** (Oct 12, one day inside last window; this map missed it) is on the Meta Model API at **$4 / $20 with $0.20 cached input** — Opus 5.5's sticker and cache read exactly; the larger Muse Wonder Full is subscription-only. (2) **OpenAI retired GPT-5.5 from Codex and ChatGPT** on Oct 14 for ChatGPT sign-in, pointing users to GPT-6.1 Sol; the API is unaffected. (3) Two open-weight releases: **Meta's Muse Spark Open** (Oct 15; 816B / 42B active, 1M context, Muse Model License with "limited commercial terms") and **DeepSeek-V4.1-Flash-1017** (Oct 17). (4) Anthropic's **Code Review** went generally available for Team and Enterprise on Oct 15. **No tracked coding agent changed its default model for a third straight window**: [Gemini CLI](agents/gemini-cli.md) `v0.65.0` did not adopt Gemini 4 Argon, and [Codex CLI](agents/codex.md) `rust-v0.163.0` keeps GPT-6.1 Sol. Codex `0.162.0` (Oct 8) did change *how* the default is resolved — the TUI now follows the app server's model default unless overridden — which means OpenAI can change the effective default without shipping a release. The [cost table](comparisons/cost-and-benchmarks.md) adds Muse Wonder and Muse Spark Open, fills GPT-5.5's price and the GPT-5.6 cache-read cells from OpenAI's pricing page, and relabels the Muse Spark rows to 1.3 (shipped Sept 2 at the same prices). Details in [market-events](market-events.md).
- **A correction this map owed from last week:** the 10-14 refresh corrected the [CodeWhale](agents/codewhale.md) profile to provider-neutral but left the old "DeepSeek + MiMo" one-liner in the catalog rows on this page and in [agents/README](agents/README.md). Those rows are now fixed in place.
- Milestones, checked against the raw counts rather than the rounded column: **Superpowers 300k**, DeepSeek Harness **250k** and **255k**, Hermes Agent **255k**, mattpocock/skills **295k**, OpenCode **215k**, scientific-agent-skills **50k**, CLI-Anything **55k**, Ruflo **75k**, Codex CLI **130k**, [anthropics/financial-services](https://github.com/anthropics/financial-services) **40k** and Trail Code **10k** (10,563). Near misses: mattpocock/skills is **796 short of 300k**, [CrewAI](agents/crewai.md) 53 short of 60k, [agentmemory](https://github.com/rohitg00/agentmemory) 263 short of 30k, [Aider](agents/aider.md) 319 short of 50k, [CodeGraph](agents/codegraph.md) 425 short of 75k, OpenCode 573 short of 220k.
- [OpenClaw](agents/openclaw.md) remains the absolute leader at 392.6k stars (+705, up 75%); it is profiled but stays out of the gain-ranked table because reliable week-over-week deltas for a project this large are noisy.

<details>
<summary>More window notes: skills-wave share, OpenClaw, and everything growing outside the top 10</summary>

- The `.claude/skills` wave **holds four of the top ten** for a second window: #1, #4, #5 and #8. Three are general collections; the fourth is now [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) (K-Dense), which took the research seat from [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) and, at 53,434 against 53,269, also passed it in total stars to become the larger of the two research collections. [mattpocock/skills](https://github.com/mattpocock/skills) at +8,787 out-gained the other three general collections combined (+3,960 Superpowers, +2,704 addyosmani, +1,593 anthropics/skills = 8,257) by **530** — the third straight window the "one directory is the wave" read holds, on a margin that shrank from 3,899. Policy unchanged: curated collections are tracked as Skills Wave entries, the framework end is covered through [Superpowers](agents/superpowers.md).
- Just off the table: [Pi](agents/pi.md) 116.9k (+1,810) at 11th, down 9% and out after 20 straight windows (see above); [anthropics/skills](https://github.com/anthropics/skills) 182.6k (+1,593) at 12th, up 52%; [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 53.3k (+1,354) at 13th and [TradingAgents](https://github.com/TauricResearch/TradingAgents) 112.5k (+1,336) at 14th — **both accelerated (+13%, +24%) and still lost their seats**, because the bar for #10 rose 78% (1,078 → 1,920); and [Codex CLI](agents/codex.md) 130.2k (+1,089) at 15th, up 4% and past 130k. OpenClaw is excluded from the board, so these off-board positions are counted the same way.
- **Last window's two reversals did not both hold.** [Open Code Review](agents/open-code-review.md) gave back **76%** (2,966 → 716) and fell from #4 to 19th, ending a five-window run on the board; it is now about 2x its pre-Trending ~370/week. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) slowed 35% but kept a seat at #8. [LiteLLM](agents/litellm.md), last window's unexplained +150%, gave back 49% (+490, 23rd), and [OpenHuman](agents/openhuman.md) halved again (+234).
- **[anthropics/financial-services](https://github.com/anthropics/financial-services) crossed 40k** (40,597, +813, down 9%, 17th). [AutoGPT](agents/autogpt.md) is back to +123 after last window's −116.
- Continuing to grow but outside the top 10 by gain (raw 7-day figures): [Pi](agents/pi.md) 116.9k (+1,810), [anthropics/skills](https://github.com/anthropics/skills) 182.6k (+1,593), [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 53.3k (+1,354), [TradingAgents](https://github.com/TauricResearch/TradingAgents) 112.5k (+1,336), [Codex CLI](agents/codex.md) 130.2k (+1,089), [n8n](agents/n8n.md) 208.2k (+868), [anthropics/financial-services](https://github.com/anthropics/financial-services) 40.6k (+813), [Browser Use](agents/browser-use.md) 118.7k (+802), [Open Code Review](agents/open-code-review.md) 47.8k (+716), [OpenHands](agents/openhands.md) 91.5k (+594), [Trail Code (Graft)](agents/graft.md) 10.6k (+574), [CodeGraph](agents/codegraph.md) 74.6k (+535), [LiteLLM](agents/litellm.md) 61.7k (+490), [Cline](agents/cline.md) 70.7k (+402), [LangGraph](agents/langgraph.md) 43.6k (+391), [jcode](agents/jcode.md) 21.1k (+382), [LangChain](agents/langchain.md) 148.2k (+354), [agentmemory](https://github.com/rohitg00/agentmemory) 29.7k (+333), [Langfuse](agents/langfuse.md) 36.1k (+321), [CrewAI](agents/crewai.md) 59.9k (+270), [ZCode](agents/zcode.md) 8.1k (+261), [OpenHuman](agents/openhuman.md) 42.2k (+234), [Goose](agents/goose.md) 55.5k (+204), [mini-swe-agent](agents/mini-swe-agent.md) 8.7k (+192), [Qwen Code](agents/qwen-code.md) 28.6k (+148), [Omnigent](agents/omnigent.md) 10.9k (+142), [Gemini CLI](agents/gemini-cli.md) 107.5k (+142), [12-factor-agents](https://github.com/humanlayer/12-factor-agents) 26.8k (+139), [Aider](agents/aider.md) 49.7k (+139), [AutoGPT](agents/autogpt.md) 187.7k (+123), [Microsoft Agent Framework](agents/microsoft-agent-framework.md) 14.2k (+123), [Grok Build](agents/grok-build.md) 27.5k (+114), [LlamaIndex](agents/llamaindex.md) 52.6k (+105), [TrueForge](agents/trueforge.md) 6.3k (+97), [Letta (MemGPT)](agents/memgpt.md) 25.2k (+86), [Kimi Code](agents/kimi-code.md) 7.9k (+83), [eve](agents/eve.md) 5.6k (+75), [QM](agents/qm.md) 15.5k (+67), [Continue](agents/continue.md) 36.3k (+61), [SWE-agent](agents/swe-agent.md) 20.6k (+56), [Open Interpreter](agents/open-interpreter.md) 68.6k (+51), [MiMoCode](agents/mimocode.md) 13.7k (+43), [OpenHarness](agents/openharness.md) 16.0k (+39), [CodeWhale](agents/codewhale.md) 41.1k (+14), [Flowise](agents/flowise.md) 55.5k (+14), [CoStrict](agents/costrict.md) 4.5k (+3)

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

- **The `.claude/skills` wave holds four seats, and one directory is most of it** (May 2026 → ongoing): curated skill collections and skills frameworks have held between two and six of the weekly heat top 10 for five months, and the count rotates rather than sitting still — 6/10, then 2/10, 3/10, 4/10, 5/10, 3/10, 4/10, and **4 of 10** again (2026-10-21). The fourth seat is a research collection again, but a different one: [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) (K-Dense) replaced academic-research-skills on an unexplained +373%. The core remains [mattpocock/skills](https://github.com/mattpocock/skills), [Superpowers](agents/superpowers.md) and [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills); Superpowers crossed **300k** and mattpocock is 796 short of it. mattpocock held #1 a third straight window and still out-gained the other three general collections combined, but by 530 stars, down from 3,899 — the key-person risk this map has flagged since June is still there, just less lopsided than last window. This map profiles the framework end through [Superpowers](agents/superpowers.md) and tracks collections on the [skill boards](rankings/skill-verticals.md).
- **The model layer became a budget decision — and the ladder now has every rung filled at both vendors**: [Claude Fable 5.1](agents/claude-fable-5.md) (Sept 1) and [GPT-6 Astra](agents/gpt-6-astra.md) (Sept 3) still both list at **$10 / $50**; below them sit **Opus 5.5** ($4 / $20, Sept 22), the two mid tiers **Sonnet 5.5** and **GPT-6.1 Sol** (both $2 / $10, Sept 28–29, both their vendor's coding-agent default), and now the floor: **GPT-6 Luna** ($0.10 / $0.50, Sept 22) and **Claude Haiku 5.5** (Oct 7, $0.10 / $0.50 for prompts up to 100K tokens, $0.50 / $2.50 above). Google joined the priced field on **Oct 13** when **Gemini 4 Argon** opened to the paid API at $2 / $10 through Nov 30, then $4 / $20, and Meta's **Muse Wonder** (Oct 12) lands on **$4 / $20 with $0.20 cache reads** — Opus 5.5's numbers exactly, which makes $4 / $20 a three-vendor price point. The column this map said separated the two mid tiers has closed: Anthropic's pricing page now lists Sonnet 5.5 cache reads at **$0.10/M**, not the $0.20 recorded from the Sept 28 changelog (Claude Code `v2.1.296` corrected its own figure on Oct 9), so Sonnet 5.5 and GPT-6.1 Sol are identical on sticker and on cache. What still separates them is long-context shape (OpenAI reprices the whole request past 272k input tokens; Anthropic does not; Haiku 5.5 prices by prompt length). See [cost & benchmarks](comparisons/cost-and-benchmarks.md).
- **Product boundaries are collapsing upward**: OpenAI merged Codex into the ChatGPT app (July 9), and at DevDay (Sept 29) moved it further off the laptop with reusable cloud environments usable from any device — on the OpenAI side, "which coding agent" keeps turning into "how you use ChatGPT." The bundled default model changed twice in a month: [GPT-6 Astra](agents/gpt-6-astra.md) from `rust-v0.153.4` (Sept 4), then **GPT-6.1 Sol** from `rust-v0.159.1` (Sept 29), carried to the main release line by `rust-v0.161.0` (Oct 7). Since `0.162.0` (Oct 8) the TUI also follows the server's model default, so the effective default can change without a release, and on **Oct 14** OpenAI retired GPT-5.5 from Codex and ChatGPT for ChatGPT sign-in. Three windows have now passed with no tracked coding agent changing a default in a release. If you run Codex on defaults, pin the model id anyway — and know that a pinned model can be retired under you; the product will not hold either still for you. See [Codex](agents/codex.md).

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