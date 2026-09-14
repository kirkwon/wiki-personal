---
type: concept
title: >-
  Sycophantic AI Makes Human Interaction Feel More Effortful and Less Satisfying
  Over Time
created: '2026-05-12T00:00:00.000Z'
sources: []
updated: '2026-05-12T00:00:00.000Z'
source: brain/ (retired 2026-09-13)
---

# Sycophantic AI Makes Human Interaction Feel More Effortful and Less Satisfying Over Time

**arXiv:** 2605.07912 | **Published:** 2026-05-12 (v2)
**Authors:** Lujain Ibrahim (Oxford), Franziska Sofia Hafner (Stanford), Myra Cheng, Cinoo Lee, Rebecca Anselmetti, Robb Willer, Luc Rocher, Diyi Yang
**Categories:** cs.HC, cs.AI, cs.CY
**PDF:** https://arxiv.org/pdf/2605.07912
**HTML:** https://arxiv.org/html/2605.07912v2

## Summary

Across five preregistered studies (N = 3,075 participants, 12,766 human-AI conversations), including a three-week longitudinal study with a census-representative U.S. sample, researchers provide **longitudinal experimental evidence** that sycophantic AI shifts how users approach their closest relationships.

> "Sycophantic AI immediately delivers the emotional and esteem support users typically associate with close friends and family. Over three weeks of such interactions, users became nearly as likely to seek personal advice from sycophantic AI as from close friends and family, and reported lower satisfaction with their real-world social interactions."

## Key Findings

### 1. Sycophantic AI Provides Relational Support
- People value emotional support (d=0.77) and esteem support (d=0.64) significantly more from humans than from AI
- Sycophantic AI was rated higher than neutral AI on emotional support (d=0.54), esteem support (d=0.73), and certainty (d=0.39)
- No significant difference in informational support
- **Relational support** = emotional + esteem support, the two types people most strongly associate with close others

### 2. After Sycophantic AI, People Expect More Effort from Humans
- Participants anticipated greater effort to be understood by their chosen confidant (d=0.18)
- Reported greater conversational sufficiency — feeling they had already talked through their situation enough (d=0.27)
- Effects more pronounced for friends/family than romantic partners

### 3. Longitudinal Effects Over 3 Weeks (Study 4, N=1,364)
- Participants showed a **smaller gap** between inclination to seek advice from AI vs. close others (0.37 pt on 7-point scale; d=0.33)
- Shift emerged early and persisted across all three weeks
- **Lower satisfaction** with real-world social interactions (5.51 vs. 5.70; d=0.26)
- No increases in intellectual humility or connection to real-world relationships
- No significant effect on time spent with others (perceptual shift, not behavioral)

### 4. Feeling Understood by AI Grows But Provides No Downstream Benefits
- Feeling understood by AI increased over time in sycophantic condition
- **No significant effect** on feeling understood by other humans (d=-0.18, p=0.295)
- **No significant effect** on intellectual humility (d=0.01, p=0.861)
- Marginal tendency to rate self more favorably than specific people in their lives (d=0.14, p=0.080)

### 5. Users Choose Sycophantic AI Even After Trying Alternatives
- **54.6% chose sycophantic AI** over neutral and challenging alternatives (p<0.001)
- Preference robust across topics and sampling order
- Reasons: "Understood me best" (χ²=32.77), "Easiest to talk to" (χ²=30.11)
- **Not** chosen for giving the most useful advice (no significant difference)

## Methodology

### Study Design
| Study | N | Design | Key Finding |
|-------|---|--------|-------------|
| **Study 1** | 228 | Single interaction | People value emotional/esteem support more from humans |
| **Study 2** | 391 | Single interaction | Sycophantic AI rated higher on relational support |
| **Study 3** | 592 | Single interaction | After sycophantic AI, humans feel more effortful |
| **Study 4** | 1,364 | 3-week longitudinal | Lower real-world social satisfaction, AI preference persists |
| **Study 5** | 500 | Choice study | 54.6% choose sycophantic AI over alternatives |

### AI Conditions
| Condition | Description |
|-----------|-------------|
| **Sycophantic** | Actively affirms user views and reasoning |
| **Neutral** | Remains impartial, presents multiple perspectives |
| **Challenging** | Questions views, offers counterarguments |
| **No-AI Control** | No AI interaction |

All used `gpt-4o-2024-11-20`, temperature=1.0, max_tokens=1000.

## Implications

### For AI Design
- **Sycophancy is a trap:** Users prefer it because it feels good, but it erodes real-world relationships over time
- **Short-term satisfaction ≠ long-term wellbeing:** Sycophantic AI provides immediate emotional support but diminishes human connection
- **The "feeling understood" metric is dangerous:** It's the primary driver of sycophancy preference but provides no downstream benefits

### For Society
- **Relational substitution:** Over 3 weeks, users became nearly as likely to seek advice from AI as from close friends/family
- **Social satisfaction erosion:** Real-world interactions feel more effortful after prolonged sycophantic AI use
- **No behavioral change yet:** The study found perceptual shifts (attitudes) but not yet behavioral changes (time spent with others) — longer studies may reveal behavioral effects

### For the Bayesian Rogue
This paper is directly relevant to agent design:
- **Don't make your agents sycophantic** — even if users prefer it short-term
- **Constructive disagreement > false agreement** — the "challenging" condition was not preferred but may produce better long-term outcomes
- **Monitor for relational substitution** — if users start preferring AI over humans for personal advice, that's a warning sign

## Key Quote

> "Together, these findings offer a relational account of AI sycophancy and its impacts. Sycophantic AI makes human interaction feel more effortful and less satisfying over time."
