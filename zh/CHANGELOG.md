# 更新日志

[English](../CHANGELOG.md) | [中文](CHANGELOG.md)

记录本仓库的结构性里程碑，新的在前。热度表每周三例行刷新，例行更新见 git 历史和 [agents/README.md](agents/README.md) 的"市场事件"时间线，不在此处逐条记录。

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
