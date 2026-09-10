---
date: 2026-07-19
type: concept
title: Youtube Video Ingestion
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- youtube
- video
- ingestion
- knowledge
- pipeline
- watch-later
- transcript
- openrouter
- research
sources:
- hermes://skill/youtube-video-ingestion
description: End-to-end pipeline for ingesting YouTube Watch Later videos into structured
  knowledge. Extracts transcripts via yt-dlp, generates structured summaries via OpenRouter
  API (owl-alpha), and imports into gbrain.
---

# Youtube Video Ingestion

> End-to-end pipeline for ingesting YouTube Watch Later videos into structured knowledge. Extracts transcripts via yt-dlp, generates structured summaries via OpenRouter API (owl-alpha), and imports into gbrain.

## Overview

- **Golden Rule (Critical — Read Before Processing)** — **ALWAYS extract real transcripts. NEVER generate plausible-sounding content from metadata alone.**
- **When This Skill Activates** — Use this skill when the user: - Wants to process their YouTube Watch Later playlist - Mentions video summaries, video knowledge base, or video skills - Asks about extracting YouTube transcripts or descriptions - Wants video-to-gbrain import - References the unified_videos_improved format - Wants batch transcript extraction with yt-dlp + local LLM enrichment
- **Prompt Optimization (AutoResearch)** — The YouTube pipeline's summarization prompt can be optimized using the `autoresearch` skill:

## Further detail

### Key Commands

| Purpose | Command | |---------|---------| | Process single video | `python3 scripts/regenerate-from-transcript.py -- <video_id>` | | Batch all videos | `python3 scripts/regenerate-from-transcript.py --all --parallel 4` | | Batch by category | `python3 scripts/regenerate-from-transcript.py --category ai --parallel 4` | | Batch first N | `python3 scripts/regenerate-from-transcript.py --batch 20` | | Dry run | `python3 scripts/regenerate-from-transcript.py --batch 5 --dry-run` | | Validate titles | `python3 scripts/validate_titles.py --limit 50` | | Import to gbrain | `bash scripts/import-to-gb

### Real Content vs Template Content

| Aspect | `*_real.md` (transcript-based) | `*_improved.md` (template) | |--------|-------------------------------|---------------------------| | extraction_source | `yt-dlp_transcript` | `unknown` or `intelligent_analysis` | | has_real_content | `True` | `False` | | Topic headings | "Matte Surfaces & Light Absorption" | "Introduction to Claude Code Make" | | Skills | "Analyze Material Quality" with 4-step loop | "Active Video Learning" with generic loop | | Size | 7K-9K chars | 3K-5K chars | | Value | High — real content | Low — plausible-sounding filler |

### Verification

After processing, verify: - [ ] `ls *_real.md | wc -l` matches expected count - [ ] **Transcript-to-metadata validation**: Run spot-checks on 8+ videos across categories confirming transcript content matches video title (see `references/transcript-validation.md`) - [ ] Sample check: open one `*_real.md`, confirm topic headings are concise (3-7 words), not raw sentences - [ ] Skills have real trigger/purpose/loop/tools, not "Active Video Learning" template - [ ] Transcript excerpt appears in the file body - [ ] Ollama logs confirm phi3 generated both topics and skills (check stderr for "Ollama

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/research/youtube-video-ingestion/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
