"""
Synthetic learner simulation for spaced repetition experiments.
Creates diverse learner profiles with realistic forgetting curves.
"""

import numpy as np
import random
from typing import List, Dict, Tuple
from dataclasses import dataclass
from baseline_algorithms import Card

@dataclass
class LearnerProfile:
    """Cognitive profile for a synthetic learner."""
    memory_strength: float = 1.0    # Base memory formation ability (0.5 - 2.0)
    forgetting_rate: float = 0.1    # How quickly memories decay (0.05 - 0.3)
    difficulty_sensitivity: float = 1.0  # How much difficulty affects performance (0.5 - 2.0)
    consistency: float = 0.8        # Performance consistency (0.6 - 1.0)
    learning_speed: float = 1.0     # How quickly ease improves (0.5 - 2.0)
    domain_expertise: float = 0.5   # Prior knowledge in domain (0.0 - 1.0)

class SyntheticLearner:
    """Simulates a learner with realistic memory dynamics."""
    
    def __init__(self, profile: LearnerProfile = None):
        if profile is None:
            profile = self._generate_random_profile()
        self.profile = profile
        
    def _generate_random_profile(self) -> LearnerProfile:
        """Generate a random but realistic learner profile."""
        return LearnerProfile(
            memory_strength=np.random.lognormal(0, 0.3),  # Log-normal for realistic distribution
            forgetting_rate=np.random.gamma(2, 0.05),     # Gamma for positive skew
            difficulty_sensitivity=np.random.lognormal(0, 0.2),
            consistency=np.random.beta(4, 1) * 0.4 + 0.6,  # Beta for bounded consistency
            learning_speed=np.random.lognormal(0, 0.2),
            domain_expertise=np.random.beta(2, 3)  # Most learners have low-medium expertise
        )
    
    def predict_recall_probability(self, card: Card, days_since_review: int) -> float:
        """
        Predict probability of successful recall based on learner profile and card history.
        Uses modified forgetting curve accounting for individual differences.
        """
        if days_since_review == 0:
            return 0.95  # Very high probability immediately after review
        
        # Base forgetting curve (Ebbinghaus-style exponential decay)
        base_retention = math.exp(-self.profile.forgetting_rate * days_since_review)
        
        # Adjust for memory strength
        strength_factor = self.profile.memory_strength
        adjusted_retention = 1 - (1 - base_retention) / strength_factor
        
        # Adjust for card difficulty and learner sensitivity  
        difficulty_penalty = card.difficulty * self.profile.difficulty_sensitivity * 0.2
        adjusted_retention *= (1 - difficulty_penalty)
        
        # Adjust for domain expertise (easier recall for familiar content)
        expertise_bonus = self.profile.domain_expertise * 0.1
        adjusted_retention += expertise_bonus
        
        # Add some noise for realism (reduced by consistency)
        noise_std = 0.1 * (1 - self.profile.consistency)
        if noise_std > 0:
            adjusted_retention += np.random.normal(0, noise_std)
        
        return max(0.01, min(0.99, adjusted_retention))
    
    def simulate_review(self, card: Card, days_since_review: int) -> int:
        """
        Simulate a review session and return grade (1-4).
        Based on recall probability and performance consistency.
        """
        recall_prob = self.predict_recall_probability(card, days_since_review)
        
        # Sample from recall probability with some noise
        performance = recall_prob + np.random.normal(0, 0.1 * (1 - self.profile.consistency))
        performance = max(0, min(1, performance))
        
        # Map performance to grade scale (1=again, 2=hard, 3=good, 4=easy)
        if performance < 0.3:
            return 1  # Again - failed recall
        elif performance < 0.6:
            return 2  # Hard - difficult but successful
        elif performance < 0.85:
            return 3  # Good - normal successful recall
        else:
            return 4  # Easy - very confident recall
    
    def update_from_feedback(self, card: Card, grade: int):
        """
        Update internal learner state based on review outcome.
        Simulates learning from the review experience.
        """
        # Learners gradually become more familiar with difficult cards
        if grade >= 3:  # Successful recall
            learning_rate = self.profile.learning_speed * 0.05
            if card.difficulty > 0.5:  # High difficulty cards
                # Learner becomes slightly better at this type of content
                self.profile.domain_expertise = min(1.0, 
                    self.profile.domain_expertise + learning_rate * card.difficulty)

