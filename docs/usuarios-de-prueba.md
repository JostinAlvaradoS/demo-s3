# Usuarios de prueba

Viven en memoria, en `api/app/users.py`. Se pierden al reiniciar la API.

| Correo | Contraseña | Para qué |
|---|---|---|
| `ana@sofka.com.co` | `demo1234` | Camino feliz |
| `luis@sofka.com.co` | `demo1234` | Segundo usuario, para probar que el token lleva el correo correcto |

Para agregar uno, sumá el par correo → `sha256(contraseña)` en `_USERS`. No metas usuarios de
prueba en el código que se despliega a `prod`.
