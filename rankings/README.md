# Category Rankings

[English](../README.md) | [中文](../zh/rankings/README.md)

The home-page [heat ranking](../README.md#recent-heat-ranking) sorts by **weekly star gain** — it shows momentum. The boards on this page sort by **current total stars** — they show the standing stock of each category. Read them together: a project high here but absent from the heat table is established; a project low here but topping the heat table is breaking out.

> **Last updated:** 2026-09-24 · **Star counts:** from the most recent tracked fetch · **Sort:** current total stars, weekly gain shown for reference

> **Note on this edition's "Weekly gain" column:** the previous refresh was a late catch-up run on 2026-08-27, so the figures below cover **2026-08-27 → 2026-09-01 (5 days)**, not 7. They are roughly 0.71× a normal window, and the previous edition's column was a 15-day catch-up — so neither this column nor the last one is directly comparable to the other. Compare on the weekly rate (gain ÷ days × 7).

## Ranking Trend

How the weekly heat top 10 has shifted since tracking began — each line is one project, higher is a better rank, breaks mean the project fell off the board that week:

<p align="center">
  <img src="../assets/heat-trend-en.svg" alt="Weekly heat ranking trend (bump chart)" width="100%" />
</p>

The through-line so far: Hermes Agent owned the early boards, the `.claude/skills` wave took over from late May, and from mid-June the top three ranks rotated almost entirely among curated skills collections. Two windows have now bent that line in different directions. On 2026-08-27 [Codex CLI](../agents/codex.md) took #2 off a vendor price cut — the first non-skills project in a top-two gain seat since June — and on **2026-09-01 it gave 57% of that back and fell to #6**, while `mattpocock/skills` lost the #1 seat it had held for nine straight windows (2026-06-24 → 2026-08-27). The project that took it, [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills), is still a skills collection — but a **domain** one, which is new. Read the current shape as the wave finding verticals rather than as the wave ending; and read both windows as a caution about single-window jumps, since three in a row (jcode, addyosmani, Codex) failed to survive the next refresh.

## Agent Board

End-to-end agents — products you point at a task. Verticals are ranked separately in [agent verticals](agent-verticals.md).

<!-- auto:board:agent -->
| Rank | Project | Vertical | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [OpenClaw](https://github.com/openclaw/openclaw) | General assistant | 390.3k | +416 | In scope · [profile](../agents/openclaw.md) |
| #2 | [Hermes Agent](https://github.com/nousresearch/hermes-agent) | General assistant | 248.4k | +2,081 | In scope · [profile](../agents/hermes-agent.md) |
| #3 | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | Coding | 234.3k | +7,096 | In scope · [profile](../agents/deepseek-harness.md) |
| #4 | [OpenCode](https://github.com/anomalyco/opencode) | Coding | 209.7k | +1,667 | In scope · [profile](../agents/opencode.md) |
| #5 | [AutoGPT](https://github.com/significant-gravitas/autogpt) | General assistant | 187.5k | +116 | In scope · [profile](../agents/autogpt.md) |
| #6 | [Claude Code](https://github.com/anthropics/claude-code) | Coding | 147.8k | +2,108 | In scope · [profile](../agents/claude-code.md) |
| #7 | [Codex CLI](https://github.com/openai/codex) | Coding | 126.2k | +1,316 | In scope · [profile](../agents/codex.md) |
| #8 | [Browser Use](https://github.com/browser-use/browser-use) | General assistant | 116.1k | +1,207 | In scope · [profile](../agents/browser-use.md) |
| #9 | [Pi](https://github.com/earendil-works/pi) | Coding | 108.9k | +2,439 | In scope · [profile](../agents/pi.md) |
| #10 | [TradingAgents](https://github.com/tauricresearch/tradingagents) | Finance | 108.3k | +1,134 | Out of scope |
| #11 | [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Coding | 107.1k | +111 | In scope · [profile](../agents/gemini-cli.md) |
| #12 | [OpenHands](https://github.com/openhands/openhands) | Coding | 89.0k | +761 | In scope · [profile](../agents/openhands.md) |
| #13 | [Cline](https://github.com/cline/cline) | Coding | 69.2k | +685 | In scope · [profile](../agents/cline.md) |
| #14 | [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | General assistant | 68.4k | +61 | In scope · [profile](../agents/open-interpreter.md) |
| #15 | [Goose](https://github.com/aaif-goose/goose) | General assistant | 54.6k | +222 | In scope · [profile](../agents/goose.md) |
| #16 | [Aider](https://github.com/aider-ai/aider) | Coding | 49.1k | +123 | In scope · [profile](../agents/aider.md) |
| #17 | [CodeWhale](https://github.com/hmbown/codewhale) | Coding | 41.0k | +43 | In scope · [profile](../agents/codewhale.md) |
| #18 | [Open Code Review](https://github.com/alibaba/open-code-review) | Coding | 40.2k | +7,112 | In scope · [profile](../agents/open-code-review.md) |
| #19 | [OpenHuman](https://github.com/tinyhumansai/openhuman) | General assistant | 40.1k | +249 | In scope · [profile](../agents/openhuman.md) |
| #20 | [Continue](https://github.com/continuedev/continue) | Coding | 36.0k | +68 | In scope · [profile](../agents/continue.md) |
| #21 | [Qwen Code](https://github.com/qwenlm/qwen-code) | Coding | 28.1k | +188 | In scope · [profile](../agents/qwen-code.md) |
| #22 | [Grok Build](https://github.com/xai-org/grok-build) | Coding | 27.1k | +241 | In scope · [profile](../agents/grok-build.md) |
| #23 | [SWE-agent](https://github.com/swe-agent/swe-agent) | Coding | 20.4k | +47 | In scope · [profile](../agents/swe-agent.md) |
| #24 | [jcode](https://github.com/1jehuang/jcode) | Coding | 20.1k | +267 | In scope · [profile](../agents/jcode.md) |
| #25 | [OpenHarness](https://github.com/hkuds/openharness) | Coding | 15.8k | +74 | In scope · [profile](../agents/openharness.md) |
| #26 | [QM](https://github.com/yc-software/qm) | General assistant | 15.2k | +101 | In scope · [profile](../agents/qm.md) |
| #27 | [MiMoCode](https://github.com/xiaomimimo/mimo-code) | Coding | 13.4k | +287 | In scope · [profile](../agents/mimocode.md) |
| #28 | [Omnigent](https://github.com/omnigent-ai/omnigent) | Coding | 10.2k | +163 | In scope · [profile](../agents/omnigent.md) |
| #29 | [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent) | Coding | 7.9k | +223 | In scope · [profile](../agents/mini-swe-agent.md) |
| #30 | [Kimi Code](https://github.com/moonshotai/kimi-code) | Coding | 7.6k | +214 | In scope · [profile](../agents/kimi-code.md) |
| #31 | [CoStrict](https://github.com/zgsm-ai/costrict) | Coding | 4.4k | +8 | In scope · [profile](../agents/costrict.md) |
<!-- /auto:board:agent -->

## Agent Infra Board

The layer under the agents — frameworks, orchestration, memory and context, gateways, and workflow engines. These are not agents you "run at a task"; they are what agent builders assemble on.

<!-- auto:board:infra -->
| Rank | Project | Group | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [n8n](https://github.com/n8n-io/n8n) | Workflow | 205.8k | +1,073 | In scope · [profile](../agents/n8n.md) |
| #2 | [LangChain](https://github.com/langchain-ai/langchain) | Framework | 146.9k | +444 | In scope · [profile](../agents/langchain.md) |
| #3 | [Ruflo](https://github.com/ruvnet/ruflo) | Orchestration | 73.2k | +490 | In scope · [profile](../agents/ruflo.md) |
| #4 | [CodeGraph](https://github.com/colbymchenry/codegraph) | Memory & context | 71.9k | +712 | In scope · [profile](../agents/codegraph.md) |
| #5 | [LiteLLM](https://github.com/berriai/litellm) | Gateway & runtime | 59.5k | +539 | In scope · [profile](../agents/litellm.md) |
| #6 | [CrewAI](https://github.com/crewaiinc/crewai) | Framework | 59.0k | +278 | In scope · [profile](../agents/crewai.md) |
| #7 | [Flowise](https://github.com/flowiseai/flowise) | Workflow | 55.5k | +10 | In scope · [profile](../agents/flowise.md) |
| #8 | [LlamaIndex](https://github.com/run-llama/llama_index) | Framework | 52.3k | +110 | In scope · [profile](../agents/llamaindex.md) |
| #9 | [CLI-Anything](https://github.com/hkuds/cli-anything) | Gateway & runtime | 49.9k | +407 | In scope · [profile](../agents/cli-anything.md) |
| #10 | [LangGraph](https://github.com/langchain-ai/langgraph) | Orchestration | 42.2k | +394 | In scope · [profile](../agents/langgraph.md) |
| #11 | [Langfuse](https://github.com/langfuse/langfuse) | Observability & evals | 35.0k | +269 | In scope · [profile](../agents/langfuse.md) |
| #12 | [agentmemory](https://github.com/rohitg00/agentmemory) | Memory & context | 28.8k | +251 | Watchlist |
| #13 | [Letta (MemGPT)](https://github.com/letta-ai/letta) | Memory & context | 24.9k | +91 | In scope · [profile](../agents/memgpt.md) |
| #14 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Framework | 13.8k | +203 | In scope · [profile](../agents/microsoft-agent-framework.md) |
| #15 | [TrueForge](https://github.com/truefoundry/trueforge) | Framework | 5.9k | +220 | In scope · [profile](../agents/trueforge.md) |
| #16 | [eve](https://github.com/vercel/eve) | Framework | 5.3k | +18 | In scope · [profile](../agents/eve.md) |
<!-- /auto:board:infra -->

## Skill Board

Skill collections, skill frameworks, and agent methodology — content assets rather than agent surfaces. Most are tracked as watchlist entries; the framework end is profiled through [Superpowers](../agents/superpowers.md). Focus areas are ranked separately in [skill verticals](skill-verticals.md).

<!-- auto:board:skill -->
| Rank | Project | Focus | Stars | Weekly gain | Map status |
| --- | --- | --- | --- | --- | --- |
| #1 | [Superpowers](https://github.com/obra/superpowers) | Curated collections | 290.7k | +2,882 | In scope · [profile](../agents/superpowers.md) |
| #2 | [mattpocock/skills](https://github.com/mattpocock/skills) | Curated collections | 268.5k | +4,613 | Watchlist |
| #3 | [anthropics/skills](https://github.com/anthropics/skills) | Curated collections | 177.8k | +1,051 | Watchlist |
| #4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Curated collections | 98.7k | +3,033 | Watchlist |
| #5 | [academic-research-skills](https://github.com/imbad0202/academic-research-skills) | Academic & scientific | 49.3k | +883 | Watchlist |
| #6 | [scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills) | Academic & scientific | 46.3k | +1,032 | Watchlist |
| #7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | Finance | 36.9k | +2,048 | Out of scope |
| #8 | [12-factor-agents](https://github.com/humanlayer/12-factor-agents) | Methodology | 26.4k | +469 | Out of scope |
<!-- /auto:board:skill -->

## Vertical Rankings

- [Agent verticals](agent-verticals.md) — coding, general assistant, finance
- [Skill verticals](skill-verticals.md) — curated collections, academic & scientific research, finance, methodology

Boards and the trend chart are regenerated by `scripts/render-rankings.py` and `scripts/render-trend.py` on every publish — do not edit the marked table blocks by hand.
