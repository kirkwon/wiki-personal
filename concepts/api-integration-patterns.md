---
date: 2026-08-02
type: concept
title: Api Integration Patterns
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- software-development
sources:
- hermes://skill/api-integration-patterns
description: Patterns for APIs with separate authentication systems.
---

# Api Integration Patterns

> Patterns for APIs with separate authentication systems.

## Overview

- **Overview** — This skill captures patterns for working with HTTP APIs that use different authentication mechanisms for different endpoints (e.g., cookie-based auth for UI, token-based for service APIs).
- **Dify-Specific Pattern** — Discovered during testing: Dify uses dual-API architecture:
- **Anti-Patterns to Avoid** — - ❌ Assuming all endpoints use the same authentication - ❌ Reusing UI auth headers on service APIs - ❌ Repeating same request variation after clear failure - ❌ Speculating without evidence ("maybe try this header") - ❌ Ignoring status codes, parsing error responses as success - ❌ Overlooking versioning in base paths - ❌ Forgetting file uploads require multipart/form-data (not JSON)

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/api-integration/api-integration-patterns/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[dify-api-integration]]
