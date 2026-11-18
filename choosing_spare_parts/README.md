# Ethiopian EV Spare-Parts Demand & Import Opportunity Research Pipeline

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tad12e/EV_data_cleaning/blob/main/choosing_spare_parts/notebooks/01_raw_data_exploration.ipynb)

A systematic, evidence-based research and data collection pipeline investigating customer demand, local supply scarcity, repair frequencies, component compatibility, and import opportunities for electric vehicle spare parts in Ethiopia.

---

## 1. Project Objectives & Core Question

> **Which vehicle-specific EV spare parts should an Ethiopian importer prioritize importing and stocking, based on available evidence of customer demand, local supply, scarcity, repair needs, sourcing feasibility, compatibility, and evidence reliability?**

This pipeline prioritizes Ethiopian ground reality: marketplaces, Telegram automotive channels, TikTok mechanics, licensed dealerships, independent workshops, and customs trade data. International data is strictly used for OEM part cross-referencing and FOB pricing—never mistaken for local Ethiopian demand.

---

## 2. Research Scope & The 30 Matrix Combinations

### A. 3 Target Vehicles
1. **BYD Seagull** (Urban Hatchback / 30.08 & 38.88 kWh / e-Platform 3.0)
2. **BYD Yuan Up** (Compact Family Crossover / 32.0 & 45.12 kWh / e-Platform 3.0 CTB)
3. **Changan Benben E-Star** (Commercial Fleet Runabout / 31.18 & 32.2 kWh / Green Taxi Fleet)

### B. 10 Initial Spare-Part Categories
1. **Brake pads** (Fast wear / friction consumable)
2. **Brake discs** (Medium wear / ventilated & solid rotors)
3. **Cabin-air filters** (Periodic maintenance / PM2.5 CN95 elements)
4. **Wiper blades** (Weather consumable / windshield visibility)
5. **Headlights** (LED projector assemblies / collision replacement)
6. **Tail lights** (Full-width LED rear signal clusters)
7. **Side mirrors** (Power-folding exterior mirrors / traffic strike replacement)
8. **Bumpers** (Front & rear molded bumper covers)
9. **Fender/body panels** (Stamped steel/aluminum outer panels & mudguards)
10. **Shock absorbers** (MacPherson front struts & rear dampers)

$$\mathbf{3\text{ Vehicles}} \times \mathbf{10\text{ Categories}} = \mathbf{30\text{ Vehicle–Part Research Matrix Combinations}}$$

---

## 3. Directory Architecture

