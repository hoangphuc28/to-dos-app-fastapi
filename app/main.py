from fastapi import FastAPI

from config import SQLALCHEMY_DATABASE_URL
from routers import auth, company, task, user
app = FastAPI()
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(company.router)
app.include_router(task.router)



@app.get("/", tags=["Health Check"])
async def health_check():
    return {"status": "ok",
            "database": SQLALCHEMY_DATABASE_URL
            }
