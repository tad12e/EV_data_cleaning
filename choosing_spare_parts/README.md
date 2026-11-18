# Ethiopian EV Spare-Parts Sourcing & Import Prioritization Pipeline (`choosing_spare_parts`)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tad12e/EV_data_cleaning/blob/main/choosing_spare_parts/notebooks/00_master_ev_parts_pipeline.ipynb)

A systematic, evidence-based research and data collection pipeline investigating customer demand, local supply scarcity, repair frequencies, component compatibility, and import opportunities for electric vehicle spare parts in Ethiopia.

---

## 1. Quick Navigation: Where to Find the Recommendations

If you are looking for the final commercial recommendations and analytical findings:
1. **Right Inside This README**: See [Section 4 below](#4-the-definitive-top-5-import-recommendations) for the complete Top 5 recommendation tables and detailed part profiles.
2. **Dedicated Final Report File**: [`reports/final_recommendations.md`](./reports/final_recommendations.md) (Full 14 KB detailed report with counter-evidence and policy analysis).
3. **Master Colab Notebook**: [`notebooks/00_master_ev_parts_pipeline.ipynb`](./notebooks/00_master_ev_parts_pipeline.ipynb) (Execute end-to-end with zero setup by clicking **`Runtime` ➔ `Run all`**).
4. **Scored Decision CSV**: [`data/processed/import_priority_scores.csv`](./data/processed/import_priority_scores.csv) (Machine-readable dataset of all 30 combinations).

---

## 2. Research Scope: The 30 Matrix Combinations

Following the vehicle selection pipeline in `choosing_car_data/`, the research scope covers the **3 dominant EV models** across **10 standardized spare-part categories**:

$$\mathbf{3\text{ Target Vehicles}} \times \mathbf{10\text{ Part Categories}} = \mathbf{30\text{ Vehicle–Part Research Combinations}}$$

* **3 Target Vehicles**:
  1. **BYD Seagull**: #1 Private Commuter EV (38.5% Import Share, >15,000 units in Addis Ababa).
  2. **BYD Yuan Up**: #1 Subcompact Crossover EV (24.0% Import Share, rapid family adoption in 2024).
  3. **Changan Benben E-Star**: #1 Commercial Taxi Fleet EV (20.0% Import Share, >2,000 green taxis in Addis Ababa).
* **10 Core Spare-Part Categories**:
  1. `brake_pads`: Front and rear ceramic/metallic friction pads.
  2. `brake_discs`: Ventilated front and solid rear cast iron rotors.
  3. `cabin_air_filters`: PM2.5 / CN95 activated carbon HVAC filter cartridges.
  4. `wiper_blades`: Aerodynamic rubber windshield wiper sets.
  5. `headlights`: Full LED projector headlight assemblies with integrated DRL.
  6. `tail_lights`: Full-width rear LED signal clusters and trunk bars.
  7. `side_mirrors`: Power-folding exterior mirror assemblies with cameras and blind-spot LEDs.
  8. `bumpers`: Molded polypropylene front and rear bumper cover shells.
  9. `fenders_body_panels`: Stamped outer steel/aluminum wing panels and mudguards.
  10. `shock_absorbers`: MacPherson front hydraulic struts and rear damper pairs.

---

## 3. In-Depth Breakdown of the 5 Spare-Part Ranking Criteria & Evidence Sources

$$\text{Total Priority Score} = 0.30(D) + 0.25(S) + 0.20(C) + 0.15(F) + 0.10(R)$$

### Pillar 1: Customer & Operational Demand ($D$) — Weight: 30%
* **What it measures**: Non-discretionary mechanical failure rates, documented workshop replacements, direct buyer requests, and availability inquiries. *(Note: Seller advertisements are strictly excluded from demand to prevent seller spam from inflating scores).*
* **Mathematical Formula**:
  $$D = \min\left(100.0, \; 15 \times N_{\text{requests}} + 1.5 \times N_{\text{repairs}} + 5 \times N_{\text{enquiries}} + 0.5 \times \text{Fleet Index}\right)$$
  *(Fleet Index: 40.0 for Seagull, 25.0 for Yuan Up, 35.0 for Benben).*
* **Evidence Tables**:
  * [`data/raw/workshops/raw_repair_evidence.csv`](./data/raw/workshops/raw_repair_evidence.csv): 298 audited repair cases across Addis Ababa EV service centers.
  * [`data/raw/customer_enquiries/raw_customer_enquiries.csv`](./data/raw/customer_enquiries/raw_customer_enquiries.csv): 12 verified multi-platform buyer scarcity inquiries.
  * [`data/processed/cleaned_evidence.csv`](./data/processed/cleaned_evidence.csv): Filtered `customer_demand` and `price_enquiry` observations.
* **Data Sources & Ground Reality**:
  * **Lideta Green Taxi Repair Hubs & Kera Mechanical Garages**: Provided verified logs showing that Addis Ababa's unpaved cobblestones and potholes cause premature failure of Changan Benben shock absorbers at ~40,000 km (36 cases) and bumper fractures (19 cases).
  * **Addis Commuter Driving**: PM2.5 high-dust road conditions clog BYD Seagull and Yuan Up cabin filters in under 8,000 km (42 cases).

---

### Pillar 2: Local Market Scarcity ($S$) — Weight: 25%
* **What it measures**: Absence of physical showroom/shelf stock, confirmed out-of-stock reports, and long pre-order delays (14 to 50 days) that leave accident and broken vehicles grounded.
* **Mathematical Formula**:
  * If verified physical floor stock is **0 units**: $S = \min\left(100.0, \; 80.0 + 10 \times N_{\text{unavailable}} + 5 \times N_{\text{orderable}}\right)$
  * If floor stock exists: $S = \min\left(100.0, \; 20 \times N_{\text{unavailable}} + 15 \times N_{\text{orderable}} + \left[1 - \frac{N_{\text{stock}}}{N_{\text{enquiries}} + 1}\right] \times 50\right)$
* **Evidence Tables**:
  * [`data/raw/suppliers/raw_supplier_evidence.csv`](./data/raw/suppliers/raw_supplier_evidence.csv): 24 verified physical showroom and telephone inventory audits.
  * [`data/raw/workshops/raw_repair_evidence.csv`](./data/raw/workshops/raw_repair_evidence.csv): Records documenting component availability bottlenecks.
* **Data Sources & Ground Reality**:
  * Audits of specialized retailers (**TAK Auto, Sunny Spare Parts, SARA General Import PLC, Bole EV Parts**) reveal a **severe market bifurcation**: fast-moving maintenance items (wipers, brake pads) have intermittent shelf stock, but collision parts (bumpers, headlights, mirrors) have **0% physical stock**, forcing taxi drivers to wait 30–50 days or resort to temporary fiberglass patches.

---

### Pillar 3: Compatibility & Fitment Certainty ($C$) — Weight: 20%
* **What it measures**: Verification of official manufacturer OEM part numbers, variant fitment certainty, and platform interchangeability (e.g., parts shared across BYD e-Platform 3.0 models).
* **Scoring Rules**:
  * **100.0**: Verified OEM part number with confirmed cross-model platform interchangeability.
  * **85.0**: Verified OEM part number from official manufacturer EPC (single-model fitment).
  * **60.0**: Aftermarket fitment listed by tier-1 supplier without official OEM stamping.
  * **40.0**: Dimensions known, but physical mounting points unverified.
* **Evidence Tables**:
  * [`data/reference/oem_part_numbers.csv`](./data/reference/oem_part_numbers.csv): 44 verified manufacturer part numbers.
  * [`data/processed/compatibility.csv`](./data/processed/compatibility.csv): 30-combination fitment register.
* **Data Sources & Ground Reality**:
  * **BYD FinDreams & Electronic Parts Catalogues (EPC)**: Confirmed that BYD Seagull and BYD Dolphin share the same front brake pad caliper architecture (`BYD-3501110-00`), and all BYD e-Platform 3.0 models (Seagull, Yuan Up, Dolphin, Atto 3) utilize the exact same CN95 cabin air filter cartridge (`BYD-8114010-00`), enabling commercial importers to minimize inventory fragmentation.

---

### Pillar 4: Sourcing Feasibility & Landed Economics ($F$) — Weight: 15%
* **What it measures**: Availability of certified Chinese tier-1 factories, unit FOB price affordability, packaging bulkiness, logistics mode (air cargo via Bole ADD vs sea freight via Port of Djibouti), and landed import duties under **Directive 922/2022**.
* **Mathematical Formula**:
  $$F = 0.40(\text{Supplier Availability}) + 0.30(\text{Price Affordability Index}) + 0.30(\text{Shipping Feasibility})$$
* **Evidence Tables**:
  * [`data/raw/suppliers/raw_overseas_sourcing.csv`](./data/raw/suppliers/raw_overseas_sourcing.csv): 12 verified tier-1 factory quotes from Chongqing, Shenzhen, Guangzhou, and Changzhou.
  * Ethiopian Ministry of Finance **Directive 922/2022**: EV spare parts clear customs at **5% customs duty** and are **completely exempt from VAT (0%), Excise Tax (0%), and Surtax (0%)**.
* **Data Sources & Ground Reality**:
  * High-value lightweight items (side mirrors @ $50 FOB, LED headlights @ $165 FOB) are optimal for **emergency air cargo via Bole ADD** (8–14 day transit). Bulky heavy items (injection-molded bumper shells @ $35 FOB, cast-iron brake rotors @ $18 FOB) require **20ft sea container consolidation via Port of Djibouti and Modjo Dry Port** to preserve 60%+ gross margins.

---

### Pillar 5: Evidence Reliability ($R$) — Weight: 10%
* **What it measures**: Multi-source data credibility, extraction verification, and freshness (0–10 scale) documented in [`docs/reliability_criteria.md`](./docs/reliability_criteria.md).
* **Scoring Rules**:
  $$R = 0.25(\text{Credibility}) + 0.25(\text{Specificity}) + 0.20(\text{Freshness}) + 0.15(\text{Directness}) + 0.15(\text{Verification})$$
* **Data Sources & Ground Reality**:
  * Observations verified by physical workshop inspections and formal distributor price lists receive high credibility scores (7.5–9.0), while anonymous social media comments receive lower scores (3.0–4.0).

---

## 4. The Definitive Top 5 Import Recommendations

The ranking engine evaluated all 30 combinations without data fabrication. Combinations with zero local records were quarantined as `Insufficient Evidence` data gaps.

### Summary Recommendation Table

| Rank | Vehicle Model | Spare-Part Category | Priority Score (0–100) | Confidence Level | Recommendation Tier | Quoted Local Retail Price (ETB) | Factory FOB Price (USD) | Est. Landed Cost (ETB) | Gross Profit Margin | Key Operational Driver |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Changan Benben E-Star** | **Bumpers (Front Cover Shell)** | **86.9** | **High** | **Strong Recommendation** | 31,000 – 38,000 ETB | $28 – $45 | ~13,500 ETB | **58% – 64%** | Taxi fleet collision shortage; 60% fiberglass patches |
| **2** | **BYD Yuan Up** | **Side Mirrors (Power-Folding Assembly)** | **86.3** | **High** | **Strong Recommendation** | 24,000 – 29,500 ETB | $42 – $58 | ~9,200 ETB | **62% – 69%** | Severe urban traffic strikes & theft; 100% stockout |
| **3** | **BYD Seagull** | **Brake Pads (Front Ceramic Set)** | **80.7** | **High** | **Strong Recommendation** | 7,500 – 9,200 ETB | $12 – $16 | ~2,800 ETB | **63% – 70%** | Massive private commuter adoption; 28 workshop repairs |
| **4** | **Changan Benben E-Star** | **Shock Absorbers (Front Strut Pair)** | **80.3** | **High** | **Strong Recommendation** | 38,000 – 48,000 ETB | $45 – $65 | ~15,800 ETB | **58% – 67%** | Pothole/curb-weight hydraulic seal blowouts at 40k km |
| **5** | **BYD Seagull** | **Headlights (LED Projector Unit)** | **74.9** | **High** | **Strong Recommendation** | 46,500 – 52,000 ETB | $140 – $190 | ~25,500 ETB | **45% – 51%** | Sealed optical units; zero local floor inventory |

---

### Deep-Dive Analytical Profiles of the Top 5

#### 1. Changan Benben E-Star — Bumpers (Front Bumper Cover)
* **Operational Reality**: >2,000 active electric taxis in Addis Ababa. 19 workshop repair cases audited. **60% of damaged Benben taxi bumpers are temporarily patched with crude fiberglass** because zero replacement plastic bumper shells exist in Addis Ababa retail stock. Importers enforce 30–45 day sea-cargo order times.
* **Compatibility**: Verified OEM Part Number `Changan-2803100-W01`. Fits Changan Benben E-Star (2020–2024). Mounts to factory lower reinforcement bars without drilling.
* **Logistics & Margins**: Sourced from Chongqing at **$28–$45 USD/unit** (MOQ 20 units). Consolidating 100 units in a 20ft sea container via Port of Djibouti yields a landed cost of ~13,500 ETB against local retail prices of 31,000–38,000 ETB (**58%–64% gross margin**).

#### 2. BYD Yuan Up — Side Mirrors (Left / Right Power-Folding Mirror Assembly)
* **Operational Reality**: Frequent urban minibus traffic strikes and street theft. Integrated 360-degree cameras and blind-spot radar wiring make used ICE mirror retrofits impossible. 14 workshop replacements audited; **100% stockout rate across audited shops** with dealers quoting 14–21 day delays.
* **Compatibility**: Verified OEM Part Numbers `BYD-8202100-00` (Left) and `BYD-8202200-00` (Right).
* **Logistics & Margins**: Sourced from Shenzhen at **$42–$58 USD/unit** (MOQ 10 pairs). Compact package dimensions make this an **ideal air-cargo candidate** (Guangzhou to Bole ADD). Landed cost is ~9,200 ETB vs local retail of 24,000–29,500 ETB (**62%–69% gross margin**).

#### 3. BYD Seagull — Front Ceramic Brake Pads
* **Operational Reality**: Fastest-selling private EV (>15,000 units in Addis). 28 workshop repair replacements documented. Consumable anchor product with guaranteed continuous demand.
* **Compatibility**: Verified OEM Part Number `BYD-3501110-00`. Features cross-model interchangeability across BYD e-Platform 3.0 compact vehicles (shared caliper architecture with BYD Dolphin Front).
* **Logistics & Margins**: Sourced at **$12–$16 USD** (MOQ 50 sets). Directive 922/2022 duty exemption keeps landed cost below 2,800 ETB, yielding **63%–70% gross margin** at 7,500–9,200 ETB retail.

#### 4. Changan Benben E-Star — Front Shock Absorbers (Strut Damper Pair)
* **Operational Reality**: Heavy battery curb weight (1,180 kg) over rough asphalt/cobblestone roads causes hydraulic damper seals to rupture by 35,000–45,000 km (36 audited workshop blowouts). Standard ICE Benben dampers bottom out immediately; EV-specific reinforced damping valves are mandatory.
* **Compatibility**: Verified OEM Part Number `Changan-2905100-W01` (Front Left) and `Changan-2905200-W01` (Front Right).
* **Logistics & Margins**: Sourced from Chongqing at **$45–$65 USD/pair** via sea freight. Landed cost is ~15,800 ETB/pair, generating over 22,000 ETB gross profit per axle set at local retail (**58%–67% gross margin**).

#### 5. BYD Seagull — LED Projector Headlight Assemblies
* **Operational Reality**: Minor frontal collisions crack internal plastic alignment tabs or shatter outer polycarbonate lenses. Because the headlight is a sealed projector unit, repair shops cannot replace the lens alone; entire assemblies must be imported on 20–35 day lead times. Zero showroom stock held locally.
* **Compatibility**: Verified OEM Part Numbers `BYD-4121010-00` (Left) and `BYD-4121020-00` (Right). Full LED projector with integrated DRL.
* **Logistics & Margins**: Sourced from Changzhou at **$140–$190 USD/unit**. Landed cost is ~25,500 ETB, retailing locally at ~48,000 ETB (**45%–51% gross margin**).

---

## 5. Summary of All 30 Combinations & Quarantined Data Gaps

```text
Rank 01: Changan Benben E-Star  Bumpers                 [Score: 86.9 | Conf: High   | STRONG RECOMMENDATION]
Rank 02: BYD Yuan Up            Side Mirrors            [Score: 86.3 | Conf: High   | STRONG RECOMMENDATION]
Rank 03: BYD Seagull            Brake Pads              [Score: 80.7 | Conf: High   | STRONG RECOMMENDATION]
Rank 04: Changan Benben E-Star  Shock Absorbers         [Score: 80.3 | Conf: High   | STRONG RECOMMENDATION]
Rank 05: BYD Seagull            Headlights              [Score: 74.9 | Conf: High   | STRONG RECOMMENDATION]
Rank 06: BYD Seagull            Shock Absorbers         [Score: 74.1 | Conf: High   | Strong Opportunity]
Rank 07: Changan Benben E-Star  Wiper Blades            [Score: 72.5 | Conf: High   | Fast-Wear Consumable]
Rank 08: BYD Yuan Up            Brake Pads              [Score: 71.4 | Conf: High   | High Opportunity]
Rank 09: BYD Seagull            Fenders & Body Panels   [Score: 68.4 | Conf: Medium | Promising Lead]
Rank 10: BYD Yuan Up            Cabin-Air Filters       [Score: 66.8 | Conf: High   | High-Turnover Consumable]
Rank 11: BYD Seagull            Tail Lights             [Score: 65.7 | Conf: Medium | Collision Replacement]
Rank 12: BYD Seagull            Side Mirrors            [Score: 65.2 | Conf: Medium | Collision Replacement]
Rank 13: BYD Seagull            Bumpers                 [Score: 64.8 | Conf: Medium | Collision Replacement]
Rank 14: BYD Seagull            Wiper Blades            [Score: 64.2 | Conf: High   | Fast Consumable]
Rank 15: BYD Yuan Up            Headlights              [Score: 63.2 | Conf: Medium | High Value Collision]
Rank 16: BYD Seagull            Cabin-Air Filters       [Score: 62.9 | Conf: Medium | Fast Consumable]
Rank 17: BYD Yuan Up            Bumpers                 [Score: 62.6 | Conf: Medium | Collision Replacement]
Rank 18: Changan Benben E-Star  Brake Discs             [Score: 56.2 | Conf: High   | Medium Wear]
Rank 19: Changan Benben E-Star  Cabin-Air Filters       [Score: 48.2 | Conf: Medium | Maintenance Consumable]
Rank 20: Changan Benben E-Star  Brake Pads              [Score: 47.8 | Conf: Medium | Maintenance Consumable]
Rank 21: BYD Seagull            Brake Discs             [Score: 47.4 | Conf: Medium | Medium Wear]
Rank 22: Changan Benben E-Star  Side Mirrors            [Score: 47.1 | Conf: Medium | Collision Replacement]
Rank 23: Changan Benben E-Star  Headlights              [Score: 46.2 | Conf: Medium | Collision Replacement]
Rank 24: BYD Yuan Up            Shock Absorbers         [Score: 44.9 | Conf: Medium | Heavy Wear]
Rank 25: BYD Yuan Up            Brake Discs             [Score: 44.4 | Conf: Medium | Medium Wear]
Rank 26: BYD Yuan Up            Wiper Blades            [Score: 41.3 | Conf: Medium | Maintenance Consumable]
-- GAPS: BYD Yuan Up            Tail Lights             [Score:  N/A | Conf: Insufficient Evidence | Data Gap]
-- GAPS: BYD Yuan Up            Fenders & Body Panels   [Score:  N/A | Conf: Insufficient Evidence | Data Gap]
-- GAPS: Changan Benben E-Star  Tail Lights             [Score:  N/A | Conf: Insufficient Evidence | Data Gap]
-- GAPS: Changan Benben E-Star  Fenders & Body Panels   [Score:  N/A | Conf: Insufficient Evidence | Data Gap]
```

---

## 6. Full Deliverable Ledger & File Links

| Document / Code File | File Path | Description |
| :--- | :--- | :--- |
| **Comprehensive Final Report** | [`reports/final_recommendations.md`](./reports/final_recommendations.md) | Exhaustive 14 KB written report detailing the Top 5 recommendations, logistics, and counter-evidence. |
| **Evidence Gaps Audit** | [`reports/evidence_gaps_report.md`](./reports/evidence_gaps_report.md) | Full audit of unresearched components, anti-bot barriers, and broker distortion caveats. |
| **Master Colab Notebook** | [`notebooks/00_master_ev_parts_pipeline.ipynb`](./notebooks/00_master_ev_parts_pipeline.ipynb) | Single-click end-to-end executable notebook combining live car ranking and spare parts cleaning. |
| **Decision Priority Matrix** | [`data/processed/import_priority_scores.csv`](./data/processed/import_priority_scores.csv) | Machine-readable scores and ranks for all 30 combinations. |
| **30-Combination Summary** | [`data/processed/vehicle_part_summary.csv`](./data/processed/vehicle_part_summary.csv) | Aggregated empirical evidence counts across 29 variables. |
| **OEM Fitment Register** | [`data/processed/compatibility.csv`](./data/processed/compatibility.csv) | Verified manufacturer part numbers and platform interchangeability notes. |
| **Publication Figures** | [`reports/figures/`](./reports/figures/) | 6 high-resolution 300 DPI analytical figures (demand, scarcity, pricing, and heatmaps). |
