# Master Data Dictionary — Ethiopian EV Spare-Parts Research Pipeline

**Project**: Ethiopian EV Spare-Parts Demand & Import Opportunity Research Pipeline  
**Module**: `choosing_spare_parts/`  
**Last Updated**: November 2026 (Task 2 Architecture Complete)  

---

## 1. Architectural Overview & Schema Standards

The data pipeline separates data into three distinct tiers:
1. **Raw Tier (`data/raw/`)**: Immutable, raw extracted records preserving original source payloads, URLs, and unedited descriptions.
2. **Processed Tier (`data/processed/`)**: Normalized, cleaned, classified, deduplicated, and scored decision tables.
3. **Reference Tier (`data/reference/`)**: Ground-truth taxonomies, manufacturer OEM numbers, and model/part alias mappings.

### Global Missing Value Policy
* Numeric fields with no verifiable local data are filled with `NaN` / empty in raw records, and explicitly evaluated as `0` or flagged as `insufficient_evidence` in analytical summaries. **No numbers, prices, or counts are fabricated.**
* Textual fields where data was unstated in the source are coded as `Unstated` or `None`.
* Absence of listings is never interpreted as proof of zero demand; it is flagged with `data_gaps: Insufficient local listing evidence`.

---

## 2. Raw Datasets Tier (`data/raw/`)

### A. Marketplace Product Listings (`data/raw/marketplaces/raw_marketplace_listings.csv`)
*Primary sources: Jiji Ethiopia, AfroMekina, Mekina.net, EthioDrive, CarGebeya, Adey Market.*

| Column | Type | Req/Opt | Description | Missing Value Rule |
| :--- | :---: | :---: | :--- | :--- |
| `raw_record_id` | String | Req | Unique surrogate key (`MKT-YYYYMMDD-XXXX`). | Mandatory |
| `platform` | String | Req | Origin marketplace name (e.g., `Jiji Ethiopia`). | Mandatory |
| `listing_id` | String | Opt | Native platform listing ID (e.g., `JIJI-81924`). | Empty if unavailable |
| `listing_url` | String | Req | Full, clickable URL to the individual listing. | Mandatory |
| `listing_title` | String | Req | Verbatim headline of the advertisement. | Mandatory |
| `original_description` | String | Opt | Full unedited text body of the classified ad. | Empty if unstated |
| `seller_name` | String | Opt | Displayed seller/business name. | `Unknown Seller` |
| `seller_id_if_public` | String | Opt | Public seller ID or profile handle. | Empty if unavailable |
| `advertised_price` | Float | Opt | Asking price numeric value. | `NaN` if unpriced |
| `currency` | String | Opt | Currency code (primarily `ETB`, occasionally `USD`). | `ETB` default |
| `location` | String | Opt | Stated location (e.g., `Addis Ababa, Bole`). | `Addis Ababa` default |
| `vehicle_model_mentioned` | String | Opt | Raw vehicle string extracted from text. | `Unspecified` |
| `part_mentioned` | String | Opt | Raw spare-part name extracted from text. | `Unspecified` |
| `stock_claim` | String | Opt | Claimed availability (`In Stock`, `Pre-order`, `By Order`). | `Unstated` |
| `published_date` | Date | Opt | Original post date in ISO 8601 (`YYYY-MM-DD`). | `Undated` |
| `scraped_date` | Date | Req | Date crawled/extracted (`YYYY-MM-DD`). | Mandatory |
| `listing_status` | String | Req | Status at collection (`Active`, `Sold`, `Expired`). | Mandatory |
| `image_urls` | String | Opt | Semicolon-separated image links. | Empty if none |
| `raw_payload_reference` | String | Opt | Link to raw JSON payload log. | Empty |
| `collection_method` | String | Req | Extraction mode (`Automated Scraper`, `Headless Browser`, `Manual`). | Mandatory |

---

### B. Vehicle Market Presence Listings (`data/raw/vehicle_listings/raw_vehicle_listings.csv`)
*Primary sources: AfroMekina, Mekina.net, EthioDrive, CarGebeya, Zemen Motors.*

