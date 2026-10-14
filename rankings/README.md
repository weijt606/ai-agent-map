# Category Rankings

[English](../README.md) | [中文](../zh/rankings/README.md)

The home-page [heat ranking](../README.md#recent-heat-ranking) sorts by **weekly star gain** — it shows momentum. The boards on this page sort by **current total stars** — they show the standing stock of each category. Read them together: a project high here but absent from the heat table is established; a project low here but topping the heat table is breaking out.

> **Last updated:** 2026-10-14 · **Star counts:** from the most recent tracked fetch · **Sort:** current total stars, weekly gain shown for reference

> **Note on this edition's "Weekly gain" column:** the figures below cover **2026-10-07 → 2026-10-14 (7 days)**, a normal window. The previous edition's column also covered 7 days, so for the first time since 09-17 the two editions' raw gains compare directly.

## Ranking Trend

How the weekly heat top 10 has shifted since tracking began — each line is one project, higher is a better rank, breaks mean the project fell off the board that week:

<p align="center">
  <img src="../assets/heat-trend-en.svg" alt="Weekly heat ranking trend (bump chart)" width="100%" />
</p>

The through-line so far: Hermes Agent owned the early boards, the `.claude/skills` wave took over from late May, and from mid-June the top three ranks rotated almost entirely among curated skills collections. **That line bent in September.** For two consecutive windows (2026-09-17 and 2026-09-24) both top-two seats were held by coding agents — [Open Code Review](../agents/open-code-review.md) and [DeepSeek Harness](../agents/deepseek-harness.md) — the first all-agent top two since **2026-05-08**, before the wave began. On 2026-09-30 the top two split again — DeepSeek Harness took its first #1 with [mattpocock/skills](https://github.com/mattpocock/skills) at #2 — and on 2026-10-07 they swapped back, mattpocock retaking #1. The wave rose to five of ten on 09-30 on the strength of two `anthropics/*` collections, then fell to **three** on 10-07 when both left; what remains is the three general collections that have carried it since June. Read the wave as durable but narrow, not as broadening. And read single-window jumps with care, because the board's own record on them is poor — jcode, addyosmani, Codex CLI, K-Dense, TradingAgents, Claude Code and, most recently, CLI-Anything all fell back the window after the one that made them look like a trend. Open Code Review and anthropics/financial-services are the counterexamples that held a second window; both then kept falling — Open Code Review for three windows running, financial-services off the board by its third. On 2026-10-14 the picture firmed up rather than moved: mattpocock/skills held #1 on its largest 7-day gain on record (+11,878) and DeepSeek Harness held #2 on a fourth straight slowdown; the wave rose to **four** seats as [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) returned, and the spike rule paid out once more (OpenHuman gave back 65% the window after its ~12x jump) while Open Code Review, the counterexample, re-accelerated 93% after three slowdowns.

## Agent Board

End-to-end agents — products you point at a task. Verticals are ranked separately in [agent verticals](agent-verticals.md).

<!-- auto:board:agent -->
| Rank | Project | Vertical | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [OpenClaw](https://github.com/openclaw/openclaw) | General assistant | 391.9k | +404 | In scope · [profile](../agents/openclaw.md) |
| #2 | [Hermes Agent](https://github.com/nousresearch/hermes-agent) | General assistant | 253.6k | +1,857 | In scope · [profile](../agents/hermes-agent.md) |
| #3 | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | Coding | 249.4k | +4,563 | In scope · [profile](../agents/deepseek-harness.md) |
| #4 | [OpenCode](https://github.com/anomalyco/opencode) | Coding | 213.4k | +1,289 | In scope · [profile](../agents/opencode.md) |
| #5 | [AutoGPT](https://github.com/significant-gravitas/autogpt) | General assistant | 187.6k | +-116 | In scope · [profile](../agents/autogpt.md) |
| #6 | [Claude Code](https://github.com/anthropics/claude-code) | Coding | 150.7k | +1,068 | In scope · [profile](../agents/claude-code.md) |
| #7 | [Codex CLI](https://github.com/openai/codex) | Coding | 129.2k | +1,048 | In scope · [profile](../agents/codex.md) |
| #8 | [Browser Use](https://github.com/browser-use/browser-use) | General assistant | 117.9k | +604 | In scope · [profile](../agents/browser-use.md) |
| #9 | [Pi](https://github.com/earendil-works/pi) | Coding | 115.0k | +1,992 | In scope · [profile](../agents/pi.md) |
| #10 | [TradingAgents](https://github.com/tauricresearch/tradingagents) | Finance | 111.1k | +1,078 | Out of scope |
| #11 | [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Coding | 107.3k | +101 | In scope · [profile](../agents/gemini-cli.md) |
| #12 | [OpenHands](https://github.com/openhands/openhands) | Coding | 90.9k | +718 | In scope · [profile](../agents/openhands.md) |
| #13 | [Cline](https://github.com/cline/cline) | Coding | 70.3k | +334 | In scope · [profile](../agents/cline.md) |
| #14 | [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | General assistant | 68.6k | +54 | In scope · [profile](../agents/open-interpreter.md) |
| #15 | [Goose](https://github.com/aaif-goose/goose) | General assistant | 55.3k | +251 | In scope · [profile](../agents/goose.md) |
| #16 | [Aider](https://github.com/aider-ai/aider) | Coding | 49.5k | +138 | In scope · [profile](../agents/aider.md) |
| #17 | [Open Code Review](https://github.com/alibaba/open-code-review) | Coding | 47.1k | +2,966 | In scope · [profile](../agents/open-code-review.md) |
| #18 | [OpenHuman](https://github.com/tinyhumansai/openhuman) | General assistant | 42.0k | +468 | In scope · [profile](../agents/openhuman.md) |
| #19 | [CodeWhale](https://github.com/codewhale-hq/codewhale) | Coding | 41.1k | +18 | In scope · [profile](../agents/codewhale.md) |
| #20 | [Continue](https://github.com/continuedev/continue) | Coding | 36.2k | +76 | In scope · [profile](../agents/continue.md) |
| #21 | [Qwen Code](https://github.com/qwenlm/qwen-code) | Coding | 28.5k | +136 | In scope · [profile](../agents/qwen-code.md) |
| #22 | [Grok Build](https://github.com/xai-org/grok-build) | Coding | 27.4k | +118 | In scope · [profile](../agents/grok-build.md) |
| #23 | [jcode](https://github.com/1jehuang/jcode) | Coding | 20.7k | +376 | In scope · [profile](../agents/jcode.md) |
| #24 | [SWE-agent](https://github.com/swe-agent/swe-agent) | Coding | 20.5k | +53 | In scope · [profile](../agents/swe-agent.md) |
| #25 | [OpenHarness](https://github.com/hkuds/openharness) | Coding | 16.0k | +64 | In scope · [profile](../agents/openharness.md) |
| #26 | [QM](https://github.com/yc-software/qm) | General assistant | 15.4k | +51 | In scope · [profile](../agents/qm.md) |
| #27 | [MiMoCode](https://github.com/xiaomimimo/mimo-code) | Coding | 13.7k | +52 | In scope · [profile](../agents/mimocode.md) |
| #28 | [Omnigent](https://github.com/omnigent-ai/omnigent) | Coding | 10.8k | +168 | In scope · [profile](../agents/omnigent.md) |
| #29 | [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent) | Coding | 8.5k | +249 | In scope · [profile](../agents/mini-swe-agent.md) |
| #30 | [Kimi Code](https://github.com/moonshotai/kimi-code) | Coding | 7.9k | +81 | In scope · [profile](../agents/kimi-code.md) |
| #31 | [ZCode](https://github.com/zai-org/zcode) | Coding | 7.8k | +317 | In scope · [profile](../agents/zcode.md) |
| #32 | [CoStrict](https://github.com/zgsm-ai/costrict) | Coding | 4.4k | +3 | In scope · [profile](../agents/costrict.md) |
<!-- /auto:board:agent -->

## Agent Infra Board

The layer under the agents — frameworks, orchestration, memory and context, gateways, and workflow engines. These are not agents you "run at a task"; they are what agent builders assemble on.

<!-- auto:board:infra -->
| Rank | Project | Group | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [n8n](https://github.com/n8n-io/n8n) | Workflow | 207.3k | +546 | In scope · [profile](../agents/n8n.md) |
| #2 | [LangChain](https://github.com/langchain-ai/langchain) | Framework | 147.8k | +313 | In scope · [profile](../agents/langchain.md) |
| #3 | [Ruflo](https://github.com/ruvnet/ruflo) | Orchestration | 74.6k | +594 | In scope · [profile](../agents/ruflo.md) |
| #4 | [CodeGraph](https://github.com/colbymchenry/codegraph) | Memory & context | 74.0k | +682 | In scope · [profile](../agents/codegraph.md) |
| #5 | [LiteLLM](https://github.com/berriai/litellm) | Gateway & runtime | 61.2k | +956 | In scope · [profile](../agents/litellm.md) |
| #6 | [CrewAI](https://github.com/crewaiinc/crewai) | Framework | 59.7k | +270 | In scope · [profile](../agents/crewai.md) |
| #7 | [Flowise](https://github.com/flowiseai/flowise) | Workflow | 55.5k | +11 | In scope · [profile](../agents/flowise.md) |
| #8 | [LlamaIndex](https://github.com/run-llama/llama_index) | Framework | 52.5k | +62 | In scope · [profile](../agents/llamaindex.md) |
| #9 | [CLI-Anything](https://github.com/hkuds/cli-anything) | Gateway & runtime | 52.1k | +486 | In scope · [profile](../agents/cli-anything.md) |
| #10 | [LangGraph](https://github.com/langchain-ai/langgraph) | Orchestration | 43.2k | +442 | In scope · [profile](../agents/langgraph.md) |
| #11 | [Langfuse](https://github.com/langfuse/langfuse) | Observability & evals | 35.8k | +345 | In scope · [profile](../agents/langfuse.md) |
| #12 | [agentmemory](https://github.com/rohitg00/agentmemory) | Memory & context | 29.4k | +211 | Watchlist |
| #13 | [Letta (MemGPT)](https://github.com/letta-ai/letta) | Memory & context | 25.1k | +65 | In scope · [profile](../agents/memgpt.md) |
| #14 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Framework | 14.1k | +144 | In scope · [profile](../agents/microsoft-agent-framework.md) |
| #15 | [Trail Code (Graft)](https://github.com/trailhq/trail-code) | Memory & context | 10.0k | +340 | In scope · [profile](../agents/graft.md) |
| #16 | [TrueForge](https://github.com/truefoundry/trueforge) | Framework | 6.2k | +152 | In scope · [profile](../agents/trueforge.md) |
| #17 | [eve](https://github.com/vercel/eve) | Framework | 5.6k | +80 | In scope · [profile](../agents/eve.md) |
<!-- /auto:board:infra -->

## Skill Board

Skill collections, skill frameworks, and agent methodology — content assets rather than agent surfaces. Most are tracked as watchlist entries; the framework end is profiled through [Superpowers](../agents/superpowers.md). Focus areas are ranked separately in [skill verticals](skill-verticals.md).

<!-- auto:board:skill -->
| Rank | Project | Focus | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [Superpowers](https://github.com/obra/superpowers) | Curated collections | 298.9k | +2,756 | In scope · [profile](../agents/superpowers.md) |
| #2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Curated collections | 290.4k | +11,878 | Watchlist |
| #3 | [anthropics/skills](https://github.com/anthropics/skills) | Curated collections | 181.0k | +1,051 | Watchlist |
| #4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Curated collections | 106.4k | +4,172 | Watchlist |
| #5 | [academic-research-skills](https://github.com/imbad0202/academic-research-skills) | Academic & scientific | 51.9k | +1,200 | Watchlist |
| #6 | [scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills) | Academic & scientific | 48.8k | +978 | Watchlist |
| #7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Finance | 39.8k | +896 | Out of scope |
| #8 | [12-factor-agents](https://github.com/humanlayer/12-factor-agents) | Methodology | 26.7k | +99 | Out of scope |
<!-- /auto:board:skill -->

## Vertical Rankings

- [Agent verticals](agent-verticals.md) — coding, general assistant, finance
- [Skill verticals](skill-verticals.md) — curated collections, academic & scientific research, finance, methodology

Boards and the trend chart are regenerated by `scripts/render-rankings.py` and `scripts/render-trend.py` on every publish — do not edit the marked table blocks by hand.
