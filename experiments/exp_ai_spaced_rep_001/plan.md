# AI Algorithm Discovery vs Expert Baselines - Experiment Plan

## Experiment Overview
**ID**: exp_ai_spaced_rep_001  
**Title**: AI Algorithm Discovery vs Expert Baselines  
**Status**: In Progress

## Bit Flip
- **Bit**: Algorithm design requires human domain expertise
- **Flip**: AI agents can autonomously discover spaced repetition algorithms superior to human expert designs

## Hypothesis
An AI agent using evolutionary search will discover algorithm variants achieving ≥10% improvement in retention efficiency while maintaining ≤5% increase in review burden compared to SM-17 baseline.

## Experimental Design

### Phase 1: Baseline Implementation (Day 1-2)
- Implement SuperMemo SM-2/SM-17 algorithms
- Implement Anki default scheduling
- Implement FSRS-4.5 algorithm
- Create standardized evaluation framework

### Phase 2: Synthetic Learner Simulation (Day 2-3)
- Generate 1000 synthetic learners with varied forgetting curves
- Model parameters: initial stability, retrievability, difficulty
- Include cognitive variation: fast/slow learners, domain expertise levels

### Phase 3: Evolutionary Algorithm (Day 4-6)
- Population: 100 algorithm variants
- Generations: 50 iterations
- Mutation operators: interval scaling, difficulty weighting, review selection
- Crossover: blend successful algorithmic components
- Multi-objective fitness: retention + efficiency + burden

### Phase 4: Evaluation & Analysis (Day 7)
- 10-fold cross-validation across learner populations
- Statistical testing: paired t-tests, effect size calculations
- Human expert interpretability review
- Performance visualization and reporting

## Success Metrics
1. **Primary**: ≥10% improvement in retention efficiency
2. **Secondary**: ≤5% increase in review burden
3. **Tertiary**: Statistical significance (p < 0.05) across validation folds

## Implementation Plan
- Language: Python
- Libraries: NumPy, SciPy, matplotlib, DEAP (evolutionary algorithms)
- Data storage: JSON for algorithm parameters, CSV for performance metrics
- Reproducibility: Fixed random seeds, version-controlled configurations

## Risk Mitigation
- **Simulation bias**: Use multiple forgetting curve models
- **Metric gaming**: Include diverse performance measures
- **Overfitting**: Cross-validation with holdout test sets

## Expected Timeline
7 days total execution time

## Data Collection
All experimental data stored in `/data/exp_ai_spaced_rep_001/`
- Baseline performance metrics
- Evolutionary algorithm generations
- Final algorithm parameters and performance