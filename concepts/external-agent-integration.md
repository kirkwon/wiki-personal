---
date: 2026-08-02
type: concept
title: External Agent Integration
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- integration
- external-tools
- agent-reach
- opencli
- skill-creator
- setup
- browser-bridge
- software-development
sources:
- hermes://skill/external-agent-integration
description: Install and bridge external agent tools into Hermes.
---

# External Agent Integration

> Install and bridge external agent tools into Hermes.

## Overview

- **When to Use** — - User shares a link to an agent tool/skill on GitHub, X/Twitter, or skills.sh - User asks to "wire up", "install", or "set up" an external agent capability - User asks whether a browser login (Safari/Chrome) helps a tool work - User wants to add platform access (Reddit, Twitter, LinkedIn) to the agent - User discovers a new CLI tool or skill factory and wants it integrated
- **The Integration Pattern** — Every external agent tool follows this lifecycle:
- **Known Tool Integrations** — See `references/known-integrations.md` for setup details of tools already wired into this environment. See `references/drawio-skill-notes.md` for the drawio-skill integration specifics (install pattern, verified capabilities, Hermes-specific notes, export pitfall). See `references/aider-bridge-setup.md` for the aider CLI bridge setup, including the Python 3.12 pyexpat crash fix, env-sourcing pattern, and headless invocation flags.

## Further detail

### Pitfalls

- **Safari logins don't transfer.** Agent tools read Chrome cookies, not Safari. If user says "I logged in", verify WHICH browser. - **Chrome extension install is manual.** No automated tool can install Chrome extensions. Always provide the exact Web Store URL and verify after. - **External skill frontmatter may break Hermes.** Date objects, unconventional fields can cause `skill_view` failures. Always test-load after copying. - **`agent-reach doctor` status may lag.** Channels can work via OpenCLI even when doctor reports `off`. Always test with a real query. - **Stage generated skills before

### Full-Subtree Skill Installs

Some upstream skills ship as a full directory tree, not a single SKILL.md:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/external-agent-integration/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
