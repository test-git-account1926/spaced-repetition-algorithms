# SuperMemo Algorithm Evolution: SM-2 to SM-18

**Primary Source**: Piotr Wozniak and SuperMemo research team  
**Timeline**: 1985-2019  
**Key References**: SuperMemo.guru, SuperMemopedia  

## CS197 Analysis Framework

### Problem
How can we automatically determine optimal spacing intervals for individual learning items to maximize long-term retention while minimizing study time? The challenge is adapting to individual item difficulty and learner performance patterns.

### Prior Assumptions in Literature (1985)
- **Assumption**: Fixed interval schedules work for all material (pre-SuperMemo)
- **Assumption**: All learning items have similar difficulty and forgetting patterns
- **Assumption**: One-size-fits-all scheduling is sufficient
- **Inadequacy**: Fixed schedules ignore individual item characteristics and learner performance

### Evolution of Key Insights

#### Algorithm SM-2 (1987) - The Foundation
**The Flip**: Items have individual **difficulty factors (E-Factors)** that determine their optimal spacing intervals.
- **Technical**: E-Factor system classifying items by difficulty
- **Impact**: Became the basis for Anki and most modern spaced repetition software

#### Algorithm SM-6 (1991) - The Regression Breakthrough  
**The Flip**: **Forgetting curves** derived from actual performance data can predict optimal intervals more accurately than fixed formulas.
- **Technical**: First algorithm using regression on forgetting curve data
- **Impact**: Introduced data-driven interval optimization

#### Algorithm SM-17 (2016) - The Memory Model Revolution
**The Flip**: Memory has **two components (stability and retrievability)** that can be modeled independently to predict optimal review timing.
- **Technical**: Two-component memory model with stability increase functions
- **Impact**: Dramatically improved accuracy over SM-2 based systems

#### Algorithm SM-18 (2019) - The Adaptive Difficulty Model
**The Flip**: Item **difficulty changes dynamically** during learning due to mnemonic anchoring and interference effects.
- **Technical**: Dynamic difficulty estimation replacing static E-Factors
- **Impact**: Addresses fundamental limitation of assuming constant item difficulty

### Technical Evolution

1. **SM-2 (1987)**: E-Factor matrix for difficulty classification
2. **SM-4 (1989)**: Adaptive interval modification based on performance  
3. **SM-5 (1989)**: Optimum factor matrix (interval ratios)
4. **SM-6 (1991)**: Forgetting curve regression for factor derivation
5. **SM-8 (1995)**: Advanced forgetting curve analysis, 30-50% improvement
6. **SM-15 (2013)**: Stability/retrievability model introduction
7. **SM-17 (2016)**: Full two-component memory model implementation
8. **SM-18 (2019)**: Dynamic difficulty estimation

### Evaluation and Performance
- **Universal Metric**: SM-17 beats SM-2 by ratio of 1.1 to 35.3
- **Least Squares Metric**: SM-2 ~54% vs SM-17 ~37% (lower is better)  
- **Practical Impact**: Can double or triple efficiency over SM-2
- **Real-world Data**: Validated on millions of repetitions from SuperMemo users

### Impact and Implications
- **Historical**: Established the entire field of algorithmic spaced repetition
- **Practical**: Powers learning platforms used by millions worldwide
- **Scientific**: Provided testable models of human memory and forgetting
- **Ongoing**: Continues evolution with latest psychological and cognitive research

## Key Research Contributions

### Bit Flip 1: Individual Item Difficulty (SM-2)
**Traditional**: All items have similar learning curves  
**SuperMemo**: Items have individual E-Factors determining optimal spacing

### Bit Flip 2: Data-Driven Optimization (SM-6)  
**Traditional**: Fixed mathematical formulas for interval calculation  
**SuperMemo**: Forgetting curves derived from actual performance data

### Bit Flip 3: Two-Component Memory (SM-17)
**Traditional**: Single memory strength parameter  
**SuperMemo**: Separate stability (storage strength) and retrievability (recall probability)

### Bit Flip 4: Dynamic Difficulty (SM-18)
**Traditional**: Item difficulty is constant throughout learning  
**SuperMemo**: Difficulty changes due to mnemonic anchoring and interference

## Research Gaps and Limitations
- Primarily validated on SuperMemo user base (potential selection bias)
- Complex algorithms may not generalize to different learning contexts
- Heavy reliance on user grading accuracy
- Limited open-source implementations of advanced algorithms

## Relevance to Current Research
SuperMemo algorithms represent the **gold standard** for spaced repetition, providing both theoretical frameworks and practical implementations validated on massive real-world datasets. Their evolution demonstrates how continuous empirical research can drive algorithmic advancement.