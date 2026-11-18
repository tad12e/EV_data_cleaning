import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

# Set publication style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['grid.color'] = '#e0e0e0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.7

BASE_DIR = '/usr/local/share/colab/agy/EV_data_cleaning/choosing_spare_parts'
OUTPUT_DIR = os.path.join(BASE_DIR, 'reports/figures')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load datasets
summary_df = pd.read_csv(os.path.join(BASE_DIR, 'data/processed/vehicle_part_summary.csv'))
priority_df = pd.read_csv(os.path.join(BASE_DIR, 'data/processed/import_priority_scores.csv'))
sup_df = pd.read_csv(os.path.join(BASE_DIR, 'data/raw/suppliers/raw_supplier_evidence.csv'))
rep_df = pd.read_csv(os.path.join(BASE_DIR, 'data/raw/workshops/raw_repair_evidence.csv'))
mkt_df = pd.read_csv(os.path.join(BASE_DIR, 'data/processed/cleaned_marketplace_listings.csv'))

# Friendly category names mapping
CAT_NAMES = {
    'wiper_blades': 'Wiper Blades',
    'shock_absorbers': 'Shock Absorbers',
    'brake_pads': 'Brake Pads',
    'cabin_air_filters': 'Cabin-Air Filters',
    'brake_discs': 'Brake Discs',
    'bumpers': 'Bumpers',
    'side_mirrors': 'Side Mirrors',
    'headlights': 'Headlights',
    'fenders_body_panels': 'Fender / Body Panels',
    'tail_lights': 'Tail Lights'
}

# ==============================================================================
# FIGURE 1: demand_by_part.png
# ==============================================================================
print("Generating Figure 1: demand_by_part.png...")

# Aggregate demand & repairs across all vehicles for each part
part_agg = summary_df.groupby('part_category').agg({
    'repair_case_count': 'sum',
    'customer_request_count': 'sum',
    'price_enquiry_count': 'sum',
    'availability_enquiry_count': 'sum'
}).reset_index()

part_agg['customer_enquiries'] = (
    part_agg['customer_request_count'] + 
    part_agg['price_enquiry_count'] + 
    part_agg['availability_enquiry_count']
)
part_agg['total_signal'] = part_agg['repair_case_count'] + part_agg['customer_enquiries']
part_agg['part_name'] = part_agg['part_category'].map(CAT_NAMES)
part_agg = part_agg.sort_values('total_signal', ascending=True)

fig, ax = plt.subplots(figsize=(12, 7), dpi=300)
y_pos = np.arange(len(part_agg))
bar_height = 0.38

rects1 = ax.barh(y_pos + bar_height/2, part_agg['repair_case_count'], 
                 height=bar_height, label='Workshop Repair Cases (Empirical Volume)', 
                 color='#1A365D', edgecolor='#0F2942', linewidth=0.8, alpha=0.92)

rects2 = ax.barh(y_pos - bar_height/2, part_agg['customer_enquiries'], 
                 height=bar_height, label='Direct Customer Requests & Enquiries', 
                 color='#DD6B20', edgecolor='#C05621', linewidth=0.8, alpha=0.92)

# Value labels on bars
for rect in rects1:
    w = rect.get_width()
    if w > 0:
        ax.annotate(f'{int(w)}',
                    xy=(w, rect.get_y() + rect.get_height() / 2),
                    xytext=(5, 0), textcoords="offset points",
                    ha='left', va='center', fontsize=9.5, fontweight='bold', color='#1A365D')

for rect in rects2:
    w = rect.get_width()
    if w > 0:
        ax.annotate(f'{int(w)}',
                    xy=(w, rect.get_y() + rect.get_height() / 2),
                    xytext=(5, 0), textcoords="offset points",
                    ha='left', va='center', fontsize=9.5, fontweight='bold', color='#C05621')
    elif part_agg.iloc[int(rect.get_y() + bar_height/2)]['part_category'] == 'tail_lights':
        ax.annotate('0 (Gap)',
                    xy=(0, rect.get_y() + rect.get_height() / 2),
                    xytext=(5, 0), textcoords="offset points",
                    ha='left', va='center', fontsize=8.5, fontstyle='italic', color='#E53E3E')

