"""Classify raw text into vehicle models and spare part taxonomy"""
import re

def classify_text(text):
    part = "Generic EV Component"
    if re.search(r"shock|strut|አማርቲዛተር", text, re.I):
        part = "Front Suspension Strut"
    elif re.search(r"obc|charger|ቻርጀር", text, re.I):
        part = "On-Board Charger (OBC)"
    elif re.search(r"compressor|ኮምፕረሰር", text, re.I):
        part = "Electric AC Compressor"
    return part
