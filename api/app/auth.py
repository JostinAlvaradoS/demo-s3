"""Verificación de credenciales y emisión de tokens."""

import os
from datetime import datetime, timedelta, timezone
from hashlib import sha256

import jwt

from app.users import find_password_hash

SECRET = os.environ["JWT_SECRET"]
TOKEN_TTL_MINUTES = 30


def verify_credentials(email, password):
    stored = find_password_hash(email)
    if stored is None:
        return False
    return stored == sha256(password.encode()).hexdigest()


def issue_token(email):
    expires = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_TTL_MINUTES)
    return jwt.encode({"sub": email, "exp": expires}, SECRET, algorithm="HS256")


def decode_token(token):
    return jwt.decode(token, SECRET, algorithms=["HS256"])
