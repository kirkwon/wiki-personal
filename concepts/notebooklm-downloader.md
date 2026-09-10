---
date: 2026-07-19
type: concept
title: Notebooklm Downloader
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- mlops
sources:
- hermes://skill/notebooklm-downloader
description: Download NotebookLM artifacts (infographics, videos, mind maps, etc.)
  using Playwright automation.
---

# Notebooklm Downloader

> Download NotebookLM artifacts (infographics, videos, mind maps, etc.) using Playwright automation.

## Overview

- **Prerequisites** — 1. **Node.js** (v16+ recommended) 2. **Playwright** installed globally or locally in the project 3. **Google Chrome/Chromium** (Playwright will install browsers if needed) 4. **NotebookLM CLI** (`nlm`) installed and authenticated (see `notebooklm-cli` skill for details)
- **Installation** — The skill is installed automatically via Hermes. To use it, ensure you have the prerequisites met.
- **Workflow** — The skill provides a script (`scripts/download_artifacts.js`) that automates downloading completed Studio artifacts from a NotebookLM notebook. Note: this only downloads artifacts that were **successfully generated** (check via `nlm studio status --json` first — see the Diagnostics section in `notebooklm-research-pipeline` skill).

## Further detail

### Configuration

The script `scripts/download_artifacts.js` accepts the following command-line arguments:

### Notes

- **Authentication**: The script attempts to reuse an existing login session. If not logged in, it will prompt for manual login in the browser window. - **Artifact Types**: Not all artifact types may be available depending on what was generated via the CLI. - **Headless Mode**: Set `--headless false` to see the browser window for debugging. - **Dependencies**: The script requires Playwright. If you encounter issues, run `npx playwright install` to ensure browsers are available.

### Pitfalls

- **Authentication in headless mode**: When running with `--headless true`, the script may not be able to authenticate properly if there's no existing valid session. The browser may close prematurely with a "Target page, context or browser has been closed" error. **Solution**: Run with `--headless false` first to authenticate manually in the visible browser, then retry with headless mode once you have a valid session. - **Browser timeout**: The script uses a default timeout of 300 seconds (5 minutes) for artifact generation. Video generation can take 3-5 minutes. If artifacts aren't generated

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mlops/notebooklm-downloader/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
