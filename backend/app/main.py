from fastapi import FastAPI
from routers import pokemon

app = FastAPI()

base_url = "https://pokeapi.co/api/v2/"

app.include_router(pokemon.router)

@app.get("/")
async def root():
    return {"message": "My last message",
            "name": "Waosers"}
