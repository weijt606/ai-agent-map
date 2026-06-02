# CodeGraph

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](codegraph.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/codegraph.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：CodeGraph 是一个本地代码知识图谱 + MCP server——它把代码库预先索引成可查询的 SQLite 数据库，让 Claude Code、Cursor、Codex CLI 这些 agent 在回答架构问题时显著减少工具调用和 token 消耗。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | colbymchenry（开源） |
| 路线 | Runtime & tools——代码知识图谱 / agent 上下文层 |
| 开源 | 是（MIT） |
| 适合谁 | 已经在用 [Claude Code](claude-code.md)、[Cursor](cursor.md)、[Codex](codex.md) CLI、opencode 或 [Hermes Agent](hermes-agent.md) 并想把代码探索成本压下来的团队 |
| 主要代价 | 多了一层索引要维护和同步；收益取决于代码库规模和探索频率 |
| GitHub 仓库 | https://github.com/colbymchenry/codegraph |

## 什么时候选它

- 你已经在用 [Claude Code](claude-code.md)、[Cursor](cursor.md)、[Codex](codex.md) CLI、opencode 或 [Hermes Agent](hermes-agent.md)，CodeGraph 通过 MCP 接入，不用学新 agent 表面。
- 你的代码库已经大到 agent 每次探索都要烧明显多的 token。
- 你想要在同一探索负载上拿到可量化的提升——项目方给出的中位数是便宜 35%、token 少 59%、快 49%、工具调用少 70%（真实代码库基准）。
- 你需要纯本地运行：无外部 API、无云、不传输数据。

## 什么时候不选

- 你的代码库小到 agent 直接扫一遍就够了，加索引层反而是 overhead。
- 你用的 agent 还不支持 MCP——没有连接器就没有价值。
- 你需要覆盖所有冷门语言——CodeGraph 通过 tree-sitter 覆盖 19+ 主流语言，长尾不保证。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 跨 agent 集成 | 非常强 | 对 [Claude Code](claude-code.md)、[Cursor](cursor.md)、[Codex](codex.md) CLI、OpenCode、Gemini、AntiGravity、Kiro、[Hermes Agent](hermes-agent.md) 都有一等公民 MCP plugin |
| 纯本地运行 | 非常强 | Tree-sitter + SQLite + FTS5，没有任何外部依赖 |
| 语言覆盖 | 强 | 19+ 语言，包括 TypeScript、Python、Go、Rust、Java |
| 实时同步 | 强 | 原生操作系统文件 watcher 保持图谱实时更新 |
| 影响分析 | 强 | 调用方/被调用方追踪、框架感知的路由识别 |

## 使用成本

复杂度：低到中。初始索引自动完成；常态成本只是保持数据库存活和 watcher 跑。收益随"这个函数在哪被调用？"这类问题的提问频率放大——小仓库不划算，中到大仓库 token 节省会主导。

## 底线

CodeGraph 是本仓库里第一个专门写给"agent 上下文基础设施"这层的 profile——意识到当 agent 越来越多做代码探索时，提升它最便宜的办法不是换更强的 agent，而是给它预先算好的结构。MCP 优先的设计让它能干净地嵌进本仓库已经收录的 agent（[Claude Code](claude-code.md)、[Cursor](cursor.md)、[Codex](codex.md) CLI、OpenCode、Gemini、AntiGravity、Kiro、[Hermes Agent](hermes-agent.md)）。如果你每周在代码问答上烧的 token 已经显著，那 35-70% 的官方改进数据就是评估时要打的基线。
