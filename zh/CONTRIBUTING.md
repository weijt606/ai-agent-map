# Contributing

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](CONTRIBUTING.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../CONTRIBUTING.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](README.md)

AI Agent Map 不追求变成“最长的 agent 链接列表”。

这个仓库刻意把门槛设窄：如果一页内容不能明显帮助读者更快做选择，那它大概率不该进来。

## 欢迎补什么

- 真正会进入主流 shortlist 的 agent profile。
- 从具体问题出发的 use-case 指南。
- 确实会被放在同一轮决策里的 comparison 页面。
- 产品边界变化、重命名、理解偏差带来的准确性修正。

## 不欢迎补什么

- 纯链接堆积。
- 复制官网营销文案。
- 把未核验的命名或产品边界写成既定事实。
- 没有决策价值的泛化排行榜。
- 没有明确使用权的 vendor logo、截图或品牌素材。

## 核心写法规则

- 为选型而写，不为热度而写。
- 必须同时写清楚 fit 和 anti-fit。
- 多写现实 trade-off，少写架构术语堆叠。
- 控制结论力度。属于编辑判断的，就按编辑判断来写。
- 如果产品公开边界本身很乱，要明确告诉读者。

## 核验标准

改 profile 之前，优先核对当前的一手来源：

- 官方产品页
- 官方文档
- 官方仓库
- 官方 release notes / changelog

如果一个项目有多个表面，不要偷懒合并成一个模糊描述。常见要分开的情况：

- 主产品 vs CLI companion
- 托管产品 vs 开源 SDK
- 当前产品 vs 已废弃 API

如果映射仍不确定，要在页面和索引里显式标成 provisional。

## 法律与版权边界

- 不直接粘贴厂商营销段落。
- 默认不要复用厂商截图。
- 默认不要在 banner 或插图里使用官方 logo。
- 优先使用原创图示、原创插画和纯文字标签。
- 使用商标名时，只用于识别产品本身，不暗示合作、背书或官方关系。

## 推荐贡献流程

1. 先确定你补的是 profile、use case 还是 comparison。
2. 先核验当前产品边界，再动笔。
3. 写到刚好足够帮助读者决策，不要写胖。
4. 如果命名、成熟度、定位有歧义，直接写 caveat。
5. 同步检查相关索引和 comparison 表，保持用词一致。

## Profile 自检清单

- 官方入口还是当前有效的吗？
- 写的是现在的产品，而不是旧版本 launch post 里的产品吗？
- 多个表面差异明显时，是否明确区分了？
- 是否清楚写了什么时候该选？
- 是否清楚写了什么时候别选？
- 如果是 provisional mapping，是否显式标出来了？

## 风格说明

- 根目录默认英文，中文用镜像文件单独维护。
- 文风要实用、轻松、易读。
- 避免论文腔和过度抽象。
- 即使参考官方资料，也尽量用自己的话重写。

## 如果拿不准

优先提一个窄范围准确性修正，而不是大范围重写。

准确性比覆盖面更重要。