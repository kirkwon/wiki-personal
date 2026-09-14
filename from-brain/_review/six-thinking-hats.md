---
type: note
title: Six Thinking Hats — Sequences & Pro Tips (v2)
links:
  - cynefin-framework
  - cynefin-decision-master-integration
  - effort-router
  - decision-making-frameworks
  - six-thinking-hats
captured_at: '2026-07-19T07:55:30.417Z'
captured_via: capture-cli
ingested_via: put_page
ingested_at: '2026-07-19T07:55:30.862Z'
source_kind: put_page
tags:
  - communication-skills
  - creativity
  - cynefin
  - de-bono
  - decision-making
  - decision-master
  - frameworks
  - go-no-go
  - group-dynamics
  - parallel-thinking
  - perspective-coverage
  - problem-solving
  - routing
  - sequences
  - six-thinking-hats
created: 2026-07-19
---
# Six Thinking Hats — Sequences & Pro Tips (v2)

Extended reference with pragmatic situation-specific sequences and bounding rules for implementation. Builds on six-thinking-hats (v1) which established the three-axis framework (Cynefin x Stakes x Six Hats).

**Created:** 2026-07-19 (v2 — enriched with Go/No-Go and problem-solving sequences)

## The Six Hats (Operational Definitions)

| Hat | Mode | Question Asked | Constraint |
|-----|------|---------------|-----------|
| ⚪ **White** | Data & Facts | What info do we have? What's missing? How to get it? | No interpretations. Objective data only. |
| 🔴 **Red** | Emotion & Intuition | What's your gut reaction? How do you feel? | No justification or logic allowed. |
| ⚫ **Black** | Caution & Risk | What are the flaws, bottlenecks, failure points? | Must be logical. Specific, solvable critiques — not vague pessimism. |
| 🟡 **Yellow** | Optimism & Value | What are the benefits? Why will it work? Best case? | Requires logical justification (unlike Red). |
| 🟢 **Green** | Creativity & Alternatives | What are the alternatives? How to overcome Black Hat risks? | No criticism allowed during this phase. |
| 🔵 **Blue** | Process & Control | Manages the process itself. | Used at start (agenda) and end (synthesis + next steps). |

## Situation-Specific Sequences (The Flowcharts)

### 1. Evaluating a Strategic Decision (Go/No-Go)
*When a specific proposal is on the table and you need to decide whether to move forward. This is the canonical high-stakes decision sequence.*

🔵 Blue → ⚪ White → 🟡 Yellow → ⚫ Black → 🟢 Green → 🔴 Red → 🔵 Blue

1. **Blue:** Define the decision that needs to be made.
2. **White:** Lay out known facts, costs, market data.
3. **Yellow:** Explore potential upside, ROI, strategic advantages.
4. **Black:** Stress-test. Structural risks, worst-case, failure points.
5. **Green:** Brainstorm ways to mitigate the Black Hat risks.
6. **Red:** Check gut feeling after hearing all angles. (Still hesitant despite logic?)
7. **Blue:** Make final decision and define action plan.

**Key insight:** Yellow comes BEFORE Black. You build the positive case first, then stress-test it. This prevents premature dismissal and ensures the risk assessment targets a fully-developed thesis. Green mitigates Black — you can't mitigate risks you haven't identified.

### 2. Solving a Complex Problem
*When something is broken or a process is failing. Focus on root cause and alternatives.*

🔵 Blue → ⚪ White → ⚫ Black → 🟢 Green → 🔵 Blue

1. **Blue:** Define the exact problem and scope.
2. **White:** Gather all logs, error reports, historical data about the failure.
3. **Black:** Analyze why the current system is failing. What are the constraints?
4. **Green:** Generate entirely new workarounds or architectural changes.
5. **Blue:** Select the best alternative to prototype and assign tasks.

**Key insight:** Stripped of Yellow/Red — this is a faster path when the problem is clearly broken and needs engineering, not buy-in.

### 3. Rapid Idea Generation (Brainstorming)
*When you need to fill a blank canvas and avoid shooting down ideas too early.*

🔵 Blue → ⚪ White → 🟢 Green → 🟡 Yellow → 🔵 Blue

1. **Blue:** Set creative goal and time limits.
2. **White:** State current baseline and constraints.
3. **Green:** Unrestricted brainstorming and idea generation.
4. **Yellow:** Filter by highlighting strongest aspects of each idea.
5. **Blue:** Categorize best ideas for further research.

**Key insight:** Black Hat is deliberately omitted. Criticism kills ideation. Yellow filters constructively — keep the strongest, defer the rest.

## Pro Tips for Implementation

### Bound the Red Hat
- **Duration:** Under 30 seconds per person. Pure instinct, not analysis.
- **Format:** Often takes the form of dot-voting or a one-word reaction.
- **Why it matters:** Longer Red Hat sessions drift into justification — which is Black or Yellow Hat thinking wearing a Red disguise. The signal is the immediate, unfiltered reaction.

### Bound the Black Hat
- **Specificity:** Solvable critiques only. "This won't scale" is a valid Black Hat. "This is doomed" is not — it's vague pessimism wearing a Black disguise.
- **Logic required:** Every Black Hat point must have a logical basis. "I don't like it" is Red, not Black.
- **Bounding prevents paralysis:** Unbounded Black Hat thinking is the most common failure mode of Six Hats implementation. Set a time limit and require actionable critiques.

### Sequencing Principle
- Always begin and end with Blue (process control).
- The middle sequence is situation-dependent.
- Red Hat is always short and never comes first (need data before gut reacts).

## Mapping to decision-master + Cynefin (Updated)

The pragmatic sequences map cleanly onto the 3D routing matrix:

| Sequence | Cynefin Domain | decision-master Phase | Stakes |
|----------|---------------|----------------------|--------|
| Go/No-Go (B-W-Y-Blk-G-R-B) | Complicated | Sieve → Decision | High |
| Solving Complex Problem (B-W-Blk-G-B) | Complicated/Complex | Sieve → Exploit | Medium-High |
| Brainstorming (B-W-G-Y-B) | Complex | Explore | Low-Medium |
| Quick Feedback (B-Blk-G-B) | Clear | Bypass | Low |

### Go/No-Go = The Missing High-Stakes Template

The Go/No-Go sequence is the canonical template for decision-master's high-stakes Sieve phase. It's richer than the current "sieve → MV → asymmetry → optionality → premortem" chain because it:
1. Builds the positive case (Yellow) before stress-testing (Black) — prevents premature dismissal
2. Inserts Green (mitigation) between Black and decision — risk reduction is generative
3. Ends with Red (gut check) before Blue (decide) — the intuition gap from v1 is closed

**Recommended update to decision-master Workflow A (Full Funnel):** Insert Red Hat gut-check after the analytical chain, before leverage-executor. The chain becomes:
```
knowledge-master (White) → bayesian-rogue-explore (Green) → socratic-sieve + asymmetry + optionality (Yellow) → premortem (Black) → Green mitigation → RED GUT CHECK → leverage-executor (Blue decide)
```

## Related

- six-thinking-hats (v1) — the three-axis framework and Red Hat gap finding
- cynefin-framework — orthogonal axis 1 (problem type)
- cynefin-decision-master-integration — the 2D matrix extended to 3D by Six Hats
- effort-router — the classifier that detects all three axes
- decision-making-frameworks — the family

## Sources

- de Bono, Edward (1985). Six Thinking Hats. Little, Brown and Company.
- User-provided operational definitions and pragmatic sequences (2026-07-19)
- Wikipedia: Six Thinking Hats (canonical sequences)
- WorkshopBank: Six Thinking Hats Method
