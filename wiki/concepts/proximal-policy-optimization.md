---
date: 2026-05-14
title: Proximal Policy Optimization (PPO)
description: "Proximal Policy Optimization (PPO)"
type: concept
tags:
- concept
- reinforcement-learning
- ppo
- policy-gradient
- deep-rl
created: '2026-05-14'
updated: '2026-05-14'
---
--

# Proximal Policy Optimization (PPO)

## Definition
Proximal Policy Optimization (PPO) is a family of policy optimization methods for reinforcement learning that alternate between sampling data through interaction with the environment and optimizing a surrogate objective function using stochastic gradient ascent. PPO strikes a balance between sample complexity, ease of implementation, and tuning sensitivity, making it one of the most widely used RL algorithms in practice.

## Historical Context
- **2017**: Schulman et al. introduced Trust Region Policy Optimization (TRPO) to ensure stable policy updates via a KL-divergence constraint.
- **2017 (later)**: Schulman, Wolski, Dhariwal, Radford, Klimov introduced Proximal Policy Optimization (PPO) as a simpler, more practical alternative to TRPO, using a clipped surrogate objective.
- **2018**: PPO became the default algorithm in many RL libraries (e.g., OpenAI Baselines, Stable Baselines3, RLlib).
- **2019**: PPO used in OpenAI Five for Dota 2 at scale.
- **2020**: PPO adapted for large-scale language model fine‑tuning via RLHF (Reinforcement Learning from Human Feedback).

## Key Contributors
- [[john-schulman]] – lead author of TRPO and PPO papers.
- [[filip-wolski]] – co‑author of PPO.
- [[prafulla-dhariwal]] – co‑author of PPO.
- [[alec-radford]] – co‑author of PPO (also known for GPT series).
- [[karl-klimov]] – co‑author of PPO.
- [[openai]] – popularized PPO through baselines and large‑scale applications.
- [[stable-baselines3-team]] – maintained widely used PPO implementation.

## Core Idea
TRPO constrains the update so that the new policy stays within a trust region measured by the average KL divergence between old and new policies. PPO approximates this constraint by modifying the surrogate objective to penalize changes that move the probability ratio too far from 1, using a clip range.

## PPO‑Clip Objective (most common variant)
Given a trajectory batch, define the probability ratio:
\[ r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_\text{old}}(a_t|s_t)} \]
The clipped surrogate objective is:
\[ L^{CLIP}(\theta) = \hat{\mathbb{E}}_t \left[ \min\left( r_t(\theta) \hat{A}_t,\; \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t \right) \right] \]
where \(\hat{A}_t\) is an estimator of the advantage function (e.g., GAE) and \(\epsilon\) is a hyperparameter (commonly 0.2). An entropy bonus is often added to encourage exploration.

## Algorithm Steps
1. **Collect data** by running the current policy for N steps.
2. **Compute advantage estimates** (e.g., using GAE).
3. **Optimize the surrogate objective** w.r.t. the policy parameters using minibatch SGD for several epochs.
4. **(Optional) Update value function** by minimizing a squared‑error loss on returns.
5. **Repeat**.

## Variants
- **PPO‑Clip** – the clipped objective described above.
- **PPO‑Penalty** – uses a KL‑penalty instead of a clip; adapts the penalty coefficient to achieve a target KL.
- **Adaptive KL Penalty** – automatically adjusts the penalty coefficient.
- **Distributed PPO** – e.g., IMPALA‑style architecture with multiple actors and a learner.
- **PPO for Continuous Control** – often paired with architectures like Gaussian policies or beta distributions.
- **PPO‑LSTM** – recurrent policies for partially observable environments.
- **PPO for Discrete Actions** – softmax policy over action space.
- **PPO with Reward Shaping / Curriculum Learning** – combines with techniques to shape learning.

