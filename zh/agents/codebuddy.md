# CodeBuddy（腾讯）

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](codebuddy.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/codebuddy.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：CodeBuddy 是腾讯云的编程产品线，有三种形态：编辑器插件、独立的 CodeBuddy IDE、终端 agent CodeBuddy Code。本地图把它放在"直接执行"路线，因为它和这里那些厂商 CLI 正面竞争的是终端 CLI。它的循环是 Claude Code 的样子，模型目录跨多家厂商，另有腾讯的企业部署选项。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 腾讯云（与 [WorkBuddy](workbuddy.md) 同属 "Buddy AI" 系列） |
| 路线 | 直接执行（终端 CLI，即 CodeBuddy Code）；插件和 IDE 是同一账号下的编辑器中心形态 |
| 使用面 | 插件支持 VS Code、JetBrains 系列、Visual Studio、Xcode、微信开发者工具；CodeBuddy IDE（Windows 10+、macOS 11+）；CodeBuddy Code CLI（macOS、Linux、Windows） |
| 版本 | 国际版（[codebuddy.ai](https://www.codebuddy.ai)）与国内版（[copilot.tencent.com](https://copilot.tencent.com)）；CLI 另可接 iOA、专有云、私有化部署的企业后端 |
| 是否开源 | **没有公开源码。** npm 包里附了 MIT 许可文本，但发的是压缩打包后的代码；腾讯 CNB 上的公开仓库只有文档、示例、更新日志和 issue。GitHub 上唯一的仓库是 `Tencent-CodeBuddy/homebrew-tap`（Homebrew 安装配方） |
| 模型 | 内置模型目录由腾讯按版本下发（文档点名混元和 DeepSeek；国内版在 CLI v2.93.4 加入 Hy3 预览版，2026-04-23）；也可通过 `models.json` 或 `CODEBUDDY_BASE_URL` 接任意 OpenAI 格式端点 |
| 最适合 | 在腾讯云上、或身处国内企业协作栈的团队，想让插件、IDE、CLI 都来自一家，并且需要私有云选项 |
| 主要代价 | 按积分计费；源码不公开；没有固定公布的模型清单 |
| 当前版本 | CodeBuddy Code 2.178.1（2026-10-29）；国内版发布说明上 CodeBuddy IDE 为 4.12.2（2026-10-14） |
| 安装 | `npm install -g @tencent-ai/codebuddy-code`（Node.js 18.20+）、`brew install Tencent-CodeBuddy/tap/codebuddy-code`，或原生二进制（Beta） |

## 为什么要收录

本地图已经收了腾讯的办公 agent [WorkBuddy](workbuddy.md) 和面向大众的[元宝](yuanbao.md)，两页都提到 CodeBuddy 是腾讯管代码仓库的那个工具，却一直没有单独写它。这一页补上。

**WorkBuddy 和 CodeBuddy 怎么分。** 腾讯国内版定价页把 "Buddy AI" 当作 WorkBuddy、CodeBuddy 等系列产品的统称，并写明 CodeBuddy 和 WorkBuddy **同一账号、积分共享**，不用分别订阅。两者按工作对象分工：WorkBuddy 处理文档、幻灯片和表格，CodeBuddy 处理代码仓库。底层其实比产品页看上去更近：CodeBuddy Code 自己的 v2.176.0 发布说明里有一组 "Resident service (WorkBuddy)" 修复。这说明 WorkBuddy 很可能跑在 CodeBuddy Code 的引擎上，但腾讯没有公开架构说明，所以这里只当作从更新日志得出的推断。腾讯 2026-07-06 发布 Hy3 的公告里，也把 WorkBuddy/CodeBuddy 并列写进了接入该模型的产品名单。

## 三种形态

| 形态 | 腾讯写的目标用户 | 形状 |
| --- | --- | --- |
| CodeBuddy 插件 | "日常编码开发者 / 特定 IDE 使用者" | 在你现有的编辑器里做补全、对话和 agent。最低版本：VS Code 1.82、JetBrains 系列 2022.2、Android Studio Flamingo、Visual Studio 2022、Xcode 14.0、微信开发者工具 1.06.2409140 |
| CodeBuddy IDE | "产品 / 设计师 / 全栈开发 / 编程初学者" | 独立编辑器，主打"对话即编程"：生成 PRD、Figma 转代码、内置 Supabase 和腾讯 CloudBase、一键部署到 CloudStudio 或 EdgeOne Pages |
| CodeBuddy Code | "DevOps / 运维 / SRE / 资深开发者" | 终端 agent，带 Shell、文件、网络工具，以及无头模式、SDK 和 IDE 桥接 |

IDE 是偏 vibe coding 的那一端，和 [Cursor](cursor.md)、[Windsurf](windsurf.md) 有重叠。CLI 才是该放进[终端编码 CLI 对比](../comparisons/coding-cli-agents.md)的部分，所以上面的路线写的是"直接执行"。

## CodeBuddy Code 和各家厂商 CLI 比起来

循环就是 Claude Code 那一套，文档里一眼能看出来：`CODEBUDDY.md` 和 `AGENTS.md` 指令文件、Shift+Tab 进入计划模式、权限模式叫 `default`、`acceptEdits`、`plan`、`bypassPermissions`、`auto`，还有 hooks、skills、插件与插件市场、子代理、`/rewind` 检查点、`-p` 无头运行。用过 [Claude Code](claude-code.md) 的人几乎不用重新学。不同的地方在这些：

- **模型目录。** [Claude Code](claude-code.md)、[Kimi Code](kimi-code.md)、[MiMoCode](mimocode.md)、[Grok Build](grok-build.md) 都围绕自家模型调校。CodeBuddy 的内置清单跨多家厂商，由腾讯后端按版本下发，腾讯自己的混元/Hy3 只是其中一个选项。它还会把 `lite` 和 `reasoning` 两类子任务自动分给更便宜或更强的模型。
- **部署版本。** 同一个 CLI 可以在国际版、国内版、iOA、专有云、私有化几种后端之间切换（`CODEBUDDY_INTERNET_ENVIRONMENT`，再加企业的 `endpoint`）。企业用户可以通过 `apiKeyHelper` 走 OAuth 客户端凭证登录。
- **国内消息渠道。** Channels（Beta）能把微信、Telegram、Discord 的消息推进正在运行的会话，另有企业微信机器人接入指南。Remote Control（Beta）可以从手机或浏览器访问本机会话。
- **IDE 触达。** `codebuddy --acp` 把它作为 ACP agent server 给 Zed 用；`--ide` 通过本地 MCP 连接接上 VS Code、Cursor、Windsurf、JetBrains 的插件。
- **SDK。** `@tencent-ai/agent-sdk`（npm，MIT）和 `codebuddy-agent-sdk`（PyPI）与 CLI 同步发版。
- **开放程度。** [Kimi Code](kimi-code.md) 和 [MiMoCode](mimocode.md) 是 MIT 开源项目，[Qwen Code](qwen-code.md) 和 [Gemini CLI](gemini-cli.md) 是 Apache-2.0。CodeBuddy Code 是附了 MIT 文本的闭源打包产物，实际处境更接近 [Claude Code](claude-code.md)。
- **发版节奏。** 发布说明显示几乎每天一个版本（2026-10-01 的 2.161.0 到 2026-10-29 的 2.178.1）。

## 什么时候选它

- 你在**腾讯云**上，或者身处国内企业协作栈（微信、企业微信、腾讯统一身份），想让插件、IDE、CLI 归一家厂商、走一张账单。
- 你需要开发者手上那个 CLI 的**专有云或私有化**版本，并用 OAuth 接企业登录。
- 你想要 Claude Code 式的终端循环，但**不想绑死在一家模型厂商**：内置目录跨厂商，`models.json` 能接任意 OpenAI 格式端点（文档给了 DeepSeek 和 OpenRouter 的例子）。
- 团队角色混合：产品和设计用 CodeBuddy IDE，工程师用插件或 CLI，共用一个账号。如果同一批人还要做办公类工作，国内版的积分和 [WorkBuddy](workbuddy.md) 是通用的。

## 什么时候不选它

- **你想读或改 agent 本身。** 没有公开源码，MIT 文本覆盖的是一份压缩打包后的代码。要国产厂商的开源终端循环，选 [Kimi Code](kimi-code.md)、[MiMoCode](mimocode.md) 或 [Qwen Code](qwen-code.md)。
- **你想确切知道跑的是哪个模型。** 内置清单按账号和版本下发，没有固定公布，得在自己装的那份里用 `/model` 查。
- **你想要对某一个模型调得最深。** 如果已经定了 Claude、GPT 或 Kimi，那家自己的 CLI 调得更好（见[怎么选](../comparisons/coding-cli-agents.md#怎么选)）。
- **你需要稳定的使用面。** 几乎每天发版，好几项功能还在 Beta（原生二进制、Channels、Remote Control），细节会一直变。国际版 IDE 发布说明页也落后于国内版（读取时国际版停在 2026-07-22 的 4.10.4，国内版已到 2026-10-14 的 4.12.2），用哪个版本就核对哪个。
- **注意重名。** VS Code 市场里还有好几个无关的扩展也叫 "CodeBuddy"。腾讯的插件发布者是 `Tencent-Cloud`（`Tencent-Cloud.coding-copilot`）。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 终端工作流 | 强 | Claude Code 式循环：计划模式、权限模式、hooks、skills、插件、子代理、检查点 |
| 使用面覆盖 | 很强 | 插件覆盖 VS Code、JetBrains、Visual Studio、Xcode、微信开发者工具，加独立 IDE 和 CLI，同一账号 |
| 模型自由度 | 强 | 跨厂商的内置目录，外加任意 OpenAI 格式端点；内置清单不公开 |
| 企业部署 | 很强 | 国际版、国内版、iOA、专有云、私有化；通过 `apiKeyHelper` 走 OAuth |
| IDE / ACP 集成 | 强 | `--acp` 接 Zed；`--ide` 桥接 VS Code、Cursor、Windsurf、JetBrains 插件 |
| 远程 / 消息 | 中 | Channels 和 Remote Control 都是 Beta；微信、企业微信、Telegram、Discord |
| 无头 / 自动化 | 强 | `-p` 模式、GitLab CI/CD 指南、定时任务、JS 与 Python SDK |
| 开源 / 可审计性 | 低 | MIT 文本附在压缩打包的代码上；没有公开源码仓库 |

## 价格（2026-10-30 读取）

两个版本都按积分计，不同模型消耗不同。下面的赠送额度是腾讯自己标的"限时"数字，会变。

| 版本 | 套餐 | 价格 | 每月积分 |
| --- | --- | --- | --- |
| 国际版 | Free | $0 | 100（另有限时每日奖励） |
| 国际版 | Pro | $10/月 或 $96/年 | 基础 1,000 + 赠送 1,000 |
| 国际版 | Team | $40/席/月 或 $480/席/年 | 每席 1,000，团队共享 |
| 国内版 | 体验版 | 免费 | 500 |
| 国内版 | 标准版 / 高级版 / 旗舰版 | 99 / 199 / 999 元/月（连续包月或年付更低） | 基础 2,000 / 4,000 / 20,000，另有限时加赠 |
| 国内版 | 企业旗舰版（SaaS） | 198 元/人/月，1 个坐席起购 | 每人 2,000，团队共享 |
| 国内版 | 企业专享版（专有云） | 316 元/人/月，100 个坐席起购 | 每人 2,000，团队共享 |

国内版三档自 2026-07-01 起生效，原来的单一付费套餐从那天拆成三档。国内版的同一份积分也能用在 WorkBuddy 上。

## 结论

CodeBuddy 一家厂商覆盖的使用面比这里多数条目都多：插件、偏 vibe coding 的 IDE、Claude Code 式的 CLI 共用一个账号，版本一直延伸到私有云。如果腾讯云或国内企业协作栈本来就是你的环境，或者你需要一个公司能自己托管的 CLI，就选它。如果你想读 agent 的源码，或者想把循环绑定在某一个模型上，就别选，[Kimi Code](kimi-code.md)、[Qwen Code](qwen-code.md) 和各家厂商 CLI 更合适。腾讯做办公的那个兄弟产品、共用同一份积分的，见 [WorkBuddy](workbuddy.md)。

## 来源

均于 2026-10-30 读取。

- 腾讯云产品文档：[CodeBuddy 产品简介](https://cloud.tencent.com/document/product/1831/134343)（最近更新 2026-08-14）
- CodeBuddy 文档（国际版）：[IDE 简介](https://www.codebuddy.ai/docs/ide/Introduction) · [IDE 安装](https://www.codebuddy.ai/docs/ide/Getting-Started/Installation) · [IDE models.json](https://www.codebuddy.ai/docs/ide/Features/models) · [Pricing](https://www.codebuddy.ai/docs/ide/Account/pricing) · [Credits](https://www.codebuddy.ai/docs/ide/Account/credits) · [IDE 发布说明](https://www.codebuddy.ai/docs/ide/release-notes/release-notes)
- CodeBuddy 文档（国内版）：[IDE 简介（三种形态、插件最低版本）](https://copilot.tencent.com/docs/ide/Introduction) · [IDE 安装和登录](https://copilot.tencent.com/docs/ide/Getting-Started/Installation) · [定价](https://copilot.tencent.com/docs/ide/Account/pricing) · [IDE 发布说明](https://copilot.tencent.com/docs/ide/release-notes/release-notes)
- CodeBuddy Code 文档：[概述](https://www.codebuddy.ai/docs/cli/overview) · [安装](https://www.codebuddy.ai/docs/cli/installation) · [身份和访问管理](https://www.codebuddy.ai/docs/cli/iam)（[中文](https://copilot.tencent.com/docs/cli/iam)） · [模型配置](https://www.codebuddy.ai/docs/cli/models) · [成本](https://www.codebuddy.ai/docs/cli/costs) · [IDE 集成](https://www.codebuddy.ai/docs/cli/ide-integrations) · [ACP](https://www.codebuddy.ai/docs/cli/acp) · [权限模式](https://www.codebuddy.ai/docs/cli/permission-modes) · [无头模式](https://www.codebuddy.ai/docs/cli/headless) · [Channels](https://www.codebuddy.ai/docs/cli/channels) · [SDK](https://www.codebuddy.ai/docs/cli/sdk)
- CodeBuddy Code 发布说明：[v2.178.1（2026-10-29）](https://www.codebuddy.ai/docs/cli/release-notes/v2.178.1) · [v2.176.0（"Resident service (WorkBuddy)" 修复）](https://www.codebuddy.ai/docs/cli/release-notes/v2.176.0) · [v2.93.4（Hy3 预览版，2026-04-23）](https://www.codebuddy.ai/docs/cli/release-notes/v2.93.4)
- 软件包：[npm 上的 `@tencent-ai/codebuddy-code`](https://www.npmjs.com/package/@tencent-ai/codebuddy-code)（2.178.1，LICENSE.txt 为 MIT 文本） · [npm 上的 `@tencent-ai/agent-sdk`](https://www.npmjs.com/package/@tencent-ai/agent-sdk) · [PyPI 上的 `codebuddy-agent-sdk`](https://pypi.org/project/codebuddy-agent-sdk/) · [VS Code 市场上的 `Tencent-Cloud.coding-copilot`](https://marketplace.visualstudio.com/items?itemName=Tencent-Cloud.coding-copilot)
- 仓库：[cnb.cool/codebuddy/codebuddy-code](https://cnb.cool/codebuddy/codebuddy-code)（文档、示例、更新日志、issue） · [Tencent-CodeBuddy/homebrew-tap](https://github.com/Tencent-CodeBuddy/homebrew-tap)
- [腾讯混元正式发布 Hy3（腾讯新闻中心，2026-07-06）](https://www.tencent.com/zh-hk/tencent-hunyuan-officially-releases-hy3-advancing-agent-capabilities-and-deeper-product-integration/)
