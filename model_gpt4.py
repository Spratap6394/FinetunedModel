# app/comparator.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_gpt4_comparator(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that compares two outputs and picks the better one."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip() # type: ignore
