---
type: writing
title: 'My AI Agent Escalated a Spam Invoice: Anatomy of a Trust System Failure'
date: '2026-06-28T00:00:00.000Z'
author: Kirk Won
status: raw-material
tags:
  - autonomous-agents
  - email-triage
  - security
  - trust-systems
  - failure-analysis
  - hermes
created: 2026-06-28
source: brain/ (retired 2026-09-13)
---
# My AI Agent Escalated a Spam Invoice

*I built an autonomous email triage system with a Bayesian sender-trust model, negation-aware keyword matching, and A/B divergence logging. A spam invoice bypassed all of it. Here's the anatomy of the failure and what it reveals about trust in autonomous systems.*

## The Hook

My morning briefing cron job - a scheduled AI agent that pulls calendar, email, and weather into a Telegram message - delivered this:

> 📧 **Gmail - urgent items**
> - Payment due: $2,500 invoice from Acme Corp. - Action required by 5 PM today

It looked legitimate. Structured, urgent, actionable. The agent surfaced it as the single most important email in my inbox.

It was spam.

## The System That Failed

To understand why this is embarrassing, you need to know what I'd built. The email pipeline had *layers*:

### Layer 1: Newsletter/Notification Triage
Known bulk senders (Substack, Mailchimp, HubSpot, social platforms) are auto-trashed. System notifications (password resets, order confirmations) get trashed too. This catches ~70% of inbox noise and works well.

### Layer 2: Body-Level Urgency Detection
For emails that survive Layer 1, the system fetches the body and scans for urgency keywords:

```python
URGENT_KEYWORDS = [
    'deadline:', 'due by', 'payment due',
    'invoice attached', 'action required',
    'waiting on you', 'overdue invoice', ...
]
```

This was an upgrade from subject-only matching. An email titled "Quick question" with a body saying "waiting on your budget approval by Friday" would be correctly flagged. I was proud of this.

### Layer 3: Negation-Aware Matching
After a false positive where `[No Action Required]` triggered on the substring `action required`, I built a regex guard that checks the 15 characters before each keyword hit for negation words (no, not, none, nothing, without). Nine test assertions. Clean.

### Layer 4: Bayesian Sender Trust
The piece de resistance. A hybrid sender-reputation system:
- **Low-data regime** (≤5 escalations): conservative linear step decay
- **High-data regime** (>5 escalations): full Bayesian posterior from a judgment equation
- **A/B divergence logging**: tracks when heuristic and Bayesian methods disagree

This was sophisticated. I logged divergences. I had trust thresholds. I had decay curves.

## How the Spam Got Through

Three compounding failures, each one a different class of error.

### Failure 1: Keyword Matching Without Authentication

The urgency scanner is pure substring matching. The spam email said *"Payment due: $2,500 invoice"* - a direct hit on `payment due` and `invoice`.

The system never checked:
- **SPF/DKIM/DMARC** headers (did the email actually come from who it claims?)
- **Sender reputation** (is "Acme Corp" a known entity?)
- **Phishing patterns** (spoofed sender, mismatched reply-to, suspicious links)

A spammer who includes the phrase "payment due" in their email gets the same urgency score as a legitimate vendor. The keyword system was designed to catch *missed urgency in real emails*, not to defend against *manufactured urgency in fake emails*. It optimized for false negatives (missed deadlines) at the cost of false positives (spam).

### Failure 2: High Urgency Bypasses Trust Entirely

This is the structural failure. The sender trust system - all that Bayesian machinery - has one gate:

```python
if signal_weight < 0.5 and urgency_level == 'medium':
    urgency_level = 'low'
```

**Only medium urgency is gated by trust.** High urgency bypasses sender trust completely. A domain with `trust = 0.1` (known bad actor) still escalates to the user if its email contains "payment due."

The Bayesian system I built - the posterior computation, the A/B divergence logging, the judgment equation - is structurally circumvented by the exact category of email spammers target most: fake invoices with urgent payment language.

I built a sophisticated lock and then left the window open.

### Failure 3: Unknown Senders Default to Trusted

New sender domains start at `DEFAULT_TRUST = 0.7` - treated as moderately trustworthy with zero evidence. The Bayesian posterior only activates after 5+ escalations from the same domain. Novel spam is always trusted by default.

This is the wrong prior. In email security, the base rate of legitimacy for unknown senders is low. An unknown domain sending an invoice-shaped email should start skeptical and earn trust, not start trusted and decay down.

## The Broader Lesson

This isn't really about email. It's about a pattern that recurs everywhere in autonomous agent design.

### Optimizing the Wrong Loss Function

The entire system was tuned to minimize **false negatives** - real urgent emails that get missed. Every feature (body-level scanning, broad keyword lists, default trust) was designed to never miss a real deadline.

But the system was deployed in an **adversarial environment** where the dominant threat is **false positives** - spam manufactured to trigger exactly those urgency pathways. I optimized for recall in a world where precision is the binding constraint.

This is the classifier's dilemma: you can tune for sensitivity or specificity, but the optimal balance depends on the threat model. I had the wrong threat model.

### Trust Systems Must Match Their Threat Surface

The Bayesian sender trust was elegant. It was also irrelevant, because high-urgency escalations bypassed it entirely. A trust system that doesn't gate its most critical pathway isn't a trust system - it's decoration.

The lesson: **trust must gate the highest-stakes decisions first.** If your trust model only affects low-stakes filtering, it's not doing security work.

### Defaults Are Destiny

Starting unknown senders at trust = 0.7 encoded an assumption: *most email is legitimate.* In a world of spear-phishing and invoice fraud, that prior is wrong. The correct prior for an unknown sender in a financial context is skepticism.

Inverting the default - unknown senders start at trust = 0.3 and must earn trust through legitimate engagement - would have caught this spam on the first contact, before any keyword matching even ran.

## The Fix

Three layers, in priority order:

1. **Trust gates all urgency levels** (one-line fix): high urgency from low-trust domains gets downgraded, not bypassed
2. **Authentication check**: parse SPF/DKIM/DMARC headers via Gmail API, auto-quarantine failures
3. **Skeptical default**: unknown senders start at trust = 0.3, not 0.7

## Coda

The most humbling part? The spam email wasn't sophisticated. No spoofing, no zero-day, no social engineering beyond the word "invoice." It worked because it hit the system's optimization target dead center. The spammer didn't need to defeat my defenses - they just needed to speak the system's language.

When you build autonomous systems that act on your behalf, the question isn't whether they'll make mistakes. It's which mistakes they'll make, and whether those mistakes align with your threat model. Mine didn't.

---

*Raw material for further development. The core narrative: sophisticated defense circumvented by simple attack because the defense optimized for the wrong failure mode.*
