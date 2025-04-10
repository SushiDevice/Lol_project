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
    pokemons = pb.APIResource("pokemon")
    
    return {"message": "hello"}

@router.get("/{name}")
async def collect(name: str, shChance: int = rd.randint(1, 3)):
    pokemon = pb.APIResource("pokemon", name)
    response = {
        "name": pokemon.name,
        "sprite": pokemon.sprites.front_default,
        "shiny": False,
        "message": ""
    }
    if shChance == 1:
        response["shiny"] = pokemon.sprites.front_shiny
        response["shiny"] = True
        response["message"] = "¡Shiny pokemon!"
    return response
