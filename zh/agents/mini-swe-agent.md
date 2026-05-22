# mini-swe-agent

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](mini-swe-agent.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/mini-swe-agent.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：mini-swe-agent 是一个故意做得很小（约 100 行 Python）但在 SWE-bench Verified 上拿到 >74% 的 coding agent——是上游团队亲手指定的 [SWE-agent](swe-agent.md) 接班版本。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | Princeton + Stanford NLP（和 [SWE-agent](swe-agent.md) 同一团队） |
| 路线 | Agent harness 框架——极简参考 |
| 开源 | 是（MIT，Python） |
| 适合谁 | 想要最小可信 harness——一坐能读完、一下午能改完 |
| 主要代价 | "没有大 config、没有大型 monorepo"是设计立场——要打磨或要全功能就不是这个项目 |
| GitHub 仓库 | https://github.com/SWE-agent/mini-swe-agent |

## 什么时候选它

- 你想一次性读完并理解整个 agent loop——整个项目只有 ~100 行 Python。
- 你想要一个可信的 SWE-bench 基线：SWE-bench Verified >74%，和重得多的系统相比都有竞争力。
- 你想要上游推荐的 SWE-agent 接班版本——SWE-agent 自己的 README 写得很清楚：「主要开发精力」在这里。
- 你的工作流是 fork 改而不是 config 调——半天就能把整个东西重写。

## 什么时候不选

- 你要的是生产级 CLI，自带工具、插件、skills——[OpenHarness](openharness.md)、[Pi](pi.md)、[OpenHands](openhands.md) 更厚但更完整。
- 你要 YAML 驱动的研究配置表面——那仍然是 [SWE-agent](swe-agent.md) 的强项。
- 你想开箱即用对接 anthropics/skills 或 MCP——mini-swe-agent 故意省掉了这一层。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 可读性 | 非常强 | 整个 agent loop 就是一个短文件 |
| SWE-bench Verified 分数 | 强 | 报告 >74%，和很多重型系统打平 |
| 可 fork 性 | 非常强 | "radically simple"就是它的设计哲学 |
| 工具 / skill 生态 | 故意很轻 | 这是设计——其他部分由你自己补 |
| 长期可运维性 | 待观察 | 项目较新（2025-06），上游维护活跃但年头不长 |

## 使用成本

复杂度：低。整个代码库小到可以审计一遍。代价是"没有的那些东西"——没有托管 config 层、没有工具插件生态、没有 UI。要生产辅助就自己写，或选别的 harness。

## 底线

mini-swe-agent 是 SWE-bench 原班作者自己日常在用的版本。和 [SWE-agent](swe-agent.md) 相比，它牺牲了可配置性换来彻底的简洁——而 SWE-bench Verified >74% 让这笔交易合理。如果你想在采用前把整个 harness 完全看懂，这是最干净的路。如果你想要一个开箱即用、带权限、带 MCP、带 skills 和工具生态的 CLI，看 [OpenHarness](openharness.md) 或 [Pi](pi.md)。
