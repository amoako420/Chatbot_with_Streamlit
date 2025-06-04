from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=API_KEY)
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."


response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    contents=prompt
)


print(response.text)