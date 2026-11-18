"""Data Quality and Anomaly Validation Engine
Module: choosing_spare_parts/src/processing/validate.py
Audits missing required fields, price sanity ranges, date formats, currencies,
outlier detection, and unrecognized taxonomy entries.
Conforms to Master Prompt Section 6.5.
"""

import re
import logging
from datetime import datetime
from typing import Dict, Any, List, Tuple, Optional
import pandas as pd

logger = logging.getLogger("validate_engine")

# Sanity price bounds in ETB per category
PRICE_BOUNDS_ETB = {
    "brake_pads": (1000.0, 35000.0),
    "brake_discs": (2000.0, 65000.0),
    "cabin_air_filters": (500.0, 15000.0),
    "wiper_blades": (300.0, 12000.0),
    "headlights": (8000.0, 150000.0),
    "tail_lights": (5000.0, 95000.0),
    "side_mirrors": (4000.0, 75000.0),
    "bumpers": (8000.0, 95000.0),
    "fenders_body_panels": (5000.0, 65000.0),
    "shock_absorbers": (4000.0, 95000.0),
    "general_vehicle_presence": (800000.0, 15000000.0)
}

def validate_date(date_str: str) -> bool:
    """Validates date format YYYY-MM-DD and sanity boundaries."""
    if not isinstance(date_str, str) or not date_str.strip() or date_str == "nan":
        return False
    try:
        dt = datetime.strptime(date_str.strip()[:10], "%Y-%m-%d")
        if dt.year < 2020 or dt.year > 2027:
            return False
        return True
    except ValueError:
        return False

def validate_price(price: Any, category: str, currency: str) -> Tuple[bool, Optional[str]]:
    """Checks price sanity, currency, and outlier status."""
    if pd.isna(price) or price is None or price == "":
        return True, None  # Non-priced observation is valid (e.g. unpriced inquiry)

    try:
        val = float(price)
        if val <= 0:
            return False, "non_positive_price"

        curr = str(currency or "ETB").upper().strip()
        if curr not in ["ETB", "USD"]:
            return False, f"unsupported_currency_{curr}"

        # If in ETB, check against bounds
        if curr == "ETB" and category in PRICE_BOUNDS_ETB:
            min_p, max_p = PRICE_BOUNDS_ETB[category]
            if val < min_p:
                return False, f"price_suspiciously_low_{val}_for_{category}"
            if val > max_p:
                return False, f"price_outlier_high_{val}_for_{category}"

        # If in USD, sanity check for parts
        if curr == "USD":
            if val > 1500.0:
                return False, f"usd_price_outlier_{val}"

        return True, None
    except ValueError:
        return False, "invalid_numeric_price"

def validate_record(row: Dict[str, Any]) -> Dict[str, Any]:
    """Runs all validation rules on a single record."""
    issues: List[str] = []
    is_valid = True
    manual_review = False

    # 1. Vehicle Model Recognition
    vehicle = str(row.get("vehicle_model", ""))
    if vehicle in ["Unknown / Unspecified", "nan", ""]:
        issues.append("unrecognized_vehicle")
        manual_review = True

    # 2. Part Category Recognition
    part = str(row.get("part_category", ""))
    if part in ["generic_spare_part", "unspecified_part", "nan", ""]:
        issues.append("unrecognized_part_category")
        manual_review = True

    # 3. Date Validation
    pub_date = str(row.get("published_date", ""))
    if not validate_date(pub_date):
        issues.append("invalid_or_missing_date")

    # 4. Price Validation
    price = row.get("price")
    curr = str(row.get("currency", "ETB"))
    price_ok, price_msg = validate_price(price, part, curr)
    if not price_ok:
        issues.append(price_msg)
        if "outlier" in price_msg or "suspiciously" in price_msg:
            manual_review = True

    # 5. URL sanity
    url = str(row.get("source_url", ""))
    if url and url != "nan" and not (url.startswith("http://") or url.startswith("https://")):
        issues.append("malformed_url")

    # 6. Overall validation status
    if any("unrecognized" in i for i in issues) or len(issues) >= 2:
        val_status = "flagged_for_review"
    elif issues:
        val_status = "minor_warnings"
    else:
        val_status = "valid"

    return {
        "validation_status": val_status,
        "validation_issues": "; ".join(issues) if issues else "none",
        "manual_review_required": manual_review
    }
