from fastapi import HTTPException
from sqlalchemy.orm import Session
from shared.enum import CompanyMode
from models.pagination import Pagination
from schemas.user import User
from models.user import UsersResponse
from sqlalchemy import func, select
from uuid import UUID
def get_users(db: Session, page: int = 1, limit: int = 10):
    if page < 1:
        page = 1
    skip = (page - 1) * limit

    # Get total number of active companies
    total_items = db.scalar(select(func.count(User.id)))
    total_pages = (total_items + limit - 1) // limit  # Ceiling division for total pages

    # Fetch the paginated active companies
    stmt = select(User).offset(skip).limit(limit)
    companies = db.scalars(stmt).all()

    # Create the response
    response = {
        "items": companies,
        "limit": limit,
        "currentPage": page,
        "totalPages": total_pages,
        "totalItems": total_items
    }
    
    return response