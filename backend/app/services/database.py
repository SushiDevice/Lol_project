from ..db import models
from ..db.connection import engine
from sqlmodel import Session

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
        

def get_user(user_id: int) -> models.users:
    with Session(engine) as session: 
        user = session.get(models.users ,user_id)
        return user
    

def get_pokemon(poke_id: int) -> models.pokemon:
    with Session(engine) as session:
        pokemon = session.get(models.pokemon, poke_id)
        return pokemon



















"""
connection = connect()
cur = connection.cursor()

# Delete tables from database


cur.execute("DROP TABLE users")
cur.execute("DROP TABLE pokemon")


try:
    #cur.execute("CREATE TABLE users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, status INTEGER )")
    cur.execute("INSERT INTO users(username, status) VALUES('DumbUser', 1)")
    connection.commit()
except:  # noqa: E722
    print("Table already exists")

#cur.execute("CREATE TABLE users(user_id, username, status )")
#cur.execute("CREATE TABLE pokemon(poke_id, name, type, status)")
#cur = cur.execute("SELECT name FROM sqlite_master")



cur.close()"""