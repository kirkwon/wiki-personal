---
date: 2026-07-19
type: concept
title: Find Skills
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- skills
- discovery
- skills.sh
- ecosystem
- vercel
- autonomous-ai-agents
sources:
- hermes://skill/find-skills
description: Discover and install agent skills from skills.sh (Vercel's open agent
  skills ecosystem). Use when user asks how to do X, wants to extend capabilities,
  or a task might benefit from an existing skill. Bridges the skills.sh directory
  with Hermes native skills.
---

# Find Skills

> Discover and install agent skills from skills.sh (Vercel's open agent skills ecosystem). Use when user asks how to do X, wants to extend capabilities, or a task might benefit from an existing skill. Bridges the skills.sh directory with Hermes native skills.

## Overview

- **When to Use** — - User asks "how do I do X" where X might be a common task with an existing skill - User says "find a skill for X" or "is there a skill that can..." - A task would benefit from specialized procedural knowledge you don't have - User wants to extend agent capabilities - You realize a recurring task pattern should be codified
- **Two Skill Ecosystems** — This skill bridges two ecosystems:
- **Porting from External Sources to Hermes Native** — When an external skill (from anthropics/skills, skills.sh, or a standalone repo) is worth porting to Hermes format, follow this workflow:

## Further detail

### When No Skill Exists

1. Acknowledge no match found 2. Offer to help directly 3. Suggest creating a custom skill: `skill_manage(action='create')` or `npx skills init my-skill`

### Common Search Categories

| Category | Example Queries | |---|---| | Web Development | react, nextjs, typescript, css, tailwind | | Testing | testing, jest, playwright, e2e | | DevOps | deploy, docker, kubernetes, ci-cd | | Documentation | docs, readme, changelog, api-docs | | Code Quality | review, lint, refactor, best-practices | | Design | ui, ux, design-system, accessibility | | Agent Workflows | planning, debugging, subagents, autonomous |

### Pitfalls

- **Don't blindly install.** Always check install count, source reputation, and audit status. - **skills.sh API requires Vercel OIDC auth.** For programmatic access without Vercel, scrape the leaderboard HTML or use `npx skills find`. - **Format mismatch.** skills.sh skills are plain SKILL.md; Hermes needs frontmatter with `metadata.hermes`. Port, don't symlink. - **Hermes is not in their agent list.** skills.sh supports editor agents (Claude Code, Cursor, etc.). Hermes skills are consumed differently — through `skill_view` at runtime.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/find-skills/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[fix-skills-list-backoff]]
