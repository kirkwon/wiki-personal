---
date: 2026-05-14
title: Convolutional Neural Networks (CNNs)
description: "Convolutional Neural Networks (CNNs)"
type: concept
tags:
- concept
- deep-learning
- computer-vision
- convolution
created: '2026-05-14'
updated: '2026-05-14'
---
--

# Convolutional Neural Networks (CNNs)

## Definition
A Convolutional Neural Network (CNN) is a class of deep neural networks most commonly applied to analyzing visual imagery. CNNs use convolutional layers that apply filters to input data, enabling the network to learn spatial hierarchies of features automatically.

## Historical Context
- **1980s**: Kunihiko Fukushima's Neocognitron introduced hierarchical feature extraction.
- **1998**: Yann LeCun et al. developed LeNet-5 for handwritten digit recognition, demonstrating practical success of CNNs.
- **2012**: AlexNet (Krizhevsky, Sutskever, Hinton) won ImageNet LSVRC-2012, popularizing deep CNNs.
- **2014**: VGGNet (Simonyan & Zisserman) showed that depth is crucial for performance.
- **2015**: ResNet (He et al.) introduced residual connections, enabling very deep networks (>100 layers).

## Key Contributors
- [[yann-lecun]] – LeNet-5, foundational work.
- [[geoffrey-hinton]] – AlexNet, deep learning advocacy.
- [[alex-krizhevsky]] – AlexNet implementation.
- [[karen-simonyan]] & [[andrew-zisserman]] – VGGNet.
- [[kaiming-he]] et al. – ResNet.

## Core Components
1. **Convolutional Layer** – applies learnable filters (kernels) to input.
2. **Activation Function** – typically ReLU introduces non-linearity.
3. **Pooling Layer** – reduces spatial dimensions (max/average pooling).
4. **Fully Connected Layer** – performs classification based on extracted features.
5. **Normalization Layer** – e.g., Batch Normalization stabilizes training.

## Variants & Architectures
- **LeNet-5** – early digit recognition.
- **AlexNet** – 8 layers, introduced dropout and ReLU.
- **VGGNet** – uniform 3x3 filters, increased depth.
- **GoogLeNet / Inception** – inception modules with multi-scale filtering.
- **ResNet** – residual blocks solve vanishing gradient problem.
- **DenseNet** – dense connections improve feature reuse.
- **MobileNet** – depthwise separable convolutions for efficiency.
- **EfficientNet** – compound scaling of depth, width, resolution.

## Applications
- Image classification (ImageNet, medical imaging).
- Object detection (Faster R-CNN, YOLO, SSD).
- Semantic segmentation (U-Net, DeepLab).
- Video action recognition (3D CNNs, SlowFast).
- Natural language processing (1D convolutions for text).
- Speech processing (raw waveform CNNs).

## Related Concepts
- [[vision-transformers]] – alternative architecture using self-attention.
- [[diffusion-models]] – generative models that can be combined with CNNs.
- [[transfer-learning]] – pretrained CNNs as feature extractors.
- [[data-augmentation]] – improves generalization for vision tasks.
- [[explainable-ai]] – techniques like Grad-CNN for CNN interpretability.

## See Also
- [[deep-learning]]
- [[computer-vision]]
- [[imagenet]]
- [[lenet-5]]
- [[alexnet]]
- [[vggnet]]
- [[resnet]]