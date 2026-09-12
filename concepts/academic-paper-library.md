------

# Academic Paper Library

> A curated collection of **143 academic papers** in GBrain spanning AI, ML, cognitive science, decision theory, and finance — the research foundation for Hermes agent architecture.
>
> **Last updated:** 2026-06-13
> **Total papers:** 143
> **Namespaces:** `papers/` (primary), overview in `~/40-archives/50-gbrain-exports/`

---

## Domain Overview

The paper library covers 8 research domains that directly inform the Hermes agent architecture:

| Domain | Count | Core Papers | Architecture Relevance |
|--------|-------|-------------|----------------------|
| **Agentic AI & Loops** | ~12 | Reflexion, ReAct, AutoHarness, Evolving Agents | Self-Harness, critic/doer separation, loop engineering |
| **Deep Learning / Transformers** | ~25 | Attention Is All You Need, BERT, GPT-3, ResNet | Foundation models, architecture backbones |
| **Reinforcement Learning** | ~15 | DQN, PPO, AlphaGo, AlphaZero, A3C | RL-based agent optimization, training paradigms |
| **Cognitive Science / Decision** | ~20 | Prospect Theory, Thinking Fast/Slow, Heuristics & Biases | Mental models, decision frameworks, cognitive biases library |
| **Knowledge Graphs / RAG** | ~5 | GraphRAG, Unifying LLMs+KGs, MACLA | GBrain knowledge graph, memory hierarchy |
| **Multi-Agent Systems** | ~10 | Project Synapse, Multi-Agent Orchestration, LEGOMem | Sub-agent delegation, task decomposition |
| **Causal AI / Finance** | ~10 | FinRL, Causal Discovery, Portfolio Risk | Hedge signal, portfolio dashboard, causal analysis |
| **Context Compression** | ~10 | STAR-KV, Structured Eviction, TokenMizer | Headroom proxy, token optimization |

---

## Key Papers (by Domain)

### Agentic AI & Self-Improving Loops
- [[papers/reflexion-llm-agent-verbal-rl|Reflexion: Language Agents with Verbal Reinforcement Learning]] (2303.11366) — *Definitive critic/doer architecture*
- [[papers/react-reasoning-acting-llm|ReAct: Synergizing Reasoning and Acting in Language Models]] (2210.03629) — *Thought-action interleaving paradigm*
- [[papers/autoharness-synthesizing-code-harness|AutoHarness: Synthesizing a Code Harness]] (2603.03329) — *Agent harness synthesis*
- [[papers/evolving-agents-harness-self-preference|Evolving Agents in the Dark: Self-Preference]] (2606.05922) — *Unsupervised harness improvement*

### Transformers & Deep Learning
- [[papers/vawsani-attention-transformer|Attention Is All You Need]] — *Transformer architecture*
- [[papers/language-models-are-few-shot-learners-gpt-3|GPT-3: Language Models are Few-Shot Learners]] — *Scaling laws*
- [[papers/gpt3-brown]]
- [[papers/bert-devlin]]
- [[papers/bert-pre-training-of-transformers-v2]]
- [[papers/deepseek-r1-reasoning-rl]]
- [[papers/deepseek-v2-moe-efficient]]
- [[papers/deepseek-v3-technical-report]]
- [[papers/deep-residual-learning-resnet]]
- [[papers/batch-normalization]]
- [[papers/dropout-regularization]]
- [[papers/dropout-srivastava]]
- [[papers/gans-goodfellow]]

### Reinforcement Learning
- [[papers/dqn-atari|Playing Atari with Deep RL]] — *DQN foundation*
- [[papers/dqn-nature|Human-Level Control Through Deep RL]]
- [[papers/human-level-control-through-deep-rl-dqn-nature]]
- [[papers/human-level-control-through-deep-rl]]
- [[papers/ppo-schulman|Proximal Policy Optimization]] — *PPO algorithm*
- [[papers/proximal-policy-optimization]]
- [[papers/trpo-schulman|Trust Region Policy Optimization]]
- [[papers/trust-region-policy-optimization]]
- [[papers/alphago-nature|Mastering Go with Deep Neural Networks]]
- [[papers/mastering-go-with-deep-neural-networks-alphago]]
- [[papers/mastering-go-with-deep-neural-networks]]
- [[papers/alphazero|Mastering Chess with Self-Play]]
- [[papers/mastering-chess-with-self-play-alphazero]]
- [[papers/mastering-chess-with-self-play]]
- [[papers/a3c-mnih|Asynchronous Methods for Deep RL (A3C)]]
- [[papers/asynchronous-methods-for-deep-rl-a3c]]
- [[papers/asynchronous-methods-for-deep-rl]]
- [[papers/policy-gradient-methods]]
- [[papers/policy-gradient-sutton]]
- [[papers/q-learning]]
- [[papers/q-learning-watkins]]
- [[papers/reinforcement-learning-an-introduction]]
- [[papers/reinforcement-learning-sutton]]

