---
date: 2026-07-19
type: concept
title: Read The Damn Docs
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- uncategorized
sources:
- hermes://skill/read-the-damn-docs
description: Use when implementing, integrating, upgrading, debugging, or answering
  anything involving third-party APIs, libraries, frameworks, CLIs, cloud services,
  model/provider SDKs, fast-moving product behavior, user requests for latest/current/official
  behavior, unfamiliar repo docs/specs, errors that may indicate API drift, or high-stakes
  auth, security, billing, data, migration, deployment, compliance, or privacy behavior.
  Forces Codex to web-search for current official docs and read primary docs before
  assuming from memory.
---

# Read The Damn Docs

> Use when implementing, integrating, upgrading, debugging, or answering anything involving third-party APIs, libraries, frameworks, CLIs, cloud services, model/provider SDKs, fast-moving product behavior, user requests for latest/current/official behavior, unfamiliar repo docs/specs, errors that may indicate API drift, or high-stakes auth, security, billing, data, migration, deployment, compliance, or privacy behavior. Forces Codex to web-search for current official docs and read primary docs before assuming from memory.

## Overview

- **Docs-First Triggers** — Read docs before proceeding when any of these are true:
- **What Counts As Docs** — Use the most authoritative source available:
- **Required Workflow** — 1. Identify the exact surface: package name, installed version, target version, provider endpoint, CLI command, config file, local helper, schema, or product feature. 2. Search the web for the current official docs unless the relevant docs are already local or the user supplied a URL. Use targeted searches such as `<product> <feature> official docs`, `<package> migration guide`, or `<provider> API reference`. 3. Open and read the docs closest to that surface. Prefer local docs first for internal code, then official upstream docs. For new packages, verify the latest version before writing impor

## Further detail

### Examples That Must Trigger Docs

- "Add Tailwind to this app." Check the current Tailwind major and its install docs from the web before creating config files or assuming old PostCSS setup. - "Use the AI SDK to stream responses." Verify the current AI SDK major, imports, provider package names, streaming helpers, and server/runtime examples from official docs. - "Wire up Stripe webhooks." Read Stripe's current signature verification, event retry, endpoint secret, and framework body-parsing docs before coding. - "Fix this Next.js caching bug." Read the docs for the installed Next.js major and router mode before assuming cache

### When A Quick Local Read Is Enough

Do not browse the web for every tiny edit. A docs pass can be local and brief when the answer is already in the repo: existing helper usage, nearby tests, typed interfaces, generated clients, ADRs, or package READMEs. But if the task depends on an external tool, package, provider, or current product behavior, web search is usually the right first step. For trivial language syntax, typo fixes, formatting, or self-contained code with no external contract, proceed normally.

### If Docs Are Unavailable

If network access, auth, or missing local files prevents reading the docs, say that plainly before relying on memory. Narrow the uncertainty, inspect source or types if available, and avoid presenting the result as confirmed-current.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/read-the-damn-docs/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
