# Graphify

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](graphify.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/graphify.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话判断：Graphify 把一个项目目录（代码，愿意的话再加上文档、SQL schema、配置、PDF、图片和视频）变成一张存成文件的知识图谱——`graph.json`、`GRAPH_REPORT.md` 和 `graph.html`——你的编码 agent 通过 `/graphify` skill、CLI 或本地 MCP server 去查它，而不是去 grep 源码。代码那一遍是本地 tree-sitter 解析，不调模型、没有向量库；每条边都标明了来路。

> **同一个名字下有两样东西。** 开源的那部分是 PyPI 上的 `graphifyy` 包（两个 y；README 提醒其他 `graphify*` 包都与它无关），Apache-2.0，本地运行，不需要账号。**Graphify Cloud** 是同一家公司另外提供的托管服务（Free、Pro、Teams、Enterprise），跨仓库维护一张常驻更新的图，另加 PR 审查、形式化验证和 Sentry/Jira 连接器。README 大力推 Cloud，包括一个"token 少 80%"的数字；README 没有给这个数字附上方法说明。下文除非写明 Cloud，说的都是本地包。

## 快速判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Graphify Labs（graphify.com；README 上挂着 Y Combinator S26 徽章）。仓库建于 2026-04-03，之后搬进 2026-06-28 才建立的 `Graphify-Labs` 组织；旧的 `safishamsi/graphify` 路径会重定向 |
| 路线 | 运行时 & 工具——代码知识图谱 / agent 上下文层 |
| 开源 | 是（Apache-2.0）；PyPI 包 `graphifyy`，CLI 为 `graphify` |
| 实现 | Python 3.10+；代码用 tree-sitter，图用 NetworkX node-link JSON，社区划分用 Leiden（不可用时退回 NetworkX Louvain） |
| 核心思想 | 一张拿来遍历的图，而不是拿来检索的 embedding 索引：每条边都标着 `EXTRACTED`、`INFERRED`（带置信分）或 `AMBIGUOUS` |
| 输入 | 代码与配置（包括 SQL、Terraform/HCL、包清单与 MCP 清单）本地解析；Markdown、PDF、Office 文件、图片以及转写后的音视频经可选的语义那一遍加入 |
| 模型 | 代码部分不用。语义那一遍在走 skill 时用 assistant 自己的模型，headless 的 `graphify extract` 则用你配置的后端（Gemini、Kimi、Claude、OpenAI、DeepSeek、Azure OpenAI、Bedrock、Ollama，或 `claude` CLI） |
| 已接入的 agent | [Claude Code](claude-code.md)、[Codex](codex.md)、[Cursor](cursor.md)、[Gemini CLI](gemini-cli.md)、[GitHub Copilot](github-copilot.md) CLI 与 VS Code Copilot Chat、[OpenCode](opencode.md)、[Aider](aider.md)、[OpenClaw](openclaw.md)、[Hermes](hermes-agent.md)、[Kimi Code](kimi-code.md)、[Pi](pi.md)、[Devin](devin.md) CLI、Kiro、Amp、Kilo Code、Factory Droid、Trae、CodeBuddy、Google Antigravity，以及跨框架的 `.agents/skills` 位置 |
| 托管档 | Graphify Cloud：Free（$0，最多 3 个索引仓库）、Pro（$15/月，按年付折合 $10/月）、Teams（前 100 个团队优惠价 $29/席/月，标准价 $40，至少 2 席）、Enterprise（定制报价，自托管）。价格取自文档定价页，2026 年 10 月 8 日更新 |
| 最适合 | 希望 agent 先问一张全项目的图再去开文件、并希望这张图把文档和设计材料也一起覆盖进来的开发者 |
| 主要代价 | 图是一份快照，要靠 hooks、`watch` 或 `update` 保持最新；对非代码文件的语义那一遍要花模型 token；发版节奏很快（0.9.x，2026 年 10 月每周好几个版本） |
| GitHub 仓库 | https://github.com/Graphify-Labs/graphify |

## 它怎么工作

在 assistant 里跑 `/graphify .`，或在 shell 里跑 `graphify extract`，会往 `graphify-out/` 写三个文件：`graph.json`（完整的图）、`GRAPH_REPORT.md`（连接最多的"god node"、识别出的社区、建议提的问题）和 `graph.html`（可点击的力导向视图）。

构建分几条路。**代码**用 tree-sitter 在本地解析，不调 LLM，什么都不离开本机；纯代码的语料不需要 API key，混合仓库可以用 `--code-only` 或 `GRAPHIFY_BACKEND=none` 保持这种状态。**音视频**用 faster-whisper 在本地转写。**文档、PDF 和图片**走语义那一遍，用的是 skill 所在 assistant 正在跑的模型，或你配置的后端。各片段随后跨文件解析、合并成一张图，再聚成社区。文件按 SHA256 打指纹，重跑时只重新抽取变了的部分。

项目自己的几处页面对语言数量说法不一——README 说约 40 种，较早的 `docs/how-it-works.md` 说 25 种——所以请以 [Supported inputs](https://docs.graphify.com/concepts/supported-inputs) 页面为准，并留意它写着覆盖程度"因语法结构而异"。

查询是在保存好的图上用三个动词：`query`（针对一句大白话问题返回一张限定范围的子图，带 token 预算）、`path A B`（两个概念之间的最短路径）和 `explain`（一个节点及其连接）。一个名字匹配到多个节点时，它会拒绝作答并列出候选，而不是去猜。同一张图也由一个**本地 MCP server**（`graphify-mcp`，十个工具，如 `query_graph`、`get_neighbors`、`shortest_path`、`god_nodes`）对外提供，走 stdio，或者走 Streamable HTTP 并用 API key 做成共享端点。

要让 assistant 默认就用这张图，`graphify <platform> install` 会写入该平台自己的机制：在 Claude Code 和 Gemini CLI 上是搜索类工具之前的 hook（Claude Code 上读文件前也会触发），在其他平台上是指令文件（`AGENTS.md`、`.cursor/rules/` 等），在 Pi 上是一个原生扩展。另有一层可选的工作记忆，记录查询结果（`graphify save-result`，标为 `useful`、`dead_end` 或 `corrected`），`graphify reflect` 再把它们整理成一份 `LESSONS.md`，供之后的查询提示。

保持最新是你自己的事：`graphify hook install` 在提交和切分支后于后台重建，`graphify watch` 在文件变动时重建，文档要求在 pull 或 merge 之后手动跑 `graphify update .`。

## 和 CodeGraph、Graft（Trail Code）有什么不同

三者都用 tree-sitter 解析仓库，再把结果交给一个现成的编码 agent。差别在结果放在哪里、agent 怎么拿到。

- **[CodeGraph](codegraph.md)** 把索引存进本地 SQLite 数据库（带 FTS5），通过 MCP 提供；agent 要调工具才看得见。范围是源代码。
- **[Graft](graft.md)**（现名 Trail Code）把图写成 `graft/` 下互相链接的 markdown 文件，每个子系统一个节点、用 `[[wikilink]]` 相连，agent 用普通文件工具去读；MCP 是第二条路。`graft/` 被有意 gitignore，所以每个开发者各自重建一份。
- **Graphify** 写的是一份 `graph.json` 加一份报告和一个 HTML 视图，通过 skill 和 CLI 或它自己的 MCP server 查询。它的团队指南给了三种做法：用 pre-commit hook 加 union 合并驱动把 `graphify-out/graph.json` 提交进仓库、每个 clone 各自构建、或跑一个共享 MCP server。它的范围经可选的语义那一遍延伸到代码之外的文档、PDF、图片和媒体，每条边都带来源标签。它也能导出 markdown wiki（`--wiki`）和 Obsidian，但图的原生形态是 JSON，不是 agent 浏览的文件。

## 什么时候选它

- **你的 agent 把回合都花在认路上。** skill 和 hooks 会让 assistant 先跑 `graphify query`，再去 grep 或一个个开文件。
- **设计文档、ADR、规格书或论文就放在代码旁边。** Graphify 把它们映射进同一张图，并把 `# NOTE:` / `# WHY:` 注释和 ADR/RFC 引用连到它们所解释的代码上。
- **你想知道哪些是读出来的、哪些是推出来的。** 每条边都标着 `EXTRACTED`、带置信分的 `INFERRED` 或 `AMBIGUOUS`；文档也提醒，动态分派、生成代码和过期的扫描都会留下空洞。
- **你需要纯代码构建保持离线。** 代码解析不要 key、不联网；`GRAPHIFY_BACKEND=ollama` 能让语义那一遍也留在本地。
- **你同时用好几个 assistant。** 每个 assistant 一条 `graphify install --platform <name>`，还有项目级安装（`--project`），写出的文件可以提交。
- **你想要一张共享的图，但不想用托管服务。** 提交 `graph.json`，或在内网里用 HTTP 跑 `graphify-mcp`，两条路都有文档。

## 什么时候不要选

- **你的仓库很小。** 项目自己的 token 表显示，6 个文件的语料上几乎没有缩减；它所声称的价值随语料规模增长。
- **你希望这张图就是 agent 直接读的一组文件。** 那是 [Graft](graft.md) 的设计；Graphify 的图是查询接口后面的 JSON。
- **你想要别人跑出来的基准。** 公开的数字（LOCOMO recall@10 0.497、LongMemEval-S 76%、在六道题的 ERPNext 套件上 82.0% 的关键事实覆盖率）出自 Graphify 自己的 harness（文件标注"Last updated: 2026-07-05"，但 2026-10-05 又改过）。三个套件里有两个测的是对话记忆，不是代码导航。
- **你的数据不能到达模型供应商。** 文档、PDF 和图片会发给 assistant 的模型或配置的后端；自动检测按设了哪个 API key 来选供应商（会打印出是哪一个），README 也注明 Kimi 后端会路由到 Moonshot 在中国的服务器。请固定 `--backend`，或用 `GRAPHIFY_BACKEND=none`。
- **本地查询日志是个问题。** 没有遥测，但默认会把每次 `query`、`path`、`explain` 和 MCP `query_graph` 调用记到 `~/.cache/graphify-queries.log`（问题、语料、返回的节点、耗时）；设 `GRAPHIFY_QUERY_LOG_DISABLE=1` 可以关掉。
- **你要厂商中立的治理。** 一个账号有 1,217 次提交，第二名是 158 次，README 也反复把人引向付费的 Cloud 产品。

## 结论

Graphify 是一个本地、Apache-2.0 的上下文层：从项目里建出一张带来源标签的知识图谱，再通过 skill、hooks、CLI 和 MCP server 把它摆到编码 agent 面前。它和本地图已收录的两个代码图谱层的区别在于范围（文档、PDF 和媒体进同一张图）和存储（一份团队可以带合并驱动提交的 `graph.json`，而不是 SQLite 索引或一文件夹 markdown）。要把它放在这些背景下掂量：快速迭代的 0.9.x 版本线、自报的基准，以及一份同时也是托管产品导流入口的 README。路线层面的视角见[记忆方案](../comparisons/memory-approaches.md)。

## 来源

- [GitHub 仓库与 README](https://github.com/Graphify-Labs/graphify) · [Releases（v0.9.96，2026-10-26）](https://github.com/Graphify-Labs/graphify/releases) · [LICENSE（Apache-2.0）](https://github.com/Graphify-Labs/graphify/blob/v8/LICENSE) · [BENCHMARKS.md](https://github.com/Graphify-Labs/graphify/blob/v8/BENCHMARKS.md) · [docs/how-it-works.md](https://github.com/Graphify-Labs/graphify/blob/v8/docs/how-it-works.md)
- 文档：[How Graphify works](https://docs.graphify.com/concepts/architecture) · [Supported inputs](https://docs.graphify.com/concepts/supported-inputs) · [Connect the graph MCP server](https://docs.graphify.com/mcp/overview) · [MCP tool reference](https://docs.graphify.com/reference/mcp-tools) · [Serve a graph over HTTP](https://docs.graphify.com/mcp/shared-http) · [Keep the graph current](https://docs.graphify.com/guides/incremental-updates) · [Record useful findings](https://docs.graphify.com/guides/work-memory) · [Share context with your team](https://docs.graphify.com/guides/team-workflows) · [Plans and pricing](https://docs.graphify.com/pricing/overview)
