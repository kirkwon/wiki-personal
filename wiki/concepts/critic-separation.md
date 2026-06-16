---
type: concept
title: Critic Separation
created: 2026-06-13
updated: 2026-06-13
tags: [critic-separation, software-development, loop-engineering]
related: [loop-engineering-plan, self-harness]
sources: ["loop-engineering-plan.md"]
---
# Critic Separation
Critic separation is the concept of separating the validation component from the execution component in a software agent. This allows for independent validation of proposed changes, enhancing the reliability and safety of the loop engineering process.

## Implementation
- Create a critic-only sub-agent template.
- Update the doer sub-agent to work with the critic sub-agent.
- Implement verification to test the critic separation.

## Importance
Critic separation is key to improving the reliability of the loop engineering process. It ensures that validation is independent of execution, reducing the risk of errors and improving overall efficiency.
---