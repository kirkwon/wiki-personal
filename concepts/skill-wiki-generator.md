---
date: 2026-07-19
type: concept
title: Skill Wiki Generator
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- knowledge-management
sources:
- hermes://skill/skill-wiki-generator
description: Generate wiki pages for skills that are missing a wiki page to close
  the declarative gap. Uses the wiki-tools CLI and the skills_list tool.
---

# Skill Wiki Generator

> Generate wiki pages for skills that are missing a wiki page to close the declarative gap. Uses the wiki-tools CLI and the skills_list tool.

## Overview

- **Steps** — 1. List all skills using `skills_list`. 2. For each skill, check if a wiki page exists (by querying the wiki for the skill name). 3. If not, create a wiki page using the skill's SKILL.md as the initial content.
- **Usage** — Run the script in `scripts/generate_skill_wikis.sh` (if available) or follow the steps above.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/skill-wiki-generator/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
