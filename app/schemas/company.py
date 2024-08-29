
from sqlalchemy import Column, Float, String, Enum
from shared.enum import CompanyMode
from schemas.base_entity import BaseEntity
from shared.db import Base
from sqlalchemy.orm import relationship

class Company(Base, BaseEntity):
    __tablename__ = "companies"
    name = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(String(255), nullable=False)
    mode = Column(Enum(CompanyMode), nullable=False, default=CompanyMode.ACTIVE)
    rating = Column(Float, nullable=False)
    users = relationship("User", back_populates="company")
    