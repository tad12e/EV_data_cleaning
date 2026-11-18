"""Master Orchestrator for Task 5 — Supplier, Importer, Distributor, Workshop & Trade Evidence
Module: choosing_spare_parts/src/collectors/run_task5_collection.py
Runs all collectors for Task 5, logs execution, and populates raw datasets across:
1. Ethiopian Suppliers & Spare Parts Sellers (raw_supplier_evidence.csv)
2. EV Importers & Distributors Trade Evidence (raw_importer_evidence.csv)
3. Repair Shops, Workshops & Technicians (raw_repair_evidence.csv)
4. Macro Trade Statistics & Customs Classifications (raw_trade_evidence.csv & raw_trade_statistics.csv)
5. Overseas Sourcing & OEM Procurement Feasibility (raw_overseas_sourcing.csv)
"""

import os
import sys
import logging
from datetime import datetime
import pandas as pd

# Setup logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOG_DIR = os.path.join(BASE_DIR, "data", "raw", "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "task5_collection.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("Task5_Orchestrator")

# Add project root to sys.path so modules can be imported directly
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
PARENT_DIR = os.path.dirname(BASE_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

from choosing_spare_parts.src.collectors.suppliers import collect_suppliers
from choosing_spare_parts.src.collectors.importers import collect_importers
from choosing_spare_parts.src.collectors.workshops import collect_workshops
from choosing_spare_parts.src.collectors.trade_data import collect_trade_data
from choosing_spare_parts.src.collectors.overseas_sourcing import collect_overseas_sourcing

def verify_task5_deliverables():
    """Audits generated datasets and prints summary statistics."""
    paths = {
        "Supplier Evidence": os.path.join(BASE_DIR, "data", "raw", "suppliers", "raw_supplier_evidence.csv"),
        "Importer Profiles": os.path.join(BASE_DIR, "data", "raw", "suppliers", "raw_importer_evidence.csv"),
        "Workshop Repair Evidence": os.path.join(BASE_DIR, "data", "raw", "workshops", "raw_repair_evidence.csv"),
        "Trade Evidence": os.path.join(BASE_DIR, "data", "raw", "trade", "raw_trade_evidence.csv"),
        "Trade Statistics (Legacy)": os.path.join(BASE_DIR, "data", "raw", "trade", "raw_trade_statistics.csv"),
        "Overseas Sourcing Quotes": os.path.join(BASE_DIR, "data", "raw", "suppliers", "raw_overseas_sourcing.csv"),
        "Failed Contacts Log": os.path.join(BASE_DIR, "docs", "failed_contacts.csv")
    }

    logger.info("=== AUDIT OF TASK 5 DELIVERABLES ===")
    all_ok = True
    for label, p in paths.items():
        if os.path.exists(p):
            df = pd.read_csv(p)
            logger.info(f"✓ {label:28}: {len(df):4d} records | File: {os.path.basename(p)}")
        else:
            logger.error(f"✗ {label:28}: MISSING FILE at {p}")
            all_ok = False
    return all_ok

def main():
    logger.info("=== STARTING TASK 5 COLLECTION PIPELINE ===")

    # 1. Ethiopian Suppliers & Spare Parts Sellers (5.1 & 5.2)
    logger.info("--- Step 1: Collecting Ethiopian EV Suppliers & Parts Sellers Evidence ---")
    try:
        collect_suppliers()
    except Exception as e:
        logger.error(f"Failed in suppliers collection: {e}", exc_info=True)

    # 2. Importers and Distributors (5.3)
    logger.info("--- Step 2: Collecting EV Importers & Distributors Trade Data ---")
    try:
        collect_importers()
    except Exception as e:
        logger.error(f"Failed in importers collection: {e}", exc_info=True)

    # 3. Repair Shops and Technicians (5.4 & 5.5)
    logger.info("--- Step 3: Collecting Workshop Repair Logs & Failure Evidence ---")
    try:
        collect_workshops()
    except Exception as e:
        logger.error(f"Failed in workshops collection: {e}", exc_info=True)

    # 4. Import/Export Evidence (5.6)
    logger.info("--- Step 4: Ingesting Customs, UN Comtrade & Macro Trade Data ---")
    try:
        collect_trade_data()
    except Exception as e:
        logger.error(f"Failed in trade data collection: {e}", exc_info=True)

    # 5. Overseas Sourcing Evidence (5.7)
    logger.info("--- Step 5: Collecting Overseas Sourcing Quotations & Factory MOQs ---")
    try:
        collect_overseas_sourcing()
    except Exception as e:
        logger.error(f"Failed in overseas sourcing collection: {e}", exc_info=True)

    # 6. Verification
    success = verify_task5_deliverables()
    if success:
        logger.info("=== TASK 5 COLLECTION PIPELINE COMPLETED SUCCESSFULLY ===")
    else:
        logger.warning("=== TASK 5 PIPELINE FINISHED WITH MISSING FILES ===")

if __name__ == "__main__":
    main()
