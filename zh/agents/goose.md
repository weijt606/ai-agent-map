# Goose

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](goose.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/goose.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Goose 更像一个可扩展的本机 agent 环境，而不只是狭义的 coding assistant。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Agentic AI Foundation，前身为 Block 主导项目 |
| 路线 | 跨 desktop、CLI 和 API 的可扩展本地 agent |
| 是否开源 | 是 |
| 最适合 | 既需要代码能力，也需要 extensions、MCP 和共享 desktop / CLI 配置的本地 agent 工作流 |
| 主要代价 | provider 配置、扩展权限管理，以及它的产品边界不只在 coding 上 |
| 官网 | https://goose-docs.ai/ |
| GitHub 仓库 | https://github.com/aaif-goose/goose |

## 什么时候选它

- 你想要一个跨 desktop 和 CLI 的开源本地 agent。
- 你希望 extensions 和 MCP 的重要性不低于单纯写代码。
- 你想让同一个 agent 表面覆盖更宽的本机工作流，而不是只盯着 coding。

## 什么时候别选

- 你只需要一个很窄的 coding assistant。
- 你想要 fully managed、低运维的云端产品。
- 你希望项目边界比当前 Block 到 AAIF 的迁移状态更简单清楚。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Local execution | 强 | 本机运行是核心设定 |
| Desktop + CLI | 强 | 共享配置是实际优势 |
| Extensions / MCP | 很强 | 这是评估 Goose 的关键点 |
| Provider flexibility | 强 | 支持多种 provider 路径 |
| Pure coding focus | 中 | 它比 coding-only workflow 更宽 |

## 使用代价

复杂度是 Medium。Goose 起步不算难，但当你开始接入 provider、extensions 和更宽的本地能力后，运维味道会明显变重。

## 最后一句

如果你要的是一个开源、本地、可扩展，而且不想立刻跳进重型托管平台的 agent 环境，Goose 值得关注。
