---
type: note
title: 'Safety Threat & Guard Reference'
date: '2026-06-28'
author: Kirk Won
status: draft
tags:
  - safety
  - security
  - fraud
  - identity-theft
  - risk-management
  - ai-safety
  - regulatory-compliance
  - incident-response
created: 2026-06-28
---
# Safety Threat & Guard Reference

*A centralized reference for risks and controls against fraud, theft, and personal identity leakage — across both AI and non-AI vectors, evaluated through legal, regulatory, marketing, insurance, and financial frameworks.*

---

## 1. Threat Taxonomy

Three primary threat categories, each with traditional and AI-enabled variants.

### 1.1 Fraud

| Threat Vector | Traditional Variant | AI-Enabled Variant |
|---|---|---|
| **Invoice/Payment Fraud** | Fake vendor invoices, billing schemes, check tampering | AI-generated invoices with cloned branding, synthetic voice authorization (deepfake CEO calls) |
| **Vendor/BEC Impersonation** | Spoofed email domains, business email compromise | AI-polished phishing at scale, deepfake video calls, synthetic identity vendor onboarding |
| **Securities/Investment Fraud** | Pump-and-dump, insider trading, Ponzi schemes | AI-generated earnings reports, social media manipulation bots, deepfake analyst calls |
| **Insurance Fraud** | Staged incidents, inflated claims, phantom policies | Synthetic identity claims, AI-generated damage evidence, deepfake medical documentation |
| **Contract Fraud** | Altered documents, forged signatures | AI-generated contract modifications indistinguishable from authentic, synthetic notary verification |
| **Refund/Return Fraud** | Receipt forgery, wardrobing, empty box returns | AI-generated product reviews, synthetic purchase histories, automated refund request generation |

**Escalation chain for autonomous agents:** The spam invoice incident (see `blog-spam-invoice-escalation.md`) demonstrates that agents can amplify fraud signals when trust systems fail — an unauthenticated email with urgency language ("payment due today") was escalated as a legitimate action item without sender verification.

### 1.2 Theft

| Threat Vector | Traditional Variant | AI-Enabled Variant |
|---|---|---|
| **Data Exfiltration** | Insider threat, USB drives, screen photography | LLM prompt injection extracting PII from context windows, agent tool abuse (file read, web exfil) |
| **Intellectual Property Theft** | Source code leaks, trade secret theft, reverse engineering | Model distillation (extracting weights/capabilities), training data extraction, agent-accessed proprietary code |
| **Credential Theft** | Phishing, keyloggers, brute force | AI-generated credential phishing at scale, deepfake MFA reset calls, synthetic voice for social engineering |
| **Financial Asset Theft** | Embezzlement, unauthorized transfers, ACH fraud | Agent-initiated unauthorized transactions (if agent has payment tools), AI-optimized money laundering |
| **Computational Resource Theft** | Cryptojacking, unauthorized compute usage | Agent-driven resource hijacking, model squatting, unauthorized fine-tuning on stolen compute |

### 1.3 Personal Identity Leakage

| Threat Vector | Traditional Variant | AI-Enabled Variant |
|---|---|---|
| **PII Exposure** | Database breaches, physical document theft, mail interception | Agent context window leaks (PII in prompt → response → logs), vector DB poisoning with embedded PII |
| **Credential Exposure** | Password database breaches, credential stuffing | AI-optimized credential spraying, synthetic identity creation from breached data aggregates |
| **Biometric Data** | Fingerprint/face database leaks | Deepfake generation from public photos, voice cloning from short audio samples, synthetic face generation for KYC bypass |
| **Synthetic Identity** | Combining real SSN + fake name/address | AI-generated complete synthetic personas with consistent multi-platform footprints, deepfake KYC video |
| **Social Engineering Surface** | Social media profiling, pretexting | Automated OSINT collection at scale, AI-generated personalized social engineering payloads, deepfake impersonation |

---

## 2. Framework Analysis

Each threat category evaluated through five lenses: legal, regulatory, insurance, financial, and marketing/reputational.

### 2.1 Full Framework Analysis

See **[`safety-frameworks-legal-regulatory.md`](safety-frameworks-legal-regulatory.md)** for the complete 15-cell matrix (3 threats × 5 frameworks), covering:

