# FSRS Algorithm (2025): The New Standard in Spaced Repetition

## CS197 Analysis

### Problem
SuperMemo's SM-2 algorithm from 1987 has remained the default in Anki and many spaced repetition systems despite significant limitations: fixed mathematical formulas, constant item difficulty assumptions, and lack of personalization based on individual forgetting patterns.

### Prior Assumptions
- Simple E-Factor multiplication is sufficient for interval calculation
- Item difficulty remains constant throughout learning
- One-size-fits-all approach works across all learners
- Hand-crafted mathematical rules outperform data-driven optimization

### Insight (Bit Flip)
**From fixed heuristics to adaptive machine learning**: FSRS uses the Three Component Model of Memory (Difficulty, Stability, Retrievability) with 19-21 trainable parameters that adapt to individual learning patterns through optimization on real review data.

### Technical Overview
- **DSR Model**: Tracks Difficulty (inherent complexity), Stability (time for retention to decay from 100% to 90%), and Retrievability (current probability of recall)
- **Machine Learning Optimization**: Uses gradient descent to optimize 19-21 parameters based on user's historical review performance
- **Adaptive Scheduling**: Calculates optimal intervals based on desired retention rate (typically 90%) rather than fixed multipliers

### Evaluation
- **Efficiency Gains**: 30% reduction in review time for same retention compared to SM-2
- **Large-Scale Validation**: Optimized on hundreds of millions of reviews from ~10k users
- **Real-World Deployment**: Integrated as default algorithm in Anki (2024-2025)
- **Universal Metrics**: Outperforms SM-2 across multiple evaluation criteria

### Impact
1. **Paradigm Shift**: First successful replacement of SM-2 after 37 years, proving machine learning can surpass hand-crafted algorithms
2. **Open Source Movement**: FSRS is open-source, enabling wide adoption across spaced repetition platforms
3. **Personalization**: Enables individual adaptation rather than one-size-fits-all approach
4. **Research Catalyst**: Demonstrates that cognitive science combined with ML can achieve significant practical improvements

## Key Formulations

### FSRS-5 (Current Version)
- **Parameters**: 19 trainable parameters optimized via gradient descent
- **Retrievability**: R(t,S) = (1 + factor × t/S)^(-w₂₀)
- **Stability Updates**: Complex formulas for post-review stability based on grade and current state

### FSRS-6 (Latest)
- **Parameters**: 21 trainable parameters
- **Same-Day Review**: S'(S,G) = S × e^(w₁₇ × (G - 3 + w₁₈)) × S^(-w₁₉)
- **Forgetting Curve**: Trainable decay parameter w₂₀

## Research Implications

### Validated Research Directions
1. **Data-Driven Optimization**: Proves that ML can outperform decades of manual algorithm tuning
2. **Individual Differences**: Demonstrates value of personalized parameters over universal constants
3. **Three-Component Memory Models**: Validates DSR framework for practical applications

### Literature-Level Bit Flip
**Assumption**: Hand-crafted spaced repetition algorithms based on psychological theory are optimal
**Flip**: Machine learning optimization on large-scale user data produces superior algorithms
**Evidence**: 30% efficiency improvement, successful deployment across millions of users

## Future Research Questions
1. How can semantic relationships between cards be incorporated into FSRS?
2. What role do circadian rhythms and learning context play in optimization?
3. Can FSRS principles be applied to other domains beyond flashcard learning?
4. How does FSRS perform for different content types (procedural vs. declarative knowledge)?

---
*FSRS represents the first successful paradigm shift in spaced repetition algorithms since SM-2, demonstrating that principled machine learning can dramatically improve upon decades of psychological research-based heuristics.*