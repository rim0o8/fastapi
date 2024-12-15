# app/interfaces/router.py
from infra.repository.user import InMemoryUserRepository
from interface.controller.user import UserController
from interface.schema.user import UserCreateRequest
from usecase.user import UserUseCase

from fastapi import APIRouter, Depends, FastAPI

router = APIRouter()


def get_user_controller():
    repository = InMemoryUserRepository()
    usecase = UserUseCase(repository)
    return UserController(usecase)


@router.get("/")
async def get_users():
    return "Hello World"


@router.get("/users")
async def get_users(controller: UserController = Depends(get_user_controller)):
    return controller.get_users()


@router.get("/users/{user_id}")
async def get_user(
    user_id: int, controller: UserController = Depends(get_user_controller)
):
    return controller.get_user(user_id)


@router.post("/users")
async def create_user(
    request: UserCreateRequest,
    controller: UserController = Depends(get_user_controller),
):
    return controller.create_user(request)


def add_router(app: FastAPI) -> FastAPI:
    app.include_router(router)
    return app
