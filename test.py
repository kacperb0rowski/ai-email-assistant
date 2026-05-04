from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY_TEST")
)

response = client.responses.create(
    model="gpt-4o-mini",
    input="write a haiku about ai"
)

print(response.output_text)