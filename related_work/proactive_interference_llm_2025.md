# Unable to Forget: Proactive Interference Reveals Working Memory Limits in LLMs Beyond Context Length

**Authors**: Chupei Wang (University of Virginia), Jiaqiu Vince Sun (New York University)  
**Year**: 2025  
**DOI**: arXiv:2506.08184  
**URL**: https://arxiv.org/abs/2506.08184

## CS197 Analysis

### 1. Problem
Large Language Models (LLMs) struggle with information retrieval when semantically similar items create interference, but existing research conflates search difficulty (finding needles in haystacks) with interference (distinguishing between similar items). This fundamental limitation affects real-world applications where related information must be accurately distinguished.

### 2. Prior Assumptions
- Longer contexts always improve retrieval performance
- Retrieval difficulty is primarily determined by input length
- LLM retrieval is merely a lookup process rather than involving generation capabilities
- Context access is the primary bottleneck in LLM information processing

### 3. Insight
**Key Innovation**: Introduces proactive interference (PI) paradigm from cognitive science, where earlier information disrupts recall of newer updates. LLMs show human-like working memory constraints beyond mere context length limitations - retrieval accuracy declines log-linearly as interference accumulates, even when target information is clearly positioned just before queries.

### 4. Technical Approach
- **PI-LLM Evaluation**: Sequential streaming of semantically related key-value updates with queries targeting only final values
- **Interference Measurement**: Log-linear decline analysis showing universal pattern across diverse models
- **Mitigation Attempts**: Prompt engineering experiments (instructing models to ignore earlier input) with limited success
- **Cognitive Science Foundation**: Adapts established proactive interference paradigm from human memory research

### 5. Evaluation
- **Universal Log-linear Decline**: Consistent pattern across multiple LLM architectures
- **Error Analysis**: Models retrieve previously overwritten values rather than correct final values
- **Prompt Engineering Limits**: Explicit instructions to ignore interference provide minimal improvement
- **Cross-Model Validation**: Results consistent across different model sizes and architectures

### 6. Impact
**Major Implications**:
- Reveals fundamental working memory bottleneck in LLMs beyond context access limitations
- Challenges assumption that longer contexts automatically improve performance
- Identifies need for approaches that strengthen models' ability to suppress irrelevant content during retrieval
- Bridges cognitive science with AI system design for memory architecture improvements

## Bit Flip Identification

**Assumption**: LLM retrieval difficulty is primarily determined by context length and search complexity  
**Flip**: LLMs exhibit human-like working memory constraints where semantic interference, not context length, is the primary limiting factor  
**Impact**: Fundamental shift from scaling context length to developing interference-resistant memory architectures

## Research Implications

This work reveals that spaced repetition algorithms for LLMs must account for semantic interference patterns, not just temporal spacing. The proactive interference paradigm suggests that:

1. **Semantic Spacing**: Items with high semantic similarity should be spaced further apart
2. **Interference-Aware Scheduling**: Review schedules should minimize semantic overlap between recent items
3. **Memory Architecture Design**: Future LLMs need explicit interference suppression mechanisms
4. **Cognitive Alignment**: LLM memory systems should incorporate human-like working memory constraints

## Connection to Spaced Repetition Research

This finding directly supports the LECTOR paper's emphasis on semantic interference modeling and provides neurocognitive foundation for content-aware spaced repetition systems. The log-linear decline pattern could inform optimal semantic spacing intervals in future algorithms.

---
*Added during CS197 literature review enhancement - identifying fundamental memory constraints in AI systems*