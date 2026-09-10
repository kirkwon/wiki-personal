---
date: 2026-07-19
type: concept
title: Hermes Web Tools
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- web
- troubleshooting
- backends
- ddgs
- firecrawl
- search
- extract
- autonomous-ai-agents
sources:
- hermes://skill/hermes-web-tools
description: 'Configure and troubleshoot Hermes web tools (web_search, web_extract,
  browser).

  Understand backend resolution chains, diagnose silent fallback errors, and

  install/configure search and extraction backends correctly. Use this skill

  whenever web_search or web_extract returns unexpected errors, when a

  configured backend appears to be ignored, when error messages name a

  different backend than what config specifies, or when you need to understand

  which backend Hermes will actually use at runtime.'
---

# Hermes Web Tools

> Configure and troubleshoot Hermes web tools (web_search, web_extract, browser).
Understand backend resolution chains, diagnose silent fallback errors, and
install/configure search and extraction backends correctly. Use this skill
whenever web_search or web_extract returns unexpected errors, when a
configured backend appears to be ignored, when error messages name a
different backend than what config specifies, or when you need to understand
which backend Hermes will actually use at runtime.

## Overview

- **When to Use** — - `web_search` returns an error naming a backend you didn't configure - `web_extract` fails or returns empty content - A `web.search_backend` or `web.extract_backend` setting appears to be ignored - You need to determine which backend Hermes will actually use at runtime - You're setting up web tools for the first time on a new profile/install
- **How Backend Resolution Works** — The source of truth is `tools/web_tools.py` in the Hermes source tree (`~/.hermes/hermes-agent/tools/web_tools.py`). The resolution chain:
- **The Silent Fallback Bug Pattern** — **Symptom:** Config says `web.search_backend: ddgs`, but web_search returns `"Firecrawl search failed: Payment Required: Insufficient credits"`.

## Further detail

### Profile Config Gotcha

Each Hermes profile has its own `config.yaml` at `~/.hermes/profiles/<name>/config.yaml`. The profile config **merges with** (not replaces) the main `~/.hermes/config.yaml`. When debugging web tool issues, check both:

### Reference Files

- `references/backend-resolution-guide.md` — Detailed function-by-function walkthrough of `web_tools.py` resolution chain with the specific debugging transcript from the session that discovered the ddgs/Firecrawl fallback bug. + - Note: Some sites (e.g., Reddit) employ advanced bot detection that may block both crawlers and browser tools; in such cases, rely on search APIs (e.g., web_search with site:) for metadata or look for public JSON endpoints. + - When a Python module is missing in the execute_code sandbox (e.g., crawl4ai), use terminal() to run a Python script with the project venv's py

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/hermes-web-tools/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
