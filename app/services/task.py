from sqlalchemy import select, func
from sqlalchemy.orm import Session
from uuid import UUID
from fastapi import HTTPException
from models.task import TaskCreate, TaskUpdate, TaskView, TasksResponse
from schemas.task import Task
from shared.enum import TaskStatus

def create_task(db: Session, task: TaskCreate) -> Task:
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, page: int = 1, limit: int = 10) -> TasksResponse:
    if page < 1:
        page = 1
    skip = (page - 1) * limit

    # Get total number of active tasks
    total_items = db.scalar(select(func.count(Task.id)).filter(Task.status == TaskStatus.ACTIVE))
    total_pages = (total_items + limit - 1) // limit  # Ceiling division for total pages

    # Fetch the paginated active tasks
    stmt = select(Task).filter(Task.status == TaskStatus.ACTIVE).offset(skip).limit(limit)
    tasks = db.scalars(stmt).all()

    # Create the response
    response = TasksResponse(
        items=tasks,
        limit=limit,
        currentPage=page,
        totalPages=total_pages,
        totalItems=total_items
    )
    
    return response

def get_task(db: Session, task_id: UUID) -> Task:
    stmt = select(Task).filter_by(id=task_id, status=TaskStatus.ACTIVE)
    task_detail = db.scalars(stmt).first()
    if task_detail is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_detail
def get_tasks(db: Session, page: int = 1, limit: int = 10, user_id: UUID = None):
    if page < 1:
        page = 1
    skip = (page - 1) * limit
    
    total_items = db.scalar(select(func.count(Task.id)).filter(Task.status == TaskStatus.INACTIVE, Task.user_id == user_id))
    total_pages = (total_items + limit - 1) // limit  # Ceiling division for total pages
    print(user_id)
    stmt = select(Task).filter(Task.status != TaskStatus.INACTIVE, Task.user_id == user_id).offset(skip).limit(limit)
    items = db.scalars(stmt).all()
    # Create the response
    response = {
        "items": items,
        "limit": limit,
        "currentPage": page,
        "totalPages": total_pages,
        "totalItems": total_items
    }
    
    return response

def update_task(db: Session, task_id: UUID, task_update: TaskUpdate) -> Task:
    stmt = select(Task).filter_by(id=task_id, status=TaskStatus.ACTIVE)
    db_task = db.scalars(stmt).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task_update.model_dump(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: UUID) -> Task:
    stmt = select(Task).filter_by(id=task_id)
    db_task = db.scalars(stmt).first()
    if db_task:
        db_task.status = TaskStatus.INACTIVE
        db.commit()
        db.refresh(db_task)
    return db_task
