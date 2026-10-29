# Google Antigravity

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](antigravity.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/antigravity.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Antigravity 是谷歌的 agent 优先开发平台。2025 年 11 月上线时是一个加了 Agent Manager 的 IDE；2026 年 5 月以后，它变成了一组入口（独立的 agent 桌面应用、终端 CLI、六款编辑器的扩展、原来的 IDE，以及 Python SDK），底下跑的是同一套谷歌 agent harness，模型以 Gemini 为主，付费档可用 Claude。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 谷歌 |
| 路线 | 编辑器中心（独立 IDE 加编辑器扩展），同一 harness 上还有 agent 管理桌面应用和 CLI |
| 是否开源 | 否。桌面应用和 IDE 闭源。[`antigravity-cli`](https://github.com/google-antigravity/antigravity-cli) 仓库里只有 README、更新日志和示例，没有源码，也没有许可证文件。[Python SDK](https://github.com/google-antigravity/antigravity-sdk-python) 是 Apache-2.0，但依赖一个编译好的运行时二进制，只随 PyPI 的 wheel 包分发 |
| 最适合 | 用 Gemini 的开发者：想在本机并行跑几个 agent 并盯着它们干活，需要内置的浏览器操作和计划审阅，也想要一个能真用的免费档 |
| 主要代价 | 配额没有公布具体数字，谷歌说随时可能调整；不支持自带 key；产品分成五个入口，更新速度各不相同；条款禁止在第三方 agent 里用 Antigravity 账号登录 |
| 状态（2026-10-30） | 2025-11-18 以免费公开预览上线；定价页现在把订阅方案标为 "Generally Available"。SDK 仍是预览版，JetBrains、Zed、Xcode、Eclipse 扩展的企业版支持也是预览 |
| 当前版本（2026-10-30） | 桌面应用 v2.28.1（2026-10-28）· CLI v1.4.0（2026-10-16）· 独立 IDE v2.6.0（2026-10-26）· VS Code 扩展 v1.10.0（2026-10-26）· SDK v0.1.22（2026-10-12） |
| 平台 | macOS 12 及以上（Apple Silicon 与 Intel）、Windows 10 64 位及以上（x64 与 ARM64）、glibc 2.28 及以上的 Linux（x64 与 ARM64）、Googlebook |
| 官网 | https://antigravity.google |

## 为什么要收录

本地图提到 Antigravity 好几次，却一直没有它的页面。[Gemini CLI](gemini-cli.md) 在这一页加入之前写的是"尚未收录"，[Gemini Task](gemini-task.md) 跑在它的 harness 上，[CodeGraph](codegraph.md)、[Omnigent](omnigent.md)、[Graphify](graphify.md)、[ECC](ecc.md)、[Orca](orca.md) 都把它列为集成对象。编辑器中心这条路线上收了 [Cursor](cursor.md) 和 [Windsurf](windsurf.md)，谷歌一个都没有。

这个缺口还盖住了一件影响选型的事。2026-05-19，谷歌开发者博客宣布把 Gemini CLI 并入 Antigravity：从 2026-06-18 起，Gemini CLI 和 Gemini Code Assist 的 IDE 扩展不再为 Google AI Pro、Ultra 订阅用户以及 Gemini Code Assist 个人版的免费用户提供服务。持有 Code Assist Standard 或 Enterprise 许可、或使用付费 Gemini API key 的不受影响。Gemini CLI 自己的配额页顶部现在挂着一条横幅，原文是 "Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026."。对用谷歌技术栈的个人开发者来说，Antigravity 现在就是谷歌自家的编码产品。

## 它是什么

按谷歌文档的说法，是一套 agent harness 加几个入口，登录在所有入口之间共享。

| 入口 | 是什么 |
| --- | --- |
| Antigravity 桌面应用（2.0） | 2026-05-19 发布的独立桌面应用，不带编辑器。谷歌的说法是 Agent Manager 长成了一个独立产品。对话按项目归组，一个项目可以跨多个文件夹。功能有子 agent、hooks、worktree、Automations（类 cron 的定时任务，v2.21.1 起由 Scheduled Tasks 改名而来）、写代码前先出计划供审阅的 `/plan`（v2.17.0）、`/goal`、`/schedule`、`/browser`、语音转写；v2.28.0（2026-10-27）起内置浏览器和 PDF 阅读器 |
| Antigravity CLI（`agy`） | 用 Go 写的终端客户端，和桌面应用共用 harness 和设置。安装用 `curl -fsSL https://antigravity.google/cli/install.sh \| bash`（macOS、Linux、Googlebook），Windows 用 PowerShell 或 CMD 脚本，装好后用 `agy` 启动，通过系统钥匙串或浏览器流程登录。它和桌面应用吃同一份方案配额、用同一份模型列表（模型页把桌面应用、CLI、IDE 并列），状态栏显示剩余 AI credits，`useG1Credits` 设置控制超额时是否扣 credits。CLI 会话可以导入桌面应用继续。`agy -p` 是给脚本和 CI 用的无头模式 |
| Antigravity IDE（独立版） | 最初的那个产品：编辑器视图有 Tab 补全、行内自然语言指令和侧栏 agent；Agent Manager 可以跨工作区同时跑多个 agent；Artifacts（任务清单、实现计划、走查记录、截图、浏览器录屏）可以直接评论来引导 agent。浏览器子 agent 在独立的 Chrome 配置里操作本地 Chrome，带允许和禁止名单 |
| IDE 扩展 | VS Code、Visual Studio 2026、JetBrains 系列、Zed、Xcode、Eclipse（Eclipse 为公开预览） |
| Antigravity SDK | Python SDK（`pip install google-antigravity`），用来在这套 harness 上搭自己的 agent，目前是预览版 |

另外还有：插件市场（2026-10-29 公布，分批开放），插件是 MCP 配置、skills、规则、hooks 和自定义 agent 的打包，在桌面应用里或用 `agy plugin install` 安装；Remote Control（2026-08-21 公布），可以在网页浏览器里操控你其他机器上的会话，agent 需要你回应时会推送通知。

IDE 的处境：2.0 发布时，现有 IDE 用户被自动升级到桌面应用，但可以继续用 IDE，谷歌当时也仍建议开发者用它，并说之后的版本会把 Agent Manager 从 IDE 里拿掉。IDE 从 v2.5.5（2026-08-13）到 v2.6.0（2026-10-26）之间没有其他版本，同一时段桌面应用发了十多个版本。企业账号无法登录独立 IDE，谷歌的企业文档也写明它不支持企业部署。想在编辑器里用 Antigravity 的组织，谷歌指向的是扩展。

## 模型（截至 2026-10-30）

出自谷歌的 "Choose a model" 页面。每个模型可选 Low、Medium、High 三档思考强度。

| 模型 | 免费与 Google AI Plus | Google AI Pro | Google AI Ultra | 企业版 |
| --- | --- | --- | --- | --- |
| Gemini 4 Argon | 无 | 有（付费方案，或符合条件设备的试用） | 有 | 有 |
| Gemini 3.8 Flash | 有 | 有 | 有 | 有 |
| Gemini 3.7 Flash、3.6 Flash、3.1 Pro | 无 | 无 | 无 | 有 |
| Claude Sonnet 5.5、Opus 5.5（thinking） | 无 | 有（仅付费，不含试用） | 有 | 有（需管理员开启，按 token 计费） |
| Claude Sonnet 4.6、Opus 4.6（thinking） | 有，2026-11-02 下线 | 有，2026-11-02 下线 | 无 | 无 |
| GPT-OSS-120b | 有，2026-11-02 下线 | 有，2026-11-02 下线 | 有，2026-11-02 下线 | 无 |

按这张表：2026-11-02 之后，免费档唯一的推理模型是 Gemini 3.8 Flash，Claude 只留在付费的 Pro、Ultra 和企业版。Gemini 和第三方模型各走一套配额，每套都有周上限和五小时上限。图像生成固定用 Nano Banana 2，不能换。Automations 默认用 Flash（v2.24.0）。用 Google Cloud 的应用默认凭据（ADC）登录时，如果你的 Vertex AI 项目有权限，桌面应用和 CLI 也会列出 Claude Opus 5.5 和 Sonnet 5.5。

## 价格与限制（截至 2026-10-30）

| 方案 | 价格（美国，每月） | Antigravity 能用到什么 |
| --- | --- | --- |
| 免费（Individual） | $0 | 每周刷新的配额、周上限、不限量的 Tab 补全和 Command 请求 |
| Google AI Pro | $19.99 | 每五小时刷新一次的配额，直到用满周上限 |
| Google AI Ultra | $99.99 或 $199.99 | 谷歌方案页写的是 Pro 的 5 倍和 20 倍；可用第三方模型；周上限最高 |
| 通过 Google Cloud 的企业方案 | Gemini Enterprise Standard、Plus 每席位 $30 起；或按量付费，不收席位费 | 桌面应用、CLI 和 IDE 扩展；第一方模型每月附带席位额度 $10（Standard）或 $15（Plus）；第三方模型按 token 计费 |

影响账算的几条细节：

- 所有方案都没有公布请求数或 token 数。方案页说限额跟 "the amount of work done by the agent" 挂钩，主要由可用算力决定，并且 "are subject to modification"。
- Pro 和 Ultra 可以买 AI credits 抵超额，按 Gemini Enterprise 的用量价扣。有个设置决定额度用完后是否自动扣 credits（Never 或 Always）。
- 不支持自带 key 或自定义端点来扩容，也没有按定制合同的组织档。
- 登录需要年满 18 岁、所在国家或地区在支持名单内的个人 Google 账号，或者所在组织已开通 Antigravity。截至 2026-10-30，中国大陆、香港、澳门和俄罗斯不在谷歌的支持国家和地区名单上。

## 什么时候选它

- 你用 Gemini，想用谷歌自己的 harness。谷歌说 Gemini 模型是和它一起调优的，Argon 在 2026-10-13 进了 Antigravity。
- 你想在本机同时跑几个 agent，并在一个地方管住它们：项目、可以直接发消息的子 agent、worktree、Automations，以及浏览器里的 Remote Control。
- 你的活需要在浏览器里验证。agent 能打开并操作浏览器，把过程录下来，以截图和录屏的形式交回给你评论。
- 你希望先审计划再写代码：`/plan` 和实现计划 artifact 都是内置的。
- 你需要一个能认真试用的免费档。它按周封顶，2026-11-02 起只剩 Gemini。
- 你是从 Gemini CLI 迁过来的。`agy` 会读 `GEMINI.md` 和 `AGENTS.md`，`agy plugin import gemini` 能把扩展转成插件。工作区 skills 要从 `.gemini/skills/` 挪到 `.agents/skills/`，MCP 服务器要挪进 `mcp_config.json`。谷歌自己说功能不是一一对应。
- 你的组织已经在用 Gemini Enterprise。桌面应用、CLI 和扩展会沿用它的 IAM、VPC Service Controls 和数据驻留控制；谷歌说企业版的代码和提示词不会用于训练其基础模型。

## 什么时候不选它

- 你需要开源或自托管。这里没有一样符合，SDK 的 Python 层除外，而它照样要用谷歌编译好的运行时。
- 你要按确定的预算做规划。配额没有数字，Pro 够不够用只能拿自己的工作负载去试。
- 你想自带模型 key，或者想在别的工具里用这份订阅。谷歌 FAQ 写明，用第三方软件（点名了 Claude Code、OpenClaw、OpenCode）配合 Antigravity 账号登录违反条款，可能导致封号；消费者方案也不支持把 `agy` 包进第三方 agent。想在别的 agent 里用 Gemini，谷歌给的路是 Gemini Enterprise 或 AI Studio 的 API key。
- 你想把独立 IDE 定为企业标准。它不支持企业部署，更新节奏也已经落后于桌面应用。
- 你在中国大陆、香港、澳门或俄罗斯，或者未满 18 岁。
- 你想要一个稳定的单一入口。2026 年 5 月以来产品重心在 agent 桌面应用，选 Antigravity 的团队还得在桌面应用、CLI、IDE 和扩展之间定一个。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 并行 agent 管理 | 很强 | 项目、子 agent、worktree、Automations；桌面应用就是围绕这件事做的 |
| 编辑器工作流 | 强 | 独立 IDE 加六款编辑器扩展；但 IDE 本身已经不是谷歌最先发新功能的地方 |
| 浏览器操作 | 强 | IDE 里有浏览器子 agent，桌面应用 v2.28.0 起内置浏览器，录屏作为 artifact |
| 计划与审阅 | 强 | 实现计划、走查记录、在 artifact 上评论、带审阅策略设置的 `/plan` |
| 远程操作 | 强 | 网页浏览器里的 Remote Control，加推送通知 |
| 模型选择 | 中 | Gemini 加付费档的 Claude 5.5；免费档 2026-11-02 起只有 Gemini；不能自带 key |
| 免费档 | 中 | 是真能用的，但按周封顶，没有公布数字 |
| 企业 | 强，但有缺口 | 桌面应用、CLI 和扩展纳入 Gemini Enterprise；独立 IDE 不在内；四款扩展的企业支持还是预览 |
| 开源 | 弱 | 桌面应用和 IDE 闭源；CLI 仓库没有源码；SDK 是 Apache-2.0，但包着编译好的二进制 |

## 与 Gemini CLI 和 Jules 的关系

谷歌在本地图上出现在四个位置，现在大多和 Antigravity 连在一起。

- [Gemini CLI](gemini-cli.md) 是谷歌的开源终端 agent。Antigravity CLI 借鉴了它的 harness，也是 2026-06-18 之后消费者用户被引导去的地方。持有 Code Assist Standard 或 Enterprise 许可、或用付费 API key 的，仍可继续用 Gemini CLI。
- [Jules](jules.md) 是另一种形态。按谷歌的 Jules 页面，它把 GitHub 仓库克隆到云端虚拟机里，出计划、给 diff、开 PR；谷歌的方案页也把 Jules 和 Antigravity 的额度分开列。Antigravity 的 agent 跑在你自己的机器上（或你通过 Remote Control 连上的机器）。想把任务交出去、等一个 PR 回来，选 Jules；想坐在 agent 旁边看它干活，选 Antigravity。2.0 的发布文章把云端部署的 agent 列为计划中，这条界线以后可能会变。
- [Gemini Task](gemini-task.md) 是 Gemini 应用里的消费者 agent，按那篇 profile 引用的 I/O 发布文章，它跑在 Antigravity harness 上。

## 运营成本

中等。安装就是下载或一行脚本，登录用 Google 账号。持续的成本在三个决定上：团队统一用哪个入口；你所在方案那份没公布数字的配额够不够你的工作负载；如果你在免费档上依赖 Claude 4.6 或 GPT-OSS，2026-11-02 下线之后怎么办。发版很频繁（光 2026 年 10 月，桌面应用就从 v2.21 发到 v2.28），默认自动更新；谷歌的发布页说明可以把更新设为手动或关闭。

## 结论

Antigravity 是谷歌在编辑器中心路线上的答案，2026 年 5 月以后也是谷歌在终端上的答案。它的长处是能看着跑的并行本地 agent、浏览器验证和计划审阅，以及一个真能拿来评估的免费档。代价是：闭源产品绑定 Google 账号，配额没法提前估，不能自带 key，也不能把订阅拿到别的工具里用，而且产品重心已经从 IDE 挪到了 agent 桌面应用。如果你希望编辑器本身始终是重心，下决定前先拿它和 [Cursor](cursor.md)、[Windsurf](windsurf.md) 比一比。

## 来源

以下均于 2026-10-30 查阅。

- 产品：[antigravity.google](https://antigravity.google/) · [Antigravity IDE](https://antigravity.google/product/antigravity-ide) · [下载页（版本与系统要求）](https://antigravity.google/download) · [发布页（更新模式）](https://antigravity.google/releases) · [定价](https://antigravity.google/pricing)
- 文档：[Overview](https://antigravity.google/docs/overview/) · [Choose a model](https://antigravity.google/docs/models/) · [Plans](https://antigravity.google/docs/plans/) · [FAQ（地区、年龄、第三方使用）](https://antigravity.google/docs/faq/) · [Enterprise](https://antigravity.google/docs/enterprise/) · [Authenticate](https://antigravity.google/docs/install/) · [IDE 扩展](https://antigravity.google/docs/ide/extensions/) · [IDE 浏览器](https://antigravity.google/docs/ide/browser/) · [从 Gemini CLI 迁移](https://antigravity.google/docs/cli/gcli-migration/) · [更新日志（桌面应用 v2.28.1、CLI v1.4.0、IDE v2.6.0、扩展 v1.10.0、SDK v0.1.22）](https://antigravity.google/docs/changelog/)
- 博客：[Introducing Google Antigravity（2025-11-18）](https://antigravity.google/blog/introducing-google-antigravity) · [Antigravity @ I/O 2026（2026-05-19）](https://antigravity.google/blog/google-io-2026) · [Introducing Antigravity 2.0（2026-05-19）](https://antigravity.google/blog/introducing-google-antigravity-2) · [Introducing Antigravity CLI（2026-05-19）](https://antigravity.google/blog/introducing-google-antigravity-cli) · [Changes to Antigravity plans（2026-05-19）](https://antigravity.google/blog/changes-to-antigravity-plans) · [Remote Control（2026-08-21）](https://antigravity.google/blog/remote-control-for-antigravity) · [Gemini 4 Argon in Antigravity（2026-10-13）](https://antigravity.google/blog/gemini-4-argon-in-google-antigravity) · [Plugin Marketplace（2026-10-29）](https://antigravity.google/blog/plugin-marketplace-in-antigravity)
- [Gemini CLI 配额与价格（替换横幅）](https://geminicli.com/docs/resources/quota-and-pricing) · [Antigravity CLI AI credits](https://antigravity.google/docs/cli/credits/)
- [谷歌开发者博客：Transitioning Gemini CLI to Antigravity CLI（2026-05-19）](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
- [Google AI 方案（美国价格）](https://gemini.google/us/subscriptions/?hl=en) · [Jules](https://jules.google/)
- GitHub：[google-antigravity/antigravity-cli](https://github.com/google-antigravity/antigravity-cli) · [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python)