## Practical Tips
- Use **generalized advantage estimation (GAE)** for low‑variance advantage estimates.
- Normalize advantages within a minibatch.
- Clip the probability ratio to `[1−ε, 1+ε]` (ε = 0.1–0.3).
- Use **Adam optimizer** with moderate learning rate (e.g., 3e‑4).
- Train for multiple epochs over the same batch (typically 3‑10).
- Add an **entropy bonus** to the loss (coefficient ~0.01) to avoid premature convergence.
- Monitor **average KL divergence** between old and new policy; if it spikes, consider lowering the learning rate or clipping range.
- For **continuous actions**, consider using a Tanh‑Gaussian policy with state‑dependent standard deviation.
- For **discrete actions**, use a categorical policy (softmax) and consider action masking if needed.

## Applications
- **Game playing**: Atari, Dota 2 (OpenAI Five), various board games.
- **Robotics**: locomotion, manipulation, grasping (e.g., in MuJoCo, Dex‑NVG).
- **Resource management**: data center cooling, job scheduling, network routing.
- **Finance**: portfolio execution, algorithmic trading.
- **Healthcare**: treatment planning, dosing regimens.
- **Dialogue systems**: fine‑tuning language models via RLHF.
- **Autonomous driving**: planning and control.
- **Recommendation systems**: slate generation, exploration‑exploitation trade‑off.
- **Energy management**: smart grids, battery control in EVs.

## Related Concepts
- [[trust-region-policy-optimization-trpo]] – predecessor that inspired PPO.
- [[policy-gradient-methods]] – REINFORCE, actor‑critic family.
- [[actor-critic]] – combines value function (critic) with policy (actor).
- [[generalized-advantage-estimation-gae]] – preferred advantage estimator for PPO.
- [[deep-q-network-dqn]] – value‑based alternative for discrete actions.
- [[soft-actor-critic-sac]] – off‑policy actor‑critic with entropy maximization.
- [[deterministic-policy-gradient-dpg]] – for continuous actions.
- [[deep-deterministic-policy-gradient-ddpg]] – actor‑critic for continuous control.
- [[proximal-policy-optimization-ppo]] – see this page.
- [[reinforcement-learning-from-human-feedback-rlhf]] – PPO is often used to fine‑tune LLMs.
- [[natural-language-evolution]] – language emergence via multi‑agent RL.
- [[exploration-strategies]] – epsilon‑greedy, Boltzmann, Thompson sampling, information‑gain bonuses.
- [[curriculum-learning]] – gradually increase task difficulty.
- [[reward-shaping]] – design intermediate rewards to guide learning.
- [[credit-assignment]] – linking delayed rewards to responsible actions.
- [[offline-rl-batch-rl]] – learning from fixed datasets without further interaction.
- [[model-based-rl]] – learns environment dynamics to plan inside the model.
- [[multi-agent-rl]] – independent learners, centralized training decentralized execution (CTDE).
- [[hierarchical-rl]] – options, feudal networks, goal‑conditioned policies.
- [[safe-reinforcement-learning]] – constraints, risk‑sensitive objectives, shielding.
- [[constrained-mdps]] – maximize reward subject to cost constraints.
- [[distributional-rl]] – predict distribution of returns (e.g., C51, QR‑DQN).
- [[quantile-regression]] – used in quantile‑based RL algorithms.
- [[meta-reinforcement-learning]] – learn to learn new RL tasks quickly.
- [[inverse-reinforcement-learning-irl]] – infer reward function from demonstrated behavior.

## See Also
- [[john-schulman]]
- [[openai-baselines]]
- [[stable-baselines3]]
- [[rllib]]
- [[openai-five]]
- [[mujoco]]
- [[dex-nvg]]
- [[rlhf]]
- [[trpo]]
- [[gae]]
- [[actor-critic]]
- [[policy-gradient]]
- [[deep-q-network-dqn]]
- [[soft-actor-critic-sac]]
- [[deterministic-policy-gradient-dpg]]
- [[deep-deterministic-policy-gradient-ddpg]]
- [[reinforcement-learning]]
- [[markov-decision-process-mdp]]
- [[partially-observable-markov-decision-process-pompd]]