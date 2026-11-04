# Category Rankings

[English](../README.md) | [中文](../zh/rankings/README.md)

The home-page [heat ranking](../README.md#recent-heat-ranking) sorts by **weekly star gain** — it shows momentum. The boards on this page sort by **current total stars** — they show the standing stock of each category. Read them together: a project high here but absent from the heat table is established; a project low here but topping the heat table is breaking out.

> **Last updated:** 2026-11-04 · **Star counts:** from the most recent tracked fetch · **Sort:** current total stars, weekly gain shown for reference

> **Note on this edition's "Weekly gain" column:** the figures below cover **2026-10-28 → 2026-11-04**: 7 calendar days, about 7.45 by fetch time, against about 6.24 in the previous edition, so raw gains overstate any speed-up by about 19%. This edition replaces the one dated 2026-11-03. Repos that entered tracking (Graphify, ECC, Orca, claude-mem, Paperclip) show no gain until next edition.

## Ranking Trend

How the weekly heat top 10 has shifted since tracking began — each line is one project, higher is a better rank, breaks mean the project fell off the board that week:

<p align="center">
  <img src="../assets/heat-trend-en.svg" alt="Weekly heat ranking trend (bump chart)" width="100%" />
</p>

The through-line so far: Hermes Agent owned the early boards, the `.claude/skills` wave took over from late May, and from mid-June the top three ranks rotated almost entirely among curated skills collections. **That line bent in September.** For two consecutive windows (2026-09-17 and 2026-09-24) both top-two seats were held by coding agents — [Open Code Review](../agents/open-code-review.md) and [DeepSeek Harness](../agents/deepseek-harness.md) — the first all-agent top two since **2026-05-08**, before the wave began. On 2026-09-30 the top two split again — DeepSeek Harness took its first #1 with [mattpocock/skills](https://github.com/mattpocock/skills) at #2 — and on 2026-10-07 they swapped back, mattpocock retaking #1. The wave rose to five of ten on 09-30 on the strength of two `anthropics/*` collections, then fell to **three** on 10-07 when both left; what remains is the three general collections that have carried it since June. Read the wave as durable but narrow, not as broadening. And read single-window jumps with care, because the board's own record on them is poor — jcode, addyosmani, Codex CLI, K-Dense, TradingAgents, Claude Code and, most recently, CLI-Anything all fell back the window after the one that made them look like a trend. Open Code Review and anthropics/financial-services are the counterexamples that held a second window; both then kept falling — Open Code Review for three windows running, financial-services off the board by its third. On 2026-10-14 the picture firmed up rather than moved: mattpocock/skills held #1 on its largest 7-day gain on record (+11,878) and DeepSeek Harness held #2 on a fourth straight slowdown; the wave rose to **four** seats as [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) returned, and the spike rule paid out once more (OpenHuman gave back 65% the window after its ~12x jump) while Open Code Review, the counterexample, re-accelerated 93% after three slowdowns. On 2026-10-21 the top held and the middle churned: mattpocock/skills kept #1 a third straight window, DeepSeek Harness kept #2 and passed Hermes Agent in total stars, and [OpenCode](../agents/opencode.md) jumped to #3 on its 2.0 launch. Below them, three repos gained 4.7 to 7.5 times their previous window with no documented cause (K-Dense, CLI-Anything, Ruflo), giving the infra layer two seats for the first time since 08-27, and Open Code Review gave back 76% and left — so it, too, did not hold. [Pi](../agents/pi.md)'s 20-window run ended, the longest run on the board ever to end; Hermes Agent (27, every window), Superpowers and mattpocock/skills (22 each) are the runs still going. On 2026-10-28 the board cooled hard (15 of 57 repos accelerated, 42 slowed) and the spike rule paid out on all three of the previous window's unexplained jumps: K-Dense gave back 68% and left, CLI-Anything and Ruflo gave back 56% and 52% but kept seats because the bar fell too, and even OpenCode's documented breakout halved. DeepSeek Harness took #1 for the second time on a flat gain as mattpocock/skills slowed 38% — mattpocock crossed 300k but stayed behind Superpowers — and TradingAgents became the new unexplained spike at #3. The wave held four seats, all general collections for the first time since 08-27; Hermes Agent (28), Superpowers and mattpocock/skills (23 each) are the runs still going. The 2026-11-04 edition replaced one dated 11-03 that ran a day early. By fetch time its window ran about 7.45 days against about 6.24, and on that basis the top held steady, with 21 of 57 repos accelerating: DeepSeek Harness held #1 for the first time, Superpowers rose 46% with no documented cause and now leads mattpocock/skills by 324, and last window's spikes split, TradingAgents keeping a seat at #4 while Gemini CLI gave back 89%. Infra lost both seats. The wave held four seats, all general collections for a second straight window; Hermes Agent (29), Superpowers and mattpocock/skills (24 each) are the runs still going.

## Agent Board

End-to-end agents — products you point at a task. Verticals are ranked separately in [agent verticals](agent-verticals.md).

<!-- auto:board:agent -->
| Rank | Project | Vertical | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [OpenClaw](https://github.com/openclaw/openclaw) | General assistant | 393.9k | +668 | In scope · [profile](../agents/openclaw.md) |
| #2 | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | Coding | 271.3k | +7,781 | In scope · [profile](../agents/deepseek-harness.md) |
| #3 | [Hermes Agent](https://github.com/nousresearch/hermes-agent) | General assistant | 260.3k | +2,631 | In scope · [profile](../agents/hermes-agent.md) |
| #4 | [OpenCode](https://github.com/anomalyco/opencode) | Coding | 224.4k | +2,120 | In scope · [profile](../agents/opencode.md) |
| #5 | [AutoGPT](https://github.com/significant-gravitas/autogpt) | General assistant | 187.9k | +99 | In scope · [profile](../agents/autogpt.md) |
| #6 | [Claude Code](https://github.com/anthropics/claude-code) | Coding | 154.4k | +874 | In scope · [profile](../agents/claude-code.md) |
| #7 | [Codex CLI](https://github.com/openai/codex) | Coding | 133.0k | +1,790 | In scope · [profile](../agents/codex.md) |
| #8 | [TradingAgents](https://github.com/tauricresearch/tradingagents) | Finance | 120.4k | +3,266 | Out of scope |
| #9 | [Browser Use](https://github.com/browser-use/browser-use) | General assistant | 120.0k | +679 | In scope · [profile](../agents/browser-use.md) |
| #10 | [Pi](https://github.com/earendil-works/pi) | Coding | 119.9k | +1,635 | In scope · [profile](../agents/pi.md) |
| #11 | [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Coding | 108.7k | +140 | In scope · [profile](../agents/gemini-cli.md) |
| #12 | [OpenHands](https://github.com/openhands/openhands) | Coding | 92.6k | +599 | In scope · [profile](../agents/openhands.md) |
| #13 | [Cline](https://github.com/cline/cline) | Coding | 71.3k | +357 | In scope · [profile](../agents/cline.md) |
| #14 | [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | General assistant | 68.8k | +97 | In scope · [profile](../agents/open-interpreter.md) |
| #15 | [Goose](https://github.com/aaif-goose/goose) | General assistant | 56.2k | +377 | In scope · [profile](../agents/goose.md) |
| #16 | [Aider](https://github.com/aider-ai/aider) | Coding | 49.9k | +159 | In scope · [profile](../agents/aider.md) |
| #17 | [Open Code Review](https://github.com/alibaba/open-code-review) | Coding | 49.4k | +861 | In scope · [profile](../agents/open-code-review.md) |
| #18 | [OpenHuman](https://github.com/tinyhumansai/openhuman) | General assistant | 42.5k | +158 | In scope · [profile](../agents/openhuman.md) |
| #19 | [CodeWhale](https://github.com/codewhale-hq/codewhale) | Coding | 41.2k | +30 | In scope · [profile](../agents/codewhale.md) |
| #20 | [Continue](https://github.com/continuedev/continue) | Coding | 36.4k | +58 | In scope · [profile](../agents/continue.md) |
| #21 | [Qwen Code](https://github.com/qwenlm/qwen-code) | Coding | 29.0k | +229 | In scope · [profile](../agents/qwen-code.md) |
| #22 | [Grok Build](https://github.com/xai-org/grok-build) | Coding | 27.7k | +108 | In scope · [profile](../agents/grok-build.md) |
| #23 | [jcode](https://github.com/1jehuang/jcode) | Coding | 21.4k | +199 | In scope · [profile](../agents/jcode.md) |
| #24 | [SWE-agent](https://github.com/swe-agent/swe-agent) | Coding | 20.7k | +63 | In scope · [profile](../agents/swe-agent.md) |
| #25 | [OpenHarness](https://github.com/hkuds/openharness) | Coding | 16.2k | +51 | In scope · [profile](../agents/openharness.md) |
| #26 | [QM](https://github.com/yc-software/qm) | General assistant | 15.6k | +82 | In scope · [profile](../agents/qm.md) |
| #27 | [MiMoCode](https://github.com/xiaomimimo/mimo-code) | Coding | 13.7k | +11 | In scope · [profile](../agents/mimocode.md) |
| #28 | [Omnigent](https://github.com/omnigent-ai/omnigent) | Coding | 11.2k | +115 | In scope · [profile](../agents/omnigent.md) |
| #29 | [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent) | Coding | 9.1k | +184 | In scope · [profile](../agents/mini-swe-agent.md) |
| #30 | [ZCode](https://github.com/zai-org/zcode) | Coding | 8.5k | +152 | In scope · [profile](../agents/zcode.md) |
| #31 | [Kimi Code](https://github.com/moonshotai/kimi-code) | Coding | 8.1k | +88 | In scope · [profile](../agents/kimi-code.md) |
| #32 | [CoStrict](https://github.com/zgsm-ai/costrict) | Coding | 4.5k | +2 | In scope · [profile](../agents/costrict.md) |
<!-- /auto:board:agent -->

## Agent Infra Board

The layer under the agents — frameworks, orchestration, memory and context, gateways, and workflow engines. These are not agents you "run at a task"; they are what agent builders assemble on.

<!-- auto:board:infra -->
| Rank | Project | Group | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [n8n](https://github.com/n8n-io/n8n) | Workflow | 209.5k | +715 | In scope · [profile](../agents/n8n.md) |
| #2 | [LangChain](https://github.com/langchain-ai/langchain) | Framework | 149.0k | +424 | In scope · [profile](../agents/langchain.md) |
| #3 | [Graphify](https://github.com/graphify-labs/graphify) | Memory & context | 141.9k | — | In scope · [profile](../agents/graphify.md) |
| #4 | [Orca](https://github.com/stablyai/orca) | Orchestration | 114.6k | — | In scope · [profile](../agents/orca.md) |
| #5 | [claude-mem](https://github.com/thedotmack/claude-mem) | Memory & context | 112.0k | — | In scope · [profile](../agents/claude-mem.md) |
| #6 | [Paperclip](https://github.com/paperclipai/paperclip) | Orchestration | 110.9k | — | In scope · [profile](../agents/paperclip.md) |
| #7 | [Ruflo](https://github.com/ruvnet/ruflo) | Orchestration | 80.8k | +1,093 | In scope · [profile](../agents/ruflo.md) |
| #8 | [CodeGraph](https://github.com/colbymchenry/codegraph) | Memory & context | 76.4k | +843 | In scope · [profile](../agents/codegraph.md) |
| #9 | [LiteLLM](https://github.com/berriai/litellm) | Gateway & runtime | 62.7k | +493 | In scope · [profile](../agents/litellm.md) |
| #10 | [CrewAI](https://github.com/crewaiinc/crewai) | Framework | 60.5k | +294 | In scope · [profile](../agents/crewai.md) |
| #11 | [CLI-Anything](https://github.com/hkuds/cli-anything) | Gateway & runtime | 58.2k | +825 | In scope · [profile](../agents/cli-anything.md) |
| #12 | [Flowise](https://github.com/flowiseai/flowise) | Workflow | 55.5k | +17 | In scope · [profile](../agents/flowise.md) |
| #13 | [LlamaIndex](https://github.com/run-llama/llama_index) | Framework | 52.8k | +107 | In scope · [profile](../agents/llamaindex.md) |
| #14 | [LangGraph](https://github.com/langchain-ai/langgraph) | Orchestration | 44.4k | +427 | In scope · [profile](../agents/langgraph.md) |
| #15 | [Langfuse](https://github.com/langfuse/langfuse) | Observability & evals | 37.0k | +364 | In scope · [profile](../agents/langfuse.md) |
| #16 | [agentmemory](https://github.com/rohitg00/agentmemory) | Memory & context | 30.1k | +178 | Watchlist |
| #17 | [Letta (MemGPT)](https://github.com/letta-ai/letta) | Memory & context | 25.3k | +76 | In scope · [profile](../agents/memgpt.md) |
| #18 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Framework | 14.5k | +184 | In scope · [profile](../agents/microsoft-agent-framework.md) |
| #19 | [Trail Code (Graft)](https://github.com/trailhq/trail-code) | Memory & context | 11.1k | +258 | In scope · [profile](../agents/graft.md) |
| #20 | [TrueForge](https://github.com/truefoundry/trueforge) | Framework | 6.4k | +46 | In scope · [profile](../agents/trueforge.md) |
| #21 | [eve](https://github.com/vercel/eve) | Framework | 5.8k | +89 | In scope · [profile](../agents/eve.md) |
<!-- /auto:board:infra -->

## Skill Board

Skill collections, skill frameworks, and agent methodology — content assets rather than agent surfaces. Most are tracked as watchlist entries; the framework end is profiled through [Superpowers](../agents/superpowers.md). Focus areas are ranked separately in [skill verticals](skill-verticals.md).

<!-- auto:board:skill -->
| Rank | Project | Focus | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [Superpowers](https://github.com/obra/superpowers) | Curated collections | 311.9k | +5,785 | In scope · [profile](../agents/superpowers.md) |
| #2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Curated collections | 311.6k | +6,918 | Watchlist |
| #3 | [ECC](https://github.com/affaan-m/ecc) | Curated collections | 296.6k | — | In scope · [profile](../agents/ecc.md) |
| #4 | [anthropics/skills](https://github.com/anthropics/skills) | Curated collections | 187.2k | +2,979 | Watchlist |
| #5 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Curated collections | 113.1k | +2,036 | Watchlist |
| #6 | [scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills) | Academic & scientific | 56.0k | +1,068 | Watchlist |
| #7 | [academic-research-skills](https://github.com/imbad0202/academic-research-skills) | Academic & scientific | 55.2k | +1,078 | Watchlist |
| #8 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Finance | 41.0k | +179 | Out of scope |
| #9 | [12-factor-agents](https://github.com/humanlayer/12-factor-agents) | Methodology | 27.0k | +75 | Out of scope |
<!-- /auto:board:skill -->

## Vertical Rankings

- [Agent verticals](agent-verticals.md) — coding, general assistant, finance
- [Skill verticals](skill-verticals.md) — curated collections, academic & scientific research, finance, methodology

Boards and the trend chart are regenerated by `scripts/render-rankings.py` and `scripts/render-trend.py` on every publish — do not edit the marked table blocks by hand.
