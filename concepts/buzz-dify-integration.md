---
date: 2026-08-02
type: concept
title: Buzz Dify Integration
created: 2026-08-02
updated: '2026-09-09'
tags:
- skill
- mlops
sources:
- hermes://skill/buzz-dify-integration
description: Deploy Buzz relay and connect Hermes to Dify-MCP.
---

# Buzz Dify Integration

> Deploy Buzz relay and connect Hermes to Dify-MCP.

## Overview

- **Prerequisites** — - Docker Engine ≥ 24.0 and Docker Compose v2 installed. - Hermes Agent installed and available on PATH. - A Dify workspace (self‑hosted or SaaS) with the **MCP Server** plugin installed. - Basic familiarity with the terminal and editing files.
- **Verification Checklist** — After completing the above steps, verify:
- **Troubleshooting** — | Symptom | Likely Cause | Fix | |---------|--------------|-----| | `docker compose up` fails with “role \"buzz\" does not exist” | The Postgres container hasn’t finished initializing or the `.env` variables don’t match the database creation expectations. | Check `docker compose logs postgres`; ensure `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` are set correctly. You may need to manually `CREATE USER` and `CREATE DATABASE` inside the Postgres container if the image doesn’t auto‑create them. | | Buzz HTTP endpoint returns `000` / connection refused | The `relay` container is not yet hea

## Further detail

### Extending the Integration

- **Multiple Dify apps**: Add additional entries under `tools.mcp` with distinct names (e.g., `dify_codegen`, `dify_test`) and point them at different Dify MCP endpoints. - **Multiple Buzz relays**: Run additional Docker Compose stacks on different ports, configure multiple gateway entries, or run a relay cluster. - **Production deployment**: For a production‑grade Buzz relay, consider enabling TLS via Caddy (see `compose.caddy.yml`), setting `BUZZ_REQUIRE_AUTH_TOKEN=true`, and managing persistent volumes with backups of Postgres and MinIO data.

### Related Skills

- `deployment` – generic cron‑job and script deployment patterns (useful for scheduling regular Buzz health checks or Dify data syncs). - `hermes-tool-integration` – pattern for adding and configuring MCP tools in Hermes. - `agent-folder-structure` – apply to the Buzz source tree to keep navigation fast for the agent.

### Source

Compiled from hands‑on experience deploying Buzz (v0.28‑ish) and integrating with Dify MCP, plus Hermes gateway and tool‑configuration docs.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/buzz-dify-integration/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
