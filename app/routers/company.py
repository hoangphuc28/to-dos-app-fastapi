from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.company import CompanyCreate, CompanyUpdate, CompanyView
from schemas.company import Company
from services.company import get_company, get_companies, create_company, update_company, delete_company
from shared.db import get_db_context

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.post("", response_model=CompanyView)
def create_company_endpoint(company: CompanyCreate, db: Session = Depends(get_db_context)):
    return create_company(db=db, company=company)

@router.get("/{company_id}", response_model=CompanyView)
def get_company_endpoint(company_id: int, db: Session = Depends(get_db_context)):
    db_company = get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@router.get("", response_model=list[CompanyView])
def get_companies_endpoint(page: int = 1, limit: int = 10, db: Session = Depends(get_db_context)):
    res = get_companies(db=db, page=page, limit=limit)
    print(res)
    return res

@router.put("/{company_id}", response_model=CompanyView)
def update_company_endpoint(company_id: int, company: CompanyUpdate, db: Session = Depends(get_db_context)):
    db_company = update_company(db=db, company_id=company_id, company_update=company)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@router.delete("/{company_id}", response_model=CompanyView)
def delete_company_endpoint(company_id: int, db: Session = Depends(get_db_context)):
    db_company = delete_company(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company