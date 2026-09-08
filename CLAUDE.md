# Login demo — monorepo

- Tres piezas independientes: `web/` (TypeScript), `api/` (Python), `infra/` (Terraform).
  Cada una tiene su propio `CLAUDE.md` con sus convenciones.
- Ningún módulo cruza fronteras: el front habla con la API por HTTP, nada más.
- Los mensajes de commit van en imperativo y en español.

Credenciales de prueba, mantenidas en un solo lugar:

@docs/usuarios-de-prueba.md
