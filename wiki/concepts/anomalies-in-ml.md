---
type: concept
title: Anomalies and Exceptions in Machine Learning
description: "--
Anomalies and Exceptions in Machine Learning"
created: 2026-04-29
updated: 2026-04-29
tags:
- ai-safety
- technology
- machine-learning
sources:
- The Alignment Problem - Brian Christian  Tom Griffiths.md
related:
- consistency-in-ai
- alignment
- ai-safety-methods
---
--
# Anomalies and Exceptions in Machine Learning

Anomalies and exceptions are edge cases where machine learning models encounter inputs or situations that differ significantly from their training data. As covered in [[the-alignment-problem---brian-christian-tom-griffiths]], these cases are a primary source of misalignment between AI systems and real-world expectations.

Key issues:
- Models trained on typical data may behave unpredictably or incorrectly when faced with rare or novel inputs.
- Anomalies can expose gaps between the model's learned behavior and actual human values.
- Managing exceptions requires strategies beyond simple rule-based approaches, since the space of possible anomalies is vast.

This connects to [[intractable-computation]]—thoroughly testing for all possible exceptions is computationally infeasible, so alignment methods must prioritize and handle anomalies strategically.