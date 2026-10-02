# Mapping pitfalls

Use these as checks against the supplied payloads, not assumptions about every provider.

| Pitfall | Decision to document |
| --- | --- |
| Geocoding turns a regional abbreviation into the wrong state | Validate country-specific geography and approved crosswalks; defer unsupported mappings. |
| A location with weak evidence is treated as headquarters | Use explicit HQ/primary evidence and a defined tie-breaker; never silently take array index zero. |
| Raw and structured location arrays differ | Compare all paths and explain dropped/inferred entries. |
| Sentinel strings such as “unknown” are treated as real values | Define null handling per field without turning real zero/false into missing values. |
| Revenue or headcount bands target numeric fields | Prefer compatible range fields. Any conversion needs approval and must be labeled as an estimate/bound, not an exact measurement. |
| Arrays target scalar fields | Define selection or joining behavior and verify that the target supports it. |
| Derived claims conflict with source data | Compare evidence and freshness; defer contradictions rather than assuming AI-derived or raw data always wins. |
| A payload path is missing in some records | Represent conditional availability and define no-value behavior. |
| Labels look identical but meanings differ | Compare semantics, such as company ownership type versus customer/prospect relationship. |
| One match key selects several CRM records | Record the collision and routing decision; never update the first match arbitrarily. |
| Existing picklist values are inconsistent | Map to verified internal values; keep unmapped values visible and unresolved. |
| A field is owned by another sync | Establish ownership and overwrite policy before recommending a second writer. |
| A field drives routing or a formula key | Trace dependencies and flag the potential change in behavior. |
| Post-save automation alters data later | Specify what a subsequent write-back pilot must verify immediately and after relevant syncs. |

These checks produce evidence and decisions. They do not authorize cleaning existing CRM data during an inventory.
