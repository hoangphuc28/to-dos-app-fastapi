from fastapi import FastAPI

from config import SQLALCHEMY_DATABASE_URL
from routers import auth, company

app = FastAPI()
app.include_router(auth.router)
app.include_router(company.router)
@app.get("/", tags=["Health Check"])
async def health_check():
    return {"status": "ok",
            "database": SQLALCHEMY_DATABASE_URL
            }
