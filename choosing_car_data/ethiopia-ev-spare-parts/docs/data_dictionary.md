# Data Dictionary

### 1. `raw_marketplace_listings.csv`
- `listing_id` (str): Unique identifier for the listing (e.g. MKT-001).
- `platform` (str): Marketplace platform name (Jiji, Adey Market, Mekina).
- `source_url` (str): Direct link to the listing.
- `title` (str): Listing headline.
- `part_name` (str): Classified spare part name.
- `vehicle_model` (str): Target vehicle model.
- `price_etb` (float): Asking price in Ethiopian Birr.
- `seller_name` (str): Name or handle of the seller.
- `phone` (str): Verified contact number.
- `location` (str): Sub-city / city in Ethiopia.
- `post_date` (date): Date ad was published.

### 2. `import_priority_scores.csv`
- `priority_rank` (int): Ranked order of import urgency (1 to N).
- `part_name` (str): Standardized component taxonomy name.
- `target_vehicle` (str): Associated primary vehicle model.
- `demand_score` (float): 0-100 score reflecting replacement frequency and fleet volume.
- `scarcity_score` (float): 0-100 score reflecting shortage in local inventory.
- `failure_rate_score` (float): 0-100 score based on workshop failure reports.
- `final_import_priority_index` (float): Composite weighted prioritization score.
