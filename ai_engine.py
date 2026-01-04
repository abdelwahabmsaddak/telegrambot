import os
from openai import OpenAI
from prompts import SYSTEM_PROMPT

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_analysis(query: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT.strip()},
            {"role": "user", "content": query.strip()},
        ],
        temperature=0.3,
    )
    return resp.choices[0].message.content.strip()
