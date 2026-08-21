---
date: 2026-07-14

title: "The Complete AI PM Loop System (GitHub for PM)"

type: infographic
source_type: image_ocr
source_file: img_069447b4d0ed.jpg
source_url: "https://www.github.com/instaply/pmskills" # inferred from content
authors:
  - "Shubham Saboo (Senior AI PM at Google)"
  - "Aakash Gupta (Decade in Product)"
ingested: 2026-07-04
extraction_method: apple_vision_ocr
extraction_confidence: 0.97
domains:
  - product-management
  - ai-agents
  - loop-engineering
  - agent-workflows
tags:
  - pm-loop
  - loop-engineering
  - github-for-pm
  - ai-pm
  - agent-loops
  - critic-doer
  - proof-gate
  - memory-layer
  - artifact-engineering
cross_links:
  - "[[loop-engineering]]"
  - "[[critic-doer-separation]]"
  - "[[agent-memory-layer]]"
  - "[[reusable-ai-artifact]]"
  - "[[proof-gate]]"
---

# The Complete AI PM Loop System (GitHub for PM)

> Infographic by **Shubham Saboo** (Senior AI PM at Google) and **Aakash Gupta** (Decade in Product).
> Extracted from a 968×968 JPEG image via Apple Vision OCR (135 text regions, avg confidence 0.97).

## Core Premise

> *"A loop is not just the agent does a task."*

The system you improve, not a one-off prompt. PM loops transform PM work into a **self-improving cycle** where each run produces a better artifact and a permanent learning.

---

## I. Anatomy of a PM Loop

Every PM loop has **four sequential stages** plus a stop condition:

```
Trigger → Action → Proof → Memory → [Stop]
                  (Gate)
```

| Stage | Role | Example Triggers/Actions |
|-------|------|--------------------------|
| **Trigger** | What starts the loop | New PRD lands; five new customer calls; launch date approaching; experiment readout; customer escalation |
| **Action** | The work the agent performs | Review and audit; summarize; compare vs prior; score vs rubric; synthesize data; draft new docs |
| **Proof (Gate)** | Evidence quality bar | Better source coverage, stronger evidence, fewer unsupported claims, higher rubric score, useful before-and-after diff |
| **Memory** | What gets saved permanently | GitHub commit, decision log, eval result, artifact changelog |
| **Stop Conditions** | When the loop terminates | Passes quality bar, no new signal, input missing/blocked |

**Key insight:** The **Proof stage is a Gate** — it decides whether to Improve, Accept, or Escalate. This mirrors the [[critic-doer-separation]] pattern.

---

## II. Loop Engineering Cycle

A **5-step meta-cycle** for improving the loop itself:

1. **Change the artifact** — Tweak a review criterion or remove a stale instruction from your agent skill.
2. **Run the agent** — Execute the workflow (e.g., review a PRD, summarize ten customer calls).
3. **Evaluate the output (quality gate)** — Assess evidence quality. Is this run demonstrably better than the last version?
4. **Keep or revert** — Sharp judgment required. Keep the better version, instantly revert the worse.
5. **Commit the learning** — Write to GitHub commit and decision log. The next loop starts from this baseline.

> *"The system you improve, not a one-off prompt."*

---

## III. Weekly Product Signal Loop (Concrete Example)

> *"One pass a week. The memo ships, the artifact gets sharper."*

### Step 1: Gather Evidence (Raw Material)
The agent pulls relevant raw inputs:
- Customer calls
- Support tickets
- Sales notes
- Experiment updates
- Analytics summaries

### Step 2: Cluster Themes
- Groups repeated pain points, objections, product gaps, and user requests
- Identifies what is new, what repeated, and what got stronger or weaker since the last report
- Flags drift from the plan

### Step 3: Compare to Last Week
- Scores good vs your bar
- Standing house: missing, blocked

### Step 4: Draft Product Signal Memo
- Agent writes the memo with evidence, exact quotes, and confidence levels, formatted for human review

### Step 5: Your Review (Gate) → Memory Layer

