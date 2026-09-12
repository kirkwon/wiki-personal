------

# Hermes Cron Management

> Manage, troubleshoot, and optimize Hermes Agent cron jobs. Covers listing, creating, updating, and debugging scheduled tasks including agent-driven and no_agent script-based jobs.

## Overview

- **Overview** — Hermes cron jobs are scheduled tasks that run automatically at specified intervals. Jobs can be: - **Agent-driven**: Execute skills or prompt-based workflows (deliver via telegram, origin, or local) - **No-agent scripts**: Execute shell scripts directly (no_agent=true, must be in ~/.hermes/scripts/)
- **The Notification Gap: No Built-In `notify_on_failure`** — **Critical architectural fact:** Hermes cron has **no built-in failure notification**. The `deliver` field only pushes *stdout* — it does not mean "notify me when this fails." When a job dies hard (exit 1, timeout, crash, provider error), here is what actually happens:
- **Cron Schedule Examples** — | Schedule | Description | |----------|-------------| | `0 9 * * *` | Daily at 9:00 AM | | `0 */6 * * *` | Every 6 hours | | `0 3 * * 0` | Weekly on Sunday at 3:00 AM | | `0 0 * * 1` | Weekly on Monday at midnight | | `every 180m` | Every 3 hours (Hermes-specific) | | `0 21 * * 0` | Weekly on Sunday at 9:00 PM |

## Further detail

### Verification Steps

After creating or updating a cron job:

### Related Skills

- **hermes-agent**: Complete Hermes Agent configuration and CLI usage - **gbrain**: GBrain CLI installation, configuration, and operation - **hermes-skill-development-workflow**: Creating, testing, and installing Hermes skills - **cron-orchestrator**: Monthly audit, quarterly tune, and agent-to-deterministic migration for cron jobs - **kanban-orchestrator**: Task decomposition and multi-agent routing (complementary pattern)

### Hermes Code Sync

Collect and back up Hermes-produced code into a version-controlled GitHub repository. Full workflow moved to **references/hermes-code-sync.md** (2026-09-05 size trim).

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/devops/hermes-cron-management/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[hermes-agent-stack]]
