---
type: concept
title: Self-Health Loop
created: 2026-07-15
updated: 2026-07-15
tags: [architecture, self-healing, monitoring, health, autonomous-systems]
---

# Self-Health Loop

## Summary

Self-Health Loop is a **meta-layer** within the Hermes agent architecture that continuously monitors system health, detects degradations, and initiates self-repair mechanisms without human intervention.

## Purpose

Self-Health Loop operates as an autonomous subsystem that:
- Monitors the health of all tool stacks and integrations
- Detects performance degradations and failures
- Initiates automatic or semi-automatic repairs
- Escalates critical issues to human attention

## Architecture

```
HEALTH CHECKS (AUTONOMOUS)
├── Tool Stack Health
│   ├── Browser availability (Camofox/Firecrawl)
│   ├── MCP server status (FRED/OpenBB)
│   ├── Model endpoint responsiveness
│   └── Cron job uptime verification
├── Memory Health
│   ├── Tier boundary appropriateness
│   ├── Memory entry usefulness scoring
│   ├── Stale memory detection
│   └── Memory promotion/demotion flow
├── Skill Health
│   ├── Skill usage frequency tracking
│   ├── Skill error rate monitoring
│   ├── Skill effectiveness measurement
│   └── Skill obsolescence detection
└── Knowledge Graph Health
    ├── Orphan page detection
    ├── Broken link identification
    ├── Concept connectivity scoring
    └── Source freshness monitoring
```

## Health Monitoring Framework

### Tier 1: Automatic Repairs
| Component | Check | Automatic Action |
|:----------| :--- | :--- |
| MCP Server | Heartbeat every 5 min | Reconnect with exponential backoff |
| Browser | Endpoint response test | Fallback to alternate backend |
| Memory Tiering | Usage pattern analysis | Promote/demote entries automatically |
| Cron Jobs | Exit status monitoring | Auto-restart on failure |

### Tier 2: Semi-Automatic Repairs
| Component | Check | Human Interaction Required |
|:----------| :--- | :--- |
| Skill Effectiveness | Error rate > 30% | Propose skill patch |
| Knowledge Freshness | Source > 30 days stale | Propose re-ingestion |
| Documentation Coverage | < 90% coverage | Generate new docs |
| Abstraction Debt | Score > threshold | Suggest simplification |

### Tier 3: Escalated Repairs
| Issue | Escalation Path |
|:------ | :--- |
| Model endpoint down | Telegram alert: "Model provider X unavailable" |
| Critical skill failure | Emergency patch procedure |
| Knowledge graph corruption | Human-mediated reset |
| Architecture misalignment | Design review session |

## Health Signals Dashboard

| Signal Category | Metric | Current | Target | Status |
|:----------------|:--------|:-------|:-------|:-------|
| Tool Stack | browser_stack | HEALTHY | HEALTHY | 🟢 |
| Tool Stack | mcp_servers | 2/3 online | 3/3 | 🟡 |
| Memory | hot_context_chars | 423 | <500 | 🟢 |
| Memory | memory_hit_rate | 67% | >80% | 🟡 |
| Skills | skills_active | 425 | 350-450 | 🟢 |
| Skills | error_rate_top_skills | 12% avg | <15% | 🟢 |
| Knowledge | brain_size | 20,451 | >20,000 | 🟢 |
| Knowledge | orphan_ratio | 8% | <10% | 🟢 |

## Integration with Learning Loop

Self-Health Loop connects to the broader Learning Loop architecture:

```
Execution Loop → Harness Loop (Self-Harness) → Meta-Loop
     ↓                ↓              ↓
  Health Signals   Harness Fixes  Loop Optimiza-
     ↓                ↓             tion
  Self-Health     Skill Patches   Architecture
     Repair       Auto-updates    Evolution
```

### Feedback Flows
1. **Health degradation** → triggers Harness Loop improvements
2. **Repeated failures** → Meta-Loop optimizes monitoring thresholds
3. **Successful repairs** → Learning Loop incorporates into skills
4. **Pattern detection** → Creates new preventive health checks

## Stopping Conditions for Health Loops

**Invalid:**
- "Health check passed"
- "No errors detected"

**Valid:**
- All critical services responding
- Memory hit rate > threshold for 3 consecutive checks
- Skill error rate < 15% for 7 days
- Knowledge freshness maintained across all sources
- Abstraction debt within bounds

## Related Pages

- [[hermes-agent-stack]] — Core architecture context
- [[loop-engineering]] — Autonomous loop design
- [[self-harness-paradigm]] — Harness improvement methodology
- [[documentation-master]] — Documentation health
- [[knowledge-master]] — Knowledge graph health
- [[cron-failure-watchdog]] — Existing health monitoring
- [[knowledge-metabolism]] — Knowledge health checks