from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine

class users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: Optional[bool] = Field(default=True)

db_file = "sqlite:///database.db"
engine = create_engine(db_file, echo=True)

SQLModel.metadata.create_all(engine)



















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