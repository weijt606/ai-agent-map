# 基准与计费方式

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](benchmarks-and-billing.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/benchmarks-and-billing.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

[热度榜](../README.md#近期热门榜)追踪流行度，[能力矩阵](../capabilities/matrix.md)追踪形态。本页追踪它俩都不显示的内容：**编码 agent 背后的模型到底多能打，以及每个 agent 怎么计费。**

本图不列价格，也不比较价格。价格变动频繁，请以各厂商自己的价格页为准。

模型时间线见[市场脉搏](../README.md#市场脉搏)和[市场事件](../market-events.md)。

## 前沿编码模型

**Artificial Analysis 编码 agent 指数**是本地图追踪的跨模型能力数字。

| 模型 | AA 编码 agent 指数 | 其他 benchmark | 备注 |
| --- | :-: | --- | --- |
| **GPT-6 Astra**（OpenAI） | — | DeepSWE v1.1 74.1% | **2026-09-03。**正式开放的版本**会拒绝自己一部分网安能力** |
| **Claude Opus 5.5**（Anthropic） | — | **Terminal-Bench 4.0 66.4%** | **2026-09-22。**Anthropic 的说法是它在多数工作上达到 Fable 5.1 的水平，输出比 Opus 5 快 30%。1M 上下文。公布的九项基准全高于 Opus 5；在 AutomationBench（40.0 对 41.4）与 Terminal-Bench-Science（58.7 对 64.6）上落后 [GPT-6 Astra](../agents/gpt-6-astra.md)。当天就成为 [Claude Code](../agents/claude-code.md) `v2.1.280` 里默认的 Opus 模型 |
| **Muse Wonder**（Meta） | — | — | **2026-10-12**——本表晚一个窗口才记下。Meta 新的 API 顶档模型，主打"前沿编码、长时运行 agent 与高级电脑操作"，100 万上下文。更大的 Muse Wonder Full 根本不上 API，只在 Muse Code 的 Power 与 Maximum 订阅档里提供 |
| **Claude Fable 5.1**（Anthropic） | — | **SWE-bench Pro 81.2** | **2026-09-01。**1M 上下文。按额度计费，不含在订阅内 |
| **GPT-6.1 Sol**（OpenAI） | — | — | **2026-09-29。**同日起成为 [Codex CLI](../agents/codex.md) `rust-v0.159.1` 的打包默认，替掉 Astra |
| **Claude Sonnet 5.5**（Anthropic） | — | **Terminal-Bench 4.0 70.6%** | **2026-09-28。**比 Sonnet 5 快 30% 以上。它的 Terminal-Bench 4.0 **高于 Opus 5.5 的 66.4%**；在其他共有基准上都落后于 Opus 5.5。同日成为 [Claude Code](../agents/claude-code.md) `2.1.284` 的默认 Sonnet 模型，1M 上下文 |
| **Gemini 4 Argon**（Google） | — | DeepSWE v1.1 77.9%；AutomationBench 51.3% | **2026-10-13 开放付费 API**（`gemini-4-argon`），9 月 30 日发布时还在网安防御者闸门之后；无防护版本仍留在 Google 的 Fairwind 计划里。只有隐式缓存；不对免费层开放；输出上限 1M。Google 的基准表不是和其他厂商同场跑的 |
| **GPT-6 Sol**（OpenAI） | — | — | **2026-09-22。**GPT-6 的中档。**它不是 GPT-5.6 Sol** —— 两代同名，写在配置文件里是实打实的坑 |
| **GPT-5.6 Sol**（OpenAI） | **80** | — | 最近一次测得的指数第一 |
| **Claude Fable 5**（Anthropic） | **77.2** | — | 9 月 1 日被 5.1 接棒；作为指数参照点保留 |
| **GPT-5.5**（OpenAI） | **76.4** | SWE-Bench Pro 58.6% | 2026 春季参照模型，已隔两代。**2026-10-14 起从 Codex 与 ChatGPT 下线（限 ChatGPT 账号登录）**；API 与用 API key 登录的 Codex 会话不受影响 |
| **Claude Opus 5**（Anthropic） | — | SWE-bench Pro 略低于 Fable 5.1 的 81.2 | 9 月 22 日之前是 Claude Code 的默认 Opus，此后由 **Opus 5.5** 接替；仍可选用。1M 上下文既是默认也是上限 |
| **Claude Opus 4.8**（Anthropic） | **72.5** | — | 7 月 24 日被 Opus 5 接棒；仍是请求触发安全分类器时的自动回退 |
| **Claude Sonnet 5**（Anthropic） | — | — | 9 月 28 日起 Claude Code 的默认 Sonnet 换成了 Sonnet 5.5 |
| **GPT-5.6 Terra**（OpenAI） | — | — | 中档，2026-07-09 |
| **GPT-6.1 Terra**（OpenAI） | — | — | **2026-10-26。**"快速、高效"，主打视觉推理与电脑操作；105 万上下文。当天进入 Plus 及以上档的 Codex 与 ChatGPT Work，**不是默认模型**。本地图读不到 OpenAI 的发布文章，因此不记基准数字 |
| **Claude Haiku 5.5**（Anthropic） | — | — | **2026-10-07**（`claude-haiku-5-5`）。1M 上下文。它的 tokenizer 对同一段文本比 Haiku 4.5 多算约 30% token。API 侧默认的 Haiku 模型；Claude Code `v2.1.293` 同日加入，但没有换自己的默认 |
| **GPT-6 Luna**（OpenAI） | — | — | **2026-09-22。**和 Sol 一样存在跨代撞名 |
| **GPT-5.6 Luna**（OpenAI） | — | — | GPT-5.6 的最低一档 |
| **Muse Spark 1.3**（Meta） | — | — | Muse Code 背后的编码模型，**2026-08-31** 转正。没有本地图愿意照抄的指数数字。Contributor 档**允许 Meta 用你的 prompt 与 completion 训练未来模型**，上限 60 请求/分，Standard 档为 3,000。这是治理决策 |

> SWE-Bench Pro 参照点：Claude Opus 4.7 得 64.3%，高于 GPT-5.5 的 58.6%。破折号（—）表示本图未追踪该数字，不是零——**Astra、Fable 5.1、Opus 5 目前没有本地图愿意照抄的指数数字**，本地图也不用第三方榜单去填这个空。benchmark 取自各 profile（[Fable 5.1](../agents/claude-fable-5.md)、[Opus 5](../agents/claude-opus-5.md)、[GPT-6 Astra](../agents/gpt-6-astra.md)、[GPT-5.5](../agents/gpt-5.5.md)）与 [market-events](../market-events.md)。指数位次会变，请以来源为准。

Muse Code **没有公开仓库**，所以不进本地图的榜单。

### 开放权重这一档

这些模型要自己托管，所以硬件和许可条款决定你能不能用。

| 模型 | 许可 | 总参数 / 激活 | 上下文 | 厂商自报的头条数字 |
| --- | --- | --- | --- | --- |
| [Kimi K3](../agents/kimi-k3.md) | **Kimi K3 License**（自定义） | 2.8T / 896 选 16 | 100 万 | Terminal-Bench 2.1 **88.3**，对比 GPT-5.6 Sol 88.8、Fable 5 88.0 |
| [GLM-5.3](../agents/glm-5.md) | **Apache-2.0** | 未按变体公布 | 100 万（自 5.2 起"扎实"） | Terminal Bench 3.0 开源 SOTA；GLM-5.2 的 Terminal-Bench 2.1 **81.0**、SWE-bench Pro **62.1** |
| [DeepSeek V4-Pro](../agents/deepseek-v4.md) | **MIT** | 1.6T / 49B | 100 万 | SWE-bench Verified **80.6**、Terminal-Bench 2.0 67.9 |
| DeepSeek V4-Flash | **MIT** | 284B / 13B | 100 万 | 给更大思考预算时推理接近 Pro。小版本更新 **V4.1-Flash-1017**（2026-10-17）：按 DeepSeek 的说法，比 V4.1-Flash 输出更短、benchmark 更好 |
| Muse Spark Open（Meta） | **Muse Model License**（自定义，"有限商用条款"） | 816B / 42B | 100 万 | 2026-10-15。Meta 称其为"迄今最强的美国开放权重模型"；针对 Mac Studio M5 Ultra 上的 MLX 做了优化 |
| [Qwen3-Coder-Next](../agents/qwen3-coder.md) | 按 checkpoint 而异 | 80B / 约 3B | 256K → 100 万（Yarn） | 在开源模型的 agentic 编码上与 Claude Sonnet 相当 |

这一档改变的四件事：

1. **顶端的差距已经小到可以争论了。** 月之暗面自己的对照把 K3 的 Terminal-Bench 2.1 放在 88.3，对 Sol 的 88.8、Fable 5 的 88.0。厂商自测当作主张看待——但这个主张*站得住*本身就是新情况。
2. **真正的分界轴是许可，不是能力。** MIT（DeepSeek）、Apache-2.0（GLM）、自定义（Kimi，以及 10 月 15 日起 Meta 的 Muse Model License）、按 checkpoint 而异（Qwen），在能力大体相当的情况下是四种实质不同的法律位置。先看许可，再看 benchmark。
3. **参数量是部署级别，不是规格表上的数字。** 2.8T 和 1.6T 是集群；Qwen3-Coder-Next 的"80B 里激活约 3B"是一台工作站。这个差别决定的真实部署，比它上面任何一行都多。
4. **不存在同口径的 benchmark 行，本页也不会伪造一个。** DeepSeek 报 SWE-bench Verified，Anthropic 报 SWE-bench Pro，OpenAI 报 DeepSWE，智谱报自家 bench。它们是不同的测量；把它们排进同一列排序，是本页能做的最误导的一件事。

## 编码 agent 怎么计费

| Agent | 计费方式 | 你付给 |
| --- | --- | --- |
| [Claude Code](../agents/claude-code.md) | 订阅（Pro/Max） + Fable 5.1 **按量额度** | Anthropic |
| [Codex](../agents/codex.md) | 打包进 ChatGPT 计划（Free → Pro）；重度 CLI 走 API | OpenAI |
| [Cursor](../agents/cursor.md) | 订阅 / 席位 | Cursor |
| [GitHub Copilot](../agents/github-copilot.md) | 订阅 / 席位；随 GitHub Enterprise 提供时从第一个请求起计量（2026-10-28） | GitHub |
| [Devin](../agents/devin.md) | 托管席位 + 用量 | Cognition |
| [Aider](../agents/aider.md)、[Cline](../agents/cline.md)、[Continue](../agents/continue.md) | **开源，自带 key** | 直接付模型 provider |
| [Pi](../agents/pi.md)、[jcode](../agents/jcode.md)、[OpenHands](../agents/openhands.md) | **开源 harness，自带 provider** | 直接付模型 provider |
| [Kimi Code](../agents/kimi-code.md)、[MiMoCode](../agents/mimocode.md)、[CodeWhale](../agents/codewhale.md) | 开源，厂商模型 | Moonshot / 小米 API；CodeWhale 任意 provider（默认 DeepSeek） |
| Muse Code（Meta）——*不在本图跟踪范围；无公开仓库* | 订阅计划（Everyday、High、Power、Maximum） + API token | Meta |

## 三种计费形态

- **开源 agent，你直接付模型 provider。** Aider、Cline、Pi、jcode、OpenHands 和各 harness 安装不收许可费，你把它们指向一个模型 API。速率限制和 key 都归你管。
- **打包订阅。** Claude Code、Codex、Cursor、Copilot 把模型用量折进一个计划，重度用量溢出到按量或 API。上限是计划的合理使用条款。
- **按量额度 / 托管用量。** Claude Code 里的 Fable 5.1 额度，以及 Devin 这类托管产品，按实际干的活计费。

还有一层**运维负担**：RAM、启动时间、自托管的运维工作。性能优先的 harness 把这点摆到明面——比如 [jcode](../agents/jcode.md) 就主打同类最低 RAM、最快启动，好让很多并行会话跑起来。每个 profile 的"使用成本"一节按项目讲这点。

按维度看能力形态见[能力矩阵](../capabilities/matrix.md)；模型层时间线见[市场事件](../market-events.md)。
