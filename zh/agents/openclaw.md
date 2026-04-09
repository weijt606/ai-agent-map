# OpenClaw

[![ZH](https://img.shields.io/badge/ZH-CURRENT-1f6feb?style=for-the-badge)](openclaw.md)
[![EN](https://img.shields.io/badge/EN-English-9ca3af?style=for-the-badge)](../../agents/openclaw.md)
[![Home](https://img.shields.io/badge/HOME-README-24292f?style=for-the-badge)](../README.md)

一句话：OpenClaw 更像一个本地优先的 agent runtime 和 control plane，不像单点 coding 工具那样轻。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | openclaw |
| 路线 | 自托管 runtime / gateway |
| 是否开源 | 是 |
| 最适合 | 消息渠道、设备、工具、长期运行型助手 |
| 主要代价 | 路由、安全、权限和运维决策很多 |
| 官方入口 | https://openclaw.ai |

## 什么时候选它

- 你需要把 agent 接到浏览器、设备节点、消息平台和定时任务。
- 你希望本地优先、自托管，并且保留很强的控制面。
- 你真正要搭的是运行层，而不是单个 coding assistant。

## 什么时候别选

- 你只要一个最小化 coding agent。
- 你希望完全托管、几乎零运维。
- 你只关心 issue-to-PR 执行，不关心渠道和 runtime。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Tool use | 很强 | 能力面很宽 |
| Code execution | 强 | 可接主机和容器环境 |
| Multi-agent routing | 强 | 适合做复杂路由 |
| Messaging / delivery | 很强 | 多渠道是重点优势 |
| Device integrations | 强 | 很适合把 agent 接进真实设备 |

## 使用代价

复杂度是 High。OpenClaw 的能力很大，但这不可能免费，它会要求你在安全、权限、路由和运维上做更多判断。

## 最后一句

如果你要的是“agent operating layer”，OpenClaw 很有意思；如果你只想写代码，它通常太重。