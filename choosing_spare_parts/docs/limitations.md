# Research Limitations & Data Integrity Caveats

**Project**: Ethiopian EV Spare-Parts Demand & Import Opportunity Research Pipeline  
**Module**: `choosing_spare_parts/`  
**Last Updated**: November 2026 (Task 2 Complete)  

---

## 1. Source Accessibility & Technical Extraction Barriers
1. **Cloudflare Anti-Bot Challenges**: Major retail classified websites (Jiji Ethiopia, PartSouq, Sunny Spare Parts) enforce Cloudflare bot protection gates (HTTP 403 / JavaScript verification challenges), preventing direct automated scraping via simple Python scripts. These require manual extraction or stealth browser automation.
2. **Defunct & Broken Domains**: Certain historically referenced platforms (e.g., `adeymarket.com`, `speedyevparts.com`, `grandevaddis.com`) fail DNS resolution or are temporarily offline, necessitating their exclusion from active collection runs.
3. **Government Web Server Instability**: Ethiopian government ministry servers (MoTL, MoFED, ECC) intermittently time out or present self-signed SSL certificate issues, requiring manual PDF policy document download.

---

## 2. Market Information Asymmetries in Ethiopia
1. **Absence of Public Digital Parts Inventories**: No Ethiopian auto dealership or spare parts shop currently publishes an open, real-time API or e-commerce SKU inventory with live stock counters.
2. **Informal Pricing & Haggling**: Asking prices quoted on Telegram channels and classifieds are opening negotiations rather than fixed transaction prices; actual sale prices are typically 5–15% lower following face-to-face inspection.
3. **Parallel Gray-Market Import Fragmentation**: A substantial portion of BYD and Changan vehicles were imported by parallel independent traders rather than the official franchised distributor, resulting in fragmented aftersales records and unrecorded private parts imports.

---

## 3. Data Specificity & Macro Trade Limitations
1. **Aggregated Customs HS Codes**: Official Ethiopian Customs Commission (ECC) and UN Comtrade import databases classify automotive spare parts under general HS Heading 8708 without separating EV components from ICE components or identifying vehicle models.
2. **Social Media Engagement Bias**: Public comments on TikTok and Telegram over-index on price complaints and viral repair incidents, which may distort the perceived failure rate of specific components.
3. **Selection Bias in Scraped Ads**: Classifieds are skewed toward slow-moving high-ticket components that require broad advertising; fast-moving consumables (e.g. wiper blades, common brake pads) frequently sell out through direct garage walk-ins without ever being advertised online.
