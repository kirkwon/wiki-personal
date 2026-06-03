---
title: Overfitting in Deep Neural Networks
type: problem
tags:
- problem
- deep-learning
- overfitting
- generalization
created: '2026-05-14'
updated: '2026-05-14'
---
--

# Overfitting in Deep Neural Networks

## Definition
Overfitting occurs when a model learns the training data too well, capturing noise and idiosyncrasies that do not generalize to unseen data, resulting in high training accuracy but poor validation/test performance.

## Historical Context
- Observed since early neural network experiments in the 1980s and 1990s.
- Became more pronounced with the rise of deep learning and large parameter counts in the 2010s.
- Notable in image classification tasks (e.g., CIFAR-10, ImageNet) where models memorized training labels.

## Key Contributors
- [[Geoffrey Hinton]] – discussed overfitting and introduced dropout.
- [[Nitish Srivastava]] et al. – formalized dropout technique.
- [[Alex Krizhevsky]] – used dropout in AlexNet.
- [[Yann LeCun]] – early work on regularization and validation.

## Symptoms
- Training loss continues to decrease while validation loss starts to increase.
- Model performs well on training data but poorly on new data.
- High variance in predictions across different training runs.

## Impact
- Wasted computational resources.
- Poor deployment performance.
- Lack of trust in model predictions.

## Solutions
- [[Dropout]]
- [[Batch Normalization]]
- [[Data Augmentation]]
- [[Early Stopping]]
- [[L1/L2 Regularization]]
- [[Ensemble Methods]]

## See Also
- [[Underfitting]]
- [[Bias-Variance Tradeoff]]
- [[Generalization]]
- [[Regularization]]