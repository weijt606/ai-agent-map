# Qwen Code

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](qwen-code.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/qwen-code.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Qwen Code 是少见的两头都开放的厂商 CLI——客户端 Apache-2.0，[模型也是开放权重](qwen3-coder.md)——而且它乐意改跑 Anthropic、OpenAI 或本地 Ollama 端点。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 阿里 / Qwen |
| 路线 | 直接执行 |
| 仓库 | [`QwenLM/qwen-code`](https://github.com/QwenLM/qwen-code)——Apache-2.0，TypeScript，**2.77 万 star** |
| 是否开源 | 是（Apache-2.0），模型同样开放 |
| 最适合 | 想要一个厂商 CLI、但不想要通常随之而来的厂商锁定的团队 |
| 主要代价 | 体量小于头部 CLI；自迭代的开发方式很特别，值得先搞清楚 |
| 使用面 | 终端、IDE 插件、桌面应用、daemon 模式、SDK、IM 机器人 |
| 博客 | https://qwenlm.github.io/blog/ |

## 为什么要收录

本地图的直接执行路线是每个模型家族收一个厂商 CLI，而阿里那个一直缺着。它同时补上了一对：本地图现在收了开放权重模型 [Qwen3-Coder](qwen3-coder.md)，而这就是厂商为跑它而发的循环。

有意思的性质在于这个组合。这里其他所有第一方 CLI，都是"开放或闭源的客户端 + **闭源**权重"。Qwen Code 两侧都开放，这让"无厂商锁定"从一句口号变成一个可核对的说法。

## 什么时候选它

- **你想在运行时换模型。** 它支持 OpenAI、Anthropic、Gemini 与 Qwen 的 API，外加任意第三方厂商或经 Ollama / vLLM 的本地模型——运行时切换，而不是装的时候定死。
- 你想要**零配置的 agent 能力**：Auto-Memory、Auto-Skills、SubAgents、Agent Teams 与 MCP，按其说法开箱即用。
- 你需要它**走出终端**：IDE 插件、桌面应用、daemon 模式、SDK，以及 Telegram、钉钉、微信、飞书的 IM 机器人——和本地图在 [WorkBuddy](workbuddy.md)、[ZCode](zcode.md) 上记录到的是同一种消息面模式。
- 你要整条栈都开放——Apache-2.0 客户端加开放权重模型——用于审计或隔离网部署。

## 什么时候不选它

- 你要最大的生态。2.77 万 star 比 [OpenCode](opencode.md) 和 [Gemini CLI](gemini-cli.md) 低一个数量级，瞄准它的第三方集成更少。
- **自迭代的开发方式对你重要。** 项目声明它用自己的 agent 和模型来提 issue、提 PR、评审代码、跑测试。这既是一个关于 agent 成熟度的有趣主张，也是一个关于评审深度的治理问题——采纳前先决定你持哪种读法。
- 你要的是厂商中立项目而不是某厂商的开放项目——那是 [OpenCode](opencode.md)。
- 你的模型承诺是 Claude 或 GPT，而且想要它们调好的默认值。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 模型自由度 | **很强** | 多协议且可运行时切换，含本地模型 |
| 开放度 | 很强 | Apache-2.0 客户端 + 开放权重模型——这个组合很少见 |
| 交付面 | 很强 | 终端、IDE、桌面、daemon、SDK、四个 IM 平台 |
| Agent 能力 | 强 | Auto-Memory、Auto-Skills、SubAgents、Agent Teams、MCP |
| 生态体量 | 中 | 采纳度明显落后于头部 CLI |
| 开发治理 | 中 | 自迭代：自己的 agent 在提 issue、提 PR、做评审 |

## 和 Qwen3-Coder 的关系

[Qwen3-Coder](qwen3-coder.md) 是模型，这个是循环。两者一起发布、一起演进，这是把它们成对使用的理由——但多协议支持意味着你可以只要循环不要模型，或只要模型不要循环。在本地图上，这个组合罕见到足以成为你去看它们任何一个的理由。

## 结论

Qwen Code 回答的是"我能不能要一家厂商的 CLI、但不要它的引力"。生态比头部小，开发流程特别，但两层都真开放，而且按设计就能在不同厂商之间搬。
