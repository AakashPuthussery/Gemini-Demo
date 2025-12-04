from fastapi import FastAPI 
from google import genai 
import os 
app = FastAPI() 

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

@app.get("/ask")
async def ask_gemini(prompt: str):
    try:
        response = client.models.generate_content_stream(
            model = "gemini-2.0-flash",
            contents = prompt
        )
        full_text =""
        for chunk in response:
            if chunk.text:
                print(chunk.text, end="")
                full_text += chunk.text
        return{"response":full_text}
    except Exception as e:
        return{"error":str(e)}