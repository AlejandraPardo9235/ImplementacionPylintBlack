from pydantic import BaseModel
from database import database

class Department(BaseModel):
    id: int
    name: str
    location: str
    
