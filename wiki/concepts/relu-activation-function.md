---
title: ReLU Activation Function
type: solution
tags:
- solution
- activation-function
- deep-learning
- neural-networks
created: '2026-05-14'
updated: '2026-05-14'
---
--

# ReLU Activation Function

## Definition
The Rectified Linear Unit (ReLU) activation function is defined as f(x) = max(0, x). It introduces non-linearity into neural networks while being computationally efficient and mitigating the vanishing gradient problem compared to sigmoid/tanh activations.

## Historical Context
- **1960s**: Early work on piecewise linear activation functions.
- **2000s**: Hahnloser et al. (2000) analyzed dynamics of networks with piecewise linear activation functions.
- **2010**: Glorot, Bordes, and Bengio (2011) empirically showed ReLU leads to better performance in deep networks.
- **2012**: Krizhevsky et al.'s AlexNet used ReLU, contributing to its ImageNet victory and popularizing ReLU in deep learning.

## Key Contributors
- [[yoshua-bengio]] – empirical validation of ReLU in deep networks.
- [[xavier-glorot]] & [[antoine-bordes]] – co-authors of the 2011 ReLU study.
- [[alex-krizhevsky]], [[ilya-sutskever]], [[geoffrey-hinton]] – used ReLU in AlexNet.
- [[volodymyr-mnih]] et al. – used ReLU in DQN for reinforcement learning.

## How It Solves the Vanishing Gradient Problem
- For positive inputs, gradient is 1 (no saturation).
- For negative inputs, gradient is 0 (can cause "dead neurons" but avoids vanishing gradients).
- Compared to sigmoid/tanh, gradients do not diminish exponentially with depth.

## Variants & Improvements
- **Leaky ReLU** – f(x) = max(αx, x) with small α (e.g., 0.01) to avoid dead neurons.
- **Parametric ReLU (PReLU)** – learns α during training.
- **Randomized ReLU (RReLU)** – α randomized during training.
- **Exponential Linear Unit (ELU)** – smooths negative region.
- **Scaled ELU (SELU)** – self-normalizing properties.
- **Gaussian Error Linear Unit (GELU)** – used in Transformers and BERT.

## Applications
- Almost all modern deep neural networks: CNNs, RNNs, Transformers.
- Computer vision (ImageNet models).
- Natural language processing (though Transformers often use GELU).
- Speech recognition.
- Reinforcement learning (DQN, policy networks).
- Generative models (GANs, VAEs).

## Related Concepts
- [[vanishing-gradient-problem]]
- [[activation-function]]
- [[sigmoid]]
- [[tanh]]
- [[leaky-relu]]
- [[elu]]
- [[gelu]]
- [[deep-learning]]
- [[neural-networks]]

## See Also
- [[deep-learning]]
- [[activation-functions]]
- [[leaky-relu]]
- [[elu]]
- [[gelu]]
- [[alexnet]]