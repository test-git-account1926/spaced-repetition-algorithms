# Experiment Ideas

## Overview

This experimental program tests the **core bit flip**: that AI agents can autonomously discover spaced repetition algorithms that outperform human-designed methods by systematically exploring the algorithm design space. Our approach challenges three fundamental assumptions in the literature:

1. **Human expertise requirement**: Algorithm design requires domain expert knowledge
2. **Near-optimality assumption**: Existing algorithms are close to optimal
3. **Universal approach assumption**: One-size-fits-all algorithms work best

## Experimental Strategy

**Core Thesis**: An AI scientist equipped with simulation environments, evaluation frameworks, and iterative optimization can discover novel spaced repetition algorithms that achieve superior performance across multiple dimensions (retention efficiency, learner burden, domain generalization).

**Validation Approach**: Compare AI-discovered algorithms against established baselines using rigorous simulation studies with statistical validation, followed by human validation studies.

## Planned Experiments

### Experiment 1: AI Algorithm Discovery vs Expert Baselines

**Bit Flip Tested**: AI can discover algorithms superior to human expert designs

- **Objective**: Validate whether an AI scientist can autonomously discover spaced repetition algorithms that outperform established methods (SuperMemo SM-2, SM-17, Anki, FSRS) on key performance metrics.

- **Hypothesis**: An AI agent using evolutionary search with performance-driven selection will discover algorithm variants achieving ≥10% improvement in retention efficiency while maintaining ≤5% increase in review burden compared to SM-17 baseline.

- **Independent Variables**: 
  - Algorithm generation method (evolutionary search, gradient-based optimization, hybrid approaches)
  - Search space constraints (parameter ranges, rule complexity limits)
  - Evaluation objectives (retention vs efficiency vs burden trade-offs)

- **Dependent Variables**:
  - Area Under Retention Curve (AURC) over 180-day simulation
  - Review efficiency (AURC per review minute)
  - Learner burden (avg daily reviews, peak review loads)
  - Algorithm complexity (parameter count, rule simplicity)

- **Methodology**:
  1. **Simulation Environment**: Implement 1000 synthetic learners with varied forgetting curves (Ebbinghaus parameters), difficulty sensitivities, and learning rates
  2. **Baseline Implementation**: Code reference implementations of SuperMemo SM-2/SM-17, Anki default, FSRS-4.5
  3. **AI Discovery Process**: Deploy evolutionary algorithm with:
     - Population of 100 algorithm variants
     - Mutation operators for interval formulas, difficulty adjustments, review scheduling
     - Multi-objective fitness combining retention, efficiency, and burden
     - 50 generations with elitist selection
  4. **Evaluation Protocol**: 10-fold cross-validation with 180-day simulation periods
  5. **Statistical Testing**: Paired t-tests on AURC scores, Wilcoxon signed-rank for non-parametric validation

- **Expected Outcomes**: 
  - AI discovers 3-5 novel algorithms achieving 8-15% retention improvement
  - Trade-off analysis reveals efficiency gains in specific learner profiles
  - Some discovered algorithms show domain-specific advantages

- **Success Metrics**: 
  - Primary: ≥10% AURC improvement with statistical significance (p<0.01)
  - Secondary: Algorithm interpretability (human expert can understand discovered rules)
  - Tertiary: Computational efficiency of discovered algorithms

- **Validity Threats & Mitigations**:
  - **Internal**: Simulation bias → Validate with multiple forgetting curve models
  - **External**: Synthetic learner limitations → Include empirical learner data validation
  - **Construct**: Metric gaming → Use multiple independent performance measures
  - **Statistical**: Multiple comparisons → Bonferroni correction for family-wise error

### Experiment 2: Semantic-Aware Algorithm Discovery

**Bit Flip Tested**: AI can incorporate semantic relationships that human-designed algorithms ignore

- **Objective**: Test whether AI agents can discover algorithms that leverage semantic similarity between items to optimize scheduling, building on LECTOR's semantic interference findings.

- **Hypothesis**: AI-discovered algorithms incorporating LLM-based semantic similarity will achieve ≥15% retention improvement over traditional item-independent scheduling, particularly for conceptually related content domains.

- **Independent Variables**:
  - Semantic integration method (embedding similarity, concept clustering, interference modeling)
  - Content domain type (vocabulary, factual knowledge, procedural skills)
  - Semantic relationship strength (high/medium/low conceptual overlap)

- **Dependent Variables**:
  - Semantic interference reduction (measured via confusion matrices)
  - Domain-specific retention curves
  - Algorithm discovery convergence time
  - Semantic representation quality (embedding coherence metrics)

- **Methodology**:
  1. **Content Preparation**: Create 3 content domains with varying semantic density:
     - High: Foreign language vocabulary with synonym clusters
     - Medium: Historical facts with chronological relationships  
     - Low: Random number-fact pairs (control condition)
  2. **Semantic Infrastructure**: Implement LLM-based similarity scoring using sentence transformers
  3. **AI Discovery Enhancement**: Extend evolutionary algorithm with:
     - Semantic-aware mutation operators
     - Interference-based fitness components
     - Content clustering algorithms
  4. **Evaluation Framework**: Compare semantic-aware vs semantic-agnostic discovered algorithms
  5. **Human Validation**: Expert review of discovered semantic strategies

