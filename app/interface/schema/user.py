# app/interfaces/schemas/user_schema.py
from pydantic import BaseModel, EmailStr


class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
