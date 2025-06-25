
from app.database.database import SessionLocal
from app.models.reservation import Reservation
from app.models.salle import Salle

from datetime import date, time
from sqlalchemy.exc import IntegrityError

def seed():
    db = SessionLocal()
    try:
        # Nettoyage de la base (dans l'ordre inverse des dépendances)
        db.query(Salle).delete()
        db.query(Reservation).delete()
        db.commit()

        # === SALLES ===
        salles = [
            Salle(id="salle1", nom="Salle A", capacité=10, localisation="1er étage", disponible=True),
            Salle(id="salle2", nom="Salle B", capacité=20, localisation="2ème étage", disponible=True),
            Salle(id="salle3", nom="Salle C", capacité=30, localisation="3ème étage", disponible=True),
            Salle(id="salle4", nom="Salle D", capacité=15,  localisation="1er étage", disponible=True),
        ]

        # === RESERVATIONS ===
        reservations = [
            Reservation(id="reservation1", salle_id="salle1", date=date(2023, 10, 1), heure=time(12, 12), utilisateur="utilisateur1", commentaire="Ceci est un commentaire"),
            Reservation(id="reservation2", salle_id="salle2", date=date(2023, 10, 2), heure=time(22, 30), utilisateur="utilisateur2", commentaire="Ceci est un commentaire"),
            Reservation(id="reservation3", salle_id="salle2", date=date(2023, 10, 3), heure=time(14, 0), utilisateur="utilisateur1", commentaire=""),
        ]

        # Ajout global
        db.add_all(salles + reservations)
        db.commit()
        print("Données de test insérées avec succès.")

    except IntegrityError as e:
        db.rollback()
        print("Erreur d'intégrité :", e)
    finally:
        db.close()

if __name__ == "__main__":
    seed()