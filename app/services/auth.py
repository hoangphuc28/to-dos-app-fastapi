from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import UserCreate, UserLogin, Token
from utils.password import hash_password, verify_password
from utils.accesstoken import create_access_token
from schemas.user import User
def create_user(user: UserCreate, db: Session):
    db_user_email = db.scalars(select(User).filter_by(email=user.email)).first()
    if db_user_email is not None:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user_username = db.scalars(select(User).filter_by(username=user.username)).first()
    if db_user_username is not None:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    hashed_password = hash_password(user.password)

    # Convert the Pydantic model to a dictionary and exclude the 'password' field
    user_data = user.model_dump(exclude={'password'})
    user_data['hashed_password'] = hashed_password

    # Create the User instance
    new_user = User(**user_data)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def verify_user(user: UserLogin, db: Session):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.username})
    token = Token(access_token=access_token, token_type="bearer")
    return token