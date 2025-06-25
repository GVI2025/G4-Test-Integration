from sqlalchemy import Column, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.database.database import Base

class Reservation(Base): 
    __tablename__ = "reservation"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    salle_id = Column(String, ForeignKey("salle.id"), nullable=False)
    date = Column(Date, nullable=False)
    heure = Column(Time, nullable=False)
    utilisateur = Column(String, nullable=False)
    commentaire = Column(String, nullable=True)

    salle = relationship("Salle", foreign_keys=[salle_id])