---
name: "Cline"
vendor: "Cline"
category: "execution"
open_source: true
complexity: "medium"
verification: "verified-public-project"
last_reviewed: "2026-04-09"
description: "Approval-first editor-native coding agent with terminal, browser, and MCP capabilities."
description_zh: "审批优先的编辑器内 coding agent，提供终端、浏览器和 MCP 能力。"
homepage: "https://docs.cline.bot/"
repo: "https://github.com/cline/cline"
---

# Cline

中文：
Cline 的核心卖点不是“完全自治”，而是“高能力 + 强审批”。它把终端、浏览器、文件编辑和 MCP 放进编辑器里，但每一步都保留人为把关。

English:
Cline is not optimized for total autonomy. Its core proposition is high capability plus strong approval control. It brings terminal, browser, file editing, and MCP into the editor while keeping humans in the loop.

## 基本信息 | Snapshot

| Field | Value |
| --- | --- |
| Name | Cline |
| Vendor | Cline |
| Category | execution |
| Open Source | Yes |
| Complexity | Medium |
| Delivery Model | Editor-native extension plus CLI path |
| Homepage | https://docs.cline.bot/ |
| Repo | https://github.com/cline/cline |

## 能力画像 | Capability Profile

| Capability | Assessment | Notes |
| --- | --- | --- |
| File editing | Strong | Public docs emphasize direct file create/edit flows with diffs and error monitoring. |
| Terminal execution | Strong | Cline can run commands and monitor long-running output. |
| Browser use | Strong | Browser-based testing and UI debugging are explicit documented capabilities. |
| MCP extensibility | Strong | Cline can connect to MCP servers and even help create custom tools. |
| Human approval | Very strong | Public docs emphasize explicit approval for every action. |
| Deployment control | Medium | Great for editor-based local workflows, less about independent cloud task orchestration. |

## 最适合的使用场景 | Best Use Cases

- 希望 agent 很强，但必须保留每一步审批。 Best for users who want a powerful agent while preserving approval on every step.
- 需要在编辑器里同时做改代码、跑命令、开浏览器调试。 Good when you need code edits, terminal commands, and browser debugging in one surface.
- 想通过 MCP 扩展专用工具能力。 Useful when you want to extend the agent with custom MCP tooling.

## 不适合的场景 | Not Suitable For

- 想把任务完全后台化，不想频繁参与。 Not ideal if you want fully detached background execution.
- 不希望人工审批带来摩擦。 Weak fit if approval overhead is unacceptable.
- 需要大型团队级别的统一云端代理平台。 Less suitable if you want a more centrally managed cloud agent platform.

## 复杂度判断 | Complexity

中文：
复杂度为 Medium。技术能力很强，但真正成本在于审批频率和操作节奏，而不是安装本身。

English:
Complexity is Medium. The real cost is approval frequency and operating rhythm, not installation difficulty.

## 实战备注 | Real-World Usage Notes

- 对个人开发者和小团队来说，Cline 很适合当“强控制模式”的 coding agent。 For individuals and small teams, Cline works well as a high-control coding agent.
- 如果你重视“看着 agent 动手，但不让它乱来”，Cline 的定位非常清晰。 If you care about watching the agent work without giving it unchecked freedom, Cline is very clear in its positioning.
- 对长时间后台任务和多 agent orchestration，它不是最自然的选择。 It is not the most natural fit for long background tasks or multi-agent orchestration.