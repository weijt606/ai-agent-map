# Today

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](today-ai.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/today-ai.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话定位：一个主打"记得你、主动帮你"的个人 AI 助理，分中国版（todayai.cn）和国际版（today.ai）。它把记忆、早晚间简报和定时任务放在中心，任务在厂商的云端电脑上跑，也可以经 Chrome 插件在你自己已登录的浏览器里点击、填表；提交表单、下单、付款这类关键步骤由你确认或接手。两个版本都写明不用能识别你的用户内容训练面向公众的基础模型。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | 中国版：**汇翮（上海）智能科技有限公司**（隐私政策与服务协议里的运营方）；国际版：**Today AI PTE. LTD.**（App Store 卖家，条款适用新加坡法律）。创始人齐俊元（*媒体*） |
| 路线 | 消费级个人 agent |
| 开源 | 否 |
| 形态 | 桌面端 Mac（Apple 芯片 / Intel，macOS 14+）、Windows（x64 / ARM64）、Linux（x64 / ARM64，AppImage）；iOS；Android（中国版官网直接给 APK，国际版走 Google Play）；网页；Chrome 插件（中国版、国际版各一个） |
| 状态 | 已上线。App Store 记录的首发日期：国际版 2026-08-27，中国版 2026-10-04；中国版 iOS 当前 1.24.0（2026-10-30）。媒体报道国内版 9 月 24–25 日发布（*媒体*） |
| 在哪里干活 | 自己"稳定的云端电脑"，"可以打开浏览器、处理文件、运行代码"，官网标注"24 小时在线"；装了插件时，也在**你的 Chrome**里读页面、点击、填表 |
| 模型 | 中国版经**阿里云百炼、腾讯云 TokenHub、金山云**调用"DeepSeek 等模型"，语音走阿里云 DashScope；国际版写的是 AI 服务商"可能包括" AWS、Anthropic、OpenAI。具体用哪个模型没有写 |
| 价格 | 中国版"**基础版永久免费**"，新用户"注册即领 3亿 Tokens，畅享 3 个月 Pro 权益"（todayai.cn，2026-10-31 读取）；中国版 Pro 价格官网没列。国际版 App Store 内购：**Pro $20/月、Ultra $200/月**；符合条件的账号可试用 7 天 Pro，Ultra 不提供试用 |
| 地区 | 中国大陆（中国版，需中国大陆手机号账号）+ 国际版 |
| 官方页面 | https://todayai.cn · https://today.ai/?international=1 |

## 它是什么

Today 把自己定位成"懂你所想，为你先行的个人 AI 助理"。它有三条主线：

- **记忆**："鲜活的记忆系统"，记住"你的日常、身边的人、偏好，以及你持续关注的目标"，"所有上下文都由你掌控"。中国版 App Store 介绍写明，记住的内容你可以查看、修改或删除。
- **主动**：根据你分享和授权的信息生成早间简报、晚间简报，跟进未完成的事，"在合适的时候提醒你，或建议下一步"。官网示例里有"邮件整理 每 2 小时""工作日 9:00"这样的周期任务；App Store 介绍写明"需要定期处理的事情，也可以设为定时任务"。
- **执行**："规划步骤、使用工具、检查进度并向你汇报"，多项任务可以在后台同时推进，你之后再看结果。连接器覆盖"日历、邮件、笔记、文件、消息、项目工具"（官网），中国版 App Store 写的是"邮件、日历、文档、读书、办公平台、运动等服务"。社区 Skills 可以在 Today 里运行。除了 Today 应用，也能"通过支持的消息渠道"和它沟通。

移动端底部标签是聊天、Today、记忆、任务，中国版第五个标签叫 Spark，国际版叫 Capabilities。

## 什么时候选它

- 你在中国大陆，想要一个以**记忆和主动提醒**为中心的助理，而不是只等你提问的聊天应用；它还能把健康数据（HealthKit / Health Connect）、日历和邮件拼进同一份简报。
- 你在好几种设备之间切换：它给了 Mac、Windows、Linux 三个桌面端，iOS、Android 两个手机端，外加网页。
- 你想让它在你**已登录的网站**里干活：装上 Chrome 插件，它能读你打开的标签页、点击、输入、填表，还能查浏览历史和书签。

## 什么时候不选它

- 你需要一份写明的审批规则。它只说提交表单、下单、付款等"关键步骤"由你确认或接手，发送、修改等外部操作"按具体功能由你确认"，没有公开逐动作的规则或禁止清单。
- 你想先知道中国版 Pro 多少钱。官网和中国区 App Store 页面都没列价格。
- 你要按具体服务挑连接器。官网只写了类别，没有公开连接器名单；媒体报道的名单彼此对不上。

## 权限与数据

**训练。** 中国版隐私政策（2026-10-25 更新并生效）："除非我们另行清晰说明并依法取得您的同意，我们不会使用可以识别您的用户内容训练面向公众的基础模型"；匿名化后的数据可用于安全、可靠性和服务质量分析。国际版隐私政策（2026-08-31 更新）写的是不允许 AI 服务商用你可识别的聊天内容、附件或健康数据训练其公开的基础模型。

**数据在哪。** 中国版个人信息"原则上存储在中国大陆境内"；实时语音对话"可能使用阿里云位于新加坡的实时语音模型服务"，开启前要你单独同意。发给第三方 AI 服务商之前，应用内会说明发什么、发给谁，并取得你的明确同意；不同意，依赖它的 AI 功能就用不了。国际版说数据可能被转移到你所在国以外处理。

**保留。** 中国版：用户内容"保存至您删除、账号注销或者相关目的实现"。国际版：AI 相关内容作为账号历史保存，可以查看和删除；在应用里删除账号会删掉聊天记录、记忆、任务和从连接应用同步来的数据。

**设备权限。** 中国版 Android 可以在你逐项同意后读短信、读写通讯录和日历、读取并清除其他应用的通知、读应用使用时长、访问全部文件。Chrome 插件会把网页内容、截图、网址以及相关的浏览历史或书签结果发回 Today 处理；断开插件"不会自动删除已经发送的数据"。

**审批。** 中国版 App Store 介绍："你可以查看操作过程，随时接管或停止。涉及提交表单、下单、付款等关键步骤时，由你确认或接手完成。"插件说明建议你在任务里写清楚边界，例如"把这张报名表填好，先不要提交"。

## 结论

一个把记忆、简报和定时任务做在中心的个人助理，桌面、手机、网页都能用，训练和数据存放写得具体：不拿可识别内容训练公开基础模型，中国版数据原则上留在中国大陆。短板在控制面：审批只写到"关键步骤由你确认"，连接器没有公开名单，中国版 Pro 的价格也没写。适合想要一个主动型助理、又想把数据留在中国大陆的人先用免费版加新用户额度试一试；要把付款或对外发信交给它之前，先在应用里看清楚它到底会在哪一步停下来问你。

## 来源

- [todayai.cn](https://todayai.cn/) · [国际版 today.ai](https://today.ai/?international=1) · [中国版下载页](https://todayai.cn/downloads) · [国际版下载页](https://today.ai/downloads)
- [中国版隐私政策（2026-10-25）](https://todayai.cn/privacy) · [中国版用户服务协议](https://todayai.cn/terms) · [国际版 Privacy Policy（2026-08-31）](https://today.ai/privacy) · [国际版 Terms of Service（2026-09-07 生效）](https://today.ai/terms)
- [Today 中国区 App Store](https://apps.apple.com/cn/app/id6775764827) · [Today 美区 App Store（含内购价格）](https://apps.apple.com/us/app/id6760608312) · [Google Play](https://play.google.com/store/apps/details?id=ai.today.android.app) · [Chrome 插件「Today AI 中国版」](https://chromewebstore.google.com/detail/edkhmdfegifiidpkfifcoiafjgbopggj) · [Chrome 插件「Today AI」](https://chromewebstore.google.com/detail/today-ai/adhckffghihcelhbpgbkbepmlhcmofjc)
- *媒体*：[量子位，2026-09-24](https://finance.sina.cn/2026-09-24/detail-inisxnuz4997238.d.html)（创始人、发布）· [融中财经 / 36氪，2026-10-22](https://eu.36kr.com/zh/p/4036453319660681)（据五源资本披露累计融资超过 2 亿美元；当时写的新用户权益是 1亿 Token 加一个月 Pro，与官网现在写的 3亿 Tokens 加 3 个月 Pro 不同，本页以官网为准）
