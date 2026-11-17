"""Date parsing and normalization utilities"""
from datetime import datetime

def parse_iso_date(date_str):
    try:
        return datetime.fromisoformat(date_str)
    except Exception:
        return datetime.now()
