from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    note = Column(Float, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"))
    ec_id = Column(Integer, ForeignKey("ecs.id"))

    student = relationship("Student")
    ec = relationship("EC")