from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    matricule: str
    fullname: str
    mention_id: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    fullname: Optional[str] = None
    mention_id: Optional[int] = None

class StudentOut(StudentBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True