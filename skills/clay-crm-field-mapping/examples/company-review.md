# Synthetic company review

All data in this example is invented. It demonstrates decisions, not a client-specific mapping.

Source payloads: Example Labs at `example.com` has revenue band `1M-5M`; Sample Systems at `example.org` has no revenue value. Both have industry labels supplied by enrichment.

| Clay path | Candidate CRM target | Evidence | Proposed handling | Client decision |
| --- | --- | --- | --- | --- |
| annual_revenue | Existing revenue-band field, if present | A band is not an exact numeric revenue | Use a verified range crosswalk; otherwise record a gap | Blank |
| industry | Existing industry property | Provider labels differ from internal option values | Crosswalk exact values; defer unmatched labels | Blank |
| company_domain | Exported record ID remains the update key | Two CRM records share a domain in this invented example | Resolve the multi-match; do not choose the first record | Blank |

Open decisions: revenue range storage, industry crosswalk, match collision, field ownership, and write posture. No CRM writes occur in this example.
