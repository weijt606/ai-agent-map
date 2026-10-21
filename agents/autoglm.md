# AutoGLM (Zhipu)

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/autoglm.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](autoglm.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: AutoGLM is Zhipu's phone-and-computer-use agent in two forms — a free consumer app that gives each user **a cloud phone and a cloud computer** to operate apps on, and **Open-AutoGLM**, an Apache-2.0 framework and 9B models that drive a real Android or HarmonyOS phone over ADB/HDC — the only personal agent on this list you can run yourself.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Zhipu (Z.ai) |
| Route | Consumer personal agent |
| Open source | **The framework and phone models are open** ([Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM), Apache-2.0); the consumer app is not |
| Form factor | iOS/Android app operating cloud devices; self-hosted framework for your own phone |
| Status | App released **Aug 19 2025**; last App Store update **July 9 2026** (v2.0.20, adding an AutoClaw entry). Open-AutoGLM last pushed **Mar 6 2026** |
| Where it runs | App: one cloud phone and one cloud computer per user, in Zhipu's data centres — your own device is not touched. Framework: your phone, controlled from your machine |
| Model | AutoGLM-Phone-9B (Chinese apps) and AutoGLM-Phone-9B-Multilingual, published on Hugging Face and ModelScope |
| Price | App free on the China App Store; framework free |
| Official pages | https://apps.apple.com/cn/app/id6748391183 · https://github.com/zai-org/Open-AutoGLM |

## When To Pick It

- You want **cross-app phone automation without giving an agent your phone**: the app works on a cloud phone instead.
- You want to **own the loop**: Open-AutoGLM is the one way on this list to run a phone agent on your own hardware and model, which also puts it next to the open harnesses elsewhere on this map.

## When Not To Pick It

- You want an actively developed product. The app's last update was in July and the open repository has not been pushed since March; Zhipu's consumer attention has moved to AutoClaw.
- You cannot accept the permission surface of the self-hosted route: driving a real phone means USB/wireless debugging (ADB or HDC) enabled on it.

## Bottom Line

Two answers to "should an agent operate my phone": the app says *use a phone in the cloud instead*, the open framework says *run it yourself*. Both are sound; neither is currently where Zhipu is investing, so check activity before you build on it.

## Sources

- [AutoGLM on the App Store (China)](https://apps.apple.com/cn/app/id6748391183)
- [zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) (README: ADB for Android, HDC for HarmonyOS NEXT; model table)
