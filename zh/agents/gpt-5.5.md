# GPT-5.5

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](gpt-5.5.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/gpt-5.5.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：GPT-5.5 是 OpenAI 2026 年春季的前沿 agentic 模型——为多步任务执行、工具调用和自我检查而设计——2026 年 7 月 9 日已被 GPT-5.6 接棒（见下方"发布后格局"）。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | OpenAI |
| 路线 | 驱动 Codex、ChatGPT 和 API 的前沿 agentic 模型（2026 年 7 月已由 GPT-5.6 接棒） |
| 是否开源 | 否 |
| 最适合 | 高自主度编码、科研、多步 agent 工作流、长上下文任务 |
| 主要代价 | API 价格是 GPT-5.4 的 2 倍，模型边界与 Codex 产品边界容易混淆 |
| 官网 | https://openai.com/index/introducing-gpt-5-5/ |
| API 文档 | https://developers.openai.com |

## 为什么要收录一个模型

本目录里大多数条目是产品或工具。GPT-5.5 是模型。收录原因：OpenAI 明确将它定位为"a new class of intelligence for real work and powering agents"，而且它的发布直接抬高了多个已有 agent 表面的能力上限——Codex、ChatGPT、GitHub Copilot，以及所有基于 API 搭 agent 的团队。

当一个模型的发布改变了基于它构建的所有 agent 的能力，它本身就进入了选型地图。

## 什么时候选它

- 你想通过 Codex 或 API 获得 OpenAI 当前最强的 agentic 编码能力。
- 你需要百万 token 上下文窗口来处理大型代码库或长流程研究任务。
- 你在意单任务消耗的 token 数——GPT-5.5 完成相同 Codex 任务所用 token 明显少于 GPT-5.4。
- 你在用 OpenAI API 搭自己的 agent，想要原生工具调用、自我检查和多步规划能力。
- 你的工作流已经跑在 ChatGPT、Codex 或 GitHub Copilot 上，想直接升级到最新模型。

## 什么时候别选

- 你需要开源或自托管模型。GPT-5.5 完全闭源。
- 你对成本敏感——输入 $5/M tokens，输出 $30/M tokens，是 GPT-5.4 的 2 倍。
- 你需要当前的前沿——2026 年春季之后双方都已迭代（GPT-5.6、Claude Fable 5、Opus 4.8），见下方"发布后格局"。
- 你要的是一个成品 agent 产品，不是一个模型。那请看 [Codex](codex.md)。
- 你需要完全本地执行，不想依赖云端。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Agentic coding | 很强 | Terminal-Bench 2.0 得分 82.7%，发布时公开 benchmark 最高 |
| Long context | 很强 | API 支持 1M token 上下文窗口 |
| Tool calling | 强 | 原生工具调用，覆盖代码执行、浏览、文件操作 |
| Self-checking | 强 | 交付结果前会验证自身输出 |
| Multi-step planning | 强 | 能够处理需要规划、工具使用和验证的多部分任务 |
| Token efficiency | 强 | 同等任务所用 token 比 GPT-5.4 更少 |
| SWE-Bench Pro | 中 | 58.6%——落后于 Claude Opus 4.7 的 64.3% |
| 开源 / 自托管 | 无 | 完全闭源，只能通过 API 和产品访问 |

## 在哪里运行

GPT-5.5 不是独立的 runtime，它通过以下表面提供：

- **ChatGPT** — Plus、Pro、Business、Enterprise 订阅
- **Codex** — OpenAI 的 agentic coding 产品，沙盒化云端执行
- **API** — Responses 和 Chat Completions API（正在逐步开放）
- **GitHub Copilot** — 在模型选择器中可选，支持 ask、edit、agent 模式

## 使用代价

复杂度 Medium 到 High。通过 ChatGPT 或 Codex 使用时体验直观，但用 API 搭 agent 的团队面临实打实的成本跃升：$5/$30 每百万 token（输入/输出），是 GPT-5.4 的整整 2 倍。OpenAI 的说法是单任务成本可能反降，因为 GPT-5.5 每个任务用的 token 更少——但团队应该拿自己的工作负载做 benchmark，而不是直接信这个结论。

## 和 Codex 的关系

本页讲的是 GPT-5.5 这个模型。[Codex](codex.md) 页面讲的是产品——云端执行环境、隔离模型和 review 工作流。GPT-5.5 驱动 Codex，但不等于 Codex。如果你在选 agent 产品，先看 Codex；如果你在选要接入自己 agent 系统的模型，看这一页。

## 发布后格局（截至 2026 年 7 月）

GPT-5.5 4 月发布后，前沿迭代得很快。三次发布改变了模型层的选型判断：

| 发布 | 日期 | 改变了什么 |
| --- | --- | --- |
| **Claude Opus 4.8**（Anthropic） | 2026-05-28 | 修复 Opus 4.7 的啰嗦与 tool-calling 问题；新增 Dynamic workflows（Claude Code 内数百个并行 subagent）；$5/$25 每百万 token |
| **[Claude Fable 5](claude-fable-5.md)**（Anthropic） | 2026-06-09 | 首个 Mythos 级模型——位于 Opus 之上的新等级；$10/$50 每百万 token，7 月 7 日起在 Claude 订阅内按额度计费 |
| **GPT-5.6**（OpenAI） | 2026-07-09 | 在 ChatGPT / Codex / API 全面接棒 GPT-5.5，分三档——Sol（$5/$30）、Terra（$2.5/$15）、Luna（$1/$6），另有 Ultra 多 agent 模式；Artificial Analysis 编码 agent 指数领先（Sol 80 vs Fable 5 77.2、GPT-5.5 76.4、Opus 4.8 72.5） |

务实的读法：GPT-5.6 Sol 与 GPT-5.5 同价且更强，新项目里 GPT-5.5 实际上已是过渡选择；2026 年 7 月真正的模型层决策是 GPT-5.6 档位选择 vs Fable 5 额度 vs 以 Opus 4.8 为可靠默认。

## 最后一句

GPT-5.5 是 OpenAI agent 生态的一次真实能力跃升——4 月发布时 agentic coding benchmark 最强、百万 token 上下文、更高 token 效率。截至 2026 年 7 月它已被同价的 GPT-5.6 接棒；本页保留在地图里，作为"2026 春季模型竞赛如何重塑 agent 选型"的参照点。
