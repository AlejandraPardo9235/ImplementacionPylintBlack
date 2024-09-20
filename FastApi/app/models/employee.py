from pydantic import BaseModel
from database import database

class Employee(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    department_id: int

    class Config:
        orm_mode = True
