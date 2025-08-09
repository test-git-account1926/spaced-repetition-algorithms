"""
Baseline spaced repetition algorithms for comparison.
Implements SM-2, SM-17, Anki, and FSRS-4.5 algorithms.
"""

import math
import random
from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Card:
    """Represents a flashcard with learning history."""
    ease_factor: float = 2.5
    interval: int = 1  # days
    repetitions: int = 0
    last_review: datetime = None
    difficulty: float = 0.3  # 0 = easy, 1 = hard
    stability: float = 1.0   # memory stability
    retrievability: float = 0.9  # current recall probability

class SM2Algorithm:
    """SuperMemo SM-2 algorithm implementation."""
    
    def schedule_review(self, card: Card, grade: int) -> Tuple[Card, int]:
        """
        Schedule next review based on SM-2 algorithm.
        Grade: 0-5 (0=total blackout, 5=perfect response)
        Returns: (updated_card, next_interval_days)
        """
        card.repetitions += 1
        
        if grade < 3:  # Failed recall
            card.repetitions = 0
            card.interval = 1
        else:  # Successful recall
            if card.repetitions == 1:
                card.interval = 1
            elif card.repetitions == 2:
                card.interval = 6
            else:
                card.interval = int(card.interval * card.ease_factor)
            
            # Update ease factor
            card.ease_factor = max(1.3, card.ease_factor + (0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02)))
        
        card.last_review = datetime.now()
        return card, card.interval

class AnkiAlgorithm:
    """Anki default algorithm (modified SM-2)."""
    
    def __init__(self):
        self.graduating_interval = 1
        self.easy_interval = 4
        self.starting_ease = 2500  # 250%
        self.easy_bonus = 1.3
        self.interval_modifier = 1.0
        self.hard_multiplier = 1.2
        self.new_interval = 0.7
        
    def schedule_review(self, card: Card, grade: int) -> Tuple[Card, int]:
        """Grade: 1=again, 2=hard, 3=good, 4=easy"""
        
        if grade == 1:  # Again
            card.repetitions = 0
            card.interval = 1
            card.ease_factor = max(1300, card.ease_factor - 200)
        elif grade == 2:  # Hard
            card.interval = max(1, int(card.interval * self.hard_multiplier))
            card.ease_factor = max(1300, card.ease_factor - 150)
        elif grade == 3:  # Good
            if card.repetitions == 0:
                card.interval = self.graduating_interval
            else:
                card.interval = max(card.interval + 1, int(card.interval * card.ease_factor / 1000))
        elif grade == 4:  # Easy
            if card.repetitions == 0:
                card.interval = self.easy_interval
            else:
                card.interval = max(card.interval + 1, int(card.interval * card.ease_factor * self.easy_bonus / 1000))
            card.ease_factor = min(card.ease_factor + 150, 2500)
            
        card.repetitions += 1
        card.last_review = datetime.now()
        return card, card.interval

class FSRS45Algorithm:
    """FSRS-4.5 algorithm implementation."""
    
    def __init__(self):
        # Default FSRS-4.5 parameters
        self.parameters = [
            0.4872, 1.4003, 3.1145, 15.4722, 7.2102,
            0.5316, 1.0651, 0.0234, 1.616, 0.1544,
            1.0824, 1.9813, 0.0953, 0.2975, 2.2042,
            0.2407, 2.9466, 0.5034, 0.6567
        ]
    
    def _stability_after_success(self, state: int, difficulty: float, stability: float) -> float:
        """Calculate stability after successful recall."""
        if state == 0:  # New
            return self.parameters[0] + self.parameters[1] * difficulty
        elif state == 1:  # Learning
            return self.parameters[2] + self.parameters[3] * difficulty
        elif state == 2:  # Review
            return stability * (1 + math.exp(self.parameters[8]) * 
                              (11 - difficulty) * 
                              math.pow(stability, -self.parameters[9]) * 
                              (math.exp((1 - self.parameters[10]) * stability) - 1))
        return stability
    
    def _stability_after_failure(self, stability: float, retrievability: float) -> float:
        """Calculate stability after failed recall."""
        return self.parameters[11] * math.pow(difficulty, -self.parameters[12]) * \
               (math.pow(stability + 1, self.parameters[13]) - 1) * \
               math.exp((1 - retrievability) * self.parameters[14])
    
    def _retrievability(self, elapsed_days: int, stability: float) -> float:
        """Calculate current retrievability."""
        return math.pow(1 + elapsed_days / (9 * stability), -1)
    
    def schedule_review(self, card: Card, grade: int) -> Tuple[Card, int]:
        """Grade: 1=again, 2=hard, 3=good, 4=easy"""
        
        elapsed_days = 0
        if card.last_review:
            elapsed_days = (datetime.now() - card.last_review).days
            
        card.retrievability = self._retrievability(elapsed_days, card.stability)
        
        if grade == 1:  # Again
            card.stability = self._stability_after_failure(card.stability, card.retrievability)
            card.interval = 1
        else:  # Success
            state = 0 if card.repetitions == 0 else (1 if card.repetitions < 2 else 2)
            card.stability = self._stability_after_success(state, card.difficulty, card.stability)
            
            # Calculate interval based on desired retention (90%)
            target_retrievability = 0.9
            card.interval = max(1, int(card.stability * (math.pow(target_retrievability, 1/(-1)) - 1) / 9))
        
        card.repetitions += 1
        card.last_review = datetime.now()
        return card, card.interval

def evaluate_algorithm(algorithm, cards: List[Card], review_sequence: List[Tuple[int, int]]) -> Dict:
    """
    Evaluate algorithm performance.
    review_sequence: List of (card_index, grade) tuples
    Returns metrics dictionary.
    """
    total_reviews = 0
    successful_reviews = 0
    retention_scores = []
    intervals = []
    
    for card_idx, grade in review_sequence:
        if card_idx >= len(cards):
            continue
            
        card = cards[card_idx]
        old_retrievability = card.retrievability
        
        card, interval = algorithm.schedule_review(card, grade)
        
        total_reviews += 1
        if grade >= 3:  # Successful recall (grade 3+ for most systems)
            successful_reviews += 1
            
        retention_scores.append(old_retrievability)
        intervals.append(interval)
    
    metrics = {
        'total_reviews': total_reviews,
        'success_rate': successful_reviews / max(total_reviews, 1),
        'avg_retention': sum(retention_scores) / max(len(retention_scores), 1),
        'avg_interval': sum(intervals) / max(len(intervals), 1),
        'total_study_time_days': sum(intervals),
        'efficiency': (sum(retention_scores) / max(len(retention_scores), 1)) / max(sum(intervals), 1)
    }
    
    return metrics

if __name__ == "__main__":
    # Quick test of algorithms
    test_cards = [Card() for _ in range(10)]
    test_sequence = [(i % 10, random.randint(1, 4)) for i in range(100)]
    
    algorithms = {
        'SM2': SM2Algorithm(),
        'Anki': AnkiAlgorithm(), 
        'FSRS45': FSRS45Algorithm()
    }
    
    print("Algorithm Performance Comparison:")
    for name, algorithm in algorithms.items():
        cards_copy = [Card() for _ in range(10)]  # Fresh cards
        metrics = evaluate_algorithm(algorithm, cards_copy, test_sequence)
        print(f"{name}: Efficiency={metrics['efficiency']:.4f}, Success={metrics['success_rate']:.2f}")