ax.set_yticks(y_pos)
ax.set_yticklabels(part_agg['part_name'], fontsize=11, fontweight='semibold')
ax.set_xlabel('Empirical Count (Recorded Events in Addis Ababa)', fontsize=11, fontweight='bold', labelpad=10)
ax.set_xlim(0, 105)

# Title & Subtitle
plt.title('Customer Demand & Workshop Repair Cases Across 10 EV Spare-Part Categories', 
          fontsize=14, fontweight='bold', pad=25, loc='left')
plt.suptitle('Aggregated empirical records across Addis Ababa repair garages, fleet operators, and digital channels (Nov 2026)',
             fontsize=10.5, color='#4A5568', x=0.125, y=0.93, ha='left')

ax.legend(loc='lower right', frameon=True, facecolor='white', framealpha=0.95, fontsize=10.5)

# Insight box
ax.text(0.68, 0.35, 
        "Key Analytical Findings:\n"
        "• Fast-Wear Dominated: Wiper blades (90 cases),\n"
        "  shock absorbers (48), and brake pads (46).\n"
        "• Pothole Deterioration: Suspension struts suffer\n"
        "  accelerated failure from heavy EV battery mass.\n"
        "• Empirical Data Gap: Tail lights (0 recorded cases)\n"
        "  reflects severe reporting blindness in digital ads.",
        transform=ax.transAxes, fontsize=8.5, verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#F7FAFC', edgecolor='#CBD5E0', alpha=0.95))

# Footnote
fig.text(0.125, -0.02, 
         "Data Source: Task 4 Customer Demand Aggregation & Task 5 Workshop Repair Audits (Sarbet, Bole Medhanialem, Lideta Green Taxi).",
         fontsize=8.5, color='#718096', style='italic')

plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'demand_by_part.png'), dpi=300, bbox_inches='tight')
plt.close(fig)

# ==============================================================================
# FIGURE 2: demand_by_vehicle.png
# ==============================================================================
print("Generating Figure 2: demand_by_vehicle.png...")

veh_agg = summary_df.groupby('vehicle_model').agg({
    'customer_request_count': 'sum',
    'price_enquiry_count': 'sum',
    'availability_enquiry_count': 'sum',
    'repair_case_count': 'sum'
}).loc[['BYD Seagull', 'BYD Yuan Up', 'Changan Benben E-Star']].reset_index()

# Add fleet share context
fleet_info = {
    'BYD Seagull': {'share': '38% Fleet Share', 'role': 'Urban Hatchback (Commuter)'},
    'BYD Yuan Up': {'share': '22% Fleet Share', 'role': 'Compact Crossover (Family)'},
    'Changan Benben E-Star': {'share': '18% Fleet Share', 'role': 'Commercial Taxi / Ride-Hailing'}
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.5), dpi=300, gridspec_kw={'width_ratios': [1.8, 1]})

# Panel 1: Demand signal breakdown (Requests, Price Enquiries, Repair Cases)
x = np.arange(len(veh_agg))
width = 0.22

r1 = ax1.bar(x - width, veh_agg['customer_request_count'], width, 
             label='Customer Part Requests', color='#3182CE', edgecolor='#2B6CB0')
r2 = ax1.bar(x, veh_agg['price_enquiry_count'], width, 
             label='Price Enquiries', color='#DD6B20', edgecolor='#C05621')
r3 = ax1.bar(x + width, veh_agg['availability_enquiry_count'], width, 
             label='Availability Checks', color='#38A169', edgecolor='#2F855A')

# Annotations on bars
for bar_group in [r1, r2, r3]:
    for bar in bar_group:
        h = bar.get_height()
        if h > 0:
            ax1.annotate(f'{int(h)}',
                         xy=(bar.get_x() + bar.get_width() / 2, h),
                         xytext=(0, 3), textcoords="offset points",
                         ha='center', va='bottom', fontsize=9, fontweight='bold')

