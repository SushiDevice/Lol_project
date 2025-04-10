from fastapi import APIRouter

#aka user
router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses= {404: {"Description": "not found"}}
)

@router.get("/{user_id}")
def get_user(user_id: int):
    """
    Get user by id
    """
    return {"user_id": user_id}