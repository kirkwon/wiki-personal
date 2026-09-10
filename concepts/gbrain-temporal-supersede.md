---
date: 2026-08-02
type: concept
title: Gbrain Temporal Supersede
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- Gbrain
- Temporal
- Knowledge-Graph
- knowledge
sources:
- hermes://skill/gbrain-temporal-supersede
description: Supersede gbrain pages with temporal validity metadata.
---

# Gbrain Temporal Supersede

> Supersede gbrain pages with temporal validity metadata.

## Overview

- **When to Use** — - A new gbrain page contradicts or updates an older page's claims - You need to mark a page as out-of-date without deleting history - Auditing the brain for stale, expired, or orphaned pages - After capturing a v2/v3 of a concept and wanting a paper trail
- **Prerequisites** — - `gbrain` CLI installed and initialized (`gbrain init` done) - Python 3.10+ with `pyyaml` (`pip install pyyaml`) - Brain directory at `~/brain/`
- **How to Run** — Invoke the supersede script through the `terminal` tool:

## Further detail

### Quick Reference

**Supersede script flags:** - `--new-slug <slug>` — the page that replaces (required) - `--supersede <slug>` — old page to mark superseded (repeatable) - `--dry-run` — show what would change without writing - `--auto` — skip confirmation prompts

### Procedure

1. **Identify the contradiction.** Use `gbrain search "<topic>"` to find related pages. Read them with `gbrain get <slug>` to confirm they make claims the new page supersedes.

### The Temporal Frontmatter Model

**Old page (superseded) gets:**

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/gbrain-temporal-supersede/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
