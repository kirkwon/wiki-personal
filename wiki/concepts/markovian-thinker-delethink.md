---
type: concept
title: Markovian Thinker Delethink
ingested_via: put_page
ingested_at: '2026-07-22T00:48:33.238Z'
source_kind: put_page
created: 2026-07-22
source: brain/ (retired 2026-09-13)
---
# The Markovian Thinker (Delethink)

## Paper
- **Title**: The Markovian Thinker: Architecture-Agnostic Linear Scaling of Reasoning
- **Authors**: Milad Aghajohari, Kamran Chitsaz, Amirhossein Kazemnejad, Sarath Chandar, Alessandro Sordoni, Aaron Courville, Siva Reddy
- **Institution**: Mila / McGill
- **ArXiv**: 2510.06557 (Oct 2025, v3 Nov 2025)
- **Cited by**: 14

## Core Idea: Markovian Thinking
Standard RL reasoning environments have unbounded state (prompt + all prior tokens → quadratic attention cost). Markovian Thinking proposes: the policy conditions on a **constant-size state**, not the full history.

## Delethink: The RL Environment
5-step loop:
1. **Redefine environment**: State = constant-size, not unbounded history
2. **Chunk**: Fixed-size reasoning chunks (e.g. 8K tokens)
3. **Write state**: Policy learns to write a textual carryover near chunk end
4. **Reset context**: Environment wipes context, reinitializes with query + carryover
5. **Continue**: Linear compute, constant memory

## Key Results
- R1-Distill 1.5B thinks in 8K chunks, reasons to 24K tokens — matches LongCoT-RL trained at 24K budget
- At 96K average thinking length: Delethink costs **7 H100-months** vs LongCoT's **27**
- Off-the-shelf models (1.5B-120B) already sample Markovian traces zero-shot
- The bottleneck is the **RL environment**, not the architecture

## Applications to Agent Systems
- Context window management: chunk reasoning, compress state, reset
- Loop engineering: each loop iteration is a "chunk" with carryover state
- SkillOpt: benchmark runs could use context resets between iterations
- Local models: enables infinite reasoning on constrained hardware (8GB RAM)

## Relation to Bayesian Thinking
- **Markov**: memoryless — next state depends only on current state (frequentist, generative)
- **Bayesian**: prior + evidence → posterior (belief updating, probabilistic)
- **Orthogonal axes**: HMMs are both Markov AND Bayesian
- Delethink uses "Markovian" in the property sense, not the statistical paradigm sense

## Implementations
- diegovachon/markov-chain-of-thought: Raspberry Pi 5, 8GB RAM, infinite System 2 reasoning