| Column | Type | Req/Opt | Description | Missing Value Rule |
| :--- | :---: | :---: | :--- | :--- |
| `raw_record_id` | String | Req | Unique key (`VEH-YYYYMMDD-XXXX`). | Mandatory |
| `platform` | String | Req | Platform name. | Mandatory |
| `listing_id` | String | Opt | Platform listing ID. | Empty |
| `listing_url` | String | Req | Direct post URL. | Mandatory |
| `listing_title` | String | Req | Headline of vehicle ad. | Mandatory |
| `original_description` | String | Opt | Unedited post text. | Empty |
| `seller_name` | String | Opt | Dealership or broker name. | `Unknown` |
| `seller_type` | String | Opt | Category (`Authorized Dealer`, `Showroom`, `Broker`, `Private`). | `Broker` default |
| `advertised_price` | Float | Req | Asking price in ETB. | Mandatory |
| `currency` | String | Req | `ETB`. | Mandatory |
| `location` | String | Opt | Addis Ababa neighborhood. | `Addis Ababa` |
| `vehicle_model_mentioned` | String | Req | Target vehicle detected (`BYD Seagull`, `BYD Yuan Up`, `Changan Benben E-Star`). | Mandatory |
| `model_year` | Integer | Opt | Stated vehicle model year (e.g., `2024`). | `NaN` |
| `mileage_km` | Integer | Opt | Odometer reading in km (0 for brand new). | `0` if Brand New |
| `published_date` | Date | Opt | Publication date (`YYYY-MM-DD`). | `Undated` |
| `scraped_date` | Date | Req | Extraction date (`YYYY-MM-DD`). | Mandatory |
| `listing_status` | String | Req | Listing status. | Mandatory |
| `post_link` | String | Req | Direct URL. | Mandatory |
| `contact_info` | String | Opt | Phone contact (+251...). | Empty |
| `collection_method` | String | Req | Scraper method. | Mandatory |

---

### C. Social Media Posts & Videos (`data/raw/social_media/raw_social_posts.csv`)
*Primary sources: TikTok video topics (`#EthiopiaEV`, `#BYDEthiopia`), dealership accounts (`@evtopia.et`, `@zemenmotors`).*

| Column | Type | Req/Opt | Description |
| :--- | :---: | :---: | :--- |
| `raw_record_id` | String | Req | Unique key (`SOC-POST-XXXX`). |
| `platform` | String | Req | `TikTok`, `Facebook`, or `Instagram`. |
| `account_name` | String | Req | Account handle (e.g., `@zemenmotors`). |
| `post_id` | String | Opt | Unique video ID from TikTok/platform. |
| `post_url` | String | Req | Direct video link (`https://www.tiktok.com/@.../video/...`). |
| `original_caption` | String | Opt | Full video caption and hashtags. |
| `video_or_image_url` | String | Opt | Direct media asset URL. |
| `published_date` | Date | Opt | Video upload timestamp (`YYYY-MM-DD`). |
| `scraped_date` | Date | Req | Collection timestamp. |
| `views` | Integer | Opt | Total video views at extraction. |
| `likes` | Integer | Opt | Total likes. |
| `shares` | Integer | Opt | Total shares. |
| `comments_count` | Integer | Opt | Total public comments recorded. |
| `vehicle_mentioned` | String | Opt | Vehicle detected in caption or tags. |
| `part_mentioned` | String | Opt | Spare part detected in caption or audio tags. |
| `original_payload_reference` | String | Opt | Raw Apify JSON log reference. |

---

### D. Social Media Public Comments (`data/raw/social_media/raw_social_comments.csv`)
*Primary sources: Apify TikTok Scraper public comments feed.*

| Column | Type | Req/Opt | Description |
| :--- | :---: | :---: | :--- |
| `raw_record_id` | String | Req | Unique key (`SOC-COMM-XXXX`). |
| `platform` | String | Req | `TikTok` / `Facebook`. |
| `post_id` | String | Req | Parent video/post ID. |
| `post_url` | String | Req | Parent post URL. |
| `comment_id` | String | Opt | Anonymous comment identifier (No PII stored). |
| `original_comment_text` | String | Req | Exact text of the public enquiry or comment. |
| `comment_date` | Date | Opt | Timestamp of comment. |
| `scraped_date` | Date | Req | Extraction date. |
| `reply_count_if_available` | Integer | Opt | Number of replies to comment. |
| `engagement_if_available` | Integer | Opt | Likes on comment. |
| `classification_status` | String | Req | `pending`, `customer_request`, `price_enquiry`, `unrelated`. |
| `original_payload_reference` | String | Opt | Raw JSON reference. |

