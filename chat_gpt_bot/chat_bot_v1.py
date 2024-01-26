import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)