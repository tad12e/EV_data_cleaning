# Uncertain & Unclassified Evidence Audit Report — Task 6

**Audit Date**: 2026-11-18  
**Total Records Flagged for Review**: 158 (60.3% of corpus)  

---

## 1. Summary of Review Triggers

Records are flagged for manual review when:
1. Vehicle model could not be differentiated beyond generic brand (e.g. "BYD EV" without Seagull/Yuan Up distinction).
2. Part terminology was colloquial or ambiguous (e.g. general "accessory" or multi-part lot).
3. Price was an outlier or outside expected component envelopes.

---

## 2. Inventory of Flagged Records

| Evidence ID | Raw Record ID | Source Dataset | Vehicle Model | Part Category | Validation Warnings |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `EVD-00001` | `MKT-20261118-0001` | marketplaces | BYD (Unspecified Model) | generic_spare_part | unrecognized_part_category |
| `EVD-00002` | `MKT-20261118-0002` | marketplaces | BYD (Unspecified Model) | generic_spare_part | unrecognized_part_category |
| `EVD-00003` | `MKT-20261118-0003` | marketplaces | BYD (Unspecified Model) | generic_spare_part | unrecognized_part_category |
| `EVD-00004` | `MKT-20261118-0004` | marketplaces | BYD Seagull | generic_spare_part | unrecognized_part_category |
| `EVD-00005` | `MKT-20261118-0005` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00006` | `MKT-20261118-0006` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00007` | `MKT-20261118-0007` | marketplaces | Cross-Model EV / Unspecified | brake_discs | price_outlier_high_650000.0_for_brake_discs |
| `EVD-00009` | `MKT-20261118-0009` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00010` | `MKT-20261118-0010` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00011` | `MKT-20261118-0011` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00012` | `MKT-20261118-0012` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00013` | `MKT-20261118-0013` | marketplaces | BYD (Unspecified Model) | generic_spare_part | unrecognized_part_category |
| `EVD-00014` | `MKT-20261118-0014` | marketplaces | Cross-Model EV / Unspecified | side_mirrors | price_outlier_high_3790000.0_for_side_mirrors |
| `EVD-00015` | `MKT-20261118-0015` | marketplaces | Cross-Model EV / Unspecified | brake_discs | price_outlier_high_4500000.0_for_brake_discs |
| `EVD-00016` | `MKT-20261118-0016` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00017` | `MKT-20261118-0017` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00018` | `MKT-20261118-0018` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00019` | `MKT-20261118-0019` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00020` | `MKT-20261118-0020` | marketplaces | BYD (Unspecified Model) | generic_spare_part | unrecognized_part_category |
| `EVD-00021` | `MKT-20261118-0021` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00022` | `MKT-20261118-0022` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00023` | `MKT-20261118-0023` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00025` | `MKT-20261118-0025` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00026` | `MKT-20261118-0026` | marketplaces | Cross-Model EV / Unspecified | generic_spare_part | unrecognized_part_category |
| `EVD-00027` | `MKT-20261118-0027` | marketplaces | BYD Seagull | generic_spare_part | unrecognized_part_category |

---

## 3. Recommended Resolution Protocol

- For quantitative demand and priority ranking (Tasks 7–9), flagged records are retained with an **uncertainty dampener** (lower reliability score).
- They provide secondary directional corroboration but cannot single-handedly drive an import recommendation.
