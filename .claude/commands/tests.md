---
description: Corre los tests del stack que se indique y resume solo lo que falló
argument-hint: "[web|api|todo]"
allowed-tools: Bash(npm test*), Bash(uv run pytest*), Read
---

Corré los tests de: $ARGUMENTS

- `web` → `cd web && npm test`
- `api` → `cd api && uv run pytest`
- `todo` → los dos, en ese orden

Si el argumento viene vacío, corré `todo`.

No me listes los que pasaron. Por cada fallo: `archivo:línea`, qué esperaba, qué obtuvo, y la
causa probable en una línea. Si todo pasa, respondé solo con el conteo.
