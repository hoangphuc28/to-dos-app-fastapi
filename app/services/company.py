from fastapi import HTTPException
from sqlalchemy.orm import Session
from shared.enum import CompanyMode
from models.pagination import Pagination
from schemas.company import Company
from models.company import CompanyCreate, CompanyUpdate, CompanyView
from sqlalchemy import func, select
from uuid import UUID

def get_company(db: Session, company_id: UUID) -> bool:
    stmt = select(Company).filter_by(id=company_id, mode=CompanyMode.ACTIVE)
    company_detail = db.scalars(stmt).first()
    if company_detail is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company_detail
def get_companies(db: Session, page: int = 1, limit: int = 10):
    if page < 1:
        page = 1
    skip = (page - 1) * limit

    # Get total number of active companies
    total_items = db.scalar(select(func.count(Company.id)).filter(Company.mode == CompanyMode.ACTIVE))
    total_pages = (total_items + limit - 1) // limit  # Ceiling division for total pages

    # Fetch the paginated active companies
    stmt = select(Company).filter(Company.mode == CompanyMode.ACTIVE).offset(skip).limit(limit)
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

def create_company(db: Session, company: CompanyCreate):
    db_company = Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def update_company(db: Session, company_id: UUID, company_update: CompanyUpdate):
    stmt = select(Company).filter_by(id=company_id, mode=CompanyMode.ACTIVE)
    db_company = db.scalars(stmt).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    for key, value in company_update.model_dump(exclude_unset=True).items():
            setattr(db_company, key, value)
    db.commit()
    db.refresh(db_company)
    
    return db_company
def delete_company(db: Session, company_id: UUID):
    stmt = select(Company).filter(Company.id == company_id)
    db_company = db.scalars(stmt).first()
    
    if db_company:
        db_company.mode = CompanyMode.INACTIVE
        db.commit()
        db.refresh(db_company)
        
    return db_company