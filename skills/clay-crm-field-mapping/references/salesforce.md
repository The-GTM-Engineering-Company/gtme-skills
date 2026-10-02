# Salesforce inspection

Use an already authorized read-only connection. The Salesforce CLI examples below use an explicitly chosen alias; a connector with equivalent read operations is also suitable. The operator completes login themselves if needed.

## Identity

Use `sf org list --json` only with a parser that emits the selected alias, username, connection status, and instance URL. Do not print the unfiltered authentication response. Avoid `sf org display`, which can expose authentication material.

Set `CRM_ORG_ALIAS` to the intended, verified alias. Never rely on a machine's default org.

```bash
sf data query --target-org "$CRM_ORG_ALIAS" \
  --query "SELECT Id, Name, OrganizationType, InstanceName, IsSandbox FROM Organization"
```

Verify the client and environment. Resolve multiple possible orgs before pulling data. Record field-level-security limits so an incomplete schema does not appear comprehensive.

## Schema

Run in the private client workspace. Replace Account with Contact when appropriate.

```bash
sf sobject describe --target-org "$CRM_ORG_ALIAS" --sobject Account --json > account_describe.json
```

Inspect `name`, `label`, `type`, `length`, `createable`, `updateable`, `calculated`, `restrictedPicklist`, active picklist values, `externalId`, `unique`, and `idLookup`.

## Dependencies

Read active validation rules and their formulas, Apex triggers, and relevant active record-triggered flows using the available metadata/Tooling API reads. Listing every active flow does not establish which flows affect this object: inspect entry conditions and field references. Do not deploy or execute DML.

Check whether a proposed match field is calculated, writable, unique, or controlled by another integration. A formula can be useful for inspection while being unsuitable for an upsert key. Do not repurpose managed-package IDs. Preserve the original exported record ID when it is the intended write-back key.

Examine duplicate keys with read queries or a bounded export. Do not assume every field supports GROUP BY. A small LIMIT is a sample, not a complete collision count. Multiple matches may be legitimate subsidiaries or locations and require an explicit routing decision.

## Population and values

```bash
sf data query --target-org "$CRM_ORG_ALIAS" \
  --query "SELECT COUNT(Id) total, COUNT(Industry) industryCount, COUNT(BillingCountry) countryCount FROM Account"
```

Use the same scope for numerator and denominator. Some field types, including long-text areas, cannot be aggregated or filtered in the same way; use a permitted alternative or mark population unmeasured. Respect aggregate/result limits and permissions when describing vocabulary or distinct values.

Compare stored values with the declared picklist options. Restricted and unrestricted picklists require explicit crosswalks; an unrestricted field accepting a string does not make that string a correct value.

Preserve postal codes as text. Discover whether state/country code fields and picklists are enabled. Trace fields used by formula keys, routing, scoring, and other integrations before recommending overwrite. A future pilot should verify immediate outcomes and any subsequent automation, on a schedule appropriate to the client's syncs.
