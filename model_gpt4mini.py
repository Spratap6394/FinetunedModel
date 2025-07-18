# app/model_gpt4mini.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_gpt4_mini(instruction: str, text: str) -> str:
    prompt = f"{instruction}\n\n{text}"
    response = client.chat.completions.create(
        model="o3-mini",  # or "gpt-4", "gpt-3.5-turbo" if desired
        messages=[
            {"role": "system", "content": "You are a Jenkins to YAML converter."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip() # type: ignore
