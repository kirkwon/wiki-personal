---
date: 2026-07-19
type: concept
title: Macos Applescript Patterns
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- apple
sources:
- hermes://skill/macos-applescript-patterns
description: Patterns, pitfalls, and working recipes for driving macOS apps via AppleScript
  from Hermes. Covers osascript execution, HTML note creation, Reminders extraction,
  and Python integration.
---

# Macos Applescript Patterns

> Patterns, pitfalls, and working recipes for driving macOS apps via AppleScript from Hermes. Covers osascript execution, HTML note creation, Reminders extraction, and Python integration.

## Overview

- **Trigger** — - User asks to read/create/search Apple Notes, Reminders, Calendar events - Any task requiring `osascript` with multi-line AppleScript - Bulk data extraction from macOS apps
- **Pitfalls** — | Pitfall | Fix | |---------|-----| | Shell heredoc `osascript <<'EOF'` | Write `.scpt` file, run `osascript file.scpt` | | `body` returns "missing value" | Check string equality before displaying | | `due date` throws on unset | Wrap in `try ... end try` | | Large HTML in AppleScript | Embed escaped HTML in `.scpt` file rather than shell arg | | Multiple accounts (iCloud, Google, Yahoo) | Specify `account "iCloud"` explicitly | | AppleScript output too large | Use delimited text output, parse in Python | | **Apple Events hang (systemic)** | **Diagnose with `timeout 15 osascript -e '...'`, use
- **References** — - `references/apple-events-hang-2026-07-16.md` — Reminders.app Apple Events hang on macOS 26.1, memo CLI source inspection, computer_use AX tree limitation, Siri as fallback - `references/google-workspace-python-compat.md` — Python 3.11/urllib3 vs 3.12+ for GWS skill

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/apple/macos-applescript-patterns/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
