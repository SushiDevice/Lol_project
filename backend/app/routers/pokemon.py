from fastapi import APIRouter
import pokebase as pb
import random as rd

router = APIRouter(
    prefix="/pokemon",
    tags=["pokemon"],
    responses= {404: {"Description": "not found"}}
)

@router.get("/pokemons")
async def showSome():
    pokemon = pb.pokemon("raichu")
    name = pokemon.name
    return name

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

#first should i poblate de database