ax1.set_xticks(x)
ax1.set_xticklabels([f"{v}\n({fleet_info[v]['share']})" for v in veh_agg['vehicle_model']], 
                    fontsize=10.5, fontweight='bold')
ax1.set_ylabel('Direct Consumer Inquiries Count', fontsize=10.5, fontweight='bold')
ax1.set_ylim(0, 9)
ax1.set_title('A. Direct Consumer Inquiries Breakdown', fontsize=12, fontweight='bold', pad=12, loc='left')
ax1.legend(loc='upper right', frameon=True, facecolor='white', fontsize=9.5)

# Panel 2: Workshop Repair Case Counts
r_rep = ax2.bar(x, veh_agg['repair_case_count'], width=0.5, 
                color=['#2B6CB0', '#4A5568', '#C53030'], edgecolor='#1A202C', alpha=0.9)

for bar in r_rep:
    h = bar.get_height()
    ax2.annotate(f'{int(h)} cases',
                 xy=(bar.get_x() + bar.get_width() / 2, h),
                 xytext=(0, 4), textcoords="offset points",
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

ax2.set_xticks(x)
ax2.set_xticklabels(['Seagull', 'Yuan Up', 'Benben E-Star'], fontsize=10.5, fontweight='bold')
ax2.set_ylabel('Workshop Repair Cases', fontsize=10.5, fontweight='bold')
ax2.set_ylim(0, 155)
ax2.set_title('B. Workshop Repair Volume (Field Service)', fontsize=12, fontweight='bold', pad=12, loc='left')

# Inset text on Panel 2
ax2.text(0.05, 0.72, 
         "Commercial Taxi Intensity:\n"
         "Benben E-Star leads in repairs (132)\n"
         "despite smaller fleet share (18%)\n"
         "due to extreme daily taxi mileage\n"
         "(150-220 km/day on rough roads).",
         transform=ax2.transAxes, fontsize=8.5,
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF5F5', edgecolor='#FEB2B2'))

fig.suptitle('Spare Parts Demand Breakdown Across Target EV Models in Ethiopia', 
             fontsize=14, fontweight='bold', y=0.98, x=0.08, ha='left')

fig.text(0.08, -0.01,
         "Data Source: Aggregated multi-platform customer demand logs & physical EV workshop records (Addis Ababa, Nov 2026).",
         fontsize=8.5, color='#718096', style='italic')

plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'demand_by_vehicle.png'), dpi=300, bbox_inches='tight')
plt.close(fig)

# ==============================================================================
# FIGURE 3: marketplace_vs_supplier_stock.png
# ==============================================================================
print("Generating Figure 3: marketplace_vs_supplier_stock.png...")

# In marketplace listings: specific part counts vs general/broker ads
# In supplier evidence: verified in_stock vs orderable
mkt_counts = {
    'wiper_blades': 1,
    'shock_absorbers': 1,
    'brake_pads': 1,
    'cabin_air_filters': 2,
    'brake_discs': 5,
    'bumpers': 1,
    'side_mirrors': 5,
    'headlights': 2,
    'fenders_body_panels': 0,
    'tail_lights': 0
}

# Physical supplier audited stock
sup_in_stock = sup_df[sup_df['stock_status'] == 'in_stock'].groupby('part_category').size().to_dict()
sup_orderable = sup_df[sup_df['stock_status'] == 'orderable'].groupby('part_category').size().to_dict()

categories_ordered = [
    'wiper_blades', 'cabin_air_filters', 'brake_pads', 'brake_discs',
    'shock_absorbers', 'side_mirrors', 'headlights', 'bumpers',
    'fenders_body_panels', 'tail_lights'
]

plot_df = pd.DataFrame({
    'category': [CAT_NAMES[c] for c in categories_ordered],
    'mkt_listings': [mkt_counts.get(c, 0) for c in categories_ordered],
    'floor_stock': [sup_in_stock.get(c, 0) for c in categories_ordered],
    'orderable': [sup_orderable.get(c, 0) for c in categories_ordered]
})

