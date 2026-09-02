# 分类排行

[English](../../rankings/README.md) | [中文](../README.md)

主页的[热门榜](../README.md#近期热门榜)按 **周增量** 排序，看的是势头；这一页的榜单按 **当前 star 总量** 排序，看的是各类别的存量格局。两边对照读：总量高但没进热榜的项目是已站稳的老玩家，总量低但冲上热榜的项目是正在爆发的新势力。

> **最后更新：** 2026-09-01 · **Star 总数：** 来自最近一次追踪抓取 · **排序：** 当前 star 总量，本周增量仅作参考

> **本期"周增量"列的说明：** 上一次例更是 2026-08-27 补跑的补更，所以下面的数字覆盖的是 **2026-08-27 → 2026-09-01（5 天）**，不是 7 天。它们大约是正常窗口的 0.71 倍；而上一期那一列是 15 天的补更窗口——所以这两列彼此都不能直接比。要比就比周率（增量 ÷ 天数 × 7）。

## 排名趋势

每周热度 Top 10 自开始追踪以来的名次变化——一条折线一个项目，越靠上名次越好，折线中断表示该周掉出榜单：

<p align="center">
  <img src="../../assets/heat-trend-zh.svg" alt="每周热度排行趋势图（bump chart）" width="100%" />
</p>

到目前为止的主线：早期榜单由 Hermes Agent 统治，5 月底起 `.claude/skills` 浪潮接管，6 月中以后前三名几乎完全在 curated skills 合集之间轮换。现在有两个窗口从不同方向把这条线掰弯了。2026-08-27 那次，[Codex CLI](../agents/codex.md) 靠一次厂商降价拿到 #2——6 月以来第一次由非 skills 项目占住增量榜前两席；而 **2026-09-01 它又把其中 57% 还了回去，掉到 #6**，同时 `mattpocock/skills` 丢掉了它连坐九个窗口（2026-06-24 → 2026-08-27）的 #1。接手的那个 [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 仍然是一个 skills 合集——但是**垂直**合集，这是新东西。现在的形态该读成"浪潮开始找垂直"，而不是"浪潮结束了"；同时这两个窗口都在提醒：单窗口的跳增要当心，连续三次（jcode、addyosmani、Codex）都没能活过下一次刷新。

## Agent 榜

端到端的 agent——拿来直接干活的产品。垂类细分见 [Agent 垂类排行](agent-verticals.md)。

<!-- auto:board:agent -->
| 排名 | 项目 | 垂类 | Stars | 本周增量 | 状态 |
| --- | --- | --- | --- | --- | --- |
| #1 | [OpenClaw](https://github.com/openclaw/openclaw) | 通用助理 | 388.5k | +792 | 已收录 · [profile](../agents/openclaw.md) |
| #2 | [Hermes Agent](https://github.com/nousresearch/hermes-agent) | 通用助理 | 239.5k | +2,595 | 已收录 · [profile](../agents/hermes-agent.md) |
| #3 | [AutoGPT](https://github.com/significant-gravitas/autogpt) | 通用助理 | 187.1k | +162 | 已收录 · [profile](../agents/autogpt.md) |
| #4 | [Claude Code](https://github.com/anthropics/claude-code) | 编程开发 | 143.7k | +593 | 已收录 · [profile](../agents/claude-code.md) |
| #5 | [Codex CLI](https://github.com/openai/codex) | 编程开发 | 120.7k | +1,915 | 已收录 · [profile](../agents/codex.md) |
| #6 | [TradingAgents](https://github.com/tauricresearch/tradingagents) | 金融 | 102.2k | +1,455 | 不收录 |
| #7 | [Pi](https://github.com/earendil-works/pi) | 编程开发 | 100.5k | +2,707 | 已收录 · [profile](../agents/pi.md) |
| #8 | [OpenHands](https://github.com/openhands/openhands) | 编程开发 | 85.9k | +681 | 已收录 · [profile](../agents/openhands.md) |
| #9 | [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | 通用助理 | 68.2k | +60 | 已收录 · [profile](../agents/open-interpreter.md) |
| #10 | [Cline](https://github.com/cline/cline) | 编程开发 | 67.3k | +381 | 已收录 · [profile](../agents/cline.md) |
| #11 | [Goose](https://github.com/aaif-goose/goose) | 通用助理 | 53.8k | +275 | 已收录 · [profile](../agents/goose.md) |
| #12 | [Aider](https://github.com/aider-ai/aider) | 编程开发 | 48.7k | +139 | 已收录 · [profile](../agents/aider.md) |
| #13 | [CodeWhale](https://github.com/hmbown/codewhale) | 编程开发 | 40.9k | +24 | 已收录 · [profile](../agents/codewhale.md) |
| #14 | [OpenHuman](https://github.com/tinyhumansai/openhuman) | 通用助理 | 39.3k | +1,111 | 已收录 · [profile](../agents/openhuman.md) |
| #15 | [Continue](https://github.com/continuedev/continue) | 编程开发 | 35.7k | +81 | 已收录 · [profile](../agents/continue.md) |
| #16 | [Grok Build](https://github.com/xai-org/grok-build) | 编程开发 | 26.3k | +235 | 已收录 · [profile](../agents/grok-build.md) |
| #17 | [Open Code Review](https://github.com/alibaba/open-code-review) | 编程开发 | 21.8k | +315 | 已收录 · [profile](../agents/open-code-review.md) |
| #18 | [SWE-agent](https://github.com/swe-agent/swe-agent) | 编程开发 | 20.2k | +41 | 已收录 · [profile](../agents/swe-agent.md) |
| #19 | [jcode](https://github.com/1jehuang/jcode) | 编程开发 | 19.0k | +322 | 已收录 · [profile](../agents/jcode.md) |
| #20 | [OpenHarness](https://github.com/hkuds/openharness) | 编程开发 | 15.6k | +65 | 已收录 · [profile](../agents/openharness.md) |
| #21 | [QM](https://github.com/yc-software/qm) | 通用助理 | 14.4k | +188 | 已收录 · [profile](../agents/qm.md) |
| #22 | [MiMoCode](https://github.com/xiaomimimo/mimo-code) | 编程开发 | 12.9k | +42 | 已收录 · [profile](../agents/mimocode.md) |
| #23 | [Omnigent](https://github.com/omnigent-ai/omnigent) | 编程开发 | 9.6k | +275 | 已收录 · [profile](../agents/omnigent.md) |
| #24 | [Kimi Code](https://github.com/moonshotai/kimi-code) | 编程开发 | 7.2k | +115 | 已收录 · [profile](../agents/kimi-code.md) |
| #25 | [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent) | 编程开发 | 6.9k | +123 | 已收录 · [profile](../agents/mini-swe-agent.md) |
| #26 | [CoStrict](https://github.com/zgsm-ai/costrict) | 编程开发 | 4.4k | +7 | 已收录 · [profile](../agents/costrict.md) |
<!-- /auto:board:agent -->

## Agent 基础设施榜

agent 之下的那一层——框架、编排、记忆与上下文、网关和工作流引擎。它们不是"指着任务就能跑"的 agent，而是 agent 开发者用来搭建系统的底座。

<!-- auto:board:infra -->
| 排名 | 项目 | 分组 | Stars | 本周增量 | 状态 |
| --- | --- | --- | --- | --- | --- |
| #1 | [n8n](https://github.com/n8n-io/n8n) | 工作流 | 203.1k | +527 | 已收录 · [profile](../agents/n8n.md) |
| #2 | [LangChain](https://github.com/langchain-ai/langchain) | 框架 | 145.4k | +373 | 已收录 · [profile](../agents/langchain.md) |
| #3 | [Ruflo](https://github.com/ruvnet/ruflo) | 编排 | 70.1k | +646 | 已收录 · [profile](../agents/ruflo.md) |
| #4 | [CodeGraph](https://github.com/colbymchenry/codegraph) | 记忆与上下文 | 69.1k | +814 | 已收录 · [profile](../agents/codegraph.md) |
| #5 | [CrewAI](https://github.com/crewaiinc/crewai) | 框架 | 58.0k | +312 | 已收录 · [profile](../agents/crewai.md) |
| #6 | [LiteLLM](https://github.com/berriai/litellm) | 网关与执行 | 57.8k | +430 | 已收录 · [profile](../agents/litellm.md) |
| #7 | [Flowise](https://github.com/flowiseai/flowise) | 工作流 | 55.4k | +5 | 已收录 · [profile](../agents/flowise.md) |
| #8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 框架 | 52.0k | +87 | 已收录 · [profile](../agents/llamaindex.md) |
| #9 | [CLI-Anything](https://github.com/hkuds/cli-anything) | 网关与执行 | 48.8k | +502 | 已收录 · [profile](../agents/cli-anything.md) |
| #10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 编排 | 40.9k | +368 | 已收录 · [profile](../agents/langgraph.md) |
| #11 | [Langfuse](https://github.com/langfuse/langfuse) | 观测与评估 | 34.1k | +285 | 已收录 · [profile](../agents/langfuse.md) |
| #12 | [agentmemory](https://github.com/rohitg00/agentmemory) | 记忆与上下文 | 27.9k | +378 | 候补 |
| #13 | [Letta (MemGPT)](https://github.com/letta-ai/letta) | 记忆与上下文 | 24.5k | +86 | 已收录 · [profile](../agents/memgpt.md) |
| #14 | [eve](https://github.com/vercel/eve) | 框架 | 4.9k | — | 已收录 · [profile](../agents/eve.md) |
<!-- /auto:board:infra -->

## Skill 榜

skill 合集、skill 框架和 agent 方法论——内容资产而非 agent 表面。多数作为候补跟踪；框架那一端通过 [Superpowers](../agents/superpowers.md) 的 profile 覆盖。方向细分见 [Skill 垂类排行](skill-verticals.md)。

<!-- auto:board:skill -->
| 排名 | 项目 | 方向 | Stars | 本周增量 | 状态 |
| --- | --- | --- | --- | --- | --- |
| #1 | [Superpowers](https://github.com/obra/superpowers) | 通用技能集 | 280.4k | +2,308 | 已收录 · [profile](../agents/superpowers.md) |
| #2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 通用技能集 | 243.9k | +5,954 | 候补 |
| #3 | [anthropics/skills](https://github.com/anthropics/skills) | 通用技能集 | 173.0k | +1,173 | 候补 |
| #4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 通用技能集 | 91.4k | +1,418 | 候补 |
| #5 | [academic-research-skills](https://github.com/imbad0202/academic-research-skills) | 学术科研 | 44.8k | +975 | 候补 |
| #6 | [scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills) | 学术科研 | 41.5k | +6,750 | 候补 |
| #7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 金融 | 34.6k | +93 | 不收录 |
| #8 | [12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 方法论 | 25.6k | +129 | 不收录 |
<!-- /auto:board:skill -->

## 垂类排行

- [Agent 垂类排行](agent-verticals.md)——编程开发、通用助理、金融
- [Skill 垂类排行](skill-verticals.md)——通用技能集、学术科研、金融、方法论

本页表格和趋势图由 `scripts/render-rankings.py` 与 `scripts/render-trend.py` 在每次发布时自动重新生成——标记块内的表格不要手工编辑。
