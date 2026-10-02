# Platform adapters

Discover the current connector operations and request schemas. Use the configured authenticated workspace; do not probe private endpoints or cycle through guessed payloads. Prefer supported read/update operations, then the ordinary campaign editor UI when needed.

## Instantly

Read the existing campaign and sequence, including all variants and threading behavior. Build the smallest supported copy update. If an API takes a whole sequence, start from the current returned structure and change only the mapped fields. Read back the sequence and campaign status after saving.

Use the current [Instantly API documentation](https://developer.instantly.ai/) and [sequence editor guide](https://help.instantly.ai/en/articles/11967303-getting-started-with-sequences-section) for the interface actually available. Do not assume the permissions, payload format, or tool naming from another installation.

## HeyReach

The [official Campaign API reference](https://www.heyreach.io/blog/campaign-api) documents `UpdateSequence` as a whole-sequence replacement. It also describes status effects: scheduled campaigns return to draft, while paused-campaign edits involve remapping lead positions. These are reasons to inspect state before choosing this route. Do not infer that an old failed call means sequence editing is universally unsupported.

Read the full current tree and preserve unrelated actions, conditions, branches, delays, variants, and node references. Verify token syntax and fallback requirements for the specific API or UI. Stop if a complete read or safe replacement is unavailable. A supported UI edit or paste-ready patch is a valid fallback, with its status reported honestly.

No automatic campaign launch/resume belongs to either adapter. See [the sync procedure](sync-procedure.md).
