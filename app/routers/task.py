from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from shared.auth import get_current_user
from models.task import TaskCreate, TaskUpdate, TaskView, TasksResponse
from services.task import create_task, get_task, get_tasks, update_task, delete_task
from shared.db import get_db_context

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("", response_model=TaskView)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db_context), current_user: dict = Depends(get_current_user)):
    return create_task(db, task)

@router.get("/{task_id}", response_model=TaskView)
def get_task_endpoint(task_id: UUID, db: Session = Depends(get_db_context), current_user: dict = Depends(get_current_user)):
    return get_task(db, task_id)
@router.get("/", response_model=TasksResponse)
def get_tasks_endpoint(page: int = 1, limit: int = 10, user_id: UUID = None, db: Session = Depends(get_db_context), current_user: dict = Depends(get_current_user)):
    return get_tasks(db, page=page, limit=limit, user_id=user_id)

@router.put("/{task_id}", response_model=TaskView)
def update_task_endpoint(task_id: UUID, task_update: TaskUpdate, db: Session = Depends(get_db_context), current_user: dict = Depends(get_current_user)):
    return update_task(db, task_id, task_update)

@router.delete("/{task_id}", response_model=TaskView)
def delete_task_endpoint(task_id: UUID, db: Session = Depends(get_db_context), current_user: dict = Depends(get_current_user)):
    return delete_task(db, task_id)
