# FSRS Benchmark Evolution and Algorithm Wars (2023-2025)

## CS197 Analysis  

### Problem
The spaced repetition field lacked standardized evaluation methods, making it impossible to objectively compare algorithms. Claims about algorithmic superiority were based on incompatible metrics and datasets, hindering scientific progress.

### Prior Assumptions in Literature  
- Algorithm comparison could be done using machine learning metrics (RMSE, log-loss)
- Small, proprietary datasets were sufficient for evaluation
- SuperMemo's dominance was unquestionable without rigorous benchmarking
- Different algorithms could be fairly compared without considering evaluation methodology bias

### Insight/Bit Flip
**Open-source benchmarking with carefully designed metrics can democratize algorithm evaluation and drive innovation.** The FSRS benchmark framework created the first standardized comparison methodology, sparking rapid algorithmic development and challenging established hierarchies.

### Technical Approach
- **Large-scale Dataset**: 727M+ review records from 10k+ Anki users
- **Time-series Cross-validation**: Prevents data leakage by respecting temporal order  
- **Multiple Metrics**: Log-loss, AUC, RMSE(bins) designed specifically for SRS evaluation
- **Anti-cheating Measures**: RMSE(bins) evolved to prevent metric gaming
- **Open Source**: Transparent evaluation enabling reproducible research
- **Standardized Interface**: Consistent API for testing different algorithms

### Evaluation Results  
- **FSRS vs SM-2**: Demonstrated significant improvements over traditional algorithms
- **SuperMemo Response**: SM-19/SM-20 development and universal metric proposals
- **Algorithm Proliferation**: Sparked development of numerous new approaches
- **Metric Evolution**: RMSE(bins) redesigned to prevent exploitation
- **Community Adoption**: Became de facto standard for SRS algorithm evaluation

### Impact  
- **Democratization**: Made algorithm evaluation accessible to researchers worldwide
- **Innovation Acceleration**: Open benchmarking sparked rapid algorithmic development  
- **Scientific Rigor**: Introduced proper evaluation methodology to SRS field
- **Community Building**: Created collaborative ecosystem around SRS research
- **Algorithm Wars**: Healthy competition between SuperMemo, FSRS, and new approaches

## Key Developments

### FSRS Evolution (2023-2025)
- **FSRS v3**: Initial breakthrough showing ML could improve on SM-2
- **FSRS v4**: Refined model with better calibration and stability  
- **Benchmark Integration**: Became focal point for algorithmic comparison
- **Community Adoption**: Integrated into Anki, spurring widespread usage

### SuperMemo Counter-response  
- **Universal Metric Development**: Piotr Wozniak's attempt to create fair comparison framework
- **SM-19 Algorithm**: Unreleased advanced algorithm claimed to surpass FSRS
- **SM-20 Development**: 5-component model including circadian rhythms
- **Evaluation Methodology Critique**: Highlighting limitations of ML metrics for SRS

### Benchmark Methodology Evolution
- **Original RMSE(bins)**: Could be "cheated" by constant predictions
- **Reformed RMSE(bins)**: Binning based on interval/reviews/lapses instead of predictions
- **Multiple Metrics**: Recognition that single metric insufficient
- **Temporal Validation**: Time-series splits to prevent overfitting

## Research Significance  
This represents a **methodological revolution** in spaced repetition research. The shift from proprietary evaluation to open benchmarking has accelerated innovation and brought scientific rigor to a field previously dominated by anecdotal evidence.

## Literature-Level Impact
- **Evaluation Standardization**: Created common framework for algorithm comparison
- **Innovation Catalyst**: Open competition drove rapid algorithmic advancement  
- **Community Formation**: Built collaborative research ecosystem
- **Methodological Rigor**: Introduced proper statistical evaluation to SRS field
- **Knowledge Democratization**: Made cutting-edge algorithms accessible to all learners

## Connection to Broader AI/ML
Demonstrates how domain-specific benchmarking (similar to ImageNet, GLUE) can transform research fields. Shows importance of evaluation methodology in driving scientific progress and preventing metric gaming.