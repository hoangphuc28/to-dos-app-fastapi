from datetime import datetime, timedelta
from jose import jwt
from config import JWT_SECRET, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES))})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt