from interface.schema.user import UserCreateRequest, UserResponse
from usecase.user import UserUseCase

from fastapi import HTTPException


class UserController:
    def __init__(self, usecase: UserUseCase):
        self.usecase = usecase

    def get_users(self):
        users = self.usecase.get_users()
        return [
            UserResponse(id=user.id, name=user.name, email=user.email) for user in users
        ]

    def get_user(self, user_id: int):
        try:
            user = self.usecase.get_user(user_id)
            return UserResponse(id=user.id, name=user.name, email=user.email)
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))

    def create_user(self, request: UserCreateRequest):
        try:
            user = self.usecase.create_user(name=request.name, email=request.email)
            return UserResponse(id=user.id, name=user.name, email=user.email)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
