# AutoGLM（智谱）

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](autoglm.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/autoglm.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：AutoGLM 是智谱的手机与电脑操作 agent，有两种形态——一个免费的消费级应用，给每位用户**一台云手机和一台云电脑**去操作应用；以及 **Open-AutoGLM**，一个 Apache-2.0 的框架加 9B 模型，通过 ADB/HDC 驱动真实的 Android 或鸿蒙手机——这份名单里唯一你能自己跑起来的个人 agent。

## 快速看点

| 项目 | 结论 |
| --- | --- |
| 厂商 | 智谱（Z.ai） |
| 路线 | 消费级个人 agent |
| 开源 | **框架和手机模型开源**（[Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)，Apache-2.0）；消费级应用不开源 |
| 形态 | 操作云端设备的 iOS/Android 应用；操作你自己手机的自托管框架 |
| 状态 | 应用 **2025-08-19** 上线；App Store 最近一次更新是 **2026-07-09**（v2.0.20，新增 AutoClaw 入口）。Open-AutoGLM 最近一次推送是 **2026-03-06** |
| 在哪里跑 | 应用：每位用户一台云手机和一台云电脑，部署在智谱的数据中心——不碰你自己的设备。框架：你的手机，由你的电脑控制 |
| 模型 | AutoGLM-Phone-9B（中文应用）与 AutoGLM-Phone-9B-Multilingual，发布在 Hugging Face 和 ModelScope |
| 价格 | 中国区 App Store 免费；框架免费 |
| 官方页面 | https://apps.apple.com/cn/app/id6748391183 · https://github.com/zai-org/Open-AutoGLM |

## 什么时候选它

- 你想要**跨应用的手机自动化，但不想把自己的手机交给 agent**：应用是在云手机上操作的。
- 你想**自己掌控循环**：在这份名单里，Open-AutoGLM 是唯一能在自己的硬件和模型上跑手机 agent 的方式，这也让它和本地图其他地方的开源 harness 站在一起。

## 什么时候不选它

- 你想要一个仍在积极开发的产品。应用最后一次更新在 7 月，开源仓库自 3 月起没有推送；智谱的消费级重心已经转向 AutoClaw。
- 你不能接受自托管路线的权限面：驱动真实手机意味着要在手机上打开 USB/无线调试（ADB 或 HDC）。

## 结论

对"该不该让 agent 操作我的手机"给出的两个答案：应用说*换一台云端的手机*，开源框架说*自己来跑*。两者都说得通；但两者目前都不是智谱的投入重点，所以在它之上搭东西之前先看看活跃度。

## 来源

- [App Store 上的 AutoGLM（中国区）](https://apps.apple.com/cn/app/id6748391183)
- [zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)（README：Android 用 ADB、HarmonyOS NEXT 用 HDC；模型表）
