# Pi

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](pi.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/pi.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Pi 是一个刻意做得很小、很有主张的 coding agent harness——只保留 agent loop、工具和 provider，其它交给扩展。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | earendil-works（2026-04-08 从 Mario Zechner / badlogic 收购而来） |
| 路线 | 可自托管的终端 coding agent + agent toolkit |
| 开源 | 是（MIT，TypeScript） |
| 适合谁 | 想把 harness 保持精简、自己掌控编排选择的开发者 |
| 主要代价 | 自带 API key、自带 skill、自带"agent 该怎么扩展"的主张 |
| 官网 | https://lefos.ai/ |
| GitHub 仓库 | https://github.com/earendil-works/pi |

## 什么时候选它

- 想要一个 coding agent CLI，只默认带核心循环（read、write、edit、bash），其它通过 skills 和扩展按需补强。
- 想要广泛的 LLM 提供方支持——OpenAI、Anthropic、Google、vLLM pods——不绑定单一厂商表面。
- 愿意把工作会话回传到 Hugging Face 作为开源训练数据，这是项目明确鼓励的玩法。

## 什么时候不选它

- 想要一个开箱即用的产品，自带 teams、dashboard 和托管后台运行。
- 不想花时间挑选要接入哪些扩展和 skill。
- 需要打磨过的编辑器表面；Pi 是 terminal-first。

## 能力画像

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 终端工作流 | 很强 | CLI 是主表面 |
| Provider 覆盖 | 很强 | 统一 API 跨 OpenAI、Anthropic、Google、vLLM |
| 工具 harness | 强 | 默认 read、write、edit、bash；通过 skills、prompt 模板、扩展包补强 |
| 开箱编排 | 刻意做轻 | 编排交给调用方是设计意图 |
| 渠道（Slack、Web UI） | 以工具包形式提供 | TUI、Web UI、Slack bot 作为独立包发布 |

## 使用代价

复杂度 Medium。安装本身简单，但 Pi 默认你会自己挑模型、挑 skill、决定 agent 怎么扩展自己。"harness rebellion" 的定位是有意为之：少打包、多自决。

## 底线

Pi 与 Aider、Claude Code 同属"终端 coding agent"路线，但刻意做得更小。2026-04-08 被 Earendil 收购（同时在做 Lefos 云端 agent 平台）之后，原本是个人项目的 Pi 拿到了真实资金，每周 star 增长明显抬升。如果想"拥有 harness 而不是租用 harness"，值得一看。
