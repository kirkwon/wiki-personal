---
created: 2026-08-23
updated: 2026-08-23
---

-
# System Replacement vs. Repair

John Gall's framework for deciding when to abandon a system entirely versus when to incrementally fix it. This is one of the most actionable takeaways from *The Systems Bible*.

## Core Idea
The only effective fix for a broken system is often replacement, not patching. Incremental fixes tend to fail, accumulate technical debt, and mask deeper structural issues. However, replacement is not always appropriate—sometimes incremental repair is sufficient.

## Decision Framework
- **Replace when**: The system's core architecture is flawed, incremental fixes have failed repeatedly, maintenance cost exceeds replacement value, or the system is fundamentally misaligned with current needs
- **Repair when**: The system's foundation is sound, problems are surface-level, incremental fixes have a track record of working, or replacement costs far exceed repair value
- **Evolve when**: The system works but needs expansion—apply [[Gall's Law]] by building a simple extension and evolving from there

## Key Warning
Gall cautions against endless repair cycles that never address root causes. He also warns against premature replacement of working systems. The decision should be based on evidence of system performance over time, not frustration.

## Connection to Other Concepts
This framework connects to [[decision-quality-vs-outcome-quality]]—a replacement decision should be evaluated on process quality, not just outcome. It also relates to [[decomposing-and-recombining]], since replacing a system often means decomposing it into simpler components and recombining them in a new architecture.
---

See also: [[the-systems-bible-john-gall]]

See also: [[gall-s-law]]

See also: [[fundamental-theorem-of-systems]]

See also: [[systematic-decision-making]]
