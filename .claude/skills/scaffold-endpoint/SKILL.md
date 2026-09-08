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

## Antes de escribir una sola línea, explorá

1. Leé `api/CLAUDE.md`: las convenciones del stack manda ese archivo, no tu criterio.
2. Leé `api/app/main.py` para copiar el estilo de declaración de rutas y el manejo de errores.
3. Leé `api/app/auth.py` para ver cómo se estructura la lógica que vive fuera del punto de entrada.
4. Buscá con Grep los usos de `HTTPException` para replicar los códigos y los mensajes.
5. Leé `api/tests/test_auth.py` para copiar el estilo de los tests y la convención de nombres.

## Después escribí

- `api/app/<nombre>.py` con la lógica. Nada de lógica en `main.py`.
- `api/tests/test_<nombre>.py` con al menos un caso feliz y un caso de error.
- El registro de la ruta en `api/app/main.py`, en el mismo estilo que las existentes.

## Reportá

Solo los archivos creados o modificados, una línea por archivo diciendo qué quedó en cada uno.
No pegues el contenido: quien te invocó ya puede leerlo.
