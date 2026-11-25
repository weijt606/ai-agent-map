# Category Rankings

[English](../README.md) | [中文](../zh/rankings/README.md)

The home-page [heat ranking](../README.md#recent-heat-ranking) sorts by **weekly star gain** — it shows momentum. The boards on this page sort by **current total stars** — they show the standing stock of each category. Read them together: a project high here but absent from the heat table is established; a project low here but topping the heat table is breaking out.

> **Last updated:** 2026-11-25 · **Star counts:** from the most recent tracked fetch · **Sort:** current total stars, weekly gain shown for reference

> **Note on this edition's "Weekly gain" column:** the figures below cover **2026-11-18 → 2026-11-25**: 7 calendar days, about 7.28 by fetch time, against about 7.07 in the previous edition, so raw gains overstate any speed-up by about 3%. DeerFlow and nanobot entered tracking at this fetch, so they have no gain this edition. Microsoft Agent Framework's repository still returns 404 and stays paused from tracking.

## Ranking Trend

How the weekly heat top 10 has shifted since tracking began — each line is one project, higher is a better rank, breaks mean the project fell off the board that week:

<p align="center">
  <img src="../assets/heat-trend-en.svg" alt="Weekly heat ranking trend (bump chart)" width="100%" />
</p>

The through-line so far: Hermes Agent owned the early boards, the `.claude/skills` wave took over from late May, and from mid-June the top three ranks rotated almost entirely among curated skills collections. **That line bent in September.** For two consecutive windows (2026-09-17 and 2026-09-24) both top-two seats were held by coding agents — [Open Code Review](../agents/open-code-review.md) and [DeepSeek Harness](../agents/deepseek-harness.md) — the first all-agent top two since **2026-05-08**, before the wave began. On 2026-09-30 the top two split again — DeepSeek Harness took its first #1 with [mattpocock/skills](https://github.com/mattpocock/skills) at #2 — and on 2026-10-07 they swapped back, mattpocock retaking #1. The wave rose to five of ten on 09-30 on the strength of two `anthropics/*` collections, then fell to **three** on 10-07 when both left; what remains is the three general collections that have carried it since June. Read the wave as durable but narrow, not as broadening. And read single-window jumps with care, because the board's own record on them is poor — jcode, addyosmani, Codex CLI, K-Dense, TradingAgents, Claude Code and, most recently, CLI-Anything all fell back the window after the one that made them look like a trend. Open Code Review and anthropics/financial-services are the counterexamples that held a second window; both then kept falling — Open Code Review for three windows running, financial-services off the board by its third. On 2026-10-14 the picture firmed up rather than moved: mattpocock/skills held #1 on its largest 7-day gain on record (+11,878) and DeepSeek Harness held #2 on a fourth straight slowdown; the wave rose to **four** seats as [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) returned, and the spike rule paid out once more (OpenHuman gave back 65% the window after its ~12x jump) while Open Code Review, the counterexample, re-accelerated 93% after three slowdowns. On 2026-10-21 the top held and the middle churned: mattpocock/skills kept #1 a third straight window, DeepSeek Harness kept #2 and passed Hermes Agent in total stars, and [OpenCode](../agents/opencode.md) jumped to #3 on its 2.0 launch. Below them, three repos gained 4.7 to 7.5 times their previous window with no documented cause (K-Dense, CLI-Anything, Ruflo), giving the infra layer two seats for the first time since 08-27, and Open Code Review gave back 76% and left — so it, too, did not hold. [Pi](../agents/pi.md)'s 20-window run ended, the longest run on the board ever to end; Hermes Agent (27, every window), Superpowers and mattpocock/skills (22 each) are the runs still going. On 2026-10-28 the board cooled hard (15 of 57 repos accelerated, 42 slowed) and the spike rule paid out on all three of the previous window's unexplained jumps: K-Dense gave back 68% and left, CLI-Anything and Ruflo gave back 56% and 52% but kept seats because the bar fell too, and even OpenCode's documented breakout halved. DeepSeek Harness took #1 for the second time on a flat gain as mattpocock/skills slowed 38% — mattpocock crossed 300k but stayed behind Superpowers — and TradingAgents became the new unexplained spike at #3. The wave held four seats, all general collections for the first time since 08-27; Hermes Agent (28), Superpowers and mattpocock/skills (23 each) are the runs still going. The 2026-11-04 edition replaced one dated 11-03 that ran a day early. By fetch time its window ran about 7.45 days against about 6.24, and on that basis the top held steady, with 21 of 57 repos accelerating: DeepSeek Harness held #1 for the first time, Superpowers rose 46% with no documented cause and now leads mattpocock/skills by 324, and last window's spikes split, TradingAgents keeping a seat at #4 while Gemini CLI gave back 89%. Infra lost both seats. The wave held four seats, all general collections for a second straight window; Hermes Agent (29), Superpowers and mattpocock/skills (24 each) are the runs still going. On 2026-11-11 [mattpocock/skills](https://github.com/mattpocock/skills) retook #1 on a 45% speed-up and passed Superpowers in total stars, while Superpowers gave back 29%, so its 11-04 jump was one more spike that did not hold; TradingAgents slowed again and left. Four of the five repos that entered tracking on 11-03 took seats on their first measured gain ([Orca](../agents/orca.md) #3, [ECC](../agents/ecc.md) #5, [claude-mem](../agents/claude-mem.md) #7, [Graphify](../agents/graphify.md) #8), which reads as the coverage gap closing rather than a breakout. That left the most unusual mix on record: infra three seats (the most in 30 windows), the wave five (all general collections, a first) and agents two (tying the fewest, 05-22). Hermes Agent (30), Superpowers and mattpocock/skills (25 each) are the runs still going. On 2026-11-18 the board cooled (23 of 60 repos accelerated, 37 slowed) and [Orca](../agents/orca.md) took #1 on a flat gain, the second infra repo to do so after CodeGraph on 06-02, as mattpocock/skills gave back 39% and DeepSeek Harness 31% (to #4, its lowest seat since it was first tracked). Hermes Agent's run ended at 30 windows, every one this board has recorded; Superpowers and mattpocock/skills (26 each) are now the longest runs still going. Open Code Review returned at #6 on an 866% jump with no documented cause, so it is the new spike. The mix held: the wave five seats (all general collections), infra three, agents two. On 2026-11-25 Orca held #1 (+38%), the first infra repo to hold it two windows running, and infra took a record four seats as CLI-Anything returned and Paperclip entered for the first time. Superpowers (+76%, to #2) and CLI-Anything (+763%, to #3) both jumped with no commit or release in the window, so both are spikes; Open Code Review gave back 48% but kept #10. mattpocock/skills (#4) and DeepSeek Harness (#6) took their lowest seats on record, and addyosmani/agent-skills' run ended at 10 windows. Superpowers and mattpocock/skills (27 each) are the longest runs still going. The mix: infra four, the wave four (all general collections), agents two.

## Agent Board

End-to-end agents — products you point at a task. Verticals are ranked separately in [agent verticals](agent-verticals.md).

<!-- auto:board:agent -->
| Rank | Project | Vertical | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [OpenClaw](https://github.com/openclaw/openclaw) | General assistant | 395.2k | +485 | In scope · [profile](../agents/openclaw.md) |
| #2 | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | Coding | 286.9k | +3,611 | In scope · [profile](../agents/deepseek-harness.md) |
| #3 | [Hermes Agent](https://github.com/nousresearch/hermes-agent) | General assistant | 266.0k | +1,708 | In scope · [profile](../agents/hermes-agent.md) |
| #4 | [OpenCode](https://github.com/anomalyco/opencode) | Coding | 229.1k | +1,427 | In scope · [profile](../agents/opencode.md) |
| #5 | [AutoGPT](https://github.com/significant-gravitas/autogpt) | General assistant | 188.2k | +101 | In scope · [profile](../agents/autogpt.md) |
| #6 | [Claude Code](https://github.com/anthropics/claude-code) | Coding | 157.0k | +936 | In scope · [profile](../agents/claude-code.md) |
| #7 | [Codex CLI](https://github.com/openai/codex) | Coding | 136.4k | +692 | In scope · [profile](../agents/codex.md) |
| #8 | [Pi](https://github.com/earendil-works/pi) | Coding | 123.8k | +1,208 | In scope · [profile](../agents/pi.md) |
| #9 | [TradingAgents](https://github.com/tauricresearch/tradingagents) | Finance | 123.8k | +726 | Out of scope |
| #10 | [Browser Use](https://github.com/browser-use/browser-use) | General assistant | 122.0k | +652 | In scope · [profile](../agents/browser-use.md) |
| #11 | [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Coding | 109.1k | +189 | In scope · [profile](../agents/gemini-cli.md) |
| #12 | [OpenHands](https://github.com/openhands/openhands) | Coding | 94.3k | +600 | In scope · [profile](../agents/openhands.md) |
| #13 | [DeerFlow](https://github.com/bytedance/deer-flow) | General assistant | 85.8k | — | In scope · [profile](../agents/deer-flow.md) |
| #14 | [Cline](https://github.com/cline/cline) | Coding | 71.9k | +148 | In scope · [profile](../agents/cline.md) |
| #15 | [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | General assistant | 69.0k | +57 | In scope · [profile](../agents/open-interpreter.md) |
| #16 | [Goose](https://github.com/aaif-goose/goose) | General assistant | 57.0k | +235 | In scope · [profile](../agents/goose.md) |
| #17 | [Open Code Review](https://github.com/alibaba/open-code-review) | Coding | 56.3k | +2,261 | In scope · [profile](../agents/open-code-review.md) |
| #18 | [nanobot](https://github.com/hkuds/nanobot) | General assistant | 50.3k | — | In scope · [profile](../agents/nanobot.md) |
| #19 | [Aider](https://github.com/aider-ai/aider) | Coding | 50.3k | +94 | In scope · [profile](../agents/aider.md) |
| #20 | [OpenHuman](https://github.com/tinyhumansai/openhuman) | General assistant | 42.8k | +104 | In scope · [profile](../agents/openhuman.md) |
| #21 | [CodeWhale](https://github.com/codewhale-hq/codewhale) | Coding | 41.2k | +24 | In scope · [profile](../agents/codewhale.md) |
| #22 | [Continue](https://github.com/continuedev/continue) | Coding | 36.6k | +52 | In scope · [profile](../agents/continue.md) |
| #23 | [Qwen Code](https://github.com/qwenlm/qwen-code) | Coding | 30.9k | +188 | In scope · [profile](../agents/qwen-code.md) |
| #24 | [Grok Build](https://github.com/xai-org/grok-build) | Coding | 27.9k | +54 | In scope · [profile](../agents/grok-build.md) |
| #25 | [jcode](https://github.com/1jehuang/jcode) | Coding | 22.0k | +165 | In scope · [profile](../agents/jcode.md) |
| #26 | [SWE-agent](https://github.com/swe-agent/swe-agent) | Coding | 20.9k | +43 | In scope · [profile](../agents/swe-agent.md) |
| #27 | [OpenHarness](https://github.com/hkuds/openharness) | Coding | 16.2k | +11 | In scope · [profile](../agents/openharness.md) |
| #28 | [QM](https://github.com/yc-software/qm) | General assistant | 15.8k | +55 | In scope · [profile](../agents/qm.md) |
| #29 | [MiMoCode](https://github.com/xiaomimimo/mimo-code) | Coding | 13.8k | +7 | In scope · [profile](../agents/mimocode.md) |
| #30 | [Omnigent](https://github.com/omnigent-ai/omnigent) | Coding | 11.6k | +140 | In scope · [profile](../agents/omnigent.md) |
| #31 | [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent) | Coding | 10.1k | +338 | In scope · [profile](../agents/mini-swe-agent.md) |
| #32 | [ZCode](https://github.com/zai-org/zcode) | Coding | 8.9k | +168 | In scope · [profile](../agents/zcode.md) |
| #33 | [Kimi Code](https://github.com/moonshotai/kimi-code) | Coding | 8.3k | +47 | In scope · [profile](../agents/kimi-code.md) |
| #34 | [CoStrict](https://github.com/zgsm-ai/costrict) | Coding | 4.5k | +-1 | In scope · [profile](../agents/costrict.md) |
<!-- /auto:board:agent -->

## Agent Infra Board

The layer under the agents — frameworks, orchestration, memory and context, gateways, and workflow engines. These are not agents you "run at a task"; they are what agent builders assemble on.

<!-- auto:board:infra -->
| Rank | Project | Group | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [n8n](https://github.com/n8n-io/n8n) | Workflow | 212.1k | +1,298 | In scope · [profile](../agents/n8n.md) |
| #2 | [Graphify](https://github.com/graphify-labs/graphify) | Memory & context | 153.2k | +3,392 | In scope · [profile](../agents/graphify.md) |
| #3 | [LangChain](https://github.com/langchain-ai/langchain) | Framework | 150.0k | +144 | In scope · [profile](../agents/langchain.md) |
| #4 | [Orca](https://github.com/stablyai/orca) | Orchestration | 137.5k | +9,266 | In scope · [profile](../agents/orca.md) |
| #5 | [claude-mem](https://github.com/thedotmack/claude-mem) | Memory & context | 119.7k | +1,608 | In scope · [profile](../agents/claude-mem.md) |
| #6 | [Paperclip](https://github.com/paperclipai/paperclip) | Orchestration | 117.0k | +2,291 | In scope · [profile](../agents/paperclip.md) |
| #7 | [Ruflo](https://github.com/ruvnet/ruflo) | Orchestration | 82.4k | +406 | In scope · [profile](../agents/ruflo.md) |
| #8 | [CodeGraph](https://github.com/colbymchenry/codegraph) | Memory & context | 78.7k | +751 | In scope · [profile](../agents/codegraph.md) |
| #9 | [CLI-Anything](https://github.com/hkuds/cli-anything) | Gateway & runtime | 65.5k | +6,191 | In scope · [profile](../agents/cli-anything.md) |
| #10 | [LiteLLM](https://github.com/berriai/litellm) | Gateway & runtime | 63.9k | +426 | In scope · [profile](../agents/litellm.md) |
| #11 | [CrewAI](https://github.com/crewaiinc/crewai) | Framework | 61.3k | +195 | In scope · [profile](../agents/crewai.md) |
| #12 | [Flowise](https://github.com/flowiseai/flowise) | Workflow | 55.6k | +18 | In scope · [profile](../agents/flowise.md) |
| #13 | [LlamaIndex](https://github.com/run-llama/llama_index) | Framework | 53.0k | +64 | In scope · [profile](../agents/llamaindex.md) |
| #14 | [LangGraph](https://github.com/langchain-ai/langgraph) | Orchestration | 45.4k | +310 | In scope · [profile](../agents/langgraph.md) |
| #15 | [Langfuse](https://github.com/langfuse/langfuse) | Observability & evals | 37.8k | +256 | In scope · [profile](../agents/langfuse.md) |
| #16 | [agentmemory](https://github.com/rohitg00/agentmemory) | Memory & context | 30.6k | +145 | Watchlist |
| #17 | [Letta (MemGPT)](https://github.com/letta-ai/letta) | Memory & context | 25.5k | +66 | In scope · [profile](../agents/memgpt.md) |
| #18 | [Trail Code (Graft)](https://github.com/trailhq/trail-code) | Memory & context | 11.5k | +158 | In scope · [profile](../agents/graft.md) |
| #19 | [TrueForge](https://github.com/truefoundry/trueforge) | Framework | 6.6k | +136 | In scope · [profile](../agents/trueforge.md) |
| #20 | [eve](https://github.com/vercel/eve) | Framework | 6.1k | +122 | In scope · [profile](../agents/eve.md) |
<!-- /auto:board:infra -->

## Skill Board

Skill collections, skill frameworks, and agent methodology — content assets rather than agent surfaces. Most are tracked as watchlist entries; the framework end is profiled through [Superpowers](../agents/superpowers.md). Focus areas are ranked separately in [skill verticals](skill-verticals.md).

<!-- auto:board:skill -->
| Rank | Project | Focus | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [mattpocock/skills](https://github.com/mattpocock/skills) | Curated collections | 332.7k | +5,645 | Watchlist |
| #2 | [Superpowers](https://github.com/obra/superpowers) | Curated collections | 326.4k | +6,753 | In scope · [profile](../agents/superpowers.md) |
| #3 | [ECC](https://github.com/affaan-m/ecc) | Curated collections | 310.5k | +4,633 | In scope · [profile](../agents/ecc.md) |
| #4 | [anthropics/skills](https://github.com/anthropics/skills) | Curated collections | 200.3k | +3,396 | Watchlist |
| #5 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Curated collections | 120.4k | +1,603 | Watchlist |
| #6 | [academic-research-skills](https://github.com/imbad0202/academic-research-skills) | Academic & scientific | 58.5k | +1,143 | Watchlist |
| #7 | [scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills) | Academic & scientific | 58.5k | +810 | Watchlist |
| #8 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Finance | 41.5k | +134 | Out of scope |
| #9 | [12-factor-agents](https://github.com/humanlayer/12-factor-agents) | Methodology | 27.4k | +132 | Out of scope |
<!-- /auto:board:skill -->

## Vertical Rankings

- [Agent verticals](agent-verticals.md) — coding, general assistant, finance
- [Skill verticals](skill-verticals.md) — curated collections, academic & scientific research, finance, methodology

Boards and the trend chart are regenerated by `scripts/render-rankings.py` and `scripts/render-trend.py` on every publish — do not edit the marked table blocks by hand.