---

### E. Telegram Posts & Channel Broadcasts (`data/raw/telegram/raw_telegram_posts.csv`)
*Primary sources: `@zemenmotors`, `@Abyssiniancarsales`, `@smartcarmarket`, `@capitalcarmarket`, `@ethiocardealers`, `@ev_ethiopia`.*

| Column | Type | Req/Opt | Description |
| :--- | :---: | :---: | :--- |
| `raw_record_id` | String | Req | Unique key (`TG-YYYYMMDD-XXXX`). |
| `channel_or_group` | String | Req | Channel handle (e.g., `@zemenmotors`). |
| `channel_id` | String | Opt | Telegram native channel ID. |
| `message_id` | Integer | Req | Message ID integer (e.g., `1428`). |
| `message_url` | String | Req | Clickable post URL (`https://t.me/zemenmotors/1428`). |
| `original_text` | String | Req | Full unedited message text. |
| `media_type` | String | Opt | `photo`, `video`, `document`, `text_only`. |
| `media_reference` | String | Opt | Internal Telegram media ID. |
| `published_date` | Date | Opt | Date message was posted (`YYYY-MM-DD`). |
| `scraped_date` | Date | Req | Date scraped (`YYYY-MM-DD`). |
| `vehicle_mentioned` | String | Opt | Target vehicle detected. |
| `part_mentioned` | String | Opt | Spare part detected. |
| `original_payload_reference` | String | Opt | Apify dataset ID. |

---

### F. Supplier Evidence & Quotations (`data/raw/suppliers/raw_supplier_evidence.csv`)
*Primary sources: Sunny Spare Parts, Yami Cars, MOENCO, Markon, SARA, Yemareyam, Evtopia.*

| Column | Type | Req/Opt | Description |
| :--- | :---: | :---: | :--- |
| `raw_record_id` | String | Req | Unique key (`SUP-YYYYMMDD-XXXX`). |
| `supplier_name` | String | Req | Business name. |
| `supplier_type` | String | Req | `Official Distributor`, `Independent Importer`, `Wholesaler`, `Broker`. |
| `supplier_location` | String | Opt | Showroom or office address. |
| `supplier_url` | String | Opt | Website or channel URL. |
| `vehicle_model` | String | Req | Standardized vehicle name. |
| `part_category` | String | Req | One of the 10 standard categories. |
| `component` | String | Req | Specific component name (e.g. `Front Brake Pads`). |
| `oem_part_number` | String | Opt | Stated OEM part number. |
| `advertised_price` | Float | Opt | Quoted price in ETB or USD. |
| `currency` | String | Opt | `ETB` / `USD`. |
| `stock_status` | String | Req | `Physical Stock`, `In Transit`, `Orderable (2-4 wks)`, `Unavailable`. |
| `availability_claim` | String | Opt | Exact claim made by supplier. |
| `orderable_status` | String | Opt | `Orderable` / `Not Orderable`. |
| `country_of_origin` | String | Opt | Country where part is sourced (e.g., `China`). |
| `import_claim` | String | Opt | Air freight / sea container claim. |
| `quote_date` | Date | Opt | Date quotation was obtained. |
| `observation_date` | Date | Req | Date recorded. |
| `evidence_url` | String | Opt | Document or post URL. |
| `original_text` | String | Opt | Quoted text or notes. |
| `verification_status` | String | Req | `Verified Physical Stock`, `Verified Quote`, `Unconfirmed Claim`. |

---

### G. Workshop & Repair Evidence (`data/raw/workshops/raw_repair_evidence.csv`)
*Primary sources: Berhanu Al-Adem, Girar EV Garage, Dehab Motors, BKME Kaliti, EV Master.*

