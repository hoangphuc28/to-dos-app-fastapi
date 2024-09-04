from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from shared.auth import get_current_user
from models.company import CompanyCreate, CompanyUpdate, CompanyView, CompaniesResponse
from schemas.company import Company
from services.company import get_company, get_companies, create_company, update_company, delete_company
from shared.db import get_db_context
from uuid import UUID

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.post("", response_model=CompanyView)
def create_company_endpoint(company: CompanyCreate, db: Session = Depends(get_db_context), current_user: dict = Depends(get_current_user)):
    return create_company(db=db, company=company)

@router.get("/{company_id}", response_model=CompanyView)
def get_company_endpoint(company_id: UUID, db: Session = Depends(get_db_context), current_user: dict = Depends(get_current_user)):
    db_company = get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@router.get("/", response_model=CompaniesResponse)
def get_companies_endpoint(page: int = 1, limit: int = 10, db: Session = Depends(get_db_context), current_user: dict = Depends(get_current_user)):
    print(current_user)
    return get_companies(db=db, page=page, limit=limit)

@router.put("/{company_id}", response_model=CompanyView)
def update_company_endpoint(company_id: UUID, company: CompanyUpdate, db: Session = Depends(get_db_context), current_user: dict = Depends(get_current_user)):
    db_company = update_company(db=db, company_id=company_id, company_update=company)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@router.delete("/{company_id}", response_model=CompanyView)
def delete_company_endpoint(company_id: UUID, db: Session = Depends(get_db_context), current_user: dict = Depends(get_current_user)):
    db_company = delete_company(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company