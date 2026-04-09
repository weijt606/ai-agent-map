# GitHub Copilot

[![中文](https://img.shields.io/badge/中文-当前页面-1f6feb?style=flat-square)](github-copilot.md)
[![English](https://img.shields.io/badge/English-Read%20in%20English-9ca3af?style=flat-square)](../../agents/github-copilot.md)

一句话：现在的 GitHub Copilot 更像一个 agent 平台，而不是单纯补全工具。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | GitHub / Microsoft |
| 路线 | VS Code + GitHub 生态里的多表面 agent 平台 |
| 是否开源 | 否 |
| 最适合 | 本地、CLI、cloud workflow 需要串起来的团队 |
| 主要代价 | 最佳体验强依赖 VS Code / GitHub 生态 |
| 官方入口 | https://code.visualstudio.com/docs/copilot/agents/overview |

## 什么时候选它

- 你的团队主要工作在 VS Code 和 GitHub 上。
- 你希望 Ask、Plan、Agent、CLI、cloud path 放在同一个入口里。
- 你希望 issue、PR、review 和编辑器执行能顺着一条工作流走。

## 什么时候别选

- 你不在 VS Code / GitHub 生态里工作。
- 你需要完全开源或强自托管。
- 你只想要一个极简、单表面的 agent。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| Local execution | 强 | 编辑器内体验已经不是附属功能 |
| Cloud delegation | 强 | 适合把任务接到 GitHub 工作流里 |
| Workflow handoff | 强 | 本地到云端切换是亮点 |
| Permission control | 强 | 控制粒度比较清楚 |
| Custom agents | 中 | 适合做角色化和专用入口 |

## 使用代价

复杂度是 Medium。基础使用很轻，但一旦你开始混用本地 agent、CLI、cloud path 和权限模式，工作流会明显变复杂。

## 最后一句

GitHub Copilot 的优势不是某一个 agent 特别强，而是它把主流开发动作塞进了同一条链路里。