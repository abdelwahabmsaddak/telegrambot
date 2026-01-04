import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_analyze(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "أنت محلل تداول محترف"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
