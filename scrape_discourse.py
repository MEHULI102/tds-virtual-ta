import requests

session = requests.Session()

# Paste the decoded cookie value exactly here
cookie_value = "82e31paGlED%2B%2B5rusxa2whDZ3EczVOdByuF0QuJ7alqDdFdm2Gt25WM6A3yTXJCJmgvZN%2FxJpPgo9aq9YgS5SGcFVIo%2BPzj%2Fd75k7rPr5mfq3HFesJepxru81tZLpA%2B10flI%2B2sVepY2FMo6YfmeiKZi3R1FZl4%2BlaNYJ9sMvZjhlOJd7pJCgIZwLEiGGtfsT71WbKbT2oJeozlD6vY0syBcBqPaOj9HK5hExexblnINJ9nm1uIBOXvQMcvlxXnl0ETn1AIx5zr%2BnvmxngpfZ%2BgpAEUJ5CPx4QRuh9l60hCelLTLpv4fAIIwhFmAXAVa%2BVX%2FyIU2NlsR2mG60kUrRHousvDDDCqHqV3gj4Aa7VMHKC7Kl8DncqqfKBWnbHLrgaXVZWQVMQ7vBo0AEPiMkpxL96hVk10Y1DtDfYDHo4qXv67wLFjP9AdI%2BvrDlJbtwEcK2NaauSgBTkXiHDj7cTADMnCLUA%3D%3D--Hkv3yWpcPPKkO1GX--VXf1RiY%2BHJLN0iGO2%2Frv6g%3D%3D"

session.cookies.set("_forum_session", cookie_value, domain="discourse.onlinedegree.iitm.ac.in")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",  # your real UA string
    "Accept": "application/json",
    "Connection": "keep-alive",
}

url = "https://discourse.onlinedegree.iitm.ac.in/latest.json?page=1"

response = session.get(url, headers=headers)
print(response.status_code)
print(response.text)
