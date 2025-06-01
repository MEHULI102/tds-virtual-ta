# app/generate_embeddings.py
import openai
import json
import os

from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

openai.api_key = os.getenv("OPENAI_API_KEY")

with open("app/database.json", "r") as f:
    posts = json.load(f)

def get_embedding(text):
    text = text.replace("\n", " ")
    response = openai.Embedding.create(
        input=[text],
        model="text-embedding-3-small"
    )
    return response['data'][0]['embedding']

# Add embeddings
for post in tqdm(posts):
    post["embedding"] = get_embedding(post["title"])

with open("app/database_with_embeddings.json", "w") as f:
    json.dump(posts, f)
