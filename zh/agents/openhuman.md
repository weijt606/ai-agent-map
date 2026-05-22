# OpenHuman

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](openhuman.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/openhuman.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：OpenHuman 是一个围绕个人数据集成搭出来的开源桌面 agent——它把 Gmail、Notion、GitHub、Slack 等 118+ 工具自动同步到本地 Memory Tree，让助手每次开机不必从零认识你。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | tinyhumansai（Senami Ekakel） |
| 路线 | 自托管 / 本地 runtime——生活集成变体 |
| 开源 | 是（GPL-3.0，Rust + TypeScript on Tauri） |
| 适合谁 | 想要一个本地控制、隐私优先、已经懂你工作上下文的个人助手 |
| 主要代价 | 接受 GPL-3.0（比 MIT 更严格），以及一套强意见的数据拉取架构 |
| GitHub 仓库 | https://github.com/tinyhumansai/openhuman |

## 什么时候选它

- 你要一个已经知道你的 Gmail、Notion、GitHub、日历和文件的桌面 agent，而不是每次会话都要手动喂上下文。
- 你在意隐私：数据留在本机，配合 Ollama 还能整条链路本地化跑。
- 你想要 Memory Tree（SQLite 里的分层摘要）加上 Obsidian 兼容 wiki——agent 关于你的知识库是透明、可浏览、可编辑的。
- 你想要 LLM 成本压缩：自带的 "TokenJuice" 层据称在请求送进模型之前就能砍掉 80% 的 token 消耗。

## 什么时候不选

- 你要的是"以编码为中心"的 agent——OpenHuman 是个人生活/工作助手，不是 [Claude Code](claude-code.md)、[Aider](aider.md) 这类的对手。
- 你需要更宽松的许可证（MIT/Apache）。GPL-3.0 会挡掉一些商业集成路径。
- 你要托管或云服务。OpenHuman 是 Tauri 桌面优先，不是 SaaS 表面。
- 你只接 1-2 个集成——它的价值随你连入的 118+ 连接器数量放大。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 个人数据集成 | 非常强 | 118+ 第三方连接器，每 20 分钟自动拉一次 |
| 持久记忆 | 强 | SQLite 里的 Memory Tree + Obsidian 兼容 wiki，都可编辑 |
| 多 LLM 路由 | 强 | 多家云厂商 + Ollama 本地运行全链路 |
| 语音 / 原生工具 | 中等 | 内置 STT/TTS、文件系统、git、网页搜索 |
| 编码为中心工作流 | 不是目标 | 编码型 agent（[Claude Code](claude-code.md)、[Aider](aider.md)、[Pi](pi.md)）覆盖那一块 |

## 使用成本

复杂度：中。桌面安装简单，但真正的价值依赖你接入工具、让自动同步循环跑几周才能积累出有意义的 Memory Tree。你还要接受 GPL-3.0 进入你的环境——在商业产品里采用前先看清许可证。

## 底线

OpenHuman 是"personal AI super intelligence"作为开源项目实际跑出来的样子：一个桌面 daemon，自动从 118+ 工具拉数据、把内容压成本地 Memory Tree、在云端或本地 LLM 之间路由。2026 年 5 月连续两周强增长之后，它的定位不再模糊——是"自托管 / 本地 runtime"这条路线的生活集成变体，和编码型 agent 不同，也跟 [Hermes Agent](hermes-agent.md)、[Mercury Agent](mercury-agent.md) 这类多通道 runtime 走的方向不一样。