- **Expected Outcomes**:
  - Semantic-aware algorithms show 10-20% improvement on high-similarity content
  - Discovery of novel interference mitigation strategies
  - Domain-specific algorithmic specializations emerge

- **Success Metrics**:
  - Primary: ≥15% retention improvement on high-semantic content (p<0.005)
  - Secondary: Semantic strategy interpretability and generalizability
  - Tertiary: Computational overhead acceptability (<2x baseline)

### Experiment 3: Adaptive Algorithm Personalization Discovery

**Bit Flip Tested**: AI can discover personalization strategies beyond simple parameter tuning

- **Objective**: Investigate whether AI agents can discover meta-algorithms that adapt to individual learner differences through novel personalization mechanisms.

- **Hypothesis**: AI-discovered adaptive algorithms will achieve ≥20% retention improvement over fixed algorithms by learning individual memory signatures and dynamically adjusting scheduling strategies.

- **Independent Variables**:
  - Personalization mechanism (memory pattern recognition, learning style adaptation, context integration)
  - Adaptation timeframe (immediate, short-term, long-term learning)
  - Individual difference dimensions (cognitive capacity, domain expertise, motivation patterns)

- **Dependent Variables**:
  - Individual learning curve optimization
  - Cross-learner algorithm performance variance
  - Adaptation convergence speed
  - Personalization strategy diversity

- **Methodology**:
  1. **Learner Simulation Enhancement**: Create 200 diverse synthetic learners with:
     - Varied cognitive profiles (memory capacity, processing speed)
     - Different learning preferences (massed vs spaced, difficulty preferences)
     - Dynamic states (motivation changes, fatigue patterns)
  2. **Meta-Learning Framework**: Implement neural network-based meta-learners that:
     - Observe individual performance patterns
     - Predict optimal algorithm parameters per learner
     - Adapt scheduling in real-time
  3. **AI Discovery Process**: Evolve meta-algorithm architectures that balance:
     - Individual optimization vs computational efficiency
     - Adaptation speed vs stability
     - Personalization depth vs algorithmic complexity
  4. **Validation Protocol**: Cross-learner generalization testing with holdout validation

- **Expected Outcomes**:
  - Discovery of 2-4 distinct personalization strategies
  - Significant individual performance improvements
  - Identification of universal vs personal optimization principles

- **Success Metrics**:
  - Primary: ≥20% retention improvement for bottom quartile learners
  - Secondary: Algorithm fairness across learner types
  - Tertiary: Personalization interpretability for educational applications

### Experiment 4: Long-term Retention Validation Study

**Bit Flip Tested**: AI-discovered algorithms maintain advantages over extended time periods

- **Objective**: Validate that AI-discovered algorithms show sustained performance advantages over 1-year simulation periods, testing long-term memory consolidation effects.

- **Hypothesis**: AI-discovered algorithms will maintain ≥8% retention advantage over 365-day periods, with benefits increasing over time due to superior long-term scheduling optimization.

- **Methodology**:
  1. **Extended Simulation**: Run best-performing algorithms from Experiments 1-3 over 365-day periods
  2. **Memory Consolidation Modeling**: Include sleep-dependent memory consolidation effects
  3. **Real-world Validation**: Deploy discovered algorithms in controlled human studies (n=100 per condition)
  4. **Longitudinal Analysis**: Track performance degradation and maintenance patterns

- **Success Metrics**:
  - Primary: Sustained ≥8% advantage at 365 days
  - Secondary: Human study validation correlation with simulation results
  - Tertiary: Long-term algorithmic stability and robustness

## Timeline and Resource Requirements

**Phase 1 (Weeks 1-4): Infrastructure Development**
- Simulation environment implementation
- Baseline algorithm coding and validation
- Evolutionary framework setup

**Phase 2 (Weeks 5-12): Core Discovery Experiments** 
- Experiments 1-2 execution
- Statistical analysis and algorithm interpretation
- Performance optimization

**Phase 3 (Weeks 13-20): Advanced Discovery**
- Experiment 3 adaptive personalization
- Cross-experiment synthesis and comparison
- Novel algorithm documentation

**Phase 4 (Weeks 21-36): Long-term Validation**
- Experiment 4 extended simulation
- Human validation study preparation and execution
- Final analysis and publication preparation

**Computing Resources**: 
- 100+ CPU hours for evolutionary searches
- GPU access for LLM-based semantic analysis
- Storage for simulation datasets and experimental logs

**Validation Standards**:
- Statistical power analysis (β = 0.8, α = 0.01)
- Effect size reporting (Cohen's d)
- Replication protocols for key findings
- Open science practices (code/data sharing)

---
*This section enhanced using CS197 research methodology focusing on bit flip validation and rigorous experimental design*
