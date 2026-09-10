---
date: 2026-07-19
type: concept
title: Knowledge Wiki Gap Filler
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- knowledge
sources:
- hermes://skill/knowledge-wiki-gap-filler
description: Create wiki pages to close skill declarative gap.
---

# Knowledge Wiki Gap Filler

> Create wiki pages to close skill declarative gap.

## Overview

- **When to Use** — - The knowledge‑eval daily shows a growing declarative gap (skills without wiki pages). - You want to keep the wiki in sync with your skill set. - You notice episodic memory (daily notes) increasing and want to confirm it's expected.
- **Prerequisites** — - Hermes agent with access to: `terminal`, `read_file`, `write_file`, `search_files`, `web_search` (optional for enriching stubs), `cronjob` (if scheduling), `memory`. - The `comprehension-debt-report.py` script must be present in `~/.hermes/scripts/`. - Write permission to `~/wiki-personal` (the default vault used by the comprehension-debt-report). If your wiki is located elsewhere, adjust the paths accordingly. - Basic shell and Python literacy.
- **How to Run** — Execute the procedure steps manually via Hermes tools, or schedule the wrapper script as a cron job.

## Further detail

### Quick Reference

- Run comprehension‑debt report: `hermes execute_code -c \"import subprocess; subprocess.run(['python3', '~/.hermes/scripts/comprehension-debt-report.py'])\"` - Wiki directory: `~/wiki-personal/` (adjust if you use a different vault). - Example wiki page frontmatter:

### Procedure

1. **Generate the Debt Report** Run the comprehension‑debt report to get current numbers and list of missing skills (if the script outputs them; otherwise compute from the JSON).

### Pitfalls

- **Filename collisions**: Two skills that differ only in case or punctuation may map to the same filename. Ensure uniqueness by adding a numeric suffix if needed. - **Frontmatter errors**: Missing or malformed YAML will prevent GBrain from processing the page. Always validate a sample page with `hermes read_file` and check that file` to confirm the frontmatter is intact. - **Overwriting existing pages**: The skill skips files that already exist; if you intend to update existing stubs, change the write mode to overwrite. - **Delay in GBrain indexing**: After creating pages, GBrain may take a m

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge/knowledge-wiki-gap-filler/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
