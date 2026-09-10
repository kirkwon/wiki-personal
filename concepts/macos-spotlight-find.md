---
date: 2026-07-19
type: concept
title: Macos Spotlight Find
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/macos-spotlight-find
description: Locate files via Spotlight with attribute filters.
---

# Macos Spotlight Find

> Locate files via Spotlight with attribute filters.

## Overview

- **When to Use** — - Need to find all files of a certain type (e.g., *.md) modified in the last N days - Want to locate files containing specific text via Spotlight's content index - Search for files by name or metadata attributes across a large workspace - Build dynamic lists of files for further processing (read, extract, etc.)
- **Prerequisites** — - macOS with Spotlight indexing enabled (default on modern macOS) - No additional software required
- **How to Run** — Invoke through the `terminal` tool with an appropriate `mdfind` command string. Optionally process the resulting list of paths with `read_file`, `web_extract`, or custom scripts.

## Further detail

### Quick Reference

- Find all markdown files: `mdfind "kMDItemFSName == '*.md'cd"` - Find files modified in last 7 days: `mdfind "kMDItemFSContentChangeDate >= $time.now(-7*24*60*60)"` - Limit search to a directory: `mdfind "kMDItemFSName == '*.md'cd && kMDPath == '/Users/kirkwon/clawd'wc"` - Find files containing text: `mdfind "kMDItemTextContent == 'your phrase'cd"`

### Procedure

1. **Define search criteria** – decide what attribute(s) to filter on (name, content, dates, etc.). 2. **Build the mdfind query** – use the syntax shown in Quick Reference; combine multiple predicates with `&&`. 3. **Add path constraint (optional)** – prepend `kMDPath == '/your/path'wc && ` to limit scope. 4. **Execute via terminal** – call the `terminal` tool with the constructed command. 5. **Process results** – each line of output is a matching file path; feed into `read_file` for content, or iterate in an `execute_code` script.

### Pitfalls

- Spotlight may lag behind real‑time filesystem changes; newly created files might not appear immediately. - Queries require correct quoting; the `cd` flag makes string comparisons case‑insensitive. - Complex date predicates need the `$time.now()` syntax; ensure the terminal tool passes the string unchanged. - If no files match, `mdfind` returns empty output (no error).

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/macos-spotlight-find/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
