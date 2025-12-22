from openai import OpenAI
import os

def test_openai_call():
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Reply with one short sentence saying hello."}
        ],
        temperature=0
    )

    return response.choices[0].message.content
