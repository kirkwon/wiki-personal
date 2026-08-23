

# Strategic Decision Framework

A unified decision-making framework combining 6 strategic filters with a scored rubric. Designed to decide WHETHER to act before deciding HOW to act.

## The Architecture

```
 ┌─────────────────────────────────────────────────────────┐
 │  PRE-FILTER: CIRCLE OF COMPETENCE                       │
 │  Are we qualified to assess this?                       │
 │  → NO: Delegate or learn                                │
 │  → YES: Proceed                                          │
 └──────────────────────┬──────────────────────────────────┘
                        │
                        ▼
 ┌─────────────────────────────────────────────────────────┐
 │  STRATEGIC FILTER (6 Steps, scored -2 to +2 each)       │
 │                                                         │
 │  Step 1: WHY          → Purpose/urgency         Score   │
 │  Step 2: UPSIDE       → Asymmetry/compounding   Score   │
 │  Step 3: FIELD        → Signal/noise/vol/complex Score   │
 │  Step 4: RESOURCES    → Bet sizing (Kelly)       Score   │
 │  Step 5: INVERT       → Premortem               Score   │
 │  Step 6: LEVERAGE     → Pareto / via negativa   Score   │
 │                                                         │
 │  TOTAL: ___ / 12                                         │
 └──────────────────────┬──────────────────────────────────┘
                        │
                        ▼
              ┌─────────────────┐
              │  DECISION RULE  │
              ├─────────────────┤
              │  ≥ +8: GO       │
              │  +4 to +7: GO   │
              │  0 to +3: HOLD  │
              │  < 0: SKIP      │
              └─────────────────┘
```

## The Rubric

| Step | -2 | -1 | 0 | +1 | +2 |
|------|----|----|----|----|----|
| **1. WHY** | No clear reason | Vague benefit | Marginal | Clear motivation | Existential / urgent |
| **2. UPSIDE** | Asymmetric downside | Symmetric downside | Symmetric | Long-term compound | 10:1+ asymmetric |
| **3. FIELD** | Chaotic, no signal | High noise/low signal | Mixed | Clear signal, bounded noise | Crystal clear |
| **4. RESOURCES** | Can't bound scope | Open-ended | Rough bounds | Clear bounds | Known exact cost |
| **5. INVERT** | Failure likely & unfixable | High-severity risk | Manageable risks | Low risk | Near-zero failure modes |
| **6. LEVERAGE** | No leverage found | 10%→20% result | 20%→40% | 20%→70% | 10%→80%+ (clear Pareto) |

## The Mental Model Stack

Each step is grounded in specific mental models from the knowledge base:

| Step | Primary Model | Supporting Models |
|------|---------------|-------------------|
| Pre-filter | Circle of Competence | Dunning-Kruger, Margin of Safety |
| Step 1 | First Principles Thinking | Via Negativa, Opportunity Cost |
| Step 2 | Ergodicity | Kelly Criterion, Tail Event Thinking |
| Step 3 | Signal vs Noise | Base Rate Neglect, Second-Order Effects |
| Step 4 | Kelly Criterion | Margin of Safety, Ergodicity |
| Step 5 | Inversion / Premortem | Via Negativa, Unintended Consequence |
| Step 6 | Pareto Principle | Leverage and Risk, First Things First |

## When to Use

- **Every non-trivial implementation** — run the full filter before executing
- **Weekly / strategic reviews** — score past decisions to calibrate the rubric
- **Resource allocation** — which project gets time/tokens this week?
- **Spike vs build decisions** — use the field assessment to decide if you need an experiment

## Calibration

The rubric should NOT be static. After each decision, log:
- Your scores before acting
- The actual outcome
- What you missed

Over time, adjust the scoring thresholds. If you're taking too many GO decisions that fail, raise the threshold. If you're skipping things that would have worked, lower it.

See also: [[pareto-principle-80-20]]

See also: [[inversion-premortem]]

See also: [[kelly-criterion-bet-sizing]]

See also: [[via-negativa-subtraction]]

See also: [[circle-of-competence]]

See also: [[ergodicity]]

See also: [[first-principles-thinking]]

See also: [[leverage-and-randomness]]

See also: [[margin-of-safety-financial]]

See also: [[base-rate-neglect]]

See also: [[super-thinking-gabriel-weinberg]]

See also: [[first-order-and-second-order-thinking]]

See also: [[the-signal-and-the-noise]]

See also: [[tail-event-thinking]]

See also: [[reasonable-vs-rational-decisions]]
