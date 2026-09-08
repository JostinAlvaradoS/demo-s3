import os

os.environ.setdefault("JWT_SECRET", "secreto-de-prueba")

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_correcto_devuelve_token():
    r = client.post("/login", json={"email": "ana@sofka.com.co", "password": "demo1234"})
    assert r.status_code == 200
    assert r.json()["token"]


def test_login_incorrecto_devuelve_401():
    r = client.post("/login", json={"email": "ana@sofka.com.co", "password": "mala"})
    assert r.status_code == 401
