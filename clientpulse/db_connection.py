from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from clientpulse.core.controllers.client_controller import ClientController


from .enviroments import Enviroments


engine: Engine
clientController: ClientController

try:
    print("Creating database connection...")
    engine = create_engine(
        Enviroments.get_instance.database_connection,
        echo=True,
    )

    print("Connecting to database...")

    engine.connect()

    print("Database connected")

    SQLModel.metadata.create_all(engine, checkfirst=True)
    clientController = ClientController(engine)
except Exception as e:
    print("Error connecting to database")
    print(e)
    exit()
