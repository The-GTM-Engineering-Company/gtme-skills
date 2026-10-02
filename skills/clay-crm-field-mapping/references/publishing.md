# Delivering the review inventory

Keep generated payloads, schema snapshots, scripts containing client context, and CSV outputs in the private client workspace. Share only through the destination the operator selected. Do not commit real client material to the public skill repository.

CSV is the portable default. Write CSVs with a CSV library and verify header/row widths, quoting, encoding, and multiline cells. Before spreadsheet delivery, ensure provider-controlled text cannot execute as a spreadsheet formula; use literal/raw cell writes or a documented escaping convention. Retain original values privately so presentation escaping is not mistaken for a transformation rule.

If the user requested an existing spreadsheet, preserve that URL. Inspect current tabs and populated ranges, then use an available Sheets connector/API or the normal import UI. Discover supported write methods; do not assume a Drive connector can or cannot edit cells. Preserve unrelated tabs and existing client decisions.

For manual import, give the operator the three files and ask them to import each as a new tab. Explain any literal-text convention used. Clipboard TSV is an optional route only after checking embedded tabs/newlines and the target selection.

After an authorized publish, read back representative headers, rows, and all three tab names. Verify saved state and return the agreed URL. A generated file or successful tool response alone does not prove the sheet is correct.
