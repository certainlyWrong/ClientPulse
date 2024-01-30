from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from clientpulse.core.controllers.client_controller import ClientController
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'localhost:3302')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'stockpulse')
DATABASE_USER = os.getenv('DATABASE_USER', 'admin')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '123456')

database_url = (f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}"
                f"@{DATABASE_URL}")

print("database_url", database_url)

print("DATABASE_HOST", DATABASE_URL)
print("DATABASE_NAME", DATABASE_NAME)
print("DATABASE_USER", DATABASE_USER)
print("DATABASE_PASSWORD", DATABASE_PASSWORD)

engine: Engine
clientController: ClientController

try:
    engine = create_engine(
        f'{database_url}/{DATABASE_NAME}',
        echo=True,
    )

    engine.connect()
    SQLModel.metadata.create_all(engine, checkfirst=True)
    clientController = ClientController(engine)
except Exception:
    print("Error connecting to database")
    exit()