### Cognitive Science & Decision Making
- [[papers/prospect-theory-kahneman-tversky|Prospect Theory]] — *Decision under risk*
- [[papers/tversky-kahneman-heuristics|Judgment Under Uncertainty: Heuristics and Biases]]
- [[papers/judgment-under-uncertainty-heuristics-and-biases]]
- [[papers/judgment-under-uncertainty-heuristics-biases]]
- [[papers/kahneman-thinking-fast-slow|Thinking, Fast and Slow]]
- [[papers/nudge-thaler-sunstein|Nudge]]
- [[papers/misbehaving-thaler|Misbehaving]]
- [[papers/simon-bounded-rationality|Bounded Rationality]]
- [[papers/ariely-predictably-irrational|Predictably Irrational]]
- [[papers/influence-cialdini|Influence: Science and Practice]]
- [[papers/social-proof-cialdini]]
- [[papers/social-proof-and-persuasion]]
- [[papers/halo-effect-cialdini]]
- [[papers/dunning-kruger-effect|Dunning-Kruger Effect]]
- [[papers/the-dunning-kruger-effect]]
- [[papers/ego-depletion]]
- [[papers/endowment-effect-loss-aversion]]
- [[papers/the-endowment-effect]]
- [[papers/loss-aversion-in-riskless-choice]]
- [[papers/loss-aversion-riskless-choice]]
- [[papers/marshmallow-test]]
- [[papers/the-marshmallow-test]]
- [[papers/growth-mindset-dweck|Growth Mindset]]
- [[papers/growth-mindset]]
- [[papers/self-theories-dweck]]
- [[papers/believing-you-can-improve]]
- [[papers/superforecasting-tetlock|Superforecasting]]
- [[papers/superforecasting]]
- [[papers/cognitive-reflection-test]]
- [[papers/six-thinking-hats]]
- [[papers/lateral-thinking-de-bono]]
- [[papers/debono-lateral-thinking]]
- [[papers/how-to-solve-it-polya]]
- [[papers/how-to-solve-it]]
- [[papers/polya-how-to-solve-it]]
- [[papers/wisdom-of-crowds]]
- [[papers/the-wisdom-of-crowds]]
- [[papers/page-diversity-bonus]]
- [[papers/diversity-bonus-page]]
- [[papers/the-difference-diversity]]
- [[papers/scientific-revolutions-kuhn]]
- [[papers/kuhn-paradigm-shift]]
- [[papers/beginning-of-infinity]]
- [[papers/the-beginning-of-infinity]]
- [[papers/deutsch-fabric-reality]]
- [[papers/fabric-of-reality-deutsch]]

### Finance & Economics
- [[papers/do-stock-prices-move-too-much]]
- [[papers/stock-prices-too-much]]
- [[papers/irrational-exuberance-shiller]]
- [[papers/irrational-exuberance]]
- [[papers/inflation-expectations]]

### Knowledge Graphs & Memory
- [[papers/graphrag-retrieval-augmented-graphs|GraphRAG]] (2501.00309)
- [[papers/sutton-barto-rl-introduction|Reinforcement Learning: An Introduction]] — *Sutton & Barto*

### Multi-Agent Systems
- [[papers/project-synapse-hierarchical-multi-agent|Project Synapse]] (2601.08156)

### Context Compression
- [[papers/star-kv-cache-compression|STAR-KV]] (2606.08382)
- [[papers/turboquant-online-vector-quantization|TurboQuant]] (2606.05868)

---

## Recent Additions (2026-06-13)

### Newly Imported Papers
- [[papers/reflexion-llm-agent-verbal-rl|Reflexion]] — Critic/doer separation (2303.11366)
- [[papers/react-reasoning-acting-llm|ReAct]] — Thought-action interleaving (2210.03629)
- [[papers/autoharness-synthesizing-code-harness|AutoHarness]] — Code harness synthesis (2603.03329)
- [[papers/evolving-agents-harness-self-preference|Evolving Agents]] — Self-preference optimization (2606.05922)
- [[papers/graphrag-retrieval-augmented-graphs|GraphRAG]] — Knowledge graph RAG (2501.00309)
- [[papers/project-synapse-hierarchical-multi-agent|Project Synapse]] — Hierarchical multi-agent (2601.08156)
- [[papers/star-kv-cache-compression|STAR-KV]] — KV cache compression (2606.08382)

### Reclassified (concept → paper)
88 papers reclassified from `type: concept` to `type: paper` — all existing papers in the `papers/` namespace now have correct typing.

---

## Usage

```bash
# List all papers
gbrain list --type paper

# Search papers by topic
gbrain search "reinforcement learning"

# Get a specific paper
gbrain get "papers/attention-is-all-you-need"

# Count papers
gbrain stats | grep paper
```

[[analyze-paper]]

[[research-paper-writing]]
