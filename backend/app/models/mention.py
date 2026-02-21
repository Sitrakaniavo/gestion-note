from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Mention(Base):
    __tablename__ = "mentions"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    niveau = Column(String, nullable=False)
    domaine_id = Column(Integer, ForeignKey("domaines.id"))

    domaine = relationship("Domaine")