fig, ax = plt.subplots(figsize=(13, 7), dpi=300)
x = np.arange(len(plot_df))
width = 0.26

b1 = ax.bar(x - width, plot_df['mkt_listings'], width, 
            label='Advertised Marketplace Listings (Classifieds / Telegram)', 
            color='#4A5568', edgecolor='#2D3748', alpha=0.9)
b2 = ax.bar(x, plot_df['floor_stock'], width, 
            label='Verified Physical Floor Stock (Immediate Showroom Availability)', 
            color='#2B6CB0', edgecolor='#1A365D', alpha=0.95)
b3 = ax.bar(x + width, plot_df['orderable'], width, 
            label='Pre-Order Only at Suppliers (10–30 Days Lead Time)', 
            color='#C53030', edgecolor='#9B2C2C', alpha=0.9)

for b_group in [b1, b2, b3]:
    for b in b_group:
        h = b.get_height()
        if h > 0:
            ax.annotate(f'{int(h)}',
                        xy=(b.get_x() + b.get_width() / 2, h),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(plot_df['category'], rotation=28, ha='right', fontsize=10, fontweight='semibold')
ax.set_ylabel('Number of Verified Observations / Records', fontsize=11, fontweight='bold')
ax.set_ylim(0, 7)

# Title & Subtitle
plt.title('Marketplace Digital Footprint vs. Verified Physical Supplier Inventory', 
          fontsize=14, fontweight='bold', pad=25, loc='left')
plt.suptitle('Demonstrating severe market asymmetry: online brokers advertise listings, but physical showroom shelves remain empty',
             fontsize=10.5, color='#4A5568', x=0.125, y=0.93, ha='left')

ax.legend(loc='upper right', frameon=True, facecolor='white', framealpha=0.95, fontsize=10)

# Highlight structural vs fast wear
ax.axvspan(-0.5, 3.5, color='#EDF2F7', alpha=0.5, zorder=0)
ax.text(1.5, 6.2, "Wear Consumables Zone\n(High floor stock, fast turn)", 
        ha='center', fontsize=9, fontweight='bold', color='#2B6CB0',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#CBD5E0'))

ax.axvspan(3.5, 9.5, color='#FFF5F5', alpha=0.5, zorder=0)
ax.text(6.5, 6.2, "Structural & Optical Bottleneck Zone\n(Floor stock near zero; pre-order mandatory)", 
        ha='center', fontsize=9, fontweight='bold', color='#C53030',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#FEB2B2'))

fig.text(0.125, -0.04, 
         "Data Source: Task 3 (Jiji, Adey Market, AfroMekina listings) vs Task 5 Physical Supplier Audits (Sunny Spares, SARA Import, Markon, Lideta). Note: 69 generic/brokered marketplace ads omitted.",
         fontsize=8.5, color='#718096', style='italic')

plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'marketplace_vs_supplier_stock.png'), dpi=300, bbox_inches='tight')
plt.close(fig)

# ==============================================================================
# FIGURE 4: scarcity_matrix.png
# ==============================================================================
print("Generating Figure 4: scarcity_matrix.png...")

# Scarcity metrics per part
scarcity_data = [
    {'part': 'Wiper Blades', 'wait_days': 0.5, 'stock_avail_pct': 100, 'air_lead': 8, 'sea_lead': 32, 'scarcity_score': 15.0, 'tier': 'Low Scarcity', 'cases': 90},
    {'part': 'Cabin-Air Filters', 'wait_days': 1.0, 'stock_avail_pct': 100, 'air_lead': 8, 'sea_lead': 35, 'scarcity_score': 15.0, 'tier': 'Low Scarcity', 'cases': 42},
    {'part': 'Brake Pads', 'wait_days': 1.5, 'stock_avail_pct': 80, 'air_lead': 10, 'sea_lead': 38, 'scarcity_score': 45.0, 'tier': 'Moderate Scarcity', 'cases': 46},
    {'part': 'Brake Discs', 'wait_days': 3.5, 'stock_avail_pct': 75, 'air_lead': 12, 'sea_lead': 40, 'scarcity_score': 45.0, 'tier': 'Moderate Scarcity', 'cases': 22},
    {'part': 'Shock Absorbers', 'wait_days': 14.0, 'stock_avail_pct': 50, 'air_lead': 14, 'sea_lead': 38, 'scarcity_score': 72.0, 'tier': 'High Scarcity', 'cases': 48},
    {'part': 'Side Mirrors', 'wait_days': 20.0, 'stock_avail_pct': 25, 'air_lead': 12, 'sea_lead': 35, 'scarcity_score': 85.0, 'tier': 'High Scarcity', 'cases': 14},
    {'part': 'Bumpers', 'wait_days': 25.0, 'stock_avail_pct': 25, 'air_lead': 18, 'sea_lead': 40, 'scarcity_score': 88.0, 'tier': 'High Scarcity', 'cases': 19},
    {'part': 'Fenders / Body', 'wait_days': 35.0, 'stock_avail_pct': 0, 'air_lead': 20, 'sea_lead': 42, 'scarcity_score': 95.0, 'tier': 'Critical Bottleneck', 'cases': 8},
    {'part': 'Tail Lights', 'wait_days': 22.0, 'stock_avail_pct': 0, 'air_lead': 15, 'sea_lead': 38, 'scarcity_score': 92.0, 'tier': 'Critical Bottleneck', 'cases': 1},
    {'part': 'Headlights', 'wait_days': 42.5, 'stock_avail_pct': 20, 'air_lead': 14, 'sea_lead': 40, 'scarcity_score': 98.0, 'tier': 'Critical Bottleneck', 'cases': 9}
]
sc_df = pd.DataFrame(scarcity_data)

fig, (ax_mat, ax_quad) = plt.subplots(1, 2, figsize=(15, 7.5), dpi=300, gridspec_kw={'width_ratios': [1.1, 1.3]})

# Panel 1: Heatmap of Supply Chain Metrics
mat_data = sc_df.set_index('part')[['stock_avail_pct', 'wait_days', 'air_lead', 'sea_lead', 'scarcity_score']]
mat_data.columns = ['Floor Stock (%)', 'Workshop Wait (d)', 'Air Freight (d)', 'Sea Freight (d)', 'Scarcity Score']

sns.heatmap(mat_data, annot=True, fmt='.1f', cmap='YlOrRd', cbar=False, ax=ax_mat,
            linewidths=1, linecolor='white', annot_kws={'fontsize': 9.5, 'fontweight': 'bold'})
ax_mat.set_title('A. Operational Lead Times & Scarcity Metrics', fontsize=12, fontweight='bold', pad=12, loc='left')
ax_mat.set_ylabel('')
ax_mat.set_yticklabels(ax_mat.get_yticklabels(), fontsize=10, fontweight='bold')
ax_mat.set_xticklabels(ax_mat.get_xticklabels(), fontsize=9.5, fontweight='semibold', rotation=25, ha='right')

# Panel 2: Quadrant Chart (Wait Time vs Scarcity Score)
colors = {'Low Scarcity': '#38A169', 'Moderate Scarcity': '#3182CE', 'High Scarcity': '#DD6B20', 'Critical Bottleneck': '#E53E3E'}

for tier, group in sc_df.groupby('tier'):
    ax_quad.scatter(group['wait_days'], group['scarcity_score'], 
                    s=group['cases']*12 + 80, color=colors[tier], label=tier, 
                    alpha=0.85, edgecolors='black', linewidth=1.2)

for _, row in sc_df.iterrows():
    offset_y = 2.5 if row['part'] != 'Fenders / Body' else -4.0
    ax_quad.annotate(row['part'], (row['wait_days'], row['scarcity_score']),
                     xytext=(4, offset_y), textcoords='offset points',
                     fontsize=9, fontweight='semibold', color='#2D3748')

# Quadrant dividing lines
ax_quad.axvline(10, color='#A0AEC0', linestyle=':', linewidth=1.5)
ax_quad.axhline(60, color='#A0AEC0', linestyle=':', linewidth=1.5)

# Quadrant background labels
ax_quad.text(1, 10, "SAFE STOCK ZONE\n(Immediate local fulfillment)", fontsize=8.5, color='#2F855A', fontweight='bold')
ax_quad.text(1, 93, "FAST TRANSIT GAP\n(High scarcity, short wait)", fontsize=8.5, color='#DD6B20', fontweight='bold')
ax_quad.text(28, 10, "TRANSITIONAL / DELAYED\n(Moderate volume)", fontsize=8.5, color='#4A5568', fontweight='bold')
ax_quad.text(28, 93, "CRITICAL BOTTLENECK ZONE\n(Zero stock, >20d lead times)", fontsize=8.5, color='#C53030', fontweight='bold')

ax_quad.set_xlabel('Average Customer Waiting Period / Lead Time (Days)', fontsize=10.5, fontweight='bold')
ax_quad.set_ylabel('Calculated Component Scarcity Score (0–100)', fontsize=10.5, fontweight='bold')
ax_quad.set_xlim(-2, 48)
ax_quad.set_ylim(0, 108)
ax_quad.set_title('B. Scarcity vs. Fulfillment Delay Quadrant (Bubble Size = Repair Volume)', 
                  fontsize=12, fontweight='bold', pad=12, loc='left')
ax_quad.legend(loc='lower right', frameon=True, facecolor='white', fontsize=9.5)

fig.suptitle('Ethiopian EV Spare Parts Scarcity & Sourcing Lead Time Matrix', 
             fontsize=14, fontweight='bold', y=0.98, x=0.08, ha='left')

fig.text(0.08, -0.01,
         "Data Source: Task 5 Workshop Repair Audits (Sarbet, Bole, Lideta) & Chinese Sourcing Inquiries (Guangzhou, Shenzhen, Changsha).",
         fontsize=8.5, color='#718096', style='italic')

plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'scarcity_matrix.png'), dpi=300, bbox_inches='tight')
plt.close(fig)

