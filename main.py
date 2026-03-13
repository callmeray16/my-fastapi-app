from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from fastapi.middleware.cors import CORSMiddleware
import os

# This tells Python: "Go look in the computer's secret settings for the key"
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

# 1. Initialize the app ONCE
app = FastAPI()

# 2. Add CORS Middleware (Crucial for your HTML file to work)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Initialize Gemini Client
# Pro-tip: Keep this key safe!

@app.get("/")
def home_page():
    return {"message": "API is live and interesting!"}

@app.get("/add/{num1}/{num2}")
def calculate(num1: int, num2: int):
    return {"operation": "addition", "sum": num1 + num2}

@app.get("/ask")
def gemini(query: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=query
        )
        # We are wrapping the text in a dictionary with the key "answer"
        return {"answer": response.text} 
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}

@app.get("/items")
def get_item(item_id: int, color: str = "white"):
    return {
        "id": item_id,
        "selected_color": color,
        "message": f"Fetching item {item_id} in {color}"
    }

#uvicorn main:app --reload
