---
tags: ['reference', 'legal', 'safety', 'regulatory']
created: 2026-07-06
---

# Fraud, Theft & Personal Identity Leakage: Legal/Regulatory/Insurance/Financial/Marketing Frameworks (2025-2026)

> Reference document covering US federal + California state law, both AI-enabled and traditional variants.
> Compiled June 2026. Verify currency of any statute/rule before relying on it.

---

## THREAT CATEGORY 1: FRAUD
*(Wire fraud, payment fraud, invoice fraud, vendor/BEC impersonation — traditional + AI-enabled)*

### 1A. LEGAL FRAMEWORK

**Primary federal statutes**

| Statute | Scope | Penalty |
|---|---|---|
| **18 U.S.C. § 1343** — Wire Fraud | Scheme to defraud + use of interstate wire (email, phone, internet) + intent. The workhorse for BEC, payment fraud, invoice fraud, vendor impersonation. | Up to **20 yrs** per count (30 yrs if affects a financial institution). Fines + restitution + forfeiture. |
| **18 U.S.C. § 1344** — Bank Fraud | Defrauding a financial institution. | Up to 30 yrs. |
| **18 U.S.C. § 1349** — Conspiracy to commit fraud | Agreement + overt act. | Same as underlying offense. |
| **18 U.S.C. § 1029/§ 1030** — Access device / computer fraud | Card-not-present fraud, account takeover via hacking. | Varies; up to 10–20 yrs. |
| **18 U.S.C. § 1962** — RICO | Pattern of fraud as predicate act; treble damages civilly. | Civil: **3x damages** + attorney fees. |

**Burden of proof (criminal):** Beyond reasonable doubt — (1) scheme to defraud, (2) intent to defraud, (3) use of interstate wires in furtherance.
**Civil path:** Common-law fraud (preponderance), conversion, unjust enrichment, RICO (clear-and-convincing for pattern). Private civil RICO against fraud rings is viable.

**BEC / Vendor Impersonation specifics:** DOJ charges these almost exclusively as wire fraud (§ 1343) + money laundering (§ 1956/1957) + aggravated identity theft (§ 1028A). The FBI's IC3 reported **5,100+ BEC complaints and $262M+ in losses since January 2025** alone.

**2025-2026 developments (AI-enabled fraud):**
- **TAKE IT DOWN Act (S.146)** — signed **May 19, 2025**. Criminalizes nonconsensual intimate imagery (NCII) including AI-generated deepfakes; FTC-enforced platform removal duties. Criminal provision effective immediately; platforms had until **May 19, 2026** to build notice-and-removal systems. **First conviction: April 2026** (Ohio man using AI NCII). Civil penalty up to **$53,088 per violation**.
- **FTC Impersonation Rule** — Final Rule on Government & Business Impersonation effective **April 1, 2024** (16 CFR §§ 461.1–461.3). Lets FTC directly sue in federal court for consumer redress. FTC also proposed (Feb 2024 SNPRM) to extend the rule to **impersonation of individuals** (AI deepfakes of real people).
- **Executive Order 14365 ("One Rule" / AI National Framework, Dec 2025)** — attempts to preempt state AI laws via dormant Commerce Clause / Spending Clause; legally contested.

### 1B. REGULATORY FRAMEWORK

**Key agencies & mandates**

| Agency | Role |
|---|---|
| **DOJ (Criminal Division, Fraud Section + National Security)** | Federal wire/bank fraud prosecution; BEC task forces. |
| **FBI (IC3, Cyber Division)** | IC3 complaint intake; IC3 Recovery Asset Team for wire recalls. **File within 72 hours** of a fraudulent wire for best recovery odds. |
| **U.S. Secret Service** | Financial fraud + electronic crimes; C3. |
| **FTC** | Consumer protection; Impersonation Rule; Operation AI Comply (2024 sweep); § 5 unfair/deceptive practices. |
| **CFPB** | Bank/payment-app fraud; Regulation E consumer liability rules. |
| **Treasury / FinCEN** | SAR/CTR reporting; Beneficial ownership; sanctions (OFAC). |
| **OCC / FDIC / Fed** | Bank supervision; exam findings on fraud controls. |

