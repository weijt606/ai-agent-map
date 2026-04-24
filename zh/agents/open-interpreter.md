# Open Interpreter

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](open-interpreter.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/open-interpreter.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Open Interpreter 让 LLM 通过自然语言直接在你的机器上执行代码——ChatGPT Code Interpreter 的开源本地替代，无沙盒限制。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Killian Lucas / Open Interpreter org |
| 路线 | 本地自然语言代码执行 |
| 是否开源 | 是，MIT |
| 最适合 | 想让 LLM 直接在本机跑 Python、JS、Shell，无文件大小和时间限制的开发者 |
| 主要代价 | 代码在你的真实机器上无沙盒运行——每条命令都是真实操作 |
| 官网 | https://www.openinterpreter.com |
| GitHub 仓库 | https://github.com/openinterpreter/open-interpreter |

## 什么时候选它

- 你想用自然语言告诉 LLM 做什么，然后它直接在你电脑上执行代码。
- 你需要文件操作——创建/编辑照片、视频、PDF、电子表格。
- 你想要浏览器和电脑控制（OS 模式，支持 Anthropic computer-use）。
- 你想要完整的互联网访问，无文件大小和时间限制。

## 什么时候别选

- 你不能接受在你的机器上无沙盒执行代码。每条命令都是真实的。
- 你需要企业 SLA 或技术支持。
- 你想要带 git 集成、PR 工作流和项目上下文的 coding agent。看 Claude Code 或 Aider。
- 你需要多 agent 编排或团队工作流。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 代码执行 | 很强 | Python、JS、Shell——直接在你的机器上 |
| 文件操作 | 强 | 创建和编辑文件、图片、视频、PDF |
| 电脑控制 | 中 | OS 模式，支持 Anthropic computer-use |
| 模型灵活性 | 强 | 支持云端和本地模型 |
| 安全 / 沙盒 | 弱 | 无内置沙盒——在你的真实机器上运行 |
| Git / 项目上下文 | 弱 | 不是为仓库感知的 coding 工作流设计的 |

## 使用代价

复杂度 Low 到 Medium。pip 安装，指定模型，开始对话。LLM API 费用是主要成本。真正的代价是风险管理——你在给 LLM 无沙盒执行任意代码的权限。

## 最后一句

Open Interpreter 是从自然语言到本地代码执行的最直接路径。能力是真实的；风险也是真实的。把它当锋利的工具，不是安全的工具。
