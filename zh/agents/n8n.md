# n8n

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](n8n.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/n8n.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：n8n 是一个工作流自动化平台，内置原生 AI agent 能力——400+ 集成、可视化构建器、可自托管。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | n8n GmbH |
| 路线 | 带 AI agent 节点的可视化工作流自动化 |
| 是否开源 | Fair-code（Sustainable Use License，源码可用，非 OSI 开源） |
| 最适合 | 想用可视化方式搭 AI agent 工作流，同时需要真实集成、触发器和自定义代码的团队 |
| 主要代价 | 自托管需要 DevOps 能力；云方案有执行次数限制；license 不是 MIT/Apache |
| 官网 | https://n8n.io |
| GitHub 仓库 | https://github.com/n8n-io/n8n |

## 什么时候选它

- 你想用可视化拖拽构建器搭 AI agent 工作流。
- 你需要 400+ 集成——Slack、Gmail、Notion、数据库、Webhook、API。
- 你想完全自托管，掌控数据。
- 你需要带 memory、工具、多 agent 编排和 LLM 评估的 AI agent——全部可视化配置。
- 你已经在用工作流自动化，想在上面加 AI agent 能力。

## 什么时候别选

- 你需要纯 OSI 开源 license。n8n 的 fair-code license 限制商业再分发。
- 你需要实时、亚秒延迟的管线。n8n 是事件驱动的，不是流处理。
- 你想要一个 coding-first agent。n8n 是工作流平台，不是 coding 助手。
- 你是非技术团队想要纯 no-code。n8n 更偏向开发者。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 可视化工作流构建器 | 很强 | 拖拽式，400+ 集成 |
| AI agent 节点 | 强 | 带 memory、工具、多 agent 编排的 Agent 节点 |
| 自托管 | 强 | Docker、Kubernetes 或裸机 |
| 集成 | 很强 | 400+ 预建连接器 |
| 自定义代码 | 强 | 可视化流程里嵌入 JavaScript 和 Python 节点 |
| LLM 支持 | 强 | OpenAI、Anthropic、Google、Ollama |
| 编码专用 | 无 | 不是 coding agent |

## 使用代价

复杂度 Medium。自托管免费且执行次数无限，但需要 Docker/Kubernetes 知识来做部署和维护。云方案从 $20 到 $800/月，按执行次数计费。真正的价值在于把 AI agent 能力和海量集成生态结合——纯 agent 框架做不到这一点。

## 最后一句

当你需要 AI agent 连接真实系统——发邮件、更新数据库、触发 Webhook、调 API——并且全部通过可视化构建器完成时，n8n 是正确选择。它不是 coding agent，它是让 agent 落地运行的工作流层。
