---
date: 2026-07-19
type: concept
title: Customize Clawd Project
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/customize-clawd-project
description: Customize a bootstrapped clawd project with specific metadata and decision
  logging.
---

# Customize Clawd Project

> Customize a bootstrapped clawd project with specific metadata and decision logging.

## Overview

- **When to Use** — - You have run `clawd-project-bootstrap` and need to customize the generated files - Starting a new project requiring specific metadata in INDEX.md, AGENTS.md, etc. - Setting up a project with custom decision logging configuration - Preparing a project for specialized use (research, development, experiments)
- **Prerequisites** — - A project directory created via `clawd-project-bootstrap` (with 01.Core, 02.Research, Archive, decisions, memory, logs subfolders) - `decision-master` skill installed (provides decision logging templates) - Access to Hermes tools: `read_file`, `write_file`, `patch`
- **How to Run** — Follow the Procedure section using Hermes tools. For batch operations, consider using `execute_code` with Python for multiple file replacements.

## Further detail

### Quick Reference

- `read_file`: Retrieve template or target file content - `write_file`: Save customized content to files - `patch`: Perform targeted placeholder replacements (alternative to full rewrite)

### Procedure

Follow these steps in order to customize a bootstrapped Clawd project:

### Pitfalls

- **Incomplete placeholder replacement**: Missing one instance causes incorrect metadata - **Wrong project number**: Using an existing number breaks git and references - **Missing decision protocol**: AGENTS.md won't have decision logging guidance - **Incorrect date format**: ACTIVITY.md expects YYYY-MM-DD format - **Forgetting parent workspace updates**: Project won't appear in workspace INDEX.md - **Template drift**: If bootstrap skill updates, customization steps may need adjustment

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/customize-clawd-project/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
