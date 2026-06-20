---
type: source
title: Research Implementing Critic Separation
created: 2026-06-16
updated: 2026-06-16
tags: [research]
related: [critic-separation, agent-looping, ai-assisted-software-development]
sources: ["research-implementing-critic-separation-2026-06-17-052850.md"]
---
# Research Implementing Critic Separation
## Introduction
Implementing Critic Separation is a crucial aspect of AI-assisted software development, which involves separating the coding agent's role from the PR review agent's role. This separation is essential to ensure that verification remains objective and rigorous, catching architectural drifts, security vulnerabilities, and logic errors that might pass standard unit tests.

## Key Concepts
1. **Critic Separation**: Critic separation is the practice of automating code validation by employing a specialized Critic Agent to review claimed implementations against established Spec contracts and the Agent Constitution.
2. **Agent Looping**: Agent looping is the practice of designing the execution cycles AI agents run through to complete tasks, focusing on how an agent perceives its environment, reasons about next steps, takes action, and decides whether to continue or stop.
3. **Adversarial Code Review**: Adversarial code review is a technique used to validate component compositions and ensure that they work as intended, by employing a Critic Agent to review the code against a set of rules and constraints.

## Implementing Critic Separation
To implement Critic Separation, developers should follow these steps:
1. **Fetch Issue Context**: Retrieve the source of truth for the work being reviewed.
2. **Gather Implementation Artifacts**: Identify what has changed and prepare the diff or the set of modified files for the Critic Agent.
3. **Load Contracts**: Identify the "laws" the implementation must follow, including relevant functional specs and the project's Constitution.
4. **Adversarial Review**: Deploy the Critic Agent with an adversarial persona to compare the code strictly against the loaded contracts.
5. **Identify Violations & Verdict**: Analyze the Critic's output and categorize violations by impact and provide specific remediation paths.

## Agent Looping
Agent looping involves designing the execution cycles AI agents run through to complete tasks. It focuses on how an agent perceives its environment, reasons about next steps, takes action, and decides whether to continue or stop. A well-engineered loop has four properties: a defined termination condition, observable intermediate states, defined retry logic, and a recovery path when the agent gets stuck.

## Real-World Applications
The principles of Critic Separation and Agent Looping apply across various systems where an AI agent runs multi-step tasks autonomously, including research and analysis agents, code generation and testing agents, knowledge capture and organization agents, and customer support and triage agents.

## Conclusion
Implementing Critic Separation and Agent Looping are essential for building reliable AI systems that can operate autonomously and efficiently. By following the steps outlined in this research and understanding the key concepts, developers can create AI agents that are capable of completing complex tasks and providing accurate results.

## Future Research Directions
Future research directions include exploring the application of Critic Separation and Agent Looping in various domains, such as finance, healthcare, and education, and investigating the use of these techniques in human-AI collaboration and decision-making.

## References
[1] **Generator-Critic Separation — Agent Patterns Catalog** (agentpatternscatalog.org)
[2] **The Jury Pattern: a mixture of critics for AI code review | Chris Reddington** (chrisreddington.com)
[3] **Role Separation Pattern | AI-Assisted Software Development** (ai-assisted-software-development.com)
[4] **Stop Letting the Agent That Wrote the Code Review It Too — Critique Blog** (critique.sh)
[5] **Adversarial Code Review | ASDLC.io** (asdlc.io)
[6] **Test each component of a compound schema independently — compound failures give no diagnostic | How to Think AI** (howtothink.ai)
[7] **EUDML | Component composition validation** (eudml.org)
[8] **Decompose complex schemas into independently testable atomic | How to Think AI** (howtothink.ai)
[9] **Validating and invalidating components** (docs.adaptivecomputing.com)
[10] **Creating a single-directory component | Using Single-Directory Components | Drupal Wiki guide on Drupal.org** (drupal.org)
[11] **Agent Looping and Systems Engineering: Building Reliable AI** (ranti.dev)
[12] **Loop Engineering: When You Stop Prompting the Agent and Start Building the System That Does - Strongly.AI** (strongly.ai)
[13] **Loop Engineering - by Addy Osmani - Elevate** (addyo.substack.com)
[14] **docs/operating-loops.md** (github.com)
[15] **What Is Loop Engineering? The Complete Guide** (remio.ai)