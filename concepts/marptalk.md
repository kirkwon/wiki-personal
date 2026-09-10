---
date: 2026-07-19
type: concept
title: Marptalk
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Slides
- MARP
- Presentation
- Markdown
- Creative
- uncategorized
sources:
- hermes://skill/marptalk
description: Create MARP (Markdown Presentation) presentations from structured content.
  Convert markdown to slide decks using the MARP CLI. Supports dark themes, code highlighting,
  diagrams, and export to HTML/PDF. Trigger on phrases like "marp", "presentation",
  "slide deck", "markdown slides", "marptalk", "presentation from markdown".
---

# Marptalk

> Create MARP (Markdown Presentation) presentations from structured content. Convert markdown to slide decks using the MARP CLI. Supports dark themes, code highlighting, diagrams, and export to HTML/PDF. Trigger on phrases like "marp", "presentation", "slide deck", "markdown slides", "marptalk", "presentation from markdown".

## Overview

- **Prerequisites** — - The `marp` CLI on PATH. Verify: invoke `marp --version` through the `terminal` tool. (Observed path: `/opt/homebrew/bin/marp` on macOS Homebrew installs; version `@marp-team/marp-cli v4.4.0` as of 2026-07.) - Node.js (the marp CLI bundles its own Chromium for PDF export).
- **When to Use** — - "Create a slideshow" / "make a presentation" / "slides from this content" - "marptalk" / "marp" / "markdown slides" - Converting a NotebookLM analysis, report, or structured doc into a visual deck
- **How to Run** — 1. Author `deck.md` (frontmatter + content) and optionally `theme.css` (custom theme). 2. Render to HTML (primary deliverable):

## Further detail

### Quick Reference

**Frontmatter essentials** (top of `deck.md`):

### Pitfalls

- **`style:` frontmatter directive does NOT take a file path.** `style: theme.css` in frontmatter is silently treated as (broken) raw CSS text, causing MARP to fall back to the default theme with NO error. To apply a custom CSS theme file you MUST register it on the CLI: `marp --theme-set theme.css`. (This was a real failure in a 2026-07 session: deck rendered, looked fine at a glance, but the entire dark theme was missing until `--theme-set` was added.) - **Silent theme fallback.** If the theme name doesn't resolve to a registered theme, MARP uses `default` and emits no warning. Always verify

### Verification

After EVERY render, confirm the custom theme actually landed (don't trust a successful exit code):

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/marptalk/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
