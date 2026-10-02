# HubSpot inspection

Use the connected HubSpot tools, authorized API access, or supplied exports. Inspect the current connector schema; operation names and object-type spelling are not portable across connectors.

## Identity and schema

Resolve the portal/account ID, account name where available, environment, and read scope. Compare with the intended client. Missing account-name metadata does not prove the connection is wrong; resolve ambiguity before pulling records. Do not echo tokens or raw auth responses.

Read the full property schema for the selected object, paginating if needed. The standard Properties API exposes `name`, `label`, `type`, `fieldType`, `options`, `calculated`, `hasUniqueValue`, and modification metadata such as `readOnlyValue`; inspect the actual response rather than assuming all attributes are present. Preserve option **internal values**, separately from labels.

Use native/existing properties where they fit. Potential company candidates include domain, industry, employee count, annual revenue, country, and any range/code properties actually present. Names, availability, validation, and editability must be established from this portal's schema. Do not copy a property inventory from another client.

## Counts and stored values

Measure the accessible population for one defined object scope. Use supported filtered counts or paginate an authorized export. Confirm whether the API's total is exact or capped before using it as a denominator. A zero result may be a real empty set; distinguish that from missing access.

Compute populated count / scope count for each candidate. Exclude empty/sentinel strings consistently and document that rule. Read actual values to identify unexpected vocabulary and formatting. If you only sampled values, label the result as a sample. SQL capabilities depend on the connector and scopes; do not request new access merely because one optional query method is unavailable.

## Write blockers and ownership

Check calculated/read-only properties, property validation rules, workflow enrollment and property updates, required values, association logic, and integration ownership. Not every connector exposes all of these. Record inaccessible checks as unresolved.

Do not assume company domain uniquely identifies a record. Search all matches and record collision rates. For contacts, examine record IDs, email behavior, and LinkedIn URL quality separately. A property's uniqueness flag alone is not a complete description of contact email matching or deduplication behavior. Prefer returning enrichment against the original exported CRM record ID.

Preserve subscription/opt-out, enrichment opt-out, bounce, and marketing-contact status. These are not enrichment targets in this skill. Check current native fields before proposing any additional person-role or education fields.

Official schema reference: [HubSpot Properties API](https://developers.hubspot.com/docs/api-reference/crm-properties-v3/guide). Use current documentation alongside the live portal schema.
