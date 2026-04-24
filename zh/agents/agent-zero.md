# Agent Zero

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](agent-zero.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/agent-zero.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Agent Zero 是一个通用自主 agent 框架，能动态创建自己的工具、执行代码、有机学习——没有预定义 pipeline。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Jan Tomasek / agent0ai |
| 路线 | 通用自主 agent 框架 |
| 是否开源 | 是 |
| 最适合 | 想要自构建、模型无关的自主 agent，能动态创建工具的开发者 |
| 主要代价 | 只能自托管，无企业支持，需要调优才能得到精确输出 |
| 官网 | https://www.agent-zero.ai |
| GitHub 仓库 | https://github.com/agent0ai/agent-zero |

## 什么时候选它

- 你想要一个在运行时自己写工具、自己执行的 agent，而不是跑固定 pipeline。
- 你需要模型灵活性——OpenAI、Anthropic、Groq、Ollama，通过 LiteLLM 接入。
- 你想要多 agent 协作，agent 能生成子 agent 分担任务。
- 你想要跨会话的持久记忆和自我纠正。

## 什么时候别选

- 你需要生产级企业支持和 SLA。
- 你想要零配置的托管 SaaS。
- 你的硬件资源有限——本地模型需要 8GB+ RAM。
- 你想要打磨和可预测性，而不是自主性和灵活性。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 动态工具创建 | 很强 | 核心设计——agent 在运行时创建自己的工具 |
| 自主执行 | 强 | 多步、自我纠正 |
| 多 agent | 强 | 生成子 agent 分担任务 |
| 持久记忆 | 强 | 跨会话记忆 |
| 模型无关 | 很强 | 通过 LiteLLM 支持任意 provider |
| 企业就绪 | 弱 | 无商业支持或 SLA |

## 使用代价

复杂度 Medium 到 High。用 Docker + Ollama 大约 10 分钟就能跑起来，但后续的模型选择和 prompt 调优靠你自己。成本来自 LLM API token 或 VPS 费用（4GB 实例约 $24/月）。

## 最后一句

Agent Zero 适合想要最大自主性的开发者——自构建工具、有机学习、无固定 pipeline。代价是：没有企业支持、没有托管选项，调优归你。
