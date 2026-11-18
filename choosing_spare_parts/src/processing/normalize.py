"""Vehicle and Spare Part Normalization Engine
Module: choosing_spare_parts/src/processing/normalize.py
Standardizes vehicle models, brands, trims, multilingual terms, and spare-part categories.
Extracts component positions (front/rear/left/right) and component types (assembly vs element).
Conforms to Master Prompt Section 6.2 & 6.3 and project configuration YAMLs.
"""

import re
import os
import logging
from typing import Dict, Tuple, Optional

logger = logging.getLogger("normalize_engine")

# Target standard vehicles
STANDARD_VEHICLES = {
    "BYD Seagull": {
        "brand": "BYD",
        "patterns": [
            r"\bseagull\b", r"\bsegull\b", r"\bsea-gull\b", r"\bdolphin\s*mini\b",
            r"比亚迪海鸥", r"海鸥", r"ሲጋል", r"ቢዋይዲ\s*ሲጋል", r"ዶልፊን\s*ሚኒ"
        ],
        "forbidden": [r"\bdolphin\b(?!\s*mini)", r"\batto\s*3\b", r"\bseal\b", r"\bsong\b"]
    },
    "BYD Yuan Up": {
        "brand": "BYD",
        "patterns": [
            r"\byuan\s*up\b", r"\byuanup\b", r"\byuan-up\b", r"比亚迪元\s*up",
            r"元\s*up", r"ዩዋን\s*አፕ", r"ዩዋን\s*አፕ"
        ],
        "forbidden": [r"\byuan\s*plus\b", r"\batto\s*3\b", r"\bhan\b", r"\btang\b"]
    },
    "Changan Benben E-Star": {
        "brand": "Changan",
        "patterns": [
            r"\bbenben\b", r"\be-star\b", r"\bestar\b", r"\bben\s*ben\b",
            r"长安奔奔", r"奔奔e-star", r"奔奔", r"ቤንቤን", r"ኢ-ስታር"
        ],
        "forbidden": [r"\bdeepal\b", r"\bchangan\s*cs\b", r"\buni-k\b", r"\buni-v\b"]
    }
}

