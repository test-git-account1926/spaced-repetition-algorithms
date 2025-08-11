# Adaptive Forgetting Curves for Spaced Repetition Language Learning (2020)

## CS197 Analysis

### Problem
- **What problem does it solve?** Creating personalized spaced repetition systems that adapt to individual learners and specific vocabulary characteristics
- **Why does it matter?** Optimal spaced repetition requires modeling individual forgetting curves and word-specific features for maximum learning efficiency

### Prior Assumptions (Bit)
- Universal forgetting curves apply equally to all learners and vocabulary items
- Simple temporal spacing is sufficient without considering linguistic complexity
- Word difficulty is uniform across learners and contexts
- Neural network models cannot effectively capture psychological forgetting patterns

### Insight (Flip)
**Word complexity is a highly informative feature that can be successfully learned by neural network models to create adaptive, personalized forgetting curves**

### Technical Approach
- **Adaptive forgetting curve models**: Incorporation of psychological and linguistic features
- **Neural network architecture**: Learns word complexity patterns from data
- **Feature engineering**: Combines temporal, linguistic, and learner meta-features
- **Recall probability prediction**: Similarity-based approach using prototype representations
- **Personalization**: Individual learner adaptation through meta-features

### Evaluation
- **Dataset**: Duolingo spaced repetition dataset with 4.28 million learner-word datapoints
- **Models**: Comparison of various forgetting curve models and neural architectures
- **Metrics**: Recall prediction accuracy, model complexity, feature importance analysis
- **Results**: Neural network models successfully learned word complexity, significantly improving prediction accuracy over baseline models

### Impact
- **Personalization advancement**: Demonstrates feasibility of adaptive individual modeling
- **Feature discovery**: Identifies word complexity as critical for spaced repetition optimization
- **Neural network validation**: Shows deep learning can capture psychological memory patterns
- **Language learning optimization**: Provides foundation for more effective vocabulary acquisition systems

## Key Insights for Spaced Repetition Research
1. **Feature importance**: Word/item complexity emerges as crucial factor beyond temporal spacing
2. **Neural network capability**: Deep learning can effectively model psychological forgetting patterns
3. **Individual differences**: Personalization through meta-features significantly improves performance
4. **Scalable adaptation**: Neural approaches enable practical implementation of adaptive systems

## Research Gaps Addressed
- **Individual adaptation mechanisms**: Provides concrete approach to learner-specific modeling
- **Content-aware scheduling**: Incorporates linguistic complexity into spacing decisions
- **Neural network integration**: Bridges psychological models with modern ML architectures

## Citation
Valverde-Albacete, F. J., & Peláez-Moreno, C. (2020). Adaptive Forgetting Curves for Spaced Repetition Language Learning. PMC. doi: PMC7334729