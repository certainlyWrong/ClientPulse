from .routes.hello_router import router_root
from clientpulse.routes.v1.client_routes import client_router
from fastapi import FastAPI


app = FastAPI(
    title="Client Pulse API",
    description="This is a very fancy project,"
    " with auto docs for the API and everything",
)


app.include_router(router_root)
app.include_router(client_router, prefix='/api/v1', tags=['v1'])