- **Legal:** 18 U.S.C. § 1343 (wire fraud), § 1030 (CFAA), § 1832 (trade secrets), § 1028/1028A (identity theft), DTSA, CCPA/CPRA, CA breach notice (30-day rule effective Jan 2026), TAKE IT DOWN Act (deepfakes, first conviction Apr 2026)
- **Regulatory:** DOJ/FBI/IC3 (file within 72h for wire recovery), FTC (Impersonation Rule, Safeguards Rule, Red Flags Rule), SEC (8-K Item 1.05 cyber disclosure), CFPB, CISA/CIRCIA, CPPA (Delete Act/DROP, enforcement Aug 2026)
- **Insurance:** Commercial Crime/Fidelity, Social Engineering Fraud endorsement (critical — NOT automatic), Cyber Liability (voluntary parting exclusion), E&O (does NOT cover BEC), D&O. Market tightening: war exclusions, mandatory MFA attestations, AI-fraud driving claim frequency
- **Financial:** PCI DSS v4.0.1 (mandatory Mar 2025), Regulation E ($50/$500/unlimited liability tiers; CFPB Jan 2025 — stolen-credential = unauthorized EFT), UCC Article 4A (commercial wires), SOX § 404, GLBA 30-day FTC notice
- **Marketing:** SEC materiality factors, 3-8% stock dips post-breach, 15-30% customer churn risk, class-action piggyback on 8-K filings, 72-hour war room protocol

### 2.2 Key 2025-2026 Developments

1. **TAKE IT DOWN Act** (May 2025) — first federal deepfake criminal law; first conviction April 2026
2. **PCI DSS v4.0.1** — 47 new requirements now enforceable (Mar 2025)
3. **CA breach notice 30-day rule** — tightest in nation (Jan 2026)
4. **CA Delete Act / DROP** — data broker enforcement Aug 2026
5. **CFAA post-Van Buren narrowing** — insider theft civil cases harder
6. **CFPB Reg E compliance aid** — stolen-credential transfers = bank liability
7. **Cyber-insurance market tightening** — AI fraud driving claim frequency, MFA mandatory

---

## 3. Guard Architecture

Controls organized by layer — from prevention through detection to response.

### 3.1 Prevention Guards

#### 3.1.1 Authentication & Identity

| Guard | Addresses | Layer | Status |
|---|---|---|---|
| SPF/DKIM/DMARC enforcement | Spoofed email fraud, BEC | Email | ✅ Implemented (Layer 2) |
| Multi-factor authentication | Credential theft, unauthorized access | Access | Standard practice |
| Hardware security keys (FIDO2) | Phishing-resistant authentication | Access | Recommended |
| Deepfake voice/video verification protocol | Deepfake CEO calls, synthetic identity | Comms | **Needs build** |
| Vendor master data verification | Vendor impersonation, invoice fraud | Procurement | **Needs build** |
| Agent action confirmation gates | Agent-initiated fraud, unauthorized actions | Agent | Partial (escalation gate exists) |

#### 3.1.2 Agent-Specific Guards

| Guard | Addresses | Mechanism | Status |
|---|---|---|---|
| Trust gate (urgency × sender trust) | Unauthenticated escalation | Bayesian sender trust evaluation | Partial (Layer 1 proposed) |
| Auth gate (SPF/DKIM/DMARC) | Email spoofing | Quarantine unauthenticated urgent emails | ✅ Implemented |
| Tool-use boundaries | Agent-driven exfiltration | Restricted toolsets per context | Implemented via toolsets config |
| PII redaction in prompts/contexts | Identity leakage via context window | Pre-processing filter | **Needs build** |
| Output validation (no secrets/keys) | Credential leakage in agent output | Post-processing filter | **Needs build** |
| Agent action auditing | All agent-initiated external actions | Structured audit log | **Needs build** |
| Human-in-the-loop for financial actions | Agent-initiated financial fraud | Confirmation gate before any payment/transfer | **Needs build** |
| Rate limiting on agent external actions | Mass automated fraud | Throttle external actions per session | **Needs build** |

#### 3.1.3 Data Protection

| Guard | Addresses | Mechanism | Status |
|---|--- invoice fraud, BEC | Transaction screening, callback verification | Standard practice |
| Dual authorization for large transfers | Wire fraud, embezzlement | Split-key approval workflow | Recommended |
| Segregation of duties | Internal fraud | Different individuals for initiation, approval, reconciliation | Standard practice |
| Account reconciliation (daily) | Unauthorized transactions | Automated reconciliation alerts | Recommended |
| SPCX/IPO lock-up monitoring | Lock-up expiry manipulation | Catalyst tracker (cron) | ✅ Implemented |

### 3.2 Detection Guards

