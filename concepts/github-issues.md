---
type: concept
title: Github Issues
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Github Issues

> Create, triage, label, assign GitHub issues via gh or REST.

## Overview

- **Prerequisites** — - Authenticated with GitHub (see `github-auth` skill) - Inside a git repo with a GitHub remote, or specify the repo explicitly
- **1. Viewing Issues** — **With gh:**
- **2. Creating Issues** — **With gh:**

## Further detail

### Steps to Reproduce

1. Navigate to /settings while logged out 2. Get redirected to /login?next=/settings 3. Log in 4. Actual: redirected to /dashboard (should go to /settings)

### Expected Behavior

Respect the ?next= query parameter." \ --label "bug,backend" \ --assignee "username"

### Bug Description

<What's happening>

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/github/github-issues/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[github-pr-workflow]]
