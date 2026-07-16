# Claude Fable 5

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](claude-fable-5.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/claude-fable-5.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Claude Fable 5 是 Anthropic 首个正式开放的 Mythos 级模型——位于 Opus 之上的新等级——2026 年 6 月起它就是 Claude 系 agent 的能力天花板，价格与配给方式也相应而来。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Anthropic |
| 路线 | 驱动 Claude Code、Claude.ai 和 API 的前沿 agentic 模型（Mythos 级） |
| 是否开源 | 否 |
| 最适合 | 最难的 agentic 工作：大型迁移、多 agent 工作流、深度研究、前沿编码 |
| 主要代价 | $10/M 输入、$50/M 输出；2026-07-07 起在 Claude 订阅内按额度计费 |
| 官方公告 | https://www.anthropic.com/news/claude-fable-5-mythos-5 |

## 为什么要收录一个模型

和 [GPT-5.5](gpt-5.5.md) 一样，这是模型而不是 agent 产品。收录原因：它给本地图上大多数 agent 所依赖的模型层引入了一个新等级（Mythos，位于 Opus 之上），而且它 6–7 月的可用性波折直接改变了 Claude Code 和 Claude 系 agent 的选型与预算方式。

Fable 5 与 **Claude Mythos 5** 共享同一底层模型：Fable 5 是面向所有人的版本，对双重用途能力附加了安全措施；Mythos 5 不带这些措施，仅向获批组织开放（网络防御、基础设施、Project Glasswing 伙伴及特选生物研究者）。

## 什么时候选它

- 你想要当前最强的 Claude 模型来做 agentic 工作——工程、研究或分析。
- 你的任务大到配得上这个价格：发布时的参照案例是 Stripe 报告"原本需要整个团队手工做两个月的代码库迁移"一天完成。
- 你在跑复杂的多 agent 工作流，希望更少轮次拿到结果。
- 你本来就在 Claude Code / Claude.ai 里工作，能为最难的任务安排额度预算。

## 什么时候别选

- 你对成本敏感——$10/$50 每百万 token，两端都是 Opus 4.8 的 2 倍，且 2026-07-07 起从订阅内含改为按量计费。
- 你的工作负载用不到 Mythos 级能力——它下面的 Opus 4.8 是可靠默认档，能覆盖大多数工作。
- 你需要开源或自托管模型。
- 你要的是成品 agent 产品而不是模型——请看 [Claude Code](claude-code.md)。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Agentic coding | 很强 | Artificial Analysis 编码 agent 指数 77.2——高于 GPT-5.5（76.4）和 Opus 4.8（72.5），低于 GPT-5.6 Sol（80） |
| 知识工作 | 很强 | 发布时金融分析 benchmark 最高分 |
| 视觉 | 很强 | 能从截图重建 web 应用源代码；自主通关《宝可梦 火红》 |
| 科研工作 | 很强 | 蛋白设计流程提速约 10 倍；首个能稳定产出新颖分子生物学假说的模型 |
| 多 agent 工作流 | 强 | 从业者反复报告的体验是"更少轮次、更强工程力" |
| 可用性稳定度 | 中 | 2026-06-12 → 07-01 因短暂出口管制全球下架；现在位于更严格的安全分类器之后，被拦截自动回退 Opus 4.8 |
| 开源 / 自托管 | 无 | 完全闭源 |

## 可用性时间线（2026）

- **6 月 9 日** —— 发布；成为 Claude Code 中 Pro/Max 订阅的默认模型。
- **6 月 12 日** —— 因一份越狱报告触发美国出口管制，全球下架。
- **7 月 1 日** —— 在更严格的安全分类器后面全球恢复；被拦截的请求会通知并回退到 Opus 4.8。
- **7 月 7 日** —— 订阅内含结束，Fable 5 改为按量计费的 usage credits。

## 和 Claude Code 的关系

本页讲的是模型。多数读者实际接触它的地方是 [Claude Code](claude-code.md)。2026 年 7 月起，Claude Code 里的现实问题是按任务决策：最难的活花 Fable 5 额度，其余留在 Opus 4.8。

## 最后一句

Fable 5 让"这个任务值得买哪一档智能"在 Anthropic 侧变成了真实的选型问题，正如 GPT-5.6 的 Sol/Terra/Luna 三档在 OpenAI 侧做的那样。能力跃升是真的；价格、按量计费和安全分类器回退也是真的——三者都要计入预算。
