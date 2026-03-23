from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Task
from pydantic import BaseModel
from typing import List

router = APIRouter()

# -------------------------
# Schemas (Pydantic V2)
# -------------------------
class TaskCreate(BaseModel):
    title: str

class TaskRead(BaseModel):
    id: int
    title: str

    model_config = {
        "from_attributes": True
    }

# -------------------------
# DB Session
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------
# Routes
# -------------------------

@router.get("/tasks", response_model=List[TaskRead])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@router.post("/tasks", response_model=TaskRead)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    # task.title contient maintenant le JSON envoyé par le frontend
    db_task = Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Deleted"}