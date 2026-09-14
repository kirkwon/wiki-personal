---
tags: ['log', 'experiment', 'research']
created: 2026-07-06
---

# A/B Test Log

## Test 1: storm-research vs research-agent

| Dimension | storm-research | research-agent |
|---|---|---|
| **Input** | "Will SpaceX maintain its $2.1T valuation post-NDX-100 inclusion?" | Same |
| **Output size** | 275 lines, 17KB | 220 lines |
| **Sources** | 13 cited (Damodaran, CNBC, Guardian, BBC, Atlantic, Bloomberg) | 15+ cited (CNBC, Reuters, TechCrunch, HN, analyst PTs) |
| **Structure** | Thesis → Anti-thesis → Synthesis (6 perspectives) | Sub-questions → Extract → Synthesize |
| **Strongest section** | Damodaran intrinsic valuation ($1.25-1.35T, 60% premium) | Financial fundamentals ($18.7B rev, $4.94B loss, 112x P/S) |
| **Speed** | 306s | 297s |
| **Conclusion** | $1.4-1.8T within 6-12 months | $1.5-2.0T within 6-12 months |

### Comparison

| Axis | Winner | Why |
|---|---|---|
| **Completeness** | storm-research | Deeper expert perspectives, richer IPO chronology, more narrative depth |
| **Actionability** | research-agent | Cleaner structure, easier to extract specific data points, clearer financial table |
| **Speed** | Tie | Both ~5 min |
| **Depth** | storm-research | Damodaran deep-dive + multi-perspective cross-validation adds analytical rigor |

### Verdict

**Keep both — different use cases.**

- Use **storm-research** when the question has genuine multiple perspectives and you want expert-informed analysis with narrative depth. Best for "what should I think about X?" questions.
- Use **research-agent** when you need structured data extraction and clear synthesis. Best for "what are the facts on X?" questions.

The ideal workflow may be: storm-research first (generates the perspectives) → research-agent second (extracts the specific data points from those perspectives).
