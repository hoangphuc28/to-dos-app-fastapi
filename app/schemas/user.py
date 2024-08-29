from sqlalchemy import Boolean, Column, ForeignKey, String, Uuid
from schemas.company import Company
from schemas.base_entity import BaseEntity
from shared.db import Base
from sqlalchemy.orm import relationship

class User(Base, BaseEntity):
    __tablename__ = "users"
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    company_id = Column(Uuid, ForeignKey("companies.id"), nullable=False)
    company = relationship("Company")

