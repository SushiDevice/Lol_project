from pathlib import Path
from sqlmodel import SQLModel, create_engine

db_path = Path(__file__).resolve().parent.parent / "database.db"
db_file = f"sqlite:///{db_path}"
engine = create_engine(db_file, echo=True)

def create_db_and_tables():
 SQLModel.metadata.create_all(engine)
