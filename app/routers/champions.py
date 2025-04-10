from fastapi import APIRouter

router = APIRouter(
    prefix="/champion",
    tags=["champions"],
    responses= {404: {"Description": "not found"}}
)

@router.get("/")
async def read():
    message = "hello!"
    return {"message": message }

@router.get("/{id}")
async def readOne(id: int):
    if id == 1:
        champ = "Trynd"
        return {"Champ": champ }
    else:
        return router.responses