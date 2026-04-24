# DSPy

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](dspy.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/dspy.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：DSPy 用声明式 Python 模块替代手写 prompt，通过编译器自动优化——编程语言模型，而不是手调 prompt。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Stanford NLP / Omar Khattab |
| 路线 | 程序化 prompt 优化框架 |
| 是否开源 | 是，MIT |
| 最适合 | 想让编译器自动找最优 prompt，而不是手工调试的团队 |
| 主要代价 | 学习曲线陡；编译后的 prompt 调试不够透明 |
| 官网 | https://dspy.ai |
| GitHub 仓库 | https://github.com/stanfordnlp/dspy |

## 什么时候选它

- 你想让编译器自动找最优 few-shot 示例和指令，而不是手写 prompt。
- 你需要可组合的 LM pipeline——像 PyTorch layer 一样串联 ChainOfThought、ReAct、ProgramOfThought 模块。
- 你在意评估驱动的优化，内置 assertion 和 metrics。
- 你想换模型时不重写 prompt——DSPy 会为新模型重新编译。

## 什么时候别选

- 你只有一个简单的单 prompt 任务。DSPy 杀鸡用牛刀。
- 你需要生产部署工具链——tracing、鉴权、限流。LangChain 在这方面更成熟。
- 你想要可视化构建器或低代码体验。
- 你要的是成品 agent 产品，不是研究级优化框架。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Prompt 优化 | 很强 | 核心设计——编译器搜索最优 prompt |
| 可组合 pipeline | 很强 | 声明式模块，像 PyTorch layer 一样串联 |
| 评估 / metrics | 强 | 内置 assertion 和基于 metric 的优化 |
| 模型无关 | 强 | OpenAI、Anthropic、Ollama、vLLM 等 |
| 生产部署工具 | 弱 | 不如 LangChain 的部署基础设施成熟 |
| 可视化构建器 | 无 | 纯 Python，代码优先 |

## 使用代价

复杂度 High。DSPy 和 prompt engineering 有本质区别——需要理解编译器、签名和优化循环。回报在于大规模 LM 调用的场景，prompt 优化能直接降成本、提质量。但学习曲线是真实的。

## 最后一句

DSPy 不是 LangChain 或 LlamaIndex 的竞品——它是互补的。它优化的是其他框架所执行的 prompt。当你想让机器找到比你手写更好的 prompt 时，选它。
