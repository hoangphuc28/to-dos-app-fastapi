from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from models.pagination import Pagination
from shared.enum import CompanyMode
from uuid import UUID

class CompanyCreate(BaseModel):
    name: str
    description: str
    mode: CompanyMode
    rating: float

class CompanyUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    rating: Optional[float]

class CompanyView(BaseModel):
    id: UUID
    name: str
    description: str
    # mode: CompanyMode
    rating: float
    model_config = ConfigDict(from_attributes=True)

class CompaniesResponse(BaseModel, Pagination):
    items: List[CompanyView]
