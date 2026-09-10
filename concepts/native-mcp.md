---
date: 2026-07-19
type: concept
title: Native Mcp
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- MCP
- Tools
- Integrations
- mcp
sources:
- hermes://skill/native-mcp
description: 'MCP client: connect servers, register tools (stdio/HTTP).'
---

# Native Mcp

> MCP client: connect servers, register tools (stdio/HTTP).

## Overview

- **When to Use** — Use this whenever you want to: - Connect to MCP servers and use their tools from within Hermes Agent - Add external capabilities (filesystem access, GitHub, databases, APIs) via MCP - Run local stdio-based MCP servers (npx, uvx, or any command) - Connect to remote HTTP/StreamableHTTP MCP servers - Have MCP tools auto-discovered and available in every conversation
- **Prerequisites** — - **mcp Python package** -- optional dependency; install with `pip install mcp`. If not installed, MCP support is silently disabled. - **Node.js** -- required for `npx`-based MCP servers (most community servers) - **uv** -- required for `uvx`-based MCP servers (Python-based servers)
- **Quick Start** — Add MCP servers to `~/.hermes/config.yaml` under the `mcp_servers` key:

## Further detail

### Configuration Reference

Each entry under `mcp_servers` is a server name mapped to its config. There are two transport types: **stdio** (command-based) and **HTTP** (url-based).

### Servers With Heavy Dependencies (OpenBB, etc.)

Some MCP servers wrap a large platform that has its own dependency tree. The MCP server package alone is just a thin wrapper — it connects fine and reports "tools discovered" but exposes zero domain-specific tools because the underlying platform extensions aren't installed.

### Sampling (Server-Initiated LLM Requests)

Hermes supports MCP's `sampling/createMessage` capability — MCP servers can request LLM completions through the agent during tool execution. This enables agent-in-the-loop workflows (data analysis, content generation, decision-making).

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mcp/native-mcp/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