# 10 Standard Spare Part Categories
STANDARD_PARTS = {
    "brake_pads": {
        "standard_name": "Brake pads",
        "patterns": [
            r"brake\s*pad", r"brake\s*pads", r"braking\s*pad", r"break\s*pad", r"break\s*pads",
            r"disc\s*pad", r"brake\s*shoe", r"brake\s*lining", r"የፍሬን\s*ፓድ", r"ፍሬን\s*ፓድ",
            r"የፍሬን\s*ታኮ", r"刹车片", r"前刹车片", r"后刹车片"
        ]
    },
    "brake_discs": {
        "standard_name": "Brake discs",
        "patterns": [
            r"brake\s*disc", r"brake\s*discs", r"brake\s*disk", r"brake\s*disks", r"brake\s*rotor",
            r"brake\s*rotors", r"ventilated\s*disc", r"የፍሬን\s*ዲስክ", r"ፍሬን\s*ዲስክ", r"刹车盘"
        ]
    },
    "cabin_air_filters": {
        "standard_name": "Cabin-air filters",
        "patterns": [
            r"cabin\s*filter", r"cabin\s*air\s*filter", r"ac\s*filter", r"a/c\s*filter",
            r"aircon\s*filter", r"pollen\s*filter", r"cn95", r"pm2\.5\s*filter",
            r"የካቢን\s*ፊልተር", r"የአየር\s*ማጣሪያ", r"አየር\s*ማጣሪያ", r"空调滤芯", r"空调滤清器"
        ]
    },
    "wiper_blades": {
        "standard_name": "Wiper blades",
        "patterns": [
            r"wiper", r"wipers", r"wiper\s*blade", r"wiper\s*blades", r"windshield\s*wiper",
            r"windscreen\s*wiper", r"wiper\s*refill", r"የመስታወት\s*መጥረጊያ", r"የፊት\s*መስታወት\s*መጥረጊያ",
            r"መጥረጊያ", r"雨刮", r"雨刮片", r"雨刷"
        ]
    },
    "headlights": {
        "standard_name": "Headlights",
        "patterns": [
            r"headlight", r"headlights", r"head\s*light", r"head\s*lights", r"headlamp",
            r"headlamps", r"front\s*light", r"front\s*lamp", r"led\s*projector\s*head",
            r"የፊት\s*መብራት", r"የፊት\nመብራት", r"የፊትፋር", r"ፊት\s*ፋር", r"ፋር", r"大灯", r"前大灯", r"前照灯"
        ]
    },
    "tail_lights": {
        "standard_name": "Tail lights",
        "patterns": [
            r"tail\s*light", r"tail\s*lights", r"taillight", r"taillights", r"rear\s*light",
            r"rear\s*lights", r"rear\s*lamp", r"tail\s*lamp", r"brake\s*light", r"trunk\s*light\s*bar",
            r"የኋላ\s*መብራት", r"የኋላ\s*መብራቶች", r"የኋላ\s*ፋር", r"ስታፕ", r"尾灯", r"后尾灯", r"贯穿式尾灯"
        ]
    },
    "side_mirrors": {
        "standard_name": "Side mirrors",
        "patterns": [
            r"side\s*mirror", r"side\s*mirrors", r"wing\s*mirror", r"rearview\s*mirror",
            r"door\s*mirror", r"exterior\s*mirror", r"mirror\s*assembly", r"የጎን\s*መስታወት",
            r"የጎን\s*መስተዋት", r"ጎን\s*መስታወት", r"后视镜", r"倒车镜"
        ]
    },
    "bumpers": {
        "standard_name": "Bumpers",
        "patterns": [
            r"bumper", r"bumpers", r"front\s*bumper", r"rear\s*bumper", r"bumper\s*cover",
            r"bumper\s*fascia", r"ባምፐር", r"የፊት\s*ባምፐር", r"የኋላ\s*ባምፐር", r"保险杠", r"前保险杠", r"后保险杠"
        ]
    },
    "fenders_body_panels": {
        "standard_name": "Fenders/body panels",
        "patterns": [
            r"fender", r"fenders", r"wing\s*panel", r"quarter\s*panel", r"body\s*panel",
            r"body\s*panels", r"mudguard", r"wheel\s*arch\s*panel", r"ፌንደር", r"የጎን\s*ፓነል",
            r"ክንፍ", r"翼子板", r"车身覆盖件"
        ]
    },
    "shock_absorbers": {
        "standard_name": "Shock absorbers",
        "patterns": [
            r"shock\s*absorber", r"shock\s*absorbers", r"shock", r"shocks", r"strut",
            r"struts", r"macpherson", r"damper", r"dampers", r"suspension\s*strut",
            r"አሞርቲሳሪ", r"አሞርቲዛተር", r"አማርቲዛተር", r"ሾክ", r"减震器", r"避震器", r"前减震"
        ]
    }
}

# Secondary non-assigned categories for auditing
SECONDARY_CATEGORIES = {
    "chargers_cables": [r"charger", r"charging", r"evse", r"cable", r"wallbox", r"ቻርጀር", r"የቻርጅ\s*ገመድ"],
    "vehicle_unit_advertisement": [r"km\s*range", r"battery\s*capacity", r"full\s*electric\s*car", r"መኪና\s*ሽያጭ", r"ለሽያጭ\s*የቀረበ\s*መኪና"]
}

