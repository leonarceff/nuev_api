import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_and_login():
    # Registro
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "testpass"})
    assert response.status_code in (200, 400)  # Puede ser 400 si ya existe
    # Login válido
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "testpass"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    # Login inválido
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "wrongpass"})
    assert response.status_code == 401

def test_protected_route():
    # Login para obtener token
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "testpass"})
    token = response.json().get("access_token")
    # Acceso a ruta protegida (ejemplo: crear municipio)
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/municipios/", json={"nombre": "Test Municipio", "descripcion": "desc"}, headers=headers)
    assert response.status_code in (200, 401, 403)
    # Acceso sin token
    response = client.post("/municipios/", json={"nombre": "Test Municipio 2", "descripcion": "desc"})
    assert response.status_code in (401, 403)
