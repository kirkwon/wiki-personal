---
date: 2026-07-19
type: concept
title: Gbrain Content Ops
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- research
sources:
- hermes://skill/gbrain-content-ops
description: Correct patterns for adding, updating, and retrieving GBrain content
  — avoiding stdin corruption, slug mismatches, and import pitfalls.
---

# Gbrain Content Ops

> Correct patterns for adding, updating, and retrieving GBrain content — avoiding stdin corruption, slug mismatches, and import pitfalls.

## Overview

- **The Problem (Lessons from 2026-05-07)** — Common failures when adding/retrieving GBrain content: 1. `gbrain put --content /dev/stdin < file` → stores literal "/dev/stdin" as body text 2. `gbrain put` on existing page → "skipped" (unchanged) 3. `gbrain import` strips directory prefixes (`concepts/` → slug without prefix) 4. Slug mismatches: user expects `concepts/foo` but actual slug is `foo` 5. `gbrain get` fails with "page_not_found" even though `gbrain list` shows it
- **Pitfalls** — - **CWD determines sync source (CRITICAL — silent link failures)**: `gbrain put` and `gbrain link` resolve the **sync source** from the current working directory. Running from `/Users/kirkwon/wiki-personal/` scopes the page to the `wiki-personal` source (5,079 pages). Running from `/Users/kirkwon/` (home) scopes to the `default` source (14,718 pages). If a page lands in the wrong source, `gbrain link` silently fails or returns `page_not_found` for targets in a different source — even though both pages exist. **Always run `gbrain put` and `gbrain link` from `/Users/kirkwon/` (home) or `/Users/k
- **Batch Deletion Pattern** — When deleting many pages (e.g., archive duplicates):

## Further detail

### Cross-Source Linking

Cross-source links fail silently because each page belongs to exactly one sync source determined by CWD at creation time. A page in `default` cannot link to a page in `wiki-personal`.

### Verification

After adding content: 1. ✅ `gbrain search "title" --limit 1` → confirms slug exists 2. ✅ `gbrain get <slug>` → confirms content is correct (not "/dev/stdin") 3. ✅ `gbrain stats` → confirms page count increased

### Integration with Other Skills

- **analyze-paper**: Use this skill's patterns when saving paper analyses to GBrain - **extract-wisdom**: Use import method for batch wisdom extraction - **summarize**: Save summaries using Method 1 (import from filesystem)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/gbrain-content-ops/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
