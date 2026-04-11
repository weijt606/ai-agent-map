# AI Edge Gallery

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](ai-edge-gallery.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/ai-edge-gallery.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：AI Edge Gallery 更适合被理解成一个端侧本地 assistant 沙盒，而不是主流 coding agent。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | Google AI Edge |
| 路线 | 端侧本地 assistant 沙盒 |
| 是否开源 | 是 |
| 最适合 | 想在手机或平板上尝试本地模型、agent skills、多模态输入和私有 on-device actions |
| 主要代价 | 它主要是移动端 edge runtime 沙盒，不在代码自动化的主路径上 |
| 官网 | https://ai.google.dev/edge |
| GitHub 仓库 | https://github.com/google-ai-edge/gallery |

## 什么时候选它

- 你想看现在手机或平板上的本地 assistant 到底能做到什么。
- 你更在意隐私、离线运行和移动端 actions，而不是云端 orchestration。
- 你想在真实设备上测试模型选择、prompt、agent skills 和 edge-device 取舍。

## 什么时候别选

- 你要的是 repo-local coding automation 或 issue-to-PR 执行。
- 你需要 desktop-first orchestration 平台和开发者工作流控制面。
- 你要的是成熟企业 agent 表面，而不是实验性 edge app。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| On-device execution | 很强 | 本地移动端推理是整个产品故事的中心 |
| Model sandboxing | 很强 | 很适合在真实硬件上试不同本地模型 |
| Agent skills / actions | 中等 | 有价值，但不是唯一看点 |
| Privacy / offline usage | 很强 | 这是它最值得看的点之一 |
| Coding automation | 弱 | 这不是它的强项 |

## 使用代价

复杂度是 Low。它比大多数自托管 runtime 更容易开始，但真正的限制会转移到设备兼容性、内存上限，以及它本质上更像 edge experimentation surface，而不是完整 workflow 平台。

## 最后一句

如果你的问题是“本地手机 assistant 现在完全离线能做到什么”，AI Edge Gallery 值得看；如果你的问题是“团队应该选哪个 coding agent”，它通常不是第一站。