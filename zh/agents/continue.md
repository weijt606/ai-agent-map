# Continue

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](continue.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/continue.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Continue 是一个开源 IDE 扩展，支持接入任意模型（云端或本地），在 VS Code 或 JetBrains 里实现补全、对话、编辑和 agentic 工作流。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Continue Dev, Inc. |
| 路线 | 开源编辑器中心 AI 助手 |
| 是否开源 | 是，Apache 2.0 |
| 最适合 | 想自选模型、想本地/私有部署、想在团队内统一 assistant 配置又不想被厂商绑定的团队 |
| 主要代价 | 模型配置自己负责——上手门槛比开箱即用产品更高 |
| 官网 | https://continue.dev |
| GitHub 仓库 | https://github.com/continuedev/continue |

## 什么时候选它

- 你想完全控制 coding assistant 用哪个模型——云端 API、本地 Ollama、自托管端点都行。
- 你在 VS Code 或 JetBrains 里工作，想要一个 GitHub Copilot 或 Cursor 的开源替代。
- 你的团队需要通过 Continue Hub 共享和分发统一的 assistant 配置。
- 你在意数据隐私，想让所有推理都在本地跑，不把代码发给第三方。
- 你想要基于源码控制规则的 AI PR 检查，作为 GitHub status check 运行。

## 什么时候别选

- 你想要零配置、开箱即用。Copilot 或 Cursor 更简单。
- 你想要一个独立的 AI 原生 IDE，而不是一个扩展。看 Cursor 或 Windsurf。
- 你想要最打磨的多文件编辑体验。Cursor 的专用编辑器更集成。
- 你需要终端优先或 CLI agent 工作流。看 Claude Code 或 Aider。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 自动补全 | 强 | Tab 补全，支持任意模型 |
| 对话 | 强 | 编辑器内 inline chat |
| 代码编辑 | 强 | inline 编辑和重构 |
| Agent 模式 | 中 | agentic 工作流可用，但成熟度不及 Cursor 或 Cline |
| 模型灵活性 | 很强 | 云端、本地、自托管——任意 provider |
| 团队配置 | 强 | Hub 和 Mission Control 统一分发 assistant 设置 |
| CI 集成 | 中 | 通过 markdown 规则做 PR 检查 |
| 独立 runtime | 无 | 纯扩展，依赖 VS Code 或 JetBrains |

## 使用代价

复杂度 Medium。工具本身免费，但模型层由你自己负责——选 provider、管 API key 或本地 GPU 资源、配置 assistant。有现成基础设施的团队会觉得很轻松；只想快速写代码的个人可能觉得配置成本不值得，不如直接买订阅产品。

## 最后一句

Continue 是模型层不想被锁定的团队的最强开源选择。代价很清楚：你拿到了完全控制权，但配置和模型成本也归你。
