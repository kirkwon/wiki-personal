---
title: Google Workspace Integration (45 Skills + NLM Bridges)
status: completed
priority: P2
created: 2026-06-28T00:00:00.000Z
updated: 2026-06-28T00:00:00.000Z
---

# Google Workspace Integration

## Summary
45 Hermes skills patched with Google Workspace integration (Gmail, Calendar, Drive, Sheets, Docs, Contacts). 7 research skills enhanced with NotebookLM bridges. Shared helper library (`gworkspace.py`) with 9 tested functions.

## Progress

### Core Infrastructure
- [x] OAuth2 setup complete — 8 scopes with full write access
- [x] Token at `~/.hermes/google_token.json` (auto-refreshes)
- [x] `gworkspace.py` shared helper (372+ lines, 9 functions, 9/9 tests passing)
- [x] Google Workspace skill v1.0.0 in Hermes skills library

### 45 Skills Integrated
- [x] 20 skills with Sheets storage
- [x] 9 skills with Gmail alerting
- [x] 8 skills with Docs presentation
- [x] 5 skills with Calendar scheduling
- [x] 4 skills with Contacts lookup
- [x] 4 skills with Drive upload
- [x] 7 skills with NotebookLM bridges

### NotebookLM Bridges (7 skills)
- [x] `last30days` → `last30days-research`
- [x] `research-agent` → `hermes-research`
- [x] `storm-research` → `storm-perspectives`
- [x] `earnings-analysis` → `earnings-tracker`
- [x] `web-researcher` → `web-research`
- [x] `morning-note` → `daily-briefing`
- [x] `conversation-logging-review` → `weekly-review`

## Key Files
- `~/.hermes/scripts/gworkspace.py` — shared helper (9 functions)
- `~/.hermes/google_token.json` — OAuth token (8 scopes)
- `~/.hermes/skills/productivity/google-workspace/` — skill directory
- `~/clawd/gworkspace-integration-log.md` — integration log (needs update: 42→45)

## Automation / Cron
- `d67be14475a0` — Morning Briefing (uses Google Workspace skill)

## Notes
- Integration log at `~/clawd/gworkspace-integration-log.md` says 42/42 — should be updated to 45/45 + 7 NLM bridges
- Pattern: `create_doc()` → `nlm source add --drive <doc-id>` is the NotebookLM bridge
