"""
Semantic-Aware Algorithm Discovery Experiment.
Tests AI discovery of algorithms leveraging semantic relationships.
"""

import json
import time
import os
import sys
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans

# Add parent directory to path to import from previous experiment
sys.path.append('../exp_ai_spaced_rep_001/run')
from baseline_algorithms import Card, evaluate_algorithm
from synthetic_learners import SyntheticLearner, LearnerProfile

class ContentDomain:
    """Represents a content domain with semantic relationships."""
    
    def __init__(self, name: str, items: List[str], semantic_density: str):
        self.name = name
        self.items = items
        self.semantic_density = semantic_density
        self.embeddings = None
        self.similarity_matrix = None
        self.clusters = None

class SemanticContentGenerator:
    """Generates content domains with different semantic densities."""
    
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
    def create_domains(self) -> List[ContentDomain]:
        """Create three content domains with different semantic densities."""
        
        # High semantic density: Medical terminology
        medical_items = [
            "Myocardial infarction - death of heart muscle tissue",
            "Cardiac arrest - sudden loss of heart function", 
            "Angina pectoris - chest pain from reduced blood flow",
            "Arrhythmia - irregular heart rhythm",
            "Bradycardia - slow heart rate below 60 bpm",
            "Tachycardia - fast heart rate above 100 bpm",
            "Hypertension - elevated blood pressure",
            "Hypotension - low blood pressure",
            "Atherosclerosis - artery hardening from plaque",
            "Stenosis - narrowing of blood vessels",
            "Pneumonia - lung infection causing inflammation",
            "Bronchitis - inflammation of bronchial tubes",
            "Asthma - airways narrow and swell with mucus",
            "Emphysema - air sacs in lungs are damaged",
            "Pleurisy - inflammation of lung lining",
            "Nephritis - kidney inflammation",
            "Hepatitis - liver inflammation",
            "Gastritis - stomach lining inflammation",
            "Arthritis - joint inflammation",
            "Dermatitis - skin inflammation"
        ]
        
        # Medium semantic density: Programming concepts
        programming_items = [
            "Recursion - function calls itself",
            "Algorithm - step-by-step problem solving procedure",
            "Variable - storage location with symbolic name",
            "Loop - repeated execution of code block",
            "Array - collection of elements at indices",
            "Hash table - key-value data structure",
            "Binary tree - tree with max two children",
            "Queue - first-in-first-out data structure",
            "Stack - last-in-first-out data structure",
            "Graph - nodes connected by edges",
            "API - interface for software communication",
            "Database - organized collection of data",
            "Framework - reusable software platform",
            "Library - collection of precompiled routines",
            "Compiler - translates source to machine code",
            "Debugging - finding and fixing code errors",
            "Testing - verifying software correctness",
            "Refactoring - improving code without changing behavior",
            "Version control - tracking code changes",
            "Deployment - releasing software to users"
        ]
        
        # Low semantic density: Random vocabulary  
        random_items = [
            "Serendipity - pleasant surprise discovery",
            "Telescope - instrument for viewing distant objects",
            "Bicycle - two-wheeled vehicle with pedals",
            "Symphony - large-scale orchestral composition",
            "Archaeology - study of human history through artifacts",
            "Photosynthesis - plants convert light to chemical energy",
            "Democracy - government by the people",
            "Metamorphosis - biological transformation process",
            "Architecture - design and construction of buildings",
            "Philosophy - study of fundamental questions",
            "Geography - study of Earth's features",
            "Chemistry - science of matter and reactions",
            "Psychology - study of mind and behavior",
            "Anthropology - study of human societies",
            "Linguistics - scientific study of language",
            "Economics - study of resource allocation",
            "Sociology - study of social behavior",
            "Literature - written artistic expression",
            "Mathematics - study of numbers and patterns",
            "Physics - science of matter and energy"
        ]
        
        domains = [
            ContentDomain("Medical", medical_items, "high"),
            ContentDomain("Programming", programming_items, "medium"), 
            ContentDomain("General", random_items, "low")
        ]
        
        # Compute embeddings and similarity matrices
        for domain in domains:
            domain.embeddings = self.model.encode(domain.items)
            domain.similarity_matrix = cosine_similarity(domain.embeddings)
            
            # Create semantic clusters
            n_clusters = min(5, len(domain.items) // 4)
            if n_clusters > 1:
                kmeans = KMeans(n_clusters=n_clusters, random_state=42)
                domain.clusters = kmeans.fit_predict(domain.embeddings)
            else:
                domain.clusters = np.zeros(len(domain.items))
        
        return domains

class SemanticGene:
    """Gene for semantic-aware algorithm operations."""
    
    def __init__(self, operation: str, parameters: Dict = None):
        self.operation = operation
        self.parameters = parameters or {}
        
    def apply(self, card: Card, similarity_scores: np.ndarray, cluster_id: int) -> float:
        """Apply semantic gene operation to scheduling decision."""
        
        if self.operation == "semantic_interference":
            # Reduce intervals for items with high similarity to recently reviewed
            max_similarity = np.max(similarity_scores) if len(similarity_scores) > 0 else 0
            interference_factor = self.parameters.get('intensity', 0.3)
            return 1.0 - (max_similarity * interference_factor)
            
        elif self.operation == "cluster_spacing":
            # Adjust intervals based on cluster membership
            cluster_factor = self.parameters.get('cluster_weight', 0.2)
            return 1.0 + (cluster_factor if cluster_id == 0 else -cluster_factor)
            
        elif self.operation == "similarity_boost":
            # Increase intervals for items learned in similar contexts
            avg_similarity = np.mean(similarity_scores) if len(similarity_scores) > 0 else 0
            boost_factor = self.parameters.get('boost_strength', 0.4)
            return 1.0 + (avg_similarity * boost_factor)
            
        elif self.operation == "semantic_ease":
            # Modify ease factor based on semantic context
            semantic_context = np.mean(similarity_scores) if len(similarity_scores) > 0 else 0.5
            ease_modifier = self.parameters.get('ease_sensitivity', 0.1)
            return 1.0 + ((semantic_context - 0.5) * ease_modifier)
            
        else:
            return 1.0

class SemanticEvolutionaryAlgorithm:
    """Evolutionary algorithm for discovering semantic-aware scheduling."""
    
    def __init__(self, domains: List[ContentDomain]):
        self.domains = domains
        self.population_size = 80
        self.generations = 40
        self.population = []
        
    def initialize_population(self):
        """Create initial population of semantic-aware algorithms."""
        
        operations = ["semantic_interference", "cluster_spacing", "similarity_boost", "semantic_ease"]
        
        for i in range(self.population_size):
            # Random number of genes (2-8)
            n_genes = np.random.randint(2, 9)
            genes = []
            
            for _ in range(n_genes):
                operation = np.random.choice(operations)
                parameters = {}
                
                if operation == "semantic_interference":
                    parameters['intensity'] = np.random.uniform(0.1, 0.5)
                elif operation == "cluster_spacing":
                    parameters['cluster_weight'] = np.random.uniform(0.1, 0.4)
                elif operation == "similarity_boost":
                    parameters['boost_strength'] = np.random.uniform(0.2, 0.6)
                elif operation == "semantic_ease":
                    parameters['ease_sensitivity'] = np.random.uniform(0.05, 0.2)
                    
                genes.append(SemanticGene(operation, parameters))
            
            self.population.append(genes)
    
    def evaluate_algorithm(self, genes: List[SemanticGene], domain: ContentDomain) -> Dict:
        """Evaluate semantic algorithm on a domain."""
        
        # Create synthetic learners
        learners = [SyntheticLearner() for _ in range(50)]  # Smaller population for speed
        
        # Create cards from domain items
        cards = [Card(difficulty=np.random.uniform(0.2, 0.8)) for _ in range(len(domain.items))]
        
        # Simulate learning process
        total_efficiency = 0
        total_success = 0
        n_reviews = 0
        
        for learner in learners[:20]:  # Sample learners for speed
            for day in range(60):  # 60-day simulation
                for card_idx, card in enumerate(cards[:10]):  # Sample cards
                    
                    # Calculate semantic context for this card
                    similarity_scores = domain.similarity_matrix[card_idx]
                    cluster_id = domain.clusters[card_idx]
                    
                    # Apply semantic genes to modify scheduling
                    interval_modifier = 1.0
                    for gene in genes:
                        modifier = gene.apply(card, similarity_scores, int(cluster_id))
                        interval_modifier *= modifier
                    
                    # Simple scheduling with semantic modification
                    modified_interval = max(1, int(card.interval * interval_modifier))
                    
                    if day % max(1, modified_interval) == 0:
                        grade = learner.simulate_review(card, day)
                        success = 1 if grade >= 3 else 0
                        
                        total_success += success
                        n_reviews += 1
                        
                        # Update card (simplified)
                        if success:
                            card.interval = max(1, int(card.interval * 1.5))
                        else:
                            card.interval = 1
        
        if n_reviews > 0:
            success_rate = total_success / n_reviews
            efficiency = success_rate / max(1, n_reviews / 100)  # Reviews per day
        else:
            success_rate = 0
            efficiency = 0
            
        return {
            'efficiency': efficiency,
            'success_rate': success_rate,
            'n_reviews': n_reviews,
            'fitness': efficiency * 0.7 + success_rate * 0.3  # Combined metric
        }
    
    def run_evolution(self) -> List[Dict]:
        """Run evolutionary algorithm across domains."""
        
        print("Running semantic-aware evolutionary discovery...")
        
        # Evaluate initial population
        fitness_scores = []
        for gen in range(self.generations):
            print(f"  Generation {gen + 1}/{self.generations}")
            
            generation_fitness = []
            for i, genes in enumerate(self.population):
                # Evaluate on all domains
                domain_scores = []
                for domain in self.domains:
                    score = self.evaluate_algorithm(genes, domain)
                    domain_scores.append(score['fitness'])
                
                # Average fitness across domains
                avg_fitness = np.mean(domain_scores)
                generation_fitness.append({
                    'algorithm_id': i,
                    'genes': genes,
                    'fitness': avg_fitness,
                    'domain_scores': domain_scores
                })
            
            # Sort by fitness
            generation_fitness.sort(key=lambda x: x['fitness'], reverse=True)
            
            # Evolution: keep top 50%, generate new bottom 50%
            if gen < self.generations - 1:
                survivors = generation_fitness[:self.population_size // 2]
                self.population = [alg['genes'] for alg in survivors]
                
                # Generate new individuals through mutation/crossover
                while len(self.population) < self.population_size:
                    # Select parent
                    parent = np.random.choice(survivors)['genes']
                    
                    # Mutate
                    child = [SemanticGene(gene.operation, gene.parameters.copy()) for gene in parent]
                    
                    # Small chance to add/remove genes
                    if np.random.random() < 0.2:
                        if len(child) > 2 and np.random.random() < 0.5:
                            child.pop(np.random.randint(len(child)))
                        else:
                            operations = ["semantic_interference", "cluster_spacing", "similarity_boost", "semantic_ease"]
                            new_op = np.random.choice(operations)
                            new_params = {'intensity': np.random.uniform(0.1, 0.5)} if new_op == "semantic_interference" else {}
                            child.append(SemanticGene(new_op, new_params))
                    
                    # Mutate parameters
                    for gene in child:
                        for param_name, param_value in gene.parameters.items():
                            if np.random.random() < 0.3:
                                noise = np.random.normal(0, param_value * 0.1)
                                gene.parameters[param_name] = max(0.01, param_value + noise)
                    
                    self.population.append(child)
        
        return generation_fitness

def run_baseline_comparison(domains: List[ContentDomain]) -> Dict:
    """Compare semantic algorithms against non-semantic baselines."""
    
    print("Running baseline (non-semantic) comparison...")
    
    # Simple non-semantic scheduling
    baseline_results = {}
    
    for domain in domains:
        print(f"  Evaluating {domain.name} domain...")
        
        learners = [SyntheticLearner() for _ in range(20)]
        cards = [Card(difficulty=np.random.uniform(0.2, 0.8)) for _ in range(len(domain.items))]
        
        total_success = 0
        n_reviews = 0
        
        for learner in learners:
            for day in range(60):
                for card_idx, card in enumerate(cards[:10]):
                    # Standard interval without semantic awareness
                    if day % max(1, card.interval) == 0:
                        grade = learner.simulate_review(card, day)
                        success = 1 if grade >= 3 else 0
                        total_success += success
                        n_reviews += 1
                        
                        if success:
                            card.interval = max(1, int(card.interval * 1.5))
                        else:
                            card.interval = 1
        
        success_rate = total_success / n_reviews if n_reviews > 0 else 0
        efficiency = success_rate / max(1, n_reviews / 100)
        
        baseline_results[domain.name] = {
            'efficiency': efficiency,
            'success_rate': success_rate,
            'n_reviews': n_reviews
        }
    
    return baseline_results

def main():
    """Execute the complete semantic-aware experiment."""
    
    print("=== Semantic-Aware Algorithm Discovery Experiment ===")
    start_time = time.time()
    
    # Phase 1: Create content domains
    print("\nPhase 1: Creating semantic content domains...")
    content_generator = SemanticContentGenerator()
    domains = content_generator.create_domains()
    
    print(f"Created {len(domains)} domains:")
    for domain in domains:
        print(f"  {domain.name}: {len(domain.items)} items ({domain.semantic_density} density)")
        avg_similarity = np.mean(domain.similarity_matrix[np.triu_indices_from(domain.similarity_matrix, k=1)])
        print(f"    Average similarity: {avg_similarity:.3f}")
    
    # Phase 2: Run baseline comparison
    baseline_results = run_baseline_comparison(domains)
    
    # Phase 3: Run semantic evolution
    semantic_optimizer = SemanticEvolutionaryAlgorithm(domains)
    semantic_optimizer.initialize_population()
    evolved_results = semantic_optimizer.run_evolution()
    
    # Phase 4: Analysis
    print("\nAnalyzing results...")
    
    # Best semantic algorithms
    top_algorithms = evolved_results[:5]
    
    # Calculate improvements
    improvements = {}
    for domain in domains:
        baseline_eff = baseline_results[domain.name]['efficiency']
        
        # Get best semantic algorithm performance on this domain
        best_semantic = max(top_algorithms, key=lambda x: x['domain_scores'][domains.index(domain)])
        domain_idx = domains.index(domain)
        semantic_eff = best_semantic['domain_scores'][domain_idx] * best_semantic['fitness']
        
        improvement = (semantic_eff - baseline_eff) / baseline_eff if baseline_eff > 0 else 0
        improvements[domain.name] = improvement
    
    # Generate report
    report = {
        'experiment_metadata': {
            'experiment_id': 'exp_semantic_aware_002',
            'title': 'Semantic-Aware Algorithm Discovery',
            'execution_date': datetime.now().isoformat(),
            'duration_minutes': (time.time() - start_time) / 60.0,
            'hypothesis_tested': 'Semantic-aware algorithms achieve ≥15% improvement on high-similarity content'
        },
        'domain_analysis': {
            domain.name: {
                'semantic_density': domain.semantic_density,
                'n_items': len(domain.items),
                'avg_similarity': float(np.mean(domain.similarity_matrix[np.triu_indices_from(domain.similarity_matrix, k=1)])),
                'n_clusters': len(np.unique(domain.clusters))
            } for domain in domains
        },
        'baseline_results': baseline_results,
        'evolutionary_results': {
            'generations': semantic_optimizer.generations,
            'population_size': semantic_optimizer.population_size,
            'top_fitness_scores': [alg['fitness'] for alg in top_algorithms]
        },
        'performance_improvements': improvements,
        'key_findings': {
            'hypothesis_supported': any(imp >= 0.15 for imp in improvements.values()),
            'best_improvement_domain': max(improvements.keys(), key=lambda k: improvements[k]),
            'best_improvement_pct': max(improvements.values()) * 100,
            'semantic_operations_discovered': list(set([
                gene.operation for alg in top_algorithms for gene in alg['genes']
            ]))
        },
        'top_algorithm_analysis': {
            'best_algorithm_genes': [
                {'operation': gene.operation, 'parameters': gene.parameters} 
                for gene in top_algorithms[0]['genes']
            ],
            'complexity_score': len(top_algorithms[0]['genes']),
            'fitness_score': top_algorithms[0]['fitness']
        }
    }
    
    # Save results
    os.makedirs('../../data/exp_semantic_aware_002', exist_ok=True)
    
    with open('../../data/exp_semantic_aware_002/experiment_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    with open('../../data/exp_semantic_aware_002/domains_data.json', 'w') as f:
        domain_data = {
            domain.name: {
                'items': domain.items,
                'similarity_matrix': domain.similarity_matrix.tolist(),
                'clusters': domain.clusters.tolist()
            } for domain in domains
        }
        json.dump(domain_data, f, indent=2)
    
    print(f"\n=== EXPERIMENT COMPLETE ===")
    print(f"Execution time: {report['experiment_metadata']['duration_minutes']:.1f} minutes")
    print(f"Hypothesis supported: {report['key_findings']['hypothesis_supported']}")
    print(f"Best improvement: {report['key_findings']['best_improvement_pct']:.1f}% on {report['key_findings']['best_improvement_domain']}")
    print(f"Results saved to: data/exp_semantic_aware_002/")
    
    return report

if __name__ == "__main__":
    report = main()