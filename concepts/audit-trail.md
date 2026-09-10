---
date: 2026-07-19
type: concept
title: Audit Trail
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- core
sources:
- hermes://skill/audit-trail
description: Track execution costs, durations, and session persistence for audit and
  optimization.
---

# Audit Trail

> Track execution costs, durations, and session persistence for audit and optimization.

## Overview

- **When to Use** — - Monitoring resource consumption of agent workflows - Tracking execution times for performance optimization - Maintaining audit trails for compliance or review - Evaluating session persistence strategies for memory systems - Analyzing cost-effectiveness of different approaches
- **Prerequisites** — - Hermes Agent installed and configured - Access to timing and resource measurement capabilities - Write access to logs/ or audit/ directory for storing audit data
- **How to Run** — Invoke through the `skill_manage` tool with action="create" to initialize the skill, then follow the Procedure section using Hermes tools like `write_file`, `read_file`, `execute_code`, and `terminal`.

## Further detail

### Quick Reference

- `write_file`: Create audit log entries - `execute_code`: Run timing and measurement scripts - `terminal`: Execute timing commands - `read_file`: Review audit logs

### Procedure

1. **Set up audit logging** - Determine what metrics to track (time, cost, tokens, etc.) - Create appropriate logging structure in logs/ or audit/ directory - Establish consistent format for audit entries

### Pitfalls

- **Overhead from measurement**: Ensure measurement itself doesn't significantly impact performance - **Incomplete tracking**: Missing key cost factors leads to inaccurate assessments - **Inconsistent formatting**: Makes analysis difficult - **Privacy concerns**: Be careful with logging sensitive information - **Storage growth**: Audit logs can grow large; consider rotation or summarization

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/core/audit-trail/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
