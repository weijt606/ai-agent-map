# OpenHarness

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](openharness.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/openharness.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：OpenHarness 是 HKUDS 出的开源 agent harness——10 个子系统、43+ 工具、兼容 anthropics/skills，外加一个个人 agent 应用 ohmo——目标是做一个你自己能跑的、生产级且最透明的 harness。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | HKUDS（香港大学数据系统实验室） |
| 路线 | Agent harness 框架——可审计的生产级 runtime |
| 开源 | 是（MIT，Python） |
| 适合谁 | 想要一个完全开放、含权限/skills/多 agent 协调的 harness——不只是一个 loop |
| 主要代价 | 比 [mini-swe-agent](mini-swe-agent.md) 重一个数量级；价值取决于你是不是真的用到那些更宽的功能 |
| GitHub 仓库 | https://github.com/HKUDS/OpenHarness |

## 什么时候选它

- 你想要一个端到端可审计的 harness——10 个有名字的子系统（engine、tools、skills、plugins、permissions、hooks、commands、MCP、memory、coordinator）让内部结构清晰可读。
- 你想要 anthropics/skills 兼容 + MCP 客户端 + Claude 风格 plugin 系统在同一个项目里。
- 你需要开箱即用的多级权限（default、auto、plan mode）、路径规则和交互式审批。
- 你想用同一个 runtime 驱动 Claude、OpenAI、Copilot、Moonshot/Kimi、GLM、MiniMax、NVIDIA NIM，或者任意 OpenAI / Anthropic 兼容端点——以及 Ollama 本地模型。
- 你想在同一个 harness 之上叠一个个人 agent 表面（ohmo），接到飞书 / Slack / Telegram / Discord。

## 什么时候不选

- 你要 100 行就能审计完的 harness——那是 [mini-swe-agent](mini-swe-agent.md) 的立场。
- 你要厂商托管的成品。OpenHarness 是学术组开源，你自己跑。
- 你要给终端用户用的成品 UI——OpenHarness 是 CLI/TUI 优先，价值在 harness 本身而不是外观。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 子系统清晰度 | 非常强 | 10 个职责明确的命名子系统 |
| 工具表面 | 非常强 | 43+ 内置工具，覆盖文件 I/O、shell、搜索、网页、MCP |
| 权限模型 | 强 | 多级模式、路径规则、交互式审批 |
| Skills / plugins | 强 | anthropics/skills 兼容、Claude 风格 plugin 格式 |
| Provider 覆盖 | 强 | 所有主流云端 LLM + OpenAI/Anthropic 兼容端点 + Ollama |
| 多 agent 协调 | 中等 | Coordinator 子系统已经存在，生产级模式仍在成熟 |

## 使用成本

复杂度：中。`pip install openharness-ai` 安装很顺手；真正的成本是观念上的——你要自己决定激活哪些子系统、接哪几个 provider、怎么管理权限。harness 本身不强加意见，你来做决定。

## 底线

OpenHarness 卡在两个极端之间：比 [mini-swe-agent](mini-swe-agent.md)（故意限制在 100 行）重得多，又比 [Cursor](cursor.md)、[Claude Code](claude-code.md) 这类厂商成品轻。10 子系统架构、anthropics/skills 兼容、MCP 支持，让它成为本仓库收录的 harness 里最"基础设施形态"的那一个——如果你想研究一个生产级 agent runtime 怎么搭出来，或者要自己写一个，这是最干净的可 fork 起点。注意它和 [CLI-Anything](cli-anything.md) 是同一个 HKUDS 团队——两个项目处在同一条「让 agent 变得生产原生」的研究线上。
