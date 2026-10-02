# Contact Job Changes & Champion Tracking

Find contacts who changed employers, preserve their previous roles, and surface champions at new accounts. The skill prepares proposed contact and company changes with evidence before approved CRM updates. Use it for database refreshes or a specific job-change signal.

**Public skill package:** [Contact Job Changes & Champion Tracking](https://github.com/The-GTM-Engineering-Company/gtme-skills/tree/main/skills/track-contact-job-changes)

No GitHub account, invitation, or username sharing is needed to download the package. Each operator still needs their own authorized access to the relevant services.

## 1. Before you start

- A local assistant that can read the complete skill folder.
- A CRM connection or contact export with stable record identifiers.
- A work-history source or a supplied export with current and previous employer evidence. Use the enrichment providers your team already has.
- The contact list, fit criteria for new accounts, opt-out rules, and a batch/provider budget.

## 2. Set up with your assistant

Open a private client workspace and paste:

```text
Install the track-contact-job-changes skill from:
https://github.com/The-GTM-Engineering-Company/gtme-skills

Read skills/track-contact-job-changes/SKILL.md and its references.
Use my existing CRM and enrichment connections. Save non-secret setup
in my private workspace. Start in report-only mode and confirm the
input list, fit rules, opt-out policy, and provider budget before
running lookups. Do not modify CRM records yet.
```

Keep the complete skill folder and its reference files together. Your assistant can install it for Codex or Claude Code, or read it directly from the downloaded repository.

## 3. Run the first scoped task

```text
Review this small contact sample for job changes. Show identity
evidence, old and new roles, freshness, company matches, and proposed
fields or associations. Preserve previous-role history and existing
suppression settings. Defer uncertain identities and incomplete fit
evidence. Return a report for my review.
```

## 4. What you should receive

- A contact-level table showing still employed, confirmed moved, or cannot confirm.
- Proposed contact refreshes, company associations, and any net-new account candidates with fit reasons.
- A private run log with verified, deferred, failed, and unconfirmed outcomes.

See the [synthetic example](https://github.com/The-GTM-Engineering-Company/gtme-skills/blob/main/skills/track-contact-job-changes/examples/review-cases.md) for the expected shape. It contains invented data.

## 5. Review and continue

Inspect a small sample first. When ready, explicitly approve the proposed changes for that batch. The assistant must recheck live records before applying and read back the result. A changed employer does not authorize sending outreach or clearing opt-outs.

## Practical limits

Data freshness and identity quality limit the result. Similar names or a shared parent-company domain are not enough to force an update. Missing write access still permits a report. This is an assistant workflow, not an always-running background monitor.

The original skill was published by Jorge Macías in the [GTM Skills library](https://www.gtmskills.com/skill/track-contact-job-changes). This GTME-maintained edition fixes reference paths and includes additional evidence and verification guidance. Its included MIT license and upstream attribution are preserved.

## Updates and help

Use the repository for the maintained skill files. Review updates before replacing an existing installation; keep client configuration and outputs outside the shared repository. These are assistant workflows, so verify the first result with the responsible owner in the actual environment.

**Need help?** Contact the GTME person who shared this page. Before sending this Notion link to a client or contractor, ensure that recipient can view the page. The GitHub package is public; Notion sharing is managed separately.
