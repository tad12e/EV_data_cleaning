"""Deduplicate multi-posted listings across platforms"""
import pandas as pd

def deduplicate_records(df):
    return df.drop_duplicates(subset=["listing_id", "part_name"])
