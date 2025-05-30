# app/scraper.py
import requests
import json
from datetime import datetime

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
API_ENDPOINT = f"{BASE_URL}/latest.json"

def scrape_posts(start_date: str, end_date: str, output_file="database.json"):
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")

    all_posts = []
    page = 0

    while True:
        res = requests.get(API_ENDPOINT, params={"page": page})
        if res.status_code != 200:
            break

        data = res.json()
        topics = data.get("topic_list", {}).get("topics", [])
        if not topics:
            break

        for topic in topics:
            created = datetime.strptime(topic["created_at"][:10], "%Y-%m-%d")
            if start_dt <= created <= end_dt:
                all_posts.append({
                    "id": topic["id"],
                    "title": topic["title"],
                    "url": f"{BASE_URL}/t/{topic['slug']}/{topic['id']}",
                    "created_at": topic["created_at"]
                })

        page += 1

    with open(output_file, "w") as f:
        json.dump(all_posts, f, indent=2)

    print(f"Saved {len(all_posts)} posts to {output_file}")
