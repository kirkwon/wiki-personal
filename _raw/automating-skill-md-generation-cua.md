---
type: research-note
title: "Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining"
source: "PDF uploaded by Kirk Won"
paper: "https://arxiv.org/abs/2606.20363"
authors: ["Yuexing Hao (MIT)", "Xiaomin Li (Harvard)"]
venue: "NeurIPS 2026"
published: 2026-06-18
tags: [skill-generation, computer-using-agents, GUI-trajectory, GRPO, Qwen3, skill-mining, trajectory-segmentation, negative-result, contrastive-learning]
date: 2026-06-27
---

# Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining

## TL;DR

MIT/Harvard team built a three-stage pipeline to **automatically mine SKILL.md files from GUI interaction trajectories** — segmentation, clustering, and GRPO policy training. The mined skill clusters are readable (5/8 clusters ≥0.95 purity), but **do not reliably transfer**: GRPO improves IW skill-step accuracy only 18.5%→20.5%, leaves BrowseComp+ unchanged, and underperforms trivial frequency baselines. A careful diagnostic study with an honest negative result.

## Paper Identity

| Field | Value |
|-------|-------|
| **arXiv** | [2606.20363](https://arxiv.org/abs/2606.20363) |
| **Venue** | NeurIPS 2026 |
| **Authors** | Yuexing Hao (MIT), Xiaomin Li (Harvard) |
| **Model** | Qwen3-8B |
| **Training** | GRPO, 4× NVIDIA H200 NVL, 6,072 seconds |
| **Benchmarks** | InteraSkill Workflows (IW), WebArena, BrowseComp+, Mind2Web, WorkArena-NLP |

## Three-Stage Pipeline

### Phase 1: Trajectory Segmentation (Boundary Detection)
- Cuts GUI trajectories at **large action changes** using Euclidean distance between adjacent action vectors
- Each action vector: 15 features (10-way primitive one-hot + coordinates + timestamp + text length + scroll amount)
- Boundary threshold ε selected by sweeping percentiles, maximizing boundary F1
- Intentionally simple — no DOM, screenshots, or accessibility tree

### Phase 2: Skill Embedding (Library Construction)
1. **Segment Representation** — Mean + diagonal variance of action vectors (bag-of-actions, length-invariant, orderless)
2. **Wasserstein Clustering** — Squared Bures distance between diagonal Gaussian summaries. Average-linkage agglomerative clustering, k=8-16
3. **Supervised-Contrastive Refinement** — MLP encoder (30→64→32→16) trained with supervised-contrastive loss on pseudo-labels

### Phase 3: Skill-Aware GRPO Training
- **Model**: Qwen3-8B from base
- **Method**: GRPO with learned trajectory reward model
- **Setup**: 8 candidate responses/prompt, temp 0.7, max completion 192 tokens, lr 5e-6
- **Hardware**: 4× NVIDIA H200 NVL (143GB each)
- **Duration**: 6,072 seconds (~1.7 hours)

## Key Results

| Metric | Result | Interpretation |
|--------|--------|---------------|
| **Cluster purity (IW)** | 5/8 clusters ≥0.95 | Mined skills ARE readable |
| **IW skill-step accuracy** | 18.5% → 20.5% (GRPO) | Marginal improvement |
| **BrowseComp+ skill-step** | 43.5% → 43.3% (GRPO) | No improvement |
| **vs Frequency baseline** | Auto-SKILL.md WORSE at every data size | Trivial prior beats learned model |
| **Cross-domain transfer** | Absent or negative | Readable ≠ transferable |

## The Honest Negative Result

This is what makes the paper valuable — it's a **rigorous diagnostic study**, not a success claim:

1. **Readable clusters don't imply useful skills** — You can cluster trajectories into identifiable patterns, but those patterns don't help policies generalize
2. **Orderless representation loses sequential structure** — Bag-of-actions can't distinguish "copy before paste" from "paste before copy"
3. **Offline reward model insufficient** — The learned reward doesn't capture what makes skills useful across domains
4. **Frequency baselines are surprisingly strong** — "What skill usually comes next?" beats learned models

## Why This Matters for Kirk's Stack

### 1. Skill Auto-Generation (The Direct Application)

Kirk has **309+ Hermes skills** — all hand-written. This paper explores whether that process can be automated:

| Current (Manual) | Paper's Approach | Gap |
|---|---|---|
| Human writes SKILL.md | Pipeline mines from trajectories | Segmentation + clustering |
| Skills include order, recovery, validation | Orderless bag-of-actions | Loses sequential info |
| Skills transfer across domains | No verified transfer | Frequency baseline wins |
| Expert knowledge encoded | Pseudo-labels from clustering | No domain expertise |

**What works**: The segmentation + clustering approach CAN identify reusable patterns. Kirk's `wiki-capture` and `session-logging` skills already capture interaction trajectories — those could feed this pipeline to identify emergent skill patterns.

### 2. Connections to Active Workstreams

| Workstream | Connection |
|---|---|
| **AutoResearch** | AutoResearch's propose→test→ratchet could use mined skills as the search space. The negative result shows that the ratchet mechanism (keeping only improvements) is essential — without it, learned skills regress. |
| **Self-Harness** | Self-Harness's Weakness Mine step is the human equivalent of trajectory mining — finding where the agent fails reveals the skill boundary. The paper's boundary detection could automate this. |
| **GRPO Training** | The paper trains Qwen3-8B with GRPO — exactly the technique in the SDAR paper (also in GBrain). SDAR solved the token-level supervision problem that this paper's coarse reward model couldn't. |
| **BINEVAL** | The paper's skill-step accuracy metric suffers from the same ceiling effects BINEVAL addresses. Binary decomposition of "is this skill correct?" would be more discriminative. |
| **LLM Novelty Literature Review** | This paper IS evidence in the novelty debate — the negative result is a form of intellectual honesty that LLM-based research can produce. AI didn't just chase positive results; it rigorously documented failure. |
| **MCP / Docker / n8n** | Computer-using agents that manage infrastructure (Docker containers, n8n workflows) could generate their own skills from interaction patterns. |

### 3. What Can Be Extracted NOW

Despite the negative transfer result, the **segmentation and clustering pipeline IS useful** for:

- **Skill auditing** — Mine Kirk's 53+ session trajectories to find repeated patterns that should be skills but aren't
- **Skill deduplication** — Cluster similar skills to identify merge candidates
- **Skill gap detection** — Find action sequences that appear frequently but have no corresponding skill
- **SKILL.md quality** — Compare hand-written skills against mined patterns to find missing recovery/validation steps

## Limitations (Author's Own)

1. Orderless segment representation discards sequential structure
2. Offline reward model doesn't capture cross-domain utility
3. GRPO setup is narrow (offline, single epoch, no live GUI during RL)
4. Boundary detector over-splits (click→type transitions trigger false boundaries)

## Future Directions (Implied by the Paper)

1. **Action-prediction error for boundary detection** (Open-World Skill Discovery approach) instead of Euclidean distance
2. **Order-preserving segment representations** (sequence models instead of bag-of-actions)
3. **Online RL with live GUI feedback** instead of offline reward model
4. **SDAR-style token-level guidance** instead of coarse trajectory-level reward

## Source

- **Paper**: [arXiv:2606.20363](https://arxiv.org/abs/2606.20363)
- **Venue**: NeurIPS 2026
- **Code**: Anonymous repo (available in paper)
- **Found via**: Kirk Won uploaded PDF (2026-06-27)
