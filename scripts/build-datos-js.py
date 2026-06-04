#!/usr/bin/env python3
"""Converts data/centrelink.json -> src/data/datos.js. Generic — auto-detects silos."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(ROOT, 'data', 'centrelink.json')
JS_PATH = os.path.join(ROOT, 'src', 'data', 'datos.js')

# Site config (fixed for this site)
SITE = {
    "domain": "centrelinkofficesaustralia.com",
    "name": "Centrelink Offices Australia",
    "tagline": "Complete directory of Centrelink Service Centres across Australia",
    "centrelink_phone": "13 24 68",
    "centrelink_phone_intl": "+61 13 24 68",
    "medicare_phone": "13 20 11",
    "total_centres": 318,
    "total_states": 8,
    "official_site": "https://www.servicesaustralia.gov.au",
    "official_locator": "https://www.servicesaustralia.gov.au/find-us",
    "data_source": "Department of Human Services public dataset, current as of 9 January 2019",
    "data_license": "Creative Commons Attribution 3.0 Australia"
}

with open(JSON_PATH, encoding='utf-8') as f:
    data = json.load(f)

js = "// AUTO-GENERATED from data/centrelink.json. DO NOT EDIT.\n"
js += "// Re-generate: python3 scripts/build-datos-js.py\n\n"
js += f"export const site = {json.dumps(SITE, ensure_ascii=False, indent=2)};\n\n"

# Auto-detect silos: keys that are lists of dicts with 'slug'
silos = []
for key, val in data.items():
    if key == 'meta':
        continue
    if isinstance(val, list) and val and isinstance(val[0], dict) and 'slug' in val[0]:
        js += f"export const {key} = {json.dumps(val, ensure_ascii=False, indent=2)};\n\n"
        silos.append(key)
    elif isinstance(val, dict):
        js += f"export const {key} = {json.dumps(val, ensure_ascii=False, indent=2)};\n\n"

# Combine indexable pages
js += "// allPages combines all indexable silos\n"
js += f"export const allPages = [{', '.join(f'...{s}' for s in silos)}];\n"

os.makedirs(os.path.dirname(JS_PATH), exist_ok=True)
with open(JS_PATH, 'w', encoding='utf-8') as f:
    f.write(js)

print(f"OK: datos.js generated ({os.path.getsize(JS_PATH):,} bytes)")
print(f"  Silos detected: {silos}")
