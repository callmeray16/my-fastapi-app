from fastapi import FastAPI

#uvicorn main:app --reload
# 2. Create your 'App' (This is your Kitchen)
app = FastAPI()

@app.get("/")
def home_page():
    # 4. Define the 'Response' (The Goods)

    return "GAY GAY GAY GAY ARAVIND"




