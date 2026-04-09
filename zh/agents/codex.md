# Codex

[![中文](https://img.shields.io/badge/中文-当前页面-1f6feb?style=flat-square)](codex.md)
[![English](https://img.shields.io/badge/English-Read%20in%20English-9ca3af?style=flat-square)](../../agents/codex.md)

一句话：如果你喜欢“把任务丢出去，在云端隔离环境里跑完，再回来 review”，Codex 很有代表性。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | OpenAI |
| 路线 | ChatGPT 内的云端软件工程 agent |
| 是否开源 | 否 |
| 最适合 | 异步任务、隔离环境、日志证据、并行委派 |
| 主要代价 | 仍偏云端 research preview，远程节奏不如本地 agent 即时 |
| 官方入口 | https://openai.com/index/introducing-codex/ |

## 什么时候选它

- 你有很多边界清晰的 coding task，想丢给 agent 并行跑。
- 你很看重测试输出、终端日志和可追踪执行证据。
- 你的团队本来就习惯 issue、PR、review 这种异步工作方式。
- 你接受主产品运行在 ChatGPT / 云端隔离环境里，而不是完全本地执行。

## 什么时候别选

- 你要的是持续、本地、对话式的结对编程体验。
- 你要求严格自托管或离线运行。
- 你真正需要的是带消息渠道和设备能力的 runtime 系统。
- 你想把开源的 Codex CLI 直接当成这个主产品本身来理解。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Isolated execution | 很强 | 每个任务独立运行是核心卖点 |
| Code execution | 强 | 能跑命令、测试、类型检查 |
| Review evidence | 强 | 很适合 review-first 团队 |
| Background delegation | 强 | 任务委派是第一心智模型 |
| GitHub / PR handoff | 强 | 适合把结果带回 review 流程 |
| Local companion surfaces | 中 | Codex CLI 相关，但不应把 CLI 的开源属性算到主产品上 |

## 使用代价

复杂度是 Medium。它帮你减轻本地运维负担，但也会把团队带进“远程委派 + 回来看结果”的异步节奏。当前更准确的理解方式是：主产品是闭源云端 agent，Codex CLI 是相关但独立的本地 companion surface。

## 最后一句

把 Codex 理解成 ChatGPT 里的云端 coding agent 会更准确；把 Codex CLI 视为配套本地入口，而不是主产品本体。