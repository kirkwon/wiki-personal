---
date: 2026-07-19
type: concept
title: Data Rebuild Vs Patch Strategy
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- data-management
- troubleshooting
- data-science
sources:
- hermes://skill/data-rebuild-vs-patch-strategy
description: Decision framework for choosing between patching corrupted files vs rebuilding
  from source data when dealing with systematic data corruption
---

# Data Rebuild Vs Patch Strategy

> Decision framework for choosing between patching corrupted files vs rebuilding from source data when dealing with systematic data corruption

## Overview

- **When to Use (Trigger)** — When you discover widespread data corruption across multiple files that needs systematic fixing. Examples: broken wikilinks, corrupted frontmatter, malformed data structures, parsing artifacts like nested brackets.
- **Purpose** — Ensure you fix data corruption at the right level - either by patching individual files (when corruption is minor and localized) or by rebuilding from source data (when corruption is severe and systematic).
- **Tools Needed** — - Python for batch processing - File inspection tools (grep, search_files) - YAML/JSON validators - Sample verification (manual spot-check)

## Further detail

### Validation Checklist

After fixing data corruption:

### Sources

- [[YAML Frontmatter Management]] - [[Systematic Debugging]]

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/data-science/data-rebuild-vs-patch-strategy/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
