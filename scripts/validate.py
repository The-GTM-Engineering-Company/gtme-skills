#!/usr/bin/env python3
"""Offline package validation; never connects to client systems."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'clay-crm-field-mapping', 'track-contact-job-changes',
    'case-study-writer', 'writing-renewal-sows', 'campaign-copy-sync',
}
errors = []
skills = {p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}
if skills != EXPECTED:
    errors.append(f'Unexpected skill set: {sorted(skills)}')

for name in sorted(skills):
    path = ROOT / 'skills' / name / 'SKILL.md'
    if not path.is_file():
        errors.append(f'{name}: missing SKILL.md')
        continue
    source = path.read_text()
    front = re.match(r'^---\n(.*?)\n---\n', source, re.S)
    if not front:
        errors.append(f'{name}: invalid frontmatter boundary')
        continue
    fields = dict(re.findall(r'^([a-z-]+): (.+)$', front.group(1), re.M))
    if fields.get('name') != name:
        errors.append(f'{name}: name differs from directory')
    if not fields.get('description', '').strip():
        errors.append(f'{name}: missing description')
    if set(fields) - {'name', 'description', 'license'}:
        errors.append(f'{name}: unsupported frontmatter field')

for path in sorted(ROOT.rglob('*.md')):
    if '.git' in path.parts:
        continue
    content = path.read_text()
    relative = path.relative_to(ROOT)
    # Validate local Markdown links, including paths with spaces/angle brackets.
    for target in re.findall(r'\]\(([^)\n]+)\)', content):
        target = target.strip().strip('<>')
        if urlparse(target).scheme or target.startswith('#'):
            continue
        target_path = unquote(target.split('#', 1)[0])
        resolved = (path.parent / target_path).resolve()
        if not resolved.is_relative_to(ROOT):
            errors.append(f'{relative}: link escapes package: {target}')
        elif not resolved.exists():
            errors.append(f'{relative}: broken link: {target}')
    if content.count('```') % 2:
        errors.append(f'{relative}: unbalanced code fences')
    if re.search(r'\[TODO:[^\]]*\]', content):
        errors.append(f'{relative}: unfinished scaffold')
    if re.search(r'/Users/|/home/|mcp__[0-9a-f]{8}-|sk-[A-Za-z0-9]{20,}|gh[pousr]_[A-Za-z0-9]{20,}', content):
        errors.append(f'{relative}: possible private path, server ID, or secret')

license_path = ROOT / 'skills/track-contact-job-changes/LICENSE'
if not license_path.exists() or 'Copyright (c) 2026 Swan' not in license_path.read_text():
    errors.append('Missing upstream MIT notice')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'PASS: {len(skills)} skill packages; frontmatter, local links, fences, attribution, and basic privacy checks.')
print('This is documentation validation, not a live CRM or campaign test.')
