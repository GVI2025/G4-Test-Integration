from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.reservation import ReservationRead, ReservationCreate, ReservationUpdate
from app.services import reservation as reservation_service
from app.database.database import get_db

router = APIRouter(prefix="/reservations", tags=["Réservations"])

@router.get('/', response_model=List[ReservationRead])
def list_reservations(db: Session = Depends(get_db)):
    return reservation_service.get_reservation(db)

@router.post('/', response_model=ReservationRead)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    return reservation_service.create_reservation(db, reservation)

@router.get('/{reservation_salle}', response_model=List[ReservationRead])
def get_reservations_by_salle(reservation_salle: str, db: Session = Depends(get_db)):
    reservations = reservation_service.get_reservations_by_salle(db, reservation_salle)
    if not reservations:
        raise HTTPException(status_code=404, detail="No reservations found for this salle")
    return reservations

@router.get('/date/{reservation_date}', response_model=List[ReservationRead])
def get_reservations_by_date(reservation_date: str, db: Session = Depends(get_db)):
    reservations = reservation_service.get_reservations_by_date(db, reservation_date)
    if not reservations:
        raise HTTPException(status_code=404, detail="No reservations found for this date")
    return reservations

@router.get('/time/{reservation_time}', response_model=List[ReservationRead])
def get_reservation_by_time(reservation_time: str, db: Session = Depends(get_db)):
    reservations = reservation_service.get_reservation_by_time(db, reservation_time)
    if not reservations:
        raise HTTPException(status_code=404, detail="No reservations found for this time")
    return reservations

@router.get('/user/{utilisateur}', response_model=List[ReservationRead])
def get_reservations_by_user(utilisateur: str, db: Session = Depends(get_db)):
    reservations = reservation_service.get_reservations_by_user(db, utilisateur)
    if not reservations:
        raise HTTPException(status_code=404, detail="No reservations found for this user")
    return reservations

@router.delete('/{reservation_id}', response_model=ReservationRead)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = reservation_service.get_reservation_by_id(db, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation_service.delete_reservation(db, reservation_id)
