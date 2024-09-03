from sqlalchemy import Uuid
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
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
    mode: Optional[CompanyMode]
    rating: Optional[float]

class CompanyView(BaseModel):
    id: UUID
    name: str
    description: str
    mode: CompanyMode
    rating: float
    model_config = ConfigDict(from_attributes=True)