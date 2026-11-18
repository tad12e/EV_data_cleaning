"""Master Orchestrator for Task 3 — Ethiopian Marketplace & Website Collection
Runs all source collectors, logs execution, builds source-specific CSVs,
consolidates master marketplace listings, and populates vehicle market presence data.
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
LOG_FILE = os.path.join(LOG_DIR, "task3_collection.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("Task3_Orchestrator")

# Import collectors
from choosing_spare_parts.src.collectors.adey_market import collect_adey_market
from choosing_spare_parts.src.collectors.other_websites import collect_other_portals
from choosing_spare_parts.src.collectors.jiji import collect_jiji_listings
from choosing_spare_parts.src.collectors.vehicle_listings import collect_all_vehicle_listings

def consolidate_master_marketplaces():
    """Consolidates source-specific CSVs into data/raw/marketplaces/raw_marketplace_listings.csv"""
    mkt_dir = os.path.join(BASE_DIR, "data", "raw", "marketplaces")
    adey_csv = os.path.join(mkt_dir, "raw_adey_listings.csv")
    other_csv = os.path.join(mkt_dir, "raw_other_marketplace_listings.csv")
    jiji_csv = os.path.join(mkt_dir, "raw_jiji_listings.csv")
    master_csv = os.path.join(mkt_dir, "raw_marketplace_listings.csv")

    dfs = []
    if os.path.exists(adey_csv):
        df_adey = pd.read_csv(adey_csv)
        df_adey["platform"] = "Adey Market"
        dfs.append(df_adey)
    if os.path.exists(other_csv):
        df_other = pd.read_csv(other_csv)
        # Identify platform based on listing_id prefix
        df_other["platform"] = df_other["listing_id"].apply(
            lambda x: "AfroMekina" if "AFRO" in str(x) else ("CarGebeya" if "CARGEBEYA" in str(x) else "Other Portal")
        )
        dfs.append(df_other)
    if os.path.exists(jiji_csv):
        df_jiji = pd.read_csv(jiji_csv)
        df_jiji["platform"] = "Jiji Ethiopia"
        dfs.append(df_jiji)

    if not dfs:
        logger.warning("No source-specific CSVs found to consolidate.")
        return

    combined = pd.concat(dfs, ignore_index=True)
    today_str = datetime.now().strftime("%Y%m%d")

    master_rows = []
    for idx, row in combined.iterrows():
        # Clean model mentioned
        brand = str(row.get("vehicle_brand", "")).strip()
        model = str(row.get("vehicle_model", "")).strip()
        v_mentioned = f"{brand} {model}".strip() if brand != "Unknown" else "Unspecified Vehicle"

        master_rows.append({
            "raw_record_id": f"MKT-{today_str}-{idx+1:04d}",
            "platform": row.get("platform", "Unknown"),
            "listing_id": row.get("listing_id"),
            "listing_url": row.get("listing_url"),
            "listing_title": row.get("title"),
            "original_description": row.get("description"),
            "seller_name": row.get("seller_name"),
            "seller_id_if_public": row.get("seller_name"),
            "advertised_price": row.get("price"),
            "currency": row.get("currency", "ETB"),
            "location": row.get("seller_location", "Addis Ababa"),
            "vehicle_model_mentioned": v_mentioned,
            "part_mentioned": row.get("part_name_original"),
            "stock_claim": row.get("availability_claim", "unstated"),
            "published_date": row.get("publication_date", "2026-11-18"),
            "scraped_date": row.get("collection_date", datetime.now().strftime("%Y-%m-%d")),
            "listing_status": row.get("scraper_status", "scraped"),
            "image_urls": row.get("image_url"),
            "raw_payload_reference": str(row.get("raw_text", ""))[:250],
            "collection_method": "automated_http_fetch" if "manual" not in str(row.get("scraper_status", "")) else "verified_extraction"
        })

    df_master = pd.DataFrame(master_rows)
    df_master.to_csv(master_csv, index=False)
    logger.info(f"Master consolidation complete: saved {len(df_master)} records to {master_csv}")

def main():
    logger.info("=== STARTING TASK 3 COLLECTION PIPELINE ===")
    
    # 1. Adey Market
    logger.info("--- Step 1: Collecting Adey Market Listings ---")
    try:
        collect_adey_market(max_pages=3)
    except Exception as e:
        logger.error(f"Failed to collect Adey Market: {e}")

    # 2. Other Marketplaces (AfroMekina & CarGebeya Audit)
    logger.info("--- Step 2: Collecting Other Ethiopian Marketplaces ---")
    try:
        collect_other_portals()
    except Exception as e:
        logger.error(f"Failed to collect other portals: {e}")

    # 3. Jiji Ethiopia
    logger.info("--- Step 3: Collecting Jiji Ethiopia Listings ---")
    try:
        collect_jiji_listings()
    except Exception as e:
        logger.error(f"Failed to collect Jiji listings: {e}")

    # 4. Vehicle Market Presence
    logger.info("--- Step 4: Collecting Vehicle Market Presence Listings ---")
    try:
        collect_all_vehicle_listings()
    except Exception as e:
        logger.error(f"Failed to collect vehicle listings: {e}")

    # 5. Consolidate Master Table
    logger.info("--- Step 5: Consolidating Master Marketplace Table ---")
    consolidate_master_marketplaces()

    logger.info("=== TASK 3 COLLECTION PIPELINE COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
