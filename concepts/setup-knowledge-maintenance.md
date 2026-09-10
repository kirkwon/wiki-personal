---
date: 2026-07-19
type: concept
title: Setup Knowledge Maintenance
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- knowledge-management
sources:
- hermes://skill/setup-knowledge-maintenance
description: Set up recurring knowledge maintenance for skills and wiki.
---

# Setup Knowledge Maintenance

> Set up recurring knowledge maintenance for skills and wiki.

## Overview

- **When to Use** — - You want to automate periodic checks for undocumented skills, unactionable concepts, stale wiki pages, and GBrain warnings. - You have just completed a knowledge evaluation and wish to turn the ad-hoc follow-up into a repeating process. - You are setting up a new Hermes instance and want to establish maintenance routines.
- **Prerequisites** — - Hermes agent with access to skill_manage, cronjob, read_file, write_file, delegate_task tools. - Existing wiki-personal and GBrain vaults (or willingness to create them). - knowledge-eval.py script present at ~/.hermes/scripts/knowledge-eval.py (or similar logic). - Basic familiarity with creating skills and cron jobs via Hermes.
- **How to Run** — Execute the steps in the Procedure section, either manually or via delegate_task. Each step can be run individually; the full setup is idempotent (safe to run multiple times).

## Further detail

### Procedure

1. Ensure the knowledge-maintenance skill exists (create if missing, update if outdated). a. Check if skill exists: `skill_view name='knowledge-maintenance'`. b. If it does not exist or needs updating, create it with skill_manage (action='create') using the SKILL.md content from the knowledge-maintenance skill (see references or recreate from the steps below). c. The knowledge-maintenance skill should contain steps to: - List all skills and compare with wiki concepts to find undocumented skills. - Check wiki concepts for associated skills to find unactionable concepts. - Identify stale wiki pa

### Quick Reference

- skill_view name='knowledge-maintenance' - cronjob list - cronjob create --name weekly-knowledge-maintenance --prompt "Run the knowledge-maintenance skill..." --schedule "0 10 * * 0" --skills knowledge-maintenance --deliver local - delegate_task goal='Run the knowledge-maintenance skill to perform periodic knowledge base maintenance tasks.'

### Pitfalls

- If the knowledge-maintenance skill is missing or broken, the cron job will fail silently (if no_agent) or produce errors. Always test the skill manually before scheduling. - Ensure the cron job's delivery method matches your preference; local delivery stores output in ~/.hermes/cron/output/<job_id>/. - The knowledge-maintenance skill may need updates if your knowledge base structure changes (e.g., new tools or scripts). - Do not schedule the cron job too frequently; weekly is sufficient for most knowledge bases.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/setup-knowledge-maintenance/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
