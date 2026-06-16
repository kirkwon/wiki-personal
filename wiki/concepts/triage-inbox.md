---
type: concept
title: Triage Inbox
created: 2026-06-13
updated: 2026-06-13
tags: [triage-inbox, software-development, loop-engineering]
related: [loop-engineering-plan, critic-separation]
sources: ["loop-engineering-plan.md"]
---
# Triage Inbox
Triage inbox is a mechanism for managing and surfacing patterns from failed validations. It involves writing structured markdown notes to a triage directory and using a cron job to sweep these notes weekly and surface patterns.

## Implementation
- Create a triage note writer.
- Set up a triage directory and index.
- Implement a weekly sweep cron job.

## Importance
The triage inbox is important for feedback and improvement in the loop engineering process. It helps in identifying and addressing patterns of failure, leading to more efficient and effective software development.
---