def generate_learner_population(n_learners: int = 1000) -> List[SyntheticLearner]:
    """
    Generate a diverse population of synthetic learners.
    Creates realistic distribution of cognitive abilities.
    """
    learners = []
    
    # Create different learner archetypes
    archetypes = [
        # Fast learner: high memory, low forgetting
        {'memory_strength': 1.8, 'forgetting_rate': 0.06, 'learning_speed': 1.6},
        
        # Struggling learner: low memory, high forgetting
        {'memory_strength': 0.7, 'forgetting_rate': 0.18, 'learning_speed': 0.8},
        
        # Inconsistent learner: average memory, low consistency  
        {'memory_strength': 1.0, 'forgetting_rate': 0.12, 'consistency': 0.65},
        
        # Domain expert: high expertise, average other traits
        {'memory_strength': 1.1, 'domain_expertise': 0.85, 'difficulty_sensitivity': 0.7},
        
        # Diligent learner: high consistency, average abilities
        {'memory_strength': 1.0, 'forgetting_rate': 0.10, 'consistency': 0.95}
    ]
    
    # Generate learners with 70% completely random, 30% based on archetypes
    for i in range(n_learners):
        if i < int(0.7 * n_learners):
            # Random learner
            learners.append(SyntheticLearner())
        else:
            # Archetype-based learner with some variation
            archetype = random.choice(archetypes)
            profile = LearnerProfile()
            
            # Apply archetype characteristics with some noise
            for attr, value in archetype.items():
                setattr(profile, attr, value * np.random.normal(1.0, 0.1))
            
            # Ensure values stay in valid ranges
            profile.memory_strength = max(0.3, min(3.0, profile.memory_strength))
            profile.forgetting_rate = max(0.02, min(0.5, profile.forgetting_rate))
            profile.difficulty_sensitivity = max(0.2, min(3.0, profile.difficulty_sensitivity))
            profile.consistency = max(0.5, min(1.0, profile.consistency))
            profile.learning_speed = max(0.3, min(3.0, profile.learning_speed))
            profile.domain_expertise = max(0.0, min(1.0, profile.domain_expertise))
            
            learners.append(SyntheticLearner(profile))
    
    return learners

def create_test_cards(n_cards: int = 100) -> List[Card]:
    """Create a diverse set of test cards with varying difficulties."""
    cards = []
    
    for i in range(n_cards):
        difficulty = np.random.beta(2, 5)  # Most cards are easy, some are hard
        card = Card(
            difficulty=difficulty,
            stability=np.random.lognormal(0, 0.2),  # Initial stability varies
            retrievability=0.9  # Start with high retrievability
        )
        cards.append(card)
    
    return cards

if __name__ == "__main__":
    # Test synthetic learner generation
    import math
    
    print("Generating synthetic learner population...")
    learners = generate_learner_population(100)
    
    # Analyze population statistics
    memory_strengths = [l.profile.memory_strength for l in learners]
    forgetting_rates = [l.profile.forgetting_rate for l in learners]
    
    print(f"Memory strength: mean={np.mean(memory_strengths):.3f}, std={np.std(memory_strengths):.3f}")
    print(f"Forgetting rate: mean={np.mean(forgetting_rates):.3f}, std={np.std(forgetting_rates):.3f}")
    
    # Test recall prediction
    test_card = Card(difficulty=0.6, stability=5.0)
    sample_learner = learners[0]
    
    print(f"\nRecall probabilities for different intervals:")
    for days in [1, 3, 7, 14, 30]:
        prob = sample_learner.predict_recall_probability(test_card, days)
        print(f"Day {days}: {prob:.3f}")