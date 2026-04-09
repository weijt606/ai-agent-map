---
name: "LangChain"
vendor: "LangChain"
category: "platform"
open_source: true
complexity: "medium"
verification: "verified-public-project"
last_reviewed: "2026-04-09"
description: "High-level framework for quickly building custom agents and autonomous applications on top of LangGraph."
description_zh: "用于快速构建自定义 agent 和 autonomous applications 的高层框架，底层建立在 LangGraph 之上。"
homepage: "https://docs.langchain.com/oss/python/langchain/overview"
repo: "https://github.com/langchain-ai/langchain"
---

# LangChain

中文：
LangChain 不应该被理解成“另一个现成 agent”。它更适合被看作自定义 agent 的高层装配层。相对 LangGraph，它牺牲一部分底层控制，换来更快的起步速度。

English:
LangChain should not be treated as another ready-made agent. It is better understood as a higher-level assembly layer for custom agents. Relative to LangGraph, it gives up some low-level control in exchange for a faster starting point.

## 基本信息 | Snapshot

| Field | Value |
| --- | --- |
| Name | LangChain |
| Vendor | LangChain |
| Category | platform |
| Open Source | Yes |
| Complexity | Medium |
| Delivery Model | Library / framework |
| Homepage | https://docs.langchain.com/oss/python/langchain/overview |
| Repo | https://github.com/langchain-ai/langchain |

## 能力画像 | Capability Profile

| Capability | Assessment | Notes |
| --- | --- | --- |
| Agent abstraction | Strong | Public docs emphasize a prebuilt agent architecture and quick custom agent creation. |
| Tool use | Strong | Tool-connected agents are a core concept and part of the quickstart flow. |
| Model integrations | Strong | LangChain positions itself as an easy way to connect across providers. |
| Speed to prototype | Strong | It is the recommended fast path when you want to build agents quickly. |
| Durable orchestration | Medium | LangChain agents are built on LangGraph, but the lower-level orchestration surface lives there. |
| Turnkey end-user UX | Low | It is a developer framework, not a finished end-user agent product. |

## 最适合的使用场景 | Best Use Cases

- 想快速搭一个自定义 agent 或 autonomous app。 Best for quickly building a custom agent or autonomous application.
- 需要模型集成、工具接入和较快原型验证。 Good when you need integrations, tools, and fast prototyping.
- 想先从高层 abstraction 开始，而不是一开始就直接操心 state machine。 Useful when you want to start high-level instead of designing orchestration from scratch.

## 不适合的场景 | Not Suitable For

- 你其实想要的是现成可用的终端 / IDE / 云端 agent。 Not a fit if you want a ready-to-run terminal, IDE, or cloud agent.
- 你需要非常细的状态控制、checkpoint 和 recovery 语义。 Weak fit when you need lower-level state and recovery control; that is where LangGraph is stronger.
- 你只是要一个简单脚本，不需要引入整套 agent 框架。 Overkill for simple scripts.

## 复杂度判断 | Complexity

中文：
复杂度为 Medium。比 LangGraph 轻，但它仍然是框架，不是产品。真正复杂的地方在于你要自己决定 agent 的工具、prompt、eval 和部署边界。

English:
Complexity is Medium. It is lighter than LangGraph, but it is still a framework rather than a product. The real complexity is that you still own tools, prompts, evals, and deployment boundaries.

## 实战备注 | Real-World Usage Notes

- 如果团队需要尽快试出一个 agent 方向，LangChain 通常比直接上 LangGraph 更快。 If the team needs to test an agent direction quickly, LangChain is usually faster than starting directly with LangGraph.
- 一旦 workflow 复杂度继续上升，很多团队最终还是会往 LangGraph 下沉。 As workflow complexity rises, many teams eventually move down into LangGraph.
- 它适合“快速组装”，不适合被误解为“可直接购买的 agent 产品”。 It is good for fast assembly, not to be confused with a purchasable agent product.