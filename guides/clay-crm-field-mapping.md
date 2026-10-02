# Clay → CRM Field Mapping

Audit how Clay enrichment should map into Salesforce or HubSpot before enabling write-back. The result is a field inventory, value maps, and an open-decisions sheet for the CRM owner to review. Useful for clients, contractors, and GTME delivery teams.

**Public skill package:** [Clay → CRM Field Mapping](https://github.com/The-GTM-Engineering-Company/gtme-skills/tree/main/skills/clay-crm-field-mapping)

No GitHub account, invitation, or username sharing is needed to download the package. Each operator still needs their own authorized access to the relevant services.

## 1. Before you start

- A local assistant such as Codex or Claude Code that can read files and run commands.
- Authorized read access to the intended Salesforce org or HubSpot portal. Sign in yourself through your normal connector or CLI.
- One object to start with: Account/Company or Contact/Person.
- At least two real sample payloads from the Clay table being mapped, saved in your private client workspace.

## 2. Set up with your assistant

Open a private client workspace and paste:

```text
Install the clay-crm-field-mapping skill from this public repository:
https://github.com/The-GTM-Engineering-Company/gtme-skills

Read skills/clay-crm-field-mapping/SKILL.md and keep the complete
folder with its references. Check my CRM connection and identify the
account and environment. Keep client payloads and outputs in my private
workspace, outside the repository. Ask only for missing setup details.
```

Keep the complete skill folder and its reference files together. Your assistant can install it for Codex or Claude Code, or read it directly from the downloaded repository.

## 3. Run the first scoped task

```text
Audit the selected CRM object against these Clay payloads. Inspect the
live schema, population rates, actual values, match keys, dependencies,
and other integrations. Produce Field Inventory, Value Maps, and Open
Decisions. Keep client decisions blank. Do not write to the CRM or
configure Clay write-back.
```

## 4. What you should receive

- **Field Inventory:** each Clay data point, candidate CRM field, transformation, evidence, and proposed write mode.
- **Value Maps:** verified mappings between provider values and CRM internal values, including unmatched values.
- **Open Decisions:** choices the CRM owner needs to resolve, such as fill-if-empty versus overwrite and company association rules.

See the [synthetic example](https://github.com/The-GTM-Engineering-Company/gtme-skills/blob/main/skills/clay-crm-field-mapping/examples/company-review.md) for the expected shape. It contains invented data.

## 5. Review and continue

Review match-key collisions, fields owned by another integration, missing targets, and contact-to-company association decisions. Counts that could not be measured must be marked unverified. Publishing the review sheet is separate from configuring write-back; the audit itself is read-only.

## Practical limits

The operator needs adequate schema and record-read permissions. Some connectors cannot inspect all automations or property rules; the report must identify those gaps. Future CRM write-back requires its own approved mapping and scoped pilot.

## Updates and help

Use the repository for the maintained skill files. Review updates before replacing an existing installation; keep client configuration and outputs outside the shared repository. These are assistant workflows, so verify the first result with the responsible owner in the actual environment.

**Need help?** Contact the GTME person who shared this page. Before sending this Notion link to a client or contractor, ensure that recipient can view the page. The GitHub package is public; Notion sharing is managed separately.
