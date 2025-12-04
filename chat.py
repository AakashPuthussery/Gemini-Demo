from google import genai
from fastapi import FastAPI 
import os

app = FastAPI()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-2.0-flash")

@app.post("/chat")
async def chat_gemini(prompt:str):
    try:
        response = chat.send_message(prompt)
        return{"response":response.text}
    except Exception as e:
         return {"error": str(e)}
# while True:
#     message = input(">")
#     if message == "exit":
#         break
#     res =  chat.send_message(message)
#     print(res.text)