# LLMKT: Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs

**Authors**: Alexander Scarlatos, Ryan S. Baker, Andrew Lan  
**Year**: 2025  
**Conference**: 15th International Learning Analytics and Knowledge Conference  
**DOI**: 10.1145/3706468.3706501  
**URL**: https://dl.acm.org/doi/10.1145/3706468.3706501

## CS197 Analysis

### Problem
Tracing student knowledge and analyzing misconceptions in open-ended dialogue tutoring has been difficult and time-consuming to implement, limiting the scalability of intelligent tutoring systems.

### Prior Assumptions
- Traditional KT methods work effectively for open-ended dialogue-based learning
- Manual dialogue analysis and knowledge component identification is scalable
- Knowledge components are easily identifiable in natural conversations
- Existing KT models can handle the complex context of dialogue interactions effectively

### Insight
**Bit Flip**: LLM-powered knowledge component identification in dialogue turns significantly outperforms existing KT methods for conversational learning.

### Technical Approach
- **LLM Prompting**: Uses LLM methods to identify knowledge components/skills in each dialogue turn
- **Dialogue Turn Analysis**: Analyzes both tutor utterances (tasks) and student responses
- **Correctness Evaluation**: LLM evaluates whether students respond correctly, verified by human experts
- **LLMKT Method**: Novel yet simple LLM-based approach for knowledge tracing in dialogues
- **Multiple KT Integration**: Applies range of KT methods on LLM-labeled data

### Evaluation
- Experiments on two tutoring dialogue datasets
- Human expert annotations validate LLM accuracy
- LLMKT significantly outperforms existing KT methods in predicting student response correctness
- Extensive qualitative analyses highlight challenges and future directions

### Impact
- Opens new possibilities for scalable dialogue-based intelligent tutoring systems
- Enables real-time knowledge state assessment during conversational learning
- Reduces authoring effort and human expertise required for dialogue-based education
- Provides foundation for AI-powered tutoring chatbots with sophisticated knowledge tracking

## Key Contributions

1. **Dialogue KT Framework**: First systematic approach to knowledge tracing in natural language tutoring dialogues
2. **LLM Integration**: Demonstrates how LLMs can support educational technology beyond content generation
3. **Validation**: Human expert validation of LLM-based knowledge component identification
4. **Performance**: Significant improvements over traditional KT methods in dialogue contexts

## Technical Innovation

### LLMKT Architecture
- **Knowledge Component Identification**: Automatic extraction from dialogue turns
- **Student Response Evaluation**: Automated correctness assessment
- **Knowledge State Tracking**: Continuous monitoring throughout dialogue sessions
- **Scalable Deployment**: Reduces manual annotation requirements

### Challenges Identified
- Complex dialogue contexts with implicit knowledge indicators
- Varying quality of student natural language responses  
- Temporal dynamics of knowledge states in conversational flow
- Balancing automated assessment with educational validity

## Relevance to Spaced Repetition Research

This work is highly relevant to conversational spaced repetition systems. The ability to track knowledge states in real-time during natural dialogue could enable:

- **Adaptive Conversational SR**: Dynamic adjustment of review schedules based on dialogue performance
- **Context-Aware Spacing**: Understanding when concepts are naturally reinforced in conversation
- **Semantic Relationship Modeling**: Using dialogue context to identify related concepts for intelligent scheduling

## Research Gaps Addressed

- **Gap**: Difficulty scaling knowledge tracing to open-ended dialogue environments
- **Solution**: LLM-powered automatic knowledge component identification and student assessment
- **Validation**: Outperforms existing methods on real tutoring dialogue datasets

## Future Directions

1. **Real-time Adaptation**: Integrating LLMKT with adaptive dialogue management
2. **Multimodal Integration**: Extending to include non-verbal cues and visual elements
3. **Long-term Tracking**: Connecting dialogue sessions for longitudinal knowledge modeling
4. **Cross-domain Validation**: Testing across different subject areas and learning contexts

---
*Added to literature review: 2025-08-11*