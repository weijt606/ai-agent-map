# DeepSeek V4

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](deepseek-v4.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/deepseek-v4.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：DeepSeek V4 是开放前沿里 MIT 许可的那一端——1.6T 参数、激活 49B、100 万上下文、SWE-bench Verified 80.6——而许可正是重点：它的分数任何有 GPU 的人都能复现。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | DeepSeek AI |
| 路线 | 开放权重 agentic 模型 |
| 权重 | [`deepseek-ai/DeepSeek-V4-Pro`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) 与 [`DeepSeek-V4-Flash`](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash)——**MIT** |
| 最适合 | 想要宽松许可前沿模型的团队，自托管或走 DeepSeek API |
| 主要代价 | Pro 是 1.6T 参数的部署问题；Flash 的存在正是为此 |
| 上下文 | 两个变体都是 100 万 token |
| 公告 | https://api-docs.deepseek.com/news/news260424/ |

## 为什么要收录

开放权重这一档，正是本地图上好几个 agent 实际在跑的东西——[CodeWhale](codewhale.md) 就是围绕 DeepSeek 与 MiMo 模型建的，[ZCode](zcode.md) 也能指向 DeepSeek 的 Anthropic 兼容端点。只收产品不收模型，本地图就回答不了它们底下那个问题。

DeepSeek 同时也是 [DeepSeek Harness](deepseek-harness.md) 的厂商，这意味着现在有一家公司同时坐在本地图的模型层和 harness 层上——而且两边都是 MIT。

## 什么时候选它

- **MIT 是硬要求。** 在这个能力级别上这是最宽松的许可；[Kimi K3](kimi-k3.md) 是自定义许可，[GLM-5.3](glm-5.md) 是 Apache-2.0。
- 你要的是**能复现而不是只能相信**的分数。MIT 下的开放权重意味着任何有足够 GPU 的独立实验室都能重跑评测——这与闭源模型公布一张表，是本质不同的证据位置。
- 你需要**便宜的长上下文**：DeepSeek 声明的设计目标就是以大幅降低的算力与显存成本做到业界领先的长上下文，手段是 token 级压缩与 DeepSeek Sparse Attention。
- 你想要同源的小号：**V4-Flash** 是 284B 总参数 / 13B 激活，DeepSeek 称在给更大思考预算时其推理能力接近 Pro。

## 什么时候不选它

- 你需要模型内原生多模态——视觉编码器在 [Kimi K3](kimi-k3.md) 那边。
- 你要开放档里最强的公布编码数字——那个论点归 [GLM-5.3](glm-5.md) 和 [Kimi K3](kimi-k3.md)，取决于你更看重哪个 benchmark。
- 你想在一般硬件上自托管 Pro。1.6T 总参数是一个集群，不是一台工作站；那个约束下的条目是 [Qwen3-Coder-Next](qwen3-coder.md)。
- 你要厂商托管的 agent 产品——DeepSeek 是分别发布模型和 harness，不是一个成品 agent。

## 架构与数字

| 属性 | V4-Pro | V4-Flash |
| --- | --- | --- |
| 总参数 / 激活参数 | 1.6T / 49B | 284B / 13B |
| 上下文 | 100 万 token | 100 万 token |
| 许可 | MIT | MIT |

| Benchmark | 分数 |
| --- | :-: |
| SWE-bench Verified | **80.6** |
| Terminal-Bench 2.0（agentic） | 67.9 |
| LiveCodeBench（Pro-Max 变体） | 93.5 |
| SimpleQA-Verified（Pro-Max 变体） | 57.9 |

模型卡里的架构要点：MoE 设计，混合注意力结合 **Compressed Sparse Attention** 与 **Heavily Compressed Attention**；用 **Manifold-Constrained Hyper-Connections** 改善信号传播；用 **Muon** 优化器保证训练稳定；预训练超过 **32T token**。DeepSeek 自己的定位是 V4-Pro 在推理、数学、STEM 与编码上领先开源模型，世界知识上仅次于 Gemini-3.1-Pro。

## 这个 SWE-bench 数字该怎么读

SWE-bench Verified 80.6 是本地图模型层里最高的数字——而它和旁边那些数字并不直接可比。Anthropic 公布的是 **SWE-bench Pro**（[Fable 5.1](claude-fable-5.md) 81.2），那是更难的变体；OpenAI 引用的是 **DeepSWE**（[GPT-6 Astra](gpt-6-astra.md) 74.1），根本没给 SWE-bench Verified。三家厂商、三个 benchmark、没有一行是同口径的。本地图记录每家自己的数字，并拒绝去搭那张会让人以为它们是同一次测量的对比表——这就是 2026 年 9 月证据的诚实状态。

## 结论

DeepSeek V4 是开放档里关于许可的那个答案，而"1.6T 参数 + MIT"这句话本身就很不寻常。有集群、要上限就选 Pro；想用五分之一的体量拿到大部分推理能力就选 Flash——并且在有人独立重跑之前，把那个 SWE-bench 数字当作 DeepSeek 在 DeepSeek 选定的 benchmark 上的自测结果，而这件事至少是它的许可允许你去做的。
