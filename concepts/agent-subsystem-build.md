---
type: concept
title: Agent Subsystem Build
created: 2026-08-21
frontmatter_added: 2026-09-13
---

# Agent Subsystem Build

> Build validated agent subsystems with GraphWork scaffolding.

## Overview

- **When to Use** — - "Build a new agent capability as a project" - "I want to close a gap from the diagram audit" - "Scaffold and implement X with full governance" - After identifying a missing subsystem in an audit/review - When the user wants eval-first, premortem-screened implementation
- **Prerequisites** — - GraphWork scaffolder: `~/clawd/32.GraphEngineeredWork/scripts/graph_scaffold.py` - OmniRoute running: `omniroute serve` (localhost:20128) — for benchmark/anchor steps - `delegate_task` available (for premortem + bias scan parallelization) - gbrain installed (optional — integration degrades gracefully if offline)
- **How to Run** — Invoke each phase through the `terminal` tool or `delegate_task`. The lifecycle is linear — each phase gates the next.

## Further detail

### Pitfalls

- **Skipping the premortem**: The #1 failure mode. A subsystem built without identifying its most likely failure is built blind. Always run premortem + bias scan before implementation. - **Same-model critic**: If the subsystem involves verification/critique, using the same model for execution and verification shares blind spots (premortem F1: "Self-Refine in a costume"). Route to a different model family. - **No offline fallback**: External services (OmniRoute, gbrain) go down. A subsystem that hard-crashes when a dependency is offline will erode trust. Always build a staging/fallback tier. -

### Verification

The anchor result is the single source of truth. If it shows <100% ground truth met, the subsystem needs more work regardless of how "done" the code looks.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/autonomous-ai-agents/agent-subsystem-build/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).

[[hermes-agent-stack]]
