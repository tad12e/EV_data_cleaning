# Ethiopia EV Spare Parts Intelligence & Supply Chain Analysis

An end-to-end framework for data ingestion, cleaning, demand-supply gap analysis, and import prioritization of Electric Vehicle (EV) spare parts and maintenance components in Ethiopia.

## Overview
As Ethiopia transitions rapidly toward electric mobility following the Ministry of Transport and Logistics (MoTL) internal combustion engine (ICE) import ban and Ministry of Finance (MoFED) tax exemptions, vehicle reliability depends heavily on the aftermarket spare parts ecosystem.

This repository tracks:
1. Market listing availability across Ethiopian classifieds (Jiji, Adey Market, Mekina).
2. Field repair evidence from specialized EV workshops (Kera, Saris, Bole).
3. Social media sentiment & customer inquiries (Telegram channels, TikTok reviews).
4. Official customs & Port of Djibouti trade flow data.

## Project Structure
- `config/`: System YAML configuration for vehicles, parts taxonomy, keywords, and endpoints.
- `data/`: Raw, processed, and reference data layers.
- `notebooks/`: Step-by-step exploratory, cleaning, and modeling Jupyter Notebooks.
- `src/`: Production-ready Python pipeline modules for ingestion, processing, analysis, and utilities.
- `reports/`: Executive recommendations, summary tables, and visualizations.
- `docs/`: Methodological specifications, data dictionary, reliability matrices, and limitations.

## Quick Start
```bash
pip install -r requirements.txt
cp .env.example .env
python -m src.collectors.telegram
python -m src.processing.normalize
python -m src.analysis.scoring
```
