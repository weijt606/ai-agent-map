# 分类排行

[English](../../rankings/README.md) | [中文](../README.md)

主页的[热门榜](../README.md#近期热门榜)按 **周增量** 排序，看的是势头；这一页的榜单按 **当前 star 总量** 排序，看的是各类别的存量格局。两边对照读：总量高但没进热榜的项目是已站稳的老玩家，总量低但冲上热榜的项目是正在爆发的新势力。

> **最后更新：** 2026-09-17 · **Star 总数：** 来自最近一次追踪抓取 · **排序：** 当前 star 总量，本周增量仅作参考

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
| #1 | [OpenClaw](https://github.com/openclaw/openclaw) | 通用助理 | 389.9k | +651 | 已收录 · [profile](../agents/openclaw.md) |
| #2 | [Hermes Agent](https://github.com/nousresearch/hermes-agent) | 通用助理 | 246.3k | +2,616 | 已收录 · [profile](../agents/hermes-agent.md) |
| #3 | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 编程开发 | 227.2k | +10,049 | 已收录 · [profile](../agents/deepseek-harness.md) |
| #4 | [OpenCode](https://github.com/anomalyco/opencode) | 编程开发 | 208.0k | +1,920 | 已收录 · [profile](../agents/opencode.md) |
| #5 | [AutoGPT](https://github.com/significant-gravitas/autogpt) | 通用助理 | 187.4k | +179 | 已收录 · [profile](../agents/autogpt.md) |
| #6 | [Claude Code](https://github.com/anthropics/claude-code) | 编程开发 | 145.7k | +1,177 | 已收录 · [profile](../agents/claude-code.md) |
| #7 | [Codex CLI](https://github.com/openai/codex) | 编程开发 | 124.9k | +2,097 | 已收录 · [profile](../agents/codex.md) |
| #8 | [Browser Use](https://github.com/browser-use/browser-use) | 通用助理 | 114.9k | +982 | 已收录 · [profile](../agents/browser-use.md) |
| #9 | [TradingAgents](https://github.com/tauricresearch/tradingagents) | 金融 | 107.2k | +3,541 | 不收录 |
| #10 | [Gemini CLI](https://github.com/google-gemini/gemini-cli) | 编程开发 | 107.0k | +153 | 已收录 · [profile](../agents/gemini-cli.md) |
| #11 | [Pi](https://github.com/earendil-works/pi) | 编程开发 | 106.5k | +3,075 | 已收录 · [profile](../agents/pi.md) |
| #12 | [OpenHands](https://github.com/openhands/openhands) | 编程开发 | 88.2k | +1,209 | 已收录 · [profile](../agents/openhands.md) |
| #13 | [Cline](https://github.com/cline/cline) | 编程开发 | 68.5k | +778 | 已收录 · [profile](../agents/cline.md) |
| #14 | [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | 通用助理 | 68.4k | +83 | 已收录 · [profile](../agents/open-interpreter.md) |
| #15 | [Goose](https://github.com/aaif-goose/goose) | 通用助理 | 54.4k | +319 | 已收录 · [profile](../agents/goose.md) |
| #16 | [Aider](https://github.com/aider-ai/aider) | 编程开发 | 49.0k | +164 | 已收录 · [profile](../agents/aider.md) |
| #17 | [CodeWhale](https://github.com/hmbown/codewhale) | 编程开发 | 41.0k | +58 | 已收录 · [profile](../agents/codewhale.md) |
| #18 | [OpenHuman](https://github.com/tinyhumansai/openhuman) | 通用助理 | 39.8k | +276 | 已收录 · [profile](../agents/openhuman.md) |
| #19 | [Continue](https://github.com/continuedev/continue) | 编程开发 | 35.9k | +98 | 已收录 · [profile](../agents/continue.md) |
| #20 | [Open Code Review](https://github.com/alibaba/open-code-review) | 编程开发 | 33.1k | +10,935 | 已收录 · [profile](../agents/open-code-review.md) |
| #21 | [Qwen Code](https://github.com/qwenlm/qwen-code) | 编程开发 | 27.9k | +193 | 已收录 · [profile](../agents/qwen-code.md) |
| #22 | [Grok Build](https://github.com/xai-org/grok-build) | 编程开发 | 26.8k | +202 | 已收录 · [profile](../agents/grok-build.md) |
| #23 | [SWE-agent](https://github.com/swe-agent/swe-agent) | 编程开发 | 20.3k | +52 | 已收录 · [profile](../agents/swe-agent.md) |
| #24 | [jcode](https://github.com/1jehuang/jcode) | 编程开发 | 19.8k | +407 | 已收录 · [profile](../agents/jcode.md) |
| #25 | [OpenHarness](https://github.com/hkuds/openharness) | 编程开发 | 15.8k | +85 | 已收录 · [profile](../agents/openharness.md) |
| #26 | [QM](https://github.com/yc-software/qm) | 通用助理 | 15.1k | +355 | 已收录 · [profile](../agents/qm.md) |
| #27 | [MiMoCode](https://github.com/xiaomimimo/mimo-code) | 编程开发 | 13.2k | +151 | 已收录 · [profile](../agents/mimocode.md) |
| #28 | [Omnigent](https://github.com/omnigent-ai/omnigent) | 编程开发 | 10.0k | +221 | 已收录 · [profile](../agents/omnigent.md) |
| #29 | [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent) | 编程开发 | 7.7k | +454 | 已收录 · [profile](../agents/mini-swe-agent.md) |
| #30 | [Kimi Code](https://github.com/moonshotai/kimi-code) | 编程开发 | 7.4k | +111 | 已收录 · [profile](../agents/kimi-code.md) |
| #31 | [CoStrict](https://github.com/zgsm-ai/costrict) | 编程开发 | 4.4k | +21 | 已收录 · [profile](../agents/costrict.md) |
<!-- /auto:board:agent -->

## Agent 基础设施榜

agent 之下的那一层——框架、编排、记忆与上下文、网关和工作流引擎。它们不是"指着任务就能跑"的 agent，而是 agent 开发者用来搭建系统的底座。

<!-- auto:board:infra -->
| 排名 | 项目 | 分组 | Stars | 本周增量 | 状态 |
| --- | --- | --- | --- | --- | --- |
| #1 | [n8n](https://github.com/n8n-io/n8n) | 工作流 | 204.7k | +900 | 已收录 · [profile](../agents/n8n.md) |
| #2 | [LangChain](https://github.com/langchain-ai/langchain) | 框架 | 146.5k | +493 | 已收录 · [profile](../agents/langchain.md) |
| #3 | [Ruflo](https://github.com/ruvnet/ruflo) | 编排 | 72.7k | +905 | 已收录 · [profile](../agents/ruflo.md) |
| #4 | [CodeGraph](https://github.com/colbymchenry/codegraph) | 记忆与上下文 | 71.2k | +1,002 | 已收录 · [profile](../agents/codegraph.md) |
| #5 | [LiteLLM](https://github.com/berriai/litellm) | 网关与执行 | 59.0k | +597 | 已收录 · [profile](../agents/litellm.md) |
| #6 | [CrewAI](https://github.com/crewaiinc/crewai) | 框架 | 58.7k | +397 | 已收录 · [profile](../agents/crewai.md) |
| #7 | [Flowise](https://github.com/flowiseai/flowise) | 工作流 | 55.5k | +20 | 已收录 · [profile](../agents/flowise.md) |
| #8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 框架 | 52.2k | +102 | 已收录 · [profile](../agents/llamaindex.md) |
| #9 | [CLI-Anything](https://github.com/hkuds/cli-anything) | 网关与执行 | 49.5k | +339 | 已收录 · [profile](../agents/cli-anything.md) |
| #10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 编排 | 41.8k | +481 | 已收录 · [profile](../agents/langgraph.md) |
| #11 | [Langfuse](https://github.com/langfuse/langfuse) | 观测与评估 | 34.7k | +310 | 已收录 · [profile](../agents/langfuse.md) |
| #12 | [agentmemory](https://github.com/rohitg00/agentmemory) | 记忆与上下文 | 28.5k | +319 | 候补 |
| #13 | [Letta (MemGPT)](https://github.com/letta-ai/letta) | 记忆与上下文 | 24.8k | +95 | 已收录 · [profile](../agents/memgpt.md) |
| #14 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 框架 | 13.6k | +134 | 已收录 · [profile](../agents/microsoft-agent-framework.md) |
| #15 | [TrueForge](https://github.com/truefoundry/trueforge) | 框架 | 5.7k | +390 | 已收录 · [profile](../agents/trueforge.md) |
| #16 | [eve](https://github.com/vercel/eve) | 框架 | 5.3k | +303 | 已收录 · [profile](../agents/eve.md) |
<!-- /auto:board:infra -->

## Skill 榜

skill 合集、skill 框架和 agent 方法论——内容资产而非 agent 表面。多数作为候补跟踪；框架那一端通过 [Superpowers](../agents/superpowers.md) 的 profile 覆盖。方向细分见 [Skill 垂类排行](skill-verticals.md)。

<!-- auto:board:skill -->
| 排名 | 项目 | 方向 | Stars | 本周增量 | 状态 |
| --- | --- | --- | --- | --- | --- |
| #1 | [Superpowers](https://github.com/obra/superpowers) | 通用技能集 | 287.8k | +4,018 | 已收录 · [profile](../agents/superpowers.md) |
| #2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 通用技能集 | 263.9k | +6,317 | 候补 |
| #3 | [anthropics/skills](https://github.com/anthropics/skills) | 通用技能集 | 176.8k | +1,405 | 候补 |
| #4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 通用技能集 | 95.7k | +2,529 | 候补 |
| #5 | [academic-research-skills](https://github.com/imbad0202/academic-research-skills) | 学术科研 | 48.4k | +1,197 | 候补 |
| #6 | [scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills) | 学术科研 | 45.3k | +1,258 | 候补 |
| #7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 金融 | 34.9k | +120 | 不收录 |
| #8 | [12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 方法论 | 25.9k | +128 | 不收录 |
<!-- /auto:board:skill -->

## 垂类排行

- [Agent 垂类排行](agent-verticals.md)——编程开发、通用助理、金融
- [Skill 垂类排行](skill-verticals.md)——通用技能集、学术科研、金融、方法论

本页表格和趋势图由 `scripts/render-rankings.py` 与 `scripts/render-trend.py` 在每次发布时自动重新生成——标记块内的表格不要手工编辑。
