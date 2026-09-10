---
date: 2026-08-02
type: concept
title: Graph Colorize
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/graph-colorize
description: Color-code the Obsidian graph view by rewriting `.obsidian/graph.json`
  colorGroups. Use this skill when the user says "color my graph", "color code obsidian",
  "colorize the graph", "color the graph by tag", "color by category", "highlight
  visibility in graph", "make the graph colorful", "distinguish tags in graph", or
  wants nodes in Obsidian's graph view tinted by tag, folder, or visibility. Generates
  a `colorGroups` array from the vault's actual tags/categories and merges it into
  the existing graph.json without clobbering other graph settings. Always backs up
  first.
---

# Graph Colorize

> Color-code the Obsidian graph view by rewriting `.obsidian/graph.json` colorGroups. Use this skill when the user says "color my graph", "color code obsidian", "colorize the graph", "color the graph by tag", "color by category", "highlight visibility in graph", "make the graph colorful", "distinguish tags in graph", or wants nodes in Obsidian's graph view tinted by tag, folder, or visibility. Generates a `colorGroups` array from the vault's actual tags/categories and merges it into the existing graph.json without clobbering other graph settings. Always backs up first.

## Overview

- **Before You Start** — 1. **Resolve config** — follow the Config Resolution Protocol in `llm-wiki/SKILL.md` (walk up CWD for `.env` → `~/.obsidian-wiki/config` → prompt setup). This gives `OBSIDIAN_VAULT_PATH`. 2. Confirm `$OBSIDIAN_VAULT_PATH/.obsidian/` exists. If it doesn't, the vault has never been opened in Obsidian — tell the user to open the vault once in Obsidian, then re-run. 3. **Warn the user if Obsidian is likely open**: Obsidian overwrites `graph.json` on close. Tell them to close the vault first, or be ready to reload (Cmd/Ctrl+R) and not touch the graph settings until they reload.
- **Step 1: Pick a Mode** — Infer the mode from the user's phrasing. If ambiguous, default to **by-tag**.
- **Step 3: Merge into graph.json (Do Not Clobber)** — 1. Read the existing `$VAULT_PATH/.obsidian/graph.json`. If it doesn't exist, start from this minimal default:

## Further detail

### Step 4: Report and Log

Print a summary like:

### Edge Cases

- **No tags in vault** in `by-tag` mode → fall back to `by-category` and tell the user. - **User wants to undo** → restore from the latest `graph.json.backup-*` and note that in `log.md`. - **User wants to clear all color groups** → set `colorGroups: []`, back up, log as `GRAPH_COLORIZE mode=clear`. - **`.obsidian/` missing** → the vault hasn't been opened in Obsidian yet. Tell the user to open it once, then re-run. Don't create `.obsidian/` yourself — Obsidian populates many files there on first open. - **Query syntax gotchas**: folder paths with spaces need quoting (`path:"my folder"`); tags

### Notes

- This is a pure config edit — no page content changes, no frontmatter writes. - Re-running is safe: each run creates a new backup, only `colorGroups` is rewritten. - If the user has manually curated color groups they want to keep, offer `combined` mode or ask before overwriting. - The palette here matches `wiki-export`'s `graph.html` community colors, so the Obsidian graph and the exported visualization look consistent.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/graph-colorize/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
