from fastapi import APIRouter
import pokebase as pb
import random as rd

router = APIRouter(
    prefix="/pokemon",
    tags=["pokemon"],
    responses= {404: {"Description": "not found"}}
)

@router.get("/")
async def showAll(show: int = 10):
    return {"message": "hello"}

@router.get("/{name}")
async def collect(name: str, shChance: int = rd.randint(1, 10)):
    pokemon = pb.APIResource("pokemon", name)
    response = {
        "name": pokemon.name,
        "sprite": pokemon.sprites.front_default,
    }
    if shChance == 1:
        response["shiny"] = pokemon.sprites.front_shiny
    return response
