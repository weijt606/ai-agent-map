# 分类排行

[English](../../rankings/README.md) | [中文](../README.md)

主页的[热门榜](../README.md#近期热门榜)按 **周增量** 排序，看的是势头；这一页的榜单按 **当前 star 总量** 排序，看的是各类别的存量格局。两边对照读：总量高但没进热榜的项目是已站稳的老玩家，总量低但冲上热榜的项目是正在爆发的新势力。

> **最后更新：** 2026-09-09 · **Star 总数：** 来自最近一次追踪抓取 · **排序：** 当前 star 总量，本周增量仅作参考

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
| #1 | [OpenClaw](https://github.com/openclaw/openclaw) | 通用助理 | 389.3k | +241 | 已收录 · [profile](../agents/openclaw.md) |
| #2 | [Hermes Agent](https://github.com/nousresearch/hermes-agent) | 通用助理 | 243.7k | +1,232 | 已收录 · [profile](../agents/hermes-agent.md) |
| #3 | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 编程开发 | 217.2k | +3,226 | 已收录 · [profile](../agents/deepseek-harness.md) |
| #4 | [OpenCode](https://github.com/anomalyco/opencode) | 编程开发 | 206.1k | +916 | 已收录 · [profile](../agents/opencode.md) |
| #5 | [AutoGPT](https://github.com/significant-gravitas/autogpt) | 通用助理 | 187.2k | +47 | 已收录 · [profile](../agents/autogpt.md) |
| #6 | [Claude Code](https://github.com/anthropics/claude-code) | 编程开发 | 144.5k | +263 | 已收录 · [profile](../agents/claude-code.md) |
| #7 | [Codex CLI](https://github.com/openai/codex) | 编程开发 | 122.8k | +814 | 已收录 · [profile](../agents/codex.md) |
| #8 | [Browser Use](https://github.com/browser-use/browser-use) | 通用助理 | 113.9k | +1,228 | 已收录 · [profile](../agents/browser-use.md) |
| #9 | [Gemini CLI](https://github.com/google-gemini/gemini-cli) | 编程开发 | 106.9k | +38 | 已收录 · [profile](../agents/gemini-cli.md) |
| #10 | [TradingAgents](https://github.com/tauricresearch/tradingagents) | 金融 | 103.6k | +924 | 不收录 |
| #11 | [Pi](https://github.com/earendil-works/pi) | 编程开发 | 103.4k | +1,028 | 已收录 · [profile](../agents/pi.md) |
| #12 | [OpenHands](https://github.com/openhands/openhands) | 编程开发 | 87.0k | +666 | 已收录 · [profile](../agents/openhands.md) |
| #13 | [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | 通用助理 | 68.3k | +20 | 已收录 · [profile](../agents/open-interpreter.md) |
| #14 | [Cline](https://github.com/cline/cline) | 编程开发 | 67.7k | +140 | 已收录 · [profile](../agents/cline.md) |
| #15 | [Goose](https://github.com/aaif-goose/goose) | 通用助理 | 54.1k | +85 | 已收录 · [profile](../agents/goose.md) |
| #16 | [Aider](https://github.com/aider-ai/aider) | 编程开发 | 48.9k | +58 | 已收录 · [profile](../agents/aider.md) |
| #17 | [CodeWhale](https://github.com/hmbown/codewhale) | 编程开发 | 40.9k | +19 | 已收录 · [profile](../agents/codewhale.md) |
| #18 | [OpenHuman](https://github.com/tinyhumansai/openhuman) | 通用助理 | 39.6k | +85 | 已收录 · [profile](../agents/openhuman.md) |
| #19 | [Continue](https://github.com/continuedev/continue) | 编程开发 | 35.8k | +36 | 已收录 · [profile](../agents/continue.md) |
| #20 | [Qwen Code](https://github.com/qwenlm/qwen-code) | 编程开发 | 27.7k | +40 | 已收录 · [profile](../agents/qwen-code.md) |
| #21 | [Grok Build](https://github.com/xai-org/grok-build) | 编程开发 | 26.6k | +94 | 已收录 · [profile](../agents/grok-build.md) |
| #22 | [Open Code Review](https://github.com/alibaba/open-code-review) | 编程开发 | 22.1k | +157 | 已收录 · [profile](../agents/open-code-review.md) |
| #23 | [SWE-agent](https://github.com/swe-agent/swe-agent) | 编程开发 | 20.3k | +33 | 已收录 · [profile](../agents/swe-agent.md) |
| #24 | [jcode](https://github.com/1jehuang/jcode) | 编程开发 | 19.4k | +158 | 已收录 · [profile](../agents/jcode.md) |
| #25 | [OpenHarness](https://github.com/hkuds/openharness) | 编程开发 | 15.7k | +33 | 已收录 · [profile](../agents/openharness.md) |
| #26 | [QM](https://github.com/yc-software/qm) | 通用助理 | 14.8k | +135 | 已收录 · [profile](../agents/qm.md) |
| #27 | [MiMoCode](https://github.com/xiaomimimo/mimo-code) | 编程开发 | 13.0k | +48 | 已收录 · [profile](../agents/mimocode.md) |
| #28 | [Omnigent](https://github.com/omnigent-ai/omnigent) | 编程开发 | 9.8k | +61 | 已收录 · [profile](../agents/omnigent.md) |
| #29 | [Kimi Code](https://github.com/moonshotai/kimi-code) | 编程开发 | 7.3k | +38 | 已收录 · [profile](../agents/kimi-code.md) |
| #30 | [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent) | 编程开发 | 7.2k | +204 | 已收录 · [profile](../agents/mini-swe-agent.md) |
| #31 | [CoStrict](https://github.com/zgsm-ai/costrict) | 编程开发 | 4.4k | +3 | 已收录 · [profile](../agents/costrict.md) |
<!-- /auto:board:agent -->

## Agent 基础设施榜

agent 之下的那一层——框架、编排、记忆与上下文、网关和工作流引擎。它们不是"指着任务就能跑"的 agent，而是 agent 开发者用来搭建系统的底座。

<!-- auto:board:infra -->
| 排名 | 项目 | 分组 | Stars | 本周增量 | 状态 |
| --- | --- | --- | --- | --- | --- |
| #1 | [n8n](https://github.com/n8n-io/n8n) | 工作流 | 203.8k | +286 | 已收录 · [profile](../agents/n8n.md) |
| #2 | [LangChain](https://github.com/langchain-ai/langchain) | 框架 | 146.0k | +200 | 已收录 · [profile](../agents/langchain.md) |
| #3 | [Ruflo](https://github.com/ruvnet/ruflo) | 编排 | 71.8k | +824 | 已收录 · [profile](../agents/ruflo.md) |
| #4 | [CodeGraph](https://github.com/colbymchenry/codegraph) | 记忆与上下文 | 70.2k | +385 | 已收录 · [profile](../agents/codegraph.md) |
| #5 | [LiteLLM](https://github.com/berriai/litellm) | 网关与执行 | 58.4k | +205 | 已收录 · [profile](../agents/litellm.md) |
| #6 | [CrewAI](https://github.com/crewaiinc/crewai) | 框架 | 58.3k | +125 | 已收录 · [profile](../agents/crewai.md) |
| #7 | [Flowise](https://github.com/flowiseai/flowise) | 工作流 | 55.4k | +19 | 已收录 · [profile](../agents/flowise.md) |
| #8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 框架 | 52.1k | +52 | 已收录 · [profile](../agents/llamaindex.md) |
| #9 | [CLI-Anything](https://github.com/hkuds/cli-anything) | 网关与执行 | 49.2k | +112 | 已收录 · [profile](../agents/cli-anything.md) |
| #10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 编排 | 41.3k | +183 | 已收录 · [profile](../agents/langgraph.md) |
| #11 | [Langfuse](https://github.com/langfuse/langfuse) | 观测与评估 | 34.4k | +144 | 已收录 · [profile](../agents/langfuse.md) |
| #12 | [agentmemory](https://github.com/rohitg00/agentmemory) | 记忆与上下文 | 28.2k | +110 | 候补 |
| #13 | [Letta (MemGPT)](https://github.com/letta-ai/letta) | 记忆与上下文 | 24.7k | +40 | 已收录 · [profile](../agents/memgpt.md) |
| #14 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 框架 | 13.4k | +70 | 已收录 · [profile](../agents/microsoft-agent-framework.md) |
| #15 | [TrueForge](https://github.com/truefoundry/trueforge) | 框架 | 5.3k | +67 | 已收录 · [profile](../agents/trueforge.md) |
| #16 | [eve](https://github.com/vercel/eve) | 框架 | 5.0k | +29 | 已收录 · [profile](../agents/eve.md) |
<!-- /auto:board:infra -->

## Skill 榜

skill 合集、skill 框架和 agent 方法论——内容资产而非 agent 表面。多数作为候补跟踪；框架那一端通过 [Superpowers](../agents/superpowers.md) 的 profile 覆盖。方向细分见 [Skill 垂类排行](skill-verticals.md)。

<!-- auto:board:skill -->
| 排名 | 项目 | 方向 | Stars | 本周增量 | 状态 |
| --- | --- | --- | --- | --- | --- |
| #1 | [Superpowers](https://github.com/obra/superpowers) | 通用技能集 | 283.8k | +1,414 | 已收录 · [profile](../agents/superpowers.md) |
| #2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 通用技能集 | 257.6k | +3,237 | 候补 |
| #3 | [anthropics/skills](https://github.com/anthropics/skills) | 通用技能集 | 175.4k | +534 | 候补 |
| #4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 通用技能集 | 93.2k | +590 | 候补 |
| #5 | [academic-research-skills](https://github.com/imbad0202/academic-research-skills) | 学术科研 | 47.2k | +661 | 候补 |
| #6 | [scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills) | 学术科研 | 44.0k | +793 | 候补 |
| #7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 金融 | 34.8k | +43 | 不收录 |
| #8 | [12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 方法论 | 25.8k | +41 | 不收录 |
<!-- /auto:board:skill -->

## 垂类排行

- [Agent 垂类排行](agent-verticals.md)——编程开发、通用助理、金融
- [Skill 垂类排行](skill-verticals.md)——通用技能集、学术科研、金融、方法论

本页表格和趋势图由 `scripts/render-rankings.py` 与 `scripts/render-trend.py` 在每次发布时自动重新生成——标记块内的表格不要手工编辑。
