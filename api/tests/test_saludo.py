import os

os.environ.setdefault("JWT_SECRET", "secreto-de-prueba")

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_el_saludo_devuelve_hola_mundo():
    r = client.get("/saludo")
    assert r.status_code == 200
    assert r.json() == {"mensaje": "hola mundo"}


def test_el_saludo_solo_responde_a_get():
    r = client.post("/saludo")
    assert r.status_code == 405
