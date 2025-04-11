from sqlmodel import SQLModel, Field
from typing import Optional

class users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    status: Optional[bool] = Field(default=True)

class pokemon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    type: str
    status: Optional[bool] = Field(default=True)

