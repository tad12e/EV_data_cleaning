"""Deduplication and Cluster Identification Engine
Module: choosing_spare_parts/src/processing/deduplicate.py
Identifies exact duplicates, repeated advertisements, cross-platform reposts,
and repeated supplier claims without discarding raw observations.
Conforms to Master Prompt Section 6.4.
"""

import re
import hashlib
import logging
from typing import List, Dict, Any
import pandas as pd

logger = logging.getLogger("deduplicate_engine")

BOILERPLATE_PATTERNS = [
    r"skip to content", r"adeymarket", r"adey market", r"all categories",
    r"phones computers cars", r"sell on adey market", r"copy link",
    r"open the post on telegram", r"call \+251", r"share · ያጋሩ",
    r"no photo in the post", r"spare parts & tires", r"not available"
]

def clean_text_for_clustering(text: str) -> str:
    """Removes website navigation boilerplate, punctuation, excess whitespace, and lowercases text."""
    if not isinstance(text, str):
        return ""
    t = text.lower()
    for b in BOILERPLATE_PATTERNS:
        t = re.sub(b, " ", t)
    cleaned = re.sub(r"[^\w\s\u1200-\u137F]", " ", t)
    return " ".join(cleaned.split())

def deduplicate_dataframe(df: pd.DataFrame, text_col: str = "observation") -> pd.DataFrame:
    """Assigns duplicate_group_id, is_duplicate, duplicate_type, deduplication_method,
    and deduplication_confidence across records while maintaining all original rows.
    """
    df = df.copy()

    # Initialize deduplication fields
    df["duplicate_group_id"] = ""
    df["is_duplicate"] = False
    df["duplicate_type"] = "primary_record"
    df["deduplication_method"] = "none"
    df["deduplication_confidence"] = 1.0

    seen_exact_hashes: Dict[str, str] = {}    # exact_hash -> group_id
    seen_urls: Dict[str, str] = {}            # exact_url -> group_id
    seen_semantic_keys: Dict[str, str] = {}   # semantic_key -> group_id
    group_counter = 1

    for idx, row in df.iterrows():
        raw_text = str(row.get(text_col, "")).strip()
        cleaned_text = clean_text_for_clustering(raw_text)

        vehicle = str(row.get("vehicle_model", "")).strip().lower()
        part = str(row.get("part_category", "")).strip().lower()
        price = str(row.get("price", "")).strip()
        seller = str(row.get("source_name", "")).strip().lower()
        url = str(row.get("source_url", "")).strip()

        # 1. Exact text hash
        exact_hash = hashlib.md5(raw_text.encode("utf-8")).hexdigest()[:12]

        # 2. Semantic Cluster Key: Combines vehicle, part, rounded price, and key words
        meaningful_tokens = [w for w in cleaned_text.split() if len(w) > 3][:6]
        semantic_key = f"{vehicle}_{part}_{price}_{'_'.join(meaningful_tokens)}"

        # Check Exact Duplicate (Identical non-trivial raw text)
        if raw_text and raw_text.lower() not in ["", "nan", "none", "null"] and len(raw_text) > 10 and exact_hash in seen_exact_hashes:
            gid = seen_exact_hashes[exact_hash]
            df.at[idx, "duplicate_group_id"] = gid
            df.at[idx, "is_duplicate"] = True
            df.at[idx, "duplicate_type"] = "exact_duplicate"
            df.at[idx, "deduplication_method"] = "exact_hash_match"
            df.at[idx, "deduplication_confidence"] = 1.0
            continue

        # Check URL Duplicate (Identical listing URL captured multiple times)
        if url and url not in ["nan", "None", "", "http://", "https://"] and len(url) > 10 and url in seen_urls:
            gid = seen_urls[url]
            df.at[idx, "duplicate_group_id"] = gid
            df.at[idx, "is_duplicate"] = True
            df.at[idx, "duplicate_type"] = "repeated_advertisement"
            df.at[idx, "deduplication_method"] = "url_match"
            df.at[idx, "deduplication_confidence"] = 0.95
            continue

        # Check Cross-Platform / Repeated Advertisement Semantic Cluster
        if meaningful_tokens and len(meaningful_tokens) >= 3 and semantic_key in seen_semantic_keys:
            gid = seen_semantic_keys[semantic_key]
            df.at[idx, "duplicate_group_id"] = gid
            df.at[idx, "is_duplicate"] = True
            df.at[idx, "duplicate_type"] = "cross_platform_repost" if "marketplace" in str(row.get("source_dataset", "")) else "repeated_advertisement"
            df.at[idx, "deduplication_method"] = "semantic_feature_clustering"
            df.at[idx, "deduplication_confidence"] = 0.88
            continue

        # Unique primary record
        new_gid = f"GRP-{group_counter:05d}"
        group_counter += 1

        if raw_text:
            seen_exact_hashes[exact_hash] = new_gid
        if url and url != "nan" and url != "None":
            seen_urls[url] = new_gid
        if meaningful_tokens:
            seen_semantic_keys[semantic_key] = new_gid

        df.at[idx, "duplicate_group_id"] = new_gid
        df.at[idx, "is_duplicate"] = False
        df.at[idx, "duplicate_type"] = "primary_record"
        df.at[idx, "deduplication_method"] = "unique_observation"
        df.at[idx, "deduplication_confidence"] = 1.0

    dup_count = df["is_duplicate"].sum()
    logger.info(f"Deduplication finished: {dup_count} duplicate records flagged across {group_counter-1} unique groups out of {len(df)} total.")
    return df
