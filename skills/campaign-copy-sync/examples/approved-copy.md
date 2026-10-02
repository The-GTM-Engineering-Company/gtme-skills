# Synthetic copy example

All copy and campaign names below are invented. They demonstrate a format, not an instruction to send.

```text
▸ INSTANTLY | Example onboarding | Email 1
Subject: Your setup checklist
Hi {{firstName}},

Here is the setup checklist you requested: https://example.com/checklist

▸ HEYREACH | Example onboarding | Message 1
Hi {{firstName}}, happy to share the setup checklist you requested.
Fallback: Hi there, happy to share the setup checklist you requested.
```

Example review cases:

- If the mapped draft sequence already matches, report no change.
- If the target has two A/B variants and the document maps only one, preserve the other.
- If a token is unknown to the target, defer that block; do not strip or guess it.
- If the campaign is active, preview first and obtain authorization for a pause if needed. Leave it paused after an approved sync.
- If HeyReach is scheduled and the chosen API would return it to draft, resolve that status consequence before writing.
- If the source or campaign changes after preview, refresh the diff before applying.
