from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

email_content = input("Enter customer mail:\n")

prompt = f"You are a professional customer support assistant. Respond to the following email, while being polite and helpful: {email_content}"

response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt
)
print("\nAI Response:\n")
print(response.output_text)