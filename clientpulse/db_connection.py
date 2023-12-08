from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from clientpulse.core.controllers.client_controller import ClientController
import os

DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT', '3306')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'clientpulse')
DATABASE_USER = os.getenv('DATABASE_USER', 'root')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '123456')

database_url = (f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}"
                f"@{DATABASE_HOST}:{DATABASE_PORT}")

print("database_url", database_url)
print("DATABASE_HOST", DATABASE_HOST)
print("DATABASE_PORT", DATABASE_PORT)
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
