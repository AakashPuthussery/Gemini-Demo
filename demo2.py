from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content_stream(
    model = "gemini-2.0-flash",
    contents = "hello"
)
full_text = ""
for chunk in response:
    if chunk.text:
        print(chunk.text, end="")
        full_text+=chunk.text
print(full_text)