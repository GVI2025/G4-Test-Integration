from datetime import date, time
from sqlalchemy.orm import Session
from app.models import Reservation as ReservationModel

def create_reservation(db: Session, reservation: ReservationModel):
    db_reservation = ReservationModel(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def get_reservation(db: Session):
    return db.query(ReservationModel).all()

def get_reservations_by_salle(db: Session, salle_id: str):
    return db.query(ReservationModel).filter(ReservationModel.salle_id == salle_id).all()

def get_reservations_by_date(db: Session, date: date):
    return db.query(ReservationModel).filter(ReservationModel.date == date).all()

def get_reservation_by_time(db: Session, time: time):
    return db.query(ReservationModel).filter(ReservationModel.heure == time).all()

def get_reservations_by_user(db: Session, utilisateur: str):
    return db.query(ReservationModel).filter(ReservationModel.utilisateur == utilisateur).all()

def get_reservation_by_id(db: Session, reservation_id: int):
    return db.query(ReservationModel).filter(ReservationModel.id == reservation_id).first()

def delete_reservation(db: Session, reservation_id: int):
    reservation = get_reservation_by_id(db, reservation_id)
    if reservation:
        db.delete(reservation)
        db.commit()
        return reservation
    return None