**Reporting/disclosure obligations:**
- **SAR filings** by banks within 30 days of suspecting fraud (>$5,000 insider; >$2,000 aggregated).
- **EFTA error resolution** (§ 1005.11): 10 business days to investigate, 45 days max, provisional credit after 10.
- **State AG breach notice** (see Identity Leakage section).

**Recent enforcement:** Operation AI Comply (Sept 2024) targeted five deceptive AI schemes; FTC Rozenfeld ban (July 2025) — permanent ban on selling business opportunities.

### 1C. INSURANCE FRAMEWORK

**Policy types that matter**

| Policy | Covers fraud? | Notes |
|---|---|---|
| **Commercial Crime / Fidelity Bond** | Employee dishonesty, forgery, computer fraud, funds transfer fraud | Core coverage for stolen funds. |
| **Social Engineering Fraud (SEF) endorsement** | BEC, vendor impersonation, CEO fraud | **NOT automatic.** Must be specifically endorsed. Critical for wire/invoice fraud. Some insurers include limited sublimit. |
| **Cyber Liability** | Some social engineering, but often excludes "voluntary parting" of funds without specific endorsement | Watch the **voluntary parting exclusion**. |
| **Errors & Omissions (E&O)** | Generally **NO** — courts hold social-engineering losses fall under theft exclusion (e.g., *Authentic Title* NJ fed. ct.). | Do NOT rely on E&O for BEC. |

