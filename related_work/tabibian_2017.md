# Optimizing Human Learning (2017)

**Authors**: Behzad Tabibian, Utkarsh Upadhyay, Abir De, Ali Zarezade, Bernhard Schölkopf, Manuel Gomez-Rodriguez  
**ArXiv**: 1712.01856  
**Institutions**: MPI for Software Systems, MPI for Intelligent Systems, Sharif University  

## CS197 Analysis Framework

### Problem
Traditional spaced repetition systems use heuristic scheduling algorithms that lack theoretical foundation. The question remains: **Can we find the optimal reviewing schedule to maximize the benefits of spaced repetition?**

### Prior Assumptions in Literature
- **Assumption**: Heuristic scheduling rules (like SuperMemo's E-Factor) are sufficient for optimal learning
- **Assumption**: Optimal scheduling cannot be derived mathematically from first principles
- **Assumption**: Memory models are too complex for practical optimization
- **Inadequacy**: These assumptions prevented the development of theoretically grounded, provably optimal scheduling algorithms

### Key Insight (Bit Flip)
**The Flip**: Spaced repetition can be formulated as an **optimal control problem for stochastic differential equations**, enabling mathematical derivation of provably optimal reviewing schedules.

**Novel Contribution**: Introduces marked temporal point processes as a flexible framework for spaced repetition and proves that optimal reviewing schedules are determined by recall probability.

### Technical Approach
1. **Mathematical Framework**: Models spaced repetition using marked temporal point processes
2. **Optimal Control Formulation**: Frames scheduling as stochastic differential equation optimization
3. **Theoretical Results**: Proves optimal schedule is given by recall probability for well-known memory models
4. **Algorithm Development**: Creates "Memorize" - scalable online algorithm for optimal review timing
5. **Memory Models**: Works with established human memory models (exponential forgetting, etc.)

### Evaluation
- **Theoretical**: Proves optimality for two well-known memory models
- **Synthetic Data**: Validates algorithm performance on simulated learning scenarios
- **Real Data**: Tests on Duolingo platform data - popular language learning application
- **Comparison**: Shows Memorize helps learners memorize more effectively than alternatives
- **Scalability**: Demonstrates online algorithm efficiency

### Impact and Implications
- **Immediate**: First theoretically grounded approach to optimal spaced repetition scheduling
- **Broader**: Establishes mathematical foundation for memory-based learning optimization
- **Practical**: Scalable algorithm suitable for real-world learning platforms
- **Research Direction**: Opens new field of mathematically rigorous learning schedule optimization

## Research Gaps Identified
- Limited to specific memory model assumptions (exponential forgetting)
- Real-world evaluation limited to one platform (Duolingo)
- No analysis of robustness to memory model misspecification
- Doesn't address individual differences in learning patterns

## Relevance to Current Research
This paper provides the **theoretical foundation** for optimal spaced repetition that many practical algorithms lack. It demonstrates how rigorous mathematical analysis can improve upon decades of heuristic approaches, offering a template for principled algorithm design.