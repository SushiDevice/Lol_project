from fastapi import FastAPI
from app.routers import pokemon, user

app = FastAPI()

base_url = "https://pokeapi.co/api/v2/"

app.include_router(pokemon.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "My last message",
            "name": "Waosers"}
