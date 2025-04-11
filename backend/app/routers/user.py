from fastapi import APIRouter
from models import 

#aka user
router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses= {404: {"Description": "not found"}}
)

@router.get("/{user_id}")
def get_user(user_id: int):

    return {"user_id": user_id}