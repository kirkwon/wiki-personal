---
date: 2026-07-19
type: concept
title: Clawd Project Bootstrap
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- devops
sources:
- hermes://skill/clawd-project-bootstrap
description: Create new clawd project folders from a template with OKF frontmatter,
  AGENTS.md run book, decision-master integration, and gbrain sync readiness.
---

# Clawd Project Bootstrap

> Create new clawd project folders from a template with OKF frontmatter, AGENTS.md run book, decision-master integration, and gbrain sync readiness.

## Overview

- **When to Use** — - Starting a new project, research track, or experiment that belongs in `~/clawd/` - User says "create a new clawd project" or "new project for X" - A new concern emerges that doesn't fit an existing numbered folder
- **Prerequisites** — - `~/clawd/` exists (it does — this is the primary workspace) - `git` available (for init + initial commit) - decision-master skill installed (for templates — already present)
- **Execution Steps** — Follow these in order. **Do not skip steps.**

## Further detail

### OKF Compliance Notes

- **`index.md`** at project root → OKF reserved name, optional frontmatter with `okf_version` - **Every `.md` file** that is a "concept document" must have YAML frontmatter with `type` field - **AGENTS.md** → `type: playbook` - **Decision records** → `type: decision-record` - **`log.md`** → OKF reserved name for changelog. We use `ACTIVITY.md` instead (existing clawd convention). OKF says `log.md` is optional, and agents reading this workspace already know to check ACTIVITY.md. If strict OKF compliance is needed later, add a symlink: `ln -s ACTIVITY.md log.md` - **`Archive/`** files should get

### gbrain Integration

After creating the project, it's ready for gbrain sync:

### Pitfalls

- **Don't renumber existing folders.** The new folder gets the NEXT number. Never shuffle numbers — inbound references (cron, config, gbrain) break. - **Don't create folders past N=50 at the top level.** If you're at N=30+, consider grouping related projects into subdirectories. The agent-folder-structure skill warns against deep nesting, but 30+ flat folders is equally bad for navigation. - **Git init inside a git-tracked parent.** `~/clawd/` may or may not have its own `.git`. The new project folder gets its OWN `.git` (independent repo). Don't add it as a submodule unless explicitly asked.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/clawd-project-bootstrap/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
