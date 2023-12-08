
from abc import ABC

from sqlalchemy import (
    Engine,
)
from sqlmodel import (
    Session,
    select,
)

from clientpulse.core.models.client_model import ClientModel


class IClientController(ABC):
    """
    Interface for the ClientController class.
    """

    @classmethod
    def find_all(cls) -> list[ClientModel]:
        raise NotImplementedError

    @classmethod
    def find_by_id(cls, id: int) -> ClientModel | None:
        raise NotImplementedError

    @classmethod
    def create(cls, client: ClientModel) -> ClientModel:
        raise NotImplementedError

    @classmethod
    def update(cls, id: int, client: ClientModel) -> ClientModel | None:
        raise NotImplementedError

    @classmethod
    def delete(cls, id: int) -> bool:
        raise NotImplementedError


class ClientController(IClientController):
    """
    Controller for the Client entity.
    """

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def find_all(self) -> list[ClientModel]:
        """
        Find all Client.
        """
        with Session(self.engine) as session:
            statement = select(ClientModel)
            Client = session.exec(statement).all()
            return list(Client)

    def find_by_id(self, id: int) -> ClientModel | None:
        """
        Find a client by its uid.
        """
        with Session(self.engine) as session:
            statement = select(
                ClientModel
            ).where(ClientModel.id == id)

            client = session.exec(statement).first()
            return client

    def create(self, client: ClientModel) -> ClientModel:
        """
        Create a client.
        """
        with Session(self.engine) as session:
            session.add(client)
            session.commit()
            session.refresh(client)
            return client

    def update(self, id: int, client: ClientModel) -> ClientModel | None:
        """
        Update a client.
        """
        with Session(self.engine) as session:
            try:
                session.add(client)
                session.commit()
                session.refresh(client)
                return client
            except Exception:
                return None

    def delete(self, id: int) -> bool:
        """
        Delete a client.
        """
        with Session(self.engine) as session:
            statement = select(
                ClientModel
            ).where(ClientModel.id == id)

            if session.exec(statement).first() is None:
                return False

            client = session.exec(statement).first()
            session.delete(client)
            session.commit()
            return True
