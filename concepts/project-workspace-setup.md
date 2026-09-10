---
date: 2026-07-19
type: concept
title: Project Workspace Setup
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/project-workspace-setup
description: Initialize project workspace structure and indices.
---

# Project Workspace Setup

> Initialize project workspace structure and indices.

## Overview

- **When to Use** — - Setting up a new project workspace with multiple subprojects - Initializing standardized INDEX.md files across project folders - Ensuring consistent folder navigation structure - Creating reusable workspace setup for agent teams
- **What This Skill Does** — This skill sets up the structural foundation for projects: - Creates project directories under the workspace root - Generates standardized INDEX.md template files in each project - Updates the root workspace INDEX.md with folder map entries - Logs setup activity to ACTIVITY.md - Optionally enriches projects with related file discovery (macOS only)
- **What This Skill Does NOT Do** — **Important**: This skill does NOT create the actual content deliverables for projects. It only creates the structural placeholders (INDEX.md files with project descriptions).

## Further detail

### What This Skill Does NOT Do

**Important**: This skill does NOT create the actual content deliverables for projects. It only creates the structural placeholders.

### Prerequisites

- A Unix‑like shell (bash, zsh) available via the Hermes `terminal` tool (works on macOS, Linux, Windows + WSL/Git Bash) - Write access to the workspace root - (Optional) For enrichment: macOS with Spotlight indexing enabled

### How to Run

Invoke through the `terminal` tool with the provided script:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/project-workspace-setup/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
