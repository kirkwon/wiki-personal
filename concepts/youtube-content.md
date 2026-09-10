---
date: 2026-07-19
type: concept
title: Youtube Content
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- media
sources:
- hermes://skill/youtube-content
description: YouTube transcripts to summaries, threads, blogs.
---

# Youtube Content

> YouTube transcripts to summaries, threads, blogs.

## Overview

- **Golden Rule (Never Break)** — **ALWAYS extract real transcripts. NEVER generate plausible-sounding fake summaries from metadata.**
- **When to use** — Use when the user shares a YouTube URL or video link, asks to summarize a video, requests a transcript, wants to extract and reformat content from any YouTube video, or wants to ingest video knowledge into their knowledge base. Transforms transcripts into structured content (chapters, summaries, threads, blog posts, skills, knowledge base entries).
- **Parsing yt-dlp JSON3 Transcripts** — The json3 format is YouTube's native transcript format. Parse it with:

## Further detail

### Helper Script (youtube-transcript-api path)

`SKILL_DIR` is the directory containing this SKILL.md file. For the fallback method:

### Output Formats

After fetching the transcript, format it based on what the user asks for:

### Workflow

1. **Extract** the transcript using yt-dlp (preferred) or youtube-transcript-api. 2. **Validate**: confirm output is non-empty. If empty, check available languages with `--list-subs`. If still empty, tell the user the video likely has transcripts disabled. 3. **Parse**: strip empty events from json3, get clean text. 5. **Extract tools and resources**: Match against a known-tools dictionary (GitHub, Netlify, OpenAI, etc.) plus URL extraction. Filter out auto-caption artifacts (mangled proper nouns).

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/media/youtube-content/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
