"""Master Orchestrator for Task 4 — Telegram, TikTok, Social Media & Customer Demand Evidence
Module: choosing_spare_parts/src/collectors/run_task4_collection.py
Runs all collectors for Task 4, logs execution, and populates raw social, telegram,
and customer demand evidence datasets.
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
LOG_FILE = os.path.join(LOG_DIR, "task4_collection.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("Task4_Orchestrator")

# Import Task 4 collectors
from choosing_spare_parts.src.collectors.telegram import collect_telegram_evidence
from choosing_spare_parts.src.collectors.tiktok_apify import collect_tiktok_social_evidence
from choosing_spare_parts.src.collectors.customer_enquiries import collect_customer_enquiries

def verify_task4_deliverables():
    """Audits generated datasets and prints summary statistics."""
    paths = {
        "Telegram Posts": os.path.join(BASE_DIR, "data", "raw", "telegram", "raw_telegram_posts.csv"),
        "Social Posts (TikTok)": os.path.join(BASE_DIR, "data", "raw", "social_media", "raw_social_posts.csv"),
        "Social Comments (TikTok)": os.path.join(BASE_DIR, "data", "raw", "social_media", "raw_social_comments.csv"),
        "Customer Demand Enquiries": os.path.join(BASE_DIR, "data", "raw", "customer_enquiries", "raw_customer_enquiries.csv")
    }

    logger.info("=== AUDIT OF TASK 4 DELIVERABLES ===")
    for label, p in paths.items():
        if os.path.exists(p):
            df = pd.read_csv(p)
            logger.info(f"✓ {label:26}: {len(df):4d} records | File: {os.path.basename(p)}")
        else:
            logger.error(f"✗ {label:26}: MISSING FILE at {p}")

def main():
    logger.info("=== STARTING TASK 4 COLLECTION PIPELINE ===")

    # 1. Telegram
    logger.info("--- Step 1: Ingesting Telegram Automotive Broadcasts & Discussions ---")
    try:
        collect_telegram_evidence()
    except Exception as e:
        logger.error(f"Failed to collect Telegram evidence: {e}")

    # 2. TikTok via Apify
    logger.info("--- Step 2: Collecting TikTok Posts & Public Comments via Apify ---")
    try:
        collect_tiktok_social_evidence()
    except Exception as e:
        logger.error(f"Failed to collect TikTok evidence: {e}")

    # 3. Customer Enquiries
    logger.info("--- Step 3: Aggregating Customer Demand & Scarcity Enquiries ---")
    try:
        collect_customer_enquiries()
    except Exception as e:
        logger.error(f"Failed to collect customer enquiries: {e}")

    # 4. Final Verification
    verify_task4_deliverables()
    logger.info("=== TASK 4 COLLECTION PIPELINE COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
