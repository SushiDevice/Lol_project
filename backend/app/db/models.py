from sqlmodel import SQLModel, Field
from typing import Optional

class users(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    status: Optional[bool] = Field(default=True)

class pokemon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    type: str
    status: Optional[bool] = Field(default=True)
    sprite: Optional[str] = Field(default=None)

#Create the many to many table between users and pokemon
#class user_pokemon(SQLModel, table=True):
    # Some code that im yet to learn and implement