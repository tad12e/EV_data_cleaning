"""Evidence Reliability and Freshness Scoring Engine
Module: choosing_spare_parts/src/processing/scoring.py
Computes objective, multi-dimensional reliability scores (0–10) and freshness scores (0–10)
adhering strictly to Master Prompt Section 6.7 & 6.8 and docs/reliability_criteria.md.
"""

import math
import logging
from datetime import datetime
from typing import Dict, Any, Tuple

logger = logging.getLogger("scoring_engine")

# Reference collection date (November 18, 2026)
COLLECTION_DATE_REF = datetime(2026, 11, 18)

# Baseline Credibility Scores by Source Category
SOURCE_CREDIBILITY_BASE = {
    "official_customs_government": 10.0,
    "authorized_distributor_oem": 9.0,
    "established_importer_wholesaler": 8.0,
    "verified_ev_workshop_technician": 7.5,
    "specialized_ev_retailer": 7.0,
    "verified_platform_merchant": 6.0,
    "classified_ad_marketplace": 5.0,
    "telegram_broadcast_channel": 4.5,
    "public_social_post": 4.0,
    "public_social_comment": 3.0,
    "anonymous_forum_post": 2.0,
    "unverified_source": 1.0
}

def calculate_freshness(published_date_str: str, collection_date_str: str = "2026-11-18") -> Tuple[int, float]:
    """Calculates age in days at collection and freshness score (0.0 to 10.0).
    Formula: Freshness = max(0.0, 10.0 - (age_in_days / 36.5))
    Returns: (age_days, freshness_score)
    """
    try:
        col_dt = datetime.strptime(str(collection_date_str)[:10], "%Y-%m-%d")
    except Exception:
        col_dt = COLLECTION_DATE_REF

    if not isinstance(published_date_str, str) or not published_date_str.strip() or published_date_str == "nan":
        # Undated evidence gets moderate freshness penalty
        return 180, 5.0

    try:
        pub_dt = datetime.strptime(str(published_date_str)[:10], "%Y-%m-%d")
        age_days = max(0, (col_dt - pub_dt).days)
    except Exception:
        age_days = 120

    # Freshness calculation on a 0-10 scale
    # Fresh (<30 days): 9.2 - 10.0
    # Moderate (30-90 days): 7.5 - 9.1
    # Aging (90-180 days): 5.0 - 7.4
    # Stale (180-365 days): 2.0 - 4.9
    # Historical (>365 days): 0.5 - 1.9
    freshness = max(0.5, min(10.0, 10.0 - (age_days / 36.5)))
    return age_days, round(freshness, 2)

def calculate_reliability_score(record: Dict[str, Any]) -> Dict[str, float]:
    """Computes transparent composite reliability score based on 6 evaluation dimensions:
    Reliability = 0.25(C) + 0.25(S) + 0.20(F) + 0.15(D) + 0.10(E) + 0.05(V)
    Adjusted based on evidence class (Compatibility vs Demand vs Stock).
    """
    evidence_class = str(record.get("evidence_type", "") or record.get("evidence_class", "")).lower()
    source_cat = str(record.get("source_category", "classified_ad_marketplace")).lower()
    vehicle = str(record.get("vehicle_model", ""))
    part = str(record.get("part_category", ""))
    oem_no = str(record.get("oem_part_number", "") or record.get("oem_number", ""))
    has_price = not (record.get("price") is None or str(record.get("price")) in ["nan", ""])

    # 1. Source Credibility (C, 25%)
    credibility = 5.0
    for k, score in SOURCE_CREDIBILITY_BASE.items():
        if k in source_cat:
            credibility = score
            break

    # 2. Evidence Specificity (S, 25%)
    # Full specificity: exact model + exact category + OEM number + position
    if vehicle not in ["Unknown / Unspecified", "Cross-Model EV / Unspecified"] and part not in ["generic_spare_part", "unspecified_part"]:
        if oem_no and oem_no != "nan":
            specificity = 10.0
        elif has_price:
            specificity = 8.5
        else:
            specificity = 7.0
    elif vehicle not in ["Unknown / Unspecified"]:
        specificity = 5.0
    else:
        specificity = 2.5

    # 3. Freshness (F, 20%)
    age_days, freshness = calculate_freshness(record.get("published_date"), record.get("collection_date"))

    # 4. Directness / Verification (D, 15%)
    if evidence_class in ["stock_confirmation", "repair_case", "purchase_report"]:
        directness = 9.5
    elif evidence_class in ["orderable_part", "exporter_quote", "price_enquiry"]:
        directness = 8.0
    elif evidence_class in ["seller_listing", "customer_demand"]:
        directness = 6.5
    elif evidence_class in ["general_vehicle_presence", "technical_observation"]:
        directness = 6.0
    else:
        directness = 4.0

    # 5. Extraction Quality & Completeness (E, 10%)
    missing_count = sum(1 for v in [vehicle, part, record.get("source_url")] if not v or str(v) == "nan")
    quality = max(2.0, 10.0 - (missing_count * 2.5))

    # 6. Corroboration (V, 5%)
    corroboration = 7.5 if has_price and vehicle not in ["Unknown / Unspecified"] else 5.0

    # Tailored weighting adjustments per Master Prompt Section 6.7:
    # - Compatibility evidence: Heavily weights Specificity (S) and OEM documentation.
    # - Stock confirmation: Heavily weights Directness (D) and Freshness (F).
    # - Customer demand: Evaluated as demand signal (honest intent), not proof of purchase.
    if evidence_class == "compatibility_evidence":
        composite = (0.15 * credibility) + (0.40 * specificity) + (0.10 * freshness) + (0.20 * directness) + (0.10 * quality) + (0.05 * corroboration)
    elif evidence_class in ["stock_confirmation", "stock_unavailable"]:
        composite = (0.25 * credibility) + (0.20 * specificity) + (0.25 * freshness) + (0.20 * directness) + (0.05 * quality) + (0.05 * corroboration)
    elif evidence_class in ["customer_demand", "price_enquiry"]:
        composite = (0.20 * credibility) + (0.25 * specificity) + (0.25 * freshness) + (0.15 * directness) + (0.10 * quality) + (0.05 * corroboration)
    else:
        # Standard balanced model
        composite = (0.25 * credibility) + (0.25 * specificity) + (0.20 * freshness) + (0.15 * directness) + (0.10 * quality) + (0.05 * corroboration)

    composite = max(1.0, min(10.0, round(composite, 2)))

    return {
        "age_days": age_days,
        "freshness_score": freshness,
        "source_credibility_score": round(credibility, 2),
        "specificity_score": round(specificity, 2),
        "directness_score": round(directness, 2),
        "extraction_quality_score": round(quality, 2),
        "reliability_score": composite
    }
