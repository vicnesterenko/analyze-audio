from sqlalchemy.orm import Session
import models
import schemas
import auth
import json


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_task(db: Session, task_id: int, user_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id,
                                        models.Task.owner_id == user_id).first()


def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    task_data = task.dict()
    if task.prompts:
        task_data["prompts"] = json.dumps(task.prompts)
    db_task = models.Task(**task_data, owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task: models.Task, task_update: schemas.TaskUpdate):
    update_data = task_update.dict(exclude_unset=True)
    if "prompts" in update_data and update_data["prompts"] is not None:
        update_data["prompts"] = json.dumps(update_data["prompts"])
    for key, value in update_data.items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: models.Task):
    db.delete(task)
    db.commit()
