import os
from openai import OpenAI
from prompts import SYSTEM_PROMPT

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze(asset: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"حلّل {asset} اليوم."}
        ],
        temperature=0.4,
    )
    return resp.choices[0].message.content.strip()
