---
date: 2026-07-19
type: concept
title: Project Integration Workflow
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/project-integration-workflow
description: Set up integration projects following structured conventions, analyze
  source material, create implementation plans, develop skills, and maintain activity
  logs.
---

# Project Integration Workflow

> Set up integration projects following structured conventions, analyze source material, create implementation plans, develop skills, and maintain activity logs.

## Overview

- **When to Use** — - Starting a new integration project with specific folder structure requirements - Need to analyze external system documentation and extract actionable recommendations - Want to follow user-specified folder conventions for plans, research, decisions, and logs - Require systematic skill creation based on analyzed source material - Need to maintain clear activity logs for cross-session continuity
- **Prerequisites** — - Hermes Agent installed and configured - Access to source material to analyze (documentation, code repositories, etc.) - Basic understanding of Hermes skill structure - Terminal access for file operations
- **How to Run** — Invoke through the `skill_manage` tool with action="create" to initialize the skill, then follow the Procedure section using Hermes tools like `write_file`, `read_file`, `search_files`, and `skill_manage`.

## Further detail

### Quick Reference

- `skill_manage`: Create and manage skills - `write_file`: Create project files and documentation - `read_file`: Analyze source material - `search_files`: Locate existing files and documentation - `execute_code`: Run analysis scripts if needed - `references/maestro-integration-lessons.md`: Lessons learned from Maestro-Hermes integration

### Procedure

1. **Set up project structure** - Create root project directory if it doesn't exist - Create numbered folders per user specification (01.Core, 02.Research, etc.) - Create standard files: INDEX.md, AGENTS.md, ACTIVITY.md - Create subfolders: decisions/, memory/, logs/, Archive/

### Pitfalls

- **Skipping folder structure setup**: Leads to disorganized projects that don't follow user specifications - **Insufficient source analysis**: Results in incomplete understanding and poor integration planning - **Vague implementation plans**: Makes execution difficult and increases risk of missed requirements - **Poor skill categorization**: Causes skills to be difficult to discover and reuse - **Inconsistent activity logging**: Breaks cross-session continuity and makes progress tracking hard

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/project-integration-workflow/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
