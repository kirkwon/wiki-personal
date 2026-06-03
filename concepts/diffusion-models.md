---
title: Diffusion Models
type: concept
tags:
- concept
- generative-models
- diffusion
- computer-vision
- machine-learning
created: '2026-05-14'
updated: '2026-05-14'
---
--

# Diffusion Models

## Definition
Diffusion models are a class of generative models that create data by reversing a gradual noising process. They learn to denoise data step-by-step, starting from pure noise and iteratively refining it into realistic samples.

## Historical Context
- **2015**: Sohl-Dickstein et al. introduced "Deep Unsupervised Learning using Nonequilibrium Thermodynamics", laying the theoretical foundation.
- **2020**: Ho et al. proposed Denoising Diffusion Probabilistic Models (DDPM), showing competitive likelihoods.
- **2021**: Song et al. unified score-based models with diffusion, leading to improved sampling.
- **2022**: Stable Diffusion (Rombach et al.) introduced latent diffusion, enabling high-resolution image generation at lower compute cost.
- **2023**: Diffusion models became dominant in text-to-image generation (DALL·E 2, Midjourney, Stable Diffusion).

## Key Contributors
- [[Jascha Sohl-Dickstein]] – foundational nonequilibrium thermodynamics approach.
- [[Jonathan Ho]] – DDPM paper (2020).
- [[Yang Song]] – score-based diffusion and improved samplers.
- [[Robin Rombach]] et al. – Stable Diffusion (latent diffusion).
- [[Chitwan Saharia]] – Imagen (text-to-image diffusion).
- [[Aditya Ramesh]] – DALL·E 2 (diffusion-based).

## Core Process
1. **Forward Diffusion** – gradually add Gaussian noise to data over T steps, approximating a standard normal distribution.
2. **Reverse Diffusion** – learn a neural network to predict and remove noise at each step, reconstructing data from noise.
3. **Training** – optimize a variational bound or simple L2 loss on noise prediction.
4. **Sampling** – start from noise, iteratively apply denoising network to generate samples.

## Variants
- **Denoising Diffusion Probabilistic Models (DDPM)** – original formulation with fixed Markov chain.
- **Denoising Diffusion Implicit Models (DDIM)** – non-Markovian sampling for faster generation.
- **Latent Diffusion Models (LDM)** – apply diffusion in latent space of an autoencoder (e.g., Stable Diffusion).
- **Score-Based Generative Models (SGMs)** – model the gradient of log probability (score) via noise-conditional networks.
- **Classifier-Guided Diffusion** – use classifier gradients for conditional generation.
- **Classifier-Free Guidance** – train unconditional and conditional models together for guidance without separate classifier.

## Applications
- Text-to-image generation (Stable Diffusion, DALL·E 2, Imagen, Midjourney).
- Image inpainting and super-resolution.
- Video generation and prediction.
- Audio synthesis (DiffWave, WaveGrad).
- Molecular generation and drug design.
- Anomaly detection (likelihood estimation).
- Data augmentation and synthesis for training.

## Related Concepts
- [[Generative Adversarial Networks (GANs)]] – alternative generative framework.
- [[Variational Autoencoders (VAEs)]] – likelihood-based generative models.
- [[Autoregressive Models]] – PixelCNN, Transformer-based generation.
- [[Energy-Based Models]] – alternative formulation of diffusion.
- [[Convolutional Neural Networks (CNNs)]] – often used as backbone in diffusion U-Net.
- [[Transformer Models]] – used in some diffusion variants for global context.
- [[Classifier Guidance]] – technique for conditional generation.
- [[Latent Space]] – LDMs operate in compressed latent space.

## See Also
- [[Stable Diffusion]]
- [[DDPM]]
- [[DDIM]]
- [[Latent Diffusion]]
- [[Score-Based Models]]
- [[Generative Models]]
- [[Computer Vision]]
- [[Machine Learning]]