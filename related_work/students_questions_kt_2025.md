# Knowledge Tracing in Programming Education Integrating Students' Questions (2025)

**Authors**: Doyoun Kim, Suin Kim, Yojan Jo  
**Venue**: ArXiv preprint  
**ArXiv**: 2502.10408  
**URL**: https://arxiv.org/abs/2502.10408

## CS197 Analysis Framework

### Problem
Traditional knowledge tracing in programming education faces unique challenges: complexity of coding tasks, diverse problem-solving methods, and cold-start problems with new questions. Current KT models ignore valuable signals from students' questions about their understanding and misconceptions.

### Prior Assumptions in Literature
- Student performance data (correct/incorrect) sufficient for knowledge tracing
- Questions asked by students are noise rather than informative signals
- Programming KT can use same approaches as other domains
- Historical interaction records alone adequate for personalization

### Key Insight
**Students' questions contain rich semantic information about understanding levels and misconceptions** that can dramatically improve knowledge tracing accuracy when properly integrated with skill information.

### Technical Approach
**SQKT (Students' Question-based Knowledge Tracing):**
- Semantically rich embeddings capturing question content and mastery level
- Automatic skill extraction from programming problems
- Integration of subjective student questions with objective performance metrics
- Cross-domain generalization capabilities

**Implementation:**
- Natural language processing of student questions
- Semantic embedding techniques for question analysis  
- Multi-modal fusion of questions and performance data
- Domain adaptation mechanisms

### Evaluation
- **Datasets**: Various Python programming courses of different difficulty levels
- **Metrics**: AUC for performance prediction, cross-domain generalization
- **Results**: 33.1% absolute improvement in AUC compared to baseline models
- **Cross-domain**: Robust generalization addressing data scarcity in advanced courses
- **Validation**: Real classroom deployment with measurable learning improvements

### Impact and Significance
**Bit Flip**: **Student questions are valuable knowledge tracing signals rather than irrelevant noise**

**Impact:**
- First integration of student questions as primary KT input signals
- Addresses cold-start problems through semantic understanding
- Enables cross-domain knowledge transfer in programming education
- Provides foundation for conversational learning systems

### Research Relevance
This work demonstrates that **semantic understanding enhances traditional performance-based learning models**. By incorporating the rich information in student questions, it moves beyond simple correctness metrics toward deeper comprehension assessment.

**Connection to Spaced Repetition**: While not directly applying spaced repetition, this work shows how semantic modeling (similar to LECTOR's semantic interference work) can dramatically improve learning system effectiveness.

**Educational Technology Impact**: Enables personalized programming tutoring systems that understand student misconceptions through natural language, not just code correctness.

**Methodological Innovation**: Provides framework for integrating unstructured student expressions (questions) with structured learning data (performance), applicable beyond programming education.

---
*Analyzed using CS197 methodology - focusing on assumption reversals in educational data utilization*