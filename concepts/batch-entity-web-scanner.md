---
type: concept
title: Batch Entity Web Scanner
created: 2026-08-21
frontmatter_added: 2026-09-13
---

date: 2026-07-19
type: concept
title: Batch Entity Web Scanner
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- web-scraping
- batch
- entities
- signal-detection
- csv-pipeline
- python
- software-development
sources:
- hermes://skill/batch-entity-web-scanner
description: Take a list of named entities (companies, firms, orgs), resolve to URLs,
  probe for signals (job openings, tech stack, etc.), handle failures gracefully,
  and store structured results. Designed for multi-sector job-hunting pipelines but
  general to any entity→signal scanning task.
---

# Batch Entity Web Scanner

> Take a list of named entities (companies, firms, orgs), resolve to URLs, probe for signals (job openings, tech stack, etc.), handle failures gracefully, and store structured results. Designed for multi-sector job-hunting pipelines but general to any entity→signal scanning task.

## Overview

- **When to Use** — - Building a job-hunting pipeline across N companies/sectors - Checking which orgs in a list have a specific capability (hiring tech roles, using a technology, etc.) - Any "scan N entities for boolean signal" task where each entity has a web presence - Multi-sector scans where you want consistent methodology across govtech, fintech, legal, etc.
- **User Preferences (Kirk)** — - **Scan ALL entities in the list** — do not cherry-pick a subset based on HQ location or estimated relevance. The user wants the full picture, then chooses what to explore. If you stop at 4 of 23, you'll get called out. - **Document the methodology** with every run. Output a summary table, not just raw files. - **Rerunnable structure**: centralized `lib/` with generalized scripts, sector-specific CSVs in their own folders, a unified `run.py` entry point.
- **Pitfalls** — 1. **Python 3.8 type hints**: `list[str]` breaks on 3.8. Use `List[str]` from `typing` or `Tuple[bool, Optional[str]]`. 2. **Cloudflare / bot protection**: Some sites block programmatic access. Log the failure and move on — do not retry indefinitely. 3. **JS-rendered career pages**: Webflow, Angular, React sites often serve empty HTML. The keyword check returns false for these. Note it in results but can't be fixed without a browser renderer. 4. **Domain guessing misses non-standard names**: "O'Melveny & Myers" → slug mismatch, or companies with radically different domain names from their trad

## Further detail

### Related Skills

- **parallel-search-orchestration**: ThreadPoolExecutor + as_completed pattern (this skill's collection layer uses that) - **project-scaffolding**: Organizing multi-directory project repos (used for the job_hunter folder structure) - **verification-before-completion**: Verifying results before claiming done (multiple ATS hit counts need verification)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/batch-entity-web-scanner/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
