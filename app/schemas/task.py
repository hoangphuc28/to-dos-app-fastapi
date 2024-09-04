from sqlalchemy import Column, Enum, ForeignKey, String, Uuid
from sqlalchemy.orm import relationship
from shared.db import Base
from shared.enum import TaskPriority, TaskStatus
from schemas.base_entity import BaseEntity
class Task(Base, BaseEntity):
    __tablename__ = "tasks"
    summary = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.ACTIVE)
    priority = Column(Enum(TaskPriority), nullable=False, default=TaskPriority.LOW)
    user_id = Column(Uuid, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="tasks")