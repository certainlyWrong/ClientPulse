from fastapi import APIRouter


router_root = APIRouter()


@router_root.get('/')
def hello_router():
    return "Hello world\n"
