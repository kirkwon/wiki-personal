---
date: 2026-07-19
type: concept
title: Catalyst Calendar
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- equity-research
sources:
- hermes://skill/catalyst-calendar
---

# Catalyst Calendar

## Overview

- **Trigger Conditions** — When the user asks to: - User asks to catalyst-calendar
- **Important Notes** — - Earnings dates shift — verify against company IR pages and Bloomberg/FactSet closer to the date - Pre-announce risk: track companies with a history of pre-announcing (positive or negative) - Conference attendance lists are valuable — which companies are presenting and which are conspicuously absent? - Some catalysts are recurring (monthly industry data) — build a template and auto-populate - Color-code by impact level: Red = high impact, Yellow = moderate, Green = routine - Archive past catalysts with the actual outcome — builds pattern recognition over time
- **Google Workspace Integration** — Catalysts are calendar-driven, so this skill writes to **both** Google Calendar (as events) and a Google Sheet named **"Hermes Catalyst Calendar"** (for the sortable tracking table). Use the shared `gworkspace.py` helper.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/finance/equity-research/catalyst-calendar/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
