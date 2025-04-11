from fastapi import APIRouter
from app.db import models
from app.services import crud

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses= {404: {"Description": "not found"}}
)

#First test this
@router.get("/{user_id}")
async def get_user(user_id: int) -> models.users:
    user = crud.get_user(user_id)
    if user is None:
        return {"message": "User not found"}
    return user

@router.post("/create_user")
async def new_user(username: str) -> None:
    crud.create_user(username)
    
    