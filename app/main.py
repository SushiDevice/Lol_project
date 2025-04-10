from fastapi import FastAPI

from routers import champions

app = FastAPI()

base_url = ""

app.include_router(champions.router)

@app.get("/")
async def root():
    return {"message": "My last message",
            "name": "Waosers"}

@app.get("/lol")
async def rt():
    return {"message": "My last message",
            "name": "Waosers"}