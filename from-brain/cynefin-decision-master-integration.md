---
type: note
title: Cynefin Integration into decision-master Routing
links:
  - cynefin-framework
  - effort-router
  - bineval-vs-effort-router
  - inversion-premortem
  - decision-making-frameworks
  - naturalistic-decision-making
captured_at: '2026-07-19T07:44:44.949Z'
captured_via: capture-cli
ingested_via: put_page
ingested_at: '2026-07-19T07:44:45.309Z'
source_kind: put_page
tags:
  - complexity
  - cynefin
  - decision-master
  - effort-routing
  - premortem
  - routing
created: 2026-07-19
---
# Cynefin Integration into decision-master Routing

Analysis of where Cynefin framework domains slot into the decision-master meta-skill's routing routines. decision-master currently has two routing mechanisms that Cynefin enriches with a third dimension.

**Created:** 2026-07-19 (during premortem and triaging work)

## The Current Routing (2 Mechanisms)

### Mechanism A: Phase Routing
User signal phrases determine which phase:
- "What are my options?" → Explore → bayesian-rogue-explore
- "Stress-test these" → Sieve → socratic-sieve
- "Execute plan Y" → Exploit → leverage-executor

### Mechanism B: Stakes Calibration (Depth)
```
Reversible <1 week?
  YES → Low → 1-3-1 rule
  NO → Capital involved?
    NO → Medium → sieve + asymmetry + premortem
    YES → High → full chain + kelly + premortem
```

## The Gap: Stakes Conflates Two Questions

Mechanism B answers "how much does it cost if wrong?" but not "what kind of problem IS this?"

Two problems with the same stakes can require fundamentally different approaches:
- **Clear + High Stakes:** Runbook deploy to production. Stakes are high but the approach is Sense-Categorize-Respond — follow the known procedure precisely. The full sieve chain is waste.
- **Complex + Low Stakes:** Which experiment to try next. Stakes are low but the approach is Probe-Sense-Respond — you need safe-to-fail probing, not a quick 1-3-1 bypass.

Cynefin separates **approach** (what kind of problem) from **depth** (how much to invest).

## The Integration: 2D Routing Matrix

### Axis 1: Cynefin Domain → Approach

| Domain | Cynefin Approach | decision-master Routing |
|--------|-----------------|------------------------|
| **Clear** | Sense→Categorize→Respond | Skip funnel. Direct execution or runbook lookup. Best practice exists — use it. |
| **Complicated** | Sense→Analyze→Respond | The Sieve chain: socratic-sieve → mean-variance → asymmetry-hunter → optionality-valuer. Multiple right answers, pick best via analysis. |
| **Complex** | Probe→Sense→Respond | Explore with emphasis on Gittins wildcards and safe-to-fail experiments. No right answer in advance — patterns emerge through interaction. |
| **Chaotic** | Act→Sense→Respond | Leverage-executor immediately with bounded-downside focus. Stabilize first, analyze later. Top-down decisive action. |

### Axis 2: Stakes → Depth (unchanged)
- Low: 1-3-1, single skill
- Medium: 3-4 skill chain
- High: full chain + kelly-sizer + premortem

### The Combined Matrix

| | Low Stakes | Medium Stakes | High Stakes |
|---|---|---|---|
| **Clear** | Execute directly | Execute + verify | Execute + verify + premortem (checklist) |
| **Complicated** | 1-3-1 analyze | Sieve chain (4 skills) | Full chain + kelly + premortem |
| **Complex** | 1-3-1 probe | Explore + safe-to-fail experiment | Full explore + probe + premortem (mandatory) |
| **Chaotic** | Act immediately | Act + stabilize + diagnose | Act + stabilize + full diagnostic + postmortem |

## Why This Matters for Premortem and Triaging

### Premortem Depth by Domain
The effort router (via Cynefin) decides how much reasoning the premortem itself gets:
- **Clear-domain plan:** Low-effort premortem. Checklist review. "Did we follow the runbook?"
- **Complicated-domain plan:** Medium-effort premortem. Expert analysis of alternatives.
- **Complex-domain plan:** High-effort premortem. Probe-sense-respond. "What patterns might emerge that we haven't seen?"
- **Chaotic-domain plan:** Max-effort premortem. Act-first validation. "What's the stabilization path if this goes wrong?"

### Triaging by Domain
Cynefin classifies the triage target, not just its priority:
- **Clear incidents:** Triage is fast — known failure, known fix. Low effort.
- **Complicated incidents:** Triage needs expertise — diagnosis required. Medium effort.
- **Complex incidents:** Triage needs probing — cause unknown, experiment to find it. High effort.
- **Chaotic incidents:** Triage is stabilization-first — stop the bleeding, classify later. Max effort, decisive action.

This enables cost-aware triage: priority (stakes) AND approach (domain) AND cost (effort) all factor into the routing decision.

## Concrete Upgrade to decision-master

### New Decision Mechanism: C (Domain Classification)

Add before stakes calibration:

```
Step 1: Classify the problem domain
  Does a runbook/standard procedure exist? → CLEAR
  Does it need expert analysis of known alternatives? → COMPLICATED
  Are outcomes only knowable after trying? → COMPLEX
  Is the situation actively failing with no clear cause? → CHAOTIC
  Unclear which applies? → CONFUSION (decompose first)

Step 2: Apply domain approach (determines which skills)
  CLEAR → skip to Exploit (direct execution)
  COMPLICATED → run Sieve chain
  COMPLEX → run Explore with probing emphasis
  CHAOTIC → run Exploit immediately with stabilization focus

Step 3: Apply stakes calibration (determines depth) [existing Mechanism B]
  Cross-reference domain x stakes in the 2D matrix above
```

### Connection to Effort Router

The effort router's Tier 1 keyword classifier can be upgraded to detect Cynefin domain indicators (constraint type, coupling, cause-effect transparency). This gives decision-master a fast pre-classification of domain before routing, without requiring the user to explicitly state it.

Flow:
```
User request → Effort Router classifies domain (Cynefin indicators)
            → decision-master routes by domain (approach)
            → decision-master calibrates by stakes (depth)
            → Sub-skills execute at the right effort level
```

## Related

- cynefin-framework — the full framework with domain indicators
- effort-router — the system that classifies effort (upgradeable to detect Cynefin domain)
- bineval-vs-effort-router — pre-task vs post-task evaluation
- inversion-premortem — premortem thinking (depth varies by Cynefin domain)
- decision-making-frameworks — the family both belong to
- naturalistic-decision-making — related research tradition (NDM informs Cynefin)

## Sources

- Snowden and Boone (2007). "A Leader's Framework for Decision Making." HBR.
- decision-master skill (strategy/decision-master/SKILL.md)
- Cynefin framework gbrain page (cynefin-framework)
