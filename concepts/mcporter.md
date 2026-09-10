---
date: 2026-07-19
type: concept
title: Mcporter
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- MCP
- Tools
- API
- Integrations
- Interop
- mcp
sources:
- hermes://skill/mcporter
description: Use the mcporter CLI to list, configure, auth, and call MCP servers/tools
  directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation.
---

# Mcporter

> Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation.

## Overview

- **Prerequisites** — Requires Node.js:
- **Discovering MCP Servers** — > **Pitfall:** mcpfinder.dev and mcp.so often return 400 errors. Use the GitHub/npm APIs directly instead.
- **Auth and Config** — Config file location: `./config/mcporter.json` (override with `--config`).

## Further detail

### Daemon

For persistent server connections:

### Notes

- Use `--output json` for structured output that's easier to parse - Ad-hoc servers (HTTP URL or `--stdio` command) work without any config — useful for one-off calls - OAuth auth may require interactive browser flow — use `terminal(command="mcporter auth <server>", pty=true)` if needed - When `web_search`/`web_extract`/`browser_navigate` all fail (Firecrawl 400 errors are common), fall back to `execute_code` with direct API calls — GitHub API and npm registry both work without auth and are fast

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mcp/mcporter/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
