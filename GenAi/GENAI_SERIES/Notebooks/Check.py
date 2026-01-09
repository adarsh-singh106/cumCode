import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the variables from .env
load_dotenv() 

# 2. Get the key from the environment
my_api_key = os.getenv("OPENAI_API_KEY")

# Check if the key loaded correctly (Optional safety check)
if not my_api_key:
    print("Error: API Key not found. Check your .env file.")
else:
    client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=my_api_key, # <--- The variable from .env goes here
    )

    completion = client.chat.completions.create(
      extra_headers={
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "My Local App",
      },
      model="openai/gpt-oss-20b:free", # Using a free model
      messages=[
        {
          "role": "user",
          "content": "what is 5 * 5 then multipy it by 10?"
        }
      ]
    )

    print(completion.choices[0].message.content)