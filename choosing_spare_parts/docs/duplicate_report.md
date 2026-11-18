# Duplicate Analysis & Cross-Posting Report — Task 6

**Audit Date**: 2026-11-18  
**Total Records Audited**: 262  
**Total Duplicate Observations Identified**: 73 (27.9%)  
**Unique Duplicate Cluster Groups**: 189  

---

## 1. Deduplication Strategy & Methodology

Records were evaluated across four cascading criteria:
1. **Exact Hash Match**: Identical raw text and parameters (`deduplication_confidence = 1.0`).
2. **URL Match**: Multiple collection passes capturing identical listing URLs (`deduplication_confidence = 0.95`).
3. **Fuzzy Text Clustering**: Normalized 80-character token matching to identify cross-platform reposts (e.g. Adey Market + AfroMekina).
4. **Broadcast Reposts**: Telegram channels rebroadcasting dealer inventory over multiple calendar dates.

---

## 2. Duplicate Type Breakdown

| Duplicate Type | Count | Share (%) | Handling Rule |
| :--- | :---: | :---: | :--- |
| **primary_record** | **189** | **72.1%** | Retained as primary evidentiary anchor. |
| **repeated_advertisement** | **41** | **15.6%** | Linked via `duplicate_group_id`; excluded from independent demand count. |
| **cross_platform_repost** | **8** | **3.1%** | Identified cross-posts across classifieds. |
| **exact_duplicate** | **24** | **9.2%** | Raw preserved; tagged `is_duplicate = True`. |

*Rule Compliance*: As specified in Section 6.4, duplicate records are **never deleted**. All raw IDs are preserved with `is_duplicate` and `duplicate_group_id` for auditable tracing.
