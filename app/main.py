from fastapi import FastAPI

app = FastAPI()

base_url = ""

@app.get("/")
async def root():
    return {"message": "Hello World"}