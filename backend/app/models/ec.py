from sqlalchemy import Column, Integer, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class EC(Base):
    __tablename__ = "ecs"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    coefficient = Column(Integer, nullable=False)
    ue_id = Column(Integer, ForeignKey("ues.id"))

    ue = relationship("UE")