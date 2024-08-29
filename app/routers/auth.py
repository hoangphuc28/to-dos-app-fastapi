from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import UserCreate, UserOut, UserLogin, Token
from shared.db import get_db_context
from utils.password import hash_password, verify_password
from utils.accesstoken import create_access_token
from schemas.user import User
from services.auth import new_user, verify_user
router = APIRouter(prefix="/auth", tags=["Auth"])
@router.post("/signup/", response_model=UserOut)
def signup(user: UserCreate,  db: Session = Depends(get_db_context)):
    new_user = new_user(user, db)
    return new_user

@router.post("/signin/", response_model=Token)
def signin(user: UserLogin, db: Session = Depends(get_db_context)):
    
    return verify_user(user, db)