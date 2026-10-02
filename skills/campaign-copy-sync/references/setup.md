# Campaign-copy setup

Save non-secret settings in the private client workspace. Capture:

- Source Google Doc URL, tab/section, and approved revision or timestamp.
- The workspace/account identity for each selected platform.
- Existing campaign IDs, exact names, and current statuses.
- Mapping from source block labels to stable target steps/nodes and variants.
- Which fields may change: subject, message body, connection note, fallback, and any explicitly selected variants. Delay or structure changes are outside this copy-only skill.
- Personalization token mapping for each interface, and a policy for unknown/missing variables.
- Signature and follow-up threading rules.
- Authorized action: preview, apply specific copy changes, or pause an active campaign before applying. Starting/resuming/scheduling sends is separate.
- Private snapshot/log destination and recovery contact.

Validate access with reads first. No global client IDs or sender identities are bundled. If the source document is not readable, a supplied approved export can be used with its freshness recorded.
