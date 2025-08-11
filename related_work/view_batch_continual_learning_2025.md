# Do Your Best and Get Enough Rest for Continual Learning (2025)

**Authors**: Hankyul Kang, Gregor Seifer, Donghyun Lee, Jongbin Ryu  
**Venue**: IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) 2025  
**ArXiv**: 2503.18371  
**URL**: https://arxiv.org/abs/2503.18371

## CS197 Analysis Framework

### Problem
Catastrophic forgetting in continual learning where neural networks lose performance on previously learned tasks when learning new ones. Current methods fail to leverage insights from human memory research.

### Prior Assumptions in Literature
- Experience replay should be constant and continuous
- Rest periods between learning sessions are unnecessary
- Random sampling from memory buffers is optimal
- Human learning principles don't apply to neural networks

### Key Insight
Direct application of Ebbinghaus' forgetting curve theory: **learning extensive data requires sufficient rest before relearning the same data**. Introduces view-batch model that optimizes recall intervals between retraining the same samples.

### Technical Approach
**View-Batch Model with two components:**
1. **Replay method** guaranteeing optimal recall intervals based on forgetting curve theory
2. **Self-supervised learning** acquiring extensive knowledge from single training samples

**Implementation:**
- Adjusts learning schedules to optimize recall intervals
- Allows network sufficient "rest" to consolidate knowledge
- Periodic retraining aligned with forgetting curves

### Evaluation
- **Datasets**: Split MNIST, Split CIFAR-100
- **Metrics**: Final accuracy, forgetting measures
- **Results**: Significant improvement over state-of-the-art continual learning methods across various protocols
- **Validation**: Empirically demonstrates alignment with forgetting curve theory

### Impact and Significance
**Bit Flip**: **Continuous learning is suboptimal; scheduled rest periods enhance neural network memory consolidation**

**Impact:**
- First systematic application of Ebbinghaus theory to neural network training
- Validates that biological memory principles directly improve artificial learning
- Provides theoretical foundation for temporal scheduling in continual learning
- Opens new research direction combining cognitive science with deep learning

### Research Relevance
This work provides critical validation for the literature-level bit flip that **spaced repetition principles are universal learning optimization principles**. By showing that rest periods improve continual learning, it bridges 140 years of memory research with modern AI training.

**Key Contribution**: Demonstrates that the spacing effect is not just applicable to human learning but is a fundamental principle that can enhance artificial neural network training when properly implemented.

---
*Analyzed using CS197 methodology - focusing on bit flips that drive transformative research*