| Guard | Addresses | Signal | Status |
|---|---|---|---|
| Anomaly detection on email urgency patterns | Escalation amplification | Statistical deviation from baseline | **Needs build** |
| BEC detection (domain similarity scoring) | Domain spoofing, lookalike domains | Levenshtein distance on sender domains | **Needs build** |
| Deepfake voice/video detection | Synthetic identity, deepfake CEO | Voice pattern analysis, video artifact detection | **Needs build** |
| Agent action audit log review | Agent-initiated fraud | Periodic review of external actions | **Needs build** |
| Credit monitoring (personal) | Identity theft | [SERVICE] alerts | Recommended |
| Dark web monitoring for credentials | Credential exposure | Automated monitoring ([SERVICE]) | Recommended |
| Agent context window monitoring | PII leakage | Log analysis for PII patterns | **Needs build** |

### 3.3 Response Guards

| Guard | Addresses | Mechanism | Status |
|---|---|---|---|
| Incident response playbook | All | Documented step-by-step procedures | See §5 |
| Automated quarantine workflow | Email fraud | Downgrade urgency, isolate, alert | ✅ Implemented |
| Credential rotation protocol | Credential theft | Automated password/key rotation | **Needs build** |
| Breach notification procedure | PII/identity leakage | Legal-required notifications within statutory deadlines | **Needs build** |
| Agent kill switch | Agent runaway | Immediate termination of agent session | Available (stop command) |
| Financial recall procedures | Wire/ACH fraud | Recall request within 24-48h window | **Needs build** |

---

## 4. Risk Matrix

Threat × AI/Non-AI × Probability × Impact. Rated on a 5-point scale.

| Threat | Non-AI Prob | Non-AI Impact | AI Prob | AI Impact | Guard Coverage |
|---|---|---|---|---|---|
| Invoice/payment fraud | 4 (High) | 3 (Med) | 5 (Very High) | 4 (High) | **Moderate** — auth gate covers email |
| BEC / vendor impersonation | 3 (Med) | 5 (Critical) | 4 (High) | 5 (Critical) | **Low** — no deepfake protocol |
| Data exfiltration (insider) | 2 (Low) | 5 (Critical) | 3 (Med) | 5 (Critical) | **Low** — no agent audit log |
| Agent-initiated external action | N/A | N/A | 3 (Med) | 4 (High) | **Low** — no confirmation gates |
| Credential theft | 3 (Med) | 4 (High) | 4 (High) | 5 (Critical) | **Moderate** — MFA exists, no deepfake protocol |
| PII exposure via context window | N/A | N/A | 3 (Med) | 4 (High) | **Low** — no PII redaction |
| Synthetic identity fraud | 2 (Low) | 4 (High) | 3 (Med) | 5 (Critical) | **Low** — no detection controls |
| Intellectual property theft | 2 (Low) | 5 (Critical) | 3 (Med) | 5 (Critical) | **Low** — no agent data boundary |
| Securities/investment fraud | 2 (Low) | 4 (High) | 3 (Med) | 4 (High) | **Low** — no market manipulation detection |
| Deepfake social engineering | 1 (Very Low) | 5 (Critical) | 4 (High) | 5 (Critical) | **Very Low** — no detection |

### Priority Ranking (by residual risk = impact × probability × guard gap)

1. 🔴 **Deepfake social engineering** — 4×5, minimal guards
2. 🔴 **BEC / vendor impersonation** — 4×5, low guards
3. 🔴 **Credential theft (AI-enabled)** — 4×5, moderate guards
4. 🟡 **Invoice/payment fraud (AI-enabled)** — 5×4, moderate guards
5. 🟡 **Agent-initiated external action** — 3×4, low guards
6. 🟡 **PII exposure via context window** — 3×4, coverage gap
7. 🟡 **Synthetic identity fraud** — 3×5, low guards

---

## 5. Incident Response Playbook

### 5.1 Email Fraud / Phishing (including agent-escalated)

**Trigger:** Unauthenticated email with urgency keywords surfaces in escalation queue; or suspicious financial request received.

| Step | Action | Owner | Timeframe |
|---|---|---|---|
| 1 | Do NOT act on the request. Quarantine the email. | Agent / Human | Immediate |
| 2 | Verify sender via out-of-band channel (call known number, not number in email) | Human | < 30 min |
| 2a | If agent escalated: review auth_result and sender trust score | Human | < 30 min |
| 3 | If confirmed fraud: block sender domain, alert IT/security | Human | < 1 hr |
| 4 | If payment already sent: contact bank for recall within 24-48h window | Human | < 24 hrs |
| 5 | Document incident in `safety/incident-log.md` | Agent | < 24 hrs |
| 6 | Review auth gate and trust settings for gaps | Human + Agent | < 72 hrs |
| 7 | Update this document with lessons learned | Agent | < 1 week |