# ==============================================================================
# FIGURE 5: price_comparison_boxplots.png
# ==============================================================================
print("Generating Figure 5: price_comparison_boxplots.png...")

# Price comparison dataset (ETB)
# Reference exchange rate: ~125 ETB / USD
# Landed cost includes FOB + International Freight + 5% EV customs duty + port handling
price_data = [
    {'part': 'Cabin-Air Filters', 'fob_etb': 375, 'landed_etb': 550, 'retail_min': 2500, 'retail_med': 3800, 'retail_max': 4200, 'margin': '85%'},
    {'part': 'Wiper Blades', 'fob_etb': 420, 'landed_etb': 700, 'retail_min': 1800, 'retail_med': 2800, 'retail_max': 3200, 'margin': '75%'},
    {'part': 'Brake Pads', 'fob_etb': 1900, 'landed_etb': 2500, 'retail_min': 7500, 'retail_med': 9200, 'retail_max': 10500, 'margin': '73%'},
    {'part': 'Brake Discs', 'fob_etb': 2750, 'landed_etb': 4300, 'retail_min': 11500, 'retail_med': 14500, 'retail_max': 28000, 'margin': '70%'},
    {'part': 'Side Mirrors', 'fob_etb': 5000, 'landed_etb': 9300, 'retail_min': 14000, 'retail_med': 26500, 'retail_max': 29500, 'margin': '65%'},
    {'part': 'Front Bumpers', 'fob_etb': 4125, 'landed_etb': 8800, 'retail_min': 31000, 'retail_med': 34000, 'retail_max': 39000, 'margin': '74%'},
    {'part': 'Shock Absorbers', 'fob_etb': 4375, 'landed_etb': 6300, 'retail_min': 38000, 'retail_med': 42000, 'retail_max': 48000, 'margin': '85%'},
    {'part': 'Fenders / Panels', 'fob_etb': 4500, 'landed_etb': 6500, 'retail_min': 18000, 'retail_med': 21000, 'retail_max': 24000, 'margin': '69%'},
    {'part': 'Tail Lights', 'fob_etb': 12500, 'landed_etb': 16200, 'retail_min': 28000, 'retail_med': 31000, 'retail_max': 34000, 'margin': '48%'},
    {'part': 'LED Headlights', 'fob_etb': 15900, 'landed_etb': 20200, 'retail_min': 27500, 'retail_med': 46500, 'retail_max': 52000, 'margin': '57%'}
]
p_comp = pd.DataFrame(price_data).sort_values('retail_med', ascending=True)

