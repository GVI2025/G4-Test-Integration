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
    "capacite": 100,
    "localisation": "Test Localisation",
}

mock_salle_create = SalleCreate(
    nom="Test Salle",
    capacite=100,
    localisation="Test Localisation",
)

mock_salle_update = SalleUpdate(
    nom="Updated Salle",
    capacite=150,
    localisation="Updated Localisation",
)

class TestSalleRouter:
    @patch("app.services.salle.get_all_salles")
    def test_list_salle(self, mock_get_all_salles):
        mock_get_all_salles.return_value = [mock_salle_data]
        response = client.get("/salles/")
        assert response.status_code == 200
        assert response.json() == [mock_salle_data]