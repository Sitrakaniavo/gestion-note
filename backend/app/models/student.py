from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    matricule = Column(String, unique=True, nullable=False)
    fullname = Column(String, nullable=False)
    mention_id = Column(Integer, ForeignKey("mentions.id"))
    is_active = Column(Boolean, default=True)

    mention = relationship("Mention")