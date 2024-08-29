from sqlalchemy import Column, Uuid, Time, func
import enum
import uuid

class BaseEntity:
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    created_at = Column(Time, server_default=func.now(), nullable=False)
    updated_at = Column(Time, onupdate=func.now(), nullable=False)
