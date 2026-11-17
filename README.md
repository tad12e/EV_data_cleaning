# Ethiopian Electric Vehicle (EV) Market Intelligence & Data Cleaning

Comprehensive data collection, cleaning, and market intelligence repository analyzing the adoption, availability, pricing, and infrastructure of Electric Vehicles (EVs) in Ethiopia.

Driven by Ethiopia's historic transition policies—including the **Ministry of Transport and Logistics (MoTL)** nationwide ban on the import of internal combustion engine (ICE) passenger vehicles and **Ministry of Finance (MoFED)** tax incentive directives—this repository consolidates multi-platform market data, dealer inventories, and government records into structured, verifiable analytical datasets.

---

## Repository Architecture

```text
EV_data_cleaning/
├── README.md                          # Repository overview & navigation
├── .gitignore
├── choosing_car_data/                 # Component 1: Vehicle Selection & Ranking Intelligence
│   ├── README.md                      # Methodology, mathematical scoring & data dictionary
│   ├── requirements.txt               # Scraper & analytical dependencies
│   ├── telegram_scraper.py            # Automated Telegram channel & keyword scraper
│   ├── web_marketplace_scraper.py     # Multi-platform automotive web & gov directives scraper
│   ├── master_vehicle_ranking.csv     # Consolidated decision matrix & final vehicle rankings
│   ├── table1_import_evidence.csv     # Customs duties, MoTL decrees & port manifest data
│   ├── table2_unique_listings.csv     # Granular vehicle classifieds feed (Telegram & Web)
│   ├── table3_dealer_availability.csv # Physical Addis Ababa showroom census & contacts
│   ├── table4_recent_activity.csv     # Listing velocity, 30-day volume & market momentum
│   ├── table5_price_competitiveness.csv # Average prices (ETB), price spreads & kWh metrics
│   ├── table6_after_sales_support.csv # Warranty terms, diagnostics & mechanic readiness
│   └── table7_market_presence.csv     # Fleet adoption, street visibility & resale liquidity
└── choosing_spare_parts/              # Component 2: Spare Parts & Component Supply
    ├── .gitkeep
    └── README.md                      # Component roadmap & schema specifications
```

---

## Core Components

### 1. [`choosing_car_data/`](./choosing_car_data/)
Houses the vehicle selection intelligence framework. It evaluates and ranks the leading electric passenger cars in Ethiopia across **7 weighted criteria**:
1. **Import Evidence (`I`)**: Official customs clearance, MoFED Directive 877/2022 tariff exemptions, and Port of Djibouti manifests.
2. **Market Listings (`L`)**: Aggregated classifieds from Telegram automotive channels and Ethiopian web portals.
3. **Dealer Availability (`D`)**: Physical floor stock readiness across Addis Ababa showrooms (Bole, Saris, Mexico, Gotera).
4. **Recent Activity (`R`)**: 7-day and 30-day listing velocity and post freshness.
5. **Price Competitiveness (`P`)**: Price-to-battery ratio (ETB/kWh) and affordability benchmarking.
6. **After-Sales Support (`A`)**: Diagnostic tool coverage (BYD VDS, Techstream, ODIS), warranty support, and mechanic training.
7. **Market Presence (`M`)**: Street visibility, commercial fleet/ride-hailing deployment, and secondary resale liquidity.

### 2. [`choosing_spare_parts/`](./choosing_spare_parts/)
Reserved for the upcoming spare parts intelligence module. It will track battery replacement costs, suspension/braking component supply chains, and specialized EV diagnostic hardware availability across Ethiopian workshops.

---

## Contributing & Data Updates
Datasets can be updated on demand using the automated scraping scripts located in [`choosing_car_data/`](./choosing_car_data/).
