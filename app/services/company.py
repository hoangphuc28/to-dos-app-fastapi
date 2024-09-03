from sqlalchemy.orm import Session
from schemas.company import Company
from models.company import CompanyCreate, CompanyUpdate

def get_company(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()

def get_companies(db: Session, page: int = 1, limit: int = 10):
    if page < 1:
        page = 1
    skip = (page - 1) * limit
    return db.query(Company).offset(skip).limit(limit).all()

def create_company(db: Session, company: CompanyCreate):
    db_company = Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def update_company(db: Session, company_id: int, company_update: CompanyUpdate):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company:
        for key, value in company_update.dict(exclude_unset=True).items():
            setattr(db_company, key, value)
        db.commit()
        db.refresh(db_company)
    return db_company

def delete_company(db: Session, company_id: int):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company:
        db.delete(db_company)
        db.commit()
    return db_company