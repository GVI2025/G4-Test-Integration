from datetime import datetime, timedelta
from app.database.database import SessionLocal
from app.models.salle import Salle
from app.models.reservation import Reservation

def update_room_availability():
    try:
        now = datetime.now()
        current_date = now.date()
        current_time = now.time()

        with SessionLocal() as db:
            rooms = db.query(Salle).all()

            for room in rooms:
                reservations = db.query(Reservation).filter(
                    Reservation.salle_id == room.id,
                    Reservation.date == current_date
                ).all()

                room_occupied = False
                for reservation in reservations:
                    start_time = reservation.heure
                    end_time = (datetime.combine(current_date, start_time) + timedelta(hours=1)).time()

                    if start_time <= current_time < end_time:
                        room_occupied = True
                        break

                room.disponible = not room_occupied

            db.commit()
            print(f"[{now}] Room availability updated.")

    except Exception as e:
        print(f"Error updating room availability: {e}")
