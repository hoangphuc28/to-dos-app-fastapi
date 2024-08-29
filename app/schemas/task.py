from sqlalchemy import Column, ForeignKey, String, Uuid
from sqlalchemy.orm import relationship
from app.shared.db import Base
from app.shared.enum import TaskPriority, TaskStatus
from schemas.base_entity import BaseEntity
import enum
class Task(Base, BaseEntity):
    __tablename__ = "tasks"
    summary = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    status = Column(enum.Enum(TaskStatus), nullable=False, default=TaskStatus.ACTIVE)
    priority = Column(enum.Enum(TaskPriority), nullable=False, default=TaskPriority.LOW)
    user_id = Column(Uuid, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="tasks")