fig, ax = plt.subplots(figsize=(13, 8), dpi=300)
y = np.arange(len(p_comp))
h = 0.26

r_fob = ax.barh(y + h, p_comp['fob_etb'], h, label='Chinese Factory FOB Price (USD converted to ETB @ 125)', 
                color='#3182CE', edgecolor='#2B6CB0', alpha=0.9)
r_landed = ax.barh(y, p_comp['landed_etb'], h, label='Estimated Landed Cost in Addis Ababa (Freight + 5% Duty + Port)', 
                   color='#DD6B20', edgecolor='#C05621', alpha=0.9)
r_retail = ax.barh(y - h, p_comp['retail_med'], h, label='Local Quoted Retail Price in Addis Ababa (Median)', 
                   color='#C53030', edgecolor='#9B2C2C', alpha=0.95)

# Error whiskers for retail price range
xerr_low = p_comp['retail_med'] - p_comp['retail_min']
xerr_high = p_comp['retail_max'] - p_comp['retail_med']
ax.errorbar(p_comp['retail_med'], y - h, xerr=[xerr_low, xerr_high], fmt='none', 
            ecolor='#1A202C', elinewidth=1.5, capsize=4, capthick=1.5)

# Annotate gross margins
for idx, row in p_comp.reset_index().iterrows():
    ax.annotate(f" {row['retail_med']:,} ETB (Gross Margin: {row['margin']})",
                xy=(row['retail_max'], idx - h),
                xytext=(6, 0), textcoords="offset points",
                ha='left', va='center', fontsize=9, fontweight='bold', color='#C53030')

