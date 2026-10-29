# TRAE

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](trae.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/trae.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

TRAE 是字节跳动的 AI IDE，分成两个版本，账号、模型和价格各自独立：国际版（trae.ai，按模型 token 价格从美元额度里扣，提供 GPT、Gemini、Kimi 等模型，美国用户另有 Claude 和 Grok）和国内版（trae.cn，按积分计费，只有国产模型）。2026 年 10 月起，同一个桌面应用里有一个 VS Code 风格的 IDE 窗口（含由 AI 主导的 SOLO 模式），以及一个独立的 Agent 窗口，用来跑并行任务、云端任务和定时任务；网页端和移动端共用同一个账号。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | 字节跳动。美国以外的国际版服务由新加坡的 SPRING (SG) PTE. LTD. 提供（见隐私政策） |
| 路线 | 编辑器中心：IDE 窗口（IDE 模式与 SOLO 模式），加上跑多 agent、云端和定时任务的 Agent 窗口 |
| 版本 | 国际版：[trae.ai](https://www.trae.ai)、[docs.trae.ai](https://docs.trae.ai)。国内版：trae.cn、[docs.trae.cn](https://docs.trae.cn)。模型列表、套餐、币种都不同；国内版单独编号（同一天国际版是 v3.6.x，国内版是 v3.4.x） |
| 入口 | TRAE 桌面端（Agent 窗口与 IDE 窗口）、TRAE 网页端、TRAE 移动端；面向 VS Code 和 JetBrains 系列的 TRAE Plugin；TRAE CLI 2.0 只在国内版企业旗舰版提供 |
| 是否开源 | 产品闭源。[`bytedance/trae-agent`](https://github.com/bytedance/trae-agent) 是另一个项目：MIT 许可的研究型 CLI agent（`trae-cli`，自带 API key），最近一次提交在 2026-02-05。`Trae-AI/TRAE` 仓库里只有两行 README |
| 最适合 | 想要兼容 VS Code 的 IDE、入门档便宜、内置模型多、还能用手机把任务派给桌面或云端的开发者；在国内、想在 IDE 里用国产模型的团队 |
| 主要代价 | 不打开隐私模式，对话数据可能被用于分析和模型训练；两个版本差别大到可以算两个产品；免费档没有 SOLO 模式，额度也没有公布具体数字；Claude 只出现在美国的模型列表里 |
| 状态（2026-10-30） | 在售。2026 年 10 月 TraeCode 与 TraeWork 合并为"全新的 TRAE"（v3.6.0，2026-10-08，上线 Agent 窗口） |
| 当前版本（2026-10-30） | 国际版 v3.6.4（更新日志 2026-10-15 条目，"v3.6.1 ~ 3.6.4"）。国内版 v3.4.4（同日） |
| 平台 | macOS 12 及以上（Apple Silicon 与 Intel）；Windows 10、11（x64）；Linux x64 与 ARM64（.deb 支持 Ubuntu 20.04+、Debian 10+，.rpm 支持 Fedora 42、RHEL 9.x）。每个账号最多同时登录 3 台设备 |
| 官网 | https://www.trae.ai |

## 为什么要收录

本地图之前只在 [Graphify](graphify.md) 里把 TRAE 列为集成对象。编辑器中心这条路线上收了 [Cursor](cursor.md)、[Windsurf](windsurf.md) 和 [Google Antigravity](antigravity.md)，字节跳动一个都没有，而字节已经通过 [豆包](doubao.md) 出现在本地图上。TRAE 是本地图上国内厂商在编辑器中心路线上的产品；腾讯的 [CodeBuddy](codebuddy.md) 归在直接执行型，因为它的竞争点在终端 CLI。

2026 年的两次调整也让旧的介绍过时了。2026-05-08（v3.5.56），原来分开的 Builder 智能体并进了统一的内置"Agent"，SOLO Coder 改名为 SOLO Agent。10 月，TraeCode（IDE）和 TraeWork（有网页版、桌面版、移动端的 agent 工作台）合并成一个产品，旧的 TraeWork 桌面版会迁移数据，并可以自动卸载。

## 它是什么

按官方文档的说法：三个客户端，桌面端两个窗口，IDE 窗口里两种模式。

| 部分 | 是什么 |
| --- | --- |
| IDE 窗口：IDE 模式 | 以代码编辑器为中心的工作区，支持 VS Code 扩展、多文件分屏、终端、调试和 Git。初次设置时可以导入 VS Code 或 Cursor 的配置。有侧栏对话、行内对话、CUE 补全（多行修改、修改点预测，以及 Python、TypeScript、Go 项目里的智能导入和重命名），以及会检索代码库、做计划、调用工具的智能体 |
| IDE 窗口：SOLO 模式 | 文档原话是 AI 主导。内置 Agent 先出计划，等你确认，再依次写代码、测试、预览、给出变更总结。有编辑器、浏览器、文档查看器等工具面板；同一项目里可以并行多个任务；Figma 转代码；内置 Supabase、Vercel 部署、AI 服务和 Stripe 支付集成；DiffView 集中查看改动 |
| Agent 窗口 | v3.6.0（2026-10-08）加入。任务工作区，可以跨项目、跨运行环境同时跑多个 agent 任务：本地文件夹、一个项目挂多个路径、通过 SSH 连上的远端目录、worktree，或基于 TRAE 官方基础容器镜像搭的云端环境。自动化（定时任务）、插件市场（插件与技能，2026-09-20 上线）和产物空间（代码改动、HTML、PPT、文档、图片、视频）也放在这里 |
| TRAE 网页端 | 只有云端环境。云端任务在网页端、移动端和 Agent 窗口之间同步 |
| TRAE 移动端 | 向云端或你自己的电脑派发任务并查看进度。和桌面端的连接授权有效期 180 天，只能访问桌面端当前打开的项目；设备离线时任务自动切到云端执行 |
| TRAE Plugin | 在 VS Code 和 JetBrains 系列（含 Android Studio）里提供补全、问答、代码解释、审查和修复 |

这些入口底下共用的能力：MCP Server、可自定义提示词和工具集的自定义智能体、技能、规则、斜杠命令、Hooks（v3.5.66，2026-06-10）、从 `.trae/agents` 加载子 agent 定义（Beta 开关，v3.5.67）、全局记忆与项目记忆、浏览器控制，以及 GitHub 和飞书/Lark 连接器。按模型开启的 Max 模式把上下文窗口扩到最高 1M token，单个任务最多 200 轮工具调用；文档提醒开启后费用会明显上升。

## 有没有 CLI

截至 2026-10-30，国际版没有。trae.ai 的企业版页面写的是 "CLI (coming soon)"。

国内版的 docs.trae.cn 有 **TRAE CLI 2.0**（命令 `traecli`）的文档：一个本地终端编码 agent，支持 macOS、Linux 和 Windows（建议用 WSL2），有交互式 TUI、给脚本和 CI 用的非交互命令 `traecli exec`、插件、技能、MCP、可接入编辑器的 Agent Client Protocol 服务端模式、目录信任，以及三种权限模式（Workspace Edit、Auto-Review、Full Access）。它自己的介绍页写明了限制：仅 TRAE 企业版旗舰版套餐客户可用。TRAE CLI 1.0 已进入"弱维护状态"。它的迁移提示可以导入 Claude Code 的子 agent 和会话，并把 `CLAUDE.md` 转成 `AGENTS.md`。

所以这一页不把 TRAE 放进 [终端编码 CLI agent](../comparisons/coding-cli-agents.md)：两个版本的个人开发者都装不了 TRAE CLI。开源的 [`bytedance/trae-agent`](https://github.com/bytedance/trae-agent) 确实有 CLI（`trae-cli run`、`trae-cli interactive`），但它的 README 把自己定位为方便"studying AI agent architectures"的研究型 agent，用的是你自己的模型服务商 key，TRAE 文档里没有说 IDE 用了它，而且仓库最近一次提交是 2026-02-05。

## 模型（截至 2026-10-30）

国际版，出自 "Built-in models & custom models" 页面（2026-10-26 更新）。可用模型取决于你所在的地区：

| 地区 | 内置模型 |
| --- | --- |
| 美国以外 | GPT-6-Astra、GPT-6-Sol、GPT-6-Luna、GPT-5.6-Sol、GPT-5.6-Terra、GPT-5.6-Luna、GPT-5.5、GPT-5.4、GPT-5.2；Gemini-3.1-Pro-Preview、Gemini-3-Flash-Preview；Seed-2.1-Turbo；GLM-5.2；DeepSeek-V4-Flash；Kimi-K3、Kimi-K2.7-Code、Kimi-K2.5；MiniMax-M3、MiniMax-M2.7。没有 Claude |
| 美国 | GPT-6.1-Sol、GPT-6-Sol、GPT-6-Luna、GPT-6-Astra、GPT-5.6-Sol、GPT-5.6-Terra、GPT-5.6-Luna、GPT-5.5；Grok-4.7、Grok-4.6；Claude Opus 5.5、Sonnet 5.5、Haiku 5.5、Opus 5、Sonnet 5、Opus 4.8、Opus 4.7、Sonnet 4.6、Haiku 4.5；Gemini-3.1-Pro-Preview、Gemini-3.1-Flash-Preview、Gemini-2.5-Pro、Gemini-2.5-Flash；Kimi-K2-0905 |

每个模型都公布了每百万 token 的输入、缓存读、缓存写、输出价格，套餐额度就按这个价格扣。举美国表里的两个例子：Claude Opus 5.5 输入 $4.00、输出 $20.00；GPT-6-Astra 在 272k 上下文以内输入 $10.00、输出 $50.00。最新的一批模型（GPT-6.x、GPT-5.6、GPT-5.5、GLM-5.2、DeepSeek-V4-Flash、Kimi-K2.7-Code、Kimi-K3）只在 2026 年秋季推出的新套餐里提供，老订阅用户升级后才能用。

免费用户只能用 Auto 模式，由 TRAE 自动挑内置模型。付费套餐还可以手动选模型。所有套餐都能加自定义模型：从预设服务商里选并填 API key（包括服务商的 Coding Plan 或 Agent Plan 额度），或者接任何兼容 OpenAI Chat Completions 或 Anthropic Messages 格式的端点，可自定义请求地址。Auto 模式不会用你加的自定义模型。

国内版，出自 docs.trae.cn：Seed-Evolving（仅 Pro 及以上）、Seed-2.1-Pro-0915、Seed-2.1-Turbo、Seed-Code、MiMo-V2.6-Flash 与 -Pro、Step-5-Preview、GLM-5.3-FlashX、GLM-5.3-Flash、GLM-5.3、GLM-5.2、DeepSeek-V4.1-Flash、DeepSeek-V4-Flash、DeepSeek-V4-Pro、Kimi-K3、Kimi-K2.8-Preview、MiniMax-M3、Qwen3.8-Flash、Qwen3.8-Max、Qwen3.7-Plus。没有 GPT、Claude、Gemini、Grok。国内版调用自定义模型不消耗积分。

## 价格与限制（截至 2026-10-30）

国际版，出自定价页和 "Plans & billing" 文档（2026-10-26 更新）：

| 方案 | 月付 | 年付 | 每月包含额度 | 云端任务并行上限 | 说明 |
| --- | --- | --- | --- | --- | --- |
| Free | $0 | $0 | "Limited"（没有公布数字） | 2 | 只能用 Auto 模式；普通队列；补全有限（定价页写每月 5,000 次）；没有 SOLO 模式 |
| Lite | $8 | $80 | $8 | 2 | 只在泰国、印尼、越南、菲律宾、印度、巴基斯坦、土耳其、马来西亚、巴西、哥伦比亚、秘鲁、尼日利亚提供 |
| Pro | $20 | $200 | $20 | 10 | 可手动选模型、快速队列、补全不限量、SOLO 模式 |
| Pro+ | $60 | $600 | $60 | 15 | 同 Pro |
| Ultra | $200 | $2,000 | $200 | 20 | 新模型优先体验 |

计费方式：

- 每次模型请求单独计量：费用 = token 用量 × 该模型的标价。先从每月的美元额度里扣。
- 额度用完后，可以开 On-Demand Usage（仅付费套餐，需要手动打开），按"模型服务商官方标准 API 价格"继续计费，每累计 $3 扣一次款。不开的话，AI 对话要等到下个周期；免费用户要等到下个月。
- 企业版单独售卖（trae.ai 上通过 BytePlus 联系）。只有购买后 24 小时内、且没用过任何服务才能退款。没有学生优惠。
- 老订阅用户只要月付不中断，换到新套餐后继续按原价续费（文档举的例子是 Pro 按 $10/月续费），额度换成新套餐的额度。

国内版，出自 docs.trae.cn《套餐与计费说明》：按积分计费，只有调用内置模型才扣积分。

| 方案 | 单月购买 | 连续包月 | 每月积分 | 云端任务并行上限 |
| --- | --- | --- | --- | --- |
| Lite | ¥49 | ¥45 | 2,000 | 2 |
| Pro | ¥99 | ¥89 | 4,000 | 10 |
| Pro+ | ¥239 | ¥219 | 12,000 | 10 |
| Ultra | ¥699 | ¥629 | 40,000 | 20 |

国内版免费用户每月登录送 500 积分，新用户注册一次性送 2,000 积分，每日签到送 100 积分。增购积分每 1,000 积分 50 元。会员调用 Seed-2.1-Turbo 和 Seed-Code 按 2.5 折扣积分；另有限时闲时折扣（22:00 至次日 8:00），免费用户用 DeepSeek V4 系列积分消耗减半。支付方式是抖音支付、支付宝、微信支付。

## 隐私与数据（截至 2026-10-30）

选 TRAE 之前先读这一节。相关条款分散在四个官方页面上。

- **默认情况下对话可能被用于训练，要自己关掉。** 隐私模式文档（国际版和国内版文字一致）写的是：你的对话内容（包括相关代码片段及 AI 生成的输出结果）"可能会被用于数据分析、产品优化以及模型训练"。隐私模式是 设置 > 账号 里的一个开关；只在登录状态下生效，退出登录后自动关闭。
- **代码库文件另算。** 不论是否开启隐私模式，TRAE 都说不会把代码库文件用于数据分析、产品优化或模型训练。为了做代码库索引，它会把文件临时上传到服务器计算嵌入向量，算完后把明文代码"永久删除"。
- **云端任务会存你的代码。** 云端智能体数据存储声明写明：你授权访问的代码仓库内容，以及 MCP、规则、记忆、Hooks 和上下文，会在会话期间存放在云端，"will never be used for any model training"。云端会话的对话和代码会一直保留，直到你删除该会话。
- **数据会给谁。** 国际版隐私政策（最近更新 2026-05-20，适用于美国以外）写明：数据控制者是新加坡的 SPRING (SG) PTE. LTD.；数据存放在新加坡和马来西亚的服务器上，并可能转移到其他地方，包括美国；AI 对话输入会分享给第三方模型开发方，点名了 Gemini（Google）和 GPT（Microsoft）；字节跳动集团内的关联实体会处理用户数据，用途包括 "training and improving our Corporate Group's technologies"。保留期限是"as long as necessary"，账号信息和用户内容一般在账号存续期间保留。
- **美国用户适用另一套政策。** 上面这份政策排除了美国，文档里也给了单独的美国客服邮箱（`ussupport@mail.traeai.us`）。本页没有读到美国专用的隐私政策。
- **企业版是另一套约定。** trae.ai 企业版页面声称零留存（"Code is encrypted in transit and never stored on our servers"）、不用你的代码训练模型，并有 SOC 2 Type 2 认证。国内企业版文档声称依托火山引擎符合 ISO/IEC 27001 与 27701，并提供私有化部署。这些是厂商的说法，本页没有看到审计报告。

## 地区可用性（截至 2026-10-30）

- 国际版的 "Supported countries and regions" 页面列出了亚洲、欧洲、美洲、大洋洲和非洲的大部分国家和地区，**没有**列入中国大陆、香港、澳门、台湾、俄罗斯、白俄罗斯、伊朗、古巴、叙利亚、委内瑞拉、埃及和加拿大。
- 国际版付费套餐只在 59 个国家和地区出售。这份名单里有香港、澳门和埃及，而可用性页面没有列这三个；两页对不上，建议在你所在的地方两页都核对一下。
- 中国大陆用户用的是独立的 trae.cn 版本，账号体系、模型和人民币价格都单独一套。写这一页时，从境外访问 trae.cn 返回 HTTP 403；本页的国内版信息来自 docs.trae.cn。

## 什么时候选它

- 你想要一个兼容 VS Code 的 IDE，能导入 VS Code 或 Cursor 的配置、继续用原来的扩展，再加上智能体、CUE 补全和 SOLO 模式。
- 你想低成本上手：12 个国家有 $8 的 Lite，Pro 是 $20，用量按公开的模型价格逐 token 扣，选便宜的模型额度就更耐用。
- 你想一份订阅用很多模型：美国以外有 OpenAI 当前这一代、Gemini、Kimi、GLM、DeepSeek、MiniMax 和 Seed，美国另有 Claude 和 Grok，还能再接自己的 key。
- 你想用手机把任务派给自己的电脑或云端环境，并在三个客户端里都能看到进度。
- 你要端到端做小型 Web 应用：SOLO 的 Figma、Supabase、Vercel、Stripe 集成能从设计稿一路做到可访问的部署链接。
- 你在中国大陆，想在 IDE 里用国产模型（Seed、GLM、DeepSeek、Kimi、Qwen、MiniMax、MiMo、Step），用人民币付费。

## 什么时候不选它

- 你的代码或对话绝不能被用于训练，而你没法保证每个成员都在登录状态下打开隐私模式。这种情况用写明不训练、零留存的企业版，或者换别的工具。
- 你的合规要求不允许把代码和提示词发给字节跳动集团的公司，或者不允许存放在新加坡和马来西亚并可能继续转移。
- 你需要开源或自托管。产品是闭源的；`trae-agent` 是另一个研究项目，不是这个 IDE。
- 你需要终端 agent。两个版本都没有面向个人的 TRAE CLI；去看 [终端编码 CLI agent](../comparisons/coding-cli-agents.md)。
- 你在美国以外又想用 Claude。非美国的模型列表里没有它，只能自己接 Anthropic 的 key。
- 你在加拿大、俄罗斯、台湾，或其他不在国际版名单上的地区。
- 你想提前知道免费档能用多少。它的额度只写了"limited"，没有数字，SOLO 模式也只给付费用户。

## 能力形状

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 编辑器工作流 | 强 | VS Code 风格的 IDE 窗口，有扩展、调试、Git、CUE 补全；能导入 VS Code 或 Cursor 设置 |
| 自主构建模式 | 强 | SOLO 模式先出计划、等确认，再写代码、测试、预览、部署；仅付费档 |
| 并行与云端任务 | 强 | Agent 窗口跨项目、SSH 主机、worktree 和云端容器；按套餐 2 到 20 个云端任务并行 |
| 定时任务 | 强 | 自动化任务支持固定时间、固定间隔，或用自然语言描述的时间规则 |
| 跨设备 | 强 | 桌面端、网页端、移动端共享任务；移动端可以操控桌面端 |
| 模型选择 | 强，但分地区 | 内置列表很宽，还能接 OpenAI 或 Anthropic 格式的自定义端点；Claude 和 Grok 只在美国；国内版只有国产模型 |
| 隐私默认值 | 弱 | 不开隐私模式，对话数据可能被用于训练；集团内实体会处理数据；企业版条款更严 |
| 终端 / CLI | 弱 | 只在国内版企业旗舰版提供 |
| 开源 | 弱 | 产品闭源；`trae-agent`（MIT）是另一个研究型 CLI |

## 和其他条目的关系

- [Cursor](cursor.md) 和 [Windsurf](windsurf.md) 形态最接近：都是从 VS Code 派生、带智能体的编辑器。TRAE 的不同在于独立的 Agent 窗口、移动端、从 $8 起按 token 计价的套餐，以及按地区拆分的模型列表。
- [Google Antigravity](antigravity.md) 是这条路线上另一个"编辑器加 agent 管理器"的设计。Antigravity 有公开的 CLI 和带 Gemini 的免费档；TRAE 的多厂商模型列表更宽，还有 SOLO 的应用构建集成，但没有公开的 CLI。
- [CodeBuddy](codebuddy.md) 是腾讯对应的产品线，同样分国际版和国内版。CodeBuddy 的终端 CLI 对个人开放，TRAE 没有。
- [豆包](doubao.md) 是字节跳动的消费级助手；TRAE 模型列表里的 Seed 系列是字节自己的模型。

## 运营成本

装起来成本低，用起来中等。下载的是普通安装包，初次设置能导入 VS Code 或 Cursor 的配置。持续的成本在三件事上：你所在的地方能用哪个版本；团队里每个人是否都打开了隐私模式（或者干脆买企业版）；模型选择和 Max 模式会多快吃掉美元额度。更新很频繁（光 2026-10-15 一天就发了四个小版本），你读到的功能可能已经改了名：Builder 并进了 Agent，SOLO Coder 改成了 SOLO Agent，TraeCode 和 TraeWork 合成了 TRAE。

## 结论

TRAE 是一个能力完整的编辑器中心产品，入口比这条路线上的大多数都多：IDE、AI 主导的 SOLO 模式、多 agent 的 Agent 窗口、网页端、移动端和定时任务，背后是一张宽而便宜、按 token 计价的模型菜单。选它之前先读数据条款：不开隐私模式，对话内容可能被用于训练；字节跳动集团内的公司会处理这些数据；严格的不训练、不留存条款跟着企业版走。它也实际上是两个产品：中国和美国以外的国际版、带 Claude 和 Grok 的美国变体，以及只有国产模型、按人民币积分计费的国内版。如果你需要终端 agent 或开源方案，看本地图上的其他条目。

## 来源

以下均于 2026-10-30 查阅。

- 官网：[trae.ai](https://www.trae.ai/) · [定价](https://www.trae.ai/pricing) · [下载中心](https://www.trae.ai/download) · [企业版（"CLI (coming soon)"、零留存、SOC 2 Type 2）](https://www.trae.ai/enterprise) · [隐私政策（最近更新 2026-05-20）](https://www.trae.ai/privacy-policy)
- 国际版文档，入门：[About TRAE](https://docs.trae.ai/ide/what-is-trae) · [TraeCode 与 TraeWork 合并为全新的 TRAE](https://docs.trae.ai/ide/traework-to-traecode-data-migration) · [桌面端、网页端与移动端](https://docs.trae.ai/ide/trae-across-desktop-web-and-mobile) · [TRAE 桌面端快速开始（系统要求）](https://docs.trae.ai/ide/get-started-with-trae-desktop) · [支持的国家和地区](https://docs.trae.ai/ide/supported-countries-and-regions) · [设备数量限制](https://docs.trae.ai/ide/device-limit) · [更新日志（v3.6.4，2026-10-15）](https://docs.trae.ai/ide/changelog)
- 国际版文档，功能：[SOLO 模式](https://docs.trae.ai/ide/solo-mode) · [智能体概述](https://docs.trae.ai/ide/agent-overview) · [自动运行与安全](https://docs.trae.ai/ide/auto-run-and-security) · [沙箱](https://docs.trae.ai/ide/sandbox) · [自动化任务](https://docs.trae.ai/ide/automated-tasks) · [云端运行环境配置](https://docs.trae.ai/ide/set-up-your-cloud-environment) · [记忆](https://docs.trae.ai/ide/memories) · [Max 模式](https://docs.trae.ai/ide/max-mode) · [TRAE Plugin](https://docs.trae.ai/plugin/what-is-trae-plugin)
- 国际版文档，模型与计费：[内置模型与自定义模型](https://docs.trae.ai/ide/models) · [Auto 模式](https://docs.trae.ai/ide/auto-mode) · [套餐与计费](https://docs.trae.ai/ide/new-plans-and-billing) · [On-Demand Usage](https://docs.trae.ai/ide/on-demand-usage) · [套餐与计费常见问题](https://docs.trae.ai/ide/plans-and-billing-faqs)
- 国际版文档，数据：[隐私模式](https://docs.trae.ai/ide/privacy-mode) · [云端智能体数据存储政策](https://docs.trae.ai/ide/data-storage-policy-for-remote-agents)
- 国内版文档：[关于 TRAE](https://docs.trae.cn/ide_what-is-trae-code) · [套餐与计费说明](https://docs.trae.cn/ide_plans-and-billing) · [内置模型 & 自定义模型](https://docs.trae.cn/ide_models) · [内置模型限时折扣](https://docs.trae.cn/ide_limited-time-discount-for-builtin-models) · [隐私模式](https://docs.trae.cn/ide_privacy-mode) · [更新日志（v3.4.4）](https://docs.trae.cn/ide_changelog) · [TRAE CLI 2.0 简介（仅旗舰版）](https://docs.trae.cn/cli_about-trae-code-cli-2) · [TRAE CLI 2.0 快速开始](https://docs.trae.cn/cli_get-started-with-trae-cli-2) · [升级到 TRAE CLI 2.0](https://docs.trae.cn/cli_get-started-with-trae-cli) · [权限与沙箱](https://docs.trae.cn/cli_permission-and-sandbox) · [企业版概览](https://docs.trae.cn/enterprise_trae-enterprise-edition-overview) · [企业版安全合规](https://docs.trae.cn/enterprise_security-compliance-and-governance)
- GitHub：[bytedance/trae-agent](https://github.com/bytedance/trae-agent)（MIT）· [Trae-AI/TRAE](https://github.com/Trae-AI/TRAE)
