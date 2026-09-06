# 成本 & benchmark

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](cost-and-benchmarks.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/cost-and-benchmarks.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

[热度榜](../README.md#recent-heat-ranking)追踪流行度，[能力矩阵](../capabilities/matrix.md)追踪形态。本页追踪它俩都不显示的两件事：**一个编码 agent 到底多能打，以及跑起来多少钱。**

到 2026 年年中，这两个问题合成了一个。模型层转向分档和按量计费——Anthropic 的 Fable 线按额度、OpenAI 的 GPT-5.6 三档定价——"这个任务用哪个模型、哪一档"就成了核心选型决策。随后两家的天花板又在 2026 年 9 月头几天各动一次（[Fable 5.1](../agents/claude-fable-5.md) 在 1 日，[GPT-6 Astra](../agents/gpt-6-astra.md) 在 3 日），并落到同一个标价。时间线见[市场脉搏](../README.md#market-pulse)和[市场事件](../market-events.md)。

## 成本有两层

1. **你烧的模型**——agent 发给前沿模型的 token。能力和每 token 价格都在这一层，对多数正经编码 agent 来说，它主导账单。
2. **agent 为封装它怎么收费**——开源（你只付模型钱）、订阅打包、按量额度，还是托管席位。这才是你实际签约的东西。

## 第一层——前沿编码模型：能力 vs 价格

**Artificial Analysis 编码 agent 指数**是本地图追踪的跨模型能力数字。价格按**每百万 token（输入 / 输出）**，取自各厂商自己的价格页。

| 模型 | AA 编码 agent 指数 | 其他 benchmark | 价格（输入 / 输出，每百万） | 缓存读 | 备注 |
| --- | :-: | --- | --- | :-: | --- |
| **GPT-6 Astra**（OpenAI） | — | DeepSWE v1.1 74.1% | **$10 / $50** | $1 | OpenAI 当前天花板，**2026-09-03**。输入超 **272k token 后换价到 $20 / $75**；Fast 模式 2 倍价；正式开放的版本**会拒绝自己一部分网安能力** |
| **Claude Fable 5.1**（Anthropic） | — | **SWE-bench Pro 81.2** | **$10 / $50** | **$0.25** | Anthropic 当前天花板，**2026-09-01**。标价与 Fable 5 相同，缓存读砍 75%。1M 上下文整窗按标准价。按额度计费，不含在订阅内 |
| **GPT-5.6 Sol**（OpenAI） | **80** | — | **$4 / $20**（促销） | — | 最近一次测得的指数第一。**2026-08-21** 从 $5 / $30 下调，为期三个月，至少到 **2026-11-21**。长上下文档 $8 / $30 |
| **Claude Fable 5**（Anthropic） | **77.2** | — | $10 / $50 | $1 | 9 月 1 日被 5.1 接棒；作为指数参照点保留 |
| **GPT-5.5**（OpenAI） | **76.4** | SWE-Bench Pro 58.6% | —（≈GPT-5.4 的 2×） | — | 2026 春季参照模型，已隔两代 |
| **Claude Opus 5**（Anthropic） | — | SWE-bench Pro 略低于 Fable 5.1 的 81.2 | $5 / $25 | $0.50 | **你实际会跑的那一档**——两端都是 Fable 的一半，1M 上下文既是默认也是上限。Fast 模式 $10 / $50 |
| **Claude Opus 4.8**（Anthropic） | **72.5** | — | $5 / $25 | $0.50 | 7 月 24 日被 Opus 5 接棒；仍是请求触发安全分类器时的自动回退 |
| **Claude Sonnet 5**（Anthropic） | — | — | **$2 / $10** | $0.20 | 走量档；首发价已转正，原定 9 月 1 日涨到 $3 / $15 的计划取消 |
| **GPT-5.6 Terra**（OpenAI） | — | — | $2 / $12 | — | 中档。7 月 9 日发布时标 $2.5 / $15，一手价格页现在显示 $2 / $12 |
| **GPT-5.6 Luna**（OpenAI） | — | — | $0.20 / $1.20 | — | 经济档。发布时标 $1 / $6，现在一手页面是 $0.20 / $1.20 |
| **Muse Spark 1.2**（Meta）—— Standard | — | — | $1.25 / $4.25 | $0.15 | Muse Code 背后的编码模型，**2026-08-31** 转正。3,000 请求/分、4M token/分。没有本地图愿意照抄的指数数字 |
| **Muse Spark 1.2**（Meta）—— Contributor | — | — | **$0.10 / $0.20** | $0.002 | 同一个模型，输入约便宜 12 倍、输出约便宜 21 倍，**代价是允许 Meta 用你的 prompt 与 completion 训练未来模型**。限 60 请求/分。这是治理决策，不是预算决策 |

> SWE-Bench Pro 参照点：Claude Opus 4.7 得 64.3%，高于 GPT-5.5 的 58.6%。破折号（—）表示本图未追踪该数字，不是零——**Astra、Fable 5.1、Opus 5 目前没有本地图愿意照抄的指数数字**，本地图也不用第三方榜单去填这个空。价格截至 **2026-09-06**，取自 [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing) 与 [developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing)；benchmark 取自各 profile（[Fable 5.1](../agents/claude-fable-5.md)、[Opus 5](../agents/claude-opus-5.md)、[GPT-6 Astra](../agents/gpt-6-astra.md)、[GPT-5.5](../agents/gpt-5.5.md)）与 [market-events](../market-events.md)。价格和指数位次会变——预算前务必以厂商为准。

能扛过每周变化的几条判断：

- **两家的天花板现在标价一样。** GPT-6 Astra 和 Claude Fable 5.1 都是 $10 / $50。这是本地图第一次记录到两家的前沿档落在完全相同的标价上，于是比较完全离开了标价，转到**缓存读**（$0.25 对 $1，4 倍差）和**长上下文的计价形状**上。
- **长上下文两家计价方式不同，而这已经成了设计约束。** Anthropic 的 1M 窗口整窗按标准价。OpenAI 在输入超过 **272k token** 后对整个请求换价——$20 / $75 而不是 $10 / $50。一个会在长会话里不断堆积上下文的 agent，可能在没人拍板的情况下越线；Claude 这边没有这条线可越。
- **账单真正堆积的地方是缓存，不是输入。** 长跑 agent 每一轮都重放一大块 prompt。$0.25/M 对 $1/M，正是 Fable 5.1 那个"典型省约 25%、重 agent 最多省 45%"的来源，而每 token 标价一分没动。只按标价比前沿模型，比的是错的那一列。
- **分档仍然是杠杆，而且两条阶梯都变深了。** Astra 之下是 GPT-5.6 的 Sol/Terra/Luna；Fable 5.1 之下是 Opus 5 和 Sonnet 5。现在单一厂商内部的价差已经大于厂商之间的价差——Sonnet 5 的 $2/$10 对 Fable 5.1 的 $10/$50，两端都是 5 倍。多数编码工作理性的默认是更便宜的那一档，只在任务确实需要时才够天花板。
- **这张表上最便宜的输出不是用钱付的。** Muse Spark 1.2 的 Contributor 档（输出 $0.20）比两家前沿天花板低 **250 倍**，差价用你 prompt 与 completion 的训练权来结算。对 agent 负载来说，这是账单里占大头那一侧的大幅折扣——也是一个开发者可以在挂着公司仓库的机器上悄悄做掉的披露决策。它还不叠加：60 请求/分的上限对同一次发布主推的并行 subagent 工作流是实打实的限制。可比的数字请用 Standard 档（$1.25 / $4.25）。另外 Muse Code **没有公开仓库**，所以不进本地图的榜单。
- **前沿价格有一部分是促销价，这让本表成为一份活文档。** Sol 的 8 月降价至少延续到 **2026-11-21**，并让它的输出价低于 Opus 5（$20 对 $25）。任何按促销价做的模型选择，都需要在 **11 月复核**一次。详见 [market-events](../market-events.md)。

### 开放权重这一档

上面那张表算的是 token 的钱。这一档算的是**硬件和许可**，账单形状不同，失效方式也不同——你不再按 token 付费，而是不管有没有人用都要付。

| 模型 | 许可 | 总参数 / 激活 | 上下文 | 厂商自报的头条数字 |
| --- | --- | --- | --- | --- |
| [Kimi K3](../agents/kimi-k3.md) | **Kimi K3 License**（自定义） | 2.8T / 896 选 16 | 100 万 | Terminal-Bench 2.1 **88.3**，对比 GPT-5.6 Sol 88.8、Fable 5 88.0 |
| [GLM-5.3](../agents/glm-5.md) | **Apache-2.0** | 未按变体公布 | 100 万（自 5.2 起"扎实"） | Terminal Bench 3.0 开源 SOTA；GLM-5.2 的 Terminal-Bench 2.1 **81.0**、SWE-bench Pro **62.1** |
| [DeepSeek V4-Pro](../agents/deepseek-v4.md) | **MIT** | 1.6T / 49B | 100 万 | SWE-bench Verified **80.6**、Terminal-Bench 2.0 67.9 |
| DeepSeek V4-Flash | **MIT** | 284B / 13B | 100 万 | 给更大思考预算时推理接近 Pro |
| [Qwen3-Coder-Next](../agents/qwen3-coder.md) | 按 checkpoint 而异 | 80B / 约 3B | 256K → 100 万（Yarn） | 在开源模型的 agentic 编码上与 Claude Sonnet 相当 |

这一档改变预算的四件事：

1. **顶端的差距已经小到可以争论了。** 月之暗面自己的对照把 K3 的 Terminal-Bench 2.1 放在 88.3，对 Sol 的 88.8、Fable 5 的 88.0。厂商自测当作主张看待——但这个主张*站得住*本身就是新情况。
2. **真正的分界轴是许可，不是能力。** MIT（DeepSeek）、Apache-2.0（GLM）、自定义（Kimi）、按 checkpoint 而异（Qwen），在能力大体相当的情况下是四种实质不同的法律位置。先看许可，再看 benchmark。
3. **参数量是部署级别，不是规格表上的数字。** 2.8T 和 1.6T 是集群；Qwen3-Coder-Next 的"80B 里激活约 3B"是一台工作站。这个差别决定的真实部署，比它上面任何一行都多。
4. **不存在同口径的 benchmark 行，本页也不会伪造一个。** DeepSeek 报 SWE-bench Verified，Anthropic 报 SWE-bench Pro，OpenAI 报 DeepSWE，智谱报自家 bench。它们是不同的测量；把它们排进同一列排序，是本页能做的最误导的一件事。

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
| Muse Code（Meta）——*不在本图跟踪范围；无公开仓库* | 订阅 **每月 $5–$50**（三档，2026-08-31 起） + API token | Meta | 中——按计划打包，Contributor 价只有在你授权训练时才拿得到 |

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
