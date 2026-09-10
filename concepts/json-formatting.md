---
date: 2026-07-19
type: concept
title: Json Formatting
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/json-formatting
description: Format, validate, query, and transform JSON data. Use this skill whenever
  the user needs to pretty-print JSON, extract data from JSON, validate JSON structure,
  convert between JSON and other formats (CSV, YAML, TOML, markdown tables), filter
  JSON arrays, or fix malformed JSON. Covers Python (json module, json_parse from
  hermes_tools), jq, and common JSON tools. Trigger on phrases like "format this JSON",
  "parse this JSON", "convert JSON to CSV", "extract from JSON", "fix JSON", "validate
  JSON", "jq this", "JSON is malformed".
---

# Json Formatting

> Format, validate, query, and transform JSON data. Use this skill whenever the user needs to pretty-print JSON, extract data from JSON, validate JSON structure, convert between JSON and other formats (CSV, YAML, TOML, markdown tables), filter JSON arrays, or fix malformed JSON. Covers Python (json module, json_parse from hermes_tools), jq, and common JSON tools. Trigger on phrases like "format this JSON", "parse this JSON", "convert JSON to CSV", "extract from JSON", "fix JSON", "validate JSON", "jq this", "JSON is malformed".

## Overview

- **Tools Available** — | Tool | Purpose | |------|---------| | `terminal` | Run jq, python3, curl for JSON work | | `execute_code` | Available via `from hermes_tools import json_parse` for embedded JSON parsing with control-char tolerance |
- **Error Handling Checklist** — When processing JSON:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/json-formatting/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
