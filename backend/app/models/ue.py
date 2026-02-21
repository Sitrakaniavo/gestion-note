from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class UE(Base):
    __tablename__ = "ues"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mention_id = Column(Integer, ForeignKey("mentions.id"))

    mention = relationship("Mention")