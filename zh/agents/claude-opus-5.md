# Claude Opus 5

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](claude-opus-5.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/claude-opus-5.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Claude Opus 5 是大多数 Claude 系 agent 真正在跑的那个模型——价格还是 Opus 档的 $5/$25（和 Opus 4.8 一样），能力却被推到接近 Fable 5，于是"上不上天花板"重新变成一个要专门决定的花销，而不是默认选项。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Anthropic |
| 路线 | 前沿 agentic 模型——Opus 档，Mythos 天花板之下真正的默认 |
| 是否开源 | 否 |
| 最适合 | 长跑 agent、1M 上下文的整仓工作、多 agent 协同、文档与表格类任务 |
| 主要代价 | $5 / $25 每百万 token（与 Opus 4.8 持平）；Fast 模式 $10 / $50 |
| API 模型 id | `claude-opus-5` |
| 官方公告 | https://www.anthropic.com/news/claude-opus-5 |

## 为什么要收录

这条路线原本只有天花板（[Claude Fable 5](claude-fable-5.md)）和一个参照点（[GPT-5.5](gpt-5.5.md)），唯独缺了"你实际会把 agent 接到哪个模型上"——而自 **2026-07-24** 起，那个模型就是 Opus 5：Claude Max 上的默认模型，Claude Pro 上能用到的最强模型。

这个缺口有实际后果。Anthropic 侧真正的选型问题从来不是"前沿是不是更强"（是），而是"你的活里有多少真的需要前沿"。Opus 5 就是回答后半句的那个条目。

## 什么时候选它

- 你想要一个模型把 agent 跑一整天，中途不用盯着额度余额。Opus 5 仍然打包在 Claude 订阅里，Fable 5 已经不是了。
- 你的活是**长上下文**：1M 窗口既是默认也是上限，指令遵循与工具调用在整个窗口内都成立——没有更小上下文的变体可退。
- 你要调度 **subagent**。Anthropic 自己的说法是 writer-verifier 模式、极少出现 agent 互相覆盖成果——那正是多 agent 方案最常见的崩法。
- 你的任务不只是代码：带非平凡公式的多 sheet 表格、结构完整的幻灯片。
- 你想按任务调开销：effort 档位可以在"智力"和"省 token"之间调，不用换模型。

## 什么时候不选它

- 单个最难任务要绝对天花板——[Fable 5.1](claude-fable-5.md) 仍然领先；网安类工作上 Mythos 5 直接强于 Opus 5。
- 你在量上对成本敏感。**Sonnet 5 是 $2/$10**，Anthropic 把它定位在接近 Opus 4.8；如果 agent 干的多是常规活，Opus 档就是 2.5 倍的账单换你可能用不上的能力。
- 你要开源或可自托管的模型——这一档完全闭源。
- 你要的是成品 agent 而不是模型，请从 [Claude Code](claude-code.md) 开始。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| Agentic 编码 | 很强 | CursorBench 3.2 距 Fable 5 峰值 0.5% 以内，价格是其一半 |
| 长上下文 | 很强 | 1M token，既是默认也是上限；最大输出 128K |
| 计算机操作 | 很强 | OSWorld 2.0——Anthropic 称其在任意价位上都优于所有模型，且以约三分之一成本超过 Fable 5 |
| 抽象推理 | 很强 | ARC-AGI 3 约为次优模型的 3 倍 |
| 工作流自动化 | 强 | Zapier AutomationBench 通过率约为次优模型的 1.5 倍 |
| 多 agent 协同 | 强 | writer-verifier 子 agent 团队，极少互相覆盖 |
| 网络安全 | 中 | 这一轴上刻意落后于 Mythos 5 |
| 开源 / 自托管 | 无 | 完全闭源 |

Anthropic 主打的头条数字是 Frontier-Bench v0.1：SOTA，且以更低成本达到 Opus 4.8 的两倍以上。单一厂商自测的 benchmark 一律当作"待你用自己负载复核的说法"——这是本地图对所有 benchmark 的固定立场。

## 档位阶梯（一手 API 价格，2026 年 9 月）

| 模型 | 输入 / 输出（每百万） | 缓存读 | 位置 |
| --- | --- | --- | --- |
| [Claude Fable 5.1](claude-fable-5.md) | $10 / $50 | **$0.25** | Mythos 级天花板；缓存读是输入价的 2.5%，而非通常的 10% |
| **Claude Opus 5** | **$5 / $25** | $0.50 | 你实际在跑的那一档；Fast 模式 $10 / $50 |
| Claude Sonnet 5 | $2 / $10 | $0.20 | 走量档——$2/$10 原本是首发促销价，后来转正为长期价 |

Claude 4.6 及以后的模型，1M 上下文在整个窗口内按标准价计费，所以在 Anthropic 这边长上下文不是单独的价格带。对照 [GPT-6 Astra](gpt-6-astra.md)：它超过 272k 输入 token 后输入价翻倍。

## 在哪里能用

- **Claude Code**——默认编码入口；被安全分类器拦下的请求会带提示回退到 Opus 4.8。
- **Claude.ai 与 Claude Cowork**——Max 上的默认，Pro 上的最强。
- **Claude API**——`claude-opus-5`，另有 Bedrock、Google Cloud、Microsoft Foundry。
- **Fast 模式**（research preview）——约 2.5 倍输出速度，2 倍价格，仅第一方 API。

## 与 Claude Code、Fable 5.1 的关系

大多数读者是在 [Claude Code](claude-code.md) 里遇到这个模型的；本 profile 面向的是"你要把什么接进自己的系统"。2026 年 7 月以来的实际分工是：**跑的时候用 Opus 5，硬骨头才花 Fable 5.1 的额度**，高频常规活再往下落到 Sonnet 5。这是逐任务的决定，也正是这条路线存在的意义。

## 结论

Opus 5 是 Anthropic 这一侧不再是"直接为天花板付费"的原因。它守住 Opus 的价格，吃掉了通往 Fable 5 的大部分距离，是没人盯额度表的时候你的 agent 在跑的那个模型。前沿档留给真正需要它的任务。
