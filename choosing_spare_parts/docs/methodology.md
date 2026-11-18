# Methodology Specification

## 1. Data Collection Architecture
Data ingestion is structured into 4 distinct channels:
* **Marketplace Listings**: Web crawlers targeting Jiji.com.et and Adey Market.
* **Social Communications**: Telegram MTProto channel scrapers extracting repair inquiries and part availability.
* **Workshop Fieldwork**: Repair tickets and component replacement logs collected from 15+ EV garages in Addis Ababa.
* **Government Decrees & Trade Logs**: Tariff schedules and port customs statistics from MoFED, MoTL, and ECC.

## 2. Cleaning & Normalization Pipeline
1. **Deduplication**: Removes reposted classifieds using URL and phone number matching.
2. **Classification**: Maps unstructured Amharic and English descriptions into standardized OEM part codes.
3. **Outlier Filtering**: Removes unrealistic prices (< 500 ETB or > 2,000,000 ETB for non-battery items).
