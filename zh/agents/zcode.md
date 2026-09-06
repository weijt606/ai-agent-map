# ZCode

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](zcode.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/zcode.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：ZCode 是智谱的桌面端 agentic 开发环境——它是一个 GUI 任务台而不是编辑器，围绕 GLM-5.3 调校，带"Goal"这种长周期任务，人不在机器前也能从微信、飞书、Telegram 上盯着它跑。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 智谱 / Z.ai |
| 路线 | 直接执行（桌面 GUI，不是终端 CLI，也不是编辑器插件） |
| 是否开源 | 否——客户端闭源；GLM 模型线单独开放权重 |
| 最适合 | GLM 优先的团队，想要有可见任务面、并能远程查看进度的长跑编码任务 |
| 主要代价 | 订阅收费；最强能力绑在智谱自家模型上 |
| 当前版本 | 3.11.2 |
| 官网 | https://zcode.z.ai |

## 为什么要收录

本地图在国产厂商这一侧原本有个实打实的洞：它收了 [Kimi Code](kimi-code.md)、[MiMoCode](mimocode.md)、[CodeWhale](codewhale.md)、[CoStrict](costrict.md) 和 [Open Code Review](open-code-review.md)，全都是终端或 CI 形态，而没有一个是 GLM 优先的团队真正会打开的那个工具。ZCode 就是那个工具，而且形态和上面所有条目都不同：**一个以任务而非文件为主对象的桌面应用**。

这个区分正是它进"直接执行"路线、而不是和 [Cursor](cursor.md)、[Windsurf](windsurf.md) 放在一起的原因。编辑器中心那条路线，讲的是编辑器始终是重心的产品；而在 ZCode 里，重心是你交出去、然后回来查看的一个目标。

## 什么时候选它

- 你已经在用 **GLM**。产品声明的设计点就是与 GLM-5.3 深度集成，另有 GLM-5.3-Flash 负责截图与图像理解。
- 你的任务是**长周期**的。"Goal" 这个功能的存在意义，就是让一个多步目标在长时间运行中被兜住，而不是一来一回的 prompt-and-diff。
- 你想**用手机盯进度**。通过微信、飞书、Telegram 远程调用是一等功能，不是事后集成——这和一个随 SSH 会话一起死掉的终端 agent 是完全不同的操作模型。
- 你想要一个覆盖 agent 工作的 GUI，又不想连带接受某个编辑器对工作流的全部主张。
- 你需要 Linux 桌面覆盖：除 macOS（Apple Silicon 与 Intel）、Windows（x64/ARM64）外，还有 `.deb`、`.rpm`、`.AppImage` 构建。

## 什么时候不选它

- **你想读代码。** 客户端闭源。如果开源是这条路线上的硬要求，[Kimi Code](kimi-code.md) 和 [CodeWhale](codewhale.md) 是可比的国产选项。
- 你是终端优先的开发者。这是桌面应用；CLI 循环是另一种人机工程学下注——见[终端编码 CLI 对比](../comparisons/coding-cli-agents.md)。
- 你不跑 GLM。它能接别的后端（见下），但调校、定价和厂商的注意力都在自家模型线上。
- 你需要成熟的治理故事。这是一个发布节奏很快的年轻产品——撰写时是 3.11.2。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 长周期执行 | 强 | "Goal" 是产品用来承载多步目标的核心原语 |
| 远程操作 | 很强 | 从微信、飞书、Telegram 驱动并监控运行 |
| 多模态输入 | 强 | GLM-5.3-Flash 处理截图与图像分析 |
| 多 agent | 强 | 围绕多个 agent 协作完成同一目标来定位 |
| 平台覆盖 | 强 | macOS（双架构）、Windows（x64/ARM64）、Linux（beta） |
| 模型自由度 | 中 | 设计上 GLM 优先；据报可用自己的 key 接其他厂商 |
| 开源 | 无 | 闭源客户端 |

**来源说明。** 官网写明的是 GLM-5.3 与 GLM-5.3-Flash。第三方教程报告 ZCode 也接受你自己的 key 去接 Anthropic、OpenRouter 以及 OpenAI 兼容端点（包括把它指向 DeepSeek 的 Anthropic 兼容地址），更早关于 3.0 的报道则把它描述成 Claude Code、Codex、Gemini 的可视化前端。这项能力**没有**出现在当前官方页面上，因此本地图记为"据报"而非"已确认"——在把多厂商方案建在它上面之前，请以你装的那个版本为准。

## 与模型层的关系

ZCode 是产品，GLM 是模型。本地图目前还没有收录 GLM 所属的开放权重模型档，那是它正在跟踪的另一个缺口。对选型真正重要的是：选 ZCode 而不是选一个厂商中立 harness 的理由，正是客户端与智谱自家模型之间的调校；所以把模型可移植性放在第一位的团队，应该改去看 [harness 路线](../comparisons/agent-harness-frameworks.md)。

## 结论

"一个 GLM 优先的开发者到底该跑什么"，ZCode 是目前最完整的答案，而它的远程调用与长周期目标设计，和本地图上大多数终端循环是真正不同的东西。代价是这种形态一贯的代价：你得到一个整合好的产品，放弃读源码，而最深的那部分能力绑在一家的模型上。
