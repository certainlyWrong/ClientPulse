from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from clientpulse.core.controllers.client_controller import ClientController


from .environment import Environment


engine: Engine
clientController: ClientController

try:
    print("Creating database connection...")
    engine = create_engine(
        Environment.get_instance.database_connection,
        echo=True,
    )

    engine.connect()

    SQLModel.metadata.create_all(engine, checkfirst=True)
    clientController = ClientController(engine)
except Exception as e:
    print("Error connecting to database")
    print(e)
    exit()
