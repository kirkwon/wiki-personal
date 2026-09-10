---
date: 2026-07-19
type: concept
title: Nano Pdf
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- PDF
- Documents
- Editing
- NLP
- Productivity
- productivity
sources:
- hermes://skill/nano-pdf
description: Edit text in existing PDFs via natural-language prompts.
---

# Nano Pdf

> Edit text in existing PDFs via natural-language prompts.

## Overview

- **Notes** — - Page numbers may be 0-based or 1-based depending on version — if the edit hits the wrong page, retry with ±1 - Always verify the output PDF after editing (use `read_file` to check file size, or open it) - The tool uses an LLM under the hood — requires an API key (check `nano-pdf --help` for config) - Works well for text changes; complex layout modifications may need a different approach

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/nano-pdf/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
