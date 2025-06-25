from sqlalchemy import Column, String, Integer, Boolean
from uuid import uuid4

from app.database.database import Base
from datetime import datetime
from app.models.reservation import Reservation

class Salle(Base):
    __tablename__ = "salle"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    nom = Column(String, unique=True, nullable=False)
    capacité = Column(Integer, nullable=False)
    localisation = Column(String, nullable=False)
    disponible = Column(Boolean, nullable=False)
