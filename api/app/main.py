"""API de login. Punto de entrada: sin lógica de negocio acá."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.auth import issue_token, verify_credentials

app = FastAPI(title="Login demo")


class LoginRequest(BaseModel):
    email: str
    password: str


@app.post("/login")
def login(body: LoginRequest):
    if not verify_credentials(body.email, body.password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"token": issue_token(body.email)}


@app.get("/health")
def health():
    return {"status": "ok"}
