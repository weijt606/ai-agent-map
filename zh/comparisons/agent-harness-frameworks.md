# Agent Harness 框架对比

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](agent-harness-frameworks.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../comparisons/agent-harness-frameworks.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

"harness" 是把 LLM 变成 agent 的最小脚手架——循环、工具表面、权限模型、skills 挂载点。这些项目你可以 fork、审计、端到端拥有，而不是照单全收的厂商产品。

六个项目的当前 star 总量见[分类排行](../rankings/README.md)；本页比的是形态，不是体量。

## 一览

| 项目 | 许可证 | 甜点区 | 体量 |
| --- | --- | --- | --- |
| [Pi](../agents/pi.md) | MIT（TS） | 终端优先的 coding harness，LLM 提供商覆盖面广 | 小核心 + 按需 skills/扩展 |
| [jcode](../agents/jcode.md) | MIT（Rust） | 快、占用小、面向多会话工作流的终端 harness，带被动语义记忆 | 精简 Rust 二进制——同类中启动最快、RAM 最低 |
| [OpenHands](../agents/openhands.md) | 开源 | 完整的开源 SWE agent（CLI + GUI + 云选项） | 最重——更接近产品 |
| [SWE-agent](../agents/swe-agent.md) | MIT（Py） | SWE-bench 背后的研究参考实现，单 YAML 配置 | 中等；上游重心转向 mini-swe-agent |
| [mini-swe-agent](../agents/mini-swe-agent.md) | MIT（Py） | ~100 行的接班版；SWE-bench Verified >74% | 极小——一次就能读完 |
| [OpenHarness](../agents/openharness.md) | MIT（Py） | 10 子系统开放 harness，带 anthropics/skills + MCP + 43 工具 | 中等；生产形态，与 [CLI-Anything](../agents/cli-anything.md) 同门 |

## 怎么选

- 按体量选，不按 star 选。合适的 harness 是那个你愿意长期维护其表面积的。
- 想要最小可信的 fork 底座：[mini-swe-agent](../agents/mini-swe-agent.md)。
- 想要生产形态、可自托管的开放 runtime：[OpenHarness](../agents/openharness.md)。
- 想发表 SWE-bench 成绩：[SWE-agent](../agents/swe-agent.md) 是规范参考，mini-swe-agent 是实际接班者。
- 想要终端优先的日常 coding harness：[Pi](../agents/pi.md)；如果优先要速度、多会话下的低 RAM、以及内置被动记忆，选 [jcode](../agents/jcode.md)。
- 想要更完整但仍开源的 SWE agent 产品：[OpenHands](../agents/openhands.md)。
