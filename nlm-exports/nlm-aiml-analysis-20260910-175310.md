---
type: nlm-export
title: 'NotebookLM Findings: aiml-analysis'
source: notebooklm
exported: '2026-09-10T17:53:10.354Z'
notebook: aiml-analysis
ingested_via: put_page
ingested_at: '2026-09-11T00:53:14.271Z'
created: '2026-09-11T00:53:14.271Z'
source_kind: put_page
tags:
  - aiml-analysis
  - nlm-export
---

# NotebookLM Findings: aiml-analysis

**Source:** NotebookLM notebook `aiml-analysis`  
**Exported:** 2026-09-10 17:53:10  
**Notebook ID:** 01c7ff35-0645-4a8c-a1fd-9a21117f760a

---

## Findings

### Q1: What are the most important insights from the sources in this notebook?

The sources across this notebook reflect a major paradigm shift in AI 
research—moving from static, single-turn conversational chatbots ("System-1" 
generators) to persistent, self-evolving **agentic systems** ("digital 
colleagues") operating in dynamic, partially observable environments [1-3].

Here are the five most critical insights synthesized from the literature in your
notebook:

---

### 1. Pure RL Elicits Emergent Reasoning, but Token-Level Credit Assignment is 
Key
Reinforcement learning with verifiable rewards (RLVR / "Zero RL") demonstrates 
that pure RL without human-annotated reasoning traces can induce emergent 
cognitive behaviors—such as self-verification, backtracking, parallel reasoning,
and long chain-of-thought planning [4-6]. 
* **The Granularity Gap:** Trajectory-level sparse rewards make credit 
assignment difficult across long interaction horizons [7, 8]. 
* **Implicit Process Supervision:** Recent methods bridge this gap without 
needing dedicated process reward models (PRMs). For instance, **Progress 
Advantage** shows that the log-probability ratio between an RL-trained policy 
and its reference policy naturally recovers an optimal per-step advantage signal
in stochastic environments [9, 10]. Similarly, frameworks like **SEED** and 
**PCSD** convert hindsight skills from completed trajectories into dense, 
token-level on-policy self-distillation signals [7, 8, 11].

### 2. System Capability is Defined by the Harness, Not Just the Model
Agentic performance is a property of the complete **Model + Harness system** 
rather than the foundation model alone [12, 13].
* **Architecture Over Scale:** Scaffolding components—such as dynamic planning, 
fresh-context execution, and independent auditing—dramatically raise the failure
floor of agents [13-15].
* **Manage–Execute–Audit Architecture:** Frameworks like **LongHorizon-Harness**
demonstrate that separating execution from state management and subjecting every
environment modification to an independent read-only auditor allows models 
(e.g., Qwen 3.7-Plus) to outperform far larger models operating in single, 
growing session contexts [14-16].

### 3. Deep Research Capitalizes on Discovery–Verification Asymmetry
Deep research tasks exhibit a fundamental structural property: finding an answer
that satisfies multiple coupled constraints across the open web is 
computationally expensive, whereas evaluating candidate proposals can be broken 
down into simpler, constraint-wise checks [17, 18].
* **Recursive State Refinement:** Systems such as **AREX** and 
**DuMate-DeepResearch** leverage this asymmetry by turning provisional answers 
into partially verified states [18, 19]. Instead of searching blindly, the agent
isolates remaining uncertainties and formulates tighter, better-targeted 
sub-problems for subsequent research rounds [17, 18].
* **Stabilizing Tool Execution:** Algorithmic extensions like **RAPO** (Reward 
Aware Policy Optimization) prune uninformative trajectories and apply steerable 
step-level rewards to stabilize multi-turn web search beyond 20+ tool calls 
without collapsing into tool fatigue or reward hacking [20-22].

### 4. World Models Shift Computation from Acting to Simulating
To avoid costly or irreversible real-world errors, modern agents increasingly 
rely on **world models** as environment proxies to simulate trajectories before 
taking actions [23-25].
* **Architectural Advantage of Diffusion:** Autoregressive models suffer from 
left-to-right causal bias in predicting globally interdependent environment 
states. In contrast, **Masked Diffusion Language Models (MDLMs)** provide 
superior text-based world models, enabling zero-shot GRPO improvements of up to 
47% across downstream agents [24, 26].
* **Mental World Modeling (MWM):** For tasks involving human interactions, world
models must predict both physical state transitions and internal mental states 
(goals, beliefs, obligations) [27, 28]. Omitting the mental state channel 
significantly degrades decision prediction accuracy in interpersonal scenarios 
[27].

### 5. Persistent Personalization Suffers from "Self-Monitoring Inversion"
As agents acquire long-term parametric and non-parametric memories across 
sessions, persistent personalization faces significant safety and fidelity 
challenges [29, 30].
* **Pervasive Over-Inference:** Benchmark evaluations reveal that models 
over-infer or fabricate user attributes in 35%–49% of personalized claims, 
creating silent memory pollution that accumulates over time [29, 30].
* **The Self-Monitoring Inversion:** At the model-selection level, a model's 
self-reported confidence in its personalized claims is *negatively correlated* 
with actual judge-verified accuracy [29, 30]. Consequently, model self-auditing 
cannot be trusted for cross-model safety benchmarks, highlighting the necessity 
of external, independent verification pipelines [29, 30].

---

💡 *Would you like to build an interactive dashboard or a tailored technical 
report summarizing one of these specific areas, such as Agentic RL or Harness 
Engineering?*

Sources:
  [1] 10 Agent Eval Methods (Hanako, Jul 2026)
  [2] 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D 
Question  (2608.01185)
  [3] A Contextual Quality Reward Model for Reliable and Efficient Best-of-N
  Samplin (2510.04087)
  [4] A Frozen Pixel-Space Diffusion Model Can Guide Itself with Its Own Samples
(2607.29122)
  [5] ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked 
Credit Assi (2608.05102)
  [6] AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents 
(2602.06855)
  [7] AISPA: User-Centric System Prompt Auditing for Large Language Model 
Applications (2607.28617)
  [8] AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight 
Speech Emot (2607.25289)
  [9] AREX: Towards a Recursively Self-Improving Agent for Deep Research 
(2607.21461)
  [10] AREX: Towards a Recursively Self-Improving Agent for Deep Research 
(2607.21461)
  [11] ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration 
(2605.03042)
  [12] AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing 
Abilities (2607.24821)
  [13] Absorbing Complexity: An Interaction-Native Knowledge Harness for 
Financial LLM  (2606.01886)
  [14] Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal 
Models (2604.08545)
  [15] Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System 
Deployment  (2606.01770)
  [16] AdvEvo-MARL: Shaping Internalized Safety through Adversarial
  Co-Evolution in M (2510.01586)
  [17] Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces 
(2605.17698)
  [18] Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large
Langua (2602.08004)
  [19] AgentForesight: Online Auditing for Early Failure Prediction in 
Multi-Agent Syst (2605.08715)
  [20] AgentGL: Towards Agentic Graph Learning with LLMs via Reinforcement 
Learning (2604.05846)
  [21] AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming
Tasks? (2608.00155)
  [22] Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design 
(2605.15871)
  [23] Agentic Reasoning for Large Language Models (2601.12538)
  [24] AlphaQuanter: An End-to-End Tool-Orchestrated Agentic Reinforcement
  Learning F (2510.14264)
  [25] Any-OPD: Heterogeneous On-Policy Distillation for Flow-Matching Models 
via Repre (2608.03316)
  [26] BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation 
Paradigms (2607.26497)
  [27] Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for
MLLM-B (2608.02791)
  [28] Beyond Feeling Better: Capability-Sustaining Emotional Dialogue as a 
Longitudina (2607.27851)
  [29] Beyond Geometric Complementarity: Coherent Overlap in Sparse 
Mixture-of-Experts  (2607.28308)
  [30] Beyond Pipelines: A Survey of the Paradigm Shift toward Model-Native
  Agentic A (2510.16720)
  [31] Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement 
Learning (2606.18831)
  [32] Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of
Social (2607.23370)
  [33] Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of
Social (2607.23370)
  [34] Bootstrapping Task Spaces for Self-Improvement (2509.04575)
  [35] Brainstacks: Cross-Domain Cognitive Capabilities via Frozen MoE-LoRA 
Stacks for  (2604.01152)
  [36] BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented 
Vision-Langua (2608.05042)
  [37] Budget-Constrained Agentic Large Language Models: Intention-Based 
Planning for C (2602.11541)
  [38] CAPEval: A Decoupled Caption Evaluation across Understanding and 
Generation (2608.02589)
  [39] CEPO: RLVR Self-Distillation using Contrastive Evidence Policy 
Optimization (2605.19436)
  [40] CLBench-V: Evaluating Multimodal Context Learning from Grounding to 
Knowledge Ac (2607.25294)
  [41] Can LLMs Correct Themselves? — Tie et al 2025
  [42] CausalDS: Benchmarking Causal Reasoning in Data-Science Agents 
(2607.08093)
  [43] CausalDS: Benchmarking Causal Reasoning in Data-Science Agents 
(2607.08093)
  [44] ChronoLens: Measuring Language Change Across Time, Languages, and 
Linguistic Lev (2608.03507)
  [45] CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy 
Optimization (2607.25659)
  [46] Code Aesthetics with Agentic Reward Feedback (2510.23272)
  [47] Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables 
Learning fro (2604.04767)
  [48] Consistency-Driven Co-Evolution for Self-Supervised Cross-Representation 
Learnin (2608.04926)
  [49] Constitutional Midtraining: Content Presence Drives Alignment Gains 
(2607.26654)
  [50] ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities? 
(2608.03874)
  [51] Controlling Reasoning Effort in LLMs
  [52] Cynefin Framework - Complexity Indicators for Effort Routing
  [53] DAPD: Dual-Anchored Policy Distillation (2608.01735)
  [54] DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with 
Adversarial P (2608.03207)
  [55] DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon 
Multimo (2608.01827)
  [56] Deferred Exposure of Future Trajectories for Verifiable Reasoning in 
Autonomous  (2608.01755)
  [57] Discovering Multiagent Learning Algorithms with Large Language Models 
(2602.16928)
  [58] Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups
from A (2608.00782)
  [59] Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems 
(2602.08847)
  [60] DreamTraj: Generating 6-DoF Object Trajectories by Reading Unrendered 
Video Diff (2608.00486)
  [61] DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive 
Search and R (2606.07299)
  [62] ECHO: Terminal Agents Learn World Models for Free (2605.24517)
  [63] ENPIRE: Agentic Robot Policy Self-Improvement in the Real World 
(2606.19980)
  [64] Effort Router - Two-Tier Reasoning Effort Classifier
  [65] Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data 
(2608.02580)
  [66] Enhancing Rubric-based RL via Self-Distillation (2607.18082)
  [67] Enterprise Deep Research: Steerable Multi-Agent Deep Research for
  Enterprise A (2510.17797)
  [68] Evaluation-Verification Reward for Consistent Multi-Reference Image 
Editing (2607.29025)
  [69] EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning 
and Conte (2606.03841)
  [70] EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for 
Autonomous Agent (2606.03108)
  [71] ExplainBench: Evaluating Code Explanations from Agents (2607.26451)
  [72] Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End 
Generati (2607.27372)
  [73] Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via 
Differential A (2607.28319)
  [74] Fathom-DeepResearch: Unlocking Long Horizon Information Retrieval and
  Synthesi (2509.24107)
  [75] Filesystem-Based Memory for LLM Agents: Organization, Evolution, and 
Sustainabil (2607.26637)
  [76] FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use 
(2603.08262)
  [77] Forecasting Probability Distributions of Financial Returns with Deep
  Neural Ne (2508.18921)
  [78] Foundation Protocol: A Coordination Layer for Agentic Society 
(2605.23218)
  [79] Free Lunch Alignment of Text-to-Image Diffusion Models without
  Preference Imag (2509.25771)
  [80] From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent 
Autonomo (2606.14502)
  [81] From Noise to Narrative: Tracing the Origins of Hallucinations in
  Transformers (2509.06938)
  [82] From Passive Metric to Active Signal: The Evolving Role of Uncertainty 
Quantific (2601.15690)
  [83] From Proprietary to Open-Source: Bridging the Distribution Gap via 
Multi-Agent P (2607.24280)
  [84] From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards 
for Open (2607.23802)
  [85] FullStack-Agent: Enhancing Agentic Full-Stack Web Coding via 
Development-Oriente (2602.03798)
  [86] FunReason-MT Technical Report: Overcoming the Complexity Barrier in
  Multi-Turn (2510.24645)
  [87] G-Zero: Self-Play for Open-Ended Generation from Zero Data (2605.09959)
  [88] GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks 
(2608.03764)
  [89] GPT-Red: Automated Red Teaming via Self-Play at Scale (2607.26115)
  [90] GROVE: Growing and Reasoning over Temporally Stratified Memory from 
Streaming Vi (2608.02392)
  [91] GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational 
Automat (2607.05369)
  [92] GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational 
Automat (2607.05369)
  [93] Genomic Next-Token Predictors are In-Context Learners (2511.12797)
  [94] GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable 
Test-Ti (2608.02585)
  [95] GrandCode: Achieving Grandmaster Level in Competitive Programming via 
Agentic Re (2604.02721)
  [96] Graph-Native Reinforcement Learning Enables Traceable Scientific 
Hypothesis Gene (2607.00924)
  [97] HP-Edit: A Human-Preference Post-Training Framework for Image Editing 
(2604.19406)
  [98] HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry 
(2606.14249)
  [99] Healthcare AI GYM for Medical Agents (2605.02943)
  [100] HelloWorld: Enabling Socially Interactive Characters in Video World 
Models (2608.05070)
  [101] Hierarchical Experimentalist Agents (2606.29315)
  [102] Hierarchical Experimentalist Agents (2606.29315)
  [103] Hunyuan3D-Buffalo 1.0: A Unified Multimodal Model for Scalable 3D 
Generation, Un (2608.02711)
  [104] I Know What I Don't Know: Latent Posterior Factor Models for 
Multi-Evidence Prob (2603.15670)
  [105] ICDAR 2026 Competition on Information Extraction from Atomic Layer 
Deposition/Et (2607.26848)
  [106] In the Driver's Seat: A Multi-Company Study on the Reality of Autonomous
Driving (2607.15820)
  [107] InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular 
View Synthe (2608.02437)
  [108] Insight Miner: A Time Series Analysis Dataset for Cross-Domain Alignment
with Na (2512.11251)
  [109] Insight-V++: Towards Advanced Long-Chain Visual Reasoning with 
Multimodal Large  (2603.18118)
  [110] InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search 
(2605.07510)
  [111] Is Deep Research Reliable? Misleading Knowledge Induces False 
Conclusions (2607.20891)
  [112] Is One Layer Enough? Training A Single Transformer Layer Can Match 
Full-Paramete (2607.01232)
  [113] Is One Layer Enough? Training A Single Transformer Layer Can Match 
Full-Paramete (2607.01232)
  [114] JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive
Diffusi (2608.03974)
  [115] K-EXAONE 2.0 Technical Report (2608.04505)
  [116] Know When to Stop: Segment-Level Credit Assignment for Reducing 
Overthinking (2607.00482)
  [117] KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with
Self-Ev (2607.12625)
  [118] KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with
Self-Ev (2607.12625)
  [119] Knowledge-Geometry Decoupling: Refreshable Pretrained Transfer for 
Streaming Rec (2608.02738)
  [120] LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a 
Structure (2607.28374)
  [121] LLM-as-a-Verifier: A General-Purpose Verification Framework (2607.05391)
  [122] LLM-as-a-Verifier: A General-Purpose Verification Framework (2607.05391)
  [123] LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models 
(2608.03457)
  [124] Language Models Need Sleep: Learning to Self-Modify and Consolidate 
Memories (2606.03979)
  [125] Latent Chain-of-Thought for Visual Reasoning (2510.23925)
  [126] LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head 
Generation (2608.00079)
  [127] Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive
  Explorat (2509.22601)
  [128] Learning to Align, Aligning to Learn: A Unified Approach for
  Self-Optimized Al (2508.07750)
  [129] LiveTradeBench: Seeking Real-World Alpha with Large Language Models 
(2511.03628)
  [130] LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks 
(2608.01964)
  [131] Loud or Silent? A Reusable Framework for Per-Modality Failure Analysis 
in Multim (2608.01462)
  [132] MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in 
Molecula (2601.02075)
  [133] Machine Bullshit: Characterizing the Emergent Disregard for Truth in
  Large Lan (2507.07484)
  [134] Masked Diffusion Language Models are Strong and Steerable Text-Based 
World Model (2607.16204)
  [135] Meissa: Multi-modal Medical Agentic Intelligence (2603.09018)
  [136] MemSFT: Mitigating Alignment Tax with an External Parametric Memory 
(2607.25614)
  [137] Mental World Modeling (2607.27201)
  [138] MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in 
E-Commerce Ope (2607.28956)
  [139] Meshy T2: Fast Native Mesh Generation with Flow Matching (2607.28675)
  [140] MiniWorld: Democratizing the Training of Video World Models from Scratch
(2608.01127)
  [141] Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent 
Failures (2607.28802)
  [142] Molt: A Scalable PyTorch-Native Training Framework for Agentic 
Reinforcement Lea (2607.21653)
  [143] Multi-Head Attention Residuals (2607.27230)
  [144] NOLLI: A Difficulty-Calibrated Puzzle Benchmark for Diagnosing the 
English-Korea (2608.04397)
  [145] NVIDIA-labs OO Agents: Native Python Object-Oriented Agents (2607.20709)
  [146] N_0-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent 
Tactile Token (2607.23782)
  [147] Neglected Free Lunch from Post-training: Progress Advantage for LLM 
Agents (2606.26080)
  [148] Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid 
Mamba-Transformer Mo (2606.15007)
  [149] Nexus : An Agentic Framework for Time Series Forecasting (2605.14389)
  [150] Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit 
Reallocat (2607.27888)
  [151] ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow 
(2607.27924)
  [152] OPD-V: Visual On-Policy Self-Distillation with Modality Balance 
(2608.05131)
  [153] OPERA: Offline Policy-guided Expert Routing and Adaptation for Universal
Biomedi (2607.25108)
  [154] OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured 
Recalibration (2605.28805)
  [155] One Future, Every Robot: Label-Efficient Collective-State Prediction 
with Decent (2607.28443)
  [156] OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents 
(2605.05185)
  [157] Orchestra-o1: Omnimodal Agent Orchestration (2606.13707)
  [158] Ovis2.5 Technical Report (2508.11737)
  [159] P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics 
Olympiads (2602.09443)
  [160] P5: Reasoning Models & Skill-to-LoRA Pipeline (2026-06-28)
  [161] PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement 
in Person (2608.04003)
  [162] PCSD: Persistent Consistency for Self-Distillation in Agentic 
Reinforcement Lear (2608.01837)
  [163] ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic 
Video Rei (2605.20342)
  [164] Parallel Decoding Distillation for Fast Image and Video Generation 
(2607.26004)
  [165] Parameter-Efficient Quantum-Inspired Fast Weight Programmers for 
Traffic-Matrix  (2606.27821)
  [166] Pedestrian Archetypes Extension -- More Pedestrian Models for Autonomous
Vehicle (2607.16922)
  [167] Personalization as Inverse Planning: Learning Latent Design Intents for 
Agentic  (2607.00407)
  [168] PhysicsAgentABM: Physics-Guided Generative Agent-Based Modeling 
(2602.06030)
  [169] Poly-OPD: Heterogeneous Multi-Teacher On-Policy Distillation for 
Capability-Sele (2608.04349)
  [170] Poplar: A Scalable Pipeline for Human-Centric Image Dataset Synthesis 
(2608.00440)
  [171] PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable 
Design Diver (2608.02218)
  [172] Presenting a Paper is an Art: Self-Improvement Aesthetic Agents for
  Academic P (2510.05571)
  [173] Progressive Agent Skill Generation via Reinforcement Learning 
(2608.01678)
  [174] Push-Wiper: Toward General-Purpose Robotic Cleaning across Varied Stains
and Sur (2608.00730)
  [175] Q03: Accelerating Learning and Skill Acquisition
  [176] Q04: Symbolic and Energy-Based Models for Reasoning
  [177] QKAN-LSTM: Quantum-inspired Kolmogorov-Arnold Long Short-term Memory 
(2512.05049)
  [178] Qualixar OS: A Universal Operating System for AI Agent Orchestration 
(2604.06392)
  [179] QuantAgent: Price-Driven Multi-Agent LLMs for High-Frequency Trading 
(2509.09995)
  [180] QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining 
(2602.07085)
  [181] Quantitative Risk Management in Volatile Markets with an Expectile-Based
  Frame (2507.13391)
  [182] QuitoBench: A High-Quality Open Time Series Forecasting Benchmark 
(2603.26017)
  [183] Quo Vadis, World Modeling? (2608.02713)
  [184] Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World 
Centric Founda (2607.28227)
  [185] RL^2-VLA: Adaptive RL Latent Compositional Steering with Test-Time 
Scaling for V (2607.26991)
  [186] Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic
Pre-tra (2603.02208)
  [187] RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving 
Recommender System (2607.29241)
  [188] Reinforcement Learning Foundations for Deep Research Systems: A Survey 
(2509.06733)
  [189] Reinforcement Learning for Self-Improving Agent with Skill Library 
(2512.17102)
  [190] Reinforcement Learning via Self-Distillation (2601.20802)
  [191] Relax Within, Balance Across: Geometry-Guided Load Balancing for 
Vision-Language (2608.00574)
  [192] RestoreKV: Recovering Full-Cache Behavior Under Aggressive 
Query-Agnostic KV Cac (2608.01247)
  [193] Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent 
Reasoning (2607.12395)
  [194] Roomer: Reflective Object-Grounded Model Editing and Repair for 3D 
Indoor Layout (2608.01973)
  [195] SAF-OPD: Stable Advantage Fusion for On-Policy Distillation (2607.29209)
  [196] SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in 
Recursive (2603.06333)
  [197] SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from
  Experi (2508.04700)
  [198] SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement 
Learning (2607.14777)
  [199] SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement 
Learning (2607.14777)
  [200] SEVerA: Verified Synthesis of Self-Evolving Agents (2603.25111)
  [201] SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space 
(2608.01397)
  [202] SGTP: Sampling-based Game-Theoretic Planning for Real-Time Multi-Vehicle
Autonom (2607.25388)
  [203] SIGNPOST-Bench: Benchmarking Text-Vision Conflict Resolution in 
Multimodal Large (2608.04244)
  [204] SIMA 2: A Generalist Embodied Agent for Virtual Worlds (2512.04797)
  [205] SKILL-KD: Contrastive Skill Distillation for LLM Agents (2607.28048)
  [206] SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation 
(2608.02287)
  [207] SPICE: Self-Play In Corpus Environments Improves Reasoning (2510.24684)
  [208] SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via
  Multi-Agent Mul (2506.24119)
  [209] ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation 
under Visua (2607.28993)
  [210] STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy 
Entropy Sta (2606.19236)
  [211] SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection 
Benchmark fo (2607.28996)
  [212] SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in 
Reinforcem (2607.10966)
  [213] Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning 
for LLMs v (2601.21590)
  [214] Scaling Agent Learning via Experience Synthesis (2511.03773)
  [215] Scaling Small Agents Through Strategy Auctions (2602.02751)
  [216] ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map 
Points to  (2608.02358)
  [217] Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in 
Agentic Vis (2607.05382)
  [218] Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in 
Agentic Vis (2607.05382)
  [219] Seeing or Knowing? Visual Context Sensitivity in Multimodal Large 
Language Model (2607.26326)
  [220] Self-Evolving Coding Agents (2608.03392)
  [221] Self-Improvements in Modern Agentic Systems: A Survey (2607.13104)
  [222] Self-Improvements in Modern Agentic Systems: A Survey (2607.13104)
  [223] Self-Improving LLM Agents at Test-Time (2510.07841)
  [224] Self-Improving World Modelling with Latent Actions (2602.06130)
  [225] ShadowDancer: Teaching Video World Models Any Action by Learning Unified
Dynamic (2607.28362)
  [226] Single-Rollout Asynchronous Optimization for Agentic Reinforcement 
Learning (2607.07508)
  [227] Skill0.5: Joint Skill Internalization and Utilization for 
Out-of-Distribution Ge (2605.28424)
  [228] SkillJack: Persistent Skill Backdoors in Self-Evolving Agents 
(2608.03509)
  [229] SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution
(2607.26784)
  [230] Smart Timing for Mining: A Deep Learning Framework for Bitcoin Hardware 
ROI Pred (2512.05402)
  [231] SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them 
(2607.27703)
  [232] Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active 
Parameters (2602.10604)
  [233] StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement 
Learning (2604.18401)
  [234] StockBench: Can LLM Agents Trade Stocks Profitably In Real-world
  Markets? (2510.02209)
  [235] Stronger Together: On-Policy Reinforcement Learning for Collaborative
  LLMs (2510.11062)
  [236] StyleForge: Indoor Furniture Styling by Counterfactual Reasoning in a 
Hypergraph (2608.01954)
  [237] SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct
and Zer (2608.02023)
  [238] Synthesizing Behaviorally-Grounded Reasoning Chains: A Data-Generation
  Framewo (2509.14180)
  [239] Synthetic Computers at Scale for Long-Horizon Productivity Simulation 
(2604.28181)
  [240] TRACE: Capability-Targeted Agentic Training (2604.05336)
  [241] TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning 
(2606.32017)
  [242] TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning 
(2606.32017)
  [243] Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care 
(2606.31036)
  [244] Teaching Models to Teach Themselves: Reasoning at the Edge of 
Learnability (2601.18778)
  [245] Tensor Logic: The Language of AI (2510.12269)
  [246] The AI Hippocampus: How Far are We From Human Memory? (2601.09113)
  [247] The Convergence: LLM Novelty Literature Review
  [248] The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in 
Self-Evolving (2602.09877)
  [249] The Landscape of Agentic Reinforcement Learning for LLMs: A Survey 
(2509.02547)
  [250] The Markovian Thinker (Delethink) - 2025
  [251] The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent
Develop (2606.04455)
  [252] The Personalization Mirage: How LLMs Fabricate User Profiles, and Why 
Self-Monit (2608.04570)
  [253] The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to 
Post-train (2607.24720)
  [254] Thinking Beyond Tokens: From Brain-Inspired Intelligence to Cognitive
  Foundati (2507.00951)
  [255] Three Orthogonal Axes for Decision Routing - Cynefin x Stakes x Six Hats
  [256] Time is Not a Label: Continuous Phase Rotation for Temporal Knowledge 
Graphs and (2604.11544)
  [257] TimeSeriesScientist: A General-Purpose AI Agent for Time Series Analysis
(2510.01538)
  [258] Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data 
(2602.21320)
  [259] ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image 
Generation (2608.04436)
  [260] Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training 
Long-Horiz (2608.05139)
  [261] Towards Autonomous and Auditable Medical Imaging Model Development 
(2607.10522)
  [262] Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality 
Synergy, Ear (2608.05000)
  [263] Towards a Science of Scaling Agent Systems (2512.08296)
  [264] Transferability for General Reasoning: An Automated Curriculum for 
Multi-Domain  (2606.25178)
  [265] TreeGRPO: Tree-Advantage GRPO for Online RL Post-Training of Diffusion 
Models (2512.08153)
  [266] TriGlue: a Biology-Inspired Generative Model for Generating Molecular 
Glue-Induc (2607.22143)
  [267] TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated 
Reasoning (2608.04007)
  [268] UEmbed: Unified Sparse and Dense Multimodal Embeddings (2608.02583)
  [269] Understanding Reasoning from Pretraining to Post-Training (2607.16097)
  [270] UniWorld-Design: From Pixel Generation to Layer-Native Design 
(2608.03971)
  [271] UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models 
(2608.04701)
  [272] UserRL: Training Interactive User-Centric Agent via Reinforcement
  Learning (2509.19736)
  [273] VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal
On-Poli (2607.28590)
  [274] VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use 
(2509.01055)
  [275] Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch 
Agent (2608.03979)
  [276] Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified
  Self-Play (2509.25541)
  [277] WCM: A World Critic Model for Vision-Language-Action Reinforcement 
Learning (2607.29613)
  [278] WMPO: World Model-based Policy Optimization for Vision-Language-Action 
Models (2511.09515)
  [279] Weak-to-Strong On-Policy Distillation (2607.26246)
  [280] WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level
  Feedba (2509.22644)
  [281] When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation
Risk, a (2608.03700)
  [282] When Does Muon Help Agentic Reinforcement Learning? (2607.16169)
  [283] When Teachers Mislead: Spurious-Signal-Aware On-Policy Distillation 
(2608.03632)
  [284] Wnuan: Staged Post-Training for Question Answering over Proprietary 
Enterprise K (2608.01862)
  [285] WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon 
Video World  (2608.04964)
  [286] WorldExam: Benchmarking World Models from Apparent Appearance to 
Inherent Reacti (2608.02603)
  [287] Would You Walk to the Car Wash? Revealing the Salience Bias of Large 
Language Mo (2607.28478)
  [288] [2011.04216] DoWhy: An End-to-End Library for Causal Inference
  [289] [2603.03329] AutoHarness: improving LLM agents by automatically 
synthesizing a code harness
  [290] [2606.05922] Evolving Agents in the Dark: Retrospective Harness 
Optimization via Self-Preference
  [291] ai-agents
  [292] convolutional-neural-networks
  [293] diffusion-models
  [294] generative-adversarial-networks
  [295] knowledge-representation
  [296] proximal-policy-optimization
  [297] reinforcement-learning
  [298] stdin-test-2
  [299] uncertainty-in-ai
  [300] β-OPSD: Deriving with Policy Optimization, Training with 
Self-Distillation (2607.28582)

Conversation ID: 1d77c7bf-b3d6-431e-94dc-fe070b64bf58
Use --conversation-id for follow-up questions

---

### Q2: What are the key themes and patterns across all sources?

Sources:
  [1] 10 Agent Eval Methods (Hanako, Jul 2026)
  [2] 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D 
Question  (2608.01185)
  [3] A Contextual Quality Reward Model for Reliable and Efficient Best-of-N
  Samplin (2510.04087)
  [4] A Frozen Pixel-Space Diffusion Model Can Guide Itself with Its Own Samples
(2607.29122)
  [5] ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked 
Credit Assi (2608.05102)
  [6] AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents 
(2602.06855)
  [7] AISPA: User-Centric System Prompt Auditing for Large Language Model 
Applications (2607.28617)
  [8] AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight 
Speech Emot (2607.25289)
  [9] AREX: Towards a Recursively Self-Improving Agent for Deep Research 
(2607.21461)
  [10] AREX: Towards a Recursively Self-Improving Agent for Deep Research 
(2607.21461)
  [11] ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration 
(2605.03042)
  [12] AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing 
Abilities (2607.24821)
  [13] Absorbing Complexity: An Interaction-Native Knowledge Harness for 
Financial LLM  (2606.01886)
  [14] Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal 
Models (2604.08545)
  [15] Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System 
Deployment  (2606.01770)
  [16] AdvEvo-MARL: Shaping Internalized Safety through Adversarial
  Co-Evolution in M (2510.01586)
  [17] Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces 
(2605.17698)
  [18] Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large
Langua (2602.08004)
  [19] AgentForesight: Online Auditing for Early Failure Prediction in 
Multi-Agent Syst (2605.08715)
  [20] AgentGL: Towards Agentic Graph Learning with LLMs via Reinforcement 
Learning (2604.05846)
  [21] AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming
Tasks? (2608.00155)
  [22] Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design 
(2605.15871)
  [23] Agentic Reasoning for Large Language Models (2601.12538)
  [24] AlphaQuanter: An End-to-End Tool-Orchestrated Agentic Reinforcement
  Learning F (2510.14264)
  [25] Any-OPD: Heterogeneous On-Policy Distillation for Flow-Matching Models 
via Repre (2608.03316)
  [26] BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation 
Paradigms (2607.26497)
  [27] Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for
MLLM-B (2608.02791)
  [28] Beyond Feeling Better: Capability-Sustaining Emotional Dialogue as a 
Longitudina (2607.27851)
  [29] Beyond Geometric Complementarity: Coherent Overlap in Sparse 
Mixture-of-Experts  (2607.28308)
  [30] Beyond Pipelines: A Survey of the Paradigm Shift toward Model-Native
  Agentic A (2510.16720)
  [31] Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement 
Learning (2606.18831)
  [32] Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of
Social (2607.23370)
  [33] Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of
Social (2607.23370)
  [34] Bootstrapping Task Spaces for Self-Improvement (2509.04575)
  [35] Brainstacks: Cross-Domain Cognitive Capabilities via Frozen MoE-LoRA 
Stacks for  (2604.01152)
  [36] BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented 
Vision-Langua (2608.05042)
  [37] Budget-Constrained Agentic Large Language Models: Intention-Based 
Planning for C (2602.11541)
  [38] CAPEval: A Decoupled Caption Evaluation across Understanding and 
Generation (2608.02589)
  [39] CEPO: RLVR Self-Distillation using Contrastive Evidence Policy 
Optimization (2605.19436)
  [40] CLBench-V: Evaluating Multimodal Context Learning from Grounding to 
Knowledge Ac (2607.25294)
  [41] Can LLMs Correct Themselves? — Tie et al 2025
  [42] CausalDS: Benchmarking Causal Reasoning in Data-Science Agents 
(2607.08093)
  [43] CausalDS: Benchmarking Causal Reasoning in Data-Science Agents 
(2607.08093)
  [44] ChronoLens: Measuring Language Change Across Time, Languages, and 
Linguistic Lev (2608.03507)
  [45] CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy 
Optimization (2607.25659)
  [46] Code Aesthetics with Agentic Reward Feedback (2510.23272)
  [47] Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables 
Learning fro (2604.04767)
  [48] Consistency-Driven Co-Evolution for Self-Supervised Cross-Representation 
Learnin (2608.04926)
  [49] Constitutional Midtraining: Content Presence Drives Alignment Gains 
(2607.26654)
  [50] ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities? 
(2608.03874)
  [51] Controlling Reasoning Effort in LLMs
  [52] Cynefin Framework - Complexity Indicators for Effort Routing
  [53] DAPD: Dual-Anchored Policy Distillation (2608.01735)
  [54] DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with 
Adversarial P (2608.03207)
  [55] DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon 
Multimo (2608.01827)
  [56] Deferred Exposure of Future Trajectories for Verifiable Reasoning in 
Autonomous  (2608.01755)
  [57] Discovering Multiagent Learning Algorithms with Large Language Models 
(2602.16928)
  [58] Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups
from A (2608.00782)
  [59] Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems 
(2602.08847)
  [60] DreamTraj: Generating 6-DoF Object Trajectories by Reading Unrendered 
Video Diff (2608.00486)
  [61] DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive 
Search and R (2606.07299)
  [62] ECHO: Terminal Agents Learn World Models for Free (2605.24517)
  [63] ENPIRE: Agentic Robot Policy Self-Improvement in the Real World 
(2606.19980)
  [64] Effort Router - Two-Tier Reasoning Effort Classifier
  [65] Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data 
(2608.02580)
  [66] Enhancing Rubric-based RL via Self-Distillation (2607.18082)
  [67] Enterprise Deep Research: Steerable Multi-Agent Deep Research for
  Enterprise A (2510.17797)
  [68] Evaluation-Verification Reward for Consistent Multi-Reference Image 
Editing (2607.29025)
  [69] EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning 
and Conte (2606.03841)
  [70] EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for 
Autonomous Agent (2606.03108)
  [71] ExplainBench: Evaluating Code Explanations from Agents (2607.26451)
  [72] Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End 
Generati (2607.27372)
  [73] Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via 
Differential A (2607.28319)
  [74] Fathom-DeepResearch: Unlocking Long Horizon Information Retrieval and
  Synthesi (2509.24107)
  [75] Filesystem-Based Memory for LLM Agents: Organization, Evolution, and 
Sustainabil (2607.26637)
  [76] FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use 
(2603.08262)
  [77] Forecasting Probability Distributions of Financial Returns with Deep
  Neural Ne (2508.18921)
  [78] Foundation Protocol: A Coordination Layer for Agentic Society 
(2605.23218)
  [79] Free Lunch Alignment of Text-to-Image Diffusion Models without
  Preference Imag (2509.25771)
  [80] From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent 
Autonomo (2606.14502)
  [81] From Noise to Narrative: Tracing the Origins of Hallucinations in
  Transformers (2509.06938)
  [82] From Passive Metric to Active Signal: The Evolving Role of Uncertainty 
Quantific (2601.15690)
  [83] From Proprietary to Open-Source: Bridging the Distribution Gap via 
Multi-Agent P (2607.24280)
  [84] From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards 
for Open (2607.23802)
  [85] FullStack-Agent: Enhancing Agentic Full-Stack Web Coding via 
Development-Oriente (2602.03798)
  [86] FunReason-MT Technical Report: Overcoming the Complexity Barrier in
  Multi-Turn (2510.24645)
  [87] G-Zero: Self-Play for Open-Ended Generation from Zero Data (2605.09959)
  [88] GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks 
(2608.03764)
  [89] GPT-Red: Automated Red Teaming via Self-Play at Scale (2607.26115)
  [90] GROVE: Growing and Reasoning over Temporally Stratified Memory from 
Streaming Vi (2608.02392)
  [91] GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational 
Automat (2607.05369)
  [92] GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational 
Automat (2607.05369)
  [93] Genomic Next-Token Predictors are In-Context Learners (2511.12797)
  [94] GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable 
Test-Ti (2608.02585)
  [95] GrandCode: Achieving Grandmaster Level in Competitive Programming via 
Agentic Re (2604.02721)
  [96] Graph-Native Reinforcement Learning Enables Traceable Scientific 
Hypothesis Gene (2607.00924)
  [97] HP-Edit: A Human-Preference Post-Training Framework for Image Editing 
(2604.19406)
  [98] HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry 
(2606.14249)
  [99] Healthcare AI GYM for Medical Agents (2605.02943)
  [100] HelloWorld: Enabling Socially Interactive Characters in Video World 
Models (2608.05070)
  [101] Hierarchical Experimentalist Agents (2606.29315)
  [102] Hierarchical Experimentalist Agents (2606.29315)
  [103] Hunyuan3D-Buffalo 1.0: A Unified Multimodal Model for Scalable 3D 
Generation, Un (2608.02711)
  [104] I Know What I Don't Know: Latent Posterior Factor Models for 
Multi-Evidence Prob (2603.15670)
  [105] ICDAR 2026 Competition on Information Extraction from Atomic Layer 
Deposition/Et (2607.26848)
  [106] In the Driver's Seat: A Multi-Company Study on the Reality of Autonomous
Driving (2607.15820)
  [107] InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular 
View Synthe (2608.02437)
  [108] Insight Miner: A Time Series Analysis Dataset for Cross-Domain Alignment
with Na (2512.11251)
  [109] Insight-V++: Towards Advanced Long-Chain Visual Reasoning with 
Multimodal Large  (2603.18118)
  [110] InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search 
(2605.07510)
  [111] Is Deep Research Reliable? Misleading Knowledge Induces False 
Conclusions (2607.20891)
  [112] Is One Layer Enough? Training A Single Transformer Layer Can Match 
Full-Paramete (2607.01232)
  [113] Is One Layer Enough? Training A Single Transformer Layer Can Match 
Full-Paramete (2607.01232)
  [114] JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive
Diffusi (2608.03974)
  [115] K-EXAONE 2.0 Technical Report (2608.04505)
  [116] Know When to Stop: Segment-Level Credit Assignment for Reducing 
Overthinking (2607.00482)
  [117] KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with
Self-Ev (2607.12625)
  [118] KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with
Self-Ev (2607.12625)
  [119] Knowledge-Geometry Decoupling: Refreshable Pretrained Transfer for 
Streaming Rec (2608.02738)
  [120] LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a 
Structure (2607.28374)
  [121] LLM-as-a-Verifier: A General-Purpose Verification Framework (2607.05391)
  [122] LLM-as-a-Verifier: A General-Purpose Verification Framework (2607.05391)
  [123] LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models 
(2608.03457)
  [124] Language Models Need Sleep: Learning to Self-Modify and Consolidate 
Memories (2606.03979)
  [125] Latent Chain-of-Thought for Visual Reasoning (2510.23925)
  [126] LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head 
Generation (2608.00079)
  [127] Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive
  Explorat (2509.22601)
  [128] Learning to Align, Aligning to Learn: A Unified Approach for
  Self-Optimized Al (2508.07750)
  [129] LiveTradeBench: Seeking Real-World Alpha with Large Language Models 
(2511.03628)
  [130] LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks 
(2608.01964)
  [131] Loud or Silent? A Reusable Framework for Per-Modality Failure Analysis 
in Multim (2608.01462)
  [132] MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in 
Molecula (2601.02075)
  [133] Machine Bullshit: Characterizing the Emergent Disregard for Truth in
  Large Lan (2507.07484)
  [134] Masked Diffusion Language Models are Strong and Steerable Text-Based 
World Model (2607.16204)
  [135] Meissa: Multi-modal Medical Agentic Intelligence (2603.09018)
  [136] MemSFT: Mitigating Alignment Tax with an External Parametric Memory 
(2607.25614)
  [137] Mental World Modeling (2607.27201)
  [138] MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in 
E-Commerce Ope (2607.28956)
  [139] Meshy T2: Fast Native Mesh Generation with Flow Matching (2607.28675)
  [140] MiniWorld: Democratizing the Training of Video World Models from Scratch
(2608.01127)
  [141] Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent 
Failures (2607.28802)
  [142] Molt: A Scalable PyTorch-Native Training Framework for Agentic 
Reinforcement Lea (2607.21653)
  [143] Multi-Head Attention Residuals (2607.27230)
  [144] NOLLI: A Difficulty-Calibrated Puzzle Benchmark for Diagnosing the 
English-Korea (2608.04397)
  [145] NVIDIA-labs OO Agents: Native Python Object-Oriented Agents (2607.20709)
  [146] N_0-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent 
Tactile Token (2607.23782)
  [147] Neglected Free Lunch from Post-training: Progress Advantage for LLM 
Agents (2606.26080)
  [148] Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid 
Mamba-Transformer Mo (2606.15007)
  [149] Nexus : An Agentic Framework for Time Series Forecasting (2605.14389)
  [150] Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit 
Reallocat (2607.27888)
  [151] ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow 
(2607.27924)
  [152] OPD-V: Visual On-Policy Self-Distillation with Modality Balance 
(2608.05131)
  [153] OPERA: Offline Policy-guided Expert Routing and Adaptation for Universal
Biomedi (2607.25108)
  [154] OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured 
Recalibration (2605.28805)
  [155] One Future, Every Robot: Label-Efficient Collective-State Prediction 
with Decent (2607.28443)
  [156] OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents 
(2605.05185)
  [157] Orchestra-o1: Omnimodal Agent Orchestration (2606.13707)
  [158] Ovis2.5 Technical Report (2508.11737)
  [159] P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics 
Olympiads (2602.09443)
  [160] P5: Reasoning Models & Skill-to-LoRA Pipeline (2026-06-28)
  [161] PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement 
in Person (2608.04003)
  [162] PCSD: Persistent Consistency for Self-Distillation in Agentic 
Reinforcement Lear (2608.01837)
  [163] ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic 
Video Rei (2605.20342)
  [164] Parallel Decoding Distillation for Fast Image and Video Generation 
(2607.26004)
  [165] Parameter-Efficient Quantum-Inspired Fast Weight Programmers for 
Traffic-Matrix  (2606.27821)
  [166] Pedestrian Archetypes Extension -- More Pedestrian Models for Autonomous
Vehicle (2607.16922)
  [167] Personalization as Inverse Planning: Learning Latent Design Intents for 
Agentic  (2607.00407)
  [168] PhysicsAgentABM: Physics-Guided Generative Agent-Based Modeling 
(2602.06030)
  [169] Poly-OPD: Heterogeneous Multi-Teacher On-Policy Distillation for 
Capability-Sele (2608.04349)
  [170] Poplar: A Scalable Pipeline for Human-Centric Image Dataset Synthesis 
(2608.00440)
  [171] PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable 
Design Diver (2608.02218)
  [172] Presenting a Paper is an Art: Self-Improvement Aesthetic Agents for
  Academic P (2510.05571)
  [173] Progressive Agent Skill Generation via Reinforcement Learning 
(2608.01678)
  [174] Push-Wiper: Toward General-Purpose Robotic Cleaning across Varied Stains
and Sur (2608.00730)
  [175] Q03: Accelerating Learning and Skill Acquisition
  [176] Q04: Symbolic and Energy-Based Models for Reasoning
  [177] QKAN-LSTM: Quantum-inspired Kolmogorov-Arnold Long Short-term Memory 
(2512.05049)
  [178] Qualixar OS: A Universal Operating System for AI Agent Orchestration 
(2604.06392)
  [179] QuantAgent: Price-Driven Multi-Agent LLMs for High-Frequency Trading 
(2509.09995)
  [180] QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining 
(2602.07085)
  [181] Quantitative Risk Management in Volatile Markets with an Expectile-Based
  Frame (2507.13391)
  [182] QuitoBench: A High-Quality Open Time Series Forecasting Benchmark 
(2603.26017)
  [183] Quo Vadis, World Modeling? (2608.02713)
  [184] Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World 
Centric Founda (2607.28227)
  [185] RL^2-VLA: Adaptive RL Latent Compositional Steering with Test-Time 
Scaling for V (2607.26991)
  [186] Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic
Pre-tra (2603.02208)
  [187] RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving 
Recommender System (2607.29241)
  [188] Reinforcement Learning Foundations for Deep Research Systems: A Survey 
(2509.06733)
  [189] Reinforcement Learning for Self-Improving Agent with Skill Library 
(2512.17102)
  [190] Reinforcement Learning via Self-Distillation (2601.20802)
  [191] Relax Within, Balance Across: Geometry-Guided Load Balancing for 
Vision-Language (2608.00574)
  [192] RestoreKV: Recovering Full-Cache Behavior Under Aggressive 
Query-Agnostic KV Cac (2608.01247)
  [193] Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent 
Reasoning (2607.12395)
  [194] Roomer: Reflective Object-Grounded Model Editing and Repair for 3D 
Indoor Layout (2608.01973)
  [195] SAF-OPD: Stable Advantage Fusion for On-Policy Distillation (2607.29209)
  [196] SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in 
Recursive (2603.06333)
  [197] SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from
  Experi (2508.04700)
  [198] SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement 
Learning (2607.14777)
  [199] SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement 
Learning (2607.14777)
  [200] SEVerA: Verified Synthesis of Self-Evolving Agents (2603.25111)
  [201] SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space 
(2608.01397)
  [202] SGTP: Sampling-based Game-Theoretic Planning for Real-Time Multi-Vehicle
Autonom (2607.25388)
  [203] SIGNPOST-Bench: Benchmarking Text-Vision Conflict Resolution in 
Multimodal Large (2608.04244)
  [204] SIMA 2: A Generalist Embodied Agent for Virtual Worlds (2512.04797)
  [205] SKILL-KD: Contrastive Skill Distillation for LLM Agents (2607.28048)
  [206] SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation 
(2608.02287)
  [207] SPICE: Self-Play In Corpus Environments Improves Reasoning (2510.24684)
  [208] SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via
  Multi-Agent Mul (2506.24119)
  [209] ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation 
under Visua (2607.28993)
  [210] STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy 
Entropy Sta (2606.19236)
  [211] SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection 
Benchmark fo (2607.28996)
  [212] SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in 
Reinforcem (2607.10966)
  [213] Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning 
for LLMs v (2601.21590)
  [214] Scaling Agent Learning via Experience Synthesis (2511.03773)
  [215] Scaling Small Agents Through Strategy Auctions (2602.02751)
  [216] ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map 
Points to  (2608.02358)
  [217] Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in 
Agentic Vis (2607.05382)
  [218] Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in 
Agentic Vis (2607.05382)
  [219] Seeing or Knowing? Visual Context Sensitivity in Multimodal Large 
Language Model (2607.26326)
  [220] Self-Evolving Coding Agents (2608.03392)
  [221] Self-Improvements in Modern Agentic Systems: A Survey (2607.13104)
  [222] Self-Improvements in Modern Agentic Systems: A Survey (2607.13104)
  [223] Self-Improving LLM Agents at Test-Time (2510.07841)
  [224] Self-Improving World Modelling with Latent Actions (2602.06130)
  [225] ShadowDancer: Teaching Video World Models Any Action by Learning Unified
Dynamic (2607.28362)
  [226] Single-Rollout Asynchronous Optimization for Agentic Reinforcement 
Learning (2607.07508)
  [227] Skill0.5: Joint Skill Internalization and Utilization for 
Out-of-Distribution Ge (2605.28424)
  [228] SkillJack: Persistent Skill Backdoors in Self-Evolving Agents 
(2608.03509)
  [229] SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution
(2607.26784)
  [230] Smart Timing for Mining: A Deep Learning Framework for Bitcoin Hardware 
ROI Pred (2512.05402)
  [231] SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them 
(2607.27703)
  [232] Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active 
Parameters (2602.10604)
  [233] StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement 
Learning (2604.18401)
  [234] StockBench: Can LLM Agents Trade Stocks Profitably In Real-world
  Markets? (2510.02209)
  [235] Stronger Together: On-Policy Reinforcement Learning for Collaborative
  LLMs (2510.11062)
  [236] StyleForge: Indoor Furniture Styling by Counterfactual Reasoning in a 
Hypergraph (2608.01954)
  [237] SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct
and Zer (2608.02023)
  [238] Synthesizing Behaviorally-Grounded Reasoning Chains: A Data-Generation
  Framewo (2509.14180)
  [239] Synthetic Computers at Scale for Long-Horizon Productivity Simulation 
(2604.28181)
  [240] TRACE: Capability-Targeted Agentic Training (2604.05336)
  [241] TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning 
(2606.32017)
  [242] TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning 
(2606.32017)
  [243] Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care 
(2606.31036)
  [244] Teaching Models to Teach Themselves: Reasoning at the Edge of 
Learnability (2601.18778)
  [245] Tensor Logic: The Language of AI (2510.12269)
  [246] The AI Hippocampus: How Far are We From Human Memory? (2601.09113)
  [247] The Convergence: LLM Novelty Literature Review
  [248] The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in 
Self-Evolving (2602.09877)
  [249] The Landscape of Agentic Reinforcement Learning for LLMs: A Survey 
(2509.02547)
  [250] The Markovian Thinker (Delethink) - 2025
  [251] The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent
Develop (2606.04455)
  [252] The Personalization Mirage: How LLMs Fabricate User Profiles, and Why 
Self-Monit (2608.04570)
  [253] The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to 
Post-train (2607.24720)
  [254] Thinking Beyond Tokens: From Brain-Inspired Intelligence to Cognitive
  Foundati (2507.00951)
  [255] Three Orthogonal Axes for Decision Routing - Cynefin x Stakes x Six Hats
  [256] Time is Not a Label: Continuous Phase Rotation for Temporal Knowledge 
Graphs and (2604.11544)
  [257] TimeSeriesScientist: A General-Purpose AI Agent for Time Series Analysis
(2510.01538)
  [258] Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data 
(2602.21320)
  [259] ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image 
Generation (2608.04436)
  [260] Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training 
Long-Horiz (2608.05139)
  [261] Towards Autonomous and Auditable Medical Imaging Model Development 
(2607.10522)
  [262] Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality 
Synergy, Ear (2608.05000)
  [263] Towards a Science of Scaling Agent Systems (2512.08296)
  [264] Transferability for General Reasoning: An Automated Curriculum for 
Multi-Domain  (2606.25178)
  [265] TreeGRPO: Tree-Advantage GRPO for Online RL Post-Training of Diffusion 
Models (2512.08153)
  [266] TriGlue: a Biology-Inspired Generative Model for Generating Molecular 
Glue-Induc (2607.22143)
  [267] TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated 
Reasoning (2608.04007)
  [268] UEmbed: Unified Sparse and Dense Multimodal Embeddings (2608.02583)
  [269] Understanding Reasoning from Pretraining to Post-Training (2607.16097)
  [270] UniWorld-Design: From Pixel Generation to Layer-Native Design 
(2608.03971)
  [271] UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models 
(2608.04701)
  [272] UserRL: Training Interactive User-Centric Agent via Reinforcement
  Learning (2509.19736)
  [273] VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal
On-Poli (2607.28590)
  [274] VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use 
(2509.01055)
  [275] Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch 
Agent (2608.03979)
  [276] Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified
  Self-Play (2509.25541)
  [277] WCM: A World Critic Model for Vision-Language-Action Reinforcement 
Learning (2607.29613)
  [278] WMPO: World Model-based Policy Optimization for Vision-Language-Action 
Models (2511.09515)
  [279] Weak-to-Strong On-Policy Distillation (2607.26246)
  [280] WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level
  Feedba (2509.22644)
  [281] When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation
Risk, a (2608.03700)
  [282] When Does Muon Help Agentic Reinforcement Learning? (2607.16169)
  [283] When Teachers Mislead: Spurious-Signal-Aware On-Policy Distillation 
(2608.03632)
  [284] Wnuan: Staged Post-Training for Question Answering over Proprietary 
Enterprise K (2608.01862)
  [285] WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon 
Video World  (2608.04964)
  [286] WorldExam: Benchmarking World Models from Apparent Appearance to 
Inherent Reacti (2608.02603)
  [287] Would You Walk to the Car Wash? Revealing the Salience Bias of Large 
Language Mo (2607.28478)
  [288] [2011.04216] DoWhy: An End-to-End Library for Causal Inference
  [289] [2603.03329] AutoHarness: improving LLM agents by automatically 
synthesizing a code harness
  [290] [2606.05922] Evolving Agents in the Dark: Retrospective Harness 
Optimization via Self-Preference
  [291] ai-agents
  [292] convolutional-neural-networks
  [293] diffusion-models
  [294] generative-adversarial-networks
  [295] knowledge-representation
  [296] proximal-policy-optimization
  [297] reinforcement-learning
  [298] stdin-test-2
  [299] uncertainty-in-ai
  [300] β-OPSD: Deriving with Policy Optimization, Training with 
Self-Distillation (2607.28582)

Conversation ID: 7804406e-0b79-4e01-bdea-e5a726b503a9
Use --conversation-id for follow-up questions

---

### Q3: What are the main conclusions and recommendations?

Across the research papers and survey syntheses, several foundational 
conclusions and actionable recommendations emerge regarding the trajectory of 
frontier AI models and agentic architectures:

---

### 1. Paradigm Shift: Model-Native Agents & Persistent Workspaces

* **Main Conclusions:**
  * **Transition to Digital Colleagues:** AI systems are evolving from fast, 
single-turn conversational chatbots into persistent "Digital Colleagues" capable
of long-horizon planning, state management, and autonomous execution [1, 2].
  * **Model-Native Internalization:** Capabilities previously managed by 
external pipeline scripts (e.g., planning, tool selection, context management) 
are increasingly being internalized directly into LLM parameters through 
Reinforcement Learning (RL) [3-5].
  * **The "Workspace + Skill" Foundation:** Combining persistent digital 
workspaces (files, terminals, databases) with reusable, parameterizable skill 
packages turns episodic tool use into stateful, reproducible work [6, 7].

* **Recommendations:**
  * Move away from fragile, prompt-scripted pipeline wrappers in favor of 
**end-to-end RL post-training** (LLM + RL + Task) to internalize core 
decision-making [4, 5, 8].
  * Architect agent deployments around **stateful workspaces** paired with 
structured, versionable skill libraries to enable continuous experience reuse 
across sessions [6, 7].

---

### 2. Self-Improvement & Training Mechanics

* **Main Conclusions:**
  * **Limits of Intrinsic Self-Correction:** Intrinsic self-correction (where a 
model critiques itself without external feedback) fails to improve reasoning 
accuracy and frequently degrades it [9]. Effective self-correction requires an 
external verifier, environment signal, or oracle [9].
  * **Emergent Reasoning via RL:** Pure outcome-driven RL (e.g., GRPO / RLVR) 
without human-labeled reasoning steps elicits emergent cognitive strategies such
as self-verification, long chain-of-thought, and dynamic backtracking [10, 11].
  * **Dual Pathways of Evolution:** Agent self-improvement operates along two 
distinct timescales: **parametric updates** to the foundation model (via RL and 
on-policy self-distillation) and **non-parametric scaffold updates** (refining 
prompts, memory indexes, and tool harnesses) [12-14].

* **Recommendations:**
  * Integrate **verifiable outcome rewards** or environment feedback loops 
rather than relying on ungrounded self-critique [5, 9].
  * Utilize autonomous **context-consolidation tools** (such as active context 
updating) to compress long interaction histories into compact improvement 
states, preserving unresolved constraints and verified evidence while 
eliminating redundant logs [15, 16].
  * Combine fast in-context adaptation (curating memory and tools) with slow, 
off-line parameter updates (e.g., on-policy self-distillation) to systematically
lock in capability gains [12, 17, 18].

---

### 3. Multi-Agent Coordination & System Scaling

* **Main Conclusions:**
  * **Heterogeneity Defeats Single-Model Blind Spots:** Pairing executor and 
reviewer agents from distinct model families (e.g., cross-family debate) yields 
significantly more effective critiques and audits than single-model 
self-refinement [19, 20].
  * **Coordination Tax & Error Amplification:** Naively scaling the number of 
agents can degrade performance due to coordination overhead and exponential 
error cascading (amplifying errors up to 17.2× in unverified topologies) [21, 
22].
  * **Decoupling via Structured Protocols:** Decoupling core cognitive reasoning
from superficial stylistic formatting (e.g., using structured JSON/Markdown 
contracts between agents) prevents style drift and verbosity collapse during 
multi-agent distillation [23, 24].

* **Recommendations:**
  * Deploy **heterogeneous multi-agent pairings** (e.g., generator and validator
from different model lineages) for high-stakes auditing and paper/code review 
tasks [19, 20].
  * Implement **centralized verification** and task-contingent routing to curb 
coordination overhead and suppress error propagation [22].
  * Establish clear **artifact contracts** (versioned text files or structured 
schemas) at agent boundaries to ensure auditability and seamless model-backend 
portability [23, 24].

---

### 4. Safety, Alignment & Governance

* **Main Conclusions:**
  * **The Self-Evolution Trilemma:** In fully closed-loop, isolated 
self-evolving agent societies, mutual information regarding safety constraints 
degrades over time, leading to goal drift, consensus hallucinations, and 
progressive alignment erosion [25-27].
  * **The Personalization & Verbosity Trap:** Memory-augmented models tend to 
over-infer user traits from small fact bases, treating unanchored inferences as 
facts and amplifying misconceptions during lossy memory updates [28, 29].

* **Recommendations:**
  * Implement explicit **drift-detection frameworks** (e.g., composite Goal 
Drift Indexing) and constraint-preservation stopping criteria to prevent 
capability optimization from overriding safety boundaries [30, 31].
  * Maintain strict **provenance tracking** for all stored memories and derived 
skills, tagging inferences with epistemic confidence levels and allowing 
human-in-the-loop steering when external knowledge is missing [29, 32-34].

---

💡 *If you'd like to explore any of these specific areas further—such as 
designing a self-improving deep research harness or configuring alignment 
safeguards like SAHOO—let me know how you'd like to proceed!*

Sources:
  [1] 10 Agent Eval Methods (Hanako, Jul 2026)
  [2] 3DZip: Spatial-Aware Feature Diversity-Guided Token Compression for 3D 
Question  (2608.01185)
  [3] A Contextual Quality Reward Model for Reliable and Efficient Best-of-N
  Samplin (2510.04087)
  [4] A Frozen Pixel-Space Diffusion Model Can Guide Itself with Its Own Samples
(2607.29122)
  [5] ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked 
Credit Assi (2608.05102)
  [6] AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents 
(2602.06855)
  [7] AISPA: User-Centric System Prompt Auditing for Large Language Model 
Applications (2607.28617)
  [8] AMRD: Adaptive Multi-Teacher Relational Distillation for Lightweight 
Speech Emot (2607.25289)
  [9] AREX: Towards a Recursively Self-Improving Agent for Deep Research 
(2607.21461)
  [10] AREX: Towards a Recursively Self-Improving Agent for Deep Research 
(2607.21461)
  [11] ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration 
(2605.03042)
  [12] AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing 
Abilities (2607.24821)
  [13] Absorbing Complexity: An Interaction-Native Knowledge Harness for 
Financial LLM  (2606.01886)
  [14] Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal 
Models (2604.08545)
  [15] Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System 
Deployment  (2606.01770)
  [16] AdvEvo-MARL: Shaping Internalized Safety through Adversarial
  Co-Evolution in M (2510.01586)
  [17] Agent Bazaar: Enabling Economic Alignment in Multi-Agent Marketplaces 
(2605.17698)
  [18] Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large
Langua (2602.08004)
  [19] AgentForesight: Online Auditing for Early Failure Prediction in 
Multi-Agent Syst (2605.08715)
  [20] AgentGL: Towards Agentic Graph Learning with LLMs via Reinforcement 
Learning (2604.05846)
  [21] AgentStream: How Well Do Self-Evolving LLM Agents Perform Under Streaming
Tasks? (2608.00155)
  [22] Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design 
(2605.15871)
  [23] Agentic Reasoning for Large Language Models (2601.12538)
  [24] AlphaQuanter: An End-to-End Tool-Orchestrated Agentic Reinforcement
  Learning F (2510.14264)
  [25] Any-OPD: Heterogeneous On-Policy Distillation for Flow-Matching Models 
via Repre (2608.03316)
  [26] BM25 Wins at Scale: A Scaling Study of Retrieval-Augmented Generation 
Paradigms (2607.26497)
  [27] Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for
MLLM-B (2608.02791)
  [28] Beyond Feeling Better: Capability-Sustaining Emotional Dialogue as a 
Longitudina (2607.27851)
  [29] Beyond Geometric Complementarity: Coherent Overlap in Sparse 
Mixture-of-Experts  (2607.28308)
  [30] Beyond Pipelines: A Survey of the Paradigm Shift toward Model-Native
  Agentic A (2510.16720)
  [31] Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement 
Learning (2606.18831)
  [32] Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of
Social (2607.23370)
  [33] Bitcoin Price Direction Prediction via Regime-Aware Multi-Modal Fusion of
Social (2607.23370)
  [34] Bootstrapping Task Spaces for Self-Improvement (2509.04575)
  [35] Brainstacks: Cross-Domain Cognitive Capabilities via Frozen MoE-LoRA 
Stacks for  (2604.01152)
  [36] BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented 
Vision-Langua (2608.05042)
  [37] Budget-Constrained Agentic Large Language Models: Intention-Based 
Planning for C (2602.11541)
  [38] CAPEval: A Decoupled Caption Evaluation across Understanding and 
Generation (2608.02589)
  [39] CEPO: RLVR Self-Distillation using Contrastive Evidence Policy 
Optimization (2605.19436)
  [40] CLBench-V: Evaluating Multimodal Context Learning from Grounding to 
Knowledge Ac (2607.25294)
  [41] Can LLMs Correct Themselves? — Tie et al 2025
  [42] CausalDS: Benchmarking Causal Reasoning in Data-Science Agents 
(2607.08093)
  [43] CausalDS: Benchmarking Causal Reasoning in Data-Science Agents 
(2607.08093)
  [44] ChronoLens: Measuring Language Change Across Time, Languages, and 
Linguistic Lev (2608.03507)
  [45] CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy 
Optimization (2607.25659)
  [46] Code Aesthetics with Agentic Reward Feedback (2510.23272)
  [47] Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables 
Learning fro (2604.04767)
  [48] Consistency-Driven Co-Evolution for Self-Supervised Cross-Representation 
Learnin (2608.04926)
  [49] Constitutional Midtraining: Content Presence Drives Alignment Gains 
(2607.26654)
  [50] ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities? 
(2608.03874)
  [51] Controlling Reasoning Effort in LLMs
  [52] Cynefin Framework - Complexity Indicators for Effort Routing
  [53] DAPD: Dual-Anchored Policy Distillation (2608.01735)
  [54] DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with 
Adversarial P (2608.03207)
  [55] DeepVoyager-VL: Incentivizing Vision-in-the-Loop Search for Long-Horizon 
Multimo (2608.01827)
  [56] Deferred Exposure of Future Trajectories for Verifiable Reasoning in 
Autonomous  (2608.01755)
  [57] Discovering Multiagent Learning Algorithms with Large Language Models 
(2602.16928)
  [58] Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups
from A (2608.00782)
  [59] Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems 
(2602.08847)
  [60] DreamTraj: Generating 6-DoF Object Trajectories by Reading Unrendered 
Video Diff (2608.00486)
  [61] DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive 
Search and R (2606.07299)
  [62] ECHO: Terminal Agents Learn World Models for Free (2605.24517)
  [63] ENPIRE: Agentic Robot Policy Self-Improvement in the Real World 
(2606.19980)
  [64] Effort Router - Two-Tier Reasoning Effort Classifier
  [65] Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data 
(2608.02580)
  [66] Enhancing Rubric-based RL via Self-Distillation (2607.18082)
  [67] Enterprise Deep Research: Steerable Multi-Agent Deep Research for
  Enterprise A (2510.17797)
  [68] Evaluation-Verification Reward for Consistent Multi-Reference Image 
Editing (2607.29025)
  [69] EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning 
and Conte (2606.03841)
  [70] EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for 
Autonomous Agent (2606.03108)
  [71] ExplainBench: Evaluating Code Explanations from Agents (2607.26451)
  [72] Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End 
Generati (2607.27372)
  [73] Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via 
Differential A (2607.28319)
  [74] Fathom-DeepResearch: Unlocking Long Horizon Information Retrieval and
  Synthesi (2509.24107)
  [75] Filesystem-Based Memory for LLM Agents: Organization, Evolution, and 
Sustainabil (2607.26637)
  [76] FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use 
(2603.08262)
  [77] Forecasting Probability Distributions of Financial Returns with Deep
  Neural Ne (2508.18921)
  [78] Foundation Protocol: A Coordination Layer for Agentic Society 
(2605.23218)
  [79] Free Lunch Alignment of Text-to-Image Diffusion Models without
  Preference Imag (2509.25771)
  [80] From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent 
Autonomo (2606.14502)
  [81] From Noise to Narrative: Tracing the Origins of Hallucinations in
  Transformers (2509.06938)
  [82] From Passive Metric to Active Signal: The Evolving Role of Uncertainty 
Quantific (2601.15690)
  [83] From Proprietary to Open-Source: Bridging the Distribution Gap via 
Multi-Agent P (2607.24280)
  [84] From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards 
for Open (2607.23802)
  [85] FullStack-Agent: Enhancing Agentic Full-Stack Web Coding via 
Development-Oriente (2602.03798)
  [86] FunReason-MT Technical Report: Overcoming the Complexity Barrier in
  Multi-Turn (2510.24645)
  [87] G-Zero: Self-Play for Open-Ended Generation from Zero Data (2605.09959)
  [88] GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks 
(2608.03764)
  [89] GPT-Red: Automated Red Teaming via Self-Play at Scale (2607.26115)
  [90] GROVE: Growing and Reasoning over Temporally Stratified Memory from 
Streaming Vi (2608.02392)
  [91] GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational 
Automat (2607.05369)
  [92] GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational 
Automat (2607.05369)
  [93] Genomic Next-Token Predictors are In-Context Learners (2511.12797)
  [94] GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable 
Test-Ti (2608.02585)
  [95] GrandCode: Achieving Grandmaster Level in Competitive Programming via 
Agentic Re (2604.02721)
  [96] Graph-Native Reinforcement Learning Enables Traceable Scientific 
Hypothesis Gene (2607.00924)
  [97] HP-Edit: A Human-Preference Post-Training Framework for Image Editing 
(2604.19406)
  [98] HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry 
(2606.14249)
  [99] Healthcare AI GYM for Medical Agents (2605.02943)
  [100] HelloWorld: Enabling Socially Interactive Characters in Video World 
Models (2608.05070)
  [101] Hierarchical Experimentalist Agents (2606.29315)
  [102] Hierarchical Experimentalist Agents (2606.29315)
  [103] Hunyuan3D-Buffalo 1.0: A Unified Multimodal Model for Scalable 3D 
Generation, Un (2608.02711)
  [104] I Know What I Don't Know: Latent Posterior Factor Models for 
Multi-Evidence Prob (2603.15670)
  [105] ICDAR 2026 Competition on Information Extraction from Atomic Layer 
Deposition/Et (2607.26848)
  [106] In the Driver's Seat: A Multi-Company Study on the Reality of Autonomous
Driving (2607.15820)
  [107] InfiniSplat: Implicit Gaussian Decoding for Large-Baseline Monocular 
View Synthe (2608.02437)
  [108] Insight Miner: A Time Series Analysis Dataset for Cross-Domain Alignment
with Na (2512.11251)
  [109] Insight-V++: Towards Advanced Long-Chain Visual Reasoning with 
Multimodal Large  (2603.18118)
  [110] InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search 
(2605.07510)
  [111] Is Deep Research Reliable? Misleading Knowledge Induces False 
Conclusions (2607.20891)
  [112] Is One Layer Enough? Training A Single Transformer Layer Can Match 
Full-Paramete (2607.01232)
  [113] Is One Layer Enough? Training A Single Transformer Layer Can Match 
Full-Paramete (2607.01232)
  [114] JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive
Diffusi (2608.03974)
  [115] K-EXAONE 2.0 Technical Report (2608.04505)
  [116] Know When to Stop: Segment-Level Credit Assignment for Reducing 
Overthinking (2607.00482)
  [117] KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with
Self-Ev (2607.12625)
  [118] KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with
Self-Ev (2607.12625)
  [119] Knowledge-Geometry Decoupling: Refreshable Pretrained Transfer for 
Streaming Rec (2608.02738)
  [120] LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a 
Structure (2607.28374)
  [121] LLM-as-a-Verifier: A General-Purpose Verification Framework (2607.05391)
  [122] LLM-as-a-Verifier: A General-Purpose Verification Framework (2607.05391)
  [123] LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models 
(2608.03457)
  [124] Language Models Need Sleep: Learning to Self-Modify and Consolidate 
Memories (2606.03979)
  [125] Latent Chain-of-Thought for Visual Reasoning (2510.23925)
  [126] LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head 
Generation (2608.00079)
  [127] Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive
  Explorat (2509.22601)
  [128] Learning to Align, Aligning to Learn: A Unified Approach for
  Self-Optimized Al (2508.07750)
  [129] LiveTradeBench: Seeking Real-World Alpha with Large Language Models 
(2511.03628)
  [130] LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks 
(2608.01964)
  [131] Loud or Silent? A Reusable Framework for Per-Modality Failure Analysis 
in Multim (2608.01462)
  [132] MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in 
Molecula (2601.02075)
  [133] Machine Bullshit: Characterizing the Emergent Disregard for Truth in
  Large Lan (2507.07484)
  [134] Masked Diffusion Language Models are Strong and Steerable Text-Based 
World Model (2607.16204)
  [135] Meissa: Multi-modal Medical Agentic Intelligence (2603.09018)
  [136] MemSFT: Mitigating Alignment Tax with an External Parametric Memory 
(2607.25614)
  [137] Mental World Modeling (2607.27201)
  [138] MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in 
E-Commerce Ope (2607.28956)
  [139] Meshy T2: Fast Native Mesh Generation with Flow Matching (2607.28675)
  [140] MiniWorld: Democratizing the Training of Video World Models from Scratch
(2608.01127)
  [141] Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent 
Failures (2607.28802)
  [142] Molt: A Scalable PyTorch-Native Training Framework for Agentic 
Reinforcement Lea (2607.21653)
  [143] Multi-Head Attention Residuals (2607.27230)
  [144] NOLLI: A Difficulty-Calibrated Puzzle Benchmark for Diagnosing the 
English-Korea (2608.04397)
  [145] NVIDIA-labs OO Agents: Native Python Object-Oriented Agents (2607.20709)
  [146] N_0-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent 
Tactile Token (2607.23782)
  [147] Neglected Free Lunch from Post-training: Progress Advantage for LLM 
Agents (2606.26080)
  [148] Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid 
Mamba-Transformer Mo (2606.15007)
  [149] Nexus : An Agentic Framework for Time Series Forecasting (2605.14389)
  [150] Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit 
Reallocat (2607.27888)
  [151] ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow 
(2607.27924)
  [152] OPD-V: Visual On-Policy Self-Distillation with Modality Balance 
(2608.05131)
  [153] OPERA: Offline Policy-guided Expert Routing and Adaptation for Universal
Biomedi (2607.25108)
  [154] OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured 
Recalibration (2605.28805)
  [155] One Future, Every Robot: Label-Efficient Collective-State Prediction 
with Decent (2607.28443)
  [156] OpenSearch-VL: An Open Recipe for Frontier Multimodal Search Agents 
(2605.05185)
  [157] Orchestra-o1: Omnimodal Agent Orchestration (2606.13707)
  [158] Ovis2.5 Technical Report (2508.11737)
  [159] P1-VL: Bridging Visual Perception and Scientific Reasoning in Physics 
Olympiads (2602.09443)
  [160] P5: Reasoning Models & Skill-to-LoRA Pipeline (2026-06-28)
  [161] PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement 
in Person (2608.04003)
  [162] PCSD: Persistent Consistency for Self-Distillation in Agentic 
Reinforcement Lear (2608.01837)
  [163] ParaVT: Taming the Tool Prior Paradox for Parallel Tool Use in Agentic 
Video Rei (2605.20342)
  [164] Parallel Decoding Distillation for Fast Image and Video Generation 
(2607.26004)
  [165] Parameter-Efficient Quantum-Inspired Fast Weight Programmers for 
Traffic-Matrix  (2606.27821)
  [166] Pedestrian Archetypes Extension -- More Pedestrian Models for Autonomous
Vehicle (2607.16922)
  [167] Personalization as Inverse Planning: Learning Latent Design Intents for 
Agentic  (2607.00407)
  [168] PhysicsAgentABM: Physics-Guided Generative Agent-Based Modeling 
(2602.06030)
  [169] Poly-OPD: Heterogeneous Multi-Teacher On-Policy Distillation for 
Capability-Sele (2608.04349)
  [170] Poplar: A Scalable Pipeline for Human-Centric Image Dataset Synthesis 
(2608.00440)
  [171] PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable 
Design Diver (2608.02218)
  [172] Presenting a Paper is an Art: Self-Improvement Aesthetic Agents for
  Academic P (2510.05571)
  [173] Progressive Agent Skill Generation via Reinforcement Learning 
(2608.01678)
  [174] Push-Wiper: Toward General-Purpose Robotic Cleaning across Varied Stains
and Sur (2608.00730)
  [175] Q03: Accelerating Learning and Skill Acquisition
  [176] Q04: Symbolic and Energy-Based Models for Reasoning
  [177] QKAN-LSTM: Quantum-inspired Kolmogorov-Arnold Long Short-term Memory 
(2512.05049)
  [178] Qualixar OS: A Universal Operating System for AI Agent Orchestration 
(2604.06392)
  [179] QuantAgent: Price-Driven Multi-Agent LLMs for High-Frequency Trading 
(2509.09995)
  [180] QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining 
(2602.07085)
  [181] Quantitative Risk Management in Volatile Markets with an Expectile-Based
  Frame (2507.13391)
  [182] QuitoBench: A High-Quality Open Time Series Forecasting Benchmark 
(2603.26017)
  [183] Quo Vadis, World Modeling? (2608.02713)
  [184] Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World 
Centric Founda (2607.28227)
  [185] RL^2-VLA: Adaptive RL Latent Compositional Steering with Test-Time 
Scaling for V (2607.26991)
  [186] Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic
Pre-tra (2603.02208)
  [187] RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving 
Recommender System (2607.29241)
  [188] Reinforcement Learning Foundations for Deep Research Systems: A Survey 
(2509.06733)
  [189] Reinforcement Learning for Self-Improving Agent with Skill Library 
(2512.17102)
  [190] Reinforcement Learning via Self-Distillation (2601.20802)
  [191] Relax Within, Balance Across: Geometry-Guided Load Balancing for 
Vision-Language (2608.00574)
  [192] RestoreKV: Recovering Full-Cache Behavior Under Aggressive 
Query-Agnostic KV Cac (2608.01247)
  [193] Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent 
Reasoning (2607.12395)
  [194] Roomer: Reflective Object-Grounded Model Editing and Repair for 3D 
Indoor Layout (2608.01973)
  [195] SAF-OPD: Stable Advantage Fusion for On-Policy Distillation (2607.29209)
  [196] SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in 
Recursive (2603.06333)
  [197] SEAgent: Self-Evolving Computer Use Agent with Autonomous Learning from
  Experi (2508.04700)
  [198] SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement 
Learning (2607.14777)
  [199] SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement 
Learning (2607.14777)
  [200] SEVerA: Verified Synthesis of Self-Evolving Agents (2603.25111)
  [201] SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space 
(2608.01397)
  [202] SGTP: Sampling-based Game-Theoretic Planning for Real-Time Multi-Vehicle
Autonom (2607.25388)
  [203] SIGNPOST-Bench: Benchmarking Text-Vision Conflict Resolution in 
Multimodal Large (2608.04244)
  [204] SIMA 2: A Generalist Embodied Agent for Virtual Worlds (2512.04797)
  [205] SKILL-KD: Contrastive Skill Distillation for LLM Agents (2607.28048)
  [206] SKT: Skill-Use Training at Scale via Verified Synthetic Data Generation 
(2608.02287)
  [207] SPICE: Self-Play In Corpus Environments Improves Reasoning (2510.24684)
  [208] SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via
  Multi-Agent Mul (2506.24119)
  [209] ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation 
under Visua (2607.28993)
  [210] STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy 
Entropy Sta (2606.19236)
  [211] SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection 
Benchmark fo (2607.28996)
  [212] SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in 
Reinforcem (2607.10966)
  [213] Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning 
for LLMs v (2601.21590)
  [214] Scaling Agent Learning via Experience Synthesis (2511.03773)
  [215] Scaling Small Agents Through Strategy Auctions (2602.02751)
  [216] ScrambleToolBench: Agents Search Exhaustively Even When Their Own Map 
Points to  (2608.02358)
  [217] Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in 
Agentic Vis (2607.05382)
  [218] Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in 
Agentic Vis (2607.05382)
  [219] Seeing or Knowing? Visual Context Sensitivity in Multimodal Large 
Language Model (2607.26326)
  [220] Self-Evolving Coding Agents (2608.03392)
  [221] Self-Improvements in Modern Agentic Systems: A Survey (2607.13104)
  [222] Self-Improvements in Modern Agentic Systems: A Survey (2607.13104)
  [223] Self-Improving LLM Agents at Test-Time (2510.07841)
  [224] Self-Improving World Modelling with Latent Actions (2602.06130)
  [225] ShadowDancer: Teaching Video World Models Any Action by Learning Unified
Dynamic (2607.28362)
  [226] Single-Rollout Asynchronous Optimization for Agentic Reinforcement 
Learning (2607.07508)
  [227] Skill0.5: Joint Skill Internalization and Utilization for 
Out-of-Distribution Ge (2605.28424)
  [228] SkillJack: Persistent Skill Backdoors in Self-Evolving Agents 
(2608.03509)
  [229] SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution
(2607.26784)
  [230] Smart Timing for Mining: A Deep Learning Framework for Bitcoin Hardware 
ROI Pred (2512.05402)
  [231] SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them 
(2607.27703)
  [232] Step 3.5 Flash: Open Frontier-Level Intelligence with 11B Active 
Parameters (2602.10604)
  [233] StepPO: Step-Aligned Policy Optimization for Agentic Reinforcement 
Learning (2604.18401)
  [234] StockBench: Can LLM Agents Trade Stocks Profitably In Real-world
  Markets? (2510.02209)
  [235] Stronger Together: On-Policy Reinforcement Learning for Collaborative
  LLMs (2510.11062)
  [236] StyleForge: Indoor Furniture Styling by Counterfactual Reasoning in a 
Hypergraph (2608.01954)
  [237] SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct
and Zer (2608.02023)
  [238] Synthesizing Behaviorally-Grounded Reasoning Chains: A Data-Generation
  Framewo (2509.14180)
  [239] Synthetic Computers at Scale for Long-Horizon Productivity Simulation 
(2604.28181)
  [240] TRACE: Capability-Targeted Agentic Training (2604.05336)
  [241] TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning 
(2606.32017)
  [242] TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning 
(2606.32017)
  [243] Teaching LLMs to Recommend and Defer in Underrepresented Epilepsy Care 
(2606.31036)
  [244] Teaching Models to Teach Themselves: Reasoning at the Edge of 
Learnability (2601.18778)
  [245] Tensor Logic: The Language of AI (2510.12269)
  [246] The AI Hippocampus: How Far are We From Human Memory? (2601.09113)
  [247] The Convergence: LLM Novelty Literature Review
  [248] The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in 
Self-Evolving (2602.09877)
  [249] The Landscape of Agentic Reinforcement Learning for LLMs: A Survey 
(2509.02547)
  [250] The Markovian Thinker (Delethink) - 2025
  [251] The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent
Develop (2606.04455)
  [252] The Personalization Mirage: How LLMs Fabricate User Profiles, and Why 
Self-Monit (2608.04570)
  [253] The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to 
Post-train (2607.24720)
  [254] Thinking Beyond Tokens: From Brain-Inspired Intelligence to Cognitive
  Foundati (2507.00951)
  [255] Three Orthogonal Axes for Decision Routing - Cynefin x Stakes x Six Hats
  [256] Time is Not a Label: Continuous Phase Rotation for Temporal Knowledge 
Graphs and (2604.11544)
  [257] TimeSeriesScientist: A General-Purpose AI Agent for Time Series Analysis
(2510.01538)
  [258] Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data 
(2602.21320)
  [259] ToolArtist: Tool-Using Unified Multimodal Models for Agentic Image 
Generation (2608.04436)
  [260] Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training 
Long-Horiz (2608.05139)
  [261] Towards Autonomous and Auditable Medical Imaging Model Development 
(2607.10522)
  [262] Towards Physics of Multimodal Pretraining: Knowledge Flow, Modality 
Synergy, Ear (2608.05000)
  [263] Towards a Science of Scaling Agent Systems (2512.08296)
  [264] Transferability for General Reasoning: An Automated Curriculum for 
Multi-Domain  (2606.25178)
  [265] TreeGRPO: Tree-Advantage GRPO for Online RL Post-Training of Diffusion 
Models (2512.08153)
  [266] TriGlue: a Biology-Inspired Generative Model for Generating Molecular 
Glue-Induc (2607.22143)
  [267] TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated 
Reasoning (2608.04007)
  [268] UEmbed: Unified Sparse and Dense Multimodal Embeddings (2608.02583)
  [269] Understanding Reasoning from Pretraining to Post-Training (2607.16097)
  [270] UniWorld-Design: From Pixel Generation to Layer-Native Design 
(2608.03971)
  [271] UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models 
(2608.04701)
  [272] UserRL: Training Interactive User-Centric Agent via Reinforcement
  Learning (2509.19736)
  [273] VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal
On-Poli (2607.28590)
  [274] VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use 
(2509.01055)
  [275] Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch 
Agent (2608.03979)
  [276] Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified
  Self-Play (2509.25541)
  [277] WCM: A World Critic Model for Vision-Language-Action Reinforcement 
Learning (2607.29613)
  [278] WMPO: World Model-based Policy Optimization for Vision-Language-Action 
Models (2511.09515)
  [279] Weak-to-Strong On-Policy Distillation (2607.26246)
  [280] WebGen-Agent: Enhancing Interactive Website Generation with Multi-Level
  Feedba (2509.22644)
  [281] When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation
Risk, a (2608.03700)
  [282] When Does Muon Help Agentic Reinforcement Learning? (2607.16169)
  [283] When Teachers Mislead: Spurious-Signal-Aware On-Policy Distillation 
(2608.03632)
  [284] Wnuan: Staged Post-Training for Question Answering over Proprietary 
Enterprise K (2608.01862)
  [285] WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon 
Video World  (2608.04964)
  [286] WorldExam: Benchmarking World Models from Apparent Appearance to 
Inherent Reacti (2608.02603)
  [287] Would You Walk to the Car Wash? Revealing the Salience Bias of Large 
Language Mo (2607.28478)
  [288] [2011.04216] DoWhy: An End-to-End Library for Causal Inference
  [289] [2603.03329] AutoHarness: improving LLM agents by automatically 
synthesizing a code harness
  [290] [2606.05922] Evolving Agents in the Dark: Retrospective Harness 
Optimization via Self-Preference
  [291] ai-agents
  [292] convolutional-neural-networks
  [293] diffusion-models
  [294] generative-adversarial-networks
  [295] knowledge-representation
  [296] proximal-policy-optimization
  [297] reinforcement-learning
  [298] stdin-test-2
  [299] uncertainty-in-ai
  [300] β-OPSD: Deriving with Policy Optimization, Training with 
Self-Distillation (2607.28582)

Conversation ID: f22c1da3-4e55-4e1a-8ad5-5c98dd45df92
Use --conversation-id for follow-up questions

---

*Auto-generated from NotebookLM → GBrain export pipeline*
