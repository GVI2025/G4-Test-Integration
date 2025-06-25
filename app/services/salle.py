from sqlalchemy.orm import Session
from app.models import Salle as SalleModel
from app.schemas.salle import SalleCreate, SalleUpdate

def get_salle(db: Session, salle_id: str):
    return db.query(SalleModel).filter(SalleModel.id == salle_id).first()

def get_salle_by_name(db: Session, name: str):
    return db.query(SalleModel).filter(SalleModel.nom == name).first()

def list_salles(db: Session, skip: int = 0, limit: int = 100, disponible: bool = None):
    if disponible is not None:
        return db.query(SalleModel).filter(SalleModel.disponible == disponible).offset(skip).limit(limit).all()
    return db.query(SalleModel).offset(skip).limit(limit).all()

def create_salle(db: Session, salle: SalleCreate):
    db_salle = SalleModel(**salle.dict())
    db.add(db_salle)
    db.commit()
    db.refresh(db_salle)
    return db_salle

def update_salle(db: Session, salle_id: str, salle_data: SalleUpdate):
    db_salle = get_salle(db, salle_id)
    if db_salle:
        for key, value in salle_data.dict().items():
            setattr(db_salle, key, value)
        db.commit()
        db.refresh(db_salle)
    return db_salle

def delete_salle(db: Session, salle_id: str):
    db_salle = get_salle(db, salle_id)
    if db_salle:
        db.delete(db_salle)
        db.commit()
    return db_salle