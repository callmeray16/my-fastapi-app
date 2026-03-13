from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

client = genai.Client(api_key="AIzaSyBMZDOkwBS5Z8-R6etXTm81Rgjin7hWUxo")



class UserProfile(BaseModel):
    username: str
    bio: str
    age: int

#uvicorn main:app --reload
# 2. Create your 'App' (This is your Kitchen)
app = FastAPI()

@app.get("/")
def home_page():
    # 4. Define the 'Response' (The Goods)
    return "This is very interesting"

@app.get("/add/{num1}/{num2}")
def calculate(num1: int, num2: int):
    result = num1 + num2
    return {
        "operation": "addition",
        "sum": result
    }

@app.get("/ai/{prompt}")
def gemini(prompt:str):
    try:
        # UPDATED: Using the currently active 2026 model IDs
        response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents= prompt)
        return response.text.replace('\n',"")
    

    except Exception as e:
        print(f"Error: {e}")

    
@app.get("/items")
def get_item(item_id: int, color: str = "white"):
    return {
        "id": item_id,
        "selected_color": color,
        "message": f"Fetching item {item_id} in {color}"
    }

@app.post("/create-user")
def create_user(user: UserProfile):
    return {"status": "User Created", "data": user}
