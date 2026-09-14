---
type: concept
title: Wiki Vault Access
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Wiki Vault Access
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- wiki
- vault
- api
- library
- python
- frontmatter
- graph
- knowledge-management
sources:
- hermes://skill/wiki-vault-access
description: Build shared Python libraries that normalize access to an Obsidian vault
  with custom frontmatter conventions. Handles dual schema generations, typed-edge
  graph traversal, stale/confidence/lifecycle fields, and write governance with dry-run.
  The foundation layer for any vault-tooling project.
---

# Wiki Vault Access

> Build shared Python libraries that normalize access to an Obsidian vault with custom frontmatter conventions. Handles dual schema generations, typed-edge graph traversal, stale/confidence/lifecycle fields, and write governance with dry-run. The foundation layer for any vault-tooling project.

## Overview

- **When This Skill Activates** — Use this when: - Building a new tool that reads/writes an Obsidian vault - You discover multiple scripts reimplementing the same frontmatter parsing - User says "let's build a unified toolset" or "we need a shared library" - Adding graph traversal, staleness detection, or write governance to vault tools - Working with an Obsidian vault that has custom YAML frontmatter schema
- **Architecture Pattern** — **Rule:** Every tool imports from `wiki_api.py`. No tool reimplements frontmatter parsing.
- **Pitfalls** — - **`load_all()` silently returns 0 pages when `use_cache=False` (the default).** The original code only populated `_page_cache` inside the `if self._use_cache:` block. When cache is off, it jumped to the yield loop yielding nothing — making `stats()` report 0 stale pages (false all-clear) or crash with `KeyError`. Fix: added `else:` branch calling `self.load_page(fp)` for every path. **If stats() reports suspiciously clean numbers, verify load_all() is actually yielding pages.** - **"No frontmatter delimiters" is NOT a parse error.** Files without `---` (raw sources, CL4R1T4S dumps, index.md)

## Further detail

### Reference

The production implementation lives in: `~/Downloads/10-projects/10-active-projects/wiki-tools/wiki_api.py` (~1,350 lines)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/wiki-vault-access/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
