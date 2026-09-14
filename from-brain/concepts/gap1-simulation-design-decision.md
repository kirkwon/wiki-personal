---
tags: ['decision', 'gap-1', 'simulation', 'game-theory']
created: 2026-07-06
---

# GAP-1 Design Decision: Game-Theoretic Finance Analysis with Simulation

**Date:** 2026-06-21
**Status:** DECISION — proceeding with hybrid approach
**Related:** [[game-theory-gaps]], [[code-world-models-general-game-playing]]

---

## The Question

How do we operationalize game theory in finance skills? Two paths:

### Path A: Analytical Game Theory
Compute Nash equilibria, payoff matrices, signaling equilibria directly. Tools: `nashpy`, `gambit`, custom solvers.

**Pros:** Rigorous, fast, deterministic
**Cons:** Only works for small games (2-4 players, discrete strategies). Real markets have thousands of players with continuous strategies. Analytical solutions don't exist for most real market scenarios.

### Path B: Agent-Based Simulation (MiroFish-inspired)
Generate agents representing market participants, let them interact in a simulated market, observe emergent behavior.

**Pros:** Handles arbitrary complexity. Captures emergent phenomena (herding, bubbles, crashes). Can model continuous strategies and many players.
**Cons:** Computationally expensive if every agent is an LLM. Results are stochastic, need many runs.

## Reference: MiroFish Architecture

[MiroFish](https://github.com/666ghj/MiroFish) (Shanda-backed, TrendShift #16144) is a multi-agent simulation engine:

1. **Seed extraction** — ingest real-world data (news, financial signals)
2. **Persona generation** — create agents with personalities, memory, behavioral logic
3. **Simulation** — agents interact freely, social evolution emerges
4. **Variable injection** — "God's-eye view" to test what-if scenarios
5. **Report generation** — ReportAgent synthesizes predictions

Built on [OASIS](https://github.com/camel-ai/oasis) (CAMEL-AI) — social media simulator supporting up to 1M agents with 23 action types, dynamic environments, recommendation systems.

**Key insight:** MiroFish uses LLM agents for ALL participants. This is expensive and designed for social media simulation (opinion spread, virality). For financial markets, most participants can be modeled with simple behavioral rules — only key strategic actors need LLM reasoning.

## DECISION: Hybrid Simulation (Path C)

**Do not replicate MiroFish's full-LLM approach.** Instead, build a hybrid:

### Layer 1: Market Microstructure (Rule-Based Agents)
- **No LLM needed.** Agents are simple programs with:
  - Capital allocation
  - Risk tolerance parameter
  - Decision rule (momentum, mean-reversion, value, index-tracking)
  - Information set (what they know and when)
- **Types:** Index funds (mechanical), momentum traders, value investors, hedgers, market makers, retail (noise traders)
- **Engine:** Python loop with order matching, price discovery
- **Cost:** Near-zero (pure computation)

### Layer 2: Strategic Decision-Makers (LLM Agents)
- **LLM-powered.** Only for actors making complex strategic decisions:
  - Elon Musk (lock-up sell decision)
  - Fed (rate decision response)
  - Large funds (index rebalancing timing — front-run or wait?)
  - Company management (secondary offering timing)
- **Cost:** 5-10 LLM calls per simulation step (not thousands)

### Layer 3: Analysis & Equilibrium Discovery
- Run 100-1000 simulations with varied parameters
- Identify dominant strategies (what consistently wins?)
- Detect emergence (herding, crashes, squeezes)
- Compare to real market data for calibration

### Why Hybrid Beats Pure Approaches

| Dimension | Analytical Only | MiroFish-Style (Full LLM) | Hybrid (Decision) |
|-----------|----------------|--------------------------|-------------------|
| Market realism | ❌ Too simple | ✅ High | ✅ High |
| Cost per run | $0 | $$$ (thousands of LLM calls) | $ (5-10 calls) |
| Speed | Seconds | Hours | Minutes |
| Captures emergence | ❌ No | ✅ Yes | ✅ Yes |
| Strategic depth | ❌ Only small games | ✅ Deep | ✅ Deep (for key actors) |
| Reproducibility | ✅ Deterministic | ❌ Stochastic | ⚠️ Semi (seed-controlled) |

## Architecture

```
┌─────────────────────────────────────────────┐
│           MARKET SITUATION INPUT             │
│  (SPCX NDX rebalance, lock-up expiry, etc.) │
└───────────────────┬─────────────────────────┘
                    │
         ┌──────────▼──────────┐
         │   AGENT GENERATION   │
         │                      │
         │  Rule-Based:          │
         │  • Index funds (mech) │
         │  • Momentum traders   │
         │  • Value investors    │
         │  • Market makers      │
         │  • Retail (noise)     │
         │                      │
         │  LLM-Powered:         │
         │  • Key strategists    │
         │  • Fed/Regulators     │
         │  • Large funds        │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │    SIMULATION LOOP    │
         │                      │
         │  For each timestep:   │
         │  1. Agents observe    │
         │  2. Agents decide     │
         │  3. Orders matched    │
         │  4. Price discovered  │
         │  5. Info propagates   │
         │                      │
         │  Inject shocks at     │
         │  scheduled events     │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │   ANALYSIS LAYER     │
         │                      │
         │  • Run N=1000 sims   │
         │  • Find dominant      │
         │    strategies         │
         │  • Detect emergence   │
         │  • Calibrate to real  │
         │    market data        │
         └──────────┬──────────┘
                    │
         ┌──────────▼──────────┐
         │  TRADEABLE OUTPUT    │
         │                      │
         │  • Optimal entry/exit│
         │  • Risk scenarios    │
         │  • Probability dist  │
         │  • Alert triggers    │
         └─────────────────────┘
```

## Connection to CWM Pattern

The CWM paper's insight applies directly:
- **CWM in games:** LLM compiles rules → MCTS searches
- **CWM in markets:** LLM compiles market participant models → simulation searches the outcome space

The simulation IS the Code World Model — an executable encoding of market rules. The classical solver is Monte Carlo simulation (run thousands of times) instead of MCTS on a game tree.

## Implementation Constraints

- **Python 3.8** compatibility (`from __future__ import annotations`)
- **No heavy ML frameworks** — pure Python + numpy
- **LLM calls via Hermes delegation** — not a separate API client
- **Output format:** Markdown report + optional HTML visualization
- **Calibration data:** yfinance via OpenBB MCP (already available)

## What We're NOT Doing (Yet)

- Not deploying MiroFish itself (Python 3.11+ required, our system is 3.8)
- Not running full social-media-style simulations (wrong domain)
- Not building a web frontend (CLI + markdown output for now)
- Not replacing analytical game theory entirely (small games still use nashpy)

## Success Criteria

The skill succeeds when, given a market situation (e.g., "SPCX entering NDX on July 6 with 4.3% float"), it produces:
1. A simulation showing likely price paths (not just point estimates)
2. Identification of the dominant strategy (what to do)
3. Risk scenarios (what could go wrong)
4. Probability distribution of outcomes (not just base/bull/bear)
5. Calibration against known historical analogs (e.g., Tesla NDX inclusion 2020)
