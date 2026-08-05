# Open Code Review

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](open-code-review.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/open-code-review.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话判断：Open Code Review（`ocr`）是阿里巴巴开源出来的 AI 代码评审 CLI——一个刻意做*窄*的 agent，在大模型外面包了一条确定性的评审流水线，用召回率换准确率；它既可以自己跑评审，也可以把推理这步交给你已经在用的 coding agent。

> **窄是故意的。** 它不是一个"顺便能评审代码"的通用 coding agent。选文件、打包文件、匹配规则、定位评论这些步骤由工程逻辑负责；模型只用在动态判断和动态取上下文这些真正有帮助的地方。这就是它全部的设计论点，也是"为什么不直接拿 [Claude Code](claude-code.md) 配个评审 skill 去啃 diff"的答案。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | 阿里巴巴集团（`alibaba/open-code-review`，open-codereview.ai） |
| 路线 | 评审优先自动化——专职代码评审 agent |
| 开源 | Apache-2.0 |
| 实现 | Go；通过 npm（`@alibaba-group/open-code-review`）、安装脚本、release 二进制或源码分发 |
| 模型 | 任何 OpenAI 或 Anthropic 兼容的 endpoint；在委派模式下甚至完全不需要 |
| 表面 | CLI（`ocr`）、CI/CD（GitHub Actions、GitLab CI、GitFlic CI、Gerrit）、Claude Code / Codex / Cursor / OpenCode 插件，以及一个可移植的 agent skill |
| 适合 | 想在 CI 里获得可复现、行级精确的评审，又不想付通用 agent token 账单的团队 |
| 主要代价 | 召回率被刻意压得比通用 agent 低；还有一套评审规则和配置要维护 |
| GitHub 仓库 | https://github.com/alibaba/open-code-review |

## 来历

它最初是阿里巴巴集团内部的官方 AI 代码评审助手。项目自述称它跑了大约两年、服务过数万名开发者、发现过数百万个代码缺陷，之后才开源出来——在这个品类里这种出身很少见：多数评审 agent 是先做成产品、再慢慢打磨，而它正好反过来。这些规模数字是厂商自述、无法独立核实，但它的设计形态和这套说法是自洽的。

## 什么时候选它

- **你的评审跑在 CI 里，必须稳定。** 它的卖点正对着通用 agent 做评审时的几个失败模式：改动一大就"偷工减料"只看部分文件、报出来的行号会漂、prompt 稍微一改质量就大幅波动。
- **token 成本是个事。** 项目声称在同等模型下只用通用 agent 约 **1/9** 的 token、且墙钟时间更短——当评审要跑在每一个 PR 上时，这个差别很实在。（厂商自跑的 benchmark，注意事项见下。）
- **你要的是准确而不是数量。** 召回率按设计就比通用 agent 低，理由是：一个大家学会无视的评审机器人，比一个话少的更糟。
- **你想保留现有 agent 和它的模型。** 在**委派模式**下，`ocr` 负责选文件和解析规则，评审本身由你的 coding agent 用它自己的大模型来做——不需要另外的 API key，也不用配 provider。
- **你需要没有 diff 也能评审。** `ocr scan` 会对整个仓库或某个目录做全文件评审，面对一个不熟悉的代码库时，你要的是这个而不是看变更集。
- 你不想自己写语言规则：内置规则集覆盖空指针风险、线程安全、XSS、SQL 注入等，跨多种语言。

## 什么时候不选它

- 你想要一个能顺手*把问题改掉*并开 PR 的 agent——那是 [Cline](cline.md)、[CoStrict](costrict.md)、[Codex](codex.md) 或 [Claude Code](claude-code.md)。`ocr` 只评审。
- 你要为安全审计追求最大召回。准确优先这个取舍是明说的，所以请把它和专门的安全工具搭配使用，别把它当成覆盖度。
- 你要的是带私有化部署、需求到测试的标准化流程、以及 IDE 表面的企业平台——那条道上 [CoStrict](costrict.md) 更贴。
- 你的仓库没有有意义的 Git 历史，或者 Git 版本低于 2.41——它的 diff 生成、代码搜索和仓库操作全都依赖 Git。

## 能力形态

| 维度 | 判断 | 说明 |
| --- | --- | --- |
| 评审准确率 | 很强（厂商自述） | 同等模型下准确率和 F1 高于通用 agent，token 只要约 1/9 |
| 召回率 | 刻意受限 | 这是对"噪音"的主动取舍，不是疏漏 |
| 行级定位 | 强 | 专门有独立的定位模块和反思模块来防止位置漂移 |
| 大变更集稳定性 | 强 | 相关文件被打包成评审单元，每个单元由一个上下文隔离的子 agent 并发评审 |
| CI/CD 集成 | 强 | GitHub Actions、GitLab CI、GitFlic CI、Gerrit |
| agent 集成 | 强 | Claude Code、Codex、Cursor、OpenCode 插件，外加给 skill 兼容 agent 的可移植 skill |
| 可观测性 | 具备 | OpenTelemetry 集成，另有浏览器端的会话查看器可回放评审 |
| 自主修复 | 非目标 | 它只留评论，不落改动 |

## 关于那个 benchmark

项目公布了一份对比：同等底层模型下与通用 agent（Claude Code）比较，数据来自 50 个热门开源仓库、200 个真实 PR、10 种编程语言、1,505 条经 80 多位资深工程师交叉验证的标注真值。这在这个品类里已经算是相当认真的评测设计，而它报告的取舍——准确率和 F1 更高、token 用量低得多、召回率更低——至少和它的架构是内部自洽的。

但它终究是**厂商自跑**的、在厂商自建的 benchmark 上、只对一个竞品。把*方向*当作可信，把*幅度*当作未经核实。如果评审质量是你的决定性因素，就拿你自己最近的几个 PR 跑一遍再定；诚实的对比对象是你今天在用的东西，跑在你自己的代码上。

## 运维成本

上手低，用好中等。安装是一条 npm 命令，`ocr config provider` / `ocr config model` 会交互式带你配 provider 并自动测连通性。会话可续跑，`ocr session comments` 能按严重级别过滤或以 JSON 输出已记录的问题——想把它接成一道卡口时你要的正是这个。长期成本在评审规则那一面：路径过滤和定向都可配置，而一个评审机器人有没有用，全看这些规则和你的代码库匹配得如何。委派模式能把模型成本完全去掉，代价是把账记到你 coding agent 的 token 上。

## 结论

Open Code Review 是目前最有力的一个论据，说明**代码评审应该是一个专门的 agent，而不是丢给通用 agent 的一段 prompt**。它的混合设计——绝不能出错的步骤交给确定性工程、只把判断题交给大模型——正对着团队对 agent 评审的那些抱怨；而背后两年的内部历史，在它的表面上是看得出来的：可续跑的会话、按严重级别过滤的 JSON 输出、四套 CI 系统、OpenTelemetry，以及一个不需要自带 API key 的委派模式。请把"准确优先于召回"当作一条真实约束而不是营销话术：这个工具是为了让人信，不是为了面面俱到。既评审又动手的 agent 见 [Cline](cline.md) 和 [CoStrict](costrict.md)；更宽的编码场景见[编码自动化](../use-cases/coding-automation.md)。
