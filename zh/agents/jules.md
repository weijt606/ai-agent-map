# Jules

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](jules.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/jules.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Jules 适合希望把编码任务交给 Google 托管云端 agent、通过 GitHub 回收结果、同时保留 CLI 和 API 入口的团队。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Google |
| 路线 | 覆盖 web、CLI 和 API 的托管云端 coding agent |
| 是否开源 | 否 |
| 最适合 | 依赖 GitHub 连接、偏异步委派、希望 agent 产出 PR 的团队 |
| 主要代价 | 它是 cloud-first、GitHub-bound，而且部分表面仍在 alpha 或快速演进中 |
| 官网 | https://jules.google/ |

## 什么时候选它

- 你想把仓库放进云端 VM 里跑，再把 PR-ready 结果带回来。
- 你希望 web、CLI/TUI 和 API 同时存在于一个 Google 托管产品里。
- 你可以接受 GitHub 是核心仓库集成点。

## 什么时候别选

- 你需要自托管、离线运行或本地编辑器优先的执行方式。
- 你现在就要求长期稳定、成熟的 API 边界。
- 你不希望工作流建立在 GitHub app 式连接仓库的模式上。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| GitHub integration | 很强 | 这是 operating model 的核心 |
| Cloud VM execution | 强 | 托管执行环境是主路径 |
| Plan approval | 强 | 是很有意义的控制点 |
| CLI / TUI | 中 | 有价值，但不是主表面 |
| API automation | 中 | 有潜力，但目前仍是 alpha |

## 使用代价

复杂度是 Medium。Jules 减少了本地环境负担，但也会把团队带进 GitHub 中心、云端优先、产品边界仍在变化的工作流。

## 最后一句

如果你想看 Google 对“托管式异步 coding delegation”这条路线的答案，而且能接受 GitHub 连接加云端执行是默认模式，Jules 值得关注。
