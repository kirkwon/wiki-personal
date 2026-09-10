---
date: 2026-08-02
type: concept
title: Gbrain Dual Layer Acl
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- knowledge
sources:
- hermes://skill/gbrain-dual-layer-acl
description: Implement gbrain dual-layer ACL for data privacy.
---

# Gbrain Dual Layer Acl

> Implement gbrain dual-layer ACL for data privacy.

## Overview

- **When to Use** — - You need to prevent personal data (PII, credentials, private notes) from leaking via gbrain export/search/query - You want to store personal-derived knowledge in gbrain while keeping raw data local - You require defense-in-depth security for personal information in your knowledge base - You've discovered that gbrain's native source isolation doesn't prevent search leakage
- **Prerequisites** — - gbrain 0.42.53.0 or later with PostgreSQL backend - Access to the gbrain database (typically at ~/.hermes/gbrain/data/gbrain.db) - PostgreSQL client tools (psql) installed and in PATH - Basic familiarity with SQL and gbrain CLI - Write access to ~/.local/bin/ for installing the wrapper script
- **How to Run** — Invoke through the `skill` tool with the gbrain-dual-layer-acl skill, or use the installed scripts directly: - `gbrain-safe` - Drop-in replacement for gbrain that filters personal data - `gbrain-tag-personal.py` - Tag pages as personal/private for ACL filtering - `gbrain-acl-audit.py` - Audit gbrain for personal data leaks

## Further detail

### Quick Reference

- gbrain-safe search "query"          # Filters personal data by default - gbrain-safe search "query" --include-personal  # Opt-in to see personal data - gbrain-tag-personal.py user --tag personal    # Tag a page as personal - gbrain-tag-personal.py --scan             # Scan for untagged PII - gbrain-acl-audit.py                       # Verify no personal data leaks

### Procedure

1. **Setup the isolated source for CRM data**

### Verification

Run the full audit to confirm no personal data leaks:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/security/gbrain-dual-layer-acl/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
