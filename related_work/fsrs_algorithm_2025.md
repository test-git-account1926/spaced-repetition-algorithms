# FSRS: Free Spaced Repetition Scheduler

## Overview
FSRS (Free Spaced Repetition Scheduler) represents the current state-of-the-art in spaced repetition algorithms, developed by Jarrett Ye and the open-source community. As of 2024-2025, FSRS has been integrated into Anki and claims to be "the most accurate spaced repetition algorithm in the world."

## Key Innovation: Three Component Model
FSRS is based on the DSR (Difficulty-Stability-Retrievability) model:

- **Retrievability (R)**: Probability of successful recall at a given moment
- **Stability (S)**: Time required for R to decrease from 100% to 90%  
- **Difficulty (D)**: Inherent complexity affecting stability growth

## Algorithm Evolution
- **FSRS v3** (2022): First practical implementation with basic DSR model
- **FSRS v4** (2023): Major improvements in parameter optimization
- **FSRS v5** (2024): Current version using 19 parameters, incorporating all daily reviews

## Performance Claims
- Outperforms legacy algorithms (SM-2, HLR) in RMSE metrics
- Uses machine learning to optimize parameters from review history
- Default parameters trained on hundreds of millions of reviews from ~10k users
- Claimed accuracy improvements of 2-15% over baseline algorithms

## CS197 Analysis

### Problem
Legacy spaced repetition algorithms like SM-2 use fixed parameters and heuristic rules that don't adapt to individual learning patterns, leading to suboptimal scheduling.

### Prior Assumptions
- Simple E-Factor models sufficient for interval calculation
- Universal parameters work across all learners
- Binary recall assessment adequate for memory modeling

### Key Insight (Bit Flip)
**Old Assumption**: Universal algorithmic parameters optimal for all users
**New Insight**: Machine learning can personalize algorithm parameters based on individual review history

### Technical Implementation
- Uses gradient descent to minimize prediction error on historical review data
- Implements power law forgetting curves with exponential decay
- Employs 19-parameter model optimized through RMSE minimization
- Integrates multiple review ratings (Again, Hard, Good, Easy) rather than binary pass/fail

### Validation
- Benchmarked against SM-2, HLR, SSP-MMC, ANKI using millions of review records
- Claims superior performance in predictive accuracy (RMSE)
- Integrated into Anki as production algorithm serving millions of users

### Impact
- Represents paradigm shift from rule-based to data-driven spaced repetition
- Demonstrates machine learning applicability to memory modeling
- Provides open-source reference implementation for academic/commercial use
- Challenges 20+ year dominance of SuperMemo algorithms

## Research Gaps and Future Directions

### Current Limitations
1. **Semantic Blindness**: FSRS treats items independently without considering semantic relationships
2. **Context Ignorance**: No awareness of learning context or content domain
3. **Individual Differences**: Limited adaptation beyond performance history
4. **Long-term Validation**: Most evaluation on days-weeks, not months-years

### Integration Opportunities
- Combine with LLM-powered semantic similarity (LECTOR approach)
- Integrate content-aware scheduling (Randazzo 2025)
- Add biological memory principles (KUL-KT Hebbian learning)
- Enhance with context-triggered recall (Irec framework)

## Relevance to AI Scientist Research
FSRS demonstrates the effectiveness of data-driven parameter optimization over fixed rules. An AI scientist could:
1. Use FSRS as a strong baseline for algorithmic discovery
2. Extend the DSR model with semantic and contextual features
3. Explore hybrid approaches combining FSRS optimization with novel scheduling rules
4. Investigate transfer learning across domains and content types

The success of FSRS validates the research direction of using machine learning to discover and optimize spaced repetition algorithms, providing both technical foundation and performance benchmarks for future algorithmic innovations.