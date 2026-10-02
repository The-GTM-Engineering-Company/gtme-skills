---
name: track-contact-job-changes
description: Verify which CRM contacts changed employers, preserve their previous roles, and propose contact or account updates. Use for contact refreshes, champion tracking, and job-change signals.
license: MIT
---

# Contact Job Changes & Champion Tracking

Compare fresh work-history evidence with the CRM, then propose a reviewed batch of changes. Use the CRM and enrichment sources the operator already has; this package requires no particular orchestration platform. It contains instructions, not provider accounts or a background worker.

## Set up

Read [the setup checklist](references/setup-checklist.md). Resolve the correct CRM/workspace, input set, person/company match keys, available data sources, fit criteria, opt-out rules, field mappings, and write policy. Save non-secret configuration in a private client workspace outside this package. Reuse confirmed configuration on later runs.

## Run

1. Read each source contact by a stable CRM record ID where available. Retain the existing employer, title, associations, owner, previous-role history, and suppression state.
2. Resolve a missing LinkedIn URL from name and context if the configured tools support it. Validate the person using more than a common name alone. Wrong or ambiguous identity means **can't confirm**.
3. Pull current and past roles from the configured source, or use a supplied export with its freshness stated. Handle overlapping current jobs explicitly. Neither the latest start date nor an existing CRM association is sufficient by itself to choose the primary employer.
4. Compare the employer using [company matching rules](references/company-matching-rules.md). Outcomes: **still there**, **confirmed left**, or **can't confirm**. Conflicting or incomplete evidence is a review item, not a forced update.
5. For a confirmed move, search the new company in the CRM. A unique verified match can receive a proposed reassociation. Multiple matches require resolution. For a net-new company, use [the fit rubric](references/tiering-a-net-new-company.md) before proposing an account creation.
6. Apply only the configured opt-out rules. A new job does not imply permission to subscribe someone, resume outreach, clear opt-outs, or erase the old employer. Preserve prior-role history and distinguish a missing company association from a proposed reassociation.
7. Present one batch table: source record, old/new role, outcome, identity/company evidence, freshness, proposed fields and associations, fit reasons, suppression effect, and unresolved questions. If writes are disabled, deliver the report and stop.
8. Apply the approved changes within the operator's authorization. Immediately before each write, re-read the contact and company match; re-evaluate if relevant data changed since approval. Do not retry an uncertain create blindly. Reconcile its result first to avoid duplicate accounts.
9. Read back written fields and associations. Report verified updates, unchanged records, deferred cases, failures, and unconfirmed outcomes separately. Save the proposal and run log privately.

No paid lookup should run without an agreed input scope and provider budget. Missing write access still allows a useful report. Missing identity/work-history evidence blocks only the affected decisions.

Read [the synthetic review examples](examples/review-cases.md) for expected decisions. This edition is based on Jorge Macías's [public GTM Skills contribution](https://www.gtmskills.com/skill/track-contact-job-changes); see [LICENSE](LICENSE).
