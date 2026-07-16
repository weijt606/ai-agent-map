# Cursor

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](cursor.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/cursor.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Cursor 适合把本地编码、后台委派和工作流集成都收进同一个 AI 编辑器表面的团队。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Cursor / Anysphere |
| 路线 | 同时覆盖本地编辑、CLI 和云端 agent 的 AI 编辑器 |
| 是否开源 | 否 |
| 最适合 | 想用一个编辑器串起编码、委派和 review 的团队 |
| 主要代价 | 产品边界很宽，而且官方 GitHub 仓库不应被误解成开源编辑器本体 |
| 官网 | https://cursor.com/docs |
| GitHub 仓库 | https://github.com/cursor/cursor |

## 什么时候选它

- 你想要一个以编辑器为中心、又能延伸到后台 agent 的统一工作流。
- 你看重 codebase indexing、rules、skills、MCP 和集成能力放在同一个入口里。
- 你希望编辑器、终端、web、mobile 和 GitHub 邻接流程尽量打通。

## 什么时候别选

- 你需要明确开源或可自托管路线。
- 你只想要一个很小、很单一的 coding tool，而不是宽表面的产品。
- 你不想让专用 AI 编辑器成为工作流核心。
- 你会因为看到官方 GitHub 仓库，就预期编辑器本体是开源的。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Editor workflow | 很强 | 编辑器仍然是中心 |
| Background agents | 强 | 云端 agent 和 web/mobile 表面都值得算进去 |
| Rules / skills / MCP | 强 | 适合做团队级定制 |
| Integrations | 强 | GitHub、Slack、Linear、JetBrains 等都在路线里 |
| Self-hosting | 弱 | 这不是选 Cursor 的原因 |

## 2026 年年中动态

整个夏天 agent 表面还在继续变宽：

- **2026 年 6 月**：Cursor 浏览器内的 Design Mode（点击、涂画或语音描述 UI 改动，交给 agent 执行）；**Cursor for iOS** 在全部付费计划公测——常驻 agent、Remote Control、实时通知、移动端 review；Teams 定价改版，新增 Premium 席位（3 倍价格换 5 倍用量）。
- **2026 年 7 月（v3.11，7 月 10 日）**：Agents Window 的云端 agent 升级——环境启动更快、可复用快照、/in-cloud subagent 隔离并行；side chats 和 agent 记录搜索；Bugbot review 快 3 倍以上且便宜 22%。

选型要点：Cursor 现在押注最重的是"随身携带的 agent"（移动端、云端、常驻）——编辑器只是若干表面之一。

## 使用代价

复杂度是 Medium。真正的代价不在安装，而在于你要决定多少工作流放进同一个 AI 编辑器里，以及愿意给它多大的 agent 自主性。

## 最后一句

更准确的理解方式是：Cursor 不是单纯 AI 编辑器，而是已经长成更宽 agent 产品的编辑器入口。如果你要一个打磨完整的日常编码加后台委派表面，它值得认真看。
