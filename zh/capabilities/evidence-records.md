# 证据记录

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](evidence-records.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../capabilities/evidence-records.md)
[![矩阵](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E7%9F%A9%E9%98%B5-0d9488?style=for-the-badge&labelColor=0f766e)](matrix.md)

[能力矩阵](matrix.md)把每个格子打成 ● / ◐ / ○ / —。光一个符号会随时间失效：半年后没人记得它当时对应的是**哪个版本**、在**哪里**验证的、**什么时候**验证的。于是读者无法核实、维护者也无法反驳——只能吵。

本页解决这个问题。每个矩阵格子都可以带一条紧凑的**证据记录**：符号还在，但现在它和背后的证据一起走。格子变得可核查，而不只是可阅读。

> 下面的记录 schema 来自 **[u/teugent](https://www.reddit.com/user/teugent)**，是他在 [r/AI_Agents 帖子](https://www.reddit.com/r/AI_Agents/comments/1v56023/)里提出的。感谢——如果你看到这里，欢迎把你标准版的证据记录 schema 贴到那个帖子里，好让我们逐字段对齐。

## 记录 schema

每个带证据的格子就是一条记录，含以下字段：

| 字段 | 含义 |
| --- | --- |
| `claim` | 断言的那项能力，一句话 |
| `score` | 现有符号——● / ◐ / ○ / —（不变） |
| `scope` | 该断言适用的产品版本 / 档位 / 套餐 |
| `source` | 验证该断言的出处链接 |
| `version` | 产品版本，或核对该断言时所依据的日期/构建 |
| `review_date` | 本格子最后一次验证的时间 |
| `evidence_type` | `documentation` · `source` · `demo` · `benchmark` 之一 |
| `recheck_condition` | 什么情况应触发重新验证（例如新的大版本） |

### 让格子可裁决的那条唯一规则：把 `evidence_type` 和 `claim` 分开

`documentation` 只能证明**项目自己宣传了什么**。只有 `source`（代码确实这么做）、可复现的 `demo`、或 `benchmark`，才能证明**实测行为**。仅靠 `documentation` 撑起的格子，是一条*关于意图的断言*，不是测量——这没问题，只要它讲清楚。当两个人对一个格子有分歧时，就是这个字段来定案："你的 ● 只是 `documentation`；这是一个反例 `demo`。"绝不要靠省略这个字段，把营销页面洗成实测行为。

证据强度，由弱到强：

```
documentation  <  source  <  demo  ≈  benchmark
（宣传的）        （确实做） （复现的）   （实测的）
```

## 记忆不是一个格子

"有记忆"是矩阵上最被过载的一个符号。两个都打 ● 的项目，行为可能天差地别：一个默默把每一轮永久存下来，另一个只是个重启即失的草稿本。共用一个标签，恰好把选型者最在意的差异藏了起来。

所以记忆格子拆成一套生命周期**子 schema**——四个关于*实际行为*的问题，而不是一个名字：

| 子字段 | 它回答的问题 |
| --- | --- |
| `what_may_be_stored` | 到底有什么能被写进记忆？ |
| `what_may_enter_active_context` | 存下来的东西里，有什么能回到模型上下文？ |
| `how_a_record_is_selected` | 一条存下的记录，靠什么机制被选中召回？ |
| `can_be_superseded_or_removed` | 一条记录能否被更新、覆盖或删除——怎么做？ |

比的是*这四项*，不是"记忆"这个词。

## 完整样例：jcode 记忆格子

其余每个记忆格子都应照这个模板来。[jcode](../agents/jcode.md) 的被动语义记忆是它的招牌，所以它的 `Mem` 格子打 **●**——下面就是这个符号连同它的证据。

| 字段 | 值 |
| --- | --- |
| `claim` | jcode 把每一轮对话嵌成语义向量，并通过记忆图谱**自动召回**相关历史（可选校验侧 agent），而不是要模型手动调记忆工具；同时也暴露显式的记忆 + 会话检索工具。 |
| `score` | ●（核心强项） |
| `scope` | jcode 开源 harness（`1jehuang/jcode`），默认构建；被动记忆默认开启，非付费或需手动开启的档位。 |
| `source` | https://github.com/1jehuang/jcode · https://jcode.sh ——另见[记忆方案](../comparisons/memory-approaches.md) |
| `version` | Pre-1.0，`main` 分支，读取于 2026-07-22（jcode 年轻且迭代快，记忆子系统仍在settling）。 |
| `review_date` | 2026-07-25 |
| `evidence_type` | **`documentation`**——依据项目自己的 README/官网对被动召回的描述得出。尚未独立复现，所以这是一项*宣传的*强项，不是实测的。见 `recheck_condition`。 |
| `recheck_condition` | jcode 任何触及记忆子系统的发版、或被动召回不再默认时，重新验证。**一旦本地复现了自动召回和校验侧 agent，就把 `evidence_type` 从 `documentation` → `demo`/`source`**。 |

### 本格子的记忆生命周期子 schema

| 子字段 | 值 |
| --- | --- |
| `what_may_be_stored` | 每一轮对话，嵌成语义向量写入记忆图谱；用户显式保存的记忆条目；完整会话记录（可检索）。 |
| `what_may_enter_active_context` | 在当前轮被自动判定为相关的历史轮/图谱节点；显式记忆查询或会话检索工具调用返回的结果。 |
| `how_a_record_is_selected` | 每轮对向量图谱做被动语义相似度检索（无需手动调工具），可选校验侧 agent 对召回候选做过滤；外加按需的显式记忆 + 会话检索工具。 |
| `can_be_superseded_or_removed` | **[待验证]**——显式记忆工具意味着可增/可管，但*被动*图谱的更新/删除语义尚未独立确认。由 `recheck_condition` 标记。 |

注意子 schema 如何*把一个未知项浮出水面*（`can_be_superseded_or_removed`）——而"记忆"这一个词会把它埋掉。这正是全部意义所在。

## 分阶段推进

把这套东西一次性铺到 ~55 行 × 9 列的每个格子上，就变成一场数据迁移苦差，然后卡死。所以它分阶段落地，最便宜、价值最高的先做。每个阶段都独立有用——每做完一阶段矩阵都还能发。

| 阶段 | 范围 | 为何是这个顺序 |
| --- | --- | --- |
| **1** | 给每个现有格子加 `evidence_type` + `review_date`。 | 最便宜、价值最高：立刻告诉读者一个符号是*宣传*还是*实测*、有多旧——这正是光一个符号答不了的两个问题。 |
| **2** | 加 `scope` + `source` + `version` + `recheck_condition`。 | 让格子完全可核查、可反驳，并定义何时过期。每格更重，所以排在便宜的胜利之后。 |
| **3** | 把每个记忆格子展开成生命周期子 schema。 | 改动最深、列最窄——最后做，等记录机制在其余格子上验证过再动。 |

### 推进状态

| 阶段 | 状态 | 备注 |
| --- | --- | --- |
| 1 | ⏳ 未开始 | 在 issue 里跟踪。 |
| 2 | ⏳ 未开始 | — |
| 3 | 🟡 模板就绪 | jcode 记忆格子上面已跑通全流程；其余记忆格子待办。 |

## 如何新增或反驳一条记录

- **新增：** 复制上面的样例表格，把每个字段填满，再把矩阵格子链到你记录的标题——如 `[●](evidence-records.md#你的标题)`。符号保持可见；链接只是*加上*证据。
- **反驳：** 开 issue 点名该格子并附上更强的证据。`demo` 或 `source` 胜过 `documentation`；更新的 `review_date` 胜过陈旧的。因为字段是显式的，分歧靠证据裁决，而不是靠嘴。

记录保持轻量——一块填好的记录，不是一个数据库。目标是让格子能被*核查*，而不是让 schema 需要被*维护*。
