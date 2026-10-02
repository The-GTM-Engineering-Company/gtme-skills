# Approved copy format

Use clear block labels and a configured mapping to existing campaign steps. A suggested format is:

```text
▸ INSTANTLY | Example campaign | Email 1
Subject: Example subject
Hi {{firstName}},

Approved message body.

▸ HEYREACH | Example campaign | Message 1
Hi {{firstName}}, approved message body.
Fallback: Hi there, approved fallback body.
```

Each block ends at the next block header. Treat an intentionally blank subject according to the verified platform threading behavior. Preserve empty versus absent values explicitly.

Google Docs may return smart quotes, headings, or bold formatting. Normalize structural markup while preserving the approved text. A malformed header, duplicate mapping, missing variant, or an unresolved literal placeholder such as `[ASSET LINK]` requires correction before apply.

Plain text converted to HTML must be escaped before adding paragraph tags. Do not double-escape content that is already approved HTML; inspect its format first. Preserve links and validate their intended destinations. Never silently append a signature token.

Token syntax may differ between a tool's API and UI. Read the target schema and a known valid existing step, then use an explicit token map. Do not blindly replace every brace in the document. Validate fallback text wherever personalization requires it.

The source document is read-only during sync. Changes to its wording are an editing task, not an implicit part of copying it into the tools.
