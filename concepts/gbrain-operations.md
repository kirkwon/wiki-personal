---
date: 2026-07-19
type: concept
title: Gbrain Operations
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- knowledge-management
sources:
- hermes://skill/gbrain-operations
description: Comprehensive GBrain workflow patterns for migration recovery, cycle
  management, and automation setup. Covers troubleshooting common issues, setting
  up continuous learning pipelines, and integrating with notification systems.
---

# Gbrain Operations

> Comprehensive GBrain workflow patterns for migration recovery, cycle management, and automation setup. Covers troubleshooting common issues, setting up continuous learning pipelines, and integrating with notification systems.

## Overview

- **Overview** — This skill provides proven workflows for GBrain operations, with focus on migration recovery, cycle management, and establishing automated maintenance pipelines. It captures lessons learned from real-world troubleshooting and automation setup.
- **gbrain think Requires API Key in Shell Environment** — **Problem:** `gbrain think "<question>"` fails with `"(no LLM available — set anthropic_api_key via gbrain config or ANTHROPIC_API_KEY env)"` even when `models.think` is configured to an OpenRouter model and `OPENROUTER_API_KEY` is set in Hermes config.
- **Troubleshooting Checklist** — **Migration Issues:** - [ ] Check git status in all source directories - [ ] Stash or commit uncommitted changes - [ ] Handle corrupted git indexes - [ ] Verify database connection: `gbrain init --url <connection_string>` - [ ] Run migration: `gbrain apply-migrations --yes`

## Further detail

### Related Skills

- `notebooklm-research-pipeline` - For research workflow integration - `obsidian-vault-management` - For Obsidian-specific operations - `autonomous-ai-agents` - For background task automation - `wiki-okf-compliance` - Make a wiki OKF-compatible (type taxonomy, descriptions, index.md manifests)

### References

- GBrain Documentation: https://hermes-agent.nousresearch.com/docs - Migration v0.32.2 Release Notes: Facts join the system-of-record invariant - Background Monitoring Scripts: See `scripts/gbrain_cycle_runner.sh` - Frontmatter Validation Patterns: See `references/frontmatter-fixes.md` - **Backup Verification Script: See `~/.hermes/scripts/backup-verify.sh`** — checks git fsck, archive SHA256 samples, daily manifest hash, gbrain health. Cron `backup-integrity-verify` runs daily at 3:05 AM.

### Support Files

- `scripts/gbrain_cycle_runner.sh` - Automated cycle monitoring and execution - `scripts/batch-timeline-add.sh` - Batch add gbrain timeline entries from entity frontmatter dates - `scripts/notify_telegram.sh` - Telegram notification integration - `scripts/fix-all-frontmatter.py` - Phase 1-2 bulk fix: remove dangling `----` artifacts, add missing `---` close, split jammed inline lists, deduplicate YAML keys - `scripts/fix-frontmatter-enhanced.py` - Phase 3-4 enhanced fix: quote colons in values, close unclosed flow collections, fix nested quotes, fix missing open/close delimiters - `scripts/fix

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/knowledge-management/gbrain-operations/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
