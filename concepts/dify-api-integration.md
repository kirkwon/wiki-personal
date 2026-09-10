---
date: 2026-08-02
type: concept
title: Dify Api Integration
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- mlops
sources:
- hermes://skill/dify-api-integration
description: Integrate with Dify API for dataset file uploads.
---

# Dify Api Integration

> Integrate with Dify API for dataset file uploads.

## Overview

- **Authentication Pattern** — Dify's console API uses a two-token authentication scheme:
- **Endpoint Discovery** — When documentation doesn't match the running instance:
- **Verification Steps** — After uploading, verify the document appears in the dataset:

## Further detail

### Related Skills

- `api-integration` - General REST API patterns - `docker-management` - For managing Dify Docker containers - `web-search` - For finding Dify API documentation - `execute_code` - For testing API interactions

### Notes

- Dify's API can vary between versions and installation methods (Docker-compose vs manual). - Always verify endpoints against your specific instance's running code. - When in doubt, inspect the actual running container's source code for route definitions.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/development/dify-api-integration/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
