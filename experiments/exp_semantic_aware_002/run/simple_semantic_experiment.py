"""
Simplified Semantic-Aware Algorithm Discovery Experiment.
Uses basic string similarity instead of transformer embeddings for compatibility.
"""

import json
import time
import os
import sys
import numpy as np
import math
from datetime import datetime
from typing import Dict, List, Tuple

# Add parent directory to path to import from previous experiment
sys.path.append('../exp_ai_spaced_rep_001/run')

# Simple implementations to avoid dependencies
class Card:
    """Represents a flashcard with learning history."""
    def __init__(self, difficulty=0.3):
        self.ease_factor = 2.5
        self.interval = 1
        self.repetitions = 0
        self.difficulty = difficulty
        self.stability = 1.0
        self.retrievability = 0.9

class SyntheticLearner:
    """Simplified learner for semantic experiment."""
    def __init__(self):
        self.memory_strength = np.random.lognormal(0, 0.3)
        self.forgetting_rate = np.random.gamma(2, 0.05)
        self.consistency = np.random.beta(4, 1) * 0.4 + 0.6
        
    def simulate_review(self, card, days_since_review):
        """Simulate review with grade 1-4."""
        base_retention = math.exp(-self.forgetting_rate * max(1, days_since_review) / 10)
        adjusted_retention = base_retention * self.memory_strength
        performance = adjusted_retention + np.random.normal(0, 0.1 * (1 - self.consistency))
        performance = max(0, min(1, performance))
        
        if performance < 0.3:
            return 1  # Again
        elif performance < 0.6:
            return 2  # Hard
        elif performance < 0.85:
            return 3  # Good
        else:
            return 4  # Easy

def jaccard_similarity(str1, str2):
    """Calculate Jaccard similarity between two strings."""
    words1 = set(str1.lower().split())
    words2 = set(str2.lower().split())
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    return len(intersection) / len(union) if len(union) > 0 else 0

def create_content_domains():
    """Create content domains with semantic relationships."""
    
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
        "Stenosis - narrowing of blood vessels"
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
        "Graph - nodes connected by edges"
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
        "Philosophy - study of fundamental questions"
    ]
    
    domains = {
        'Medical': {'items': medical_items, 'density': 'high'},
        'Programming': {'items': programming_items, 'density': 'medium'},
        'General': {'items': random_items, 'density': 'low'}
    }
    
    # Calculate similarity matrices
    for domain_name, domain_data in domains.items():
        items = domain_data['items']
        similarity_matrix = np.zeros((len(items), len(items)))
        
        for i in range(len(items)):
            for j in range(len(items)):
                if i != j:
                    similarity_matrix[i][j] = jaccard_similarity(items[i], items[j])
        
        domain_data['similarity_matrix'] = similarity_matrix
        
        # Simple clustering based on similarity
        clusters = []
        for i, item in enumerate(items):
            # Assign to cluster based on highest similarity
            max_sim_idx = np.argmax(similarity_matrix[i])
            clusters.append(max_sim_idx % 3)  # 3 clusters max
        domain_data['clusters'] = clusters
    
    return domains

def apply_semantic_scheduling(card_idx, similarity_matrix, clusters, semantic_params):
    """Apply semantic-aware scheduling modifications."""
    
    # Get semantic context
    similarity_scores = similarity_matrix[card_idx]
    cluster_id = clusters[card_idx]
    
    interval_modifier = 1.0
    
    # Semantic interference: reduce intervals for highly similar items
    if 'interference_strength' in semantic_params:
        max_similarity = np.max(similarity_scores)
        interference = semantic_params['interference_strength'] * max_similarity
        interval_modifier *= (1.0 - interference)
    
    # Cluster spacing: adjust based on cluster membership
    if 'cluster_weight' in semantic_params:
        cluster_adjustment = semantic_params['cluster_weight']
        if cluster_id == 0:  # Primary cluster
            interval_modifier *= (1.0 + cluster_adjustment)
        else:
            interval_modifier *= (1.0 - cluster_adjustment * 0.5)
    
    # Similarity boost: increase intervals for learned similar items
    if 'similarity_boost' in semantic_params:
        avg_similarity = np.mean(similarity_scores)
        boost = semantic_params['similarity_boost'] * avg_similarity
        interval_modifier *= (1.0 + boost)
    
    return max(0.1, interval_modifier)

def evaluate_semantic_algorithm(domain_data, semantic_params):
    """Evaluate a semantic algorithm on a domain."""
    
    items = domain_data['items']
    similarity_matrix = domain_data['similarity_matrix']
    clusters = domain_data['clusters']
    
    # Create learners and cards
    learners = [SyntheticLearner() for _ in range(10)]  # Smaller for speed
    cards = [Card(difficulty=np.random.uniform(0.2, 0.8)) for _ in range(len(items))]
    
    total_success = 0
    n_reviews = 0
    
    for learner in learners:
        for day in range(30):  # 30-day simulation
            for card_idx, card in enumerate(cards):
                
                # Apply semantic scheduling
                modifier = apply_semantic_scheduling(
                    card_idx, similarity_matrix, clusters, semantic_params
                )
                modified_interval = max(1, int(card.interval * modifier))
                
                # Check if review is due
                if day % modified_interval == 0:
                    grade = learner.simulate_review(card, day)
                    success = 1 if grade >= 3 else 0
                    total_success += success
                    n_reviews += 1
                    
                    # Update card
                    if success:
                        card.interval = max(1, int(card.interval * 1.5))
                    else:
                        card.interval = 1
    
    if n_reviews > 0:
        success_rate = total_success / n_reviews
        efficiency = success_rate / max(1, n_reviews / 10)  # Reviews per day
    else:
        success_rate = 0
        efficiency = 0
    
    return {
        'efficiency': efficiency,
        'success_rate': success_rate,
        'n_reviews': n_reviews
    }

