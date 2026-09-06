# GLM-5.3

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](glm-5.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/glm-5.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：按智谱自己的数字，GLM-5.3 是最强的开放权重编码模型，许可是 Apache-2.0——它同时也是本地图上第一个"漏洞发现能力做到 SOTA、权重可直接下载、前面没有任何闸门"的模型。

> 本页覆盖 GLM-5 系列（5、5.1、5.2、5.3 与 5.3-Flash），它们从同一个仓库发布。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 智谱 / Z.ai |
| 路线 | 开放权重 agentic 模型 |
| 权重 | [`zai-org/GLM-5`](https://github.com/zai-org/GLM-5)——**Apache-2.0** |
| 最适合 | 在自己掌控的权重上跑长周期编码 agent，且要标准宽松许可 |
| 主要代价 | 主要证据来自厂商自测 benchmark；另见下面的网安一节 |
| 上下文 | 扎实的 100 万 token（自 5.2 起） |
| 博客 | https://z.ai/blog/glm-5.3 |

## 为什么要收录

两个理由，第二个才是这篇比一张规格表长的原因。

第一，GLM 是 [ZCode](zcode.md) 底下的模型，而本地图收了产品却没有收让它成立的那个东西。第二，GLM-5.3 是迄今最清楚的一个实例，展示了本地图一直在闭源那侧追踪的一个模式：**厂商会设闸门的能力，这次不带闸门地到了。**

## 什么时候选它

- 你要 **Apache-2.0**。在这里的开放前沿模型里，这是最干净的许可——[Kimi K3](kimi-k3.md) 是自定义许可，[DeepSeek V4](deepseek-v4.md) 是 MIT。
- **编码就是全部的活。** 智谱把 5.3 定位为最强的开放权重编码模型，称其在自家 Z.ai Code Bench 上比 5.2 提升 50%，并在 Terminal Bench 3.0 与 Agents' Last Exam 上达到开源 SOTA。
- 你需要撑得住的长上下文：5.2 引入了智谱称之为*扎实*的 100 万 token 上下文，用 IndexShare 在每四层稀疏注意力间复用同一个 indexer，在 100 万上下文长度下把每 token FLOPs 降低 2.9 倍。
- 你想按任务调开销——5.2 加了多档思考 effort。
- 你想要效率变体：**GLM-5.3-Flash** 是重新训练的基座，采用稀疏加线性的混合注意力架构与 Manifold-Constrained Hyper-Connections（mHC），目标是压低长上下文的 serving 成本。

## 什么时候不选它

- 你需要厂商中立的证据。头条提升是在自家 benchmark 上测的，本地图把它记为厂商主张。
- 你需要同一个模型里的原生多模态——[Kimi K3](kimi-k3.md) 把视觉编码器做进了模型里。
- 你要的是托管产品而不是权重——那是 [ZCode](zcode.md) 和 Z.ai API 平台。
- **你对双用途能力有明确的政策立场。** 见下节；对一些机构这是不部署它的理由，对另一些机构这恰恰是部署它的理由。

## 公布的数字（厂商自测）

| Benchmark | GLM-5.2 | GLM-5.1 | 说明 |
| --- | :-: | :-: | --- |
| Terminal-Bench 2.1 | **81.0** | 62.0 | 智谱称这与 Claude Opus 4.8（85.0）只差几分 |
| SWE-bench Pro | **62.1** | 58.4 | 5.2 发布时的最强开源结果 |

对 5.3，智谱给出的提升口径是"自家代码 benchmark 上比 5.2 提升 50%"加"Terminal Bench 3.0 与 Agents' Last Exam 上开源 SOTA"，而不是一张公开的对位表。[Kimi K3 自己的对照表](kimi-k3.md)把 GLM-5.2 在 Terminal-Bench 2.1 上记为 82.7——与智谱的 81.0 接近，这是两家都有动机去测的数字之间一次有用的交叉验证。

## 关于网安能力的一节

智谱把话说得很直白：随着后训练规模扩大，**网安能力的成长快于他们的预期**——GLM-5.3 在 CyberGym 的漏洞发现上是 SOTA，而且它增益最大的地方在利用链更上游处，在利用类 benchmark 上**比 GLM-5.2 翻倍还多**。

把这个放在本地图同一时间窗里记录的闭源那侧旁边看。[GPT-6 Astra](gpt-6-astra.md) 正式开放的版本**拒绝自己一部分网安能力**，更多能力在 Daybreak Blue 审批之后。Anthropic 的 Mythos 档——与 [Fable 5.1](claude-fable-5.md) 同一底层模型、保护措施更轻——通过 Project Glasswing 只对经审核的机构开放。GLM-5.3 则是：能力在、Apache-2.0 许可、外加一个下载链接。

本地图不对这件事的好坏发表评论，只记录它在选型上的具体后果：**在开放权重这一档，闸门是你的政策，不是厂商的。** 你要是在这里部署，harness 里的审批设计正在替你做闭源厂商本来会替你做的那部分工作——见[观测与评估](../comparisons/observability-and-evals.md)与[能力矩阵](../capabilities/matrix.md)里的审批列。这同时也意味着评估这个模型的防守方，拥有和攻击方一样的访问权限——这正是开放权重那一侧为自己辩护的论点。

## 结论

要在自托管权重上、用标准许可跑一个编码 agent，GLM-5.3 是本地图上最强的那个理由。把自家 benchmark 的说法当作说法看待；把网安能力当作一个活的治理决策而不是脚注——这是本地图第一次不得不为一个可公开下载的模型写下这句话。
