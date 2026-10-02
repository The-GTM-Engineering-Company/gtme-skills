# Applying a copy-only sync

## Before a write

Save the source revision, target workspace/campaign IDs, current status, complete relevant sequence, and proposed copy patch to the private workspace. The baseline must be sufficient to compare or restore the changed fields.

Validate mapping, subjects, links, tokens, fallbacks, platform limits, and all affected variants. Resolve unfilled placeholders. Re-read source and target immediately before mutation; a concurrent edit invalidates the prior diff unless it is demonstrably unrelated.

Use existing authorization for the specific changes. Explain any necessary pause or scheduled-to-draft side effect before acting if not already authorized. Do not change a campaign merely to discover whether a write works.

## Write and read back

Apply one platform/campaign at a time so a partial result is clear. Read back all changed fields plus the surrounding unchanged sequence and status. Compare with both the approved source and the baseline. Preserve any unrelated edits made by others.

An API timeout or ambiguous UI save is an unknown outcome. Re-read before retrying. Do not re-submit a replacement blindly. If verification fails, stop further writes to that campaign and report what is known.

If one platform succeeds and the other fails, report the partial sync. Do not revert a verified success automatically or claim both succeeded. Any rollback should use the recorded baseline after checking for later edits and confirming it is within the recovery authorization.

## Report

For each campaign: source revision, fields/steps changed, verified results, current campaign status, remaining issues, and private log location. Distinguish a saved change from a paste-ready patch and from a campaign that has been launched. This skill never launches or resumes sending.
