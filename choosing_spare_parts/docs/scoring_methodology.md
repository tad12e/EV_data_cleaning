# Import Priority Scoring & Evidence Confidence Methodology

**Project**: Ethiopian EV Spare-Parts Demand & Import Opportunity Research Pipeline  
**Module**: `choosing_spare_parts/`  
**Last Updated**: November 2026 (Task 2 Complete)  

---

## 1. Executive Scoring Model

The **Import Priority Score (0–100)** determines which vehicle-specific spare parts an Ethiopian importer should prioritize ordering, stocking, and distributing. It synthesizes five evidence-based pillars:

$$\text{Total Priority Score} = 0.30(D) + 0.25(S) + 0.20(C) + 0.15(F) + 0.10(R)$$

| Criterion | Weight | Definition & Evidence Base |
| :--- | :---: | :--- |
| **Customer Demand ($D$)** | **30%** | Frequency of customer requests, price enquiries, availability questions, repair cases, and active vehicle fleet presence. *(Advertisements are explicitly excluded from demand).* |
| **Local Scarcity ($S$)** | **25%** | Absence of verified local floor stock, frequency of unavailable reports, lead times exceeding 30 days, and price markups over international FOB. |
| **Compatibility Confidence ($C$)** | **20%** | Verification of OEM part numbers, inter-model platform interchangeability (e.g. e-Platform 3.0), and model-year/trim fitment certainty. |
| **Sourcing Feasibility ($F$)** | **15%** | Availability of verified tier-1 Chinese manufacturers, unit FOB pricing, packaging weight/dimensions, and air/sea container logistics feasibility via Djibouti. |
| **Evidence Reliability ($R$)** | **10%** | The mean data quality, source credibility, and freshness of the underlying evidence records. |
| **Total** | **100%** | **Composite Import Priority Index** |

---

## 2. Decoupled Evidence Confidence Classification

Import Priority must **never be confused with Evidence Confidence**. 
* A part may have **High Priority** (estimated large demand/shortage) but **Low Confidence** (based on informal social complaints or hearsay).
* A part may have **Low Priority** (readily available locally) but **High Confidence** (verified by multiple dealership catalogues).

Every combination is assigned one of four distinct Confidence Levels:

| Confidence Level | Minimum Requirements | Strategic Implication for Importer |
| :---: | :--- | :--- |
| **High** | $\ge 5$ verified independent records, verified OEM part number, corroborated local pricing, and active distributor verification. | **Actionable Opportunity**: Importer can proceed with quotation and stocking decisions with high certainty. |
| **Medium** | $2 - 4$ relevant records, clear model/part identification, but missing physical distributor stock audit or exact OEM cross-reference. | **Promising Lead**: Requires phone confirmation of local stock and overseas supplier MOQ before capital allocation. |
| **Low** | $1$ isolated record or indirect evidence (e.g., general discussion, unverified broker post). | **High Speculative Risk**: Do not invest capital without primary physical inspection. |
| **Insufficient Evidence** | $0$ verified local records. | **Data Gap**: Explicitly flagged as unresearched or absent in local digital footprint; **never scored as zero demand**. |

---

## 3. Mathematical Metric Formulations

### A. Demand Score ($D$, 0–100)
$$D = \min\left(100, \; 15 \times N_{\text{requests}} + 10 \times N_{\text{repairs}} + 5 \times N_{\text{enquiries}} + 0.5 \times \text{Fleet Presence Index}\right)$$

### B. Scarcity Score ($S$, 0–100)
$$S = \min\left(100, \; 20 \times N_{\text{unavailable}} + 15 \times N_{\text{pre-order}} + \left[1 - \frac{N_{\text{stock confirmed}}}{N_{\text{total enquiries}} + 1}\right] \times 50\right)$$
*(Note: If a part has 0 verified physical floor stock across all audited Addis Ababa showrooms, scarcity is scored $\ge 80$).*

### C. Compatibility Score ($C$, 0–100)
* **100.0**: Verified OEM part number from official manufacturer EPC with cross-model interchangeability confirmed.
* **80.0**: Verified OEM part number, single-model fitment confirmed.
* **60.0**: Aftermarket fitment listed by tier-1 supplier (e.g. Bosch, TRW) without official OEM stamping.
* **30.0**: Dimensions known, but physical mounting points unverified.
* **0.0**: Unverified fitment.

### D. Sourcing Feasibility ($F$, 0–100)
$$F = 0.40(\text{Supplier Availability}) + 0.30(\text{Price Affordability Index}) + 0.30(\text{Shipping Feasibility})$$
* Fast-moving lightweight wear items (cabin filters, wiper blades, brake pads) score higher on shipping feasibility than heavy stamped panels or fragile glass.

---

## 4. Missing Data & Zero-Score Policy
1. When zero records are found for a vehicle-part combination, it is assigned `Priority: Pending Further Research` and `Confidence: Insufficient Evidence`.
2. It is **never given a 0 priority score interpreted as "customers do not need this part"**.
3. It is entered into `data/processed/evidence_gaps.csv` for targeted manual investigation.
