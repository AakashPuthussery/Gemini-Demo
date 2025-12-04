from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Upload the file
uploaded_file = client.files.upload(file="aa.pdf")

# Generate summary
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        "Summary of the PDF:",
        uploaded_file
    ]
)

print(response.text)