ax.set_yticks(y)
ax.set_yticklabels(p_comp['part'], fontsize=11, fontweight='semibold')
ax.set_xlabel('Price in Ethiopian Birr (ETB)', fontsize=11, fontweight='bold', labelpad=10)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{int(x):,}'))
ax.set_xlim(0, 68000)

plt.title('Price Comparison: Chinese FOB vs. Landed Cost vs. Addis Ababa Retail Quoted Price', 
          fontsize=14, fontweight='bold', pad=25, loc='left')
plt.suptitle('Illustrating high importer gross margins (48%–85%) driven by local component scarcity and parallel markup',
             fontsize=10.5, color='#4A5568', x=0.125, y=0.93, ha='left')

ax.legend(loc='lower right', frameon=True, facecolor='white', framealpha=0.95, fontsize=10)

fig.text(0.125, -0.02, 
         "Data Source: Task 5 Chinese OEM Factory Inquiries (FOB USD) vs Ethiopian Supplier Price Quotes (ETB, Nov 2026). Whiskers denote min/max quotes.",
         fontsize=8.5, color='#718096', style='italic')

plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'price_comparison_boxplots.png'), dpi=300, bbox_inches='tight')
plt.close(fig)

# ==============================================================================
# FIGURE 6: priority_ranking_heatmap.png
# ==============================================================================
print("Generating Figure 6: priority_ranking_heatmap.png...")

# Reshape priority scores into 10 x 3 matrix
pivot_df = priority_df.pivot(index='part_category', columns='vehicle_model', values='total_priority_score')
pivot_conf = priority_df.pivot(index='part_category', columns='vehicle_model', values='confidence_level')

