# ml-intern

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](ml-intern.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/ml-intern.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：ml-intern 是一个"ML 工程师"自主 agent——丢任务给它，它会读论文、写代码、并把 ML 成果走完整流程发布到 Hugging Face。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | Hugging Face |
| 路线 | 垂直领域自主 agent（ML 工程） |
| 开源 | 是（Apache-2.0，Python） |
| 适合谁 | 想让 agent 把"我读到一篇论文"推到"Hub 上的 model card"全流程，并深度用 HF 工具链 |
| 主要代价 | 长循环 agentic loop 的 LLM API 开销，加上对产出做 review 的纪律 |
| 官方网址 | https://smolagents-ml-intern.hf.space（Web 前端） |
| GitHub 仓库 | https://github.com/huggingface/ml-intern |

## 什么时候选它

- 想要一个面向 ML 研究和工程的专用自主 agent，而不是通用 coding agent。
- 已经在 Hugging Face 生态里，想原生访问 repos、datasets、models 和 papers。
- 能接受长 agentic loop（最多 ~300 轮迭代）以及对应的 token 预算。

## 什么时候不选它

- 想要通用自主 agent——ml-intern 是 ML workflow 取向。
- 需要每一步严格审批；ml-intern 是为放手迭代设计的，敏感操作才弹审批。
- 不用 Hugging Face Hub；它的价值很大程度上绑在 HF 生态。

## 能力画像

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 自主循环 | 强 | 最多 300 轮 plan → 工具 → 结果 → 再 plan |
| HF Hub 集成 | 很强 | 原生访问 repos、datasets、models、papers |
| 代码执行 | 强 | 沙盒里跑代码做测试 |
| 模型 provider 覆盖 | 强 | Anthropic、OpenAI、本地端点、MCP 服务器 |
| 通用任务能力 | 有限 | 整个框架取向就是 ML 工程 |

## 使用代价

复杂度 Medium-High。安装本身简单（`uv sync`），但运行成本会叠加：长 loop 烧 token 很快，会话自动上传到私有 HF dataset（既是 feature 也是成本），有意义的产出仍需要人工 review。API 预算要算清楚。

## 底线

ml-intern 填上了自主 agent 版图里的一块空缺：大多数自主 agent（AutoGPT、Agent Zero）是通用的，而 ml-intern 是 ML 工程取向，深入 Hugging Face 技术栈。如果你的问题就是 ML 任务（从论文到上线一条龙），它是当前最强候选；如果不是，选通用自主 agent 或 coding agent 会更合适。
