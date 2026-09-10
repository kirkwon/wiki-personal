---
date: 2026-07-19
type: concept
title: Gif Search
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- GIF
- Media
- Search
- Tenor
- API
- media
sources:
- hermes://skill/gif-search
description: Search/download GIFs from Tenor via curl + jq.
---

# Gif Search

> Search/download GIFs from Tenor via curl + jq.

## Overview

- **When to use** — Useful for finding reaction GIFs, creating visual content, and sending GIFs in chat.
- **Setup** — Set your Tenor API key in your environment (add to `${HERMES_HOME:-~/.hermes}/.env`):
- **Prerequisites** — - `curl` and `jq` (both standard on macOS/Linux) - `TENOR_API_KEY` environment variable

## Further detail

### API Parameters

| Parameter | Description | |-----------|-------------| | `q` | Search query (URL-encode spaces as `+`) | | `limit` | Max results (1-50, default 20) | | `key` | API key (from `$TENOR_API_KEY` env var) | | `media_filter` | Filter formats: `gif`, `tinygif`, `mp4`, `tinymp4`, `webm` | | `contentfilter` | Safety: `off`, `low`, `medium`, `high` | | `locale` | Language: `en_US`, `es`, `fr`, etc. |

### Available Media Formats

Each result has multiple formats under `.media_formats`:

### Notes

- URL-encode the query: spaces as `+`, special chars as `%XX` - For sending in chat, `tinygif` URLs are lighter weight - GIF URLs can be used directly in markdown: `![alt](url)`

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/.archive/gif-search/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
