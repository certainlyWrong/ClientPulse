from fastapi import APIRouter
from clientpulse.core.models.client_model import ClientModel

from clientpulse.db_connection import clientController


client_router = APIRouter(prefix='/client', tags=['client'])


@client_router.get('/')
async def find_all_clients():
    clients = clientController.find_all()
    return clients


@client_router.get('/{client_id}/')
async def find_client_by_uid(client_id: int):
    result = clientController.find_by_id(client_id)
    print("result", result)
    return result or {"message": "Client not found"}


@client_router.post('/')
async def create_client(client: ClientModel):
    client = clientController.create(client)
    return client


@client_router.patch('/{client_id}/')
async def update_client(client_id: int, client: ClientModel):
    result = clientController.update(client_id, client)
    return result or {"message": "Client not found"}


@client_router.delete('/{client_id}/')
async def delete_client(client_id: int):
    result = clientController.delete(client_id)

    return (
        {"message": "Client deleted successfully"}
        if result
        else
        {"message": "Client not found"}
    )
