from fastapi.testclient import TestClient
from unittest.mock import patch, ANY
from datetime import datetime

from app.main import app
from app.schemas.salle import SalleCreate, SalleUpdate
from app.models import Salle as SalleModel

client = TestClient(app)

mock_salle_data = {
    "id": "test_id",
    "nom": "Test Salle",
    "capacité": 200,
    "localisation": "Test Localisation",
    "disponible": True,
}

mock_salle_create = SalleCreate(
    nom="Test Salle",
    capacité=100,
    localisation="Test Localisation",
    disponible=True,
)

mock_salle_client = SalleModel(
    id="test_id",
    nom="Test Salle",
    capacité=100,
    localisation="Test Localisation",
    disponible=True,
)

mock_salle_update = SalleUpdate(
    nom="Updated Salle",
    capacité=150,
    localisation="Updated Localisation",
    disponible=False,
)

class TestSalleRouter:
    @patch("app.services.salle.list_salles")
    def test_list_salle(self, mock_get_all_salles):
        mock_get_all_salles.return_value = [mock_salle_data]
        response = client.get("/salles/")
        assert response.status_code == 200
        assert response.json() == [mock_salle_data]

    @patch("app.services.salle.get_salle")
    def test_get_salle(self, mock_get_salle_by_id):
        mock_get_salle_by_id.return_value = mock_salle_data
        response = client.get("/salles/test_id")
        assert response.status_code == 200
        assert response.json() == mock_salle_data

    @patch("app.services.salle.get_salle_by_name")
    def test_get_salle_by_name(self, mock_get_salle_by_name):
        mock_get_salle_by_name.return_value = mock_salle_data
        response = client.get("/salles/name/Test%20Salle")
        assert response.status_code == 200
        assert response.json() == mock_salle_data

    @patch("app.services.salle.create_salle")
    def test_create_salle(self, mock_create_salle):
        mock_create_salle.return_value = mock_salle_data
        response = client.post("/salles/", json=mock_salle_create.model_dump())
        assert response.status_code == 200
        assert response.json() == mock_salle_data

    @patch("app.services.salle.update_salle")
    def test_update_salle(self, mock_update_salle):
        updated_salle = mock_salle_client
        updated_salle.nom = mock_salle_update.nom
        updated_salle.capacité = mock_salle_update.capacité
        updated_salle.localisation = mock_salle_update.localisation
        updated_salle.disponible = mock_salle_update.disponible
        
        mock_update_salle.return_value = updated_salle

        # Test the update endpoint
        response = client.put(
            "/salles/test_id", 
            json={
                "nom": "updated salle",
                "capacité": 150,
                "localisation": "updated localisation",
                "disponible": False
            }
        )

        assert response.status_code == 200
        assert response.json()["nom"] == mock_salle_update.nom
        assert response.json()["capacité"] == mock_salle_update.capacité
        assert response.json()["localisation"] == mock_salle_update.localisation

    @patch("app.services.salle.delete_salle")
    def test_delete_salle(self, mock_delete_salle):
        mock_delete_salle.return_value = mock_salle_data
        response = client.delete("/salles/test_id")
        assert response.status_code == 200