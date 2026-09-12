------

# One Recipe, Many Harnesses: What Self-Evolution Encodes Across Languages and Models

**Abstract**: Self-evolving harnesses are closed-loop systems where an agent inspects its own rollouts and edits its prompts, tools, and memory. They improve coding agents but prior work only reported aggregate gains. This paper disentangles what evolved harnesses actually encode by fixing the evolution recipe across 8 programming languages × 3 base models and analyzing the artifacts.

## Core Findings

1. **The loop works with two nulls**: Evolved harnesses beat both minimal seed and hand-designed mini-SWE-agent in most cells, but show near-zero gains for Python (all models) and GPT-5-mini (all languages).

2. **Gains = defect compensation, not new capability**: Harnesses never enable repairs the base model couldn't express — they install rules like "never modify test files", "verify compiles before submitting", "run failing test first". Gain size tracks the cell's defect mass: a harness closes the gap between what a policy *can* do and what it *does*.

3. **Shared playbook, disjoint plumbing**: All evolved harnesses converge on the same abstract disciplines (60-80% concept overlap) but instantiate them with almost entirely different ecosystem machinery (20-40% language-specific: commands, test paths, layout conventions).

4. **Bounded portability**: A transplanted harness helps in 18/20 cross-language pairs but hits native ceiling in only some; distilling everything into one universal harness recovers just 48-68% of native gains on Java/C++/TypeScript. For complex ecosystems, native re-evolution remains necessary.

## Practical Implications for Multi-Model Stacks

- **Defect profile is leading indicator**: Measure a model's failure signature first — if it commits few recoverable execution defects, harness work there yields ~null (explains Python/GPT-5-mini nulls).
- **Don't share one harness across models**: Distillation loses the ecosystem/cell-specific margin; expect to recover only ~half the gain.
- **Per-cell beats per-platform**: Static scaffolds hard-code one guess, but binding defect differs by (task-domain, model) cell — separate wrappers per agent CLI are endorsed.
- **Honest ceiling**: Harness engineering raises execution consistency, not capability. If a model can't express the fix, no scaffold work gets it there.

## Relevance to Current Setup

This validates the eval-first premise while warning: when a cell shows near-zero improvement, read it as "defect mass ≈ 0" not "loop broken". Directly informs where to invest harness effort in dojo/SkillOpt loops.

## Related Concepts
- [[self-harness]]
- [[recursive-self-improvement-systems]]
- [[decision-master]]
- [[bayesian-rogue-explore]]
- [[asymmetry-hunter]]
- [[knowledge-master]]

[[hermes-agent-stack]]

[[documentation-master]]
