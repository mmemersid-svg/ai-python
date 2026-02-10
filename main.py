
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

while True:
    user = input(">> ")
    if user.lower() == "q":
        print("bye")
        break

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=user,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level="low")
        ),
    )

    print("ai:", response.text)