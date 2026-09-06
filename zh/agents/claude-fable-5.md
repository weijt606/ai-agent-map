# Claude Fable 5.1

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](claude-fable-5.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/claude-fable-5.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Claude Fable 5.1 是 2026-09-01 起 Anthropic 的 Mythos 级天花板——标价与 Fable 5 一模一样，缓存读价砍掉 75%，让长会话 agent 实打实变便宜；它是你花额度去买的那个模型，不是你整天跑的那个。

> 本页覆盖整条 Fable 线。文件仍沿用 2026 年 6 月首次收录时的 `claude-fable-5.md` 路径，以免既有链接失效。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Anthropic |
| 路线 | 前沿 agentic 模型（Mythos 级）——[Opus 5](claude-opus-5.md) 之上的天花板 |
| 是否开源 | 否 |
| 最适合 | 最难的 agentic 工作：大型迁移、多 agent 工作流、深度研究、前沿编码 |
| 主要代价 | $10 / $50 每百万 token；2026-07-07 起在 Claude 订阅内按额度计费 |
| 缓存读 | **$0.25 / M**——输入价的 2.5%，而通常是 10% |
| 官方公告 | https://www.anthropic.com/news/claude-fable-5-mythos-5 |

## 为什么要收录一个模型

和 [GPT-6 Astra](gpt-6-astra.md) 一样，这是模型而不是 agent 产品。收录原因：它给本地图上大多数 agent 所依赖的模型层引入了一个新等级（Mythos，位于 Opus 之上），而且它的定价与可用性轨迹直接改变了 Claude Code 和 Claude 系 agent 的选型与预算方式。

Fable 与 **Mythos** 在每个版本上共享同一底层模型，区别在安全访问：Fable 5.1 面向所有人开放；Mythos 5.1 保护措施更轻，仅通过 Project Glasswing 向经审核的组织开放——网络防御、基础设施，以及特选生命科学研究。

## 什么时候选它

- 你想要当前最强的 Claude 模型来做 agentic 工作——工程、研究或分析。
- 你的任务大到配得上这个价格。Fable 5 发布时的参照案例是 Stripe 报告"原本需要整个团队手工做两个月的代码库迁移"一天完成。
- **你的 agent 每一轮都要重读一大块上下文。** 这是 5.1 特有的理由：缓存读从 $1/M 降到 $0.25/M，Anthropic 给出的口径是典型负载省约 25%、重 agent 负载最多省 45%，而标价一分没动。
- 你在安全相邻的代码上被误拒过。Anthropic 称 5.1 让 Claude Code 用户的网安类误报少了约 60%。

## 什么时候别选

- 你对成本敏感——$10/$50 每百万 token，两端都是 [Opus 5](claude-opus-5.md) 的 2 倍，且 2026-07-07 起从订阅内含改为按量计费。
- 你的工作负载用不到 Mythos 级能力。**它下面的 Opus 5 才是可靠默认档**，以一半价格吃掉了大部分距离；再往下还有 $2/$10 的 Sonnet 5。
- 你需要开源或自托管模型。
- 你要的是成品 agent 产品而不是模型——请看 [Claude Code](claude-code.md)。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Agentic coding | 很强 | Terminal-Bench 4.0 从 42.0%（Fable 5）升到 **55.8%** |
| 软件工程 | 很强 | **SWE-bench Pro 81.2**——对 Fable 5 与 Opus 5 都是小幅领先 |
| 科研工作 | 很强 | Terminal-Bench-Science 翻倍有余，24.7% → **52.6%** |
| 知识工作 | 很强 | Fable 5 发布时金融分析 benchmark 最高分 |
| 视觉 | 很强 | 能从截图重建 web 应用源代码；自主通关《宝可梦 火红》 |
| 长会话经济性 | 强 | 缓存读为输入价的 2.5%——本地图上所有前沿模型里最便宜的缓存读 |
| 可用性稳定度 | 中 | 2026-06-12 → 07-01 因短暂出口管制全球下架；现在位于更严格的安全分类器之后，被拦截自动回退到 Opus 档 |
| 开源 / 自托管 | 无 | 完全闭源 |

**来源说明。** Anthropic **没有**为 Fable 5 或 Fable 5.1 公布 SWE-bench Verified 分数。外面流传的 5.1"SWE-bench Verified 95%"来自第三方榜单。Anthropic 自己报的软件工程数字是 SWE-bench Pro 81.2，本地图记的就是这个。

## 版本与可用性时间线（2026）

- **6 月 9 日** —— Fable 5 发布；成为 Claude Code 中 Pro/Max 订阅的默认模型。
- **6 月 12 日** —— 因一份越狱报告触发美国出口管制，全球下架。
- **7 月 1 日** —— 在更严格的安全分类器后面全球恢复；被拦截的请求会通知并回退到 Opus 档。
- **7 月 7 日** —— 订阅内含结束，Fable 改为按量计费的 usage credits。
- **7 月 24 日** —— [Opus 5](claude-opus-5.md) 发布并成为其下的默认档，"要不要花这个额度"的比较对象随之改变。
- **9 月 1 日** —— **Fable 5.1 与 Mythos 5.1** 发布。缓存读砍 75%、上表的 benchmark 提升、Claude Code 网安误报少约 60%，以及对 Claude 生成文本的隐形水印——按欧盟法规要求，配套检测 API 面向符合条件的组织私有预览。

## 和 Claude Code 的关系

本页讲的是模型。多数读者实际接触它的地方是 [Claude Code](claude-code.md)。现实问题是按任务决策：**最难的活花 Fable 5.1 额度，其余留在 [Opus 5](claude-opus-5.md)。**

## 最后一句

Fable 让"这个任务值得买哪一档智能"在 Anthropic 侧变成了真实的选型问题，正如 GPT-5.6 的三档在 OpenAI 侧做的那样。5.1 这次没动标价，动的是长跑 agent 真正产生的那部分账单。价格、按量计费、分类器回退三者都要计入预算；而如果你的 agent 会反复重放大块上下文，9 月 1 日之后这笔账要重算。
