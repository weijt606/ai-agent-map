# GPT-5.5

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](gpt-5.5.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/gpt-5.5.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：GPT-5.5 是 OpenAI 的前沿 agentic 模型，从底层为多步任务执行、工具调用和自我检查而设计。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | OpenAI |
| 路线 | 驱动 Codex、ChatGPT 和 API 的前沿 agentic 模型 |
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
- 你最看重 tool-use 和 SWE-bench 成绩——Claude Opus 4.7 在 SWE-Bench Pro 上目前领先（64.3% vs 58.6%）。
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

## 最后一句

GPT-5.5 是 OpenAI agent 生态的真实能力跃升——发布时 agentic coding benchmark 最强、百万 token 上下文、更高 token 效率。代价也很清楚：它是目前最贵的 OpenAI 模型，完全闭源，而且在部分 tool-use benchmark 上落后于 Claude。它最大的影响是抬高了所有基于 OpenAI API 搭建的 agent 的能力天花板。
