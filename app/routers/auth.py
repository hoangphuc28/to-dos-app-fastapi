from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import UserCreate, UserOut, Token
from shared.db import get_db_context
from services.auth import create_user, verify_user
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(prefix="/auth", tags=["Auth"])
@router.post("/signup/", response_model=UserOut)
def signup(user: UserCreate,  db: Session = Depends(get_db_context)):
    new_user = create_user(user, db)
    return new_user

@router.post("/signin/", response_model=Token)
def signin(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_context)):
    
    return verify_user(user, db)