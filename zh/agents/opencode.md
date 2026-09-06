# OpenCode

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](opencode.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/opencode.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：OpenCode 是体量最大的厂商中立开源编码 agent——20.5 万 star，MIT——而本地图此前已经在五个 profile 里把它当作集成对象反复提到，却始终没给它写过一页。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Anomaly Co（社区项目） |
| 路线 | 直接执行 |
| 仓库 | [`anomalyco/opencode`](https://github.com/anomalyco/opencode)——MIT，TypeScript，**20.5 万 star** |
| 是否开源 | 是（MIT） |
| 最适合 | 想要一个不属于任何模型厂商的终端编码 agent |
| 主要代价 | 模型你自己选、自己付；没有厂商为自家权重去调这条循环 |
| 使用面 | 终端，另有**处于 beta 的桌面应用**（macOS / Windows / Linux） |
| 官网 | https://opencode.ai |

> **命名说明。** 仓库已从 `sst/opencode` 迁到 **`anomalyco/opencode`**；旧路径仍会重定向，Homebrew tap 与 Nix flake 都指向新组织。同一个项目、同一份 star 数、自 2025 年 4 月以来的同一段历史。

## 为什么要收录

因为它本来就已经在这儿了。[QM](qm.md) 把 OpenCode 列进它能跑的 harness，[Omnigent](omnigent.md) 为它提供适配，[Superpowers](superpowers.md) 有它的插件，[CodeGraph](codegraph.md) 有面向它的 MCP 集成，[Open Code Review](open-code-review.md) 也发了它的插件。五个 profile 把它当基础设施用，却没有一个能链接到解释"它是什么"的页面——直到这一页。

这值得点名为一种失效模式：一个项目可以在一张地图自己的正文里变成承重结构，却从未走过这张地图的收录流程。

## 什么时候选它

- **你要循环层面的厂商中立。** [Claude Code](claude-code.md)、[Codex](codex.md)、[Gemini CLI](gemini-cli.md)、[Kimi Code](kimi-code.md)、[Qwen Code](qwen-code.md) 都是第一方工具，默认设置跟着自家模型走。OpenCode 的动机不同，因为作者不卖模型。
- 你要的是**体量大、活跃开发**的开源 agent，而不是精简的那种——20.5 万 star 是现存最大的 agent 仓库之一，写这一页的当天它还在提交。
- 你希望**安装这件事别成为你的问题**：curl 脚本、npm、Homebrew、Scoop、Chocolatey、pacman/AUR、mise、Nix 都是一等支持。
- 你想在同一个项目里**要一个 GUI 选项**——桌面应用提供 `.dmg`、`.exe`、`.deb`、`.rpm`、`.AppImage`，但明确标着 beta。
- 你要在它之上做东西：上面那串集成说明生态已经默认它存在。

## 什么时候不选它

- **你想要某家厂商调好的默认值。** 如果你已经绑定某个模型家族，第一方 CLI 通常调得更好——见[终端编码 CLI 对比](../comparisons/coding-cli-agents.md)。
- 你想要一个能一口气读完、可审计的小循环——那是 [mini-swe-agent](mini-swe-agent.md)，OpenCode 在这条光谱的另一端。
- 你要今天就有稳定的桌面体验：它标着 beta。
- 你需要支持合同，或者一家能升级投诉的公司。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 模型自由度 | 很强 | 核心主张：没有哪家的模型享有特权 |
| 生态引力 | 很强 | harness、技能层、评审工具都把它当一等目标 |
| 安装与分发 | 很强 | 八种以上包管理器，外加桌面构建 |
| 交付面 | 强 | 终端优先；桌面应用 beta |
| 治理 | 中 | MIT 社区项目，近期换过组织 |
| 可审计性 | 中 | 开放，但很大——这不是能一口气读完的循环 |

## 和本地图其他条目的关系

在 [harness 路线](../comparisons/agent-harness-frameworks.md)上，OpenCode 通常是**被驱动**的那个而不是驱动者：[QM](qm.md) 和 [Omnigent](omnigent.md) 都把它和 Claude Code、Codex 并列着跑。这是关于它究竟是什么的最清楚的信号——一条可靠的、厂商中立的循环，别的层愿意架在它上面。

## 结论

如果你的要求是"一个不受任何模型厂商控制的正经编码 agent"，它已经是默认答案有一段时间了。它此前没进本地图是疏漏而不是判断——而五个 profile 早就依赖它，就是证据。
