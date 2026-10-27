# claude-mem

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](claude-mem.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/claude-mem.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：claude-mem 是一个加装到现有 agent 上的记忆层。生命周期 hooks 记录 agent 做了什么，由模型压缩成观察记录和摘要，下次会话开始时把相关部分注入回去；想往深里查，还有 MCP 搜索工具。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | Alex Newman（[@thedotmack](https://github.com/thedotmack)）和贡献者 |
| 路线 | Runtime & tools——给其他 agent 用的跨会话记忆层 |
| 仓库 | [`thedotmack/claude-mem`](https://github.com/thedotmack/claude-mem)——Apache-2.0，TypeScript；截至 2026-10-28 有 10.36 万 star |
| 开源 | open core。引擎、Claude-Mem Server、CLI、SDK、适配器和 MCP 工具是 Apache-2.0；托管云、团队/组织同步、SSO 等企业功能保留为商业部分 |
| 付费档 | **CMEM Pro**（托管 observer、云同步、私有 MCP 链接）：30 天试用，之后 $30/月；Heavy $70/月，Max $100/月（超额另计费） |
| 适配哪些 agent | [Claude Code](claude-code.md)（插件 marketplace）、[Codex](codex.md)、[OpenCode](opencode.md)（1.3.4+，含 2.x）、[OpenClaw](openclaw.md) gateway、[Pi](pi.md)、[DeepSeek Harness](deepseek-harness.md)、[Grok Bot](grok-bot.md)、T3 Code、Antigravity CLI、Oh My Pi；仓库简介里还列了 Gemini、[Hermes](hermes-agent.md) 和 Copilot |
| 适合谁 | 想让项目上下文跨会话延续、又不想手写记忆文件的开发者 |
| 主要代价 | 本地要跑一个 worker（Bun）和做向量搜索的 Chroma；生成记忆本身要调模型，费用记在你的套餐、你自己的 key 或托管 observer 上 |
| 当前版本 | v15.3.0（2026-10-26）；安装命令 `npx claude-mem install` |
| 官网 | https://cmem.ai · 文档 https://docs.claude-mem.ai |

## 它怎么运作

六个生命周期 hook（`SessionStart`、`UserPromptSubmit`、`PreToolUse`、`PostToolUse`、`Stop`、`SessionEnd`）把 agent 的动作发给本地的 **worker 服务**——一个带网页查看器的 HTTP API，由 Bun 管理。**observer** 模型把原始工具调用整理成带类型的观察记录和会话摘要，存进 **SQLite**（FTS5 关键词搜索），再配一个 **Chroma** 向量库做语义 + 关键词的混合搜索。到下一次 `SessionStart`，相关上下文会被自动注入。

需要深挖时，agent 走项目称为"渐进披露"的三步 MCP 工具：`search` 返回紧凑索引（每条约 50–100 token），`timeline` 看某条结果前后发生了什么，`get_observations` 只拉选中 ID 的完整内容。README 估计这比一次全取省约 10 倍 token。用 `<private>` 标签包住的内容不会被存储。

**observer 跑在哪。** 首次安装时，安装器会让你在浏览器里登录 claude-mem（邮件魔法链接），再选 provider：托管的 claude-mem observer（CMEM Pro，厂商的卖点是把记忆生成从你 agent 的订阅额度里挪出去）、你自己的 OpenRouter 或 Gemini key，或者你的 Anthropic 套餐。传 `--provider`、设 `CLAUDE_MEM_ONLINE_OPTIN=false` 或在 CI 里运行，都会跳过登录。Grok Bot 集成默认用托管服务。README 说登录不需要绑卡，但定价页写的是试用需要信用卡或借记卡。

## 什么时候选它

- 你希望 agent 每次开会话就知道上一次发生了什么，又不想手工维护 `CLAUDE.md` 或记忆文件。
- 你在多个 harness 之间切换，想让它们共用一个记忆库。项目给 Claude Code、Codex、OpenCode、Pi、DeepSeek Harness、OpenClaw 等都提供了适配。
- 你想要省 token 的调回方式：先看索引，需要时才取完整内容。
- 你能接受本地常驻一个 worker，并且要么有给 observer 用的模型 key，要么愿意为托管版付费。

## 什么时候不选

- 你想要能当普通文件读写的记忆。claude-mem 把记忆存在 SQLite 和 Chroma 里，通过网页查看器访问；要文件式方案，看 [MiMoCode](mimocode.md) 或 `CLAUDE.md` 约定。
- 你不希望会话活动离开本机。纯本地可以跑，但默认安装流程会把你引向托管 observer，开了云同步数据也会存在 CMEM 那边。
- 你现在就需要开放许可下的团队共享记忆。团队/组织同步保留为商业部分，TeamBrain 试点也还没公布公开定价。
- 你要的是代码结构上下文而不是历史记录。那是 [CodeGraph](codegraph.md) 和 [Graft](graft.md) 的活。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 跨会话记忆 | 非常强 | hooks 自动采集、压缩成观察记录、会话开始时注入 |
| 检索 | 强 | SQLite FTS5 加 Chroma 混合搜索；三步 MCP 调回 |
| 跨 agent 集成 | 强 | 为十来个 harness 提供适配和安装器，深浅不一（比如 Grok Bot 是靠监听聊天日志文件） |
| 隐私控制 | 中等 | `<private>` 标签、凭证脱敏、可跳过在线登录 |
| 纯本地运行 | 中等 | 支持，但 observer 模型要自己提供，并主动退出托管默认 |
| 独立运行时 | 不是目标 | 它替 agent 记事，自己不行动 |

## 使用成本

复杂度：中。安装器会装好 Bun、uv（向量搜索用）、hooks 和 worker，出问题有 `doctor` 命令修复。持续成本在 observer：每次会话都要模型做摘要，费用记在你的 Anthropic 套餐、你的 OpenRouter 或 Gemini key 上，或者付 CMEM Pro（$30/月起）。发版很频繁：2026-10-23 到 10-26 之间从 v15.0.2 走到了 v15.3.0，要做好经常更新的准备。

采用之前还有一点要知道：README 结尾有一节"What About CMEM?"，说 CMEM 是一个加密货币代币，"由第三方创建，但得到 Claude-Mem 作者的正式认可"，并附上了 Base 链上的合约地址。cmem.ai 的产品页面没有提到它。这不改变软件怎么工作，但它是这个项目公开形象的一部分。

## 底线

claude-mem 是被动调回这种模式的外挂版：agent 不用换，加上 hooks 替它记事。如果你的痛点是"每次会话都从零开始"，它正对着这个问题，而且能跨很多 harness 用。登录之前先想好 observer 要跑在哪，因为开源引擎和托管产品是有意分开的两样东西。

## 来源

- [claude-mem README](https://github.com/thedotmack/claude-mem#readme) · [Releases](https://github.com/thedotmack/claude-mem/releases) · [LICENSE（Apache-2.0）](https://github.com/thedotmack/claude-mem/blob/main/LICENSE) · [docs/license.md](https://github.com/thedotmack/claude-mem/blob/main/docs/license.md) · [docs/ip-boundary.md](https://github.com/thedotmack/claude-mem/blob/main/docs/ip-boundary.md) · [cmem.ai](https://cmem.ai/) · [cmem.ai 定价](https://cmem.ai/pricing) · [文档](https://docs.claude-mem.ai/)
