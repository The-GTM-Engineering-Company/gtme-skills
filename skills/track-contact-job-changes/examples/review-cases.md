# Synthetic review cases

All companies and people here are fictional.

| Evidence | Expected result |
| --- | --- |
| A validated person has fresh history showing a different employer; its company page and domain match one existing account | Propose the role update and reassociation, preserving previous history. |
| A profile shares the contact's common name but employment/location evidence conflicts | Can't confirm identity; no CRM write. |
| Two operating companies share a parent domain | Defer account selection until business identity is resolved. |
| A net-new employer passes geography but required employee-count evidence is missing | Needs review; do not classify it as fit or create an account. |
| The contact was updated by a human after the proposed batch was approved | Re-read and re-evaluate the changed proposal before writing. |
| A create operation times out | Inspect whether the account was created before any retry; report an unconfirmed outcome if unresolved. |

In report-only mode every row remains a recommendation, including high-confidence matches.
