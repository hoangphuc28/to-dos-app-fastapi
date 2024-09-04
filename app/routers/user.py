from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import UserCreate, UsersResponse
from shared.db import get_db_context
from services.user import get_users
router = APIRouter(prefix="/users", tags=["Users"])
@router.get("", response_model=UsersResponse)
def get_users_endpoint(page: int = 1, limit: int = 10, db: Session = Depends(get_db_context)):
    new_user = get_users(page=page, limit=limit, db=db)
    return new_user