---
date: 2026-07-19
type: concept
title: Git Changelog
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- git
- changelog
- release-notes
- documentation
- conventional-commits
- software-development
sources:
- hermes://skill/git-changelog
description: 'Generate structured changelogs from git commit history: retrieve commits
  between two SHAs, categorize by conventional commit types, format with PR links,
  and update CHANGELOG.md.'
---

# Git Changelog

> Generate structured changelogs from git commit history: retrieve commits between two SHAs, categorize by conventional commit types, format with PR links, and update CHANGELOG.md.

## Overview

- **Parameters** — | Parameter | Required | Description | |-----------|----------|-------------| | `start_sha` | ✅ | Starting git SHA (exclusive — commits after this are included) | | `end_sha` | ✅ | Ending git SHA (inclusive) |
- **Pitfalls** — - Filter merge commits with `--no-merges` - Fallback to commit SHA links if remote URL unavailable - For 100+ commits, summarize by category rather than listing every commit - If no tags exist, ask user for SHA range
- **Google Workspace Integration** — Publish release notes as a Google Doc so they're shareable, version-tracked, and accessible to stakeholders who don't access the git repo directly.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/git-changelog/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
