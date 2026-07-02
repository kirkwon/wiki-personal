---
slug: email-safety-system
title: Email Triage & Safety System
status: active
priority: P1
created: 2026-06-28T00:00:00.000Z
updated: 2026-06-28T00:00:00.000Z
---

# Email Triage & Safety System

## Summary
Autonomous email triage with Bayesian sender trust, SPF/DKIM/DMARC authentication gate, and centralized safety reference for fraud, theft, and identity leakage.

## Why
The spam invoice incident (Jun 28) proved unauthenticated emails with urgency keywords bypass the trust system. Building layered defenses — authentication, trust evaluation, and comprehensive safety documentation.

## Progress

- [x] **Layer 2:** SPF/DKIM/DMARC authentication gate (`check_authentication()` in inbox-triage.py)
- [x] Auth gate tested (6/6 unit tests pass, compiles clean)
- [x] Gmail skill patched with Layer 2 documentation
- [x] Safety reference created (`~/brain/safety-reference.md`, 280 lines)
- [x] Legal/regulatory framework analysis (`~/brain/safety-frameworks-legal-regulatory.md`, 339 lines)
- [x] Blog draft: spam invoice escalation (`~/brain/blog/blog-spam-invoice-escalation.md`)
- [ ] **Layer 1:** Trust gate for ALL urgency levels (not just medium) — proposed, not implemented
- [ ] **Layer 3:** Flip DEFAULT_TRUST from 0.7 to 0.3 for unknown senders — proposed, not implemented
- [ ] Deepfake voice/video verification protocol
- [ ] Agent action audit logging
- [ ] PII redaction filter in agent contexts
- [ ] Human-in-the-loop confirmation gate for financial actions

## Next Steps
1. Implement Layer 1 (trust gate applies to high urgency too)
2. Implement Layer 3 (DEFAULT_TRUST 0.7 → 0.3)
3. Fix Financial Strategy Notebook cron error
4. Build agent action audit log

## Blockers / Needs Input
- Layers 1 & 3 were proposed but user chose "layer 2" only. Ready to implement when confirmed.

## Key Files / Resources
- `~/.hermes/scripts/inbox-triage.py` — triage engine with auth gate
- `~/brain/safety-reference.md` — master safety reference
- `~/brain/safety-frameworks-legal-regulatory.md` — 15-cell legal framework matrix
- `~/brain/blog/blog-spam-invoice-escalation.md` — blog draft

## Automation / Cron
- `e12b122dccdf` — Inbox Triage (3x daily: 7am, noon, 9pm)
- `90b70ac0e59a` — Inbox Triage 4:30pm
- `c737b2f7d216` — Weekly triage sweep (Mon 9am)

## Notes
- Incident that triggered this: unauthenticated spam invoice from "Acme Corp" escalated as "Payment due: $2,500 — Action required by 5 PM today" in morning briefing.
- Layer 2 quarantines unauthenticated high-urgency emails (downgrade, not drop).
