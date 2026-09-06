# Gemini CLI

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](gemini-cli.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/gemini-cli.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Gemini CLI 是谷歌的开源终端 agent，也是本地图上唯一一个**免费额度足以干真活**的第一方编码 CLI——个人谷歌账号每天 1,000 次请求。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 谷歌 |
| 路线 | 直接执行 |
| 仓库 | [`google-gemini/gemini-cli`](https://github.com/google-gemini/gemini-cli)——Apache-2.0，TypeScript，**10.7 万 star** |
| 是否开源 | 是（Apache-2.0） |
| 最适合 | 在 Gemini 上做终端工作，以及任何需要零成本可用 agent 的人 |
| 主要代价 | 免费档有速率限制；用量大了就要走谷歌的付费计划 |
| 免费额度 | 个人谷歌账号 **每分钟 60 次、每天 1,000 次请求** |
| 文档 | https://geminicli.com/docs/ |

## 为什么要收录

本地图有一个事实性漏洞。它自己的市场事件时间线在 2026 年 8 月记下 Meta 的 Muse Code"补上第一方编码 CLI 阵营的最后一块"——而这个阵营从头到尾都缺着谷歌那一个。本地图收了 [Claude Code](claude-code.md)、[Codex](codex.md)、[Grok Build](grok-build.md)、[Kimi Code](kimi-code.md)、[MiMoCode](mimocode.md)、[CodeWhale](codewhale.md)，却没有那个 10.7 万 star 的厂商 CLI 的页面。

它同样在 [CodeGraph](codegraph.md)、[Superpowers](superpowers.md)、[oh-my-claudecode](oh-my-claudecode.md) 里被当作集成对象提到——和藏住 [OpenCode](opencode.md) 的是同一个模式。

## 什么时候选它

- **预算是约束条件。** 个人账号每天 1,000 次免费不是试用，是够日常干活的量，而这条路线上没有第二家提供。
- 你想要**循环内置谷歌搜索接地**——它是内置工具，不是你得自己接的 MCP server。对研究形态的任务，这相对这里其他所有 CLI 都是实打实的差异点。
- 你想在终端里用带 **100 万上下文的 Gemini 3**，并且要厂商自己的调校。
- 你想要客户端上的宽松许可：Apache-2.0，不同于这条路线上那些闭源第一方 CLI。
- 你要 MCP 支持和终端优先的设计，但不想因此接受一整个 IDE 的主张。

## 什么时候不选它

- 你的模型承诺在别处。这个工具的存在是为了跑 Gemini；如果你在 Claude 或 GPT 上，它们自家的 CLI 调得更好——见[编码 CLI 对比](../comparisons/coding-cli-agents.md)。
- **你需要可预测的吞吐。** 带每分钟和每天上限的免费档，就是横在 agent 循环中间的一道限流；在依赖它之前先把付费路径算进预算。
- 你要一条厂商中立的循环——那是 [OpenCode](opencode.md)。
- 你需要本地部署或离线运行。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 入门成本 | **很强** | 这条路线里最慷慨的免费档，且差距明显 |
| 搜索接地 | 很强 | 谷歌搜索是内置工具，不是外挂 |
| 长上下文 | 很强 | Gemini 3，100 万 token 上下文窗口 |
| 可扩展性 | 强 | MCP 支持自定义集成 |
| 许可 | 强 | 客户端 Apache-2.0 |
| 吞吐可预测性 | 中 | 免费档按分钟和按天双重限流 |
| 模型自由度 | 弱 | 它是谷歌为谷歌模型做的 CLI |

## 与谷歌其他 agent 入口的关系

谷歌在本地图上出现在三个容易混淆的位置。[Jules](jules.md) 是管理式后台 agent；**Antigravity** 是谷歌的 agent 优先 IDE，被 [CodeGraph](codegraph.md) 与 [Omnigent](omnigent.md) 当作集成对象提到，但本地图尚未收录；Gemini CLI 则是你自己驱动的终端循环。要任务队列就拿 Jules，要坐在循环里就拿这个。

## 结论

免费额度是头条，而且不是噱头——对个人开发者、以及任何没有预算科目就要评估 agent 的人，这是本地图上门槛最低的正经 agent。在把自动化建在它上面之前先掂量限流，并把模型锁定当作换取调校的代价。
