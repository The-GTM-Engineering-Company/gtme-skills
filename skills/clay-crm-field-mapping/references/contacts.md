# Contact and person mapping

Apply the main workflow and CRM reference first. Contact payloads commonly contain arrays for experience, education, projects, languages, and current roles. Inspect the actual table's payloads; array lengths and availability are not universal.

## Collapse rules and employer selection

Record one explicit selection/collapse decision per array before mapping its children to scalar fields. Options include keeping an approved current value, storing selected history in text, using an existing related object, or excluding the array. Do not create a new data model as part of this audit.

Multiple current employers or overlapping promotion records require a role-selection policy. Name, current-role indicators, dates, business context, and company identifiers are evidence. Existing CRM association is useful context but does not prove a job is current; the person may have moved. Do not select a side venture solely because it has the latest start date, or trust a provider's `latest_experience` without understanding its semantics. Defer ambiguous choices.

## Associations and identifiers

Treat contact-to-company association as its own inventory row and open decision. Measure the existing association rate. Separate filling a missing association from replacing an existing one; the latter can affect deals, ownership, and reporting. Domain mismatch can flag a possible job change, but does not authorize reassociation.

Preserve the source CRM record ID through export/enrichment. Assess email and LinkedIn identifiers for missing values, duplicate matches, wrong profile types, and formatting drift. Validate identity before treating an enrichment result as that contact. LinkedIn vanity URLs can change; numeric IDs are useful where reliably supplied, but do not assume a native field exists or is unused.

## Contact-specific checks

- Respect contact/enrichment opt-outs, subscription status, bounce flags, and marketing-contact status. Do not change them through a field-mapping task.
- Make email/phone coverage explicit: a rich role-history payload may contain neither.
- Scan every array element; the first experience entry may have no end date while older entries do.
- Distinguish month precision from day precision in dates. Do not invent a precise day.
- Check whether location text is actually a date range or an unstructured label.
- Separate degree programs from short courses before choosing education fields.
- Treat capped connection counts as lower bounds where the provider specifies that behavior.
- Prefer company-level firmographics on the company. Duplicating them onto contacts creates a maintenance decision when someone moves.

Job-change detection is a separate workflow with identity evidence, timing, and approved actions. List it as a decision when relevant; this mapping audit does not execute it.
