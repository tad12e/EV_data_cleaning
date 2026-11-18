# Explicit Research Assumptions & Operational Hypotheses

**Project**: Ethiopian EV Spare-Parts Demand & Import Opportunity Research Pipeline  
**Module**: `choosing_spare_parts/`  
**Last Updated**: November 2026 (Task 2 Complete)  

---

## 1. Automotive Engineering & Maintenance Assumptions
1. **Regenerative Braking Friction Reduction**: Electric vehicles utilize regenerative braking, which reduces friction pad wear by 40–50% compared to equivalent ICE vehicles. Brake pad replacement is modeled at 30,000–45,000 km, but brake discs suffer premature corrosion/warping in wet rainy seasons due to underutilization.
2. **Rough Road Infrastructure Acceleration**: Operating on uneven asphalt and cobblestone corridors in Addis Ababa accelerates failure of suspension struts, bushings, and shock absorbers, making shock absorbers a high-frequency replacement despite relatively young vehicle fleet ages.
3. **Severe Particulate Dust Conditions**: Elevated dust levels and construction activity in Addis Ababa require cabin-air filter replacement every 10,000–15,000 km (substantially faster than European/Chinese OEM guidelines of 20,000–30,000 km).
4. **Collision Damage Vulnerability**: Congested urban traffic in Addis Ababa produces high frequency of low-speed bumper collisions, fender scrapes, and side mirror impacts, driving high replacement demand for exterior cosmetic parts.

---

## 2. Market Structure & Channel Behavior Assumptions
1. **Digital Footprint vs. Physical Trade**: Dealerships and workshops in Addis Ababa conduct ~80% of business via direct phone inquiries, walk-ins, and Telegram, rather than maintaining automated e-commerce web stock counters.
2. **Zero-Inventory Default**: Because live stock numbers are unmetered on Ethiopian dealership websites, verified inventory counts are set to `0` or flagged as unconfirmed unless supported by an in-person workshop inspection or direct phone quotation.
3. **Order-to-Delivery Lead Times**: Spare parts sourced via standard maritime container shipping through Djibouti require 4–8 weeks; emergency air freight parts through Ethiopian Airlines Cargo require 7–14 days at significantly higher landed cost.
4. **Foreign Exchange (FX) Access**: Importers with access to National Bank of Ethiopia (NBE) green mobility priority forex allocations or export retention accounts face lower landed landed costs than parallel importers forced to source currency on secondary markets.

---

## 3. Data Representation Assumptions
1. **Advertised Volume vs. Actual Sales**: Classified vehicle listings reflect marketing presence and inventory velocity, not total vehicle registrations or road populations.
2. **Missing Search Evidence**: A zero-result search for a specific spare part in Ethiopian channels indicates that local digital advertising is absent, **not that EV owners do not require the part**.
3. **International Sourcing Equivalency**: Chinese OEM component pricing (FOB Shanghai/Ningbo in RMB/USD) provides the technical floor price for parts, but must be adjusted by 15% customs tariff, maritime freight, port handling, and domestic transport to calculate landed cost in Addis Ababa.
