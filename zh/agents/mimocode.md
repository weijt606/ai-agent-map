# MiMoCode

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](mimocode.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/mimocode.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：MiMoCode 是小米官方的终端 coding agent——Claude Code 形态的循环，但核心放了一套持久的跨会话记忆系统，让 agent 跨多次运行始终保持对项目的深入理解，而不是每次重新学。

> **与 [CodeWhale](codewhale.md) 的区别：** CodeWhale 是第三方用 Rust 写的 TUI，*包装* DeepSeek + MiMo 模型。MiMoCode（`XiaomiMiMo/MiMo-Code`，2026-06-10 上线）是小米自家为 MiMo 系列出的第一方 CLI。画面里有同一个模型家族，但厂商和代码库都不同。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | 小米（MiMo 团队） |
| 路线 | 直接执行——终端 coding agent |
| 开源 | 是 |
| 实现 | TypeScript |
| 许可 | MIT |
| 模型 | MiMo Auto（限时免费、零配置通道）；小米 MiMo 平台；任意主流 LLM API |
| 适合谁 | 想要一个记忆优先、为单项目长程任务调优的 coding CLI 的开发者 |
| 主要代价 | 全新（上线才几天）——功能面和稳定性还在快速变动 |
| GitHub 仓库 | https://github.com/XiaomiMiMo/MiMo-Code |

## 什么时候选它

- 你想要把持久项目记忆做成内置而不是插件：MiMoCode 维护项目 `MEMORY.md`、自动会话 checkpoint、scratch 笔记和按任务进度，恢复时通过 SQLite FTS5 检索重新注入。
- 你想要零配置启动——内置的 **MiMo Auto** 通道限时免费、不需要 API key，如果你已经用 Claude Code，还能一步导入。
- 你的工作是长程会话，上下文重建（窗口满时从最新 checkpoint + 记忆重建上下文）比纯速度更重要。

## 什么时候不选

- 你需要久经考验的工具——它 2026-06-10 才上线，还非常早期，会快速变化。
- 你把厂商中立的可移植性当作头号卖点——MiMoCode 支持自定义 provider，但优先围绕 MiMo 栈搭建；[Pi](pi.md) 或 [Aider](aider.md) 是更中立的底座。
- 你需要云端委派、并行 agent 或脱机后台运行——那是 [Codex](codex.md) 或 [Devin](devin.md) 的领地。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 终端工作流 | 强 | TUI 原生；`build` / `plan` / `compose` 模式用 Tab 切换 |
| 跨会话记忆 | 非常强 | 项目记忆、checkpoint、笔记、任务进度——核心差异点 |
| 上下文管理 | 强 | 自动 checkpoint、上下文重建、预算化注入 |
| 多 provider 支持 | 中 | 默认 MiMo Auto + 小米平台；支持自定义 OpenAI 兼容 provider |
| 后台执行 | 不是目标 | 前台、单开发者循环 |

## 使用成本

复杂度：低。安装是一行脚本或 `npm install -g @mimo-ai/cli`，首次启动会带你走完配置；MiMo Auto 暂时把 API key 这一步完全省掉。真正的成本是成熟度：这是个上线才几天的项目，记忆系统、agent 模式和 provider 方案都还在动。

## 底线

MiMoCode 是终端 coding agent 领域里"记忆优先"的那个——小米官方为 MiMo 模型出的 CLI，设计成让 agent 跨会话带着项目理解，而不是每次冷启动。如果单代码库的长程工作是你的痛点，又能接受全新工具，值得一看；如果你需要稳定性或厂商中立，[Aider](aider.md) 或 [Pi](pi.md) 更稳。别把它和 [CodeWhale](codewhale.md)（第三方 DeepSeek + MiMo TUI）搞混；想要 Moonshot 官方的 Kimi CLI，看 [Kimi Code](kimi-code.md)。
