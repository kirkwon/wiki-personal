---
date: 2026-06-13
type: source
title: Loop Engineering Plan
created: 2026-06-13
updated: 2026-06-13
tags: [loop-engineering, software-development, hermes-agent]
sources: ["loop-engineering-plan.md"]
---
# Loop Engineering Plan
The Loop Engineering Plan is a detailed implementation plan for improving the efficiency and effectiveness of software development tasks. It involves the use of a software agent, Hermes Agent (deepseek-v4-flash), and various components such as critic separation, triage inbox, skill auto-patch, and /goal primitive.

## Key Components
- Critic Separation: Separating the validation component from the execution component in a software agent.
- Triage Inbox: A mechanism for managing and surfacing patterns from failed validations.
- Skill Auto-Patch: The ability of the system to automatically propose updates to existing skills based on new findings.
- /goal Primitive: A run-until-done wrapper that iterates until a condition is met or a maximum number of iterations is reached.

## References
- [Addy Osmani - Loop Engineering](https://addyosmani.com/blog/loop-engineering/)
- [Self-Harness skill](~/.hermes/skills/software-development/self-harness/)
- [methodology-loop.md](~/wiki-personal/wiki/concepts/methodology-loop.md)
- [delegate_task documentation](~/.hermes/hermes-agent/docs/)
---