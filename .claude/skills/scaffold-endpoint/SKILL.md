---
name: scaffold-endpoint
description: >
  Agrega un endpoint nuevo a la API de FastAPI siguiendo las convenciones ya establecidas en el
  repo. Usar cuando se pida crear, agregar o andamiar un endpoint, una ruta, un handler o un
  recurso nuevo en `api/`. No usar para modificar endpoints existentes.
context: fork
allowed-tools: [Read, Glob, Grep, Write]
argument-hint: "<nombre-del-endpoint>"
---

# Andamiar un endpoint

Endpoint a crear: `$ARGUMENTS`

Esta skill define el **procedimiento**, no las convenciones. Las convenciones del stack las manda
`api/CLAUDE.md` y las de testing `.claude/rules/tests.md`: se cargan solas al tocar esos archivos y
no se repiten acá. Si hay que cambiar una convención, se cambia allá y esta skill la sigue sin
tocarse.

## 1. Explorar antes de escribir

En este orden, y sin saltarse pasos:

1. `api/CLAUDE.md` — las convenciones del stack. Manda ese archivo, no tu criterio.
2. `api/app/main.py` — el estilo de declaración de rutas y cómo se propagan los errores.
3. `api/app/auth.py` — cómo se estructura un módulo de lógica y qué expone.
4. Grep de `HTTPException` — los códigos y los mensajes que ya se usan, para no inventar otros.
5. Un test existente de `api/tests/` — el estilo de armado y de aserción.

## 2. Producir

- `api/app/<nombre>.py` con la lógica del endpoint.
- `api/tests/test_<nombre>.py` cubriendo, como mínimo, el camino feliz y un camino de error.
- El registro de la ruta en `api/app/main.py`.

## 3. Reportar

Solo los archivos creados o modificados, una línea por archivo diciendo qué quedó en cada uno.
No pegues el contenido: quien te invocó ya puede leerlo.