| Column | Type | Req/Opt | Description |
| :--- | :---: | :---: | :--- |
| `raw_record_id` | String | Req | Unique key (`REP-YYYYMMDD-XXXX`). |
| `workshop_name_or_anonymous_id` | String | Req | Workshop name or anonymous ID. |
| `workshop_location` | String | Opt | Addis Ababa neighborhood. |
| `vehicle_model` | String | Req | Vehicle model serviced. |
| `model_year_if_known` | Integer | Opt | Vehicle model year. |
| `part_category` | String | Req | One of the 10 standard categories. |
| `specific_component` | String | Req | Specific component replaced or repaired. |
| `repair_type` | String | Req | `Periodic Replacement`, `Collision Repair`, `Suspension Overhaul`. |
| `replacement_or_repair` | String | Req | `Replacement` vs `Repaired/Refurbished`. |
| `quantity` | Integer | Opt | Number of units replaced. |
| `observation_period` | String | Opt | Reporting timeframe (e.g., `Last 6 Months`). |
| `repair_date` | Date | Opt | Date repair occurred. |
| `technician_statement` | String | Opt | Direct quotation or summary of technician's observation. |
| `evidence_url` | String | Opt | Source link. |
| `collection_date` | Date | Req | Date recorded. |
| `verification_status` | String | Req | `Technician Statement`, `Invoice Observed`, `Workshop Observation`. |

---

### H. Customer Enquiries & Demand Signals (`data/raw/customer_enquiries/raw_customer_enquiries.csv`)
*Primary sources: Telegram EV Community (`@ev_ethiopia`), TikTok video comments, Facebook EV groups.*

| Column | Type | Req/Opt | Description |
| :--- | :---: | :---: | :--- |
| `raw_record_id` | String | Req | Unique key (`ENQ-YYYYMMDD-XXXX`). |
| `platform` | String | Req | Origin platform (`Telegram`, `TikTok`, `Facebook`). |
| `source_name` | String | Req | Channel or group name. |
| `source_url` | String | Req | Direct message or post link. |
| `enquiry_date` | Date | Opt | Date customer posted inquiry. |
| `vehicle_model` | String | Req | Vehicle model specified by user. |
| `part_category` | String | Req | Target part category. |
| `enquiry_type` | String | Req | `Availability Enquiry`, `Price Enquiry`, `Where to Buy`, `Repair Complaint`. |
| `original_text` | String | Req | Unedited inquiry text. |
| `price_enquiry` | Boolean | Req | `True` if user asks for price. |
| `availability_enquiry` | Boolean | Req | `True` if user asks where to find in stock. |
| `purchase_report` | Boolean | Req | `True` if user reports successful purchase. |
| `urgency` | String | Opt | `High (Vehicle Down)`, `Medium`, `Routine`. |
| `response_or_resolution` | String | Opt | Whether seller or community responded with stock. |
| `collection_date` | Date | Req | Date recorded. |

---

### I. Import, Export & Trade Statistics (`data/raw/trade/raw_trade_statistics.csv`)
*Primary sources: UN Comtrade, Ethiopian Customs Commission, Ethiopian Statistical Service.*

| Column | Type | Req/Opt | Description |
| :--- | :---: | :---: | :--- |
| `raw_record_id` | String | Req | Unique key (`TRD-YYYY-XXXX`). |
| `source` | String | Req | `UN Comtrade`, `ECC`, `ESS`. |
| `source_url` | String | Req | Direct URL. |
| `country` | String | Req | `Ethiopia`. |
| `reporting_year` | Integer | Req | Year (e.g., `2024`, `2025`). |
| `commodity_code` | String | Req | HS Code (e.g., `8708.30`, `8708.80`, `8708.29`). |
| `commodity_description` | String | Req | Official HS commodity title. |
| `import_or_export` | String | Req | `Import`. |
| `partner_country` | String | Req | `China`, `United Arab Emirates`, `World`. |
| `trade_quantity` | Float | Opt | Metric units or kilograms imported. |
| `quantity_unit` | String | Opt | `kg`, `units`, `number of items`. |
| `trade_value` | Float | Req | Stated value (CIF USD or ETB). |
| `currency` | String | Req | `USD` / `ETB`. |
| `collection_date` | Date | Req | Extraction date. |
| `notes` | String | Opt | Notes on aggregation level. |
| `specificity_level` | String | Req | `Broad HS Category (Not Model Specific)` vs `Model Specific`. |

