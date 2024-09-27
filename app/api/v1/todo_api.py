from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import schemas as schemas
from app.config.database import get_db
from app.services.v1 import todo_service

router = APIRouter(
    prefix="/todos",
    tags=['todo']
)


@router.post("/create/", response_model=schemas.ToDoResponse)
def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    return todo_service.create_todo(db=db, todo=todo)

# Get a single ToDo item by ID
@router.get("/get/{todo_id}", response_model=schemas.ToDoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = todo_service.get_todo_by_id(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    return db_todo

# Get all ToDo items
@router.get("/get/all/", response_model=list[schemas.ToDoResponse])
def get_all_todos(db: Session = Depends(get_db)):
    return todo_service.get_all_todos(db=db)

# Update a ToDo item
@router.put("/update/{todo_id}", response_model=schemas.ToDoResponse)
def update_todo(todo_id: int, todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    db_todo = todo_service.update_todo(db=db, todo_id=todo_id, todo_update=todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    return db_todo

# Delete a ToDo item
@router.delete("/remove/{todo_id}", response_model=schemas.ToDoResponse)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = todo_service.delete_todo(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    return db_todo