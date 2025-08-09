"""
Evolutionary algorithm for discovering novel spaced repetition algorithms.
Uses genetic programming to evolve scheduling strategies.
"""

import random
import numpy as np
import math
from typing import List, Dict, Tuple, Callable, Any
from dataclasses import dataclass
from copy import deepcopy
import json

from baseline_algorithms import Card
from synthetic_learners import SyntheticLearner, generate_learner_population, create_test_cards

@dataclass
class AlgorithmGene:
    """Represents a gene in the algorithm DNA."""
    operation: str  # Operation type: 'multiply', 'add', 'power', 'min', 'max', 'threshold'
    param1: float   # First parameter
    param2: float   # Second parameter (if needed)
    input_var: str  # Input variable: 'ease', 'interval', 'difficulty', 'retrievability', 'repetitions'

class EvolvedAlgorithm:
    """Represents an evolved spaced repetition algorithm."""
    
    def __init__(self, genes: List[AlgorithmGene] = None):
        if genes is None:
            genes = self._random_genes()
        self.genes = genes
        self.fitness_scores = {}
        
    def _random_genes(self, n_genes: int = 8) -> List[AlgorithmGene]:
        """Generate random genes for initial population."""
        genes = []
        operations = ['multiply', 'add', 'power', 'min', 'max', 'threshold', 'ease_adjust']
        variables = ['ease', 'interval', 'difficulty', 'retrievability', 'repetitions', 'stability']
        
        for _ in range(n_genes):
            gene = AlgorithmGene(
                operation=random.choice(operations),
                param1=random.uniform(0.1, 3.0),
                param2=random.uniform(0.5, 2.0),
                input_var=random.choice(variables)
            )
            genes.append(gene)
        
        return genes
    
    def schedule_review(self, card: Card, grade: int) -> Tuple[Card, int]:
        """Execute the evolved algorithm to schedule next review."""
        
        # Initialize working variables
        vars_dict = {
            'ease': card.ease_factor,
            'interval': card.interval,
            'difficulty': card.difficulty,
            'retrievability': card.retrievability,
            'repetitions': card.repetitions,
            'stability': card.stability,
            'grade': grade
        }
        
        # Handle failure case (grade < 3)
        if grade < 3:
            card.repetitions = 0
            new_interval = max(1, int(self._apply_genes(vars_dict, 'failure')))
            card.interval = new_interval
            card.ease_factor = max(1.3, card.ease_factor * 0.85)  # Reduce ease on failure
        else:
            # Success case - apply evolved algorithm
            card.repetitions += 1
            
            # Calculate new interval using genes
            new_interval = self._apply_genes(vars_dict, 'success')
            card.interval = max(1, int(new_interval))
            
            # Update ease factor using genes
            ease_adjustment = self._apply_genes(vars_dict, 'ease')
            card.ease_factor = max(1.3, min(5.0, card.ease_factor + ease_adjustment))
            
            # Update stability (simple model)
            if hasattr(card, 'stability'):
                card.stability *= (1 + 0.1 * grade / 4.0)
        
        # Update retrievability based on new interval (decay model)
        if card.interval > 0:
            card.retrievability = max(0.1, card.retrievability * math.exp(-0.05 * card.interval))
        
        return card, card.interval
    
    def _apply_genes(self, vars_dict: Dict[str, float], context: str) -> float:
        """Apply genetic operations to calculate result."""
        result = vars_dict.get('interval', 1.0)  # Start with current interval
        
        # Filter genes by context (some genes only apply to success/failure/ease adjustment)
        relevant_genes = self.genes
        if context == 'failure':
            relevant_genes = [g for g in self.genes if 'failure' not in g.operation or g.param1 < 1.5]
        elif context == 'ease':
            relevant_genes = [g for g in self.genes if 'ease' in g.operation or g.input_var == 'ease']
            result = 0.0  # Start with 0 for ease adjustments
        
        for gene in relevant_genes:
            input_val = vars_dict.get(gene.input_var, 1.0)
            
            # Apply genetic operation
            if gene.operation == 'multiply':
                result *= (input_val * gene.param1)
            elif gene.operation == 'add':
                result += (input_val * gene.param1 + gene.param2)
            elif gene.operation == 'power':
                base = max(0.1, abs(input_val))
                power = max(0.1, min(3.0, gene.param1))
                result *= math.pow(base, power) * gene.param2
            elif gene.operation == 'min':
                result = min(result, input_val * gene.param1 + gene.param2)
            elif gene.operation == 'max':
                result = max(result, input_val * gene.param1 + gene.param2)
            elif gene.operation == 'threshold':
                if input_val > gene.param1:
                    result *= gene.param2
                else:
                    result *= (1.0 / gene.param2)
            elif gene.operation == 'ease_adjust':
                # Special operation for ease factor adjustments
                if context == 'ease':
                    grade_bonus = vars_dict.get('grade', 3) - 3  # -2 to +1
                    result += grade_bonus * gene.param1 * 0.1
        
        return result
    
    def mutate(self, mutation_rate: float = 0.3):
        """Mutate the algorithm by modifying genes."""
        for gene in self.genes:
            if random.random() < mutation_rate:
                # Mutate parameters
                if random.random() < 0.5:
                    gene.param1 *= random.uniform(0.8, 1.25)
                    gene.param1 = max(0.05, min(5.0, gene.param1))
                else:
                    gene.param2 *= random.uniform(0.8, 1.25)
                    gene.param2 = max(0.1, min(5.0, gene.param2))
                
                # Sometimes change operation or input variable
                if random.random() < 0.1:
                    operations = ['multiply', 'add', 'power', 'min', 'max', 'threshold', 'ease_adjust']
                    gene.operation = random.choice(operations)
                
                if random.random() < 0.1:
                    variables = ['ease', 'interval', 'difficulty', 'retrievability', 'repetitions', 'stability']
                    gene.input_var = random.choice(variables)
    
    def crossover(self, other: 'EvolvedAlgorithm') -> 'EvolvedAlgorithm':
        """Create offspring by crossing over with another algorithm."""
        # Single-point crossover
        crossover_point = random.randint(1, min(len(self.genes), len(other.genes)) - 1)
        
        new_genes = self.genes[:crossover_point] + other.genes[crossover_point:]
        offspring = EvolvedAlgorithm(new_genes)
        
        # Small chance to add or remove a gene
        if random.random() < 0.1 and len(offspring.genes) < 12:
            offspring.genes.append(offspring._random_genes(1)[0])
        elif random.random() < 0.1 and len(offspring.genes) > 3:
            offspring.genes.pop(random.randint(0, len(offspring.genes) - 1))
        
        return offspring
    
    def to_dict(self) -> Dict:
        """Serialize algorithm to dictionary."""
        return {
            'genes': [
                {
                    'operation': gene.operation,
                    'param1': gene.param1,
                    'param2': gene.param2,
                    'input_var': gene.input_var
                }
                for gene in self.genes
            ],
            'fitness_scores': self.fitness_scores
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'EvolvedAlgorithm':
        """Deserialize algorithm from dictionary."""
        genes = [
            AlgorithmGene(**gene_data)
            for gene_data in data['genes']
        ]
        algorithm = cls(genes)
        algorithm.fitness_scores = data.get('fitness_scores', {})
        return algorithm

def evaluate_algorithm_fitness(algorithm: EvolvedAlgorithm, 
                             learners: List[SyntheticLearner], 
                             cards: List[Card],
                             simulation_days: int = 100) -> Dict[str, float]:
    """
    Evaluate algorithm fitness across multiple learners and cards.
    Returns dictionary of performance metrics.
    """
    
    total_retention = 0.0
    total_reviews = 0
    total_study_time = 0
    successful_reviews = 0
    
    n_evaluations = min(50, len(learners))  # Sample subset for speed
    selected_learners = random.sample(learners, n_evaluations)
    
    for learner in selected_learners:
        learner_cards = [deepcopy(card) for card in cards[:20]]  # Sample 20 cards per learner
        
        # Simulate learning over time
        for day in range(simulation_days):
            for i, card in enumerate(learner_cards):
                # Check if card is due for review
                if card.last_review is None or \
                   (day - card.last_review.day if hasattr(card.last_review, 'day') else day) >= card.interval:
                    
                    # Simulate learner performance
                    days_since_review = day - (card.last_review.day if card.last_review and hasattr(card.last_review, 'day') else 0)
                    grade = learner.simulate_review(card, days_since_review)
                    
                    # Apply algorithm
                    from datetime import datetime, timedelta
                    card.last_review = datetime.now() - timedelta(days=simulation_days-day)
                    
                    old_retrievability = card.retrievability
                    updated_card, interval = algorithm.schedule_review(card, grade)
                    learner_cards[i] = updated_card
                    
                    # Track metrics
                    total_reviews += 1
                    total_study_time += interval
                    if grade >= 3:
                        successful_reviews += 1
                    total_retention += old_retrievability
    
    # Calculate fitness metrics
    if total_reviews == 0:
        return {'fitness': 0.0, 'retention': 0.0, 'efficiency': 0.0, 'success_rate': 0.0}
    
    avg_retention = total_retention / total_reviews
    success_rate = successful_reviews / total_reviews
    avg_interval = total_study_time / total_reviews
    efficiency = avg_retention / max(avg_interval, 1.0)  # Retention per day of spacing
    
    # Multi-objective fitness combining retention, efficiency, and success
    fitness = (avg_retention * 0.4 + efficiency * 0.4 + success_rate * 0.2)
    
    return {
        'fitness': fitness,
        'retention': avg_retention,
        'efficiency': efficiency, 
        'success_rate': success_rate,
        'avg_interval': avg_interval,
        'total_reviews': total_reviews
    }

class EvolutionaryOptimizer:
    """Main evolutionary algorithm for optimizing spaced repetition algorithms."""
    
    def __init__(self, population_size: int = 100, generations: int = 50):
        self.population_size = population_size
        self.generations = generations
        self.population = []
        self.best_algorithms = []
        self.generation_stats = []
        
    def initialize_population(self):
        """Initialize random population of algorithms."""
        self.population = [EvolvedAlgorithm() for _ in range(self.population_size)]
        
    def run_evolution(self, learners: List[SyntheticLearner], cards: List[Card]) -> List[EvolvedAlgorithm]:
        """Run the evolutionary algorithm."""
        
        print(f"Starting evolution: {self.population_size} algorithms, {self.generations} generations")
        
        for generation in range(self.generations):
            print(f"\nGeneration {generation + 1}/{self.generations}")
            
            # Evaluate fitness for all algorithms
            fitness_scores = []
            for i, algorithm in enumerate(self.population):
                if i % 10 == 0:
                    print(f"  Evaluating algorithm {i + 1}/{len(self.population)}")
                
                metrics = evaluate_algorithm_fitness(algorithm, learners, cards)
                algorithm.fitness_scores = metrics
                fitness_scores.append(metrics['fitness'])
            
            # Track generation statistics
            gen_stats = {
                'generation': generation + 1,
                'max_fitness': max(fitness_scores),
                'avg_fitness': sum(fitness_scores) / len(fitness_scores),
                'min_fitness': min(fitness_scores)
            }
            self.generation_stats.append(gen_stats)
            print(f"  Best fitness: {gen_stats['max_fitness']:.4f}, Avg: {gen_stats['avg_fitness']:.4f}")
            
            # Select best algorithms for next generation
            sorted_pop = sorted(zip(self.population, fitness_scores), key=lambda x: x[1], reverse=True)
            elite_size = self.population_size // 10  # Keep top 10%
            
            new_population = [alg for alg, _ in sorted_pop[:elite_size]]  # Elitism
            
            # Generate offspring through crossover and mutation
            while len(new_population) < self.population_size:
                # Tournament selection
                parent1 = self._tournament_selection(sorted_pop)
                parent2 = self._tournament_selection(sorted_pop)
                
                # Crossover
                offspring = parent1.crossover(parent2)
                
                # Mutation
                offspring.mutate()
                
                new_population.append(offspring)
            
            self.population = new_population
            
            # Save best algorithms from this generation
            best_algorithm = sorted_pop[0][0]
            self.best_algorithms.append(deepcopy(best_algorithm))
        
        # Return final sorted population
        final_fitness = [(alg, evaluate_algorithm_fitness(alg, learners, cards)['fitness']) 
                        for alg in self.population]
        return [alg for alg, _ in sorted(final_fitness, key=lambda x: x[1], reverse=True)]
    
    def _tournament_selection(self, sorted_population: List[Tuple], tournament_size: int = 5):
        """Select parent using tournament selection."""
        tournament = random.sample(sorted_population, min(tournament_size, len(sorted_population)))
        return max(tournament, key=lambda x: x[1])[0]  # Return algorithm with highest fitness
    
    def save_results(self, filename: str, best_algorithms: List[EvolvedAlgorithm]):
        """Save evolution results to file."""
        results = {
            'generation_stats': self.generation_stats,
            'best_algorithms': [alg.to_dict() for alg in best_algorithms[:10]],  # Top 10
            'evolution_params': {
                'population_size': self.population_size,
                'generations': self.generations
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)

if __name__ == "__main__":
    # Quick test run
    print("Testing evolutionary algorithm...")
    
    # Generate test data
    learners = generate_learner_population(50)  # Smaller for testing
    cards = create_test_cards(30)
    
    # Run small evolution
    optimizer = EvolutionaryOptimizer(population_size=20, generations=5)
    optimizer.initialize_population()
    
    best_algorithms = optimizer.run_evolution(learners, cards)
    
    print(f"\nEvolution complete! Best fitness: {best_algorithms[0].fitness_scores['fitness']:.4f}")
    print(f"Best algorithm has {len(best_algorithms[0].genes)} genes")