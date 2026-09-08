"""Almacén de usuarios en memoria. En producción esto sería una tabla."""

from hashlib import sha256

_USERS = {
    "ana@sofka.com.co": sha256(b"demo1234").hexdigest(),
    "luis@sofka.com.co": sha256(b"demo1234").hexdigest(),
}


def find_password_hash(email):
    return _USERS.get(email)


def exists(email):
    return email in _USERS
