# Category Rankings

[English](../README.md) | [中文](../zh/rankings/README.md)

The home-page [heat ranking](../README.md#recent-heat-ranking) sorts by **weekly star gain** — it shows momentum. The boards on this page sort by **current total stars** — they show the standing stock of each category. Read them together: a project high here but absent from the heat table is established; a project low here but topping the heat table is breaking out.

> **Last updated:** 2026-09-01 · **Star counts:** from the most recent tracked fetch · **Sort:** current total stars, weekly gain shown for reference

> **Note on this edition's "Weekly gain" column:** the previous refresh was a late catch-up run on 2026-08-27, so the figures below cover **2026-08-27 → 2026-09-01 (5 days)**, not 7. They are roughly 0.71× a normal window, and the previous edition's column was a 15-day catch-up — so neither this column nor the last one is directly comparable to the other. Compare on the weekly rate (gain ÷ days × 7).

## Ranking Trend

How the weekly heat top 10 has shifted since tracking began — each line is one project, higher is a better rank, breaks mean the project fell off the board that week:

<p align="center">
  <img src="../assets/heat-trend-en.svg" alt="Weekly heat ranking trend (bump chart)" width="100%" />
</p>

The through-line so far: Hermes Agent owned the early boards, the `.claude/skills` wave took over from late May, and from mid-June the top three ranks rotated almost entirely among curated skills collections. Two windows have now bent that line in different directions. On 2026-08-27 [Codex CLI](../agents/codex.md) took #2 off a vendor price cut — the first non-skills project in a top-two gain seat since June — and on **2026-09-01 it gave 57% of that back and fell to #6**, while `mattpocock/skills` lost the #1 seat it had held for ten straight windows. The project that took it, [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills), is still a skills collection — but a **domain** one, which is new. Read the current shape as the wave finding verticals rather than as the wave ending; and read both windows as a caution about single-window jumps, since three in a row (jcode, addyosmani, Codex) failed to survive the next refresh.

## Agent Board

End-to-end agents — products you point at a task. Verticals are ranked separately in [agent verticals](agent-verticals.md).

<!-- auto:board:agent -->
| Rank | Project | Vertical | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [OpenClaw](https://github.com/openclaw/openclaw) | General assistant | 388.5k | +792 | In scope · [profile](../agents/openclaw.md) |
| #2 | [Hermes Agent](https://github.com/nousresearch/hermes-agent) | General assistant | 239.5k | +2,595 | In scope · [profile](../agents/hermes-agent.md) |
| #3 | [AutoGPT](https://github.com/significant-gravitas/autogpt) | General assistant | 187.1k | +162 | In scope · [profile](../agents/autogpt.md) |
| #4 | [Claude Code](https://github.com/anthropics/claude-code) | Coding | 143.7k | +593 | In scope · [profile](../agents/claude-code.md) |
| #5 | [Codex CLI](https://github.com/openai/codex) | Coding | 120.7k | +1,915 | In scope · [profile](../agents/codex.md) |
| #6 | [TradingAgents](https://github.com/tauricresearch/tradingagents) | Finance | 102.2k | +1,455 | Out of scope |
| #7 | [Pi](https://github.com/earendil-works/pi) | Coding | 100.5k | +2,707 | In scope · [profile](../agents/pi.md) |
| #8 | [OpenHands](https://github.com/openhands/openhands) | Coding | 85.9k | +681 | In scope · [profile](../agents/openhands.md) |
| #9 | [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | General assistant | 68.2k | +60 | In scope · [profile](../agents/open-interpreter.md) |
| #10 | [Cline](https://github.com/cline/cline) | Coding | 67.3k | +381 | In scope · [profile](../agents/cline.md) |
| #11 | [Goose](https://github.com/aaif-goose/goose) | General assistant | 53.8k | +275 | In scope · [profile](../agents/goose.md) |
| #12 | [Aider](https://github.com/aider-ai/aider) | Coding | 48.7k | +139 | In scope · [profile](../agents/aider.md) |
| #13 | [CodeWhale](https://github.com/hmbown/codewhale) | Coding | 40.9k | +24 | In scope · [profile](../agents/codewhale.md) |
| #14 | [OpenHuman](https://github.com/tinyhumansai/openhuman) | General assistant | 39.3k | +1,111 | In scope · [profile](../agents/openhuman.md) |
| #15 | [Continue](https://github.com/continuedev/continue) | Coding | 35.7k | +81 | In scope · [profile](../agents/continue.md) |
| #16 | [Grok Build](https://github.com/xai-org/grok-build) | Coding | 26.3k | +235 | In scope · [profile](../agents/grok-build.md) |
| #17 | [Open Code Review](https://github.com/alibaba/open-code-review) | Coding | 21.8k | +315 | In scope · [profile](../agents/open-code-review.md) |
| #18 | [SWE-agent](https://github.com/swe-agent/swe-agent) | Coding | 20.2k | +41 | In scope · [profile](../agents/swe-agent.md) |
| #19 | [jcode](https://github.com/1jehuang/jcode) | Coding | 19.0k | +322 | In scope · [profile](../agents/jcode.md) |
| #20 | [OpenHarness](https://github.com/hkuds/openharness) | Coding | 15.6k | +65 | In scope · [profile](../agents/openharness.md) |
| #21 | [QM](https://github.com/yc-software/qm) | General assistant | 14.4k | +188 | In scope · [profile](../agents/qm.md) |
| #22 | [MiMoCode](https://github.com/xiaomimimo/mimo-code) | Coding | 12.9k | +42 | In scope · [profile](../agents/mimocode.md) |
| #23 | [Omnigent](https://github.com/omnigent-ai/omnigent) | Coding | 9.6k | +275 | In scope · [profile](../agents/omnigent.md) |
| #24 | [Kimi Code](https://github.com/moonshotai/kimi-code) | Coding | 7.2k | +115 | In scope · [profile](../agents/kimi-code.md) |
| #25 | [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent) | Coding | 6.9k | +123 | In scope · [profile](../agents/mini-swe-agent.md) |
| #26 | [CoStrict](https://github.com/zgsm-ai/costrict) | Coding | 4.4k | +7 | In scope · [profile](../agents/costrict.md) |
<!-- /auto:board:agent -->

## Agent Infra Board

The layer under the agents — frameworks, orchestration, memory and context, gateways, and workflow engines. These are not agents you "run at a task"; they are what agent builders assemble on.

<!-- auto:board:infra -->
| Rank | Project | Group | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [n8n](https://github.com/n8n-io/n8n) | Workflow | 203.1k | +527 | In scope · [profile](../agents/n8n.md) |
| #2 | [LangChain](https://github.com/langchain-ai/langchain) | Framework | 145.4k | +373 | In scope · [profile](../agents/langchain.md) |
| #3 | [Ruflo](https://github.com/ruvnet/ruflo) | Orchestration | 70.1k | +646 | In scope · [profile](../agents/ruflo.md) |
| #4 | [CodeGraph](https://github.com/colbymchenry/codegraph) | Memory & context | 69.1k | +814 | In scope · [profile](../agents/codegraph.md) |
| #5 | [CrewAI](https://github.com/crewaiinc/crewai) | Framework | 58.0k | +312 | In scope · [profile](../agents/crewai.md) |
| #6 | [LiteLLM](https://github.com/berriai/litellm) | Gateway & runtime | 57.8k | +430 | In scope · [profile](../agents/litellm.md) |
| #7 | [Flowise](https://github.com/flowiseai/flowise) | Workflow | 55.4k | +5 | In scope · [profile](../agents/flowise.md) |
| #8 | [LlamaIndex](https://github.com/run-llama/llama_index) | Framework | 52.0k | +87 | In scope · [profile](../agents/llamaindex.md) |
| #9 | [CLI-Anything](https://github.com/hkuds/cli-anything) | Gateway & runtime | 48.8k | +502 | In scope · [profile](../agents/cli-anything.md) |
| #10 | [LangGraph](https://github.com/langchain-ai/langgraph) | Orchestration | 40.9k | +368 | In scope · [profile](../agents/langgraph.md) |
| #11 | [Langfuse](https://github.com/langfuse/langfuse) | Observability & evals | 34.1k | +285 | In scope · [profile](../agents/langfuse.md) |
| #12 | [agentmemory](https://github.com/rohitg00/agentmemory) | Memory & context | 27.9k | +378 | Watchlist |
| #13 | [Letta (MemGPT)](https://github.com/letta-ai/letta) | Memory & context | 24.5k | +86 | In scope · [profile](../agents/memgpt.md) |
| #14 | [eve](https://github.com/vercel/eve) | Framework | 4.9k | — | In scope · [profile](../agents/eve.md) |
<!-- /auto:board:infra -->

## Skill Board

Skill collections, skill frameworks, and agent methodology — content assets rather than agent surfaces. Most are tracked as watchlist entries; the framework end is profiled through [Superpowers](../agents/superpowers.md). Focus areas are ranked separately in [skill verticals](skill-verticals.md).

<!-- auto:board:skill -->
| Rank | Project | Focus | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [Superpowers](https://github.com/obra/superpowers) | Curated collections | 280.4k | +2,308 | In scope · [profile](../agents/superpowers.md) |
| #2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Curated collections | 243.9k | +5,954 | Watchlist |
| #3 | [anthropics/skills](https://github.com/anthropics/skills) | Curated collections | 173.0k | +1,173 | Watchlist |
| #4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Curated collections | 91.4k | +1,418 | Watchlist |
| #5 | [academic-research-skills](https://github.com/imbad0202/academic-research-skills) | Academic & scientific | 44.8k | +975 | Watchlist |
| #6 | [scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills) | Academic & scientific | 41.5k | +6,750 | Watchlist |
| #7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Finance | 34.6k | +93 | Out of scope |
| #8 | [12-factor-agents](https://github.com/humanlayer/12-factor-agents) | Methodology | 25.6k | +129 | Out of scope |
<!-- /auto:board:skill -->

## Vertical Rankings

- [Agent verticals](agent-verticals.md) — coding, general assistant, finance
- [Skill verticals](skill-verticals.md) — curated collections, academic & scientific research, finance, methodology

Boards and the trend chart are regenerated by `scripts/render-rankings.py` and `scripts/render-trend.py` on every publish — do not edit the marked table blocks by hand.
