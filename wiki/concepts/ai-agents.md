---
title: AI Agents
type: concept
tags:
- concept
- agent
- agentic-ai
- autonomous-ai
- planning
- reasoning
created: '2026-05-14'
updated: '2026-05-14'
---
--

# AI Agents

## Definition
An AI agent is a system that perceives its environment, takes actions to achieve goals, and can learn or adapt over time. Agents combine perception, reasoning, planning, memory, and tool use to operate autonomously or semi-autonomously in complex domains.

## Historical Context
- **1950s-60s**: Early AI programs like the Logic Theorist and General Problem Solver exhibited goal‑directed behavior.
- **1970s**: Shakey the robot (SRI) integrated perception, planning, and execution.
- **1980s**: Expert systems with rule‑based reasoning; early BDI (Belief‑Desire‑Intention) agents.
- **1990s**: Softbot agents (Etzioni & Weld) for web tasks; multi‑agent systems research.
- **2000s**: Cognitive architectures (ACT-R, SOAR, OpenCog); software agents for e‑commerce.
- **2010s**: Deep reinforcement learning agents (DeepMind’s DQN, AlphaGo); conversational assistants (Siri, Alexa).
- **2020s**: Large language model (LLM)‑based agents (AutoGPT, BabyAGI, HuggingGPT, Hermes, ReAct, Reflexion); tool‑augmented LLMs; agent frameworks (LangChain, LlamaIndex, Semantic Kernel).

## Key Contributors
- [[allen-newell]] & [[herbert-a-simon]] – Logic Theorist, GPS.
- [[shakey-project]] (SRI) – integrated robotics agent.
- [[ronald-brachman]] – early work on knowledge representation for agents.
- [[michael-wooldridge]] & [[nicholas-r-jennings]] – foundations of multi‑agent systems.
- [[peter-stone]] – robot soccer agents (CMUnited).
- [[richard-sutton]] & [[andrew-barto]] – reinforcement learning foundations for agents.
- [[volodymyr-mnih]] et al. – Deep Q‑Network (DQN) agents.
- [[david-silver]] & [[demis-hassabis]] – AlphaGo agents.
- [[yoav-shoham]] – agent-oriented programming.
- [[andrew-ng]] – Stanford AI helicopter agents.
- [[hado-van-hasselt]] – Double DQN.
- [[lerrel-pinto]] & [[abhinav-gupta]] – RL for robotics agents.
- [[jason-weston]] et al. – Memory Networks.
- [[antoine-bordes]] et al. – Dynamic Memory Networks.
- [[sainbayar-sukhbaatar]] et al. – End‑to‑end memory networks.
- [[alexander-rush]] et al. – question answering with attention.
- [[mike-lewis]] et al. – BART and sequence‑to‑sequence models.
- [[hyung-won-chung]] et al. – instruction‑tuned LLMs (FLAN).
- [[aarohi-srivastava]] et al. – BIG‑bench.
- [[jason-wei]] et al. – chain‑of‑thought prompting.
- [[hunter-lightman]] et al. – process supervision.
- [[guodong-zhang]] et al. – reward modeling.
- [[long-ouyang]] et al. – InstructGPT and RLHF.
- [[openai]] – GPT series and assistant agents.
- [[hugging-face]] – Transformers and agent tools.
- [[langchain]] – LLM‑agent framework.
- [[llamaindex]] – data‑agent framework.
- [[semantic-kernel]] – Microsoft agent SDK.
- [[autogpt]] – early LLM‑agent loop.
- [[babyagi]] – task‑driven autonomous agent.
- [[hermes-agent]] – local, extensible agent framework.
- [[react]] – reasoning + acting paradigm.
- [[reflexion]] – self‑reflection for agents.
- [[hugginggpt]] – LLM as controller for Hugging Face models.

## Core Components
1. **Perception** – processing sensory/input data (vision, language, sensors).
2. **Memory** – short‑term (context window) and long‑term (vector stores, knowledge graphs).
3. **Reasoning & Planning** – logical deduction, chain‑of‑thought, tree‑of‑thought, RL‑based planning.
4. **Tool Use** – invoking APIs, running code, accessing databases.
5. **Action Space** – discrete (e.g., answer, click) or continuous (e.g., motor torques).
6. **Learning & Adaptation** – fine‑tuning, RLHF, in‑context learning, episodic memory.
7. **Alignment & Safety** – reward modeling, constitutional AI, interpretability.

