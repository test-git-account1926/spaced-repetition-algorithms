# Human-like Forgetting Curves in Deep Neural Networks (2025)

**Authors**: Dylan Kline (University of Rochester)  
**ArXiv**: 2506.12034v2  
**Published**: May 2025 (revised June 2025)  

## CS197 Analysis Framework

### Problem
**Catastrophic forgetting** in neural networks prevents them from retaining previously learned knowledge when learning new tasks. Unlike human memory, which exhibits predictable forgetting curves that can be mitigated through spaced repetition, artificial neural networks lack similar memory consolidation mechanisms.

### Prior Assumptions in Literature
- **Assumption**: Neural network forgetting is fundamentally different from human forgetting
- **Assumption**: Catastrophic forgetting requires specialized architectures or complex regularization
- **Assumption**: Human memory research has limited applicability to artificial neural networks
- **Inadequacy**: These assumptions missed the opportunity to leverage decades of cognitive science research

### Key Insight (Bit Flip)
**The Flip**: Artificial neural networks can exhibit **human-like forgetting curves**, enabling the direct application of cognitive science principles (like spaced repetition) to mitigate catastrophic forgetting.

**Novel Contribution**: Demonstrates that DNNs naturally emulate human memory decay patterns, opening new avenues for continual learning based on established psychological principles.

### Technical Approach
1. **Retention Metric**: Computes recall probability by evaluating similarity between current and stored prototype representations
2. **Forgetting Curve Measurement**: Quantitative framework to measure information retention in neural networks
3. **Scheduled Review**: Uses retention metrics to schedule review sessions for targeted knowledge reinforcement
4. **Multi-Layer Perceptron Experiments**: Tests on MLPs to validate human-like forgetting patterns

### Evaluation
- **Architecture**: Multi-Layer Perceptrons
- **Methodology**: Measured forgetting curves and knowledge robustness through scheduled reviews
- **Key Finding**: Neural networks exhibit exponential forgetting similar to Ebbinghaus curves
- **Result**: Knowledge becomes increasingly robust through spaced repetition-style review schedules

### Impact and Implications
- **Immediate**: Provides new perspective on continual learning by connecting to human memory research
- **Broader**: Bridges cognitive science and neural network design
- **Research Direction**: Enables applying 140+ years of human memory research to AI systems
- **Practical**: Offers computationally efficient approach to catastrophic forgetting

## Research Gaps Identified
- Limited to MLPs - unclear how findings extend to modern architectures (Transformers, CNNs)
- No comparison with state-of-the-art continual learning methods
- Lacks theoretical analysis of why neural networks exhibit human-like forgetting
- Missing evaluation on complex, realistic datasets

## Relevance to Current Research
This work establishes a **fundamental bridge** between human memory research and artificial neural networks. It suggests that spaced repetition principles, refined over decades in cognitive science, can be directly applied to solve catastrophic forgetting - a major challenge in AI.