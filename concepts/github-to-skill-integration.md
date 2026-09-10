---
date: 2026-07-19
type: concept
title: Github To Skill Integration
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- Github
- Skills
- Integration
- Curation
- Subagents
- software-development
sources:
- hermes://skill/github-to-skill-integration
description: Turn GitHub repos into integrated Hermes skills with wiring.
---

# Github To Skill Integration

> Turn GitHub repos into integrated Hermes skills with wiring.

## Overview

- **When to Use** — - "Turn these GitHub repos into a skill" (prompts, snippets, configs, templates) - "Curate the best N items from each repo and build a reusable skill" - "Integrate the new skill into my existing scripts/workflows" - User provides multiple URLs + a focus ("formatting and research", "auth flow only") - Need to wire a new skill into existing cron scripts or templates
- **Prerequisites** — - `web_extract` available (or `web_search` for discovery) - `skill_view` the `skill-creator` and `subagent-driven-development` skills - Target infra known: existing scripts, cron jobs, or templates the skill should wire into
- **How to Run** — Invoke through the `terminal`, `web_extract`, `skill_manage`, and `delegate_task` tools across four phases.

## Further detail

### Pitfalls

- **Truncated extracts hide prompts in the middle** — cached files at `~/.hermes/cache/web/` have full text; read with `read_file` offset to get the truncated middle - **Skill dirs reject `projects/`** — only `assets/references/scripts/templates` allowed. Test projects go in the workspace (`~/clawd/`), not the skill - **Subagent "already present" claims** — always verify with `search_files` before accepting. Subagents conflate "I didn't change it" with "it was already there" - **Structurally different sibling files** — 5 scripts with the same name pattern may have different headers (some lack

### Verification

Run the full chain end-to-end and confirm the output artifact exists with expected structure:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/github-to-skill-integration/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
