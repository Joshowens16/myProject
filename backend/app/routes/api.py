from fastapi import APIRouter
from app.services.greeting_service import get_greeting

router = APIRouter()


@router.get("/hello")
def hello(name: str | None = None):
    return {"message": get_greeting(name)}
