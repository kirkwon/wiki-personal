---
date: 2026-08-02
type: concept
title: Fix Skills List Backoff
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/fix-skills-list-backoff
description: Add exponential backoff to skills_list tool.
---

# Fix Skills List Backoff

> Add exponential backoff to skills_list tool.

## Overview

- **Problem** — The skills_list tool in ~/.hermes/hermes-agent/tools/skills_tool.py was failing repeatedly due to rate limiting when making frequent calls to list available skills, causing the dojo evaluation to flag it as needing a "add_backoff" fix.
- **Solution** — Apply exponential backoff with jitter to the skills_list function to make it resilient to temporary rate limits and service disruptions.
- **Modified Function** — Here's how to modify the skills_list function in /Users/kirkwon/.hermes/hermes-agent/tools/skills_tool.py:

## Further detail

### Key Changes Made

1. **Added imports**: `time` and `random` for the backoff logic 2. **Wrapped the main logic in a retry loop**: With configurable max_retries (3) and base_delay (1.0 seconds) 3. **Added exponential backoff**: Delay increases as `base_delay * (2 ** attempt)` 4. **Added jitter**: Multiplies delay by a random factor between 0.5 and 1.0 to prevent thundering herd 5. **Enhanced error handling**: Distinguishes between transient errors (worth retrying) and permanent errors (fail fast) 6. **Added logging**: Warns when retries occur for debugging and monitoring 7. **Preserved original functionality**: A

### Why This Fixes the Issue

- **Rate Limit Handling**: When the skills tool is called too frequently and hits rate limits (HTTP 429), it will automatically retry with increasing delays - **Network Resilience**: Handles temporary network issues, timeouts, and service unavailability (5xx errors) - **Thundering Herd Prevention**: The jitter component prevents multiple instances from retrying in perfect sync - **Fast Failure for Permanent Errors**: Authentication errors, invalid requests, etc. are not retried unnecessarily - **Logging**: Provides visibility into when retries are happening for operational awareness

### Testing the Fix

To verify this fix works correctly:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/fix-skills-list-backoff/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
