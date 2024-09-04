from typing import List
from pydantic import BaseModel, EmailStr
from uuid import UUID

from models.pagination import Pagination
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

class Token(BaseModel):
    access_token: str
    token_type: str
class UsersResponse(BaseModel, Pagination):
    items: List[UserOut]
    