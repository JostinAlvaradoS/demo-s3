# api — Python + FastAPI

- Se corre con `uv run uvicorn app.main:app --reload`. Dependencias en `pyproject.toml`.
- `app/main.py` es punto de entrada: sin lógica de negocio. La verificación va en `app/auth.py`.
- Tests con **pytest**, en `tests/`. Nombres `test_<comportamiento>`.
- `JWT_SECRET` se lee de entorno. Nunca hardcodearlo, nunca loggearlo, nunca devolverlo en una
  respuesta.
- Un login fallido responde 401 sin decir si el que falló fue el correo o la contraseña.
