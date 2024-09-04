from pydantic import BaseModel
from uuid import UUID
from enum import Enum
from models.pagination import Pagination
from shared.enum import TaskPriority, TaskStatus
class TaskCreate(BaseModel):
    summary: str
    description: str
    status: TaskStatus = TaskStatus.ACTIVE
    priority: TaskPriority = TaskPriority.LOW
    user_id: UUID

class TaskUpdate(BaseModel):
    summary: str = None
    description: str = None
    status: TaskStatus = None
    priority: TaskPriority = None

class TaskView(BaseModel):
    id: UUID
    summary: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    user_id: UUID

    class Config:
        orm_mode = True
class TasksResponse(BaseModel, Pagination):
    items: list[TaskView]