def normalize_vehicle(raw_text: str) -> Tuple[str, str, float]:
    """Standardizes vehicle model name and brand from raw text.
    Returns: (standard_model, brand, confidence)
    """
    if not isinstance(raw_text, str) or not raw_text.strip():
        return "Unknown / Unspecified", "Unknown", 0.0

    text_lower = raw_text.lower()

    for model, config in STANDARD_VEHICLES.items():
        # Check forbidden patterns first to prevent illegal merges
        forbidden = False
        for f in config["forbidden"]:
            if re.search(f, text_lower, re.IGNORECASE):
                forbidden = True
                break
        if forbidden:
            continue

        for p in config["patterns"]:
            if re.search(p, text_lower, re.IGNORECASE):
                return model, config["brand"], 0.95

    # Check for general brand mention
    if "byd" in text_lower or "ቢዋይዲ" in text_lower:
        return "BYD (Unspecified Model)", "BYD", 0.60
    if "changan" in text_lower or "ቻንጋን" in text_lower:
        return "Changan (Unspecified Model)", "Changan", 0.60

    return "Cross-Model EV / Unspecified", "Generic", 0.30

def normalize_part(raw_text: str) -> Tuple[str, float]:
    """Maps freeform part description to one of the 10 Standard Categories.
    Returns: (part_category, confidence)
    """
    if not isinstance(raw_text, str) or not raw_text.strip():
        return "unspecified_part", 0.0

    text_lower = raw_text.lower()

    for category, config in STANDARD_PARTS.items():
        for p in config["patterns"]:
            if re.search(p, text_lower, re.IGNORECASE):
                return category, 0.95

    for category, patterns in SECONDARY_CATEGORIES.items():
        for p in patterns:
            if re.search(p, text_lower, re.IGNORECASE):
                return category, 0.85

    return "generic_spare_part", 0.30

def extract_component_position(raw_text: str) -> Dict[str, Optional[str]]:
    """Extracts component position (front/rear, left/right, upper/lower) and unit type."""
    if not isinstance(raw_text, str):
        return {"longitudinal": "unspecified", "lateral": "unspecified", "unit_type": "component"}

    text_lower = raw_text.lower()

    # Longitudinal: front vs rear
    longitudinal = "unspecified"
    if re.search(r"\bfront\b|የፊት|前", text_lower):
        longitudinal = "front"
    elif re.search(r"\brear\b|\bback\b|የኋላ|后", text_lower):
        longitudinal = "rear"

    # Lateral: left vs right vs pair
    lateral = "unspecified"
    if re.search(r"\bleft\b|የግራ|左", text_lower):
        lateral = "left"
    elif re.search(r"\bright\b|የቀኝ|右", text_lower):
        lateral = "right"
    elif re.search(r"\bpair\b|\bset\b|ጥንድ|一套", text_lower):
        lateral = "pair_set"

    # Unit type: assembly vs element/pad/refill
    unit_type = "component"
    if re.search(r"\bassembly\b|\bassy\b|ሙሉ\s*ክፍል|总成", text_lower):
        unit_type = "assembly"
    elif re.search(r"\belement\b|\brefill\b|\bcartridge\b|\binsert\b", text_lower):
        unit_type = "insert_element"

    return {
        "longitudinal": longitudinal,
        "lateral": lateral,
        "unit_type": unit_type
    }

def extract_model_year_and_trim(raw_text: str) -> Tuple[Optional[str], Optional[str]]:
    """Extracts 4-digit model year and vehicle trim if specified in text."""
    if not isinstance(raw_text, str):
        return None, None

    year_match = re.search(r"\b(202[0-6])\b", raw_text)
    model_year = year_match.group(1) if year_match else None

    text_lower = raw_text.lower()
    trim = None
    if "vitality" in text_lower:
        trim = "Vitality"
    elif "free" in text_lower:
        trim = "Free"
    elif "flying" in text_lower:
        trim = "Flying"
    elif "301km" in text_lower or "301 km" in text_lower:
        trim = "301km Standard"
    elif "401km" in text_lower or "401 km" in text_lower:
        trim = "401km Long Range"

    return model_year, trim
