---
type: concept
title: Hermes S6 Container Supervision
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Hermes S6 Container Supervision

> Modify, debug, or extend the s6-overlay supervision tree inside the Hermes Agent Docker image — adding new services, debugging profile gateways, understanding the Architecture B main-program pattern.

## Overview

- **When to use this skill** — Load this skill when you're working on: - Adding or removing a static service in the Hermes Docker image (something that should be supervised at every container start, like the dashboard) - Diagnosing why a per-profile gateway isn't starting, restarting, or surviving `docker restart` - Understanding why the container's CMD is `/opt/hermes/docker/main-wrapper.sh` and how leading-dash args reach the user's program - Modifying `cont-init.d` boot scripts (UID remap, volume seeding, profile reconciliation) - Changing the rendered run-script for per-profile gateways (Phase 4)
- **Key files** — | Path | Role | |---|---| | `Dockerfile` | s6-overlay install + cont-init.d wiring + `ENTRYPOINT ["/init", "/opt/hermes/docker/main-wrapper.sh"]` | | `docker/stage2-hook.sh` | The "old entrypoint logic" — UID remap, chown, seed, skills sync. Runs as cont-init.d/01-hermes-setup. | | `docker/cont-init.d/02-reconcile-profiles` | Calls `hermes_cli.container_boot` on every boot to restore profile gateway slots from the persistent volume. | | `docker/main-wrapper.sh` | The container's CMD. Routes user args, drops to hermes via `s6-setuidgid`, exec's the chosen program. | | `docker/s6-rc.d/main-herme
- **Why Architecture B (CMD as main program, not s6-supervised)** — The original plan (v1–v3) called for main hermes to run as a supervised s6-rc service. Two real s6-overlay v3 mechanics blocked that:

## Further detail

### Related skills

- `hermes-agent-dev`: General hermes-agent codebase navigation - `hermes-tool-quirks`: Specific Hermes-tool workarounds (sed/grep/etc.) — load when debugging the s6 stack's interaction with hermes built-in tools.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/software-development/hermes-s6-container-supervision/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[hermes-agent-stack]]