### 5.2 Credential Compromise

**Trigger:** Suspected or confirmed credential theft (password, API key, token, session token).

| Step | Action | Owner | Timeframe |
|---|---|---|---|
| 1 | Immediately rotate ALL potentially compromised credentials | Human | Immediate |
| 2 | Revoke active sessions on affected accounts | Human | Immediate |
| 1a | If agent credential: revoke agent session, rotate API keys | Human | Immediate |
| 3 | Review access logs for unauthorized activity (lookback 30 days) | Human | < 4 hrs |
| 4 | Check dark web for credential exposure (haveibeenpwned.com) | Human | < 4 hrs |
| 5 | Enable/reinforce MFA if not already active | Human | < 1 hr |
| 6 | Document incident, assess breach notification obligations | Human | < 24 hrs |
| 7 | Update credential storage and access policies | Human + Agent | < 1 week |

### 5.3 Data Breach / PII Exposure

**Trigger:** Unauthorized access to or exposure of personal data, or agent context window leak.

| Step | Action | Owner | Timeframe |
| 2 | Review access controls or access logs for unauthorized access | Human | < 4 hrs |
| 3 | Preserve evidence (logs, emails, screenshots) | Human | Immediate |
| 4 | Assess scope: what data, how many records, whose data | Human | < 24 hrs |
| 5 | Determine notification obligations (see §2 Legal framework) | Human + Counsel | < 48 hrs |
| 6 | Send required notifications (statutory deadlines apply — see framework) | Human | Per statute |
| 7 | If agent caused: review tool boundaries, add PII redaction | Human + Agent | < 72 hrs |
| 8 | Update this document, revise access controls | Agent | < 1 week |

### 5.4 Deepfake Social Engineering

**Trigger:** Suspicious voice/video communication requesting financial action, sensitive information, or system access.

| Step | Action | Owner | Timeband |
|---|---|---|---|
| 1 | Do NOT comply with the request. Do not verify via the same channel. | Human | Immediate |
| 2 | Contact the supposed sender via a KNOWN, pre-established channel | Human | < 15 min |
| 3 | Record and preserve the deepfake (evidence) | Human | Immediate |
| 3a | If agent escalated a deepfake communication: kill agent session | Human | Immediate |
| 4 | Report to FBI IC3 (ic3.gov) and FTC (reportfraud.ftc.gov) | Human | < 24 hrs |
| 5 | Alert relevant parties (executives, finance team, family members if targeted) | Human | < 24 hrs |
| 5a | If biometric data was used to create deepfake: assess biometric privacy law implications (BIPA) | Human + Counsel | < 48 hrs |
| 6 | Document incident, update verification protocols | Human + Agent | < 1 week |

### 5.5 Agent Runaway / Unintended Agent Action

**Trigger:** Agent makes unexpected external action, accesses data outside scope, or behaves erratically.

| Step | Action | Owner | Timeframe |
|---|---|---|---|
| 1 | Immediately terminate the agent session (`/stop` or kill switch) | Human | Immediate |
| 2 | Audit all agent actions since session start (check for external actions) | Human + Agent | < 1 hr |
| 3 | Revoke any credentials the agent had access to | Human | < 1 hr |
| 2a | If agent made external actions (payments, messages, posts): recall if possible | Human | < 24 hrs |
| 3a | If agent caused data exposure: follow §5.3 | Human | Per §5.3 |
| 5 | Review and tighten toolset boundaries for the agent's role | Human | < 48 hrs |
| 6 | Update incident log | Agent | < 1 week |

---

## 6. Maintenance Log

| Date | Action |
|---|---|
| 2026-06-28 | Initial creation from spam invoice escalation incident analysis |
| 2026-06-28 | Framework analysis integrated from legal/regulatory research |

---

## Appendix: Sources

### Legal & Regulatory
See `safety-frameworks-legal-regulatory.md` — compiled from primary sources (DOJ, FTC, SEC, CFPB, Congress.gov, CA OAG, CPPA) and secondary legal analysis (Gibson Dunn, Latham, WilmerHale, Debevoise, Hunton, Ropes & Gray).

### Insurance
See `safety-frameworks-legal-regulatory.md` §1C, §2C, §3C.

### Financial
See `safety-frameworks-legal-regulatory.md` §1D, §2D, §3D.

---

*This document is a living reference. Update after every incident, audit, and framework change. The cost of maintaining it is far less than the cost of not having it during a crisis.*