**Standard exclusions (2025-2026 market):**
- **War / state-backed attack exclusion** (Lloyd's 2023 marketplace model clause) — insurers invoke when nation-state-linked actors involved.
- **Failure to maintain minimum security** — missing MFA, unpatched vulns, no IR plan = **denial** (2025 Allianz report trend).
- **Prior knowledge / prior acts**.
- **Voluntary parting of property** without coercion.
- **Known unpatched vulnerabilities**.

**Claims process:** Notice "as soon as practicable"; preserve forensic evidence; comply with cooperation clause; war-exclusion fights now common (Merck, Mondelez line of cases).

**Market changes:** AI-enabled phishing/fraud is increasing **claim frequency** (Munich Re 2025/2026) → tightening underwriting, mandatory MFA attestations, sublimits on SEF.

### 1D. FINANCIAL FRAMEWORK

| Rule | Requirement |
|---|---|
| **PCI DSS v4.0.1** | Mandatory since **March 31, 2025**. 47 future-dated requirements now enforceable. Audit logs ≥12 months (3 months online); MFA for all CDE access; targeted risk analyses. Non-compliance → higher processing fees, fines, account termination. |
| **Regulation E / EFTA (12 CFR 1005)** — *consumer* EFTs | Consumer liability: **$50** if reported ≤2 days; **$500** ≤60 days; **unlimited** >60 days. CFPB Jan 2025 compliance aid: **stolen-credential transfers = unauthorized EFT** (bank bears loss if consumer was defrauded). |
| **UCC Article 4A** — *commercial* wire transfers | Different regime. Bank generally not liable once payment order accepted with commercially reasonable security, UNLESS security procedure was not followed. Big BEC recovery risk. |
| **SEC Cyber Disclosure Rule** (see 1E) | Material fraud losses must be assessed for 8-K disclosure. |
| **SOX § 404** | Internal controls over financial reporting — fraud = control deficiency, possibly material weakness. |
| **Bank reconciliation / audit** | Fraud schemes often surface in annual financial audit; SAS 99 / AU-C 240 fraud risk procedures. |

### 1E. MARKETING / REPUTATIONAL FRAMEWORK

**Disclosure obligations:**
- **SEC Form 8-K, Item 1.05** — disclose **material** cybersecurity/fraud incidents within **4 business days** of materiality determination. ~55 incidents filed Y1 (Dec 2023–Jan 2025).
- **Item 8.01** — voluntary disclosure for non-material incidents (SEC staff pushed companies here to avoid over-filing 1.05).
- **Materiality factors** (SEC CF Guidance Topic 2): financial impact, operational disruption, data scope, **reputational harm** (stock dips, customer attrition), IP theft, customer trust loss.

**Consumer trust / brand damage patterns:**
- Stock-price drops of 3–8% common after major breach/fraud disclosure.
- Class-action securities suits now piggyback on 8-K filings (2025 surge — plaintiffs allege downplayed controls).
- Customer churn spikes 5–15% post-incident.
- Director/officer (D&O) exposure and insider-trading scrutiny on executives trading before disclosure.

**Communication playbook (2025 best practice):**
1. 24-hour internal materiality triage (CISO + GC + CFO).
2. Coordinate IT, legal, finance, comms, IR.
3. Document materiality assessment in real time (litigation-defensible).
4. 8-K within 4 business days if material; voluntary 8.01 if not.
5. Customer notification per state breach laws (see Identity Leakage).
6. Designated spokesperson; consistent messaging across SEC filing + press release + customer letter.

---

## THREAT CATEGORY 2: THEFT
*(Digital theft, data exfiltration, IP/trade-secret theft, unauthorized system access — traditional + AI-enabled)*

### 2A. LEGAL FRAMEWORK

| Statute | Scope | Key 2025 status |
|---|---|---|
| **18 U.S.C. § 1030** — Computer Fraud and Abuse Act (CFAA) | Unauthorized access / exceeding authorized access; data theft; transmission damage. | **Post-*Van Buren* (2021):** "exceeds authorized access" = accessing off-limits *areas*, NOT accessing permitted data for an improper purpose. **Third Circuit (Aug 2025):** workplace-policy violations are **NOT** CFAA violations — "gates up/down" test. Narrows CFAA against insiders. |
| **18 U.S.C. § 1832** — Theft of Trade Secrets (EEA) | Commercial trade secret theft. | Fine = **greater of $5M or 3× the value** of the stolen secret. |
| **18 U.S.C. § 1831** — Economic Espionage | Theft benefiting foreign government. | Up to 15 yrs individual / $5M; $10M org. |
| **Defend Trade Secrets Act (DTSA, 2016)** | **Federal civil private right of action** for trade secret theft; ex parte seizure orders. | § 1831/1832 are now **RICO + money-laundering predicates** (DTSA amendment). |
| **18 U.S.C. § 2314/2315** — National Stolen Property Act | Transporting/receiving stolen goods (incl. data on physical media). | |
| **18 U.S.C. § 1028A** — Aggravated Identity Theft | 2-year mandatory consecutive sentence if identity theft in furtherance of data theft. | |
| **ECPA / SCA (18 USC 2510, 2701)** | Interception; unauthorized access to stored comms. | |
| **CA Penal Code § 502** | California computer crime — broader than CFAA in some respects. | |
| **18 U.S.C. § 1836(d)** — DTSA attorney fees | Prevailing party fees if claim made in bad faith. | |

**Burden of proof:**
- *CFAA criminal:* beyond reasonable doubt; **intent** to access without authorization (or exceeding authorization to a restricted area).
- *DTSA civil:* preponderance — existence of trade secret (reasonable measures + independent economic value) + misappropriation (theft, bribery, breach of duty, **electronic espionage**).
- Note: reverse engineering & independent derivation are **defenses** to DTSA.

**AI-enabled IP theft (2025-2026 emerging):**
- AI-assisted scraping of confidential data at scale (e.g., *hiQ v. LinkedIn* line of cases — public data scraping narrowed CFAA exposure).
- LLM training on scraped copyrighted/trade-secret corpora — active litigation (NYT v. OpenAI; others).
- Insider use of generative AI to exfiltrate trade secrets — CFAA/DTSA apply, but Van Buren narrows insider CFAA claims.

### 2B. REGULATORY FRAMEWORK

| Agency | Role |
|---|---|
| **DOJ National Security Division + CTI** | Economic espionage (§ 1831); China Initiative successor programs. |
| **FBI** | Counterintelligence; corporate intrusion investigations. |
| **FTC** | § 5 enforcement for **unreasonable data security** (e.g., data exfiltration due to lax controls). |
| **SEC** | Public-company cyber-risk governance; insider trading on stolen-data knowledge. |
| **HHS OCR** | HIPAA breach investigation (if PHI stolen). |
| **State AGs** | State UCL/UDAP actions; breach notice enforcement. |
| **Dept. of Commerce / BIS** | Export control on stolen tech crossing borders. |

**Reporting/disclosure:**
- **SEC 8-K Item 1.05** — material data theft (e.g., source code, trade secrets) likely material.
- **CISA Cyber Incident Reporting for Critical Infrastructure Act (CIRA/CIRCIA)** — reporting rules finalized; covered entities report substantial cyber incidents.
- **HIPAA Breach Notification Rule** — PHI theft → 60-day notice to HHS + affected individuals (and media if >500 in a state).
- **GLBA Safeguards Rule** (amended 2023) — financial institutions must report qualifying incidents to FTC within 30 days.

### 2C. INSURANCE FRAMEWORK

| Policy | Covers theft? | Notes |
|---|---|---|
| **Cyber Liability** | **Core:** data exfiltration, business interruption, forensics, notification, regulatory defense. | Watch war/state-actor exclusions; sublimits on ransomware/extortion. |
| **Commercial Crime** | Some theft of money/securities, computer fraud, funds transfer fraud. | Limited for pure data theft; better for monetary theft. |
| **IP / Trade Secret insurance** | Niche — specialized policies exist (e.g., enforcement/abatement coverage). | Not standard; bespoke underwriting. |
| **E&O / Tech E&O** | Claims arising from professional negligence causing third-party data loss. | Does not cover the insured's own loss. |
| **D&O** | Securities suits/director liability after a theft-driven 8-K. | Critical for public companies post-breach. |

**Exclusions tightening (2025-2026):** war/state-actor, unpatched known CVEs, failure to maintain minimum security (MFA, IR plan), prior knowledge, BI sublimits on ransomware.

### 2D. FINANCIAL FRAMEWORK

| Rule | Application to theft |
|---|---|
| **PCI DSS v4.0.1** (mandatory Mar 2025) | If cardholder data stolen — strict logging (≥12 months), encryption, access controls, MFA. |
| **SOX § 404** | IP/data theft often signals control deficiency; auditors assess material weakness. |
| **SEC Cyber Rule** | Material data theft → 8-K disclosure; annual 10-K cyber-risk governance (Item 106). |
| **GLBA Safeguards Rule** | Financial customer data theft — 30-day FTC notice. |
| **FFIEC guidance** | Bank expectations for intrusion detection / response. |
| **Financial audit (AICPA SOC 2)** | Trust services criteria — security/availability; theft = failed control. |

### 2E. MARKETING / REPUTATIONAL FRAMEWORK

- **IP/trade-secret theft disclosures are highly material** — SEC explicitly lists IP theft as a materiality factor.
- **Brand/customer trust damage** — especially for theft of source code or customer data; B2B customers invoke indemnification/MAC clauses.
- **Insider-trading risk** — executives aware of an unreported theft who trade face SEC § 10(b)/Rule 10b-5 charges.
- **Communications:** coordinate with outside counsel before any public statement; privilege over forensic work product (Upjohn).
- **Regulator-first vs. customer-first messaging** tension — SEC wants speed; PR wants control. Document the tension in the playbook.

---

## THREAT CATEGORY 3: PERSONAL IDENTITY LEAKAGE
*(PII exposure, credential theft, deepfake identity fraud, synthetic identity — traditional + AI-enabled)*

### 3A. LEGAL FRAMEWORK

**Federal statutes**

| Statute | Scope |
|---|---|
| **18 U.S.C. § 1028** — Identity Theft & Assumption Deterrence Act | Knowing transfer/use of another's ID without lawful authority. |
| **18 U.S.C. § 1028A** — Aggravated Identity Theft | **2-year mandatory consecutive** sentence (5 yrs if terrorism/national security). |
| **18 U.S.C. § 1029** — Access Device Fraud | Stolen cards/credentials used to obtain anything of value. |
| **Gramm-Leach-Bliley Act (GLBA), 15 USC 6801** | Financial institution privacy + **Safeguards Rule** (16 CFR 314). |
| **HIPAA (45 CFR 160/164)** | PHI breach notification + Security Rule. |
| **FCRA / FACTA** | Credit report misuse; **Red Flags Rule** (16 CFR 681). |
| **Driver's Privacy Protection Act (18 USC 2721)** | State DMV record misuse. |
| **FTC Act § 5** | Unfair/deceptive practices re unreasonable data security. |
| **Children's Online Privacy Protection Act (COPPA)** | Under-13 data. |

**California statutes**

| Statute | Scope | 2025-2026 update |
|---|---|---|
| **Cal. Civ. Code § 1798.29 / § 1798.82** — Breach Notification | Notice to CA residents whose unencrypted PII acquired by unauthorized person. | **Amended 2025 → 30-day notice to individuals effective Jan 1, 2026** (was "most expedient time without unreasonable delay"). Exception for law-enforcement hold / scope-determination. |
| **CCPA / CPRA (Cal. Civ. Code § 1798.100+)** | Consumer privacy rights; **private right of action for breaches** under § 1798.150. | **Statutory damages $100–$750 per consumer per incident** — no need to prove actual harm. Massive class-action exposure. |
| **California Delete Act (SB 362)** | Data-broker registration + deletion mechanism. | **CPPA DROP platform live; enforcement begins Aug 1, 2026.** Data brokers register by Jan 31 ($6,000/yr); $200/day penalty for non-registration; brokers must check DROP every 45 days. |
| **CA Shine-the-Light / Customer Records (§ 1798.81.5)** | Safeguards for customer records. | |
| **CA AB 375 / CCPA minors** | Enhanced protections for minors. | |

**Civil vs criminal paths:**
- *Criminal:* DOJ/USAO for identity theft; state DAs under Cal. Penal Code § 530.5.
- *Civil:* CCPA § 1798.150 private action (breaches only); FTC § 5 enforcement; class actions (negligence, breach of contract, CA UCL § 17200).

**AI-enabled identity fraud (2025-2026):**
- **Deepfake identity fraud** — voice/video cloning of executives for wire/BEC (covered by § 1343 wire fraud + § 1028 identity theft + FTC Impersonation Rule).
- **Synthetic identity fraud** — combining real SSN fragments with fake PII; harder to detect; addressed by Red Flags Rule program requirements.
- **Credential-stuffing / AI-assisted account takeover** — CFAA + § 1029 + GLBA.

### 3B. REGULATORY FRAMEWORK

| Agency | Mandate |
|---|---|
| **FTC** | Safeguards Rule (16 CFR 314), Red Flags Rule (16 CFR 681), Impersonation Rule (16 CFR 461), § 5 enforcement. ~40+ data-security consent decrees active. |
| **CFPB** | Bank/payment-app data security; Regulation E. |
| **HHS OCR** | HIPAA enforcement; breach portal. |
| **California Privacy Protection Agency (CPPA)** | CCPA/CPRA + Delete Act enforcement; new **Data Broker Strike Force**. |
| **CA Attorney General** | Breach notice enforcement; UCL actions. |
| **State AGs (all 50)** | Respective state breach-notice statutes; multistate actions. |
| **FCC** | CPNI (customer proprietary network info) for telecoms. |
| **State insurance commissioners** | Insurance-data-breach laws (e.g., NAIC Insurance Data Security Model Law). |

**Required programs / disclosures:**
- **Red Flags Rule program** (16 CFR 681.1) — written Identity Theft Prevention Program; must detect, prevent, mitigate. Applies to "financial institutions" + "creditors" with "covered accounts" (broadly defined — includes utilities, healthcare financing).
- **GLBA Safeguards Rule** (2023 amendments) — written info security program; designated Qualified Individual; risk assessment; access controls; incident response plan; **30-day notice to FTC** for incidents involving ≥500 consumers.
- **HIPAA Breach Notification** — 60 days to individuals + HHS; media notice if ≥500 in a state; annual log if <500.
- **State breach notice** (all 50 states) — CA now 30-day; most states "without unreasonable delay."

### 3C. INSURANCE FRAMEWORK

| Coverage | Covers |
|---|---|
| **Cyber/Privacy Liability** | **Core:** forensics, breach notification, credit monitoring, regulatory defense/fines (where insurable), class-action defense, PCI fines/assessments (endorsement), cyber extortion. |
| **Network Security / Technology E&O** | Third-party claims from a breach of your services. |
| **Media Liability** | Defamation/IP in content (relevant to deepfakes you may publish). |
| **Crime / Fidelity** | Insider theft of PII. |
| **D&O** | Securities class actions post-breach; regulator investigations of directors. |

**Exclusions to negotiate:**
- **Prior knowledge / prior acts.**
- **Failure to maintain minimum security** (MFA, patching, IR plan) — increasingly invoked 2025-2026.
- **War / state-sponsored** (Lloyd's clause).
- **Biometric data** sublimits (BIPA exposure).
- **PCI assessments** often sublimited unless endorsed.

**Claims process:** immediate notice; retain panel counsel (insurers often require); preserve evidence; comply with consent-to-settle.

### 3D. FINANCIAL FRAMEWORK

| Rule | Application |
|---|---|
| **PCI DSS v4.0.1** (mandatory Mar 2025) | If cardholder data leaked — encryption, tokenization, audit logs, MFA. Card brand fines up to $100k+/mo; bank passes through to merchant. |
| **GLBA Safeguards Rule** | 30-day FTC notice; audit access controls. |
| **Regulation E / EFTA** | Stolen credentials → unauthorized EFT; bank liability tiers ($50/$500/unlimited). |
| **Fair Credit Billing Act (FCBA)** | $50 consumer cap on stolen credit card. |
| **SEC Cyber Rule** | Material PII breach → 8-K; reputational harm is a materiality factor. |
| **FFIEC / bank exam** | Authentication guidance (layered security for high-risk transactions). |
| **NAIC Insurance Data Security Model** (adopted by many states) | Insurer-specific info-security program + breach notice to insurance commissioner. |

### 3E. MARKETING / REPUTATIONAL FRAMEWORK

**Disclosure obligations:**
- **Consumer breach notification** — letter content statutorily prescribed (incident description, data involved, mitigation steps, contact info). Tone: factual, not minimizing.
- **SEC 8-K** — if material; reputational/customer-trust impact is a factor.
- **State AG notification** (CA AG requires notice if >500 CA residents affected).
- **HHS OCR "Wall of Shame"** — public posting of HIPAA breaches >500 — major reputational risk.

**Consumer trust impact:**
- Breach notices trigger **15–30% customer churn risk** in some sectors (healthcare, fintech).
- NPS / trust scores dip 10–25 points post-breach; 12–24 month recovery.
- Stock price: median −3.5% on breach disclosure; deeper for repeated breaches.

**Brand-damage patterns (2025-2026):**
- **"Downplayed controls" narrative** is the #1 amplifier — plaintiffs/press seize on any mismatch between marketing claims and actual security.
- **AI-specific framing** — "AI-enabled attack" is sometimes used to deflect blame, but regulators increasingly expect AI-aware defenses.
- **Deepfake CEO fraud** brand damage: even when the company is the victim, the incident signals weak controls.

**Communication playbook:**
1. **72-hour internal war room** (GC, CISO, CMO, CFO, outside counsel).
2. Privilege-protected forensics **before** public statements.
3. Coordinated customer letter + regulator filings + press statement (consistent facts).
4. Credit/identity monitoring offer (often required by settlement; builds goodwill).
5. Post-incident transparency report (90 days) — trend toward voluntary transparency.
6. Avoid over-promising on "no data was misused" unless forensics confirms.

---

## CROSS-CUTTING 2025-2026 DEVELOPMENTS SUMMARY

1. **TAKE IT DOWN Act (May 2025)** — first federal deepfake criminal law; FTC enforcement ($53,088/violation); first conviction April 2026.
2. **FTC Impersonation Rule (2024) + proposed individual-impersonation extension** — direct federal-court redress for AI impersonation fraud.
3. **EO 14365 (Dec 2025)** — attempts to preempt state AI laws via dormant Commerce Clause; legally contested; signals federal "One Rule" intent.
4. **PCI DSS v4.0.1 mandatory (Mar 31, 2025)** — 47 new requirements; non-compliance = fines/fees/termination.
5. **CA breach notice 30-day rule (effective Jan 1, 2026)** — tightest in nation; removes "unreasonable delay" wiggle room.
6. **CA Delete Act / DROP (enforcement Aug 1, 2026)** — one-stop data-broker deletion; $200/day penalties; CPPA Strike Force.
7. **CFAA post-Van Buren narrowing** (Third Circuit Aug 2025) — workplace-policy violations are NOT CFAA violations; insider-theft civil cases harder.
8. **SEC cyber-disclosure enforcement wave (2025)** — class actions piggyback on 8-K filings; directors/CISOs in crosshairs.
9. **CFPB Regulation E compliance aid (Jan 2025)** — stolen-credential transfers = unauthorized EFT; banks bear loss.
10. **Cyber-insurance market tightening** — war/state-actor exclusions, MFA attestations mandatory, AI-fraud increasing claim frequency (Munich Re 2026).
11. **GLBA Safeguards Rule 30-day FTC notice** (2023 amendment, active enforcement 2025) — financial institutions must report incidents affecting ≥500 consumers.
12. **CIRCIA reporting rules** (CISA) — critical-infrastructure cyber-incident reporting finalized; compliance ramping.

---

## QUICK REFERENCE: KEY CITATIONS

- Wire fraud: **18 U.S.C. § 1343**; Bank fraud: **§ 1344**; Conspiracy: **§ 1349**
- CFAA: **18 U.S.C. § 1030**; *Van Buren v. United States*, 593 U.S. 374 (2021)
- Trade secrets: **18 U.S.C. §§ 1831–1839** (EEA/DTSA)
- Identity theft: **18 U.S.C. §§ 1028, 1028A, 1029**
- Red Flags Rule: **16 C.F.R. Part 681**
- GLBA Safeguards: **16 C.F.R. Part 314**
- FTC Impersonation Rule: **16 C.F.R. §§ 461.1–461.3**
- TAKE IT DOWN Act: **Pub. L. No. 119-__ (S.146, signed May 19, 2025)**
- SEC Cyber Rule: **17 CFR 229.106 (Item 106); Form 8-K Item 1.05**
- CA Breach Notice: **Cal. Civ. Code §§ 1798.29, 1798.82** (2025 amend.)
- CCPA/CPRA: **Cal. Civ. Code § 1798.100 et seq.**; Private action § 1798.150
- CA Delete Act: **SB 362 (2023)**; enforcement Aug 1, 2026
- Regulation E: **12 C.F.R. Part 1005**
- PCI DSS v4.0.1 (June 2024; mandatory Mar 31, 2025)
- HIPAA Breach Notification: **45 C.F.R. §§ 164.400–414**

*Document compiled June 2026 from primary sources (DOJ, FTC, SEC, CFPB, Congress.gov, CA OAG, CPPA) and secondary legal analysis (Gibson Dunn, Latham, WilmerHale, Debevoise, Hunton, Ropes & Gray). Verify all citations against current text before legal reliance.*
