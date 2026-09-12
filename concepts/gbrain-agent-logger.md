------

# Gbrain Agent Logger

> Triggers at the end of a session or when completing major tasks. Writes a structured markdown log to clawd/26.Agent-Logs-GBrain/ to share memory with other agents via gbrain.

## Overview

- **Triggering Condition** — Trigger this skill whenever: 1. You have completed a major task or project. 2. The user asks you to "log your work". 3. You hit a major blocker that you cannot resolve and are handing the session back to the user or another agent.
- **Log Destination** — Write your log file to the following directory: `/Users/kirkwon/clawd/26.Agent-Logs-GBrain/logs/`
- **Schema Rules** — You MUST format your log exactly as follows, using Markdown and YAML frontmatter. Do not deviate from these headers.

## Further detail

### Ingestion (Automatic)

You do NOT need to trigger ingestion. A Hermes cron job (`agent-logs-gbrain-sync`, every 30 min) runs `gbrain sync --source agent-logs` which picks up any new log file in this directory. Your log will be searchable via `gbrain query` within 30 minutes of writing it.

### Execution Steps

1. Create the markdown content conforming to the schema above. 2. Use your file writing tools to save it to `/Users/kirkwon/clawd/26.Agent-Logs-GBrain/logs/`. 3. If the user permits, commit the new log file to the `26.Agent-Logs-GBrain` local repository. 4. Do NOT attempt to run `gbrain ingest` or `gbrain import` — sync is automatic.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/gbrain-agent-logger/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[hermes-agent-stack]]
