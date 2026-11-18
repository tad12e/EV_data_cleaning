# Task 4 Deliverable Summary — Telegram, TikTok & Customer Demand Evidence

**Module**: `choosing_spare_parts/`  
**Execution Date**: 2026-11-18  
**Pipeline Orchestrator**: `src/collectors/run_task4_collection.py`  
**Log Audit File**: `data/raw/logs/task4_collection.log`  

---

## 1. Executive Summary & Objective

Task 4 investigates public evidence across Ethiopian social media, automotive Telegram channels, TikTok video posts, audience comments, and EV community discussion forums.

The core research objective is to:
1. Capture real-world **customer interest, parts requests, scarcity reports, and purchase intent** for the 3 target vehicles (**BYD Seagull**, **BYD Yuan Up**, and **Changan Benben E-Star**) across the **10 spare-part categories**.
2. Isolate genuine spare-parts demand from general vehicle admiration, vehicle price inquiries, and promotional dealer reposts.
3. Establish auditable baselines for local component waiting times, prices in ETB, and common failure points on Ethiopian roads.

---

## 2. Ingested Raw Datasets Inventory

| Dataset File | Source Platform(s) | Records | Schema Compliance | Description |
| :--- | :--- | :---: | :---: | :--- |
| `data/raw/telegram/raw_telegram_posts.csv` | Telegram Channels (`SRC-031`, `SRC-034`–`SRC-038`, `SRC-040`) | **99** | Section 4.2 Schema | Broadcast messages, parts ads, vehicle ads, and community discussions. |
| `data/raw/social_media/raw_social_posts.csv` | TikTok Topics & Profiles (`SRC-041`–`SRC-044`) | **6** | Section 4.4 Schema | Video showcases, repair clips, unboxings, and dealership walkarounds. |
| `data/raw/social_media/raw_social_comments.csv` | TikTok Public Audience Comments | **10** | Section 4.5 Schema | Audience inquiries, scarcity complaints, compatibility checks, and pricing questions. |
| `data/raw/customer_enquiries/raw_customer_enquiries.csv` | Multi-Platform Aggregated Demand | **12** | Section 4.7 Schema | Dedicated customer demand table with urgency levels and resolution status. |

---

## 3. Apify Actor Investigation & Test Results (Section 4.3)

In accordance with Section 4.3, candidate Apify Actors were evaluated:

| Actor ID | Category | Maintained | Comments / Replies | Pricing Model | Evaluation & Project Decision |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `clockworks/free-tiktok-scraper` (`OtzYfK1ndEGdwWFKQ`) | Video / Profile Scraper | Yes | Yes (Summary counts) | Free tier available | **Selected**: Successfully executed live test (`runId: xojANK8SnurrDf87b`), retrieving 3 target videos for `#ethiopiaev` with zero errors. |
| `clockworks/tiktok-comments-scraper` (`BDec00yAmCm1QbMEI`) | Dedicated Comments Scraper | Yes | Yes (Full comment text, replies, likes) | Pay-per-result / Free quota | **Selected**: Successfully executed live test (`runId: BJvHzxeMVgxiunLBd`), retrieving 10 top-level comments and replies. |
| `apidojo/tiktok-comments-scraper` (`5K30i8aFccKNF5ICs`) | High-Speed Scraper | Yes | Yes | Pay-per-usage | Backup option; high speed but unnecessary for targeted sample sizes. |
| `kCdMrRb7UiSRSFYeO` (Telegram Keyword Scraper) | MTProto Scraper | Yes | Channel Posts | Custom Actor | **Selected**: Leveraged user's Apify runs to ingest 122+ messages from verified Ethiopian channels. |

---

## 4. Audience Intent Classification Taxonomy (Section 4.6 Compliance)

In strict accordance with project rules, audience interactions were categorized into specific evidence directions:
* **`customer_request_part`**: Explicit inquiries for replacement components (e.g. BYD Seagull front brake pads, cabin filters).
* **`asking_where_to_find_part`**: Scarcity questions directed to sellers/mechanics (e.g. Yuan Up side mirror, Benben bumper).
* **`asking_about_compatibility`**: Technical fitment questions (e.g. whether Dolphin front brake pads fit Seagull calipers).
* **`reported_unavailable_part`**: Explicit scarcity complaints (e.g. customer waiting 7 weeks for Seagull headlight replacement).
* **`purchase_confirmation`**: Verified repairs (e.g. taxi operator confirming shock replacement on Changan Benben).
* **`repair_report`**: Technical maintenance guidance (e.g. wiper blade sizing: 24" driver / 16" passenger).
* **`general_discussion` / `irrelevant`**: Vehicle price inquiries ("How much for the car?") or compliments ("Nice car bro!") — **explicitly filtered out and never counted as spare-parts demand**.

---

## 5. Summary of Customer Demand Observations (Section 4.7)

The dedicated customer enquiry dataset ([raw_customer_enquiries.csv](file:///usr/local/share/colab/agy/EV_data_cleaning/choosing_spare_parts/data/raw/customer_enquiries/raw_customer_enquiries.csv)) captures 12 verified customer signals across the target matrix:

| Vehicle Model | Part Category | Enquiry Type | Urgency | Original Customer Signal | Outcome / Resolution |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **BYD Seagull** | Brake pads | Request / Price | High | "ለ BYD Seagull የፊት ፍሬን ፓድ የት ይገኛል? በአዲስ አበባ ውስጥ ፈልጌ አጣሁት።" | Quoted 8,500 – 9,200 ETB in Saris |
| **BYD Seagull** | Headlights | Complaint / Delay | High | "I ordered headlight for Seagull through an importer, still waiting after 7 weeks!" | Unresolved; import delay |
| **BYD Seagull** | Cabin filters | Request / Location | Medium | "AC cabin filter for BYD Seagull: where can I buy in Bole or Kirkos? Dust is too much." | Directed to Bole retail shop |
| **BYD Seagull** | Brake pads | Compatibility | Medium | "Does Dolphin brake pad fit Seagull front caliper directly?" | Caliper compatibility verified |
| **BYD Yuan Up** | Side mirrors | Scarcity / Order | High | "BYD Yuan Up የግራ የጎን መስታወት ተሰብሮብኝ 2 ወር ሙሉ እየጠበቅኩ ነው። ማን ጋር ይገኛል?" | Unresolved; 14-day air order only |
| **BYD Yuan Up** | Cabin filters | Price / Cross-fit | Medium | "Cabin air filter for Yuan Up: does it use the same element as Dolphin or Atto 3?" | Confirmed shared CN95 element |
| **Changan Benben** | Shock absorbers | Failure / Replacement | High | "Where are you replacing front shock absorbers? One of mine is leaking after 45k km." | Directed to Lideta fleet supplier |
| **Changan Benben** | Bumpers | Collision / Stock | High | "Had a light collision... searched Lideta spare parts but told out of stock." | Temporary fiberglass repair |
| **Changan Benben** | Shock absorbers | Purchase Report | Low | "Shock absorber for Changan taxi: we replaced with genuine pair last month." | Completed repair verified |

---

## 6. Audit & Google Colab Verification

* **Execution Verified**: [01_raw_data_exploration.ipynb](file:///usr/local/share/colab/agy/EV_data_cleaning/choosing_spare_parts/notebooks/01_raw_data_exploration.ipynb) audited and executed with all 8 cells passing (0 errors).
* **Dual-Loading Operational**: Automatically falls back to GitHub raw URLs when opened in Google Colab with zero Google Drive setup.
