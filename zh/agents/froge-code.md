# Froge Code

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](froge-code.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/froge-code.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：这个页面目前按 Automagik Forge 暂定映射，适合 review-first、多尝试、多 worktree 的 coding automation 流程。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 当前映射 | Automagik Forge |
| 路线 | review-first 自动化平台 |
| 是否开源 | 是 |
| 最适合 | 任务板、多次尝试、人工挑选结果 |
| 主要代价 | 名称仍待进一步确认，流程也更重 |
| 官方入口 | https://forge.automag.ik |

## 什么时候选它

- 你想把 coding automation 做成任务板式流程。
- 你想比较不同 provider 或 agent 在同一类任务上的表现。
- 你想把尝试结果隔离在 worktree 中，降低污染主工作区的风险。

## 什么时候别选

- 你只想要一个 agent 从 issue 一路跑到交付，不想管理任务板。
- 你不想碰 provider、attempt、review 这些额外操作概念。
- 你需要的是高度自定义的状态机式 orchestration。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Task orchestration | 强 | 任务板和尝试流程是主轴 |
| Code execution | 强 | worktree 隔离很适合对比输出 |
| Multi-provider control | 强 | 可以把不同执行者放在一起比较 |
| Human oversight | 很强 | 人工挑选结果是核心设计 |
| MCP | 强 | 适合接到更大的自动化工作流里 |

## 使用代价

复杂度是 Medium。它把控制权保留下来了，但也意味着你要维护任务结构、尝试策略和 review 节奏。

## 最后一句

它的价值在流程可见性，不在“单个 agent 有多神奇”。