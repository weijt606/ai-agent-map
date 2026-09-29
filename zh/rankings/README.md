# 分类排行

[English](../../rankings/README.md) | [中文](../README.md)

主页的[热门榜](../README.md#近期热门榜)按 **周增量** 排序，看的是势头；这一页的榜单按 **当前 star 总量** 排序，看的是各类别的存量格局。两边对照读：总量高但没进热榜的项目是已站稳的老玩家，总量低但冲上热榜的项目是正在爆发的新势力。

> **最后更新：** 2026-09-30 · **Star 总数：** 来自最近一次追踪抓取 · **排序：** 当前 star 总量，本周增量仅作参考

> **本期"周增量"列的说明：** 下面的数字覆盖 **2026-09-24 → 2026-09-30（6 天）**，比正常窗口少一天。上一期那一列是 7 天，所以两列原始数字不能直接比——要比就比周率（增量 ÷ 天数 × 7）。

## 排名趋势

每周热度 Top 10 自开始追踪以来的名次变化——一条折线一个项目，越靠上名次越好，折线中断表示该周掉出榜单：

<p align="center">
  <img src="../../assets/heat-trend-zh.svg" alt="每周热度排行趋势图（bump chart）" width="100%" />
</p>

到目前为止的主线：早期榜单由 Hermes Agent 统治，5 月底起 `.claude/skills` 浪潮接管，6 月中以后前三名几乎完全在 curated skills 合集之间轮换。**这条线在 9 月被掰弯了。** 连续两个窗口（2026-09-17 与 2026-09-24），增量榜前两席都由 coding agent 占住——[Open Code Review](../agents/open-code-review.md) 与 [DeepSeek Harness](../agents/deepseek-harness.md)——这是自 **2026-05-08**、也就是这波浪潮开始之前，第一次出现前二全是 agent。2026-09-30 这一期前二又分开了：DeepSeek Harness 拿到它的第一个 #1，[mattpocock/skills](https://github.com/mattpocock/skills) 回到 #2，而浪潮升到十席中的**五席**，连续第三次多拿一席。现在的形态该读成"浪潮在向垂直和厂商集合扩散"，而不是"浪潮结束了"。同时对单窗口跳增要格外当心，因为本榜自己的记录并不好看——jcode、addyosmani、Codex CLI、K-Dense、TradingAgents，以及最近的 Claude Code，都在那个让它们看起来像趋势的窗口之后的下一期回落了。Open Code Review 与 anthropics/financial-services 是最近的反例：两者都扛过了第二个窗口，随后也都是放缓，而不是继续上冲。

## Agent 榜

端到端的 agent——拿来直接干活的产品。垂类细分见 [Agent 垂类排行](agent-verticals.md)。

<!-- auto:board:agent -->
| 排名 | 项目 | 垂类 | Stars | 本周增量 | 状态 |
| --- | --- | --- | --- | --- | --- |
| #1 | [OpenClaw](https://github.com/openclaw/openclaw) | 通用助理 | 390.8k | +450 | 已收录 · [profile](../agents/openclaw.md) |
| #2 | [Hermes Agent](https://github.com/nousresearch/hermes-agent) | 通用助理 | 250.1k | +1,652 | 已收录 · [profile](../agents/hermes-agent.md) |
| #3 | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 编程开发 | 240.0k | +5,633 | 已收录 · [profile](../agents/deepseek-harness.md) |
| #4 | [OpenCode](https://github.com/anomalyco/opencode) | 编程开发 | 210.9k | +1,243 | 已收录 · [profile](../agents/opencode.md) |
| #5 | [AutoGPT](https://github.com/significant-gravitas/autogpt) | 通用助理 | 187.6k | +102 | 已收录 · [profile](../agents/autogpt.md) |
| #6 | [Claude Code](https://github.com/anthropics/claude-code) | 编程开发 | 148.6k | +781 | 已收录 · [profile](../agents/claude-code.md) |
| #7 | [Codex CLI](https://github.com/openai/codex) | 编程开发 | 127.2k | +1,009 | 已收录 · [profile](../agents/codex.md) |
| #8 | [Browser Use](https://github.com/browser-use/browser-use) | 通用助理 | 116.7k | +656 | 已收录 · [profile](../agents/browser-use.md) |
| #9 | [Pi](https://github.com/earendil-works/pi) | 编程开发 | 110.4k | +1,467 | 已收录 · [profile](../agents/pi.md) |
| #10 | [TradingAgents](https://github.com/tauricresearch/tradingagents) | 金融 | 109.3k | +937 | 不收录 |
| #11 | [Gemini CLI](https://github.com/google-gemini/gemini-cli) | 编程开发 | 107.2k | +56 | 已收录 · [profile](../agents/gemini-cli.md) |
| #12 | [OpenHands](https://github.com/openhands/openhands) | 编程开发 | 89.5k | +543 | 已收录 · [profile](../agents/openhands.md) |
| #13 | [Cline](https://github.com/cline/cline) | 编程开发 | 69.6k | +392 | 已收录 · [profile](../agents/cline.md) |
| #14 | [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | 通用助理 | 68.5k | +60 | 已收录 · [profile](../agents/open-interpreter.md) |
| #15 | [Goose](https://github.com/aaif-goose/goose) | 通用助理 | 54.8k | +185 | 已收录 · [profile](../agents/goose.md) |
| #16 | [Aider](https://github.com/aider-ai/aider) | 编程开发 | 49.3k | +144 | 已收录 · [profile](../agents/aider.md) |
| #17 | [Open Code Review](https://github.com/alibaba/open-code-review) | 编程开发 | 42.6k | +2,387 | 已收录 · [profile](../agents/open-code-review.md) |
| #18 | [CodeWhale](https://github.com/hmbown/codewhale) | 编程开发 | 41.0k | +9 | 已收录 · [profile](../agents/codewhale.md) |
| #19 | [OpenHuman](https://github.com/tinyhumansai/openhuman) | 通用助理 | 40.2k | +96 | 已收录 · [profile](../agents/openhuman.md) |
| #20 | [Continue](https://github.com/continuedev/continue) | 编程开发 | 36.1k | +60 | 已收录 · [profile](../agents/continue.md) |
| #21 | [Qwen Code](https://github.com/qwenlm/qwen-code) | 编程开发 | 28.2k | +123 | 已收录 · [profile](../agents/qwen-code.md) |
| #22 | [Grok Build](https://github.com/xai-org/grok-build) | 编程开发 | 27.2k | +101 | 已收录 · [profile](../agents/grok-build.md) |
| #23 | [SWE-agent](https://github.com/swe-agent/swe-agent) | 编程开发 | 20.4k | +57 | 已收录 · [profile](../agents/swe-agent.md) |
| #24 | [jcode](https://github.com/1jehuang/jcode) | 编程开发 | 20.2k | +156 | 已收录 · [profile](../agents/jcode.md) |
| #25 | [OpenHarness](https://github.com/hkuds/openharness) | 编程开发 | 15.9k | +41 | 已收录 · [profile](../agents/openharness.md) |
| #26 | [QM](https://github.com/yc-software/qm) | 通用助理 | 15.3k | +64 | 已收录 · [profile](../agents/qm.md) |
| #27 | [MiMoCode](https://github.com/xiaomimimo/mimo-code) | 编程开发 | 13.6k | +116 | 已收录 · [profile](../agents/mimocode.md) |
| #28 | [Omnigent](https://github.com/omnigent-ai/omnigent) | 编程开发 | 10.3k | +159 | 已收录 · [profile](../agents/omnigent.md) |
| #29 | [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent) | 编程开发 | 8.1k | +170 | 已收录 · [profile](../agents/mini-swe-agent.md) |
| #30 | [Kimi Code](https://github.com/moonshotai/kimi-code) | 编程开发 | 7.7k | +100 | 已收录 · [profile](../agents/kimi-code.md) |
| #31 | [CoStrict](https://github.com/zgsm-ai/costrict) | 编程开发 | 4.4k | +1 | 已收录 · [profile](../agents/costrict.md) |
<!-- /auto:board:agent -->

## Agent 基础设施榜

agent 之下的那一层——框架、编排、记忆与上下文、网关和工作流引擎。它们不是"指着任务就能跑"的 agent，而是 agent 开发者用来搭建系统的底座。

<!-- auto:board:infra -->
| 排名 | 项目 | 分组 | Stars | 本周增量 | 状态 |
| --- | --- | --- | --- | --- | --- |
| #1 | [n8n](https://github.com/n8n-io/n8n) | 工作流 | 206.3k | +497 | 已收录 · [profile](../agents/n8n.md) |
| #2 | [LangChain](https://github.com/langchain-ai/langchain) | 框架 | 147.3k | +334 | 已收录 · [profile](../agents/langchain.md) |
| #3 | [Ruflo](https://github.com/ruvnet/ruflo) | 编排 | 73.5k | +361 | 已收录 · [profile](../agents/ruflo.md) |
| #4 | [CodeGraph](https://github.com/colbymchenry/codegraph) | 记忆与上下文 | 72.4k | +440 | 已收录 · [profile](../agents/codegraph.md) |
| #5 | [LiteLLM](https://github.com/berriai/litellm) | 网关与执行 | 59.9k | +377 | 已收录 · [profile](../agents/litellm.md) |
| #6 | [CrewAI](https://github.com/crewaiinc/crewai) | 框架 | 59.2k | +235 | 已收录 · [profile](../agents/crewai.md) |
| #7 | [Flowise](https://github.com/flowiseai/flowise) | 工作流 | 55.5k | +16 | 已收录 · [profile](../agents/flowise.md) |
| #8 | [LlamaIndex](https://github.com/run-llama/llama_index) | 框架 | 52.4k | +59 | 已收录 · [profile](../agents/llamaindex.md) |
| #9 | [CLI-Anything](https://github.com/hkuds/cli-anything) | 网关与执行 | 51.0k | +1,084 | 已收录 · [profile](../agents/cli-anything.md) |
| #10 | [LangGraph](https://github.com/langchain-ai/langgraph) | 编排 | 42.5k | +280 | 已收录 · [profile](../agents/langgraph.md) |
| #11 | [Langfuse](https://github.com/langfuse/langfuse) | 观测与评估 | 35.2k | +227 | 已收录 · [profile](../agents/langfuse.md) |
| #12 | [agentmemory](https://github.com/rohitg00/agentmemory) | 记忆与上下文 | 29.0k | +249 | 候补 |
| #13 | [Letta (MemGPT)](https://github.com/letta-ai/letta) | 记忆与上下文 | 25.0k | +111 | 已收录 · [profile](../agents/memgpt.md) |
| #14 | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 框架 | 13.9k | +105 | 已收录 · [profile](../agents/microsoft-agent-framework.md) |
| #15 | [Graft](https://github.com/trailhq/graft) | 记忆与上下文 | 9.4k | — | 已收录 · [profile](../agents/graft.md) |
| #16 | [TrueForge](https://github.com/truefoundry/trueforge) | 框架 | 6.0k | +78 | 已收录 · [profile](../agents/trueforge.md) |
| #17 | [eve](https://github.com/vercel/eve) | 框架 | 5.4k | +73 | 已收录 · [profile](../agents/eve.md) |
<!-- /auto:board:infra -->

## Skill 榜

skill 合集、skill 框架和 agent 方法论——内容资产而非 agent 表面。多数作为候补跟踪；框架那一端通过 [Superpowers](../agents/superpowers.md) 的 profile 覆盖。方向细分见 [Skill 垂类排行](skill-verticals.md)。

<!-- auto:board:skill -->
| 排名 | 项目 | 方向 | Stars | 本周增量 | 状态 |
| --- | --- | --- | --- | --- | --- |
| #1 | [Superpowers](https://github.com/obra/superpowers) | 通用技能集 | 292.9k | +2,265 | 已收录 · [profile](../agents/superpowers.md) |
| #2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 通用技能集 | 272.0k | +3,550 | 候补 |
| #3 | [anthropics/skills](https://github.com/anthropics/skills) | 通用技能集 | 179.0k | +1,166 | 候补 |
| #4 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 通用技能集 | 99.9k | +1,197 | 候补 |
| #5 | [academic-research-skills](https://github.com/imbad0202/academic-research-skills) | 学术科研 | 49.9k | +604 | 候补 |
| #6 | [scientific-agent-skills](https://github.com/k-dense-ai/scientific-agent-skills) | 学术科研 | 47.1k | +790 | 候补 |
| #7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 金融 | 38.2k | +1,297 | 不收录 |
| #8 | [12-factor-agents](https://github.com/humanlayer/12-factor-agents) | 方法论 | 26.5k | +97 | 不收录 |
<!-- /auto:board:skill -->

## 垂类排行

- [Agent 垂类排行](agent-verticals.md)——编程开发、通用助理、金融
- [Skill 垂类排行](skill-verticals.md)——通用技能集、学术科研、金融、方法论

本页表格和趋势图由 `scripts/render-rankings.py` 与 `scripts/render-trend.py` 在每次发布时自动重新生成——标记块内的表格不要手工编辑。
