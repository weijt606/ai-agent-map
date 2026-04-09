# Claude Code

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](claude-code.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/claude-code.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：如果你想在终端和 IDE 里高频和 agent 协作写代码，Claude Code 通常是最顺手的起点之一。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Anthropic |
| 路线 | 本地和 IDE 优先的直接执行型 coding agent |
| 是否开源 | 否 |
| 最适合 | 高频本地 coding 协作 |
| 主要代价 | 权限、环境和操作节奏仍然要自己管 |
| 官方入口 | https://code.claude.com/docs/en/overview |

## 什么时候选它

- 你想在本地仓库里边聊边改、边跑命令边修问题。
- 你希望 instructions、MCP、subagents 能在一条工作流里配合使用。
- 你不想把整个开发流程搬到另一个平台上。

## 什么时候别选

- 你只想把任务扔给云端后台，自己回来收结果。
- 你需要完全开源、自托管的整套方案。
- 你不想自己管理权限、工具接入和本地环境。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Tool use | 强 | 读写代码、执行命令、接开发工具是核心体验 |
| Code execution | 强 | 终端 loop 是产品主轴之一 |
| MCP | 强 | 很适合把专用工具接进本地工作流 |
| Subagents | 强 | 适合做分工和上下文隔离 |
| Scheduling | 中 | 有后台和定时路径，但不是主要心智模型 |

## 使用代价

复杂度是 Medium。上手不算难，真正的门槛在于怎么写好项目指令、怎么限制权限、怎么把 MCP 和 subagents 用得不混乱。

## 最后一句

Claude Code 更像“长期可用的开发增强层”，不是一次性任务投递箱。