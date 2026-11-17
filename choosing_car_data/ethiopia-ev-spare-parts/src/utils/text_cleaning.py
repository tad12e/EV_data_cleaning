"""Text cleaning, Amharic transliteration, and regex helpers"""
import re

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"\s+", " ", text).strip()
    return text
