"""Assign credibility and reliability weights to evidence tiers"""
def get_source_weight(source_tier):
    weights = {"Tier 1 (Authoritative)": 1.0, "Tier 2 (High)": 0.85, "Tier 3 (Moderate)": 0.65}
    return weights.get(source_tier, 0.5)
