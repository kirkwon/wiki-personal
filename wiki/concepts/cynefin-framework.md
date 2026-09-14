---
type: note
title: Cynefin Framework - Complexity Indicators for Effort Routing
links:
  - effort-router
  - raschka-reasoning-effort
  - bineval-vs-effort-router
  - complexity
  - decision-making-frameworks
  - naturalistic-decision-making
  - inversion-premortem
  - system-reassessment
captured_at: '2026-07-19T07:40:24.757Z'
captured_via: capture-cli
ingested_via: put_page
ingested_at: '2026-07-19T07:40:25.179Z'
source_kind: put_page
tags:
  - complexity
  - cynefin
  - decision-making
  - effort-routing
  - indicators
  - premortem
  - sense-making
created: 2026-07-19
source: brain/ (retired 2026-09-13)
---
# Cynefin Framework — Complexity Indicators for Effort Routing

Dave Snowden's sense-making framework (1999, IBM) classifies decision contexts by the nature of cause-effect relationships. It provides five domains, each requiring a fundamentally different response. This page documents Cynefin and maps its domain indicators to reasoning effort levels for the effort router.

**Created:** 2026-07-19 (during premortem and triaging work)

## The Five Domains

### Clear (formerly Simple/Obvious)
- **Epistemic state:** Known knowns. Cause-effect is obvious.
- **Constraints:** Fixed — actions must be done in a certain way in a certain order.
- **Coupling:** Tightly constrained, no degrees of freedom.
- **Approach:** Sense to Categorize to Respond. Follow established best practice.
- **Example:** Loan-payment processing. Identify, categorize, apply the rule.
- **Risk:** Complacency. Success breeds assumption that best practice (past practice) always works. Catastrophic clockwise shift to Chaotic when it breaks.

### Complicated
- **Epistemic state:** Known unknowns. Cause-effect exists but requires expertise to discover.
- **Constraints:** Governing — looser rules, policies that bound but don't dictate.
- **Coupling:** Tightly coupled problems.
- **Approach:** Sense to Analyze to Respond. Consult experts, evaluate alternatives.
- **Example:** Database performance degradation. Engineers investigate and diagnose.
- **Multiple right answers exist.** The skill is finding the best one.

### Complex
- **Epistemic state:** Unknown unknowns. Cause-effect only understood in hindsight.
- **Constraints:** Enabling — allow a system to function but don't control the process.
- **Coupling:** Loosely coupled.
- **Approach:** Probe to Sense to Respond. Run safe-to-fail experiments, learn, adapt.
- **Example:** Users abandoning a new feature, no one knows why. A/B tests, iterate.
- **No right answers exist in advance.** Patterns emerge through interaction.

### Chaotic
- **Epistemic state:** No discernible cause-effect.
- **Constraints:** None. Problems are de-coupled.
- **Coupling:** De-coupled.
- **Approach:** Act to Sense to Respond. Stabilize first, then learn.
- **Example:** Active cyberattack. Isolate systems immediately, analyze later.
- **Action — any action — is the first and only appropriate response.** Top-down broadcast communication.

### Confusion (Disorder)
- **Epistemic state:** Unclear which domain applies.
- **Approach:** Break the problem down until each part can be classified into one of the four domains.
- **Multiple perspectives jostle, factional leaders argue, cacophony rules.**

## Cynefin to Effort Level Mapping

This is the key insight for the effort router: Cynefin domains provide richer classification indicators than task-type keywords.

| Cynefin Domain | Effort Level | Rationale |
|----------------|-------------|-----------|
| Clear | **low** | Best practice exists, just follow the runbook. No reasoning needed. |
| Complicated | **medium** | Requires analysis but the problem is tractable. Expert reasoning, bounded scope. |
| Complex | **high** | No right answer, needs experimentation. High reasoning for safe-to-fail probing. |
| Chaotic | **max** | Act first, think later. But the actions taken must be high-reasoning because stakes are existential. |
| Confusion | **max** | Escalate until the problem is decomposed and classified. |

