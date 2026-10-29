# Gemini CLI

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](gemini-cli.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/gemini-cli.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Gemini CLI 是谷歌的开源终端 agent，但它**已经不是谷歌给个人用户的免费入口**：2026 年 6 月 18 日起，免费用户和 Google AI Pro、Ultra 订阅用户改由 [Google Antigravity](antigravity.md) 的 CLI 承接。它现在是给 Gemini Code Assist Standard / Enterprise 组织和付费 Gemini API key 用的 Apache-2.0 客户端。

> **更正（2026-10-30）：** 本 profile 原先以面向个人的免费额度开头，而这一点从 2026-06-18 起已经不成立。谷歌的配额页面顶部现在写着："Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026." 谷歌开发者博客（2026 年 5 月 19 日）说，自该日起 Gemini CLI 不再服务 Google AI Pro 和 Ultra 订阅用户、Gemini Code Assist 个人版的免费用户以及 Code Assist IDE 扩展；Code Assist Standard / Enterprise 组织和付费的 Gemini、Gemini Enterprise Agent Platform API key 继续可用，Antigravity CLI 则"对所有人开放"。"每分钟 60 次"这个数字也一并撤回：谷歌页面上没有给出每分钟的具体数字。下文已就地改正。来源：[Gemini CLI 配额与价格](https://geminicli.com/docs/resources/quota-and-pricing)、[谷歌开发者博客](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 谷歌 |
| 路线 | 直接执行 |
| 仓库 | [`google-gemini/gemini-cli`](https://github.com/google-gemini/gemini-cli)——Apache-2.0，TypeScript，**10.9 万 star（2026-10-28）** |
| 是否开源 | 是（Apache-2.0） |
| 最适合 | Code Assist Standard / Enterprise 组织和付费 Gemini API key 用户在 Gemini 上做终端工作 |
| 主要代价 | 2026-06-18 起个人用户没有免费路径；需要 Code Assist Standard / Enterprise 授权或付费 API key，并有每分钟和每天的请求上限 |
| 免费额度 | **2026-06-18 起不再面向个人用户。** 谷歌配额页面仍为 Gemini Code Assist 个人版列出每天 1,000 次请求，但这批用户已在 2026-06-18 转到 Antigravity CLI；每分钟上限没有公布具体数字 |
| 文档 | https://geminicli.com/docs/ |

## 为什么要收录

本地图有一个事实性漏洞。它自己的市场事件时间线在 2026 年 8 月记下 Meta 的 Muse Code"补上第一方编码 CLI 阵营的最后一块"——而这个阵营从头到尾都缺着谷歌那一个。本地图收了 [Claude Code](claude-code.md)、[Codex](codex.md)、[Grok Build](grok-build.md)、[Kimi Code](kimi-code.md)、[MiMoCode](mimocode.md)、[Qwen Code](qwen-code.md)，时间线里也记了 Meta 的 Muse Code，却没有那个 10.9 万 star（2026-10-28）的厂商 CLI 的页面。

它同样在 [CodeGraph](codegraph.md)、[Superpowers](superpowers.md)、[oh-my-claudecode](oh-my-claudecode.md) 里被当作集成对象提到——和藏住 [OpenCode](opencode.md) 的是同一个模式。

## 什么时候选它

- **你的组织已经买了 Gemini Code Assist Standard 或 Enterprise，或者你用的是付费 Gemini API key。** 这是谷歌在 2026-06-18 之后保留的访问方式。如果你是个人用户、预算又是约束条件，请改看 [Google Antigravity](antigravity.md)。
- 你想要**循环内置谷歌搜索接地**——它是内置工具，不是你得自己接的 MCP server。对研究形态的任务，这相对这里其他所有 CLI 都是实打实的差异点。
- 你想在终端里用带 **100 万上下文的 Gemini 3**，并且要厂商自己的调校。
- 你想要客户端上的宽松许可：Apache-2.0，不同于这条路线上那些闭源第一方 CLI。
- 你要 MCP 支持和终端优先的设计，但不想因此接受一整个 IDE 的主张。

## 什么时候不选它

- 你的模型承诺在别处。这个工具的存在是为了跑 Gemini；如果你在 Claude 或 GPT 上，它们自家的 CLI 调得更好——见[编码 CLI 对比](../comparisons/coding-cli-agents.md)。
- **你需要可预测的吞吐。** 每分钟和每天的请求上限，就是横在 agent 循环中间的一道限流；在依赖它之前先把付费路径算进预算。
- 你要一条厂商中立的循环——那是 [OpenCode](opencode.md)。
- 你需要本地部署或离线运行。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 入门成本 | 对个人用户弱 | 免费用户和 Google One 用户已在 2026-06-18 转到 Antigravity CLI；现在需要 Code Assist Standard / Enterprise 授权或付费 API key |
| 搜索接地 | 很强 | 谷歌搜索是内置工具，不是外挂 |
| 长上下文 | 很强 | Gemini 3，100 万 token 上下文窗口 |
| 可扩展性 | 强 | MCP 支持自定义集成 |
| 许可 | 强 | 客户端 Apache-2.0 |
| 吞吐可预测性 | 中 | 请求按分钟和按天双重限流 |
| 模型自由度 | 弱 | 它是谷歌为谷歌模型做的 CLI |

## 与谷歌其他 agent 入口的关系

谷歌在本地图上出现在三个容易混淆的位置。[Jules](jules.md) 是管理式后台 agent；[Google Antigravity](antigravity.md) 是谷歌的 agent 优先平台（桌面应用、IDE、编辑器扩展和 `agy` CLI），也是 2026-06-18 之后谷歌把原先用 Gemini CLI 的免费用户和 Google One 用户转过去的地方；Gemini CLI 则是你自己驱动的终端循环。要任务队列就拿 Jules，要坐在循环里就拿这个。

## 结论

免费额度在 2026-06-18 之前是头条。那天谷歌把个人免费用户和 Google AI Pro、Ultra 订阅用户转到了 [Google Antigravity](antigravity.md) 的 CLI，如果你属于这一类，请从那里开始。Gemini CLI 仍是 Code Assist Standard / Enterprise 组织和付费 Gemini API key 用的 Apache-2.0 终端 agent。在把自动化建在它上面之前先掂量限流，并把模型锁定当作换取调校的代价。
