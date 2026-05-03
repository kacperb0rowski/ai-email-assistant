import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

email_content = input("Hello, how can I help you today? ")
print(email_content)

