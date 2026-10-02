# Setup checklist

Use the operator's existing task context and connected tools to fill this in. Ask only for missing or ambiguous information. Keep the configuration in a private workspace, such as `.contact-job-change/config.json`, not in the downloaded package. Store credential references, never credentials.

| Setting | Capture |
| --- | --- |
| Target | CRM, account/portal identity, environment, allowed objects |
| Input | Explicit segment, view, CSV, or record IDs; batch limit |
| Access | Report only, or approved CRM writes and their scope |
| Person keys | Source record ID, validated email/profile identifiers |
| Company keys | Domain and LinkedIn company page, with collision handling |
| Sources | Work-history source and freshness; optional URL, email, and company-enrichment tools |
| Budget | Provider usage/credit limit for this batch |
| Fit | Required criteria, optional criteria, and unknown-data handling |
| Suppression | Exact conditions and fields for an approved opt-out; never clear existing consent flags implicitly |
| Mapping | Current and previous role fields, review flags, company association, fit tier, and any allowed email updates |
| Output | Private report/log location and intended recipients |

Work-history evidence is required to conclude someone moved. A URL finder is unnecessary when a valid URL already exists. Email lookup and company enrichment are optional until a particular decision needs them; do not force the operator to buy all four capabilities.

Use existing connected CRM and enrichment tools or supplied data. Discover each tool's schema before calling it. If a capability is absent, explain the affected output and request a suitable source. Do not silently substitute a guessed result.

Fit policy is described in [tiering](tiering-a-net-new-company.md). Show the resolved configuration before the first run. Preserve prior configuration and explain intentional changes when reconfiguring.
