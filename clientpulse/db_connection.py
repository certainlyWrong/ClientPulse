from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from clientpulse.core.controllers.client_controller import ClientController


from .enviroments import Enviroments


engine: Engine
clientController: ClientController

try:
    engine = create_engine(
        Enviroments.get_instance.database_connection,
        echo=True,
    )

    try:
        engine.connect()
    except Exception:
        print("Database not found, creating database")

        engine = create_engine(
            Enviroments.get_instance.database_connection,
            echo=True,
        )

    SQLModel.metadata.create_all(engine, checkfirst=True)
    clientController = ClientController(engine)
except Exception as e:
    print("Error connecting to database")
    print(e)
    exit()
