title: Loop Engineering
status: active
priority: P2
created: 2026-06-28T00:00:00.000Z
updated: 2026-06-28T00:00:00.000Z
---

# Loop Engineering

## Summary
Designing self-running agent loops: heartbeat, SKILL.md, state files, verifiers, worktrees, MCP — transitioning from prompting to engineering autonomous systems.

## Why
Manual prompting doesn't scale. Loop engineering enables agents to prompt agents, verify work, and iterate without humans — the foundation for autonomous quant research and knowledge maintenance.

## Progress

- [x] Core framework documented (`~/brain/loop-engineering.md`, 171 lines)
- [x] Graph of Thoughts integration patterns mapped
- [x] Loop engineering roadmap source captured
- [x] 6-component loop architecture defined (heartbeat, SKILL.md, state file, verifier, worktrees, MCP)
- [x] Implementation plan created (`~/clawd/loop-engineering/plan.md`)
- [ ] Phase 1: Critic separation (doer/critic in separate sub-agents)
- [ ] Phase 2: Triage inbox (visibility into loop status)
- [ ] Phase 3: Skill auto-patch (feedback-driven skill updates)
- [ ] Phase 4: /goal primitive (automation framework)
- [ ] Game-theory gaps operationalized (7 gaps identified)

## Next Steps
1. Phase 1: Build critic-only sub-agent template (`critic-agent.sh`)
2. Define the 4-condition loop viability test
3. Blog post: "Stop prompting. Start engineering loops."

## Blockers / Needs Input
- Phase sequencing: P0 (critic separation + triage) before P1 (skill auto-patch + /goal)

## Key Files / Resources
- `~/brain/loop-engineering.md` — core framework
- `~/brain/graph-of-thoughts.md` — GoT concepts
- `~/brain/loop-engineering-got-integration.md` — GoT + loop patterns
- `~/brain/concepts/game-theory-gaps.md` — 7 gaps in game theory operationalization
- `~/brain/concepts/gap1-simulation-design-decision.md` — hybrid market simulation design
- `~/clawd/loop-engineering/plan.md` — 4-phase implementation plan

## Automation / Cron
- None directly. Symphony/Kanban (paused) is the execution layer for this.

## Notes
- Pairs naturally with Causal AI / Hedge Agent project (autonomous quant loops)
- "Boris Cherny: I don't prompt Claude anymore, I write loops" — great blog hook
