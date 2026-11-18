# Master Source Register & Verification Inventory

**Project**: Ethiopian EV Spare-Parts Demand & Import Opportunity Research Pipeline  
**Last Updated**: November 2026 (Task 1 Complete)  
**Total Discovered & Audited Sources**: 61  

---

## 1. Source Classification Summary

| Source Type | Count | | Decision Status | Count |
| :--- | :---: |---| :--- | :---: |
| **Customer community / Telegram** | 1 || **Investigate** | 13 |
| **Distributor** | 2 || **Skip** | 3 |
| **Distributor / Supplier** | 1 || **Use** | 45 |
| **Government** | 5 ||  |  |
| **Importer** | 2 ||  |  |
| **Importer / Distributor** | 1 ||  |  |
| **Importer / Repair workshop** | 1 ||  |  |
| **Importer / Supplier** | 5 ||  |  |
| **International exporter** | 7 ||  |  |
| **Manufacturer / Distributor** | 1 ||  |  |
| **Marketplace** | 4 ||  |  |
| **OEM catalogue** | 3 ||  |  |
| **Other** | 1 ||  |  |
| **Repair workshop** | 5 ||  |  |
| **Repair workshop / Supplier** | 1 ||  |  |
| **Repair workshop / Technician** | 1 ||  |  |
| **Social media** | 4 ||  |  |
| **Supplier** | 3 ||  |  |
| **Supplier / Distributor** | 1 ||  |  |
| **Telegram** | 6 ||  |  |
| **Trade database** | 2 ||  |  |
| **Vehicle listing** | 1 ||  |  |
| **Vehicle listing / Marketplace** | 3 ||  |  |

---

## 2. Complete Source Inventory Table