---

## 3. Processed Datasets Tier (`data/processed/`)

### A. Cleaned Evidence Master Table (`data/processed/cleaned_evidence.csv`)
*Consolidates all verified, deduplicated evidence records linking vehicle and part.*

| Column | Type | Foreign Key / Constraint | Description |
| :--- | :---: | :--- | :--- |
| `evidence_id` | String | Unique Primary Key (`EVD-XXXXXX`) | Master record identifier. |
| `raw_record_id` | String | FK $\rightarrow$ `data/raw/*` | Traceability link to original raw record. |
| `source_dataset` | String | Dataset name | `marketplaces`, `telegram`, `suppliers`, etc. |
| `vehicle_model` | String | Constrained (`BYD Seagull`, `BYD Yuan Up`, `Changan Benben E-Star`) | Standardized vehicle model. |
| `part_category` | String | Constrained (1 of 10 categories) | Standardized part category. |
| `specific_component` | String | Free string | Specific component (e.g., `Front MacPherson Strut`). |
| `component_position` | String | `Front`, `Rear`, `Left`, `Right`, `Universal` | Physical mounting position. |
| `evidence_type` | String | Standard taxonomy | `customer_request`, `stock_confirmation`, `repair_case`, etc. |
| `evidence_direction` | String | `Demand`, `Supply`, `Neutral` | Analytical direction of evidence. |
| `source_category` | String | Category | E.g., `Official Distributor`, `Social Media`. |
| `source_name` | String | Name | Business or channel name. |
| `source_url` | String | Clickable URL | Source link. |
| `observation` | String | Summary | Factual observation summary. |
| `price` | Float | Numeric | Normalized price in ETB. |
| `currency` | String | `ETB` | Currency code. |
| `stock_status` | String | Taxonomy | `Confirmed Available`, `Unavailable`, `By Order`, `Unstated`. |
| `oem_part_number` | String | Opt | Verified OEM part number if stated. |
| `compatibility_status` | String | Taxonomy | `Verified OEM Fitment`, `Interchangeable`, `Unverified`. |
| `published_date` | Date | ISO 8601 | Publication timestamp. |
| `collection_date` | Date | ISO 8601 | Extraction timestamp. |
| `freshness_score` | Float | 0.0 - 10.0 | Calculated time-decay score. |
| `source_credibility_score` | Float | 0.0 - 10.0 | Source authority score. |
| `specificity_score` | Float | 0.0 - 10.0 | Model & part detail precision score. |
| `verification_score` | Float | 0.0 - 10.0 | Independent corroboration score. |
| `extraction_quality_score` | Float | 0.0 - 10.0 | Scraper parsing fidelity score. |
| `reliability_score` | Float | 0.0 - 10.0 | Composite weighted evidence reliability. |
| `duplicate_group_id` | String | FK $\rightarrow$ Deduplication group | Grouping ID for cross-posted advertisements. |
| `is_duplicate` | Boolean | `True` / `False` | Retained primary vs secondary repost flag. |
| `manual_review_required` | Boolean | `True` / `False` | Flag for ambiguous classification. |
| `confidence_notes` | String | Text | Audit explanation for assigned scores. |
| `limitations` | String | Text | Explicit limitations of this evidence point. |

---

### B. Summary & Scoring Matrices
* `data/processed/vehicle_part_summary.csv`: Aggregates the **30 vehicle–part combinations** across demand, supply, price, and reliability metrics.
* `data/processed/import_priority_scores.csv`: Decision matrix combining **Demand (30%)**, **Scarcity (25%)**, **Compatibility (20%)**, **Sourcing Feasibility (15%)**, and **Reliability (10%)** into total import priority ranks with decoupled **Confidence Levels** (`high`, `medium`, `low`, `insufficient_evidence`).
