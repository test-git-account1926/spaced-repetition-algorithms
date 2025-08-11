# Memory3: Language Modeling with Explicit Memory

**Authors**: Hongkang Yang, Zehao Lin, Wenjin Wang, Hao Wu, et al.  
**Year**: 2024  
**Venue**: ArXiv  
**DOI**: 2407.01178v1  
**URL**: https://arxiv.org/html/2407.01178v1

## CS197 Analysis Framework

### Problem
Large language model training and inference is extremely costly, transporting knowledge from raw data to meaningful computation. The knowledge storage in model parameters is expensive and leads to large parameter sizes, high training costs, and high inference costs.

### Prior Assumptions
- Knowledge must be stored primarily in model parameters (implicit memory)
- Working memory (context key-values) is the only alternative to parameter storage
- Larger parameter counts are necessary for better performance
- RAG systems are the primary solution for external knowledge access

### Insight
**Bit Flip**: Introduction of "explicit memory" as a third form of memory in LLMs, cheaper than model parameters and text retrieval-augmented generation. Most knowledge can be externalized to explicit memories, allowing LLMs to maintain smaller parameter sizes while achieving better performance.

### Technical Approach
1. **Memory Hierarchy**: Three types of memory in LLMs:
   - Implicit memory (model parameters)
   - Working memory (context key-values) 
   - **Explicit memory** (novel external memory format)

2. **Memory Circuitry Theory**: Theoretical framework supporting knowledge externalization

3. **Memory Sparsification Mechanism**: Makes storage tractable by compressing and organizing explicit memories

4. **Two-Stage Pretraining**: 
   - Stage 1: Standard pretraining to build foundational capabilities
   - Stage 2: Memory formation training to learn explicit memory utilization

### Evaluation
- Trained 2.4B parameter Memory3 model from scratch
- Achieved better performance than much larger LLMs
- Outperformed RAG models while maintaining higher decoding speed
- Demonstrated that explicit memories can be retrieved and utilized effectively during inference

### Impact
**Literature-Level Implications**: 
- **Challenges assumption** that knowledge storage is limited to parameters vs. RAG
- **Proposes new paradigm** where most knowledge is externalized, reducing parameter requirements
- **Cost reduction potential**: Proportional savings in training, inference, and storage costs based on knowledge externalization ratio
- **Bridges cognitive science and AI**: Mirrors human memory hierarchy with short-term and long-term memory distinctions

## Relevance to Spaced Repetition Research

This work is highly relevant because:
1. **Memory consolidation parallels**: The two-stage pretraining mirrors memory consolidation processes in cognitive science
2. **Retrieval mechanisms**: Explicit memory retrieval shares principles with spaced repetition's active recall
3. **Cost efficiency**: Demonstrates how strategic memory organization can dramatically reduce computational costs
4. **Foundation for adaptive systems**: Explicit memory could enable dynamic, personalized spaced repetition implementations

## Research Gaps Identified
- No investigation of temporal dynamics in explicit memory formation
- Lacks exploration of forgetting mechanisms in explicit memory
- Missing integration with spaced repetition principles for memory consolidation
- No personalization or adaptive retrieval strategies based on usage patterns

## Key Quotes
> "Explicit memory is the third form of memory in LLMs after implicit memory (model parameters) and working memory (context key-values)."

> "With most of its knowledge externalized to explicit memories, the LLM can enjoy a smaller parameter size, training cost, and inference cost, all proportional to the amount of remaining 'abstract knowledge'."