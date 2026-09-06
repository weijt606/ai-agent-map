# DeepSeek Harness

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](deepseek-harness.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/deepseek-harness.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：DeepSeek Harness（`dsh`）是一个**没有特权内核**的 agent harness——模型适配层、工具注册表、会话日志，乃至 agent 循环本身，全都是可以从配置里替换掉的插件——它在三周内拿到 21.3 万 star，而项目自己仍标着 developer preview。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | DeepSeek AI |
| 路线 | Agent harness 框架 |
| 仓库 | [`deepseek-ai/deepseek-harness`](https://github.com/deepseek-ai/deepseek-harness)——MIT，TypeScript |
| 是否开源 | 是（MIT） |
| 最适合 | 想自己掌控循环、又不想为了改一个零件去 fork 整个项目的团队 |
| 主要代价 | **developer preview**——README 明确警告会有破坏兼容性的变更 |
| 启动命令 | `npx @deepseek-ai/dsh web`（Web UI 在 `127.0.0.1:3080`） |
| 文档 | https://deepseek-harness.github.io/deepseek-harness/ |

## 为什么要收录

本地图的 [harness 路线](../comparisons/agent-harness-frameworks.md)此前有三种形态：你 fork 下来自己拥有的循环（[Pi](pi.md)、[jcode](jcode.md)）、驱动其他循环的 meta-harness（[QM](qm.md)、[Omnigent](omnigent.md)），以及部署起来用 HTTP 调用的 harness（[TrueForge](trueforge.md)）。`dsh` 是第四种：**一个没有内核可 fork 的 harness。**

它建在 [Cordis](https://github.com/cordiverse/cordis) 上——一个插件内核，插件向共享 context 贡献服务、类型化事件和可回滚的 effect。项目自己的架构文档说得很直白：*"产品的每一部分都是插件，包括模型适配层、工具注册表、会话日志，以及 agent 循环本身，因此每一部分都可以从配置里替换。没有需要打补丁的特权内核。"*

## 什么时候选它

- 你想替换 agent 的**某一个零件**——循环、沙箱策略、工具注册表——而不用维护整个项目的 fork。注册行为是 effect，插件卸载时会自动回滚，所以拆掉和装上一样干净。
- 你需要从同一套代码里得到多种交付形态。内置 profile 有 `web`（浏览器应用）、`headless`（一次性运行，无 server）、`sdk`（JSON-RPC server，带 TypeScript 与 Python 客户端）、`sdk-minimal`，以及 `acp`（仅自动化用的 [Agent Client Protocol](https://agentclientprotocol.com) server）。
- 你想在信任它之前先把组合看清楚：`dsh --profile web --dump-config` 会打印你这台机器实际启动的插件树，打印出来的任何一行都能用你自己的 patch 替换掉。
- 你想要一个厂商官方 harness 上的宽松许可——MIT，第三方依赖许可单独披露。

## 什么时候不选它

- **你需要 API 稳定。** README 的原话：*"DeepSeek Harness 处于 developer preview 且在快速迭代。一定会有破坏兼容性的变更。"* 插件契约明确尚未冻结。
- 你想今天就上手、不想先想架构。profile / bundle / patch 这套分层模型确实比单文件循环要多学一些，它自己的文档甚至建议你用一个 agent 去探索这份代码。
- 你要的是带支持合同的托管产品——这是一个仓库，不是一项服务。
- 你希望只能走厂商自己的模型。事实上不是，但周边生态（文档、插件 topic、Discord）由 DeepSeek 运营。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 可扩展性 | 很强 | 真正的差异点：包括 agent 循环在内，一切都是可替换插件 |
| 交付面 | 很强 | Web UI、headless 一次性运行、JSON-RPC SDK（TS + Python）、ACP server |
| 审批与沙箱 | 强 | 沙箱与审批策略在共享的 `dsh-base` 层里，不是各 profile 各自外挂 |
| 会话持久性 | 强 | append-only 的 `SessionEvent` 日志加内存态存储；会话事件是重载后仍然存在的事实 |
| 可观测性 | 强 | telemetry 是基础层的接缝；capability 事件（`fs/*`、`tools/*`、`telemetry/*`）不需要引入循环就能挂上策略 |
| 稳定性 | **弱** | 按项目自己的标注，developer preview |
| 治理 | 中 | MIT 且接受贡献，但由厂商主导、迭代很快 |

## 组合机制怎么运作

三个名词承担了主要工作，在评估其他任何东西之前值得先搞懂：

- **bundle** 是"配置行 + 它们挂载的代码"的分发格式。`dsh-base` 是共享的第一层——模型适配层、工具、持久化、沙箱与审批策略、设置、凭据、telemetry。
- **profile** 是一个具名组合：它把若干 bundle 叠起来，容纳树外插件，并保存你自己的 `cordis.patch.yml`。
- **patch** 按确定顺序生效——profile 里列出的每个 bundle、profile 自己的 patch、home 级 patch，最后是 `--patch` 覆盖层——它按 id 定位某一行，替换其配置或插入新行。

自定义 profile 默认热重载 patch；`headless`、`sdk`、`sdk-minimal`、`acp` 只在启动时应用一次，因为一次性或 stdio 应用在接管工作之后再替换依赖，会让那个生命周期失效。

## 和本地图其他条目的关系

对 [Pi](pi.md)、[jcode](jcode.md)，差别在所有权模型：那些是你 fork 下来拥有的循环，`dsh` 是你组合并打补丁的一棵树。对 [QM](qm.md)、[Omnigent](omnigent.md)，`dsh` 不是 meta-harness——它不驱动 Claude Code 或 Codex，它就是被驱动的那个。对 [TrueForge](trueforge.md)，两者都提供 SDK 和 server，但 TrueForge 的单位是你部署好、用 HTTP 调用的服务，`dsh` 的单位是你在本地重新组合的插件树。

## 结论

插件内核不是新想法；把它用到 **agent 循环本身**上、并且放在一个厂商官方的 MIT 仓库里，是新的。采纳曲线（三周 21.3 万 star、2.5 万 fork）说明这个卖点立住了。把它和项目给自己贴的标签放在一起权衡：developer preview，契约未冻结。如果你在建的东西本来就会不断改，它很合适；如果你需要钉住一个接口然后走人，它不合适。
