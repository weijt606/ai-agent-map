# Capabilities

中文：
这个目录定义跨 agent 的能力维度。它不是功能堆叠清单，而是帮助读者判断“这个 agent 的能力边界在哪里”的公共语言。

English:
This directory defines cross-agent capability dimensions. It is not a feature dump. It is the shared language used to describe where an agent's real capability boundary sits.

## 当前能力词汇表 | Current Capability Vocabulary

| Capability | Meaning in this repo |
| --- | --- |
| Tool use | Agent can call external tools or APIs such as shell, browser, Slack, or databases. |
| Code execution | Agent can run code, tests, or shell commands in a real environment. |
| Memory | Agent can preserve or retrieve useful context across steps or sessions. |
| Orchestration | Agent can coordinate a workflow, not just answer a prompt. |
| Multi-agent | Agent can delegate or parallelize work across subagents or role-based workers. |
| Human approval | Workflow supports explicit review, interrupt, or approval gates. |
| Scheduling | System can run work on a timer or event trigger. |
| Delivery surfaces | System can deliver results through CLI, web UI, messaging, or devices. |
| Deployment control | Team can choose managed, self-hosted, local-first, or framework-level ownership. |

## 怎么使用这些维度 | How To Use These Dimensions

- 先看哪些能力是“必须有”。 First identify which capabilities are mandatory.
- 再看这些能力是“核心能力”还是“附带支持”。 Then decide whether a capability is core or merely supported.
- 最后看代价，尤其是安全、运维和 review 责任。 Finally check the cost, especially security, ops, and review burden.