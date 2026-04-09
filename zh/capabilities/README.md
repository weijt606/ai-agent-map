# Capabilities

[![ZH](https://img.shields.io/badge/ZH-CURRENT-1f6feb?style=for-the-badge)](README.md)
[![EN](https://img.shields.io/badge/EN-English-9ca3af?style=for-the-badge)](../../capabilities/README.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-24292f?style=for-the-badge)](../README.md)

这个目录不是功能清单，而是一个统一词汇表。

它的作用是让不同 agent 页面能说同一种语言，不然很容易出现“都支持，但其实强弱完全不同”的错觉。

## 当前重点维度

| 维度 | 这里真正关心什么 | 典型问题 |
| --- | --- | --- |
| Tool use | 能不能真的调用外部工具或 API | 它只是会聊天，还是能实际动手 |
| Code execution | 能不能在真实环境里跑命令、测试和脚本 | 它会说怎么改，还是会自己跑起来 |
| Memory | 能不能跨步骤、跨会话保留有用上下文 | 它每次都像第一次见你吗 |
| Orchestration | 能不能管理工作流，而不只是响应提示词 | 它会推进任务，还是只会回一段话 |
| Multi-agent | 会不会 delegation、subagents、并行协作 | 它是单工位，还是多工位 |
| Human approval | 有没有显式审批、暂停、review 节点 | 你能不能把关键动作拦下来 |
| Scheduling | 能不能按时间或事件触发后台运行 | 它能不能定时干活 |
| Delivery surfaces | 它在哪里和你交互 | 终端、编辑器、Web、Slack、Telegram 还是设备 |
| Deployment control | 你能控制多少运行边界 | 托管、自托管、本地优先还是纯框架 |

## 使用这些维度时的顺序

1. 先圈出必须有的能力。
2. 再判断这是“核心强项”还是“顺带支持”。
3. 最后看这项能力带来的代价，比如安全、运维、审批负担和密钥管理。