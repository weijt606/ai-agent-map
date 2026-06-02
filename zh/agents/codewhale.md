# CodeWhale

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](codewhale.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/codewhale.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：CodeWhale（原 DeepSeek-TUI）是一个用 Rust 写的终端 coding agent，围绕 DeepSeek 和 MiMo 模型生态搭建——形态和 Claude Code 或 Codex CLI 一样，但把低成本的国产推理模型当一等公民，而不是 fallback provider。

> **更名（2026 年 5 月底）：** 项目从 `Hmbown/DeepSeek-TUI` 改名为 [`Hmbown/CodeWhale`](https://github.com/Hmbown/CodeWhale)，并从只支持 DeepSeek 扩展到 **DeepSeek + MiMo**（小米开源模型），同时上线了产品官网 [codewhale.net](https://codewhale.net/)。旧的 `DeepSeek-TUI` 链接会自动重定向。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | Hmbown（开源社区） |
| 路线 | 直接执行——终端 coding agent |
| 开源 | 是 |
| 实现 | Rust |
| 模型 | DeepSeek + MiMo（小米） |
| 适合谁 | 想要 Claude Code 风格的循环、但跑在 DeepSeek / MiMo 性价比曲线上的开发者 |
| 主要代价 | 设计上绑定较窄的模型集——如果这些模型路线图卡住，agent 也跟着卡 |
| GitHub 仓库 | https://github.com/Hmbown/CodeWhale |

## 什么时候选它

- 你想专门针对 DeepSeek 或 MiMo 模型跑一个终端 coding agent（成本、能力、地区可用性），而不是经过通用 harness。
- 你倾向于极简终端表面，而不是桌面或 IDE 体验。
- 你想要 Claude Code 和 Aider 带火的"单进程、单开发者"循环，但锚定在低成本国产推理模型上。

## 什么时候不选

- 你需要广泛的 provider 可移植性——[Pi](pi.md) 或 [Aider](aider.md) 这类通用 harness 是更稳的底座。
- 你想要打磨过的托管产品；这个仍是社区项目，表面积故意做窄。
- 你需要云端委派、并行 agent 或后台运行——那是 [Codex](codex.md) 或 [Devin](devin.md) 的领地。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 终端工作流 | 强 | TUI 原生，单进程循环 |
| DeepSeek / MiMo 调优 | 非常强 | 针对这些模型的工具使用和推理模式做了适配 |
| 多 provider 支持 | 弱 | 目标就是 DeepSeek + MiMo 栈，广泛可移植性不是目标 |
| 后台执行 | 不是目标 | 前台、单开发者循环 |

## 使用成本

复杂度：低-中。安装很简单；真正的成本是绑定较窄的模型集。如果 DeepSeek 或 MiMo 在你所在区域的价格或可用性变化，会直接影响 agent。

## 底线

CodeWhale 是当初以 DeepSeek-TUI 之名首次出现在本仓库热门快照里的那个国产模型原生终端 coding agent。它不打算做通用 harness——就是把 Claude Code 形态的循环重新围绕低成本国产模型搭一遍。如果你选型的一部分动因是成本或访问 DeepSeek / MiMo 推理模型，这是最直接的"Claude Code 风格 + 国产栈"路径。如果可移植性比性价比更重要，[Pi](pi.md) 或 [Aider](aider.md) 是更好的底座。
