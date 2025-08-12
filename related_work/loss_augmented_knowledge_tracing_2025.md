# Survey of Loss Augmented Knowledge Tracing (2025)

## CS197 Analysis Framework

### Problem
Traditional loss functions like cross-entropy and MSE often fail to address challenges in knowledge tracing due to data quality limitations and learning process inefficiencies, limiting model performance and robustness in educational prediction tasks.

### Prior Assumptions in Prior Work
- Standard loss functions (cross-entropy, MSE) are sufficient for knowledge tracing
- Simple supervised learning approaches can adequately capture student learning patterns
- Loss function design is not a primary factor in KT model performance
- Contrastive learning techniques are not applicable to educational sequence modeling

### Insight
Advanced loss function design through regularization and contrastive learning techniques can significantly enhance knowledge tracing model performance by addressing data quality issues and improving learning process efficiency.

### Technical Overview
**Loss Augmentation Strategies**:
- **Contrastive Knowledge Tracing**: Bi-CLKT, CL4KT, SP-CLKT, CoSKT approaches
- **Prediction-consistent DKT**: Maintaining consistency across prediction horizons
- **Loss regularization**: Additional terms to improve model robustness
- **Performance benchmarks**: Comparative analysis of different loss augmentation methods

### Proof/Evaluation
- Comprehensive survey of loss-augmented KT algorithms
- Performance benchmarks across multiple contrastive learning approaches
- Analysis of real-world deployment challenges
- Comparison with traditional KT methods using standard loss functions

### Impact
- **Bit Flip**: Standard loss functions adequate → Advanced loss design through contrastive learning is crucial for KT performance
- Establishes loss function design as fundamental component of KT research
- Demonstrates significant improvements through contrastive learning techniques
- Provides roadmap for future KT research directions including hybrid loss strategies

### CS197 Significance
This survey reveals that the choice of loss function is not merely a technical detail but a fundamental design decision that can significantly impact knowledge tracing performance, suggesting that loss function innovation should be a primary research focus in educational AI.

**Citation**: Shukurlu, A. (2025). Survey of Loss Augmented Knowledge Tracing. arXiv preprint arXiv:2504.15163.