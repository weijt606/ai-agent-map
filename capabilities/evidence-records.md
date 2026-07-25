# Evidence Records

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/capabilities/evidence-records.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](evidence-records.md)
[![Matrix](https://img.shields.io/badge/BACK-MATRIX-0d9488?style=for-the-badge&labelColor=0f766e)](matrix.md)

The [capability matrix](matrix.md) scores each cell as ● / ◐ / ○ / —. A bare mark ages badly: six months later nobody remembers *what edition* it applied to, *where* it was checked, or *when*. So a reader can't verify it and a maintainer can't dispute it — they can only argue.

This page fixes that. Every matrix cell can carry a compact **evidence record**: the mark stays, but it now travels with the evidence behind it. Cells become checkable, not just readable.

> The record schema below comes from **[u/teugent](https://www.reddit.com/user/teugent)**, who raised this in the [r/AI_Agents thread](https://www.reddit.com/r/AI_Agents/comments/1v56023/). Thanks — and if you're reading this, drop your canonical evidence-record schema in that thread so we can align field-for-field.

## The Record Schema

Each cell that carries evidence is one record with these fields:

| Field | What it holds |
| --- | --- |
| `claim` | The capability being asserted, in one sentence |
| `score` | The existing mark — ● / ◐ / ○ / — (unchanged) |
| `scope` | The product edition / tier / plan the claim applies to |
| `source` | Link to where the claim is verified |
| `version` | Product version, or the date/build the claim was checked against |
| `review_date` | When this cell was last verified |
| `evidence_type` | One of `documentation` · `source` · `demo` · `benchmark` |
| `recheck_condition` | What should trigger re-verification (e.g. a new major version) |

### The one rule that makes cells resolvable: keep `evidence_type` separate from the `claim`

`documentation` only establishes **what a project advertises**. Only `source` (the code does it), a reproducible `demo`, or a `benchmark` establish **observed behavior**. A cell backed solely by `documentation` is a *claim about intent*, not a measurement — and that is fine, as long as it says so. When two people disagree about a cell, this field is what settles it: "your ● is `documentation`-only; here's a `demo` that contradicts it." Never launder a marketing page into observed behavior by omitting the field.

Evidence strength, weakest to strongest:

```
documentation  <  source  <  demo  ≈  benchmark
(advertised)      (it does)   (reproduced)  (measured)
```

## Memory Is Not One Cell

"Has memory" is the most overloaded mark on the matrix. Two projects both scored ● can behave nothing alike: one silently persists every turn forever, the other holds a scratchpad that evaporates on restart. A shared label hides exactly the difference a selector cares about.

So a memory cell decomposes into a lifecycle **sub-schema** — four questions about *actual behavior*, not a name:

| Sub-field | The question it answers |
| --- | --- |
| `what_may_be_stored` | What can be written to memory at all? |
| `what_may_enter_active_context` | Of what's stored, what can come back into the model's context? |
| `how_a_record_is_selected` | By what mechanism is a stored record chosen for recall? |
| `can_be_superseded_or_removed` | Can a record be updated, overridden, or deleted — and how? |

Compare *these four*, not the word "memory."

## Worked Example: jcode Memory Cell

The template every other memory cell should follow. [jcode](../agents/jcode.md)'s passive semantic memory is its headline feature, so its `Mem` cell scores **●** — here is that mark with its evidence attached.

| Field | Value |
| --- | --- |
| `claim` | jcode embeds each conversation turn as a semantic vector and **auto-recalls** relevant history through a memory graph (optional verifier side-agent), instead of requiring the model to call memory tools by hand; explicit memory + session-search tools are also exposed. |
| `score` | ● (core strength) |
| `scope` | jcode OSS harness (`1jehuang/jcode`), default build; passive memory is on by default, not a paid or opt-in tier. |
| `source` | https://github.com/1jehuang/jcode · https://jcode.sh — see also [memory approaches](../comparisons/memory-approaches.md) |
| `version` | Pre-1.0, `main` branch as read on 2026-07-22 (jcode is young and fast-moving; the memory subsystem is still settling). |
| `review_date` | 2026-07-25 |
| `evidence_type` | **`documentation`** — established from the project's own README/site describing passive recall. Not yet independently reproduced, so this is an *advertised* strength, not a measured one. See `recheck_condition`. |
| `recheck_condition` | Re-verify on any jcode release that touches the memory subsystem, or if passive recall stops being a default. **Upgrade `evidence_type` from `documentation` → `demo`/`source`** once auto-recall and the verifier side-agent are reproduced locally. |

### Memory lifecycle sub-schema for this cell

| Sub-field | Value |
| --- | --- |
| `what_may_be_stored` | Every conversation turn, embedded as a semantic vector into a memory graph; explicit user-saved memory entries; full session transcripts (searchable). |
| `what_may_enter_active_context` | Prior turns / graph nodes auto-selected as relevant on the current turn; results returned by explicit memory-lookup or session-search tool calls. |
| `how_a_record_is_selected` | Passive semantic-similarity retrieval over the vector graph on each turn (no manual tool call needed), with an optional verifier side-agent filtering recalled candidates; plus on-demand explicit memory + session-search tools. |
| `can_be_superseded_or_removed` | **[needs verification]** — explicit memory tools imply add/manage, but the update/deletion semantics of the *passive* graph are not yet independently confirmed. Flagged by `recheck_condition`. |

Note how the sub-schema *surfaces an unknown* (`can_be_superseded_or_removed`) that the single word "memory" would have buried. That is the whole point.

## Staged Rollout

Applied cell-by-cell across ~55 rows × 9 columns, all at once, this becomes a data-migration chore and stalls. So it ships in phases, cheapest-and-highest-value first. Each phase is independently useful — the matrix stays shippable after every one.

| Phase | Scope | Why this order |
| --- | --- | --- |
| **1** | Add `evidence_type` + `review_date` to every existing cell. | Cheapest, highest value: instantly tells a reader whether a mark is *advertised* or *observed*, and how stale it is — the two questions a bare mark can't answer. |
| **2** | Add `scope` + `source` + `version` + `recheck_condition`. | Makes cells fully checkable and disputable, and defines when they expire. Heavier per-cell, so it follows the cheap win. |
| **3** | Expand every memory cell into the lifecycle sub-schema. | Deepest change, narrowest column — do it last, once the record mechanism is proven on the rest. |

### Rollout status

| Phase | Status | Notes |
| --- | --- | --- |
| 1 | ⏳ Not started | Tracked in the issue. |
| 2 | ⏳ Not started | — |
| 3 | 🟡 Template ready | jcode memory cell worked end-to-end above; remaining memory cells pending. |

## How To Add Or Dispute A Record

- **Add one:** copy the worked-example tables, fill every field, and link the matrix cell to your record's heading — e.g. `[●](evidence-records.md#your-heading)`. Keep the mark visible; the link only *adds* the evidence.
- **Dispute one:** open an issue naming the cell and attaching stronger evidence. A `demo` or `source` beats `documentation`; a fresher `review_date` beats a stale one. Because the fields are explicit, the disagreement resolves on evidence instead of opinion.

Keep records lightweight — a filled record block, not a database. The goal is a cell someone can *check*, not a schema someone has to *maintain*.
