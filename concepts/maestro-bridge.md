---
date: 2026-07-19
type: concept
title: Maestro Bridge
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- mcp
sources:
- hermes://skill/maestro-bridge
description: Bridge to Maestro's MCP server enabling invocation of Maestro's 25 workflow
  commands through Hermes' delegation system.
---

# Maestro Bridge

> Bridge to Maestro's MCP server enabling invocation of Maestro's 25 workflow commands through Hermes' delegation system.

## Overview

- **Overview** — Maestro provides a comprehensive AI agent workflow system with: - 25 workflow commands organized into Analysis, Fix & Improve, Enhancement, and Utility categories - Persistent memory layer (decision logs, audit trails, session history) - Context gathering protocol (.maestro/context.md or .maestro.md) - MCP server for integration with various AI coding agents
- **Implementation Approach** — The bridge operates by: 1. Starting Maestro's MCP server as a subprocess (stdio transport) 2. Mapping Hermes delegation requests to Maestro MCP tool calls 3. Relaying results back through Hermes' delegation system 4. Managing the MCP server lifecycle
- **Available Commands** — Through this bridge, Hermes can invoke all 25 Maestro commands:

## Further detail

### Usage

Delegate tasks to this skill using Hermes' delegation system:

### Troubleshooting

If you encounter issues with the Maestro MCP bridge:

### Configuration

The bridge assumes Maestro is available via npx. Ensure Node.js and the Maestro package are installed:

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mcp/maestro-bridge/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
