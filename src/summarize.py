from openai import OpenAI
from prompts import SYSTEM_PROMPT, build_summary_prompt
import os

client = OpenAI()

def summarize_item(item):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": build_summary_prompt(
                    item["title"],
                    item.get("summary", "")
                )
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
