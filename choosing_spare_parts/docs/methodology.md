# Research Methodology Specification

**Project**: Ethiopian EV Spare-Parts Demand & Import Opportunity Research Pipeline  
**Module**: `choosing_spare_parts/`  
**Last Updated**: November 2026 (Task 2 Architecture Complete)  

---

## 1. Research Lifecycle & Pipeline Workflow

```
[Phase 1: Source Discovery & Audit]
       │ (docs/source_register.csv — 61 Audited Sources)
       ▼
[Phase 2: Multi-Platform Ingestion]
       │ (config/search_queries.yaml — 30 Vehicle-Part Combinations)
       ├─► Telegram MTProto (Apify)
       ├─► Web Classifieds (Requests / BeautifulSoup)
       ├─► TikTok Video & Comments (Apify)
       ├─► Manual Dealership & Workshop Logs
       ▼
[Phase 3: Raw Evidence Preservation]
       │ (data/raw/* — Immutable Raw CSV Tables)
       ▼
[Phase 4: Cleaning, Classification & Deduplication]
       │ (Notebook 02 — Normalization, Alias Resolution, De-duping)
       ▼
[Phase 5: Analytical Evaluation]
       │ (Notebooks 03 & 04 — Demand/Supply & Compatibility/Sourcing)
       ▼
[Phase 6: Multi-Criteria Decision Scoring]
       │ (Notebook 05 — Import Priority Scores & Decoupled Confidence)
       ▼
[Phase 7: Actionable Importer Recommendations]
       │ (reports/final_recommendations.md)
```

---

## 2. Source Discovery & Validation Protocol
Before scraping, each potential evidence provider undergoes a 6-step audit:
1. **Existence Check**: Confirm domain DNS resolution, channel availability, and verified presence in Addis Ababa.
2. **Access Testing**: Determine whether automated fetch is blocked (e.g., HTTP 403 anti-bot gates), restricted, or fully open.
3. **Relevance Screening**: Confirm actual presence of passenger EV components or target models (excluding industrial conversion kits).
4. **Freshness Assessment**: Record latest post/listing date; flag content older than 180 days with a time-decay penalty.
5. **Collection Feasibility**: Establish whether extraction proceeds via automated API, scraper, headless browser, or manual phone inquiry.
6. **Decision Recording**: Classify into `Use` (45 sources), `Investigate` (13 sources), or `Skip` (3 sources).

---

## 3. Vehicle & Part Matching Protocol
* Vehicle identification applies strict alias resolution using `config/vehicle_aliases.yaml`. Similar models (e.g., BYD Dolphin vs. BYD Seagull; BYD Yuan Plus vs. BYD Yuan Up) are **strictly isolated to prevent cross-model contamination**.
* Part identification maps colloquial, multilingual, and misspelled strings into the **10 Standard Categories** using `config/part_aliases.yaml`. Ambiguous terms (e.g., generic "filter" or "lights") are flagged for manual review rather than guessed.

---

## 4. Evidence Direction & Classification Taxonomy
Every raw record is categorized into a standard evidence direction:
* **Demand Signals**: `customer_request`, `price_enquiry`, `availability_enquiry`, `purchase_report`, `repair_case`. *(Advertisements are explicitly never counted as demand).*
* **Supply Signals**: `stock_confirmation`, `stock_unavailable`, `orderable_by_supplier`, `supplier_quote`, `product_listing`.
* **Technical / Macro Signals**: `oem_catalogue`, `compatibility_evidence`, `import_evidence`, `technician_observation`.

---

## 5. Deduplication & Data Integrity
Deduplication handles cross-posting across Ethiopian automotive channels:
1. Group records by exact URL, phone number, vehicle model, part category, and normalized price.
2. Assign a unique `duplicate_group_id`.
3. Retain the earliest published ad as primary (`is_duplicate = False`); mark subsequent reposts as secondary (`is_duplicate = True`).
4. **Preserve All Raw Records**: Duplicates are never permanently deleted from raw datasets; they are flagged in `cleaned_evidence.csv` to keep the audit trail complete.
