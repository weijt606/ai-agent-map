# LangChain

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](langchain.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/langchain.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：LangChain 不是现成 agent，更像一个让你快速装出自定义 agent 的高层装配层。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | LangChain |
| 路线 | 高层 agent 框架 |
| 是否开源 | 是 |
| 最适合 | 快速做自定义 agent 原型 |
| 主要代价 | 复杂 workflow 往往还是要下沉到更底层 |
| 官网 | https://docs.langchain.com/oss/python/langchain/overview |
| GitHub 仓库 | https://github.com/langchain-ai/langchain |

## 什么时候选它

- 你想快速搭一个自定义 agent 或 autonomous app。
- 你要的是高层 abstraction，不想一开始就自己设计状态机。
- 你想快速验证方向，而不是先做厚重的平台建设。

## 什么时候别选

- 你其实想买一个现成可用的 coding agent。
- 你需要很细的 checkpoint、recovery 和长期状态控制。
- 你只是写个简单脚本，不需要整套 agent 框架。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Agent abstraction | 强 | 起步速度快 |
| Tool use | 强 | 很适合做工具接入 |
| Model integrations | 强 | 跨 provider 连接很方便 |
| Speed to prototype | 强 | 它最实用的优点之一 |
| Durable orchestration | 中 | 真正更细的控制还是在 LangGraph |

## 使用代价

复杂度是 Medium。它比 LangGraph 轻，但仍然是框架。真正的成本是你仍要自己定义工具、prompt、eval 和部署边界。

## 最后一句

如果你的目标是“先把自定义 agent 搭起来”，LangChain 比直接上更底层框架更顺手。