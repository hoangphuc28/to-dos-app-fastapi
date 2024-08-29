from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import UserCreate, UserOut, UserLogin, Token
from shared.db import get_db_context
from utils.password import hash_password, verify_password
from utils.accesstoken import create_access_token
from schemas.user import User
router = APIRouter(prefix="/auth", tags=["Auth"])
@router.post("/signup/", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db_context)):
    db_user = db.scalars(select(User).filter_by(email=user.email)).first()
    if db_user is not None:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(user.password)

    # Convert the Pydantic model to a dictionary and remove the 'password' field
    user_data = user.dict(exclude={'password'})
    user_data['hashed_password'] = hashed_password

    # Create the User instance
    new_user = User(**user_data)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.post("/signin/", response_model=Token)
def signin(user: UserLogin, db: Session = Depends(get_db_context)):
    db_user = db.query(user).filter(user.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}