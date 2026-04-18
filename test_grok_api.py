"""
Test script to verify Grok API connectivity
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

response = client.chat.completions.create(
    model="grok-4",
    messages=[
        {"role": "system", "content": "You are Grok, built by xAI."},
        {"role": "user", "content": "Hello from Gravit integration test. Confirm connection."}
    ],
    temperature=0.7,
    max_tokens=100
)

print("✅ Grok API is working!")
print("Response:", response.choices[0].message.content)
