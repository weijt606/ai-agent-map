# GenericAgent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](generic-agent.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/generic-agent.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：GenericAgent 是一个自演进自主 agent——从 3.3K 行种子代码起步，让它在每完成一个任务时自己长出 skill tree。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | lsdefine（复旦团队） |
| 路线 | 自演进型自主 agent |
| 开源 | 是（MIT，Python） |
| 适合谁 | 想要 agent 自己结晶出新 skill、而不是依赖预打包工具的研究者和操作者 |
| 主要代价 | "边用边长"意味着没有固定配置——agent 的实际行为会随使用方式漂移 |
| 官网 | https://github.com/lsdefine/GenericAgent |
| GitHub 仓库 | https://github.com/lsdefine/GenericAgent |

## 什么时候选它

- 想要一个能"从完成任务里学新 skill"的自主 agent，而不是预加载固定工具集的。
- 喜欢能完整读完的最小种子代码（~3,300 行）。
- 关心 token 效率——团队声称在"全系统控制"场景下比同类框架低 ~6x token 消耗。

## 什么时候不选它

- 想要稳定固定的工具表面；这里 skill tree 自己往下长是设计意图，不是副作用。
- 需要开箱即用的 UI、dashboard 或托管云端运行。
- 需要每个动作都要 audit / review；这个设计是偏向自主、而不是每步审批。

## 能力画像

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 系统级控制 | 强 | 九个原子工具覆盖浏览器、终端、文件系统、设备 |
| 自演进 | 强（定义特征） | 每完成一个任务，会把执行路径结晶成 skill tree 里的可复用 skill |
| Token 效率 | 强（项目声称） | 项目自测在等价场景下比同类低 ~6x token |
| 开箱即用功能 | 刻意做轻 | 不打包 teams、dashboard、托管运行 |
| 稳定性 | 演进中 | 2026 年 1 月项目，本 map 上观察 2 周后才纳入 |

## 使用代价

复杂度 Medium。种子代码本身小到能读完和魔改，但运行代价比较特殊：因为 agent 会自己长 skill，第二个月的行为很可能跟第一个月不一样。这是核心价值主张，不是 bug——但也意味着行为可预测性比固定工具集 agent 低。

## 底线

GenericAgent 填上 map 当前缺的一块：从小种子里自演进出来的自主 agent，而不是预加载的自主 agent。如果在研究这个模式，或者想要一份能完全掌控的小型代码库，GenericAgent 是当前最强候选。如果是主流生产用途，AutoGPT 或 Agent Zero 仍然更稳。
