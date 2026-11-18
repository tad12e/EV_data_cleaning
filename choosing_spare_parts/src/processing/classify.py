"""Evidence Classification Engine
Module: choosing_spare_parts/src/processing/classify.py
Classifies multi-source raw records into standard evidence classes adhering strictly
to Master Prompt Section 6.6.
"""

import re
import logging
from typing import Tuple

logger = logging.getLogger("classify_engine")

# 15 Standard Evidence Classes
VALID_EVIDENCE_CLASSES = {
    "customer_demand",
    "price_enquiry",
    "purchase_report",
    "repair_case",
    "seller_listing",
    "stock_confirmation",
    "stock_unavailable",
    "orderable_part",
    "import_evidence",
    "exporter_quote",
    "compatibility_evidence",
    "technical_observation",
    "general_vehicle_presence",
    "irrelevant",
    "uncertain"
}

def classify_evidence_record(
    source_dataset: str,
    raw_text: str,
    stock_status: str = "",
    enquiry_type: str = "",
    price: float = None,
    seller_or_customer: str = ""
) -> Tuple[str, str, float]:
    """Determines evidence class, evidence direction, and classification confidence.
    Returns: (evidence_class, evidence_direction, confidence)
    """
    text = (raw_text or "").lower()
    stock = (stock_status or "").lower()
    enq = (enquiry_type or "").lower()
    sc = (seller_or_customer or "").lower()

    # 1. Macro Trade / Customs Dataset
    if "trade" in source_dataset:
        return "import_evidence", "market_context", 0.95

    # 2. Workshop & Repair Records
    if "repair" in source_dataset or "workshop" in source_dataset:
        if "repair" in text or "replaced" in text or "work-order" in text:
            return "repair_case", "operational_demand", 0.95
        return "technical_observation", "technical_insight", 0.90

    # 3. Overseas Sourcing Quotations
    if "overseas" in source_dataset:
        return "exporter_quote", "sourcing_feasibility", 0.95

    # 4. Supplier & Importer Evidence
    if "supplier" in source_dataset:
        if stock == "in_stock" or "in stock" in stock:
            return "stock_confirmation", "local_supply", 0.95
        elif stock in ["orderable", "orderable_by_supplier"] or "order" in stock:
            return "orderable_part", "procurement_lead_time", 0.90
        elif stock in ["out_of_stock", "unavailable"]:
            return "stock_unavailable", "supply_scarcity", 0.90
        return "seller_listing", "local_supply", 0.85

    # 5. Customer Enquiries Dataset
    if "customer_enquiries" in source_dataset:
        if "complaint" in enq or "unavailable" in enq:
            return "stock_unavailable", "supply_scarcity", 0.95
        elif "price" in enq or "ዋጋ" in text:
            return "price_enquiry", "customer_intent", 0.95
        elif "purchase" in enq or "bought" in text:
            return "purchase_report", "verified_demand", 0.95
        elif "compatibility" in enq:
            return "compatibility_evidence", "technical_compatibility", 0.90
        return "customer_demand", "customer_intent", 0.95

    # 6. Social Comments (TikTok)
    if "social_comments" in source_dataset:
        if any(w in text for w in ["nice car", "ዋው", "super", "love it", "wow"]):
            return "irrelevant", "noise", 0.90
        if any(w in text for w in ["ስንት ነው ዋጋው", "ዋጋ", "how much", "price", "ዋጋው ስንት"]):
            if any(p in text for p in ["ፍሬን", "brake", "መስታወት", "mirror", "ባምፐር", "filter", "ሾክ", "part"]):
                return "price_enquiry", "customer_intent", 0.90
            return "general_vehicle_presence", "vehicle_interest", 0.80
        if any(w in text for w in ["አላችሁ", "የት ይገኛል", "where to find", "looking for", "ይገኛል"]):
            return "customer_demand", "customer_intent", 0.90
        if any(w in text for w in ["2 ወር", "ተሰብሮ", "አጣሁት", "waiting", "out of stock"]):
            return "stock_unavailable", "supply_scarcity", 0.90
        if any(w in text for w in ["ይገጥማል", "fit", "compatible", "ልዩነት"]):
            return "compatibility_evidence", "technical_compatibility", 0.85
        return "uncertain", "ambiguous", 0.50

    # 7. Telegram Posts
    if "telegram" in source_dataset:
        if sc == "customer" or any(w in text for w in ["የሚሸጥ አለ", "የት ይገኛል", "ፈላጊ ነኝ"]):
            return "customer_demand", "customer_intent", 0.90
        if any(w in text for w in ["in stock", "አስገብተናል", "አለቀ", "ይዘዙ"]):
            if "አስገብተናል" in text or "in stock" in text:
                return "stock_confirmation", "local_supply", 0.90
            return "orderable_part", "procurement_lead_time", 0.85
        if any(w in text for w in ["km range", "0 km", "የተሸጠ", "sold", "አዲስ መኪና"]):
            return "general_vehicle_presence", "vehicle_unit_supply", 0.90
        return "seller_listing", "local_supply", 0.80

    # 8. Marketplace Listings (Adey, Jiji, AfroMekina)
    if "marketplace" in source_dataset:
        if any(w in text for w in ["ev car", "zero mileage", "range 405", "range 305"]):
            return "general_vehicle_presence", "vehicle_unit_supply", 0.90
        return "seller_listing", "local_supply", 0.85

    # 9. Vehicle Listings
    if "vehicle_listings" in source_dataset:
        return "general_vehicle_presence", "vehicle_unit_supply", 0.95

    return "uncertain", "unclassified", 0.40
