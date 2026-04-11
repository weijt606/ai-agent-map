# oh-my-claudecode

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](oh-my-claudecode.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/oh-my-claudecode.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：oh-my-claudecode 更像 Claude Code 之上的工作流和 orchestration layer，而不是它的替代品。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Yeachan Heo 与贡献者社区 |
| 路线 | 面向 Claude Code 的工作流 / orchestration layer |
| 是否开源 | 是 |
| 最适合 | 想在 Claude Code 里加入 teams、可复用 skills、持久执行模式和跨 provider advisor flow |
| 主要代价 | 你仍然要以 Claude Code 为基础表面，而且这层工作流会比原生 Claude Code 更重 |
| 官网 | https://yeachan-heo.github.io/oh-my-claudecode-website |
| GitHub 仓库 | https://github.com/Yeachan-Heo/oh-my-claudecode |

## 什么时候选它

- 你已经在用 Claude Code，只是想把 orchestration 做得更强，而不是换掉底层 agent。
- 你想要 team workflow、可复用 skills、Ralph / Autopilot 这类持久模式，以及可选的多 provider 交叉判断。
- 你想给 Claude Code session 补上通知、可观测性，或者 OpenClaw 这类 gateway 集成。

## 什么时候别选

- 你根本不用 Claude Code，也不想把它当成基础表面。
- 你想要最轻量的本地 coding loop，不想加更多工作流概念。
- 你想要的是完全托管的云端产品，而不是本地插件和 runtime layer。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Multi-agent orchestration | 很强 | Team mode 是它最核心的产品故事 |
| Workflow reuse | 强 | skills 和引导式执行模式是重要差异化 |
| Provider advisory | 强 | 能把 Codex、Gemini 拉进来做侧向 advisor |
| Observability | 强 | HUD、日志和 callbacks 让运行态更可见 |
| Detached cloud execution | 中等 | 更像加强本地和 tmux 驱动流程，而不是取代托管云 agent |

## 使用代价

复杂度是 Medium。安装并不算离谱，真正的成本在于你是在 Claude Code 之上再叠一层工作流、配置和可选 provider 工具。命名边界也稍微有点乱：仓库名和命令叫 oh-my-claudecode，但 npm 包名仍然是 `oh-my-claude-sisyphus`。

## 最后一句

如果 Claude Code 已经是你的基础 agent，而你又想要更强的结构化执行、委派和复用模式，oh-my-claudecode 很值得排进 shortlist。