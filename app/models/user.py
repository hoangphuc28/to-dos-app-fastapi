from pydantic import BaseModel, EmailStr
from uuid import UUID
class UserCreate(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    password: str


class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    is_active: bool
    is_admin: bool


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
