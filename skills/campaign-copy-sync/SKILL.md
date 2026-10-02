---
name: campaign-copy-sync
description: Compare approved Google Docs campaign copy with existing Instantly and HeyReach sequences, then apply authorized copy changes with snapshots and readback. Use when a source document changes or campaign copy has drifted.
---

# Campaign Copy Sync

Keep existing campaign copy aligned with an approved source document. Sync only the named campaigns and steps. This skill does not create or launch campaigns, add leads, send messages, or change senders, budgets, exclusions, schedules, or sequence structure.

## Set up

Read [setup](references/setup.md) and [the document format](references/document-format.md). Resolve the source document/tab, approved revision, workspace identities, campaign IDs, step mapping, copy fields, token mapping, and private snapshot/log location. Read-only preview is the initial mode.

The operator uses their own Google Docs and campaign-tool access. Credentials stay in existing connectors or private secret storage. Keep all configuration, document content, and snapshots outside this package.

## Preview

1. Read the specified document/tab in full. If a connector concatenates tabs, locate the selected copy section explicitly and exclude strategy/comments that are not campaign text.
2. Read the complete existing target sequences, variants, fallback text, branch structure, delays, and campaign status using the available supported API or UI. Follow [adapter guidance](references/adapters.md).
3. Map document blocks to exact existing steps. Ambiguous or missing step identity is a blocker; do not match by order when branching/variants make that unsafe.
4. Normalize only formatting needed by the destination. Preserve approved words, subject threading, personalization, fallbacks, and signatures according to configuration. Do not invent copy or “improve” the source text.
5. Show the old/new copy diff, affected targets, validation issues, and any unavoidable status side effect. Report a no-op if the content already matches.

## Apply and verify

Use [the sync procedure](references/sync-procedure.md). Act within the operator's approved changes; do not interpret access to a campaign as permission to alter it. Capture a private baseline and re-read both source and targets immediately before writing. If relevant content changed, reconcile the diff first.

Change copy fields only. A full sequence-replacement API must preserve every unrelated node, branch, delay, and variant. If the tool cannot preserve those fields, use a supported UI edit or deliver a paste-ready patch; report which actions remain manual.

Keep draft/paused campaigns inactive. Do not start, resume, or schedule sending as part of a copy sync. An active campaign requires an explicitly authorized pause before editing through a method that requires it; leave it paused and report that state. For a scheduled campaign, do not use a route that changes status without the operator's explicit approval of that consequence.

After saving, read back the actual campaign copy and status, including fallback fields. Report each platform separately as verified, unchanged, deferred, failed, or unconfirmed. Do not describe a generated patch or API response alone as a completed sync.

See [the synthetic copy example](examples/approved-copy.md). Launching or resuming outreach is a separate operator decision.
