# Vehicle Selection & Market Intelligence (`choosing_car_data`)

This directory contains the cleaned datasets, scraper scripts, and ranking methodology used to evaluate and select electric vehicle models in Ethiopia.

---

## The 7 Criteria Evaluation Model

Each model is evaluated across **7 weighted criteria**, producing an aggregate normalized score (0–100):

$$\text{Final Score} = 0.20(I) + 0.15(L) + 0.15(D) + 0.15(R) + 0.10(P) + 0.15(A) + 0.10(M)$$

Where:
* **$I$ (Import Evidence, Weight: 20%)**: Customs duty exemption application (0% CKD, 5% SKD, 15% CBU under MoFED Directive 877/2022), MoTL green transport transition priority, and Port of Djibouti manifests.
* **$L$ (Unique Listings, Weight: 15%)**: Frequency of verified unique vehicle ads across classifieds and Telegram channels.
* **$D$ (Dealer Availability, Weight: 15%)**: Floor stock readiness (*In-Stock / Ready* vs. *Pre-order*) across Addis Ababa dealerships (MOENCO, Kairos Addis, Zemen, Sara Import, EthioDrive dealers).
* **$R$ (Recent Activity, Weight: 15%)**: Listing velocity over 7-day and 30-day windows and active channel promotion.
* **$P$ (Price Competitiveness, Weight: 10%)**: Retail price in ETB relative to battery capacity (ETB per kWh) and affordability index.
* **$A$ (After-Sales Support, Weight: 15%)**: Authorized service centers, availability of diagnostic computers (BYD VDS, Toyota Techstream, cloned ODIS), and mechanic familiarity.
* **$M$ (Market Presence, Weight: 10%)**: Street visibility in Addis Ababa, adoption in ride-hailing/taxi fleets, and secondary market liquidity.

---

## Current Master Vehicle Ranking Summary

| Rank | Model | Final Score | Import (`I`) | Listings (`L`) | Dealer (`D`) | Recency (`R`) | Price (`P`) | After-Sales (`A`) | Market (`M`) | Primary Positioning |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **BYD Seagull** | **89.2** | 85.0 | 95.0 | 98.0 | 96.0 | 86.0 | 96.0 | 96.0 | Dominant Daily City Hatchback |
| **2** | **BYD Yuan Up** | **82.5** | 80.0 | 82.0 | 95.0 | 85.0 | 68.0 | 95.0 | 92.0 | High-Demand Compact Family Crossover |
| **3** | **Changan Benben E-Star** | **79.8** | 75.0 | 78.0 | 85.0 | 75.0 | 98.0 | 82.0 | 85.0 | Top Entry-Level Budget / Ride-Hailing |
| **4** | **Toyota bZ4X** | **77.4** | 70.0 | 85.0 | 92.0 | 80.0 | 62.0 | 88.0 | 90.0 | Executive & Diplomatic Crossover |
| **5** | **Volkswagen ID.6** | **53.6** | 50.0 | 75.0 | 70.0 | 65.0 | 48.0 | 30.0 | 45.0 | 7-Seater Luxury Family SUV |
| **6** | **Volkswagen ID.4** | **48.2** | 45.0 | 60.0 | 65.0 | 50.0 | 65.0 | 30.0 | 38.0 | Legacy Gray-Market Import |

---

## Dataset Directory

| File | Primary Contents |
| :--- | :--- |
| **`master_vehicle_ranking.csv`** | Consolidated matrix combining scores, formulas, and cross-references. |
| **`table1_import_evidence.csv`** | Official customs duty classifications, port manifests, and government directive URLs. |
| **`table2_unique_listings.csv`** | Granular listing feed (78+ records) with prices, conditions, dates, and seller contacts. |
| **`table3_dealer_availability.csv`** | Directory of showrooms in Addis Ababa, floor unit counts, and phone contacts. |
| **`table4_recent_activity.csv`** | 30-day listing velocities, active promotional channels, and momentum status. |
| **`table5_price_competitiveness.csv`** | Average asking price (ETB), price spreads, battery kWh, and efficiency ratios. |
| **`table6_after_sales_support.csv`** | Authorized workshops, battery diagnostic tool readiness, and warranty terms. |
| **`table7_market_presence.csv`** | City visibility index, taxi fleet adoption, and secondary cash liquidity. |

---

## Data Collection & Scraping Pipeline

### 1. Telegram Automotive Channel Scraper (`telegram_scraper.py`)
Collects live messages, media, prices, and phone contacts from Ethiopian automotive Telegram channels using the Apify MTProto Actor:
```bash
pip install -r requirements.txt
python telegram_scraper.py
```

### 2. Multi-Platform Web Scraper (`web_marketplace_scraper.py`)
Scrapes listings across Ethiopian vehicle classifieds (AfroMekina, Mekina.net, EthioDrive, CarGebeya) and integrates dealer networks (BYD MOENCO, Kairos Addis, Evtopia) alongside official government records:
```bash
python web_marketplace_scraper.py
```
