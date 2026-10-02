# Campaign Copy Sync (Google Docs → Instantly / HeyReach)

Keep existing campaign copy aligned with an approved Google Doc. Compare the source with Instantly and/or HeyReach, apply approved copy changes, and verify the saved result. Use either platform or both.

**Public skill package:** [Campaign Copy Sync (Google Docs → Instantly / HeyReach)](https://github.com/The-GTM-Engineering-Company/gtme-skills/tree/main/skills/campaign-copy-sync)

No GitHub account, invitation, or username sharing is needed to download the package. Each operator still needs their own authorized access to the relevant services.

## 1. Before you start

- Read access to the approved Google Doc, including the intended copy tab or section.
- Authorized access to the selected campaign workspace and existing campaigns.
- Clear mapping from document blocks to campaign steps and variants, plus token, fallback, signature, and threading rules.
- A private workspace for configuration, before/after snapshots, and the sync log.

## 2. Set up with your assistant

Open a private client workspace and paste:

```text
Install the campaign-copy-sync skill from:
https://github.com/The-GTM-Engineering-Company/gtme-skills

Read skills/campaign-copy-sync/SKILL.md and its references. Resolve
my source document, selected platform workspaces, campaign IDs, step
mapping, and token rules. Keep configuration and snapshots private.
Start with a read-only preview. Do not change campaign status, copy,
leads, senders, schedules, or sending behavior during setup.
```

Keep the complete skill folder and its reference files together. Your assistant can install it for Codex or Claude Code, or read it directly from the downloaded repository.

## 3. Run the first scoped task

```text
Compare the approved copy document with the selected campaigns.
Show the exact old/new copy diff, affected steps and variants, missing
fallbacks or placeholders, and current campaign status. Explain any
status effect required by the available update method. Do not apply
changes until they are authorized.
```

## 4. What you should receive

- A source-to-campaign copy diff, with validation issues and status effects clearly identified.
- After approval: verified copy updates for each selected platform, or a clearly labeled paste-ready patch if direct editing is unavailable.
- A private baseline snapshot and change log, with the final campaign status and unresolved items.

See the [synthetic example](https://github.com/The-GTM-Engineering-Company/gtme-skills/blob/main/skills/campaign-copy-sync/examples/approved-copy.md) for the expected shape. It contains invented data.

## 5. Review and continue

Approve the exact changes after reviewing the diff. Draft and paused campaigns stay inactive. If an active campaign needs a pause, approve that action explicitly; it remains paused after the sync. Launching or resuming outreach is a separate decision. The assistant must read back the saved copy, fallbacks, and status.

## Practical limits

The available API or editor must support a copy-only change without losing unrelated sequence structure. Whole-sequence replacement requires preserving branches, delays, and variants. Scheduled HeyReach campaigns can return to draft through the sequence API; resolve that consequence before editing.

## Updates and help

Use the repository for the maintained skill files. Review updates before replacing an existing installation; keep client configuration and outputs outside the shared repository. These are assistant workflows, so verify the first result with the responsible owner in the actual environment.

**Need help?** Contact the GTME person who shared this page. Before sending this Notion link to a client or contractor, ensure that recipient can view the page. The GitHub package is public; Notion sharing is managed separately.
