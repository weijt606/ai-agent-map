# AutoGPT

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](autogpt.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/autogpt.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：AutoGPT 从最初刷屏的 GPT-4 自主实验，进化成了带可视化工作流构建器、市场和多模型支持的 agent 搭建平台。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Significant Gravitas Ltd. |
| 路线 | 自主 agent 平台，带可视化工作流构建器 |
| 是否开源 | 是，自定义 license（source-available） |
| 最适合 | 想通过可视化界面搭建和分享自主 agent，同时支持多种模型 |
| 主要代价 | 自主循环很烧 token；自托管需要 Docker 和基础设施管理 |
| 官网 | https://agpt.co |
| GitHub 仓库 | https://github.com/Significant-Gravitas/AutoGPT |

## 什么时候选它

- 你想用可视化拖拽构建器来设计自主 agent。
- 你需要多模型支持——OpenAI、Anthropic、Google、Meta、Mistral 等。
- 你想浏览和使用市场里的预建 agent 模板。
- 你想从 n8n、Make 或 Zapier 导入已有工作流。
- 你想要云平台和自托管两种部署选项。

## 什么时候别选

- 你需要确定性、可审计的执行，用于高风险或合规场景。
- 你想要一个打磨完善的成品产品。AutoGPT 很多方面仍处于 beta 阶段。
- 无人监管的自主 agent 循环让你不放心——长时间运行可能烧 token 并产生不可靠结果。
- 你需要 coding-first agent。看 Claude Code、Codex 或 Devin。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 可视化工作流构建器 | 强 | 拖拽式 action、logic、integration 模块 |
| 自主执行 | 强 | 多步自主任务执行，支持重试 |
| 多模型支持 | 很强 | 支持大部分主流 LLM provider |
| 市场 | 中 | 有 agent 和工作流模板 |
| 工作流导入 | 中 | 可从 n8n / Make / Zapier 导入 |
| 确定性 / 可靠性 | 弱 | 模糊任务容易循环和幻觉 |
| 编码专用 | 弱 | 通用型，不是 coding-first |

## 使用代价

复杂度 High。自托管需要 Docker、数据库配置和持续维护。平台本身免费，但 LLM API token 消耗很快——自主循环和重试会快速消耗预算。项目从 2023 年至今多次转型，API 和架构仍在稳定中。

## 最后一句

AutoGPT 是知名度最高的自主 agent 项目（182k stars），从 CLI 实验发展到可视化平台。代价是：野心很大、功能很广，但可靠性和打磨程度还在追赶中。
