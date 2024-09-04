
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from utils.accesstoken import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signin", scheme_name="JWT")

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    user = verify_token(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user