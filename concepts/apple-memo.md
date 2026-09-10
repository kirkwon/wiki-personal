---
date: 2026-07-19
type: concept
title: Apple Memo
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- apple
sources:
- hermes://skill/apple-memo
description: Manage Apple Notes via the memo CLI tool.
---

# Apple Memo

> Manage Apple Notes via the memo CLI tool.

## Overview

- **Installation** — The `memo` tool should already be installed via Homebrew (`brew install mjambon/memo/memo`). This skill assumes it is available in your PATH.
- **Integration with Hermes** — You can use `delegate_task` to run memo commands in the background, e.g., to backup notes nightly.
- **Notes** — - The `memo` tool stores notes in `~/Library/Group Containers/group.com.apple.notes/`. - Requires macOS Accessibility permissions for some operations. - For full AppleScript access, see the `apple-notes` skill. - Notes are exported as plain text; original formatting (checklists, tables) may be lost.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/apple/apple-memo/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
