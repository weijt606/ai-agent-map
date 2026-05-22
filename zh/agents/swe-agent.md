# SWE-agent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](swe-agent.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/swe-agent.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：SWE-agent 是 SWE-bench 背后的原始研究 harness——Princeton + Stanford 给"丢一个工具接口给 LLM、让它去修真 GitHub issue"这件事做的参考实现。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | Princeton + Stanford NLP（John Yang、Carlos Jimenez、Kilian Lieret 等） |
| 路线 | Agent harness 框架——研究参考 |
| 开源 | 是（MIT，Python） |
| 适合谁 | 做 SWE-bench / SWE-bench-Verified 研究、想要 single-YAML 配置可改的研究者和工程师 |
| 主要代价 | 上游开发重心已经转到 [mini-swe-agent](mini-swe-agent.md)；SWE-agent 现在是更重的历史参考 |
| GitHub 仓库 | https://github.com/SWE-agent/SWE-agent |

## 什么时候选它

- 你在做 SWE-bench / SWE-bench-Verified 研究，需要原论文用的那套 harness。
- 你想要一份可 hack 的 single-YAML 配置，prompting 策略、工具集和命令表面都在同一个文件里。
- 你需要 EnIGMA 这类攻击型安全 / CTF 任务的扩展——SWE-agent 是这条线的标准底座。
- 你在写论文要为方法论选型辩护，需要开源 harness 里被引用最多的那一个。

## 什么时候不选

- 你要的是最精简的 harness——同一个团队的 [mini-swe-agent](mini-swe-agent.md) 已经是接班产品，上游 README 自己写了"大部分当前开发精力在 mini-swe-agent"。
- 你想要打磨过的成品 UI——SWE-agent 是研究工具，不是开发者产品。
- 你要的是开箱即用、provider 覆盖广、工具生态丰富——[OpenHarness](openharness.md) 和 [Pi](pi.md) 在日常使用上更顺手。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 研究可复现 | 非常强 | SWE-bench 标准参考 harness |
| 配置表面 | 非常强 | 一份 YAML 控制 prompting、tools、agent 行为 |
| 多用途 | 强 | GitHub issue 修复、CTF（EnIGMA）、编程竞赛 |
| 模型 provider 灵活度 | 强 | 支持任意 LM provider |
| 上游维护 | 减速中 | 主要开发精力已经转移到 mini-swe-agent |

## 使用成本

复杂度：中。single-YAML 设计让做实验/改 prompt 都很便宜，但代码比 mini-swe-agent 重，文档也是研究级。你买的不是打磨，而是"被论文引用最多的参考实现"。

## 底线

SWE-agent 代表了"先按研究项目设计、不是先按开发者产品设计"的 harness。如果你要发 SWE-bench 数字、做安全 agent 研究、或者要在方法论上为基线背书，这是标准起点。如果你只是想要一个轻一点的、日常能跑的 harness，按上游自己的推荐去看 [mini-swe-agent](mini-swe-agent.md)。
