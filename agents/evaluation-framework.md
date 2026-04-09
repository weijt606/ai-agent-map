# Agent Evaluation Framework

中文：
这个框架不追求给 agent 打一个总分，而是帮助读者回答一个更实用的问题：这个 agent 适不适合我的任务和我的团队。

English:
This framework is not designed to produce a single score. Its purpose is to help a reader answer a more useful question: does this agent fit my task and operating model?

## 必填字段 | Required Fields

| Field | What to record | Why it matters |
| --- | --- | --- |
| `name` | Canonical project name and vendor or owner | Avoid alias confusion |
| `category` | `execution`, `automation`, `multi-agent`, or `platform` | Helps readers narrow quickly |
| `capabilities` | Concrete capability surface such as tool use, execution, memory, scheduling, orchestration | Keeps the profile practical |
| `best use cases` | Problems this agent is genuinely good at | Turns description into guidance |
| `not suitable for` | Scenarios where the agent is a poor fit | Prevents bad adoption decisions |
| `complexity level` | `low`, `medium`, or `high` with a short explanation | Sets setup and ops expectations |
| `real-world usage notes` | Practical observations, caveats, trust boundaries, or operator requirements | Makes the profile usable for production decisions |

## 推荐字段 | Recommended Fields

| Field | What to record |
| --- | --- |
| `open_source` | Whether the system is open-source, closed-source, or mixed |
| `homepage` / `repo` | Official entry points |
| `verification` | Whether the profile is fully verified or has naming / positioning ambiguity |
| `delivery model` | Managed SaaS, self-hosted runtime, library, local-first app, and so on |
| `last_reviewed` | When the profile was last updated |

## 分类定义 | Category Definitions

| Category | Meaning |
| --- | --- |
| `execution` | A direct worker agent that takes a task and executes it with tools. |
| `automation` | A system centered on repeatable workflows, task queues, scheduling, approval steps, or task orchestration. |
| `multi-agent` | A system that explicitly delegates, coordinates, or parallelizes work across subagents. |
| `platform` | Infrastructure or framework used to build, host, route, or operate agents. |

## 复杂度定义 | Complexity Definitions

| Level | Meaning |
| --- | --- |
| `low` | A small team or individual can get value quickly with limited setup and few moving parts. |
| `medium` | Setup is reasonable, but successful use still requires workflow changes, permissions, or operational discipline. |
| `high` | The system needs significant orchestration design, infra ownership, security work, or observability to run well. |

## 写作规则 | Authoring Rules

- 优先写任务结果，不优先写架构术语。 Write task outcomes before architecture details.
- 必须说明边界条件。 Every profile must state the boundary conditions.
- 不要把“支持某能力”写成“擅长某能力”。 Do not confuse support for a feature with real strength in that area.
- 尽量写出 operator 视角的成本。 Capture the operator cost: setup, review burden, trust model, and maintenance.
- 如果公开信息不足，明确说明，不要补全想象中的细节。 If public information is incomplete, say so instead of inventing detail.

## 建议的 Front Matter | Suggested Front Matter

```yaml
---
name: "Agent Name"
vendor: "Vendor or owner"
category: "execution"
open_source: true
complexity: "medium"
verification: "verified-public-project"
last_reviewed: "2026-04-09"
description: "One-sentence English summary."
description_zh: "一句中文概述。"
homepage: "https://example.com"
repo: "https://github.com/example/repo"
---
```

## 建议的页面结构 | Suggested Page Structure

```md
# Agent Name

简短定位。 Short positioning.

## 基本信息 | Snapshot

## 能力画像 | Capability Profile

## 最适合的使用场景 | Best Use Cases

## 不适合的场景 | Not Suitable For

## 复杂度判断 | Complexity

## 实战备注 | Real-World Usage Notes
```

## 这个框架刻意不做什么 | What This Framework Deliberately Avoids

- 不做统一分数。 No single total score.
- 不做“谁更强”的空泛排行。 No vague strength ranking.
- 不把研究原型和生产工具当成同一类对象。 No false equivalence between research prototypes and production tools.
- 不以 star、融资、热度代替适配度。 No popularity-based evaluation.