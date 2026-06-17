---
tags: [permanent-question, research, ml-theory]
created: 2026-05-25
question: "What approaches meaningfully accelerate learning — curriculum learning, active learning, knowledge distillation, continual learning, few-shot adaptation? What tradeoffs matter?"
type: permanent-question
reviewed: 2026-05-25
---

# Q03: Accelerating Learning in Systems

**Status:** Active - accumulating

## Question
*What approaches meaningfully accelerate learning — curriculum learning, active learning, knowledge distillation, continual learning, few-shot adaptation? What tradeoffs matter?*

## Current State of Knowledge

### 1. Active Learning (Learn What Matters)
- **Core idea**: Instead of training on random data, the model asks for labels on the most uncertain/important examples
- **Finance applicability**: Labeled financial data is expensive (requires expert annotation or real-world consequences). Active learning maximizes signal per label.
- **Use case**: If you have a small labeled dataset of insider trading signals, use active learning to pick the most informative cases first
- **Limitation**: Requires a model that can express uncertainty (Bayesian methods, ensembles)

### 2. Curriculum Learning (Start Simple, Grow Complex)
- **Core idea**: Train on easy examples first, then progressively harder ones
- **Evidence**: Works well in RL (starting with simple environments), less clear in supervised learning
- **In Finance**: Start with regime-predictable periods, then add edge cases. Or start with simple features, add complex ones.
- **Related**: Self-paced learning — model controls its own curriculum

### 3. Knowledge Distillation (Learn from a Bigger Model)
- **Core idea**: Train a small model to mimic a large model's soft predictions
- **In Finance**: Use a large model ( GPT-4 ) to generate synthetic labels or pseudo-labels for a smaller, faster model
- **Evidence**: Works. Distilled BERT models (DistilBERT) retain 97% performance with 60% less compute
- **Key tradeoff**: The small model is faster but less expressive. Useful for real-time inference.

### 4. Transfer Learning (Leverage Pretraining)
- **Core idea**: Pretrain on large related dataset, fine-tune on small target dataset
- **In Finance**: Pretrain on broad market data, fine-tune on specific asset class or strategy
- **Problem**: Markets are non-stationary. Pretrained patterns may not transfer across regimes.
- **Better approach**: Domain-adaptive pretraining (continue pretraining on in-domain corpus)

### 5. Few-Shot / Zero-Shot (Learn from Description)
- **Core idea**: Give model task description + few examples in context, no weight updates needed
- **In Finance**: Describe a new anomaly detection task in natural language, model applies it
- **Limitation**: Few-shot works for general reasoning, less reliable for precise numerical tasks
- **Use case**: Good for ideation, hypothesis generation, not for live trading signals

### 6. Continual Learning (Learn Without Forgetting)
- **Core idea**: System learns sequential tasks without catastrophic forgetting
- **In Finance**: Model needs to learn new regimes (2020 COVID, 2022 rates) without forgetting 2008
- **Methods**: 
  - Elastic Weight Consolidation (EWC) — protect important weights from previous tasks
  - Rehearsal — store exemplars of previous tasks
  - Progressive neural networks — add new columns for new tasks
- **Real problem**: In finance, old regimes matter. A model that forgets 2008 is dangerous.

### 7. Causal Inference Acceleration
- Using causal graphs to reduce the sample complexity of learning
- Instead of learning everything from data, encode causal structure and learn only the causal mechanisms
- Potentially huge efficiency gains if the causal structure is known

## Key Papers
- Settles — "Active Learning Literature Survey" (comprehensive review)
- Bengio et al. — "Curriculum Learning" (2009, original curriculum learning)
- Hinton et al. — "Distilling the Knowledge in a Neural Network" (2015, distillation)
- Kirkpatrick et al. — "Overcoming Catastrophic Forgetting in NNs" (EWC)

## Emerging Methodology

For a personal system learning about finance:
- **Active learning is underutilized**: Most quants label data randomly. Systematic active learning would dramatically improve signal.
- **Causal inference + ML** is the highest-leverage combination: Use domain knowledge to constrain what causal structures are possible, then ML learns the rest.
- **Distillation** is practical: Use a frontier model to generate insights, distill into faster local models.
- **Continual learning** matters: Build explicit regime memory so the system knows when conditions change.

### Loop Engineering & Agent Systems
- **`/goal` primitive (run-until-done)**: Long-running agent tasks that persist through interruptions, enabling autonomous research and iteration loops without manual restart.
- **Loop engineering automation**: Systematically building feedback loops (observe → decide → act → learn) into agent workflows so each cycle improves the next.
- **Triage inbox feedback loop**: A persistent inbox where raw inputs (ideas, errors, observations) are triaged, prioritized, and fed back into the learning system — closing the loop between discovery and action.
- **Skill auto-patch from learning**: When an agent learns something new, the skill file itself is patched to encode that knowledge permanently — the system improves its own capabilities over time.

## Connections
- [[Q02]] — accelerated learning feeds self-improvement
- [[Q01]] — these techniques reduce the skills gap
- [[loop-engineering]] — core methodology for building learning loops into agent systems
- [[methodology-loop]] — meta-loop that governs how methodology evolves through usage

## Last Updated
_2026-05-25_ — Initial research position
_2026-06-13_ — Added loop engineering / agent systems methodology, updated status to Active - accumulating, added [[loop-engineering]] and [[methodology-loop]] connections