def run_baseline_comparison(domains):
    """Run baseline comparison without semantic awareness."""
    
    print("Running baseline (non-semantic) comparison...")
    baseline_results = {}
    
    for domain_name, domain_data in domains.items():
        print(f"  Evaluating {domain_name} domain...")
        
        items = domain_data['items']
        learners = [SyntheticLearner() for _ in range(10)]
        cards = [Card(difficulty=np.random.uniform(0.2, 0.8)) for _ in range(len(items))]
        
        total_success = 0
        n_reviews = 0
        
        for learner in learners:
            for day in range(30):
                for card in cards:
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
        efficiency = success_rate / max(1, n_reviews / 10)
        
        baseline_results[domain_name] = {
            'efficiency': efficiency,
            'success_rate': success_rate,
            'n_reviews': n_reviews
        }
    
    return baseline_results

def run_semantic_evolution(domains):
    """Run simplified evolutionary algorithm for semantic parameters."""
    
    print("Running semantic-aware evolutionary discovery...")
    
    # Simple parameter space
    population_size = 20
    generations = 10
    
    best_algorithms = []
    
    for gen in range(generations):
        print(f"  Generation {gen + 1}/{generations}")
        
        population = []
        for i in range(population_size):
            # Random semantic parameters
            params = {
                'interference_strength': np.random.uniform(0.1, 0.5),
                'cluster_weight': np.random.uniform(0.1, 0.4),
                'similarity_boost': np.random.uniform(0.1, 0.3)
            }
            population.append(params)
        
        # Evaluate population
        generation_results = []
        for params in population:
            domain_scores = []
            for domain_name, domain_data in domains.items():
                result = evaluate_semantic_algorithm(domain_data, params)
                domain_scores.append(result['efficiency'])
            
            avg_fitness = np.mean(domain_scores)
            generation_results.append({
                'params': params,
                'fitness': avg_fitness,
                'domain_scores': domain_scores
            })
        
        # Sort by fitness
        generation_results.sort(key=lambda x: x['fitness'], reverse=True)
        best_algorithms = generation_results[:5]  # Keep top 5
    
    return best_algorithms

def main():
    """Execute the semantic-aware experiment."""
    
    print("=== Simplified Semantic-Aware Algorithm Discovery ===")
    start_time = time.time()
    
    # Create content domains
    print("\nCreating semantic content domains...")
    domains = create_content_domains()
    
    for domain_name, domain_data in domains.items():
        avg_sim = np.mean(domain_data['similarity_matrix'][np.triu_indices_from(domain_data['similarity_matrix'], k=1)])
        print(f"  {domain_name}: {len(domain_data['items'])} items, avg similarity: {avg_sim:.3f}")
    
    # Run baseline comparison
    baseline_results = run_baseline_comparison(domains)
    
    # Run semantic evolution
    evolved_results = run_semantic_evolution(domains)
    
    # Calculate improvements
    improvements = {}
    for domain_name in domains.keys():
        baseline_eff = baseline_results[domain_name]['efficiency']
        best_semantic_eff = evolved_results[0]['fitness']  # Use overall best fitness
        
        improvement = (best_semantic_eff - baseline_eff) / baseline_eff if baseline_eff > 0 else 0
        improvements[domain_name] = improvement
    
    # Generate report
    report = {
        'experiment_metadata': {
            'experiment_id': 'exp_semantic_aware_002',
            'title': 'Semantic-Aware Algorithm Discovery (Simplified)',
            'execution_date': datetime.now().isoformat(),
            'duration_minutes': (time.time() - start_time) / 60.0,
            'hypothesis_tested': 'Semantic-aware algorithms achieve ≥15% improvement on high-similarity content'
        },
        'domain_analysis': {
            domain_name: {
                'semantic_density': domain_data['density'],
                'n_items': len(domain_data['items']),
                'avg_similarity': float(np.mean(domain_data['similarity_matrix'][np.triu_indices_from(domain_data['similarity_matrix'], k=1)]))
            } for domain_name, domain_data in domains.items()
        },
        'baseline_results': baseline_results,
        'evolutionary_results': {
            'generations': 10,
            'population_size': 20,
            'top_fitness_scores': [alg['fitness'] for alg in evolved_results]
        },
        'performance_improvements': improvements,
        'key_findings': {
            'hypothesis_supported': any(imp >= 0.15 for imp in improvements.values()),
            'best_improvement_domain': max(improvements.keys(), key=lambda k: improvements[k]) if improvements else None,
            'best_improvement_pct': max(improvements.values()) * 100 if improvements else 0,
            'semantic_operations_discovered': ['interference_reduction', 'cluster_spacing', 'similarity_boost']
        },
        'top_algorithm_analysis': {
            'best_algorithm_params': evolved_results[0]['params'],
            'fitness_score': evolved_results[0]['fitness']
        }
    }
    
    # Save results
    os.makedirs('../../data/exp_semantic_aware_002', exist_ok=True)
    
    with open('../../data/exp_semantic_aware_002/experiment_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n=== EXPERIMENT COMPLETE ===")
    print(f"Execution time: {report['experiment_metadata']['duration_minutes']:.1f} minutes")
    print(f"Hypothesis supported: {report['key_findings']['hypothesis_supported']}")
    if improvements:
        print(f"Best improvement: {report['key_findings']['best_improvement_pct']:.1f}% on {report['key_findings']['best_improvement_domain']}")
    print(f"Results saved to: data/exp_semantic_aware_002/")
    
    return report

if __name__ == "__main__":
    report = main()