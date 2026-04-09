# LangGraph

[![中文](https://img.shields.io/badge/中文-当前页面-1f6feb?style=flat-square)](langgraph.md)
[![English](https://img.shields.io/badge/English-Read%20in%20English-9ca3af?style=flat-square)](../../agents/langgraph.md)

一句话：LangGraph 适合那些已经确定要自己搭长期运行、有状态、可恢复 agent workflow 的团队。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | LangChain |
| 路线 | 底层 orchestration 框架 |
| 是否开源 | 是 |
| 最适合 | 持久化、有状态、审批流、恢复能力 |
| 主要代价 | 设计和运维成本最高 |
| 官方入口 | https://docs.langchain.com/oss/python/langgraph/overview |

## 什么时候选它

- 你需要 checkpoint、state、approval、recovery 这类框架级能力。
- 你想把 agent 当成内部平台能力来建设。
- 你已经接受“这是平台工程，不是买工具”这个前提。

## 什么时候别选

- 你今天就想拿到一个现成 coding agent。
- 你没有工程资源去维护 prompts、tools、eval 和 observability。
- 你的任务其实简单到脚本或托管产品就能解决。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Durable execution | 强 | 核心价值之一 |
| Memory | 强 | 适合长期运行 workflow |
| Human-in-the-loop | 强 | 审批和中断很自然 |
| Multi-agent orchestration | 强 | 很适合复杂协作流程 |
| Ready-to-run UX | 弱 | 它不是成品 agent |

## 使用代价

复杂度是 High。它给你极高可控性，但代价就是你也要承担系统设计、测试和运行期可观测性。

## 最后一句

LangGraph 的价值在“让你搭出自己的 agent system”，不是“替你决定 agent 应该怎么工作”。