# Agent Evaluation Framework

[![ZH](https://img.shields.io/badge/ZH-CURRENT-1f6feb?style=for-the-badge)](evaluation-framework.md)
[![EN](https://img.shields.io/badge/EN-English-9ca3af?style=for-the-badge)](../../agents/evaluation-framework.md)
[![Home](https://img.shields.io/badge/HOME-README-24292f?style=for-the-badge)](../README.md)

这个框架不是拿来给 agent 打总分的。

它只做一件事：让不同页面能被横向比较，而不是每个条目都写成完全不同的风格。

## 必填内容

| 字段 | 要回答什么 |
| --- | --- |
| `name` | 它到底叫什么，归谁所有 |
| `category` | 它更像执行器、自动化系统、多 agent 系统，还是平台 |
| `capabilities` | 它真正强的能力边界在哪里 |
| `best use cases` | 什么问题适合先看它 |
| `not suitable for` | 什么场景别先选它 |
| `complexity level` | 用起来到底轻不轻 |
| `real-world usage notes` | 实操里最容易踩的坑和最值得注意的成本 |

## 推荐补充内容

| 字段 | 用途 |
| --- | --- |
| `open_source` | 判断开源、闭源还是 mixed |
| `homepage` / `repo` | 指向官方入口 |
| `verification` | 说明是否存在命名或定位歧义 |
| `delivery model` | 说明它是本地、托管、自托管还是框架 |
| `last_reviewed` | 标明最近一次核验时间 |

## 分类定义

| 分类 | 这里怎么理解 |
| --- | --- |
| `execution` | 你把任务交给它，它直接做事 |
| `automation` | 它更像工作流、任务板、调度或审批系统 |
| `multi-agent` | 它会显式做 delegation、subagents 或并行协作 |
| `platform` | 它更像搭建、托管、路由或编排 agent 的底座 |

## 复杂度定义

| 级别 | 这里的意思 |
| --- | --- |
| `low` | 很快就能上手，额外运维和流程改造较少 |
| `medium` | 能开始用，但想用好还是需要权限、流程或环境管理 |
| `high` | 需要明显的系统设计、运维、安全或观测成本 |

## 写作规则

- 先写结果，再写架构。
- 一定要写“别在什么场景用它”。
- 不把“支持某能力”偷换成“在这个能力上最强”。
- 明确写出 operator 成本，比如审批负担、环境维护、密钥和安全边界。
- 如果公开资料不足，直接写“未完全核验”。

## 推荐页面结构

```md
# Agent Name

一句话定位。

## 一眼判断

## 什么时候选它

## 什么时候别选

## 能力侧写

## 使用代价

## 最后一句
```

## 这个框架刻意不做什么

- 不做统一总分。
- 不做空泛排行榜。
- 不把研究原型和生产工具混成一类。
- 不拿 star 数和热度代替适配度。