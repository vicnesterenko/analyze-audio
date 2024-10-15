from pydantic import BaseModel
from typing import List, Optional


class TaskBase(BaseModel):
    name: str
    audio_link: Optional[str] = None
    prompts: Optional[List[str]] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    username: str
    password: str
