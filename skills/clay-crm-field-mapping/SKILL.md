---
name: clay-crm-field-mapping
description: Audit how Clay enrichment should map to Salesforce or HubSpot fields, including population, value transformations, match keys, and write blockers. Produce a review inventory before configuring write-back.
---

# Clay → CRM Field Mapping

Build a decision aid from the client's actual schema and sample payloads. CRM inspection is read-only: this task does not create fields, update records, or configure a Clay write-back. Every proposed mapping ends with a client decision.

## Scope and connection

Identify the intended client, CRM account/portal, environment, available permissions, and one object: Account/Company or Contact/Person. Use the target already supplied; ask if the target is ambiguous or the observed connection does not match. The operator signs in through their own tools. Do not collect credentials or print tokens.

Use [Salesforce](references/salesforce.md) or [HubSpot](references/hubspot.md) for the relevant inspection. Tool names and schemas vary by connector; discover the available read operations instead of assuming a particular server ID.

Obtain at least two actual Clay payloads from the table being mapped. Keep payloads, schema dumps, and outputs in a private client workspace outside this public skill. For Contact/Person, also read [contact mapping](references/contacts.md).

## Build the evidence

1. Read the live schema: API/internal name, label, type, length, options, calculation/read-only flags, uniqueness, and external IDs. Map to existing fields first.
2. Inspect write blockers: validation/property rules, workflows, triggers, other writers, match-key collisions, and association rules. If the tools cannot inspect one of these, mark it unverified rather than absent.
3. Measure population and actual value vocabulary. Use consistent filters and denominators; label samples, API ceilings, permissions gaps, and unsupported counts. A top-values sample is not a distinct count.
4. Flatten every supplied payload, including every array element. Mark paths present in only some records. Read [mapping pitfalls](references/landmines.md) before recommending transformations.
5. Identify each candidate target and the transformation it needs. A vendor prefix is a clue to ownership, not proof; check the integration and field history where available. Propose no competing writer until ownership is resolved.
6. Record useful unmapped data as a gap candidate. Describe its value; do not invent a new field schema or create anything during this audit.

## Deliver and review

Produce **Field Inventory**, **Value Maps**, and **Open Decisions** following [the inventory spec](references/inventory-spec.md). Preserve blank decision/owner cells for the client. Keep all payload paths represented, including gaps and rejected mappings.

Use [publishing guidance](references/publishing.md) to deliver CSVs or populate the agreed review spreadsheet. An instruction to audit does not authorize creating or sharing an external sheet. Respect a supplied spreadsheet URL and any existing content.

Walk through blocking decisions: record match key, fill-if-empty/overwrite posture, ownership conflicts, association policy, and unmatched values. A later write-back task should use approved decisions and a scoped pilot; an inventory is not approval to write.

See [the synthetic example](examples/company-review.md) for the output shape.
