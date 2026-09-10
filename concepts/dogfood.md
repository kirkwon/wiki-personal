---
date: 2026-07-19
type: concept
title: Dogfood
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- qa
- testing
- browser
- web
- dogfood
- software-development
sources:
- hermes://skill/dogfood
description: 'Exploratory QA of web apps: find bugs, evidence, reports.'
---

# Dogfood

> Exploratory QA of web apps: find bugs, evidence, reports.

## Overview

- **Overview** — This skill guides you through systematic exploratory QA testing of web applications using the browser toolset. You will navigate the application, interact with elements, capture evidence of issues, and produce a structured bug report.
- **Prerequisites** — - Browser toolset must be available (`browser_navigate`, `browser_snapshot`, `browser_click`, `browser_type`, `browser_vision`, `browser_console`, `browser_scroll`, `browser_back`, `browser_press`) - A target URL and testing scope from the user
- **Inputs** — The user provides: 1. **Target URL** — the entry point for testing 2. **Scope** — what areas/features to focus on (or "full site" for comprehensive testing) 3. **Output directory** (optional) — where to save screenshots and the report (default: `./dogfood-output`)

## Further detail

### Workflow

Follow this 5-phase systematic workflow:

### Tools Reference

| Tool | Purpose | |------|---------| | `browser_navigate` | Go to a URL | | `browser_snapshot` | Get DOM text snapshot (accessibility tree) | | `browser_click` | Click an element by ref (`@eN`) or text | | `browser_type` | Type into an input field | | `browser_scroll` | Scroll up/down on the page | | `browser_back` | Go back in browser history | | `browser_press` | Press a keyboard key | | `browser_vision` | Screenshot + AI analysis; use `annotate=true` for element labels | | `browser_console` | Get JS console output and errors |

### Fallback: Headless QA via Playwright (When Browser Tools Fail)

When `browser_navigate` fails (e.g., Camofox/CdpServer not running) or `browser_vision`/`vision_analyze` returns 429 (model plan limitation), you can still do thorough QA using **Playwright directly** via the Hermes venv. Playwright is already installed for browser tooling, so this works with zero setup.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/dogfood/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
