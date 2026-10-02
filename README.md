# GTME Skills

Reusable agent skills from **The GTM Engineering Company** for clients, contractors, and delivery teams. Each folder contains the full instructions and references for one workflow.

| Skill | Use it for | Access needed |
| --- | --- | --- |
| [Clay → CRM Field Mapping](skills/clay-crm-field-mapping) | Review enrichment mappings before write-back | Salesforce or HubSpot read access; sample Clay payloads |
| [Contact Job Changes & Champion Tracking](skills/track-contact-job-changes) | Verify employer changes and propose CRM updates | CRM and a work-history enrichment source, or supplied exports |
| [Client Case Study Writer](skills/case-study-writer) | Produce evidence-backed named and anonymized case studies | Approved engagement evidence; Notion optional |
| [SOW Completion Audit & Renewal Scope](skills/writing-renewal-sows) | Audit delivery and draft the next scope | Previous scope and delivery evidence; document publishing optional |
| [Campaign Copy Sync](skills/campaign-copy-sync) | Sync approved Google Docs copy to Instantly and/or HeyReach | Source document and access to the selected campaign tools |

Also available: [HubSpot autonomous deduplication](https://github.com/The-GTM-Engineering-Company/hubspot-autonomous-deduplication), maintained in its own repository.

## Start with your assistant

Open a private client workspace in Codex, Claude Code, or another assistant that can read local files. Paste this and replace the skill folder name:

```text
Install one skill from this public repository:
https://github.com/The-GTM-Engineering-Company/gtme-skills

Skill folder: skills/clay-crm-field-mapping

Clone or download the repository without GitHub authentication. Read the
selected SKILL.md and its references. Keep the complete skill folder together.
Check required connections and ask only for missing setup information.
Keep client configuration and outputs in my private workspace, outside the
downloaded repository. Show me the first scoped task before changing live data.
```

No GitHub account or invitation is needed to read or download these files. Service access and paid enrichment, when used, are supplied by the operator. The skills are instructions for an assistant, not hosted automations or bundled connector accounts.

## Setup guides

- [Clay → CRM Field Mapping](guides/clay-crm-field-mapping.md)
- [Contact Job Changes & Champion Tracking](guides/track-contact-job-changes.md)
- [Client Case Study Writer](guides/case-study-writer.md)
- [SOW Completion Audit & Renewal Scope](guides/writing-renewal-sows.md)
- [Campaign Copy Sync (Google Docs → Instantly / HeyReach)](guides/campaign-copy-sync.md)

## Manual installation

```bash
git clone https://github.com/The-GTM-Engineering-Company/gtme-skills.git
```

Copy the **whole selected folder**, including references and examples, to your assistant's supported skill directory. Codex uses `~/.codex/skills/`; Claude Code uses `~/.claude/skills/`. A project-local installation is also possible where your assistant supports it. Review an existing installation before replacing it. You can also ask the assistant to read a SKILL.md directly without installing it globally.

Use a separate private workspace for each client. Do not put real payloads, CRM exports, case-study evidence, campaign snapshots, or credentials into this repository. Configuration examples contain invented data only.

## Updating and maintaining

Pull updates into the source checkout, review the changes, and then update the selected installed folder. Keep client-specific overrides in the private workspace. Run `python3 scripts/validate.py` before proposing a change.

These packages were checked for valid entrypoints, complete local references, and removal of client-specific configuration. They do not establish that a particular customer's permissions, CRM schema, or campaign interface is supported without setup verification.

See [usage permissions](ACCESS.md), [contributing](CONTRIBUTING.md), and [attribution](NOTICE.md). Maintained by The GTM Engineering Company. For a client setup question, contact the GTME person who shared the skill.
