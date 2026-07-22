# 成本 & benchmark

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](cost-and-benchmarks.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/cost-and-benchmarks.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

[热度榜](../README.md#recent-heat-ranking)追踪流行度，[能力矩阵](../capabilities/matrix.md)追踪形态。本页追踪它俩都不显示的两件事：**一个编码 agent 到底多能打，以及跑起来多少钱。**

到 2026 年年中，这两个问题合成了一个。模型层转向分档和按量计费——Anthropic 的 Fable 5 按额度、OpenAI 的 GPT-5.6 三档定价——"这个任务用哪个模型、哪一档"就成了核心选型决策。时间线见[市场脉搏](../README.md#market-pulse)和[市场事件](../market-events.md)。

## 成本有两层

1. **你烧的模型**——agent 发给前沿模型的 token。能力和每 token 价格都在这一层，对多数正经编码 agent 来说，它主导账单。
2. **agent 为封装它怎么收费**——开源（你只付模型钱）、订阅打包、按量额度，还是托管席位。这才是你实际签约的东西。

## 第一层——前沿编码模型：能力 vs 价格

**Artificial Analysis 编码 agent 指数**是本图追踪的跨模型能力数字。价格按每 **100 万 token（输入 / 输出）**计。

| 模型 | AA 编码 agent 指数 | 其他 benchmark | 价格（输入 / 输出 每 1M） | 备注 |
| --- | :-: | --- | --- | --- |
| **GPT-5.6 Sol**（OpenAI） | **80** | — | $5 / $30 | 当前指数第一；另有多 agent "Ultra" 档 |
| **GPT-5.6 Terra**（OpenAI） | — | — | $2.5 / $15 | 7 月 9 日 GPT-5.6 发布的中档 |
| **GPT-5.6 Luna**（OpenAI） | — | — | $1 / $6 | GPT-5.6 的经济档 |
| **Claude Fable 5**（Anthropic） | **77.2** | — | $10 / $50 | Mythos 级；按量额度计费，不打包进订阅 |
| **GPT-5.5**（OpenAI） | **76.4** | SWE-Bench Pro 58.6% | —（≈GPT-5.4 的 2×） | 2026 春季参照模型 |
| **Claude Opus 4.8**（Anthropic） | **72.5** | — | $5 / $25 | 两侧都是 Fable 5 的一半（见 [Fable 5 profile](../agents/claude-fable-5.md)）；Claude Code 里可靠的默认 |

> SWE-Bench Pro 参照点：Claude Opus 4.7 得 64.3%，高于 GPT-5.5 的 58.6%。破折号（—）表示本图未追踪该数字，不是零。数据截至 **2026 年 7 月**，取自厂商 profile（[Claude Fable 5](../agents/claude-fable-5.md)、[GPT-5.5](../agents/gpt-5.5.md)）；价格和指数位次会变——预算前务必以厂商为准。

能一周周站得住的结论：

- **指数差距真实但不大**——当前前沿大致 72–80。而*价格*差距要大得多（Luna 的 $1/$6 vs Fable 5 的 $10/$50 输出，是输出 token 上约 8× 的差距）。多数编码工作里，便宜档才是理性默认；只有任务真需要时才够到指数顶端。
- **分档现在是那根杠杆。** GPT-5.6 的 Sol/Terra/Luna、以及 Claude 的 Fable 5-对-Opus-4.8 之分，意味着同一个 agent 指向不同模型，成本会天差地别。这是逐任务决策，不是一次性设置。

## 第二层——编码 agent 怎么收费

封装层的计费模型决定了你付钱给谁、账单多可预测。

| Agent | 计费模型 | 你付给 | 可预测性 |
| --- | --- | --- | --- |
| [Claude Code](../agents/claude-code.md) | 订阅（Pro/Max） + Fable 5 **按量额度** | Anthropic | 中——Opus 4.8 打包内含；Fable 5 用量浮动 |
| [Codex](../agents/codex.md) | 打包进 ChatGPT 计划（Free → Pro）；重度 CLI 走 API | OpenAI | 中——计划打包 + API 溢出 |
| [Cursor](../agents/cursor.md) | 订阅 / 席位（Teams 定价） | Cursor | 高——固定席位，模型用量在额度内 |
| [GitHub Copilot](../agents/github-copilot.md) | 订阅 / 席位 | GitHub | 高——固定席位 |
| [Devin](../agents/devin.md) | 托管席位 + 用量 | Cognition | 低-中——托管执行叠加用量成本 |
| [Aider](../agents/aider.md)、[Cline](../agents/cline.md)、[Continue](../agents/continue.md) | **开源，自带 key** | 直接付模型 provider | 低——你看到原始 token 成本，无加价 |
| [Pi](../agents/pi.md)、[jcode](../agents/jcode.md)、[OpenHands](../agents/openhands.md) | **开源 harness，自带 provider** | 直接付模型 provider | 低——你拥有循环，也拥有账单 |
| [Kimi Code](../agents/kimi-code.md)、[MiMoCode](../agents/mimocode.md)、[CodeWhale](../agents/codewhale.md) | 开源，厂商 / 低成本模型 | Moonshot / 小米 / DeepSeek API | 低——国产模型栈把每 token 成本压得低 |

## 三种成本形态

- **"免费" agent，你付模型钱。** Aider、Cline、Pi、jcode、OpenHands 和各 harness 装起来不花钱——整份账单就是你指向的那个模型 API。最便宜也最透明，但速率限制、key、超支风险都归你。
- **打包订阅。** Claude Code、Codex、Cursor、Copilot 把模型用量折进一个固定计划（重度用量溢出到按量/API）。对稳定的个人使用最可预测；天花板是计划的合理使用上限。
- **按量额度 / 托管用量。** Claude Code 里的 Fable 5 额度，以及 Devin 这类托管产品，按实际干的活计费。这是单个硬任务可能迅速变贵的地方——也是选对*档位*（第一层）最要紧的地方。

还有一层 token 账单藏起来的**运维成本**：RAM、启动时间、自托管的运维负担。性能优先的 harness 把这点摆到明面——比如 [jcode](../agents/jcode.md) 就主打同类最低 RAM、最快启动，专门让很多并行会话跑起来便宜。每个 profile 的"使用成本"一节按项目讲这点。

## 怎么选

1. **先估你的主导成本。** 每天在前沿模型上重度编码？第一层（模型）主导——优化档位。轻量或阵发式使用？打包订阅通常更便宜也更省心。
2. **让计费模型匹配你的可预测性需求。** 要固定预算项的团队要席位制（Cursor、Copilot）；要透明、无加价的开发者要开源 agent + 自己的 key。
3. **只为你会用到的指数付钱。** 前沿之间的能力差距不大，价格差距很大。默认用便宜档，逐任务往上够，而不是所有东西都跑在最贵的模型上。

按维度看能力形态见[能力矩阵](../capabilities/matrix.md)；模型层时间线见[市场事件](../market-events.md)。
