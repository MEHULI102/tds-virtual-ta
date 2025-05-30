# app/qa_engine.py
import openai
import json
import base64
import pytesseract
from PIL import Image
import io

OPENAI_API_KEY = "your_api_key_here"

def image_to_text(image_b64: str) -> str:
    try:
        img = Image.open(io.BytesIO(base64.b64decode(image_b64)))
        return pytesseract.image_to_string(img)
    except:
        return ""

def fetch_relevant_content(question: str) -> list:
    with open("app/database.json", "r") as f:
        posts = json.load(f)

    related = [post for post in posts if any(word.lower() in post["title"].lower() for word in question.split())]
    return related[:3]

def generate_answer(question: str, image: str = None) -> dict:
    if image:
        question += "\nImage Text: " + image_to_text(image)

    relevant_posts = fetch_relevant_content(question)
    context = "\n".join([f"{post['title']} - {post['url']}" for post in relevant_posts])

    prompt = f"""Answer this question based on the following posts:\n{context}\n\nQuestion: {question}"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "answer": response.choices[0].message["content"].strip(),
        "links": [{"url": post["url"], "text": post["title"]} for post in relevant_posts]
    }