```text
choosing_spare_parts/
├── README.md                          # Master module documentation
├── requirements.txt                   # Analytical and scraper dependencies
├── .env.example                       # API credentials template (Apify, Telegram)
├── .gitignore                         # Version control exclusions
│
├── config/                            # Structured YAML system configurations
│   ├── vehicles.yaml                  # Technical specs of the 3 target vehicles
│   ├── parts.yaml                     # The 10 standardized spare-part categories
│   ├── vehicle_aliases.yaml           # English, Chinese, and Amharic model aliases
│   ├── part_aliases.yaml              # Multilingual part aliases & ambiguous mappings
│   ├── search_queries.yaml            # 30-combination multi-platform search matrix
│   └── sources.yaml                   # 61 source collection profiles & rate limits
│
├── data/
│   ├── raw/                           # Immutable raw collection records (9 separate tiers)
│   │   ├── marketplaces/              # Product classifieds (Jiji, AfroMekina, Mekina.net)
│   │   ├── vehicle_listings/          # Complete vehicle presence ads
│   │   ├── social_media/              # TikTok video posts & public comments
│   │   ├── telegram/                  # Channels broadcast messages (@zemenmotors, etc.)
│   │   ├── suppliers/                 # Stock confirmations & direct quotations
│   │   ├── workshops/                 # Garage repair observations & technician statements
│   │   ├── customer_enquiries/        # Community demand & scarcity reports (@ev_ethiopia)
│   │   └── trade/                     # Customs (ECC) & UN Comtrade macro trade data
│   │
│   ├── processed/                     # Cleaned, classified, and scored analytical datasets
│   │   ├── cleaned_evidence.csv       # Master normalized evidence table
│   │   ├── vehicles.csv               # Processed target vehicle specifications
│   │   ├── parts.csv                  # Standardized 10 parts reference
│   │   ├── sources.csv                # Complete 61 validated source register
│   │   ├── compatibility.csv          # OEM part interchangeability matrix
│   │   ├── vehicle_part_summary.csv   # The 30-combination aggregated summary
│   │   └── import_priority_scores.csv # Decision matrix with decoupled confidence
│   │
│   └── reference/                     # Authoritative ground-truth reference tables
│       ├── oem_part_numbers.csv       # Initial verified OEM and cross-reference numbers
│       └── model_aliases.csv          # Normalized vehicle alias cross-walk
│
├── notebooks/                         # Executable Jupyter Notebooks (Google Colab Ready)
│   ├── 01_raw_data_exploration.ipynb
│   ├── 02_cleaning_and_validation.ipynb
│   ├── 03_demand_supply_analysis.ipynb
│   ├── 04_compatibility_and_sourcing.ipynb
│   └── 05_import_priority_scoring.ipynb
│
├── src/                               # Modular Python pipeline utilities
│   ├── collectors/                    # Platform collectors (Telegram, TikTok, Web)
│   ├── processing/                    # Normalizers, deduplicators, classifiers
│   ├── analysis/                      # Demand, supply, and scoring algorithms
│   └── utils/                         # Date parsers, text cleaners, loggers
│
├── reports/                           # Final outputs and visual deliverables
│   ├── figures/                       # Priority charts and demand plots
│   ├── tables/                        # Formatted decision matrices
│   └── final_recommendations.md       # Top-5 evidence-based import recommendations
│
└── docs/                              # Comprehensive auditability & methodological ledger
    ├── source_register.csv            # 61 discovered & audited sources in CSV
    ├── source_register.md             # Human-readable categorized source register
    ├── data_dictionary.md             # Complete schema dictionary for all tables
    ├── methodology.md                 # End-to-end analytical workflow
    ├── reliability_criteria.md        # 0–10 evidence quality scoring rules
    ├── scoring_methodology.md         # 5-factor import priority formula
    ├── assumptions.md                 # Explicit operational & engineering assumptions
    └── limitations.md                 # Technical, access, and market data caveats
```

---

## 4. Multi-Factor Import Priority Model

$$\text{Total Priority Score} = 0.30(D) + 0.25(S) + 0.20(C) + 0.15(F) + 0.10(R)$$

* **$D$ (Customer Demand, 30%)**: Customer requests, price enquiries, availability questions, and repair frequencies. *(Advertisements are explicitly never counted as demand)*.
* **$S$ (Local Scarcity, 25%)**: Absence of verified showroom floor stock and high frequency of "unavailable" reports.
* **$C$ (Compatibility Confidence, 20%)**: Verification of OEM part numbers and cross-model platform interchangeability.
* **$F$ (Sourcing Feasibility, 15%)**: Availability of tier-1 Chinese manufacturers, FOB price points, and shipping feasibility.
* **$R$ (Evidence Reliability, 10%)**: Composite 0–10 data quality score based on credibility, specificity, freshness, and corroboration.

### Decoupled Evidence Confidence
Every vehicle-part pair is classified independently into:
`High` | `Medium` | `Low` | `Insufficient Evidence`
*(A part with zero local evidence is flagged as `Insufficient Evidence`—never scored as zero demand).*

---

## 5. Google Colab Execution Guideline for Instructors

All notebooks in `notebooks/` are engineered to run seamlessly in **Google Colab** with **zero setup and no Google Drive mounting needed**:
```python
import pandas as pd
GITHUB_RAW = "https://raw.githubusercontent.com/tad12e/EV_data_cleaning/main/choosing_spare_parts"
df_parts = pd.read_csv(f"{GITHUB_RAW}/data/processed/parts.csv")
display(df_parts)
```