## Agent Architectures
- **ReAct** – interleaves reasoning and acting traces.
- **Reflexion** – adds self‑reflection loops to improve performance.
- **AutoGPT** – iteratively prompts LLM to propose and execute subtasks.
- **BabyAGI** – task‑queue driven agent with memory.
- **Hermes Agent** – modular agent with tools, skills, memory, and planning modes.
- **LangChain Agents** – zero‑shot, structured‑chat, and plan‑and‑execute agents.
- **LlamaIndex Agents** – query‑engine‑centric agents for data retrieval.
- **Semantic Kernel Agents** – skill‑based orchestration with planning.
- **RL‑Based Agents** – policy networks trained via PPO, SAC, etc.
- **Multi‑Agent Systems** – societies of agents communicating via protocols (FEA, FIPA, KQML).

## Applications
- **Personal assistants** – scheduling, email, information retrieval.
- **Customer service** – chatbots with tool access (orders, refunds).
- **Software engineering** – code generation, debugging, PR reviews (Devin, Copilot Workspace).
- **Scientific discovery** – literature review, hypothesis generation, experiment design.
- **Finance** – portfolio analysis, trading signals, risk assessment.
- **Healthcare** – triage, diagnostic support, patient monitoring.
- **Robotics** – navigation, manipulation, task planning.
- **Gaming** – NPC behavior, game testing, procedural content generation.
- **Autonomous vehicles** – perception, planning, control loops.
- **Scientific assistants** – drug discovery, materials design, climate modeling.
- **Knowledge work** – report writing, data analysis, presentation creation.

## Related Concepts
- [[reinforcement-learning]] – provides learning mechanisms for agents.
- [[planning]] – classical and AI planning algorithms.
- [[tool-use-ai]] – how agents invoke external capabilities.
- [[memory-ai]] – short‑term context, long‑term storage, knowledge graphs.
- [[reasoning]] – deduction, induction, abduction, analogical, commonsense.
- [[large-language-models-llms]] – foundation for many modern agents.
- [[prompt-engineering]] – designing effective instructions for agents.
- [[chain-of-thought-cot]] – intermediate reasoning steps.
- [[tree-of-thought-tot]] – branching reasoning for search.
- [[reflexion]] – self‑evaluation and correction.
- [[autogpt]] – early agent loop.
- [[babyagi]] – task‑driven agent.
- [[langchain]] – framework for LLM agents.
- [[llamaindex]] – data‑centric agent framework.
- [[semantic-kernel]] – Microsoft agent SDK.
- [[hermes-agent]] – local, extensible agent framework.
- [[multi-agent-systems]] – societies of interacting agents.
- [[agent-communication-languages]] – ACL, KQML, FIPA‑SL.
- [[belief-desire-intention-bdi]] – classical agent architecture.
- [[cognitive-architectures]] – ACT‑R, SOAR, OpenCog.
- [[embodied-agents]] – agents with physical bodies (robots).
- [[software-agents]] – agents operating in digital environments.
- [[knowledge-agents]] – agents focused on information retrieval and synthesis.
- [[task-agents]] – agents that execute specific jobs (e.g., scheduling).
- [[dialogue-agents]] – conversational agents.
- [[autonomous-agents]] – agents that operate without continuous human input.

## See Also
- [[hermes-agent]]
- [[langchain]]
- [[llamaindex]]
- [[semantic-kernel]]
- [[autogpt]]
- [[babyagi]]
- [[react]]
- [[reflexion]]
- [[multi-agent-systems]]
- [[reinforcement-learning]]
- [[planning]]
- [[tool-use-ai]]
- [[memory-ai]]
- [[reasoning]]
- [[large-language-models-llms]]
- [[prompt-engineering]]
- [[chain-of-thought]]
- [[tree-of-thought]]
- [[reflexion]]