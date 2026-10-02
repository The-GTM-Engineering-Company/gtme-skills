# Inventory spec

Three tabs. Emit as CSVs into a private client output directory outside this public repository, then deliver per [publishing.md](publishing.md). Preserve any existing client decisions when refreshing an inventory.

Generate with a Python script using the `csv` module — never hand-write CSV, since cells contain commas and quotes. Validate before publishing:

```bash
python3 -c "
import csv
for fn in ['tab1_field_inventory.csv','tab2_value_maps.csv','tab3_open_decisions.csv']:
    rows=list(csv.reader(open(fn)))
    hdr=len(rows[0]); bad=[i for i,r in enumerate(rows) if len(r)!=hdr]
    tabs=sum(1 for r in rows for c in r if '\t' in c or '\n' in c)
    print(f'{fn}: {len(rows)-1} rows x {hdr} cols, ragged={bad or \"none\"}, paste-unsafe cells={tabs}')
"
```

`paste-unsafe cells` must be 0 — embedded tabs or newlines break the clipboard publish.

## Tab 1 — Field Inventory

One row per Clay data point. A single Clay field may appear on several rows if it has competing candidate targets; that is the point — the client picks.

| Column | Contents |
|---|---|
| Ref | Stable row number for referencing in review |
| Group | Identity / Location / Industry / Size / Descriptive / Metadata |
| Clay Field (JSON path) | Full path, e.g. `derived_datapoints.subindustry` |
| Clay Type | string / integer / array / range-string / datetime |
| Sample — {Company A} | Real value from payload 1 |
| Sample — {Company B} | Real value from payload 2 |
| Candidate CRM Field (Label) | Human-readable target |
| CRM API Name | Exact API name. `(no target)` if none exists |
| CRM Type / Length | e.g. `string / 80`, `picklist / 255` |
| Picklist (Restricted?) | `No` / `Yes - RESTRICTED` / `No (UNRESTRICTED)` |
| CRM Populated % | Measured. `not measurable` for long-text |
| Existing CRM Value Format | What the data actually looks like today |
| Transform Needed? | `No` / `Yes` / `Yes - TYPE MISMATCH` |
| Transformation Rule | Concrete and executable in Clay |
| Rec. Write Mode | `OVERWRITE` / `WRITE IF EMPTY` / `DO NOT WRITE` / `see D-NN` |
| Risk / Error Mode | What breaks, and whether it errors loudly or silently |
| Owned by Another Sync? | `No` / `YES - vendor owns` |
| **DECISION** | **Blank — client fills** |
| **OWNER** | **Blank — client fills** |
| Notes | Evidence, caveats, gotchas |

Rules:

- **Never leave a Clay data point off the sheet.** If there is no target, the row still exists with `(no target)` and `NO TARGET — GAP`. Silent omission reads as "covered".
- Cite measured numbers, not impressions. `17.9%` beats "sparsely populated".
- Where a Clay data point has no existing CRM home, the row still exists. Set API Name to `(no target)` and Write Mode to `NO TARGET — GAP`, and use Notes to say what the data is good for. These are the **gap candidates** the client reviews to decide whether a field is worth creating. Do not invent API names, types, or lengths — describe the data, not the schema.
- Roll the gap candidates up into a single Tab 3 decision ("which of these N Clay data points justify a new field?"), so the client makes one batched call instead of N scattered ones.
- Flag *why* a write mode is recommended, so the client can disagree with the reasoning rather than just the conclusion.

## Tab 2 — Value Maps

The lookup tables, one block per mapping. Repeat the Map ID down the rows; leave Map Name blank after the first row of a block.

| Column | Contents |
|---|---|
| Map ID | `VM-1`, `VM-2`, … |
| Map Name | e.g. `Employee band: Clay size -> hs_employee_range` |
| Source (Clay) | Exact incoming value |
| Target (CRM) | Exact outgoing value |
| Confidence | `Exact` / `Likely` / `Ambiguous` / `Gap` / `Blocked` / `To build` |
| Notes | Why, and what is unresolved |

Include a row for values that **cannot** be mapped (`Blocked`, `Gap`). A visible gap gets fixed; an omitted one ships.

Typical maps: country ISO-2 → name · employee band → CRM band vocabulary · Clay industry → CRM industry (per tier) · region → territory · revenue band → number.

## Tab 3 — Open Decisions

| Column | Contents |
|---|---|
| ID | `D-01`, `D-02`, … |
| Decision Needed | The question, in one line |
| Why It Matters | Consequence of getting it wrong |
| Options | `A) … B) … C) …` |
| Recommendation | Yours, with reasoning |
| Owner | Who decides |
| **DECISION** | **Blank** |
| Status | `OPEN` / `OPEN - BLOCKING` / `RESOLVED` |

Mark `OPEN - BLOCKING` only where downstream rows genuinely cannot be finalised — typically a vendor-owned namespace or an unresolved match key. Overusing it destroys the signal.

Decisions that recur across engagements: write posture for run 1 · standard address fields vs enrichment namespace · whether to touch the industry picklist at all · how to store range values · non-US state handling · HQ selection rule · multi-match guard · which enrichment source wins where several already exist.
