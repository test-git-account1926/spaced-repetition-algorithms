# Task Scheduling & Forgetting in Multi-Task Reinforcement Learning (2025)

**Authors**: Marc Speckmann, Theresa Eimer  
**Institution**: Leibniz University Hannover  
**arXiv**: [2503.01941](https://arxiv.org/html/2503.01941v1)  
**Date**: 2025 (updated from 2016 reference)

## CS197 Analysis

### 1. Problem
How to prevent catastrophic forgetting in multi-task reinforcement learning by applying human learning theory principles to task scheduling and curriculum design.

### 2. Prior Work Assumptions
- Performance-based metrics sufficient for RL curriculum design
- Forgetting in RL agents fundamentally different from human forgetting
- Reactive approaches to forgetting (after it occurs) are adequate
- Leitner/SuperMemo systems would transfer directly to RL settings

### 3. Insight/Novel Contribution
**Bit Flip**: RL agents exhibit human-like forgetting curves, but prevention strategies from human learning theory don't transfer directly due to asymmetrical learning and retention patterns between tasks.

### 4. Technical Approach
- **Forgetting Analysis**: Systematic study of forgetting behavior in RL across MiniGrid tasks
- **Human Learning Methods**: Implementation of Leitner and SuperMemo systems for RL
- **Comparison**: Evaluation against Prioritized Level Replay (PLR) baseline
- **Task Scheduling**: Spaced repetition principles applied to multi-task RL curricula
- **Failure Analysis**: Investigation of why human methods don't transfer perfectly

### 5. Evaluation
- **Environment**: MiniGrid benchmark suite for multi-task evaluation
- **Metrics**: Task retention, learning efficiency, forgetting curve analysis
- **Baselines**: PLR (performance-based) vs Leitner/SuperMemo (retention-based)
- **Results**: Human-like forgetting curves confirmed, but transfer methods show limitations
- **Analysis**: Identified asymmetrical learning patterns as key difference

### 6. Impact & Implications
- **Negative Results**: Important finding that human spaced repetition doesn't directly transfer
- **Theoretical Insight**: RL task interactions more complex than human memory models
- **Research Direction**: Need for RL-specific adaptation of spacing principles
- **Methodological**: Establishes framework for studying forgetting in multi-task RL

## Key Insights
- **Cross-Domain Patterns**: RL agents do exhibit human-like forgetting curves
- **Transfer Limitations**: Direct application of human learning methods fails
- **Asymmetrical Learning**: Tasks have different learning/retention patterns in RL
- **Curriculum Design**: Need for RL-specific scheduling algorithms

## Research Gaps Addressed
- Limited understanding of forgetting patterns in multi-task RL
- Assumption that human learning methods transfer directly to AI
- Need for proactive (vs reactive) forgetting prevention in RL
- Lack of systematic comparison between retention-based and performance-based curricula

## Bit Flip Identified
**Assumption**: Human learning and memory principles transfer directly to reinforcement learning agents  
**Flip**: While RL agents show human-like forgetting curves, they require specialized scheduling algorithms due to asymmetrical task interactions  
**Evidence**: Leitner/SuperMemo underperform PLR despite similar forgetting patterns  
**Impact**: Need for RL-specific adaptation of cognitive science principles

## Relevance to AI Scientist Research
This work provides crucial insights for developing spaced repetition algorithms for AI systems - confirming the universal nature of forgetting curves while highlighting the need for domain-specific adaptations rather than direct transfer of human learning methods.