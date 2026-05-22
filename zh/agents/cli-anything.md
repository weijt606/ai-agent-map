# CLI-Anything

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](cli-anything.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/cli-anything.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：CLI-Anything 是 HKUDS（香港大学数据科学组）做的一个框架，它会为任意软件自动生成基于 Click 的命令行接口——立场很明确：「明天的用户是 agent」，所以它直接把人类设计的软件重写成 agent 友好的 CLI。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | HKUDS（香港大学数据科学组） |
| 路线 | Runtime & tools——agent-native 软件桥接层 |
| 开源 | 是（Apache-2.0） |
| 适合谁 | 需要 agent 控制那些没有 API 的软件（创作工具、办公套件、科研应用）的团队 |
| 主要代价 | 生成的 CLI 要跟着上游应用持续维护；pipeline 还在成熟中 |
| GitHub 仓库 | https://github.com/HKUDS/CLI-Anything |

## 什么时候选它

- 你要 agent 操作 Blender、GIMP、LibreOffice、QGIS、FreeCAD、ComfyUI、Calibre 这种软件，又不想写 GUI 自动化。
- 你更想要结构化 CLI 控制（JSON 输出、`--help` 自省、REPL 模式），而不是脆弱的截屏抓取。
- 你愿意为目标应用跑一次 7 阶段 pipeline（analyze → design → implement → test → document → publish）。
- 你希望每个生成的 CLI 都作为正式 PyPI 包发布，并附带 agent 可读的 SKILL.md。

## 什么时候不选

- 目标软件本身已经有可用 API 或 CLI——直接用上游就行。
- 价值点在"视觉交互"而不是"状态变化"——实时游戏、视频剪辑、动画时间轴这类不适合。
- 你要的是打磨好的生产级产品。CLI-Anything 测试覆盖（18+ 应用上 2330+ 测试通过）已经不弱，但仍是学术组项目，定位还在成熟。

## 能力轮廓

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| CLI 自动生成 | 非常强 | 7 阶段 pipeline，Click + REPL + JSON 输出模式 |
| 覆盖宽度 | 强 | 已经为 18+ 专业应用生成了可用 CLI |
| Agent 表面 | 强 | `--help` 自省、`--json` 输出、结构化错误、SKILL.md 文档 |
| 长期维护 | 待观察 | 上游应用演进后生成的 CLI 需要重新验证 |
| 生产化 | 中等 | Apache-2.0 + HKUDS 学术组维护，不是商业厂商 |

## 使用成本

复杂度：中到高。每个目标应用跑一次 pipeline，但生成的每个 CLI 都是独立资产，需要持续维护。最适合"我要 agent 稳定地驱动这个复杂桌面应用"这种场景，对"我只是要调一个 REST API"过于重型。

## 底线

CLI-Anything 把通常的思路反转过来——不是教 agent 怎么点 GUI，而是把软件重写成 agent 不必点 GUI 就能用。已经生成的 18+ CLI（创作、办公、科研、AI/ML 工具）说明这不是空想；Click + REPL + JSON 输出的组合是干净的 agent 表面。真正的检验在于：pipeline 能不能为你自己的目标应用产出一个可维护的 CLI——如果能，那它相对 GUI 自动化就有明显优势。
