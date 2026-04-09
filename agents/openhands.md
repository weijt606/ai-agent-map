---
name: "OpenHands"
vendor: "OpenHands"
category: "execution"
open_source: true
complexity: "medium"
verification: "verified-public-project"
last_reviewed: "2026-04-09"
description: "Open-source AI-driven development agent with CLI, local GUI, cloud, enterprise, and SDK surfaces."
description_zh: "开源 AI-driven development agent，提供 CLI、本地 GUI、云端、企业和 SDK 多种表面。"
homepage: "https://github.com/OpenHands/OpenHands"
repo: "https://github.com/OpenHands/OpenHands"
---

# OpenHands

中文：
OpenHands 是目前最值得关注的开源软件工程 agent 项目之一。它不是只给你一个 CLI，也不是只给你一个 demo UI，而是把 CLI、local GUI、cloud、enterprise 和 SDK 都铺出来了。

English:
OpenHands is one of the most important open-source software engineering agent projects to track. It is not just a CLI or a demo UI; it spans CLI, local GUI, cloud, enterprise, and SDK surfaces.

## 基本信息 | Snapshot

| Field | Value |
| --- | --- |
| Name | OpenHands |
| Vendor | OpenHands |
| Category | execution |
| Open Source | Yes |
| Complexity | Medium |
| Delivery Model | CLI, local GUI, cloud, enterprise, and SDK |
| Homepage | https://github.com/OpenHands/OpenHands |
| Repo | https://github.com/OpenHands/OpenHands |

## 能力画像 | Capability Profile

| Capability | Assessment | Notes |
| --- | --- | --- |
| Self-hosting | Strong | Public docs document local setup, Docker-based flows, and enterprise deployment. |
| CLI workflow | Strong | The CLI supports interactive tasks, approvals, resume, and headless automation paths. |
| GUI workflow | Strong | Local GUI gives a laptop-hosted app surface with optional repo mounting. |
| Cloud deployment | Strong | Public materials document cloud and enterprise offerings alongside OSS paths. |
| MCP / extensibility | Medium | MCP support is documented in CLI flows and broader product surfaces. |
| Ops burden | Medium | Self-hosting typically involves Docker, model configuration, and runtime setup. |

## 最适合的使用场景 | Best Use Cases

- 想用开源方式获得较完整的软件工程 agent。 Best for teams that want a more complete open-source software engineering agent.
- 既想 CLI，也想 GUI，还希望保留未来迁移到 cloud 或 enterprise 的路径。 Good when you want CLI and GUI today with room to evolve toward cloud or enterprise.
- 希望在自托管和托管之间保留选择权。 Useful when you want flexibility between self-hosted and hosted operating models.

## 不适合的场景 | Not Suitable For

- 需要极低运维、极轻安装成本。 Not ideal if you need very low setup and ops burden.
- 只想要编辑器里的轻量 agent，而不想引入 Docker 和额外 runtime。 Weak fit if you want a lightweight editor-only agent.
- 只需要 orchestration framework，而不是现成软件工程 agent。 Overkill if you only need an orchestration framework.

## 复杂度判断 | Complexity

中文：
复杂度为 Medium。因为它是开源可运行系统，所以价值很高；也因为它是真系统，部署和环境成本不会低到像浏览器 SaaS 那样轻。

English:
Complexity is Medium. It is valuable precisely because it is a real open-source runnable system, and that also means deployment and environment cost will not be as light as a pure SaaS experience.

## 实战备注 | Real-World Usage Notes

- OpenHands 很适合用来评估“开源 agent 能否替代闭源 coding agent 的部分能力”。 OpenHands is useful for evaluating how far open-source software engineering agents can substitute for closed-source offerings.
- Docker、模型 API key、搜索配置等准备项会直接影响首次体验。 Docker, model API keys, and search configuration directly affect the first-run experience.
- 如果你重视可迁移性和开放度，它是高优先级候选。 If openness and deployment flexibility matter, it is a high-priority candidate.