"""Calculate composite import priority scores for spare parts"""
import pandas as pd

def calculate_import_priority(demand_score, scarcity_score, failure_rate):
    # Composite score formula: 0.40*Demand + 0.35*Scarcity + 0.25*FailureRate
    return round(0.40 * demand_score + 0.35 * scarcity_score + 0.25 * failure_rate, 2)
