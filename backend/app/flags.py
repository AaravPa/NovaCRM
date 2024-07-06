from typing import Dict, List

class FeatureFlags:
    def __init__(self):
        self.flags: Dict[str, Dict] = {
            "ai_lead_scoring": {
                "enabled": True,
                "rollout_percentage": 50,
                "description": "AI-powered lead scoring"
            },
            "advanced_analytics": {
                "enabled": True,
                "rollout_percentage": 25,
                "description": "Advanced analytics dashboard"
            },
            "webhook_notifications": {
                "enabled": False,
                "rollout_percentage": 0,
                "description": "Webhook notifications for integrations"
            }
        }
    
    def is_enabled(self, flag: str, user_id: int = None) -> bool:
        if flag not in self.flags:
            return False
        
        flag_config = self.flags[flag]
        if not flag_config.get("enabled", False):
            return False
        
        # Deterministic rollout based on user_id
        if user_id and flag_config.get("rollout_percentage", 100) < 100:
            hash_value = hash(f"{user_id}:{flag}") % 100
            return hash_value < flag_config["rollout_percentage"]
        
        return True

flags = FeatureFlags()
