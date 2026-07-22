# 更新日志

[English](../CHANGELOG.md) | [中文](CHANGELOG.md)

记录本仓库的结构性里程碑，新的在前。热度表每周三例行刷新，例行更新见 git 历史和 [agents/README.md](agents/README.md) 的"市场事件"时间线，不在此处逐条记录。

## 2026-07-22 —— jcode 加入 harness 路线

- **新增 [jcode](agents/jcode.md) profile**（EN + zh）——这个 Rust 多会话 coding harness（`1jehuang/jcode`，MIT，10.6k）在进入每周增量前 10（#7）后，从候补转正为已收录 profile。它与 [Pi](agents/pi.md) 一起归入 **agent harness 框架** 路线，并接入 [harness 对比](comparisons/agent-harness-frameworks.md)（现为六个）、[选型矩阵](comparisons/mainstream-agent-landscape.md) 和 [编码自动化指南](use-cases/coding-automation.md)。覆盖数升至 55 个 profile；`catalog.json` 已把 jcode 标为已收录。

## 2026-07-16 —— 主页瘦身、厂商信息刷新、市场事件档案

- **README 重构降密度**：两个市场事件板块收成三条"市场脉搏"要点；50 行覆盖表折叠成四个可展开分组；热榜附注折叠；harness 表迁至 [comparisons/agent-harness-frameworks.md](comparisons/agent-harness-frameworks.md)；导航合并并新增排行入口。
- **厂商 profile 追平 2026 年 7 月**：Codex（7 月 9 日并入 ChatGPT 应用、GPT-5.6 驱动）、Claude Code（Fable 5 / Opus 4.8 模型演进）、Cursor、GitHub Copilot、GPT-5.5（发布后格局）。
- **新增 [Claude Fable 5](agents/claude-fable-5.md) profile**——Anthropic 的 Mythos 级加入前沿 agentic 模型路线。
- **新增 [market-events.md](../market-events.md)**（EN + zh）：结构性事件的长期档案，skills 浪潮数据已刷新。

## 2026-07-16 —— 排行体系扩建：趋势图、分类榜、垂类榜

- **每周排名趋势图（bump chart）**（`assets/heat-trend-{en,zh}.svg`），嵌入两个语言的主页和 [rankings/](rankings/README.md)。2026-04-11 以来的每个每周 top-N 窗口已从 git 历史回溯进 `scripts/history.json`；图表随每次发布自动重绘。
- **新增 [rankings/](rankings/README.md) 板块**（EN + zh 镜像）：Agent 榜、Agent 基础设施榜、Skill 榜，按当前 star 总量排序——存量视角，与主页按增量排序的热榜互补。
- **垂类排行**：agent 分为编程开发 / 通用助理 / 金融（[agent-verticals](rankings/agent-verticals.md)），skill 分为通用技能集 / 学术科研 / 金融 / 方法论（[skill-verticals](rankings/skill-verticals.md)）。
- **追踪仓库 23 → 42**：Claude Code、Aider、Cline、Continue、OpenHands、SWE-agent、mini-swe-agent、OpenHarness、Goose、AutoGPT、LangChain、LangGraph、CrewAI、LlamaIndex、n8n、Letta、Open Interpreter、LiteLLM、Flowise 加入每周 star 追踪，分类元数据在 `scripts/catalog.json`。
- **管线**：所有排行表格随发布自动重新生成；`validate.py` 新增历史文件与 README 热表的交叉校验，并拒绝过期图表。

## 2026-06-17 —— 每周更新自动化机制

`scripts/` 增加每周工具链：`fetch-stars.py`（star 抓取 + 快照）、`validate.py`（完整性闸门：链接、中英对等、热表同步）、`weekly-update.sh`（发布闸门——校验不通过一律不推送）、周三 playbook，以及每次 push 都跑的 CI 校验。

## 2026-06-11 —— 终端 Coding CLI 对比

新增对比页[终端 Coding CLI Agent 对比](comparisons/coding-cli-agents.md)；同期收录 Kimi Code、MiMoCode、CoStrict。

## 2026-05-23 —— Agent harness 框架路线

harness 框架拆为一级路线（Pi、OpenHands、SWE-agent、mini-swe-agent、OpenHarness），主页增加聚焦表。同周收录 OpenHuman、CodeGraph、CLI-Anything。

## 2026-05-19 —— 记录 `.claude/skills` 浪潮

skills 浪潮成为持续追踪的市场事件：curated 合集作为候补跟踪，框架端通过 Superpowers 的 profile 覆盖。

## 2026-04-24 —— 框架批次 + 像素风 banner

收录 Continue、CrewAI、AutoGPT、LlamaIndex、n8n、MemGPT；热度表加上更新时间戳和快照窗口；换上像素风 banner。

## 2026-04-11 —— 引入热度排行

第一份每周热度快照：按 star 增量排名的热门 agent 覆盖表。

## 2026-04-09 —— 项目启动

双语（EN + zh）agent 地图启动：路线分类、第一批 coding agent profile、对比页与用例脚手架。
