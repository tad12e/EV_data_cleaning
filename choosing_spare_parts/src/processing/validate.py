"""Validation rules for price outliers and verified phone numbers"""
import re

def validate_phone(phone_str):
    return bool(re.search(r"(?:\+?251|0)9[0-9]{8}", str(phone_str)))
