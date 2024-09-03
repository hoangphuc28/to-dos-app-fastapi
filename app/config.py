import os
from dotenv import load_dotenv

load_dotenv()

def get_connection_string(asyncMode: bool = False) -> str:
    db_engine = os.environ.get("DB_ENGINE") if not asyncMode else os.environ.get("ASYNC_DB_ENGINE")
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USERNAME")
    db_pass = os.getenv("DB_PASSWORD")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    return f"{db_engine}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

#Database connection string
SQLALCHEMY_DATABASE_URL = get_connection_string()
SQLALCHEMY_DATABASE_URL_ASYNC = get_connection_string(True)

#JWT 
JWT_SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv(key="ACCESS_TOKEN_EXPIRE_MINUTES")