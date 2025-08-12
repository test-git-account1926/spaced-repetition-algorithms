
## Overview  
csadas
I want to investigate how an AI scientist can autonomously discover, design, and evaluate new spaced repetition algorithms. The AI scientist will run experiments on both established methods and newly generated variations, aiming to optimize for long-term retention efficiency, low learner burden, and adaptability across domains.  

## Key Research Questions  
1. What scheduling strategies maximize retention efficiency while minimizing learner burden?  
2. Which combinations of interval spacing, difficulty weighting, and review selection rules lead to the best long-term recall?  
3. How do novel scheduling algorithms perform across different content domains and learner profiles compared to existing methods?  

## Methodology  
Here is the plan:  
- **Baseline Implementation**: Provide the AI scientist with reference implementations of existing algorithms for benchmarking.  
- **Algorithm Generation**: Instruct the AI scientist to create new algorithms by modifying, combining, or extending existing scheduling rules.  
- **Simulation Environment**: Use simulated learners with parameterized forgetting curves, varied difficulty levels, and slip/guess probabilities.  
- **Optimization Process**: AI scientist iteratively proposes new algorithms, tests them against baselines, and refines them based on performance metrics.  
- **Evaluation Metrics**:  
  - Long-term retention (Area Under the Retention Curve - AURC)  
  - Efficiency (AURC per minute spent reviewing)  
  - Learner burden (average daily reviews, dropout rate)  
  - Generalization performance across domains  
- **Reporting**: AI scientist outputs a ranked leaderboard of algorithms, detailed performance analysis, and formal descriptions of novel methods it discovers.  
 