## Indicators — Far Better Than Keyword Matching

The current Tier 1 effort router classifies by task vocabulary (read/email/deploy). Cynefin offers task-structure indicators that classify the epistemic nature of the problem:

### Indicator 1: Constraint Type
- Fixed constraints (runbook, SOP, legal structure) -> Clear -> low effort
- Governing constraints (policies, rules of thumb) -> Complicated -> medium
- Enabling constraints (boundaries that allow emergence) -> Complex -> high
- No constraints (formless, unconstrained) -> Chaotic -> max

### Indicator 2: Coupling
- Tightly constrained, no degrees of freedom -> Clear -> low
- Tightly coupled problems -> Complicated -> medium
- Loosely coupled problems -> Complex -> high
- De-coupled problems -> Chaotic -> max

### Indicator 3: Cause-Effect Transparency
- Obvious (do X, expect Y) -> Clear -> low
- Discoverable with expertise -> Complicated -> medium
- Only in hindsight -> Complex -> high
- Not at all -> Chaotic -> max

### Indicator 4: Knowledge State (Rumsfeldian)
- Known knowns -> Clear -> low effort
- Known unknowns -> Complicated -> medium
- Unknown unknowns -> Complex -> high

## Domain Transitions (The Fold)

Cynefin is dynamic. Domains shift:
- **Clockwise drift:** Chaotic -> Complex -> Complicated -> Clear (as knowledge accumulates)
- **Catastrophic failure:** Clear -> Chaotic (the fold between complacency and collapse)
- **Counter-clockwise:** Knowledge loss, generational questioning of rules

For the effort router this means: effort levels should track domain shifts, not just task type. A task that starts Clear can shift Complex mid-execution (the output doesn't work, debugging reveals emergent behavior).

## Application to Premortem and Triaging

### Premortem
The effort router decides how much reasoning to spend ON the premortem itself:
- Clear-domain plan (routine deploy): low-effort premortem (checklist review)
- Complex-domain plan (new feature, unknown outcomes): high-effort premortem (probe-sense-respond)

BINEVAL then evaluates whether the premortem surfaced real risks (binary: did it identify a failure mode that would have occurred?).

### Triaging
Cynefin classifies the triage target:
- Clear incidents (known service down): triage is fast, low effort, follow runbook
- Complex incidents (users abandoning, no cause): triage needs probing, high effort

This enables cost-aware triage: not just what matters most, but what matters most per token spent, AND what decision approach the situation actually requires.

## Upgrade Path for the Effort Router

Current Tier 1 keywords (read/email/deploy) are task-vocabulary indicators. Cynefin indicators are task-structure indicators. The upgrade:

1. Add constraint-type detection: Does the task reference a runbook, SOP, or standard procedure? -> Clear -> low effort
2. Add expertise detection: Does the task require analysis or diagnosis? -> Complicated -> medium
3. Add uncertainty detection: Are outcomes only knowable after execution? -> Complex -> high
4. Add crisis detection: Is the situation actively failing with no clear cause? -> Chaotic -> max

These structural indicators are more robust than vocabulary because the same task (e.g., "fix the database") can be Clear (restart a known-failed service), Complicated (diagnose unfamiliar perf issue), or Complex (users leaving, no cause).

## Related

- effort-router — the system this upgrades
- raschka-reasoning-effort — the two-knob framework (model size x reasoning effort)
- bineval-vs-effort-router — pre-task vs post-task evaluation
- complexity — the general concept
- decision-making-frameworks — the family Cynefin belongs to
- naturalistic-decision-making — related research tradition
- inversion-premortem — premortem thinking
- system-reassessment — this analysis is a system reassessment

## Sources

- Snowden and Boone (2007). "A Leader's Framework for Decision Making." Harvard Business Review 85(11): 68-76.
- Kurtz and Snowden (2003). "The new dynamics of strategy: Sense-making in a complex and complicated world." IBM Systems Journal 42(3): 462-483.
- The Cynefin Company (thecynefin.co)
- Wikipedia: Cynefin framework
