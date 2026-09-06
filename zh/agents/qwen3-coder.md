# Qwen3-Coder

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](qwen3-coder.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/qwen3-coder.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：当模型必须塞进你现有硬件时，Qwen3-Coder 就是那条开放权重路线——Qwen3-Coder-Next 每 token 在 80B 里只激活约 3B，而按阿里自己的说法，它在开源模型的 agentic 编码上达到与 Claude Sonnet 相当的水平。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 阿里 / Qwen |
| 路线 | 开放权重 agentic 模型 |
| 权重 | [`QwenLM/Qwen3-Coder`](https://github.com/QwenLM/Qwen3-Coder) · [Hugging Face](https://huggingface.co/collections/Qwen/qwen3-coder-687fc861e53c939e52d52d10) |
| 规格 | Qwen3-Coder-480B-A35B-Instruct、30B-A3B-Instruct，以及 **Qwen3-Coder-Next**（80B-A3B） |
| 最适合 | 本地与成本受限、但仍需要真 agentic 编码的部署 |
| 主要代价 | 不是开放档能力的天花板——它拿上限换体量 |
| 上下文 | 原生 256K，用 Yarn 可扩到 100 万 |
| 博客 | https://qwenlm.github.io/blog/qwen3-coder-next/ |

## 为什么要收录

这条路线上其他模型回答的都是"开放权重能贴近前沿到什么程度"。Qwen3-Coder 回答的是另一个、并且对很多团队更实际的问题：**真正塞得进去的最好 agentic 编码模型是哪个？**

[Kimi K3](kimi-k3.md) 是 2.8T 参数，[DeepSeek V4](deepseek-v4.md) Pro 是 1.6T。那是集群。Qwen3-Coder-Next 建在 Qwen3-Next-80B-A3B-Base 上，用混合注意力加 MoE 的架构，每 token 只激活约 3B 参数——完全是另一个部署级别，这也正是它能和那些 benchmark 上赢过它的模型并列的理由。

## 什么时候选它

- **模型必须跑在你所在的地方**——一台工作站、一个单节点、一个物理隔离环境，或者一个 1.6T 模型达不到的成本上限。
- 你要把它接进现有循环：Qwen 明确支持 **Qwen Code、Cline 和 Claude Code**，并有专门设计的 function call 格式。
- 你需要**仓库级上下文**又不想付前沿账单：原生 256K，用 Yarn 到 100 万。
- 你的代码库很偏门——这条线宣称支持 **358 种编程语言**。
- 你要的是多个尺寸而不是一种部署形态：顶上是 480B-A35B，小部署有 30B-A3B，效率首选是 Next。

## 什么时候不选它

- 你要开放档的能力上限——那是 [Kimi K3](kimi-k3.md) 或 [GLM-5.3](glm-5.md)，取决于看哪个 benchmark。
- 你需要模型内原生视觉。
- 你想从本页拿到许可保证：GitHub 仓库没有暴露标准 license 字段，所以**请在你打算用的那个 Hugging Face checkpoint 上核对许可**——Qwen 这条线历史上对不同尺寸给过不同条款，本地图不替你断言。
- 你要的是成品 agent——那是 Qwen Code，一个本地图尚未收录的独立项目。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 单位能力的效率 | 很强 | Next 在 80B 里激活约 3B；选这条线的理由就在这 |
| Agentic 编码 | 强 | 阿里定位为在开源模型的 agentic 编码与浏览器操作上与 Claude Sonnet 相当 |
| 长上下文 | 强 | 原生 256K，Yarn 到 100 万，面向仓库级理解 |
| harness 兼容性 | 很强 | Qwen Code、Cline、Claude Code；SGLang 与 vLLM 里有专用 tool parser |
| 语言广度 | 很强 | 358 种编程语言 |
| 能力上限 | 中 | 有意不去争开放档的顶端 |
| 许可清晰度 | **按 checkpoint 自行核对** | 本页不断言；部署前请在具体 checkpoint 上确认 |

## 部署注意

function calling 依赖 Qwen 在 **SGLang** 与 **vLLM** 里的 tool parser，而且特殊 token 及其 token id 为了与 Qwen3 保持一致做过更新——所以务必用新的 tokenizer。这类细节在 agent 循环里会变成一次无声的工具调用失败，所以它出现在本页，而不是被留在模型卡里。

## 结论

Qwen3-Coder 是开放档里那个务实选项：上限不是最高，但它的部署故事是一台机器而不是一个集群，而且在本地图已经覆盖的 harness 里有一等支持。如果你的约束是硬件或成本而不是能力，就从这里开始、再往上比——并且在上线前，读一下你那个具体 checkpoint 的许可。
