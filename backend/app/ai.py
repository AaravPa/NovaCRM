import os
from typing import List, Dict

class LeadScoringModel:
    def __init__(self):
        self.weights = {
            "engagement": 0.4,
            "firmographic": 0.3,
            "behavioral": 0.3
        }
    
    def score_lead(self, contact: Dict) -> float:
        score = 0.0
        
        # Engagement scoring
        email_opens = contact.get("email_opens", 0)
        engagement_score = min(email_opens / 10, 1.0) * self.weights["engagement"]
        
        # Firmographic scoring (company size, industry)
        firmographic_score = 0.7 * self.weights["firmographic"]
        
        # Behavioral scoring
        behavioral_score = 0.5 * self.weights["behavioral"]
        
        score = engagement_score + firmographic_score + behavioral_score
        return min(score, 100.0)
    
    def rank_contacts(self, contacts: List[Dict]) -> List[Dict]:
        scored = []
        for contact in contacts:
            scored.append({
                **contact,
                "score": self.score_lead(contact)
            })
        
        return sorted(scored, key=lambda x: x["score"], reverse=True)

ai_model = LeadScoringModel()
