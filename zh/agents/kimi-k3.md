# Kimi K3

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](kimi-k3.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/kimi-k3.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Kimi K3 是第一个开放的 3T 级模型——2.8T 参数、原生多模态、100 万上下文——而且按它自己公布的对照表，在 agentic 编码上它是在和闭源前沿互有胜负，不是落后。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 月之暗面（Moonshot AI） |
| 路线 | 开放权重 agentic 模型 |
| 权重 | [`MoonshotAI/Kimi-K3`](https://github.com/MoonshotAI/Kimi-K3) · [Hugging Face](https://huggingface.co/moonshotai) |
| 许可 | **Kimi K3 License**——自定义许可，不是 OSI 标准许可；商用部署前务必先读 |
| 最适合 | 想要前沿级 agentic 能力、同时把权重握在自己手里的团队 |
| 主要代价 | 2.8T 参数首先是个部署问题，其次才是许可问题 |
| 上下文 | 1,048,576 token；文本与图像 |
| 技术博客 | https://www.kimi.com/blog/kimi-k3 |

## 为什么要收录

本地图的模型层此前只有两家闭源厂商，留下一个没被回答的问题：**自己托管权重，到底要放弃多少？** 2025 年大部分时间里，诚实的答案是"放弃很多"。K3 是让这个答案变得可争论的那个条目。

它同时也是 [Kimi Work](kimi-work.md) 底下的模型、[Kimi Code](kimi-code.md) 的近亲，所以它补上了本地图已经有三分之二的那个闭环。

## 什么时候选它

- 你要的是**开放的前沿权重**。月之暗面的说法就是如此：完整发布权重，让前沿智能可用于研究、部署与进一步创新。
- 你的 agent 要在**大仓库上跑长会话**。它声明的设计点正是在极少人工监督下维持长工程会话、在庞大代码库里导航、调度终端工具。
- 你需要**原生视觉进入循环**，而不是外挂一个看图说话：MoonViT-V2 编码器（401M）是模型的一部分，厂商举的例子包括视觉在环的游戏开发与 CAD。
- 你需要真正的长上下文——原生 100 万 token。
- 你在意 serving 效率：量化感知训练直接给出 MXFP4 权重配 MXFP8 激活。

## 什么时候不选它

- **许可是自定义的。** 它是 "Kimi K3 License"，不是 Apache-2.0 或 MIT。如果你的硬要求是标准宽松许可，要对比的是 [DeepSeek V4](deepseek-v4.md)（MIT）和 [GLM-5.3](glm-5.md)（Apache-2.0）。
- **你部署不起。** 2.8T 总参数、每 token 从 896 个专家里激活 16 个，是一次严肃的部署；如果开放权重的意义本来是本地跑，请看 [Qwen3-Coder-Next](qwen3-coder.md)。
- 你要的是带支持的托管产品——这是一次权重发布。
- 你需要第三方中立的 benchmark 叙述：下面那张表是月之暗面自己做的。

## 架构

| 属性 | 数值 |
| --- | --- |
| 总参数 | 2.8T（按月之暗面说法，首个开放的 3T 级模型） |
| 专家 | 896 个，每 token 选 16 个，另有 2 个共享专家 |
| 注意力 | Kimi Delta Attention（KDA）与 Gated MLA，加 Attention Residuals |
| 上下文长度 | 1,048,576 token |
| 视觉编码器 | MoonViT-V2，401M 参数 |
| 量化 | MXFP4 权重 / MXFP8 激活，量化感知训练 |
| 模态 | 文本与图像 |

月之暗面把**相对 Kimi K2 约 2.5 倍的整体扩展效率提升**归因于支撑这套专家配置的 Stable LatentMoE 框架。

## 公布的对照

以下是**月之暗面自己的数字**，取自模型 README，均为 max 档。本地图转载它，是因为"一家厂商在具名 benchmark 上对比具名闭源模型"是一个可核对的主张——不是因为它中立。

| Benchmark | Kimi K3 | Claude Fable 5 | GPT-5.6 Sol | Claude Opus 4.8 | GLM-5.2 |
| --- | :-: | :-: | :-: | :-: | :-: |
| Terminal-Bench 2.1 | **88.3** | 88.0 | 88.8 | 84.6 | 82.7 |
| SWE-Marathon | **42.0** | 35.0 | 39.0 | 40.0 | 13.0 |
| ProgramBench | **77.8** | 76.8 | 77.6 | 71.9 | 63.7 |
| FrontierSWE | 81.2 | **86.6** | 71.3 | 66.7 | 67.3 |
| DeepSWE | 67.5 | 70.0 | **73.0** | 59.0 | 46.2 |
| GPQA Diamond | 93.5 | 92.6 | **94.1** | 91.0 | 91.2 |

值得读的是形状：在长周期 agentic 工作上（Terminal-Bench、SWE-Marathon、ProgramBench），K3 与闭源前沿持平或领先；而在单发的软件工程 benchmark 上（DeepSWE、FrontierSWE），它落在 Fable 5 或 Sol 后面。这个区分比一个总排名有用得多，而且它对得上你实际会怎么部署它。

## 与月之暗面产品的关系

K3 是模型。[Kimi Code](kimi-code.md) 是终端编码 agent，[Kimi Work](kimi-work.md) 是桌面知识工作 agent。想要月之暗面那套循环就拿产品；本页面向的是"把一个模型接进自己系统"的情形——接进什么，见 [harness 路线](../comparisons/agent-harness-frameworks.md)。

## 结论

K3 是迄今最有力的论据，说明开放权重档是市场顶端的真实选项，而不是省钱的退路——但有两条比 benchmark 表更重要的保留：许可是自定义的，以及 2.8T 参数意味着 serving 账单取代了 token 账单。如果许可纯净度重要，去比 [DeepSeek V4](deepseek-v4.md)；如果编码就是全部的活，去比 [GLM-5.3](glm-5.md)。
