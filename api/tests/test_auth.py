import os

os.environ.setdefault("JWT_SECRET", "secreto-de-prueba")

from app.auth import decode_token, issue_token, verify_credentials


def test_credenciales_validas_pasan():
    assert verify_credentials("ana@sofka.com.co", "demo1234") is True


def test_credenciales_invalidas_no_pasan():
    assert verify_credentials("ana@sofka.com.co", "otra") is False


def test_usuario_inexistente_no_pasa():
    assert verify_credentials("nadie@sofka.com.co", "demo1234") is False


def test_el_token_lleva_el_email_del_usuario():
    token = issue_token("luis@sofka.com.co")
    assert decode_token(token)["sub"] == "luis@sofka.com.co"
