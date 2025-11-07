#!/usr/bin/env python3
import sys
import glob
import re

errors = []

for path in glob.glob("cards/*.md"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            txt = f.read()
    except Exception as e:
        errors.append(f"{path}: could not read file: {e}")
        continue

    if not txt.startswith("---"):
        errors.append(f"{path}: missing YAML front matter")
        continue

    m = re.match(r'---\n(.*?)\n---\n', txt, re.S)
    if not m:
        errors.append(f"{path}: malformed YAML front matter")
        continue

    fm = m.group(1)
    if not re.search(r'^name:\s*.+', fm, re.M):
        errors.append(f"{path}: missing 'name' in front matter")
    if not re.search(r'^tags:\s*.+', fm, re.M):
        errors.append(f"{path}: missing 'tags' in front matter")

    if '## Q:' not in txt:
        errors.append(f"{path}: missing '## Q:' header")
    if '## Answer (Technical)' not in txt:
        errors.append(f"{path}: missing '## Answer (Technical)' header")
    if '## Answer (Non-Technical)' not in txt:
        errors.append(f"{path}: missing '## Answer (Non-Technical)' header")

if errors:
    print("Card lint failed:")
    for e in errors:
        print(e)
    sys.exit(1)
else:
    print("All cards passed validation.")