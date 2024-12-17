from typing import Any

from fastapi import APIRouter, Request
from pydantic import BaseModel

from app.api.deps import SessionDep
from app.core.security import get_password_hash
from app.models import (
    User,
    UserPublic,
)

router = APIRouter(tags=["private"], prefix="/private")


class PrivateUserCreate(BaseModel):
    email: str
    password: str
    full_name: str
    is_verified: bool = False


@router.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}


@router.get("/highlight-io-check/")
async def root(request: Request):
    return {"message": f"This might not be a great idea {5 / 0}"}


@router.get("/sentry-debug/")
async def trigger_error():
    division_by_zero = 1 / 0  # noqa: F841


@router.post("/users/", response_model=UserPublic)
def create_user(user_in: PrivateUserCreate, session: SessionDep) -> Any:
    """
    Create a new user.
    """

    user = User(
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=get_password_hash(user_in.password),
    )

    session.add(user)
    session.commit()

    return user
