---
date: 2026-07-19
type: concept
title: Obsidian Vault Cleanup
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- note-taking
sources:
- hermes://skill/obsidian-vault-cleanup
description: Fix common Obsidian vault formatting issues - infobox syntax, YAML frontmatter
  errors, template placeholders, and related field syntax
---

# Obsidian Vault Cleanup

> Fix common Obsidian vault formatting issues - infobox syntax, YAML frontmatter errors, template placeholders, and related field syntax

## Overview

- **When to Use** — - Importing notes from Wikipedia or other wikis (infobox syntax) - Migrating notes from other note-taking systems - Frontmatter not rendering as properties in Obsidian - YAML parsing errors in markdown files - Inconsistent tag/category formatting across vault - Template placeholders (`{{date}}`, `{{title}}`) in non-template files
- **Quick Reference Table** — | Issue | Pattern to Find | Fix | |-------|-----------------|-----| | Infobox | `== Infobox ==` | Convert to `## Quick Reference` | | Related field | `related: [[A]], [[B]]` | Convert to `related:\n  - [[A]]\n  - [[B]]` | | Template date | `{{date}}` | Replace with actual date | | Empty category | `category: []` | Replace with `category: ["General"]` | | Unquoted tags | `tags: [my tag]` | Replace with `tags: ["my tag"]` |
- **Common Pitfalls** — 1. **Don't skip backup** - Always backup before bulk operations 2. **Test on sample first** - Run fixes on 5-10 files before applying to entire vault 3. **Check YAML carefully** - Comma-separated wikilinks are the most common YAML error 4. **Template files are different** - Don't fix placeholders in actual template files 5. **Verify after fixing** - Always run verification script after bulk fixes

## Further detail

### Verification Checklist

- [ ] No `== Infobox ==` syntax remaining - [ ] All frontmatter parses as valid YAML - [ ] No template placeholders in non-template files - [ ] All category arrays have values - [ ] Tags are properly quoted when containing spaces - [ ] Related fields use proper YAML array format - [ ] Properties render correctly in Obsidian

### Related Skills

- [obsidian](obsidian) - Basic Obsidian vault operations - [obsidian-vault-management](obsidian-vault-management) - Vault enhancement and visualization - [unified-book-library-management](unified-book-library-management) - Book library formatting

### References

- Obsidian Frontmatter: https://help.obsidian.md/Editing+and+formatting/Properties - YAML Specification: https://yaml.org/spec/ - Obsidian Wikilinks: https://help.obsidian.md/Linking+notes+and+files/Internal+links

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/note-taking/obsidian-vault-cleanup/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