# Reorder indices and columns
row_order = [
    'shock_absorbers', 'headlights', 'side_mirrors', 'bumpers', 'brake_pads',
    'fenders_body_panels', 'brake_discs', 'cabin_air_filters', 'wiper_blades', 'tail_lights'
]
col_order = ['BYD Seagull', 'BYD Yuan Up', 'Changan Benben E-Star']

pivot_df = pivot_df.reindex(index=row_order, columns=col_order)
pivot_conf = pivot_conf.reindex(index=row_order, columns=col_order)

fig, ax = plt.subplots(figsize=(11, 9), dpi=300)

# Custom diverging/sequential color palette
cmap = sns.color_palette("YlOrRd", as_cmap=True)

sns.heatmap(pivot_df, annot=False, cmap=cmap, cbar=True, vmin=20, vmax=95,
            linewidths=1.5, linecolor='#E2E8F0', ax=ax,
            cbar_kws={'label': 'Total Import Priority Score (0–100)', 'shrink': 0.8})

# Overlay text: Score + Confidence tag
for i in range(len(row_order)):
    for j in range(len(col_order)):
        val = pivot_df.iloc[i, j]
        conf = pivot_conf.iloc[i, j]
        
        # Determine text color based on background darkness
        text_color = 'white' if val >= 75 else '#1A202C'
        
        if conf == 'Insufficient Evidence':
            conf_str = '[DATA GAP]'
            text_color = '#742A2A'
            # Add subtle hatch pattern
            ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, hatch='///', 
                                       edgecolor='#E53E3E', linewidth=1.5, zorder=3))
        elif conf == 'High':
            conf_str = '[High Conf]'
        elif conf == 'Medium':
            conf_str = '[Med Conf]'
        else:
            conf_str = '[Low Conf]'
            
        ax.text(j + 0.5, i + 0.42, f'{val:.1f}', 
                ha='center', va='center', fontsize=11, fontweight='bold', color=text_color, zorder=4)
        ax.text(j + 0.5, i + 0.68, conf_str, 
                ha='center', va='center', fontsize=8.5, fontweight='semibold', color=text_color, zorder=4)

ax.set_yticklabels([CAT_NAMES[c] for c in row_order], fontsize=11, fontweight='semibold')
ax.set_xticklabels(['BYD Seagull\n(38% Fleet Share)', 'BYD Yuan Up\n(22% Fleet Share)', 'Changan Benben E-Star\n(18% Fleet Share)'], 
                   fontsize=11, fontweight='bold')
ax.set_ylabel('')
ax.set_xlabel('')

plt.title('30-Combination EV Spare Parts Import Priority & Evidence Confidence Matrix', 
          fontsize=13.5, fontweight='bold', pad=25, loc='left')
plt.suptitle('Synthesizing Demand (30%), Scarcity (25%), Compatibility (20%), Feasibility (15%), and Reliability (10%)',
             fontsize=10, color='#4A5568', x=0.125, y=0.93, ha='left')

# Strategic insight legend
fig.text(0.125, -0.05,
         "Decision Framework & Confidence Tiering:\n"
         "• Score ≥ 80.0 [High Conf]: Top Strategic Priority — Immediate Sea/Air bulk procurement (BYD Pads/Mirrors/Struts, Benben Bumpers).\n"
         "• Score 65.0–79.9 [High Conf]: Routine Wear Baseline — High turnover, low margin risk (Cabin filters, Wiper blades, Brake discs).\n"
         "• [DATA GAP] (Hatched): Zero direct local observations — Pending physical dealer audit; NEVER interpreted as zero demand.",
         fontsize=8.5, color='#2D3748', bbox=dict(boxstyle='round,pad=0.5', facecolor='#F7FAFC', edgecolor='#CBD5E0'))

plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'priority_ranking_heatmap.png'), dpi=300, bbox_inches='tight')
plt.close(fig)

print("All 6 figures successfully generated in", OUTPUT_DIR)
