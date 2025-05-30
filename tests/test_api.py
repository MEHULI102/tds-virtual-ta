# tests/test_api.py
import requests

API_URL = "http://localhost:8000/api/"

data = {
    "question": "Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?",
    "image": None
}

res = requests.post(API_URL, json=data)
print(res.json())
