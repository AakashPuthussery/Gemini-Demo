from fastapi import FastAPI
from google import genai
import os

app = FastAPI()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.get("/ask")
async def ask_gemini(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
@app.get("/")
def home():
    return {"message": "FastAPI + Gemini is running!"}