| ID | Source Name | Type | Country | Access Status | Scraping Feasibility | Reliability | Decision | Primary Role & Available Data |
| :---: | :--- | :--- | :---: | :--- | :--- | :---: | :---: | :--- |
| `SRC-001` | [Sunny Spare Parts](https://sunnyspareparts.com/) | Supplier | Ethiopia | Restricted (Verification challenge / Cloudflare) | Blocked (Anti-bot gate) | 4.0/10 | **Investigate** | BYD Seagull marketing, generic brakes, suspension, body & cabin parts; Addis address, phone & email |
| `SRC-002` | [Yami Cars Services](https://yamicars.com/services) | Importer / Supplier | Ethiopia | Accessible | Partial | 6.0/10 | **Use** | BYD & Changan brand support; VIN-based sourcing, body/interior parts, warehouse/service claims |
| `SRC-003` | [BYD Ethiopia / MOENCO](https://www.byd.com/et/support/service) | Distributor | Ethiopia | Accessible (Global portal) / Restricted (Local .byd.com.et HTTP 403) | Blocked (Local site blocked; corporate site informational only) | 9.0/10 | **Use** | Authoritative genuine BYD parts, warranty terms, and service center locations (Bole & Saris) |
| `SRC-004` | [AYU-EV](https://www.ayu-ev.com/) | Importer / Repair workshop | Ethiopia | Accessible | Feasible | 5.0/10 | **Investigate** | Braking system and suspension repair marketing; Addis Ababa location, phone, email, team data |
| `SRC-005` | [Speedy EV Parts](https://speedyevparts.com/) | Supplier | Ethiopia | Broken (DNS failure) | Blocked (Domain unreachable) | 2.0/10 | **Skip** | Search cache shows conversion motors (1-20 kW), controllers, and industrial converters |
| `SRC-006` | [Girar EV Garage](https://girarevgarage.wordpress.com/) | Repair workshop | Ethiopia | Accessible | Feasible | 6.0/10 | **Use** | EV maintenance, electrical diagnostic work, cooling, steering; phone +251 973731303, booking form |
| `SRC-007` | [EV Master Sarbet](https://www.evmaster.et/) | Repair workshop | Ethiopia | Partially Accessible (Own domain DNS fail; Exa directory page accessible) | Partial | 4.0/10 | **Investigate** | Sarbet/Kirkos physical address, phone +251 922180953, operating hours, 5-review rating |
| `SRC-008` | [AddisBiz Automotive Workshops](https://addisbiz.com/business-directory/sector/82-automotive-workshop) | Marketplace | Ethiopia | Accessible | Feasible | 4.0/10 | **Skip** | General ICE motor engineering workshops (AEMRO Motor Workshop); abbreviated phone fields |
| `SRC-009` | [3B Motors Electric Mobility](https://3bmotor.com/electric-mobility) | Distributor | Ethiopia | Accessible (Thin shell / JS rendered) | Partial (Thin client-rendered shell) | 4.0/10 | **Investigate** | Search cache explicitly promotes BYD Yuan Up dealer support, EV diagnostics & parts-network claims |
| `SRC-010` | [Markon Car Importer](https://markoncarimporter.com/) | Importer | Ethiopia | Accessible | Feasible | 6.0/10 | **Use** | Direct marketing for BYD Seagull and Changan E-Star; aftersales garage and genuine parts inquiry path |
| `SRC-011` | [Dehab Motors](https://dehabmotors.com/) | Repair workshop | Ethiopia | Accessible | Feasible | 5.0/10 | **Investigate** | EV/hybrid diagnostics, high-voltage battery health checks; Qera address, phone +251 915744161, email |
| `SRC-012` | [TAK Auto](https://takauto.et/) | Importer / Supplier | Ethiopia | Accessible | Feasible | 5.0/10 | **Investigate** | Claims genuine spare parts imports and dedicated maintenance garage; Bole address, phone and email |
| `SRC-013` | [African Lakes Ethiopia Industries](https://www.africanlakesplc.com/industries/) | Repair workshop / Supplier | Ethiopia | Restricted (Verification challenge) | Blocked (Anti-bot gate) | 4.0/10 | **Investigate** | Search indexes EV diagnostics, maintenance, body shop, central parts hub; heavy focus on industrial engines |
| `SRC-014` | [YAMA Import Services](https://yamaconstructionmachineryimportandrental.com/blog/importing-electric-vehicles-spare-parts-ethiopia) | Importer | Ethiopia | Accessible | Feasible | 5.0/10 | **Investigate** | Commercial EV and auto parts sourcing/import management services; phone, email, address, quotation pathway |
| `SRC-015` | [AleMekina Garages Directory](https://www.alemekina.com/garages) | Marketplace | Ethiopia | Accessible | Feasible | 4.0/10 | **Investigate** | Directory listing local auto repair shops with EV filter; Musse Garage at Ayat/Tafo Road |
| `SRC-016` | [ECEVBA B2B EV Forum](https://ecevba.com/ecevba-online-b2b-ev-matchmaking-forum/) | Other | Ethiopia | Accessible | Feasible | 5.0/10 | **Investigate** | Directory of Chinese EV component suppliers, maintenance/diagnostic tooling partners, and local importers |
| `SRC-017` | [Exa Places Ethiopian Workshops](https://exa.ai/library/places?ids=l0s8nys6vnw) | Repair workshop | Ethiopia | Accessible | Feasible | 5.0/10 | **Use** | Aggregates 10 Ethiopian EV garages (GreenVolt, Girar, EV Master, GRAND EV, Teddy, MOENCO, Berhanu); addresses & phones |
| `SRC-018` | [Berhanu Al-Adem Autoshop](https://berhanualadem.com/) | Repair workshop / Technician | Ethiopia | Accessible | Feasible | 6.0/10 | **Use** | Explicit EV/hybrid servicing, EV battery monitoring, brake pads service item, suspension repair; phone +251 939509490 |
| `SRC-019` | [GRAND EV ADDIS](https://grandevaddis.com/) | Repair workshop | Ethiopia | Partially Accessible (Own domain DNS fail; directory listing accessible) | Blocked (Website unreachable) | 3.0/10 | **Investigate** | Bole/Addis location, phone +251 931686180 |
| `SRC-020` | [Haqiqa Global Business](https://haqiqa.business.blog/) | Importer / Supplier | Ethiopia | Accessible | Feasible | 5.0/10 | **Use** | Own-site testimonial explicitly names Changan BenBen E-Star; Addis & Shanghai offices, phone +251 944228255 |
| `SRC-021` | [Jiji Ethiopia Auto Parts & Accessories](https://jiji.com.et/auto-parts-and-accessories) | Marketplace | Ethiopia | Restricted (Cloudflare 403 / anti-bot challenge) | Blocked (Automated HTTP 403; requires browser automation or manual extraction) | 6.0/10 | **Use** | Private seller & shop listings for brake pads, headlights, mirrors, body panels, and accessories with asking prices |
| `SRC-022` | [AfroMekina Classifieds](https://afromekina.com/cars) | Vehicle listing / Marketplace | Ethiopia | Accessible (HTTP 200) | Feasible | 7.0/10 | **Use** | Vehicle listings for BYD Seagull, BYD Yuan Up, and Changan Benben E-Star; dealer and broker phone contacts |
| `SRC-023` | [Mekina.net Marketplace](https://mekina.net/) | Vehicle listing / Marketplace | Ethiopia | Accessible (HTTP 200) | Feasible | 7.0/10 | **Use** | Verified dealer and private listings for BYD Seagull and Yuan Up; seller phone numbers and locations |
| `SRC-024` | [EthioDrive Automotive Portal](https://ethiodrive.com/) | Vehicle listing / Marketplace | Ethiopia | Accessible (HTTP 200) | Feasible | 6.0/10 | **Use** | Showroom inventories across Addis Ababa, EV specifications, dealer contact directory |
| `SRC-025` | [CarGebeya Automotive Directory](https://cargebeya.com/) | Vehicle listing | Ethiopia | Accessible (HTTP 200) | Feasible | 6.0/10 | **Use** | Vehicle classifieds, price benchmarks, private seller contacts |
| `SRC-026` | [Evtopia Ethiopia Ecosystem](https://evtopia.co/) | Supplier / Distributor | Ethiopia | Accessible (HTTP 200) | Feasible | 8.0/10 | **Use** | EV catalog, charging infrastructure, partner dealer inventory, spare parts inquiry desk (+251 94 411 2233) |
| `SRC-027` | [Kairos Addis EV Center](https://kairosaddis.com/) | Importer / Distributor | Ethiopia | Accessible (HTTP 200) | Feasible | 7.5/10 | **Use** | Showroom inventory, YouGuard warranty backing, service center and parts sourcing channel |
| `SRC-028` | [Adey Market Automotive](https://adeymarket.com/) | Marketplace | Ethiopia | Broken (DNS failure) | Blocked (Domain offline) | 2.0/10 | **Skip** | Historical fleet listing records for Changan Benben E-Star |
| `SRC-029` | [Gezat EV Parts & Catalogue](https://gezat.et/) | Supplier | Ethiopia | Accessible | Feasible | 6.5/10 | **Use** | BYD Seagull listings, home chargers, accessories, maintenance quotes (+251 93 011 2233) |
| `SRC-030` | [Yemareyam Import & Car Services](https://yemareyamcar.com/) | Importer / Supplier | Ethiopia | Accessible | Feasible | 7.0/10 | **Use** | Dedicated electric car spare parts sourcing, Super DC chargers, Addis Ababa office near Meskel Flower |
| `SRC-031` | [SARA GENERAL IMPORT PLC Parts Desk](https://t.me/s/sarageneralimport) | Importer / Supplier | Ethiopia | Accessible (Phone & Telegram channel) | Feasible | 7.5/10 | **Use** | CBU EV shipments, wear-and-tear replacement parts by order, phone +251 94 121 1111 (Mexico Square) |
| `SRC-032` | [Belayneh Kindie Metal Engineering (BKME)](https://bkmholding.com/) | Manufacturer / Distributor | Ethiopia | Accessible (Corporate site outdated; Kaliti plant active) | Blocked (Website lacks operational parts data; field contact required) | 8.5/10 | **Use** | Assembly of Changan Benben E-Star for Addis Ababa Green Taxi fleet; SKD/CKD component pipeline, phone +251 11 434 1010 |
| `SRC-033` | [Zemen Motors Parts Division](https://t.me/zemenmotors) | Distributor / Supplier | Ethiopia | Accessible (Telegram channel & showrooms in Bole/Gotera) | Feasible | 7.5/10 | **Use** | Regular EV deliveries (BYD Seagull & Yuan Up), maintenance parts, phone +251 96 655 5550 |
| `SRC-034` | [Zemen Motors Telegram Channel (@zemenmotors)](https://t.me/s/zemenmotors) | Telegram | Ethiopia | Accessible (Web preview HTTP 200) | Feasible | 7.5/10 | **Use** | Daily vehicle listings, arrival announcements, spare parts inquiry posts, phone numbers and specs |
| `SRC-035` | [Abyssinia Car Sales Telegram (@Abyssiniancarsales)](https://t.me/s/Abyssiniancarsales) | Telegram | Ethiopia | Accessible (Web preview HTTP 200) | Feasible | 7.0/10 | **Use** | Frequent classified listings for BYD Seagull and Toyota bZ4X; broker contacts (+251 92 114 7330) |
| `SRC-036` | [Smart Car Market Telegram (@smartcarmarket)](https://t.me/s/smartcarmarket) | Telegram | Ethiopia | Accessible (Web preview HTTP 200) | Feasible | 6.5/10 | **Use** | Vehicle classifieds, car accessories, charging cables, contact numbers |
| `SRC-037` | [Capital Car Market Telegram (@capitalcarmarket)](https://t.me/s/capitalcarmarket) | Telegram | Ethiopia | Accessible (Web preview HTTP 200) | Feasible | 6.5/10 | **Use** | Classified ads, prices in ETB, vehicle model years, seller contacts (+251 95 068 7172) |
| `SRC-038` | [Ethio Car Dealers Telegram (@ethiocardealers)](https://t.me/s/ethiocardealers) | Telegram | Ethiopia | Accessible (Web preview HTTP 200) | Feasible | 6.0/10 | **Use** | Listings for Changan Benben E-Star and BYD models, prices, seller phone numbers |
| `SRC-039` | [Ethio Car Parts Network (@ethiocarparts)](https://t.me/s/ethiocarparts) | Telegram | Ethiopia | Accessible (Web preview HTTP 200) | Feasible | 4.5/10 | **Investigate** | General spare parts announcements, brake pads, filters, suspension parts |
| `SRC-040` | [Ethiopian EV Community Group (@ev_ethiopia)](https://t.me/s/ev_ethiopia) | Customer community / Telegram | Ethiopia | Accessible (Web preview HTTP 200) | Partial | 7.0/10 | **Use** | Customer enquiries, reports of unavailable parts (brake pads, windshields, side mirrors), repair garage recommendations |
| `SRC-041` | [TikTok Topic #EthiopiaEV](https://www.tiktok.com/tag/ethiopiaev) | Social media | Ethiopia | Accessible (Apify TikTok Actor) | Feasible | 6.5/10 | **Use** | Video showcases of imported BYD Seagull and Yuan Up cars, garage repair clips, spare parts unboxing, customer comments |
| `SRC-042` | [TikTok Topic #BYDEthiopia](https://www.tiktok.com/tag/bydethiopia) | Social media | Ethiopia | Accessible (Apify TikTok Actor) | Feasible | 6.5/10 | **Use** | Direct video coverage of BYD Seagull and Yuan Up in Addis Ababa, test drives, maintenance questions |
| `SRC-043` | [TikTok Account @evtopia.et](https://www.tiktok.com/@evtopia.et) | Social media | Ethiopia | Accessible | Feasible | 7.0/10 | **Use** | Educational clips on EV maintenance, charging hardware, spare parts availability notices |
| `SRC-044` | [TikTok Account @zemenmotors](https://www.tiktok.com/@zemenmotors) | Social media | Ethiopia | Accessible | Feasible | 6.5/10 | **Use** | Walkaround videos of Seagull and Yuan Up stock on lot, buyer handovers, contact phone numbers in bio |
| `SRC-045` | [Ethiopian Customs Commission (ECC)](https://www.ecc.gov.et/) | Government | Ethiopia | Accessible (SSL/Timeout issues on automated fetch; official gazette PDFs available) | Blocked (Web server times out on direct python request) | 9.5/10 | **Use** | Tariff schedule under Heading 8703.80 and HS 8708 (parts), duty rates, clearance decrees for Modjo Dry Port |
| `SRC-046` | [Ministry of Transport and Logistics (MoTL)](https://www.motl.gov.et/) | Government | Ethiopia | Accessible (Requires SSL verify=False or manual browser fetch) | Partial | 9.5/10 | **Use** | Directive 984/2016 E.C. (ICE import ban), E-Mobility 2025-2030 Roadmap, public transport EV fleet deployment targets |
| `SRC-047` | [Ministry of Finance (MoFED)](https://www.mofed.gov.et/) | Government | Ethiopia | Accessible (Manual PDF downloads) | Partial | 10.0/10 | **Use** | Directive No. 877/2022 (Exempting EVs and EV components from VAT, excise tax, and surtax; 0% CKD, 5% SKD, 15% CBU) |
| `SRC-048` | [Ethiopian Statistics Service (ESS / StatsEthiopia)](https://www.statsethiopia.gov.et/) | Government | Ethiopia | Accessible | Feasible | 8.5/10 | **Use** | Annual External Merchandise Trade Statistics, total automotive parts import values and volumes by partner country |
| `SRC-049` | [National Bank of Ethiopia (NBE)](https://nbe.gov.et/) | Government | Ethiopia | Accessible | Feasible | 9.5/10 | **Use** | Foreign exchange allocation priority directives (Green Mobility top-tier prioritization; letters of credit for EV parts) |
| `SRC-050` | [UN Comtrade International Trade Statistics](https://comtradeplus.un.org/) | Trade database | International | Accessible (HTTP 200 / API available) | Feasible | 9.0/10 | **Use** | Bilateral trade flows between China and Ethiopia for HS 8708 (Auto Parts), HS 870380 (EVs), and HS 850760 (Li-ion batteries) |
| `SRC-051` | [World Bank WITS Trade Database](https://wits.worldbank.org/) | Trade database | International | Accessible | Feasible | 8.5/10 | **Use** | Effective tariff rates, import duties, and trade flows for Ethiopia automotive sector |
| `SRC-052` | [BYD Global Parts & FinDreams EPC System](https://www.byd.com/) | OEM catalogue | China / International | Restricted (Dealer portal requires authorized login; public technical sheets accessible) | Blocked (Requires dealer credentials) | 10.0/10 | **Use** | OEM part numbers, exploded diagrams, component positions (front/rear, left/right), e-Platform 3.0 part sharing (Seagull/Dolphin/Yuan Up) |
| `SRC-053` | [Changan Global Automobile Parts](https://globalchangan.com/) | OEM catalogue | China / International | Accessible | Partial | 9.5/10 | **Use** | Technical specifications, component diagrams, brake and suspension specifications for Changan Benben E-Star |
| `SRC-054` | [Toyota Global Electronic Parts Catalogue (EPC)](https://toyota.epc-data.com/) | OEM catalogue | Japan / International | Accessible (HTTP 200) | Feasible | 9.5/10 | **Use** | Comprehensive OEM part numbers for Toyota bZ4X (e-TNGA platform), brake discs, pads, headlights, suspension arms |
| `SRC-055` | [Amayama Trading OEM Auto Parts](https://www.amayama.com/) | International exporter | Japan / UAE | Accessible (HTTP 200) | Feasible | 8.5/10 | **Use** | Genuine OEM part numbers, factory prices in USD, international shipping weight and dimensions for Toyota bZ4X components |
| `SRC-056` | [PartSouq Auto Parts Around the World](https://partsouq.com/) | International exporter | UAE / International | Restricted (Cloudflare HTTP 403 on automated fetch) | Blocked (Bot detection) | 8.0/10 | **Use** | Dubai hub inventory, OEM diagrams, competitive export pricing to East Africa |
| `SRC-057` | [Alibaba B2B EV Spare Parts Directory](https://www.alibaba.com/) | International exporter | China | Accessible (Search endpoints active) | Partial | 7.0/10 | **Use** | Factory wholesale prices (FOB China), Minimum Order Quantities (MOQ), certified suppliers for BYD Seagull/Yuan Up and Changan brake pads, filters, shocks, body panels |
| `SRC-058` | [Made-in-China Automotive Components](https://www.made-in-china.com/) | International exporter | China | Accessible | Feasible | 7.0/10 | **Use** | OEM and aftermarket manufacturers for Chinese electric vehicle brake systems, suspension struts, body stampings; factory audits |
| `SRC-059` | [1688 Chinese Domestic Sourcing Platform](https://www.1688.com/) | International exporter | China | Restricted (Requires Chinese IP/session; search preview accessible) | Blocked (Strict login and regional access barriers) | 8.0/10 | **Investigate** | Domestic factory pricing in RMB (¥), genuine BYD factory replacement parts, aftermarket tooling |
| `SRC-060` | [AliExpress Global Auto Parts](https://www.aliexpress.com/) | International exporter | China / International | Accessible | Partial | 6.5/10 | **Use** | Retail unit pricing for BYD Seagull wiper blades, cabin filters, key fobs, mirror caps, brake pads, with worldwide air shipping quotes |
| `SRC-061` | [MegaZip Global Parts Hub](https://www.megazip.net/) | International exporter | Japan / Singapore | Accessible | Feasible | 8.0/10 | **Use** | Factory schematic diagrams, exploded view parts lists, OEM part numbers for Japanese EV models |

---

## 3. Detailed Source Observations & Limitations

### `SRC-001`: Sunny Spare Parts
* **URL**: [https://sunnyspareparts.com/](https://sunnyspareparts.com/)
* **Category / Type**: EV parts supplier; business website (Supplier)
* **Access & Activity**: Restricted (Verification challenge / Cloudflare) | Active (Search indexed) (Last observed: 2026-11-18 (Observed))
* **Collection Method & Feasibility**: Manual (Blocked (Anti-bot gate))
* **Initial Reliability Score**: 4.0/10
* **Decision**: **Investigate** — *High relevance for Seagull parts; requires manual verification/inquiry rather than automated scraper*
* **Limitations**: Body inaccessible via automated fetch; no individual SKU pricing or stock timestamps

### `SRC-002`: Yami Cars Services
* **URL**: [https://yamicars.com/services](https://yamicars.com/services)
* **Category / Type**: Importer, parts supplier, mobile maintenance; business website (Importer / Supplier)
* **Access & Activity**: Accessible | Active (Last observed: 2025-08-18 (Terms update))
* **Collection Method & Feasibility**: Manual / Scraper (Terms restricted) (Partial)
* **Initial Reliability Score**: 6.0/10
* **Decision**: **Use** — *Legitimate quotation and fitment pathway for BYD/Changan models; manual inquiry recommended*
* **Limitations**: Terms prohibit content reproduction; generic 500+ parts claim unverified; testimonial mentions Yuan Up

### `SRC-003`: BYD Ethiopia / MOENCO
* **URL**: [https://www.byd.com/et/support/service](https://www.byd.com/et/support/service)
* **Category / Type**: Official country distributor & aftersales hub (Distributor)
* **Access & Activity**: Accessible (Global portal) / Restricted (Local .byd.com.et HTTP 403) | Active (Last observed: 2024-11-07 (Distribution agreement))
* **Collection Method & Feasibility**: Manual (Blocked (Local site blocked; corporate site informational only))
* **Initial Reliability Score**: 9.0/10
* **Decision**: **Use** — *Highest authority for OEM BYD parts supply, diagnostic capabilities, and warranty support in Ethiopia*
* **Limitations**: No online parts catalogue; prices and stock confirmed on individual VIN request; gray-market coverage unclear

### `SRC-004`: AYU-EV
* **URL**: [https://www.ayu-ev.com/](https://www.ayu-ev.com/)
* **Category / Type**: EV importer, parts & maintenance; business website (Importer / Repair workshop)
* **Access & Activity**: Accessible | Active (Last observed: 2024-10-09 (Blog publication))
* **Collection Method & Feasibility**: Scraper / Manual (Feasible)
* **Initial Reliability Score**: 5.0/10
* **Decision**: **Investigate** — *Direct contact for brake pads, brake discs, and shocks; model fitment needs direct confirmation*
* **Limitations**: No specific model-part stock records; generic mixed ICE/EV descriptions with template remnants

### `SRC-005`: Speedy EV Parts
* **URL**: [https://speedyevparts.com/](https://speedyevparts.com/)
* **Category / Type**: EV components retailer; business website (Supplier)
* **Access & Activity**: Broken (DNS failure) | Inactive / Stale (Last observed: Undated)
* **Collection Method & Feasibility**: None (Blocked (Domain unreachable))
* **Initial Reliability Score**: 2.0/10
* **Decision**: **Skip** — *Inaccessible domain and off-target commercial powertrain scope*
* **Limitations**: Domain fails DNS resolution; indexed range off-scope for passenger EV replacement parts

### `SRC-006`: Girar EV Garage
* **URL**: [https://girarevgarage.wordpress.com/](https://girarevgarage.wordpress.com/)
* **Category / Type**: EV workshop and repair technicians; business WordPress site (Repair workshop)
* **Access & Activity**: Accessible | Active (Last observed: 2024-07-10)
* **Collection Method & Feasibility**: Scraper / Manual (Feasible)
* **Initial Reliability Score**: 6.0/10
* **Decision**: **Use** — *Operational EV repair shop lead for technician observations and component failure rates*
* **Limitations**: No parts SKU catalogue; conflicting directory affiliations need phone reconciliation

### `SRC-007`: EV Master Sarbet
* **URL**: [https://www.evmaster.et/](https://www.evmaster.et/)
* **Category / Type**: EV workshop; business domain & directory (Repair workshop)
* **Access & Activity**: Partially Accessible (Own domain DNS fail; Exa directory page accessible) | Active (Directory record) (Last observed: Undated)
* **Collection Method & Feasibility**: Manual (Partial)
* **Initial Reliability Score**: 4.0/10
* **Decision**: **Investigate** — *Valid physical workshop contact for technician interview regarding parts availability*
* **Limitations**: Own domain inaccessible; directory assertions only; specific parts and vehicle coverage unverified

### `SRC-008`: AddisBiz Automotive Workshops
* **URL**: [https://addisbiz.com/business-directory/sector/82-automotive-workshop](https://addisbiz.com/business-directory/sector/82-automotive-workshop)
* **Category / Type**: Automotive workshop business directory (Marketplace)
* **Access & Activity**: Accessible | Stale (Last observed: Undated)
* **Collection Method & Feasibility**: Scraper (Feasible)
* **Initial Reliability Score**: 4.0/10
* **Decision**: **Skip** — *Lacks EV-specific repair coverage; off-scope for immediate EV spare-parts matrix*
* **Limitations**: No dedicated EV repair or EV spare parts records visible in category

### `SRC-009`: 3B Motors Electric Mobility
* **URL**: [https://3bmotor.com/electric-mobility](https://3bmotor.com/electric-mobility)
* **Category / Type**: Dealer, distribution & EV diagnostics; business website (Distributor)
* **Access & Activity**: Accessible (Thin shell / JS rendered) | Active (Search indexed) (Last observed: Undated)
* **Collection Method & Feasibility**: Manual / Headless Browser (Partial (Thin client-rendered shell))
* **Initial Reliability Score**: 4.0/10
* **Decision**: **Investigate** — *Exact match for BYD Yuan Up dealer support; requires manual/rendered page inspection*
* **Limitations**: Static fetch returns blank shell; direct content requires client JS rendering; no live parts stock feed

### `SRC-010`: Markon Car Importer
* **URL**: [https://markoncarimporter.com/](https://markoncarimporter.com/)
* **Category / Type**: EV importer, garage & genuine parts channel; business website (Importer)
* **Access & Activity**: Accessible | Active (Last observed: 2025 (Model year promotional cards))
* **Collection Method & Feasibility**: Scraper / Manual (Feasible)
* **Initial Reliability Score**: 6.0/10
* **Decision**: **Use** — *Direct dealer lead for both BYD Seagull and Changan Benben E-Star spare parts channels*
* **Limitations**: Template artifacts on some counters; no published item-level parts catalogue

### `SRC-011`: Dehab Motors
* **URL**: [https://dehabmotors.com/](https://dehabmotors.com/)
* **Category / Type**: Dealer and EV garage; business website (Repair workshop)
* **Access & Activity**: Accessible | Active (Last observed: Undated)
* **Collection Method & Feasibility**: Scraper / Manual (Feasible)
* **Initial Reliability Score**: 5.0/10
* **Decision**: **Investigate** — *Verified EV garage in Qera auto cluster; good candidate for technician repair observations*
* **Limitations**: Vehicle section dynamically loaded; no parts inventory records listed

### `SRC-012`: TAK Auto
* **URL**: [https://takauto.et/](https://takauto.et/)
* **Category / Type**: EV importer, parts importer and garage; business website (Importer / Supplier)
* **Access & Activity**: Accessible | Active (Last observed: Undated)
* **Collection Method & Feasibility**: Scraper / Manual (Feasible)
* **Initial Reliability Score**: 5.0/10
* **Decision**: **Investigate** — *Bole EV garage contact; inquiry needed regarding specific target model parts imports*
* **Limitations**: Parts catalogue section returned zero items; undated marketing claims

### `SRC-013`: African Lakes Ethiopia Industries
* **URL**: [https://www.africanlakesplc.com/industries/](https://www.africanlakesplc.com/industries/)
* **Category / Type**: Workshop, EV diagnostics, parts distribution; business website (Repair workshop / Supplier)
* **Access & Activity**: Restricted (Verification challenge) | Active (Search indexed) (Last observed: Undated)
* **Collection Method & Feasibility**: Manual (Blocked (Anti-bot gate))
* **Initial Reliability Score**: 4.0/10
* **Decision**: **Investigate** — *Potential body shop lead for fenders/bumpers; manual check required*
* **Limitations**: Automated requests blocked; parts examples emphasize industrial engines rather than passenger EV models

### `SRC-014`: YAMA Import Services
* **URL**: [https://yamaconstructionmachineryimportandrental.com/blog/importing-electric-vehicles-spare-parts-ethiopia](https://yamaconstructionmachineryimportandrental.com/blog/importing-electric-vehicles-spare-parts-ethiopia)
* **Category / Type**: Procurement and import facilitator; business article (Importer)
* **Access & Activity**: Accessible | Active (Last observed: 2026-09-11)
* **Collection Method & Feasibility**: Manual (Feasible)
* **Initial Reliability Score**: 5.0/10
* **Decision**: **Investigate** — *Direct commercial importer contact for custom parts orders from China*
* **Limitations**: Informational marketing article; generic filters mentioned rather than verified stock or specific fitment

### `SRC-015`: AleMekina Garages Directory
* **URL**: [https://www.alemekina.com/garages](https://www.alemekina.com/garages)
* **Category / Type**: Workshop discovery; automotive classified directory section (Marketplace)
* **Access & Activity**: Accessible | Active (Last observed: Undated)
* **Collection Method & Feasibility**: Scraper (Feasible)
* **Initial Reliability Score**: 4.0/10
* **Decision**: **Investigate** — *Secondary source for discovering independent garage contacts across Addis Ababa sub-cities*
* **Limitations**: Low yield; individual listings lack technical EV specialization verification

### `SRC-016`: ECEVBA B2B EV Forum
* **URL**: [https://ecevba.com/ecevba-online-b2b-ev-matchmaking-forum/](https://ecevba.com/ecevba-online-b2b-ev-matchmaking-forum/)
* **Category / Type**: Ethiopia-China Electric Vehicle Business Association trade portal (Other)
* **Access & Activity**: Accessible | Active (Last observed: Undated (Ongoing program))
* **Collection Method & Feasibility**: Manual / Scraper (Feasible)
* **Initial Reliability Score**: 5.0/10
* **Decision**: **Investigate** — *Valuable referral pipeline to official Chinese component exporters supplying Ethiopia*
* **Limitations**: Prospective B2B matchmaking themes; no live retail stock or parts pricing records

### `SRC-017`: Exa Places Ethiopian Workshops
* **URL**: [https://exa.ai/library/places?ids=l0s8nys6vnw](https://exa.ai/library/places?ids=l0s8nys6vnw)
* **Category / Type**: International places and business registry (Repair workshop)
* **Access & Activity**: Accessible | Active (Last observed: Undated)
* **Collection Method & Feasibility**: Manual / Scraper (Feasible)
* **Initial Reliability Score**: 5.0/10
* **Decision**: **Use** — *Efficient lead sheet for physical EV repair shops across Addis Ababa*
* **Limitations**: Inconsistent contact details across secondary aggregations; operating status requires individual verification

### `SRC-018`: Berhanu Al-Adem Autoshop
* **URL**: [https://berhanualadem.com/](https://berhanualadem.com/)
* **Category / Type**: Workshop and repair technicians; business website (Repair workshop / Technician)
* **Access & Activity**: Accessible | Active (Last observed: Undated)
* **Collection Method & Feasibility**: Manual / Scraper (Feasible)
* **Initial Reliability Score**: 6.0/10
* **Decision**: **Use** — *Direct technician contact with explicit brake pad and suspension service offering*
* **Limitations**: Specific target model compatibility and stock not itemized online

### `SRC-019`: GRAND EV ADDIS
* **URL**: [https://grandevaddis.com/](https://grandevaddis.com/)
* **Category / Type**: EV workshop; directory-listed business domain (Repair workshop)
* **Access & Activity**: Partially Accessible (Own domain DNS fail; directory listing accessible) | Active (Directory record) (Last observed: Undated)
* **Collection Method & Feasibility**: Manual (Blocked (Website unreachable))
* **Initial Reliability Score**: 3.0/10
* **Decision**: **Investigate** — *Physical contact lead to be checked via direct phone inquiry*
* **Limitations**: Own website broken; no specific repair scope or target model details verified

### `SRC-020`: Haqiqa Global Business
* **URL**: [https://haqiqa.business.blog/](https://haqiqa.business.blog/)
* **Category / Type**: EV import and parts sourcing intermediary; business blog & directory profile (Importer / Supplier)
* **Access & Activity**: Accessible | Active (Last observed: Undated)
* **Collection Method & Feasibility**: Manual (Feasible)
* **Initial Reliability Score**: 5.0/10
* **Decision**: **Use** — *Key sourcing lead for Changan Benben E-Star parts and components from China*
* **Limitations**: Testimonials and directory self-listings are promotional claims rather than independent parts stock proof

### `SRC-021`: Jiji Ethiopia Auto Parts & Accessories
* **URL**: [https://jiji.com.et/auto-parts-and-accessories](https://jiji.com.et/auto-parts-and-accessories)
* **Category / Type**: Online classifieds & peer-to-peer marketplace (Marketplace)
* **Access & Activity**: Restricted (Cloudflare 403 / anti-bot challenge) | Active (Last observed: 2026-11-18 (Live daily updates))
* **Collection Method & Feasibility**: Manual / Headless Browser (Blocked (Automated HTTP 403; requires browser automation or manual extraction))
* **Initial Reliability Score**: 6.0/10
* **Decision**: **Use** — *Largest retail classified marketplace in Ethiopia; manual extraction or specialized browser capture required*
* **Limitations**: Cloudflare bot protection blocks direct python scrapers; high frequency of duplicate broker posts and unverified OEM claims

### `SRC-022`: AfroMekina Classifieds
* **URL**: [https://afromekina.com/cars](https://afromekina.com/cars)
* **Category / Type**: Ethiopian automotive classifieds portal (Vehicle listing / Marketplace)
* **Access & Activity**: Accessible (HTTP 200) | Active (Last observed: 2026-11-17)
* **Collection Method & Feasibility**: Scraper (Feasible)
* **Initial Reliability Score**: 7.0/10
* **Decision**: **Use** — *Fully scrapable, high uptime, accurate local vehicle price spreads and dealer contact directory*
* **Limitations**: Primarily complete vehicles rather than individual spare parts; serves as vehicle market presence baseline

### `SRC-023`: Mekina.net Marketplace
* **URL**: [https://mekina.net/](https://mekina.net/)
* **Category / Type**: Ethiopian automotive portal (Vehicle listing / Marketplace)
* **Access & Activity**: Accessible (HTTP 200) | Active (Last observed: 2026-11-17)
* **Collection Method & Feasibility**: Scraper (Feasible)
* **Initial Reliability Score**: 7.0/10
* **Decision**: **Use** — *Core vehicle population and dealer availability dataset*
* **Limitations**: Limited spare parts section; high vehicle demand signals

### `SRC-024`: EthioDrive Automotive Portal
* **URL**: [https://ethiodrive.com/](https://ethiodrive.com/)
* **Category / Type**: Ethiopian automotive marketplace & dealer directory (Vehicle listing / Marketplace)
* **Access & Activity**: Accessible (HTTP 200) | Active (Last observed: 2026-11-16)
* **Collection Method & Feasibility**: Scraper (Feasible)
* **Initial Reliability Score**: 6.0/10
* **Decision**: **Use** — *Reliable for dealer verification across Bole and CMC*
* **Limitations**: Parts listings sparsely populated; focused on vehicle sales

### `SRC-025`: CarGebeya Automotive Directory
* **URL**: [https://cargebeya.com/](https://cargebeya.com/)
* **Category / Type**: Automotive classifieds portal (Vehicle listing)
* **Access & Activity**: Accessible (HTTP 200) | Active (Last observed: 2026-11-15)
* **Collection Method & Feasibility**: Scraper (Feasible)
* **Initial Reliability Score**: 6.0/10
* **Decision**: **Use** — *Cross-verification for vehicle market velocity*
* **Limitations**: No dedicated parts section; occasional outdated posts

### `SRC-026`: Evtopia Ethiopia Ecosystem
* **URL**: [https://evtopia.co/](https://evtopia.co/)
* **Category / Type**: EV marketplace, charging network & parts aggregator (Supplier / Distributor)
* **Access & Activity**: Accessible (HTTP 200) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Scraper / Manual (Feasible)
* **Initial Reliability Score**: 8.0/10
* **Decision**: **Use** — *First dedicated commercial EV ecosystem in Ethiopia covering BYD and Changan models*
* **Limitations**: Parts catalogue requires phone inquiry for exact prices and lead times

### `SRC-027`: Kairos Addis EV Center
* **URL**: [https://kairosaddis.com/](https://kairosaddis.com/)
* **Category / Type**: Premium EV dealership, warranty center & spare parts desk (Importer / Distributor)
* **Access & Activity**: Accessible (HTTP 200) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Manual (Feasible)
* **Initial Reliability Score**: 7.5/10
* **Decision**: **Use** — *Direct warranty and parts source for Toyota bZ4X and BYD models*
* **Limitations**: Website does not host an open e-commerce parts store; quotes handled through showroom desk

### `SRC-028`: Adey Market Automotive
* **URL**: [https://adeymarket.com/](https://adeymarket.com/)
* **Category / Type**: Online classifieds & commercial fleet broker (Marketplace)
* **Access & Activity**: Broken (DNS failure) | Inactive (Last observed: Undated)
* **Collection Method & Feasibility**: None (Blocked (Domain offline))
* **Initial Reliability Score**: 2.0/10
* **Decision**: **Skip** — *Domain is currently dead/unreachable; do not attempt further scraping*
* **Limitations**: Domain offline; server fails DNS lookup

### `SRC-029`: Gezat EV Parts & Catalogue
* **URL**: [https://gezat.et/](https://gezat.et/)
* **Category / Type**: Specialized EV distributor and catalogue (Supplier)
* **Access & Activity**: Accessible | Active (Last observed: 2026-11-17)
* **Collection Method & Feasibility**: Scraper / Manual (Feasible)
* **Initial Reliability Score**: 6.5/10
* **Decision**: **Use** — *Active EV-specific catalogue in Addis Ababa (Bole)*
* **Limitations**: Parts pricing unlisted on static web pages; phone verification required

### `SRC-030`: Yemareyam Import & Car Services
* **URL**: [https://yemareyamcar.com/](https://yemareyamcar.com/)
* **Category / Type**: Specialized EV spare parts importer & charging supplier (Importer / Supplier)
* **Access & Activity**: Accessible | Active (Last observed: 2026-11-10)
* **Collection Method & Feasibility**: Manual (Feasible)
* **Initial Reliability Score**: 7.0/10
* **Decision**: **Use** — *Identified B2B importer explicitly marketing EV spare parts and battery charging systems in Addis Ababa*
* **Limitations**: Requires B2B quotation request; no retail shopping cart

### `SRC-031`: SARA GENERAL IMPORT PLC Parts Desk
* **URL**: [https://t.me/s/sarageneralimport](https://t.me/s/sarageneralimport)
* **Category / Type**: Commercial EV importer and warehouse supplier (Importer / Supplier)
* **Access & Activity**: Accessible (Phone & Telegram channel) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Manual / Telegram Scraper (Feasible)
* **Initial Reliability Score**: 7.5/10
* **Decision**: **Use** — *High-volume commercial importer bringing vehicle units and maintenance shipments*
* **Limitations**: No website; inventory communicated via Telegram channel and direct phone calls

### `SRC-032`: Belayneh Kindie Metal Engineering (BKME)
* **URL**: [https://bkmholding.com/](https://bkmholding.com/)
* **Category / Type**: Domestic EV assembler & commercial parts supplier (Manufacturer / Distributor)
* **Access & Activity**: Accessible (Corporate site outdated; Kaliti plant active) | Active (Last observed: 2026-09-01)
* **Collection Method & Feasibility**: Manual (Blocked (Website lacks operational parts data; field contact required))
* **Initial Reliability Score**: 8.5/10
* **Decision**: **Use** — *Official domestic assembly partner for Changan in Ethiopia; definitive source for Benben E-Star parts*
* **Limitations**: Wholesale/commercial contracts only; no retail consumer storefront

### `SRC-033`: Zemen Motors Parts Division
* **URL**: [https://t.me/zemenmotors](https://t.me/zemenmotors)
* **Category / Type**: EV dealership and aftersales supplier (Distributor / Supplier)
* **Access & Activity**: Accessible (Telegram channel & showrooms in Bole/Gotera) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Telegram Scraper / Manual (Feasible)
* **Initial Reliability Score**: 7.5/10
* **Decision**: **Use** — *Prominent distributor with direct daily market activity for target BYD vehicles*
* **Limitations**: Website is broken; relies 100% on Telegram feed and showroom staff

### `SRC-034`: Zemen Motors Telegram Channel (@zemenmotors)
* **URL**: [https://t.me/s/zemenmotors](https://t.me/s/zemenmotors)
* **Category / Type**: Dealership broadcast channel (Telegram)
* **Access & Activity**: Accessible (Web preview HTTP 200) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Telegram Scraper (Apify) (Feasible)
* **Initial Reliability Score**: 7.5/10
* **Decision**: **Use** — *High-volume channel with direct mentions of BYD Seagull and Yuan Up*
* **Limitations**: Posts mix new arrivals with promotional reposts; parts availability requires textual keyword filtering

### `SRC-035`: Abyssinia Car Sales Telegram (@Abyssiniancarsales)
* **URL**: [https://t.me/s/Abyssiniancarsales](https://t.me/s/Abyssiniancarsales)
* **Category / Type**: Automotive classifieds broadcast channel (Telegram)
* **Access & Activity**: Accessible (Web preview HTTP 200) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Telegram Scraper (Apify) (Feasible)
* **Initial Reliability Score**: 7.0/10
* **Decision**: **Use** — *Consistent stream of verified vehicle ads and customer price inquiries*
* **Limitations**: Broker-dominated; claims must be checked against duplicate listings

### `SRC-036`: Smart Car Market Telegram (@smartcarmarket)
* **URL**: [https://t.me/s/smartcarmarket](https://t.me/s/smartcarmarket)
* **Category / Type**: Multi-dealer vehicle & parts broadcast channel (Telegram)
* **Access & Activity**: Accessible (Web preview HTTP 200) | Active (Last observed: 2026-11-17)
* **Collection Method & Feasibility**: Telegram Scraper (Apify) (Feasible)
* **Initial Reliability Score**: 6.5/10
* **Decision**: **Use** — *Broad reach across Addis Ababa automotive brokers*
* **Limitations**: Occasional reposting of older ads

### `SRC-037`: Capital Car Market Telegram (@capitalcarmarket)
* **URL**: [https://t.me/s/capitalcarmarket](https://t.me/s/capitalcarmarket)
* **Category / Type**: Automotive marketplace channel (Telegram)
* **Access & Activity**: Accessible (Web preview HTTP 200) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Telegram Scraper (Apify) (Feasible)
* **Initial Reliability Score**: 6.5/10
* **Decision**: **Use** — *High posting velocity in Addis Ababa*
* **Limitations**: Parts posts are interspersed with general ICE car ads

### `SRC-038`: Ethio Car Dealers Telegram (@ethiocardealers)
* **URL**: [https://t.me/s/ethiocardealers](https://t.me/s/ethiocardealers)
* **Category / Type**: Broker network channel (Telegram)
* **Access & Activity**: Accessible (Web preview HTTP 200) | Active (Last observed: 2026-11-17)
* **Collection Method & Feasibility**: Telegram Scraper (Apify) (Feasible)
* **Initial Reliability Score**: 6.0/10
* **Decision**: **Use** — *Useful for tracking secondary retail pricing*
* **Limitations**: Broker commission ads; prices may be inflated over direct importer quotes

### `SRC-039`: Ethio Car Parts Network (@ethiocarparts)
* **URL**: [https://t.me/s/ethiocarparts](https://t.me/s/ethiocarparts)
* **Category / Type**: Specialized auto parts broadcast channel (Telegram)
* **Access & Activity**: Accessible (Web preview HTTP 200) | Stale (Last observed: 2025-12-10)
* **Collection Method & Feasibility**: Telegram Scraper (Apify) (Feasible)
* **Initial Reliability Score**: 4.5/10
* **Decision**: **Investigate** — *Check for historical spare parts price baselines*
* **Limitations**: Low posting frequency; predominantly ICE parts with occasional generic EV inquiries

### `SRC-040`: Ethiopian EV Community Group (@ev_ethiopia)
* **URL**: [https://t.me/s/ev_ethiopia](https://t.me/s/ev_ethiopia)
* **Category / Type**: Public EV owner discussion group (Customer community / Telegram)
* **Access & Activity**: Accessible (Web preview HTTP 200) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Manual / Apify (Partial)
* **Initial Reliability Score**: 7.0/10
* **Decision**: **Use** — *Primary source for genuine customer demand signals, repair complaints, and scarcity reports*
* **Limitations**: User experiences and informal claims; must be classified as customer demand observations rather than technical fitment

### `SRC-041`: TikTok Topic #EthiopiaEV
* **URL**: [https://www.tiktok.com/tag/ethiopiaev](https://www.tiktok.com/tag/ethiopiaev)
* **Category / Type**: Public short-form video topic & hashtag feed (Social media)
* **Access & Activity**: Accessible (Apify TikTok Actor) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Apify TikTok Scraper (Feasible)
* **Initial Reliability Score**: 6.5/10
* **Decision**: **Use** — *Fastest-growing platform for visual verification of incoming vehicle shipments and workshop procedures*
* **Limitations**: Content is heavily marketing-driven; comments require parsing for customer purchase and scarcity signals

### `SRC-042`: TikTok Topic #BYDEthiopia
* **URL**: [https://www.tiktok.com/tag/bydethiopia](https://www.tiktok.com/tag/bydethiopia)
* **Category / Type**: Brand-specific video hashtag (Social media)
* **Access & Activity**: Accessible (Apify TikTok Actor) | Active (Last observed: 2026-11-17)
* **Collection Method & Feasibility**: Apify TikTok Scraper (Feasible)
* **Initial Reliability Score**: 6.5/10
* **Decision**: **Use** — *Specific match for target BYD Seagull and BYD Yuan Up models*
* **Limitations**: Informal social environment; price quotes in comments must be corroborated

### `SRC-043`: TikTok Account @evtopia.et
* **URL**: [https://www.tiktok.com/@evtopia.et](https://www.tiktok.com/@evtopia.et)
* **Category / Type**: Commercial EV company TikTok channel (Social media)
* **Access & Activity**: Accessible | Active (Last observed: 2026-11-15)
* **Collection Method & Feasibility**: Apify TikTok Scraper / Manual (Feasible)
* **Initial Reliability Score**: 7.0/10
* **Decision**: **Use** — *Credible commercial EV brand providing regular informational updates*
* **Limitations**: Promotional channel; claims should be verified against physical stock

### `SRC-044`: TikTok Account @zemenmotors
* **URL**: [https://www.tiktok.com/@zemenmotors](https://www.tiktok.com/@zemenmotors)
* **Category / Type**: Dealership video storefront (Social media)
* **Access & Activity**: Accessible | Active (Last observed: 2026-11-16)
* **Collection Method & Feasibility**: Apify TikTok Scraper / Manual (Feasible)
* **Initial Reliability Score**: 6.5/10
* **Decision**: **Use** — *High buyer comment engagement suitable for comment scraping*
* **Limitations**: Video captions lack technical component numbers; comments contain rich buyer inquiries

### `SRC-045`: Ethiopian Customs Commission (ECC)
* **URL**: [https://www.ecc.gov.et/](https://www.ecc.gov.et/)
* **Category / Type**: Customs authority & import manifest registry (Government)
* **Access & Activity**: Accessible (SSL/Timeout issues on automated fetch; official gazette PDFs available) | Active (Last observed: 2026-10-15 (Tariff schedule update))
* **Collection Method & Feasibility**: Manual (Gazette PDFs & Tariff Books) (Blocked (Web server times out on direct python request))
* **Initial Reliability Score**: 9.5/10
* **Decision**: **Use** — *Statutory authority for import tariffs, customs duty rates, and dry port clearance processes*
* **Limitations**: Trade data aggregates automotive spare parts under general HS 8708 headings without vehicle model separation

### `SRC-046`: Ministry of Transport and Logistics (MoTL)
* **URL**: [https://www.motl.gov.et/](https://www.motl.gov.et/)
* **Category / Type**: Government transport ministry (Government)
* **Access & Activity**: Accessible (Requires SSL verify=False or manual browser fetch) | Active (Last observed: 2026-08-20)
* **Collection Method & Feasibility**: Manual (Policy documents) (Partial)
* **Initial Reliability Score**: 9.5/10
* **Decision**: **Use** — *Authoritative regulatory framework driving the entire Ethiopian EV import and parts mandate*
* **Limitations**: Strategic policy documents rather than real-time spare parts supply data

### `SRC-047`: Ministry of Finance (MoFED)
* **URL**: [https://www.mofed.gov.et/](https://www.mofed.gov.et/)
* **Category / Type**: Government finance ministry (Government)
* **Access & Activity**: Accessible (Manual PDF downloads) | Active (Last observed: 2024-12-01)
* **Collection Method & Feasibility**: Manual (Partial)
* **Initial Reliability Score**: 10.0/10
* **Decision**: **Use** — *Definitive legal foundation for the import profitability and tariff structure of EV components*
* **Limitations**: Fiscal tax code; does not track individual spare part import volumes

### `SRC-048`: Ethiopian Statistics Service (ESS / StatsEthiopia)
* **URL**: [https://www.statsethiopia.gov.et/](https://www.statsethiopia.gov.et/)
* **Category / Type**: National statistics institute (Government)
* **Access & Activity**: Accessible | Active (Last observed: 2025-11-30 (Annual Trade Bulletin))
* **Collection Method & Feasibility**: Manual (Statistical Tables) (Feasible)
* **Initial Reliability Score**: 8.5/10
* **Decision**: **Use** — *Macro baseline for Ethiopia-China automotive trade volumes*
* **Limitations**: Published with retrospective time lag; parts aggregated under broad HS codes

### `SRC-049`: National Bank of Ethiopia (NBE)
* **URL**: [https://nbe.gov.et/](https://nbe.gov.et/)
* **Category / Type**: Central bank & foreign exchange regulator (Government)
* **Access & Activity**: Accessible | Active (Last observed: 2026-07-28 (FX Directives))
* **Collection Method & Feasibility**: Manual (Feasible)
* **Initial Reliability Score**: 9.5/10
* **Decision**: **Use** — *Determines commercial importer forex access and LC approval feasibility for importing parts*
* **Limitations**: Financial monetary policy; no retail part references

### `SRC-050`: UN Comtrade International Trade Statistics
* **URL**: [https://comtradeplus.un.org/](https://comtradeplus.un.org/)
* **Category / Type**: Global United Nations trade database (Trade database)
* **Access & Activity**: Accessible (HTTP 200 / API available) | Active (Last observed: 2025-12-31)
* **Collection Method & Feasibility**: API / Manual Export (Feasible)
* **Initial Reliability Score**: 9.0/10
* **Decision**: **Use** — *Traceable international trade baseline verifying dollar volumes and metric tonnage entering Ethiopia*
* **Limitations**: Does not break down trade by individual car model or component SKU; represents macro trade reality

### `SRC-051`: World Bank WITS Trade Database
* **URL**: [https://wits.worldbank.org/](https://wits.worldbank.org/)
* **Category / Type**: Trade and tariff integration system (Trade database)
* **Access & Activity**: Accessible | Active (Last observed: 2025-12-31)
* **Collection Method & Feasibility**: Manual Export (Feasible)
* **Initial Reliability Score**: 8.5/10
* **Decision**: **Use** — *Cross-verifies Ethiopian customs tariff applications against global reporting*
* **Limitations**: Macro data only; broad commodity classifications

### `SRC-052`: BYD Global Parts & FinDreams EPC System
* **URL**: [https://www.byd.com/](https://www.byd.com/)
* **Category / Type**: Official manufacturer electronic parts catalogue (OEM catalogue)
* **Access & Activity**: Restricted (Dealer portal requires authorized login; public technical sheets accessible) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Manual (Blocked (Requires dealer credentials))
* **Initial Reliability Score**: 10.0/10
* **Decision**: **Use** — *Gold standard for verifying OEM part numbers, fitment, and inter-model compatibility*
* **Limitations**: Full EPC software requires authorized dealer access; reference part numbers must be extracted via verified distributor manuals

### `SRC-053`: Changan Global Automobile Parts
* **URL**: [https://globalchangan.com/](https://globalchangan.com/)
* **Category / Type**: Manufacturer parts & export portal (OEM catalogue)
* **Access & Activity**: Accessible | Active (Last observed: 2026-11-10)
* **Collection Method & Feasibility**: Manual (Partial)
* **Initial Reliability Score**: 9.5/10
* **Decision**: **Use** — *Definitive compatibility reference for Changan Benben E-Star*
* **Limitations**: Consumer retail ordering not available; serves as engineering and compatibility reference

### `SRC-054`: Toyota Global Electronic Parts Catalogue (EPC)
* **URL**: [https://toyota.epc-data.com/](https://toyota.epc-data.com/)
* **Category / Type**: Automotive OEM parts reference database (OEM catalogue)
* **Access & Activity**: Accessible (HTTP 200) | Active (Last observed: 2026-11-15)
* **Collection Method & Feasibility**: Scraper / Manual (Feasible)
* **Initial Reliability Score**: 9.5/10
* **Decision**: **Use** — *Enables exact cross-referencing of Toyota bZ4X wear parts and body panels*
* **Limitations**: International Japanese/European/Chinese spec variations require VIN check

### `SRC-055`: Amayama Trading OEM Auto Parts
* **URL**: [https://www.amayama.com/](https://www.amayama.com/)
* **Category / Type**: Direct OEM parts exporter (International exporter)
* **Access & Activity**: Accessible (HTTP 200) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Scraper / API (Feasible)
* **Initial Reliability Score**: 8.5/10
* **Decision**: **Use** — *High-reliability price and overseas sourcing benchmark for genuine Toyota parts*
* **Limitations**: Focused on Japanese brands (Toyota); limited direct coverage of Chinese domestic BYD/Changan parts

### `SRC-056`: PartSouq Auto Parts Around the World
* **URL**: [https://partsouq.com/](https://partsouq.com/)
* **Category / Type**: Middle East OEM parts exporter & hub (International exporter)
* **Access & Activity**: Restricted (Cloudflare HTTP 403 on automated fetch) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Manual (Blocked (Bot detection))
* **Initial Reliability Score**: 8.0/10
* **Decision**: **Use** — *Primary Middle East sourcing channel used by Ethiopian auto parts importers in Kera*
* **Limitations**: Automated requests blocked; requires manual query for specific part numbers

### `SRC-057`: Alibaba B2B EV Spare Parts Directory
* **URL**: [https://www.alibaba.com/](https://www.alibaba.com/)
* **Category / Type**: Global B2B wholesale platform (International exporter)
* **Access & Activity**: Accessible (Search endpoints active) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Scraper / Manual (Partial)
* **Initial Reliability Score**: 7.0/10
* **Decision**: **Use** — *Indispensable for sourcing feasibility, FOB unit cost benchmarking, and container shipping calculations*
* **Limitations**: Represents overseas supplier supply and FOB prices—must never be confused with Ethiopian local stock or domestic demand

### `SRC-058`: Made-in-China Automotive Components
* **URL**: [https://www.made-in-china.com/](https://www.made-in-china.com/)
* **Category / Type**: B2B export manufacturer directory (International exporter)
* **Access & Activity**: Accessible | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Scraper / Manual (Feasible)
* **Initial Reliability Score**: 7.0/10
* **Decision**: **Use** — *Direct access to tier-1 and aftermarket factories producing replacement parts for BYD and Changan*
* **Limitations**: Supplier claims must be verified; overseas supply only

### `SRC-059`: 1688 Chinese Domestic Sourcing Platform
* **URL**: [https://www.1688.com/](https://www.1688.com/)
* **Category / Type**: Domestic Chinese wholesale manufacturer network (Alibaba Group) (International exporter)
* **Access & Activity**: Restricted (Requires Chinese IP/session; search preview accessible) | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Manual (Blocked (Strict login and regional access barriers))
* **Initial Reliability Score**: 8.0/10
* **Decision**: **Investigate** — *Reflects the actual ground-floor procurement cost that Ethiopian parallel importers pay in China*
* **Limitations**: Interface in Chinese; access gated; requires manual inspection of sample items

### `SRC-060`: AliExpress Global Auto Parts
* **URL**: [https://www.aliexpress.com/](https://www.aliexpress.com/)
* **Category / Type**: B2C international direct parts shopping portal (International exporter)
* **Access & Activity**: Accessible | Active (Last observed: 2026-11-18)
* **Collection Method & Feasibility**: Scraper / Manual (Partial)
* **Initial Reliability Score**: 6.5/10
* **Decision**: **Use** — *Useful upper-bound price benchmark for emergency air-freight spare parts*
* **Limitations**: Consumer retail pricing with inflated individual air courier costs; does not reflect container bulk freight economics

### `SRC-061`: MegaZip Global Parts Hub
* **URL**: [https://www.megazip.net/](https://www.megazip.net/)
* **Category / Type**: OEM parts catalogue and international distributor (International exporter)
* **Access & Activity**: Accessible | Active (Last observed: 2026-11-17)
* **Collection Method & Feasibility**: Scraper / Manual (Feasible)
* **Initial Reliability Score**: 8.0/10
* **Decision**: **Use** — *Accurate schematic parts diagrams for cross-referencing wear parts*
* **Limitations**: Focuses on Japanese/US/EU market cataloguing; Chinese domestic BYD/Changan models absent
