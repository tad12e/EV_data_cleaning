# Source Reliability & Evidence Quality Framework

**Project**: Ethiopian EV Spare-Parts Demand & Import Opportunity Research Pipeline  
**Module**: `choosing_spare_parts/`  
**Last Updated**: November 2026 (Task 2 Complete)  

---

## 1. The 0–10 Reliability Scoring Scale

Every collected evidence record is evaluated across an objective 0–10 composite scale:

| Score Range | Classification | Meaning | Evidence Handling |
| :---: | :--- | :--- | :--- |
| **9.0 – 10.0** | **Definitive / High Confidence** | Strong, direct, recent (<60 days), vehicle-specific, and independently corroborated evidence (e.g., official OEM distributor warranty bulletin, verified customs declaration, physical invoice). | Direct inclusion in primary scoring without discount. |
| **7.0 – 8.9** | **Reliable** | Clear details from a known commercial source (licensed importer, operational garage), but with minor verification gaps (e.g., active classified listing with confirmed seller phone number and price). | Weighted at full value for market presence; corroborated with secondary sources. |
| **5.0 – 6.9** | **Moderate Uncertainty** | Relevant evidence with moderate ambiguity (e.g., social media comment stating part was unavailable, dealer post without itemized SKU, or inquiry older than 180 days). | Included with uncertainty dampener; requires secondary verification flag. |
| **3.0 – 4.9** | **Weak / Indirect** | Indirect, outdated (>365 days), or incomplete evidence (e.g., generic advertisement stating "all EV parts available", unconfirmed broker repost). | Discounted heavily; cannot alone justify an import recommendation. |
| **1.0 – 2.9** | **Very Uncertain / Ambiguous** | Highly speculative claims, anonymous social comments with unclear vehicle fitment, or broken/unverified platforms. | Flagged for manual review; excluded from quantitative demand scoring. |
| **0.0** | **Invalid / Rejected** | Fabricated, duplicate, completely irrelevant, or demonstrably incorrect technical claims. | Logged in raw audit trail; dropped from cleaned dataset. |

---

## 2. Six-Dimensional Evidence Evaluation Matrix

The composite reliability score is calculated as:

$$\text{Reliability Score} = 0.25(C) + 0.25(S) + 0.20(F) + 0.15(D) + 0.10(V) + 0.05(E)$$

Where:
1. **$C$ (Source Credibility, 25%)**:
   * *10.0*: Official Government Ministry, Customs Commission, OEM Manufacturer.
   * *8.0*: Licensed Ethiopian EV Distributor (MOENCO, Kairos, Evtopia) or verified assembly plant (BKME).
   * *6.0*: Established automotive showroom or operational workshop (Girar, Berhanu Al-Adem).
   * *4.0*: Independent classified seller or marketplace broker.
   * *2.0*: Anonymous social media user or untraceable forum post.
2. **$S$ (Evidence Specificity, 25%)**:
   * *10.0*: Explicitly states exact vehicle model, trim, model year, part category, component position (L/R), and OEM part number.
   * *7.5*: Explicitly states exact vehicle model, part category, and price in ETB, but lacks OEM part number.
   * *5.0*: Mentions vehicle brand and generic category (e.g., "BYD brake pads") without model differentiation.
   * *2.5*: Generic automotive claim (e.g., "EV parts available in Addis").
3. **$F$ (Freshness / Time Decay, 20%)**:
   * *10.0*: $\le 30$ days old (Active current quarter).
   * *8.0*: $31 - 90$ days old.
   * *6.0*: $91 - 180$ days old.
   * *4.0*: $181 - 365$ days old.
   * *2.0*: $> 365$ days old.
   * *0.0*: Undated historical post with no activity for $> 2$ years.
4. **$D$ (Directness of Observation, 15%)**:
   * *10.0*: First-hand physical stock verification, confirmed transaction receipt, or technician repair log.
   * *7.5*: Direct seller quotation or active showroom advertisement with contact number.
   * *5.0*: Customer enquiry or complaint reporting part search or unavailability.
   * *2.5*: General discussion, promotional promise to import, or secondhand commentary.
5. **$V$ (Independent Corroboration / Verification, 10%)**:
   * *10.0*: Corroborated across two or more independent platforms (e.g., Telegram post + physical showroom audit).
   * *5.0*: Single independent source with verified contact phone number.
   * *0.0*: Isolated single-instance claim with no corroboration.
6. **$E$ (Extraction Quality, 5%)**:
   * *10.0*: Clean structured data extracted with high parser confidence.
   * *5.0*: Unstructured text parsed via NLP/regex with minor ambiguities.
   * *1.0*: Scraper parsing warning or OCR uncertainty.

---

## 3. Explicit Deductions & Penalty Rules

| Condition | Penalty Deduction | Rationale |
| :--- | :---: | :--- |
| **Broken / Inaccessible Website** | **-3.0** | Source cannot be independently verified via live web fetch. |
| **Outdated Information (> 1 Year)** | **-2.5** | Fast-changing EV regulatory and market dynamics render old prices obsolete. |
| **Broker Repost / Duplicate Ad** | **-2.0** | Inflates volume artificially without representing unique physical inventory. |
| **Ambiguous Part Classification** | **-2.0** | Uncertainty regarding whether component fits target model. |
| **Unresponsive Phone / Defunct Channel** | **-3.0** | Seller cannot be reached to confirm stock. |
