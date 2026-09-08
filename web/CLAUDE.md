# web — TypeScript + Vite

- `strict` está activo y no se negocia. Nada de `any`: si el tipo no se sabe, es `unknown`.
- **Todo `fetch` sale por `src/api.ts`.** Ningún otro módulo llama a la red directo.
- El token va en `sessionStorage`, nunca en `localStorage` ni en una cookie sin `HttpOnly`.
- Tests con **vitest**, en archivos `*.test.ts` junto al código que prueban.
- Los mensajes de error que ve el usuario van en español y no filtran detalle del backend.
