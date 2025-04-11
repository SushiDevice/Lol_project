from ..db import models
from ..db.connection import engine
from sqlmodel import Session, select

def create_user(name: str) -> None:
    with Session(engine) as session:
        new_user = models.users(username=name, status=True)
        session.add(new_user)
        session.commit()
        print(f"User {name} created sucessfully")
        session.close()

def create_pokemon(name: str, type: str) -> None:
    with Session(engine) as session:
        new_pokemon = models.pokemon(name=name, type=type) 
        session.add(new_pokemon)
        session.commit()
        session.close()

def get_user(id: int) -> models.users:
    with Session(engine) as session: 
        stmt = select(models.users).where(models.users.user_id == id)
        results = session.exec(stmt)
        result = results.first()
        return result

def get_pokemon(name: str) -> models.pokemon:
    with Session(engine) as session:
        stmt = select(models.pokemon).where(models.pokemon.name == name)
        results = session.exec(stmt)
        result = results.first()
        return result