| Decision | Action |
|----------|--------|
| **Improve** | Improve rubric, tighten evidence bar for claims |
| **Accept** | Shipped changes |
| **Escalate** | Add launch blocker checks to checklist |

---

## IV. Reusable AI Artifact

> *"The system you improve, not a one-off prompt."*

The artifact (PRD review skill, call summarizer, eval rubric, launch checklist) is a **durable asset** that compounds across runs. It is version-controlled in GitHub.

---

## V. GitHub Memory Layer

> *"Not just files. The durable memory that lets loops improve."*

| Component | Purpose |
|-----------|---------|
| **GitHub repo** (`org/pm-loop-memory`) | Version control for artifacts and decision logs |
| **Commits** | 147 commits — each commit is a learning |
| **Decision log** | Human-readable rationale for each change |
| **Eval result** | Quantitative quality scores |
| **Artifact changelog** | What changed and why |

### Outcome: Improved PM Work Every Run
- Cleaner synthesis, less noise and more signal
- Sharper feedback, better criteria and calls and decisions
- Launch blockers caught, issues surfaced early, risk reduced

---

## Relationship to Existing Loop Engineering

This infographic describes **PM-domain loop engineering** using GitHub as the memory substrate. It maps cleanly onto the [[loop-engineering]] skill:

| PM Loop Stage | Loop Engineering Equivalent |
|---------------|------------------------------|
| Trigger | Loop trigger (cron, event, `/goal`) |
| Action | Doer script |
| Proof (Gate) | Critic validation |
| Memory | Decision log + artifact + eval result |
| Change the artifact | Skill auto-patch detection (Phase 3) |
| Keep or revert | Baseline diff / revert |
| Commit the learning | Baseline update |

**Key differences from our implementation:**
1. **GitHub as memory** — PM loop uses Git commits as the memory layer; our loop uses `~/loop-state/` + skill files
2. **Human-in-the-loop Gate** — PM loop has a human review step (Improve/Accept/Escalate); our loop uses automated critic
3. **Domain-specific artifacts** — PRD reviews, call summaries, signal memos vs generic file validation

---

## Modifications to Current Agentic Loops

Extracted insights applicable to our [[loop-engineering]] implementation:

### 1. Add a "Proof" Gate Naming
Our critic step is functionally equivalent to their "Proof" stage. Rename for clarity: **Trigger → Doer → Proof → Memory**.

### 2. Explicit Stop Conditions
The PM loop defines explicit stop conditions (passes quality bar, no new signal, input missing/blocked). Our loop should add these to prevent infinite cycling.

### 3. Artifact-as-Asset Framing
The "Reusable AI Artifact" framing is valuable. Each skill (PRD review, summarizer, rubric) is a durable asset. This reinforces treating skills as [[reusable-ai-artifact]]s, not disposable prompts.

### 4. Human Gate Option (Escalate)
The PM loop's three-way gate (Improve / Accept / Escalate) is richer than our binary PASS/FAIL. An **Escalate** path would route ambiguous results to human review instead of forcing a binary decision.

### 5. "Compare to Last Week" Baseline Diff
The signal loop explicitly compares current output to last week's. Our skill-patch-detect already does baseline diffs — this validates that approach and suggests we should surface the diff in the human review UI.

### 6. Memory Layer as Git
Using Git commits as the durable memory layer (147 commits) is a strong pattern. Our decision log + eval results could be Git-versioned for full auditability.

---

## Extraction Notes

- **Source:** 968×968 JPEG infographic
- **Method:** Apple Vision OCR (`screen_ocr.py`) — 135 text regions, avg confidence 0.97
- **Layout:** Complex multi-panel infographic with flowchart elements, color-coded sections, and small text. Apple Vision captured near-perfect text including arrows (→), confidence scores, and fine-grained labels.
- **Limitations:** Spatial relationships (which text belongs to which box) required manual reconstruction from bounding boxes. Pure OCR cannot capture color-coding or visual hierarchy.
- **See also:** [[extraction-method-comparison-ocr-vision-vlm]] for the full 4-method comparison that produced this page.
