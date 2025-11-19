#!/usr/bin/env python3

import requests
import re
import random
import json

BASE = "https://developer.android.com"


def fetch(url):
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.text


def fetch_partial(url, max_bytes=4096):
    """
    Download only the first part of the OTA ZIP.
    Equivalent to: (ulimit -f 2; wget $OTA)
    """
    resp = requests.get(url, stream=True, timeout=15)
    resp.raise_for_status()

    data = b""
    for chunk in resp.iter_content(chunk_size=512):
        data += chunk
        if len(data) >= max_bytes:
            break

    return data.decode("latin1", errors="ignore")


print("Fetching Pixel Beta metadata...")

# 1. Fetch version list
versions_html = fetch(f"{BASE}/about/versions")

# 2. Find latest Android version / QPR page
match = re.findall(r"https://developer.android.com/about/versions/.*?[0-9]\"", versions_html)
latest_page = sorted(set(match), reverse=True)[0].rstrip('"')

latest_html = fetch(latest_page)

# 3. Find OTA QPR Beta page
ota_match = re.search(r'href="(.*download-ota.*qpr.*?)"', latest_html)
ota_page = BASE + ota_match.group(1)

ota_html = fetch(ota_page)

# 4. Extract rows
model_list = re.findall(r"<td>(.*?)</td>", ota_html)
product_list = re.findall(r"ota/(.*?_beta)", ota_html)
ota_url_list = re.findall(r'href="(https.*?ota/.*?_beta.*?)"', ota_html)

# Random selection
idx = random.randrange(len(product_list))

MODEL = model_list[idx]
PRODUCT = product_list[idx]
DEVICE = PRODUCT.replace("_beta", "")
OTA_URL = ota_url_list[idx]

print(f"Selected: {MODEL} ({PRODUCT})")
print(f"OTA URL = {OTA_URL}")

# 5. Fetch partial ZIP data (first 4KB)
print("Fetching first 4KB from OTA (metadata extraction)...")
partial_data = fetch_partial(OTA_URL, max_bytes=4096)

# 6. Extract metadata
fp = re.search(r"post-build=(.*)", partial_data)
sp = re.search(r"security-patch-level=(.*)", partial_data)

if not fp or not sp:
    print("ERROR: Could not extract fingerprint or patch!")
    print("Partial data received:")
    print(partial_data[:500])
    exit(1)

FINGERPRINT = fp.group(1).strip()
SECURITY_PATCH = sp.group(1).strip()

print("Fingerprint extracted!")
print(FINGERPRINT)

# 7. Write pif.json
data = {
    "MANUFACTURER": "Google",
    "MODEL": MODEL,
    "PRODUCT": PRODUCT,
    "DEVICE": DEVICE,
    "FINGERPRINT": FINGERPRINT,
    "SECURITY_PATCH": SECURITY_PATCH,
    "DEVICE_INITIAL_SDK_INT": "32"
}

with open("pif.json", "w") as f:
    json.dump(data, f, indent=4)

print("\n pif.json generated successfully!")
