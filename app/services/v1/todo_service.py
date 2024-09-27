from sqlalchemy.orm import Session
from app.models import models
from app.schemas import schemas

def create_todo(db: Session, todo: schemas.ToDoCreate):
    db_todo = models.ToDo(title=todo.title, is_done=todo.is_done, starred=todo.starred)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()

def get_all_todos(db: Session):
    return db.query(models.ToDo).all()

def update_todo(db: Session, todo_id: int, todo_update: schemas.ToDoCreate):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo is None:
        return None
    db_todo.title = todo_update.title
    db_todo.is_done = todo_update.is_done
    db_todo.starred = todo_update.starred
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo is None:
        return None
    db.delete(db_todo)
    db.commit()
    return db_todo
