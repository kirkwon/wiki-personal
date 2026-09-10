---
date: 2026-08-02
type: concept
title: Browser History Ingestion
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/browser-history-ingestion
description: Import and normalize browser history data.
---

# Browser History Ingestion

> Import and normalize browser history data.

## Overview

- **Description** — This skill provides a standardized approach to importing, normalizing, and preparing browser history data (Safari, Chrome) for further analysis in the Web History Intelligence project. It covers extracting history from native browser stores, handling permissions and fallbacks, normalizing formats, and preparing data for enrichment pipelines.
- **When to Use** — Use this skill when you need to: - Import browsing history from Safari or Chrome on macOS - Normalize history data into a common schema - Prepare data for topic enrichment, interest classification, or knowledge extraction - Handle common obstacles like database locks, permission issues, and missing data
- **Required Tools** — - `osascript` (macOS AppleScript) - `sqlite3` command line or Python sqlite3 module - Standard Python libraries: json, subprocess, datetime, pathlib, tempfile, shutil

## Further detail

### Output Conventions

- Raw imports: `02.Research/incoming/<browser>_history_<timestamp>.json` - Normalized: `02.Research/refined/normalized_history_<timestamp>.jsonl` - Summaries: `*_summary.txt` alongside each output

### Pitfalls and Troubleshooting

- **Safari database locked**: Even read-only attempts may fail due to macOS protections; prefer direct SQLite access with Full Disk Access permission (requires restarting Hermes after granting). - **Safari AppleScript syntax errors on macOS Ventura+**: Traditional syntax like `every history item` fails with errors -2741/-2740; use SQLite method as primary approach. - **Chrome database locked**: Always copy to temp file before reading. - **Timestamp conversion errors**: Verify epoch offsets (Safari: +978307200 from 2001-01-01; Chrome: -11644473600 from 1601-01-01). - **Missing title fields**: A

### Reference Scripts

- `03.Scripts/import_safari_history.py` – Safari import with fallback - `03.Scripts/import_chrome_history.py` – Chrome import with temp copy - `03.Scripts/update_node_status.py` – Update GRAPH.md node status - `03.Scripts/normalize_history.py` – Merge and normalize histories

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/browser-history-ingestion/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
