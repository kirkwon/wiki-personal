---
date: 2026-07-19
type: concept
title: Conversation Logging Review
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- productivity
sources:
- hermes://skill/conversation-logging-review
description: Systematic conversation compression, logging, and weekly review process.
  Captures prompts, responses, decisions, artifacts, and tags for knowledge extraction
  and pattern recognition.
---

# Conversation Logging Review

> Systematic conversation compression, logging, and weekly review process. Captures prompts, responses, decisions, artifacts, and tags for knowledge extraction and pattern recognition.

## Overview

- **When to Use/Trigger** — - **Immediately after complex conversations** with decisions, insights, or artifacts - **Before starting weekly review** to prepare compressed logs - **When user asks for conversation history** or what was discussed - **When identifying patterns** across conversations (similar problems, recurring themes) - **When user wants to surface insights** from past conversations - **Automated via cron job** for weekly reviews (every Sunday evening)
- **Tools Used** — - **File Creation** (`write_file`): Create compressed conversation logs, review summaries, insight cards - **Directory Management**: Organize logs by date, category, and review status - **Python Scripts**: Parse conversation history, extract key elements, tag content - **Cron Jobs**: Schedule weekly reviews automatically - **Terminal Commands**: `ls`, `grep`, `find` for log searching and filtering
- **Compressed Log Format** — Each compressed conversation log follows this structure:

## Further detail

### Conversation Summary

**Topic:** Framework core meta books identification **Duration:** ~15 minutes **Context:** Building book knowledge system similar to YouTube knowledge graph

### Key Prompts

1. "Can you give me a list of the meta books and their authors?" 2. "I am referring to the 5 books you mentioned in the framework core" 3. "Yes. This should be systematic and I need a review process and way to surface it. Can we have a weekly review"

### Decisions Made

1. **Framework Core Confirmed:** 5 meta-books form foundation of book knowledge system 2. **Logging System Needed:** Systematic way to capture conversation insights 3. **Weekly Review Process:** Automated review to surface patterns and decisions 4. **Tagging Strategy:** Use tags for filtering and pattern recognition

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/productivity/conversation-